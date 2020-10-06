import pickle
from datetime import datetime
from uuid import uuid4

import Utils.redis_object as re
import aioredis
from API.v1 import app_v1
from Models.user import UserIn
from Utils.constants import REDIS_URL, TESTING
from Utils.db_functions import db_insert_user
from Utils.db_object import db
from Utils.redis_object import check_test_redis
from Utils.security import authenticate, check_jwt_token, create_jwt_token, get_hashed_password
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

app = FastAPI(title="What to do in the Hague?", description="Freetime activities collected in and around the Hague",
              version='1.0.0')
app.include_router(app_v1, prefix='/v1', dependencies=[Depends(check_test_redis)])


@app.on_event('startup')
async def connect_db():
    if not TESTING:
        await db.connect()
        print('DB connected.')
        re.redis = await aioredis.create_redis_pool(REDIS_URL)
        print('Redis connected')


@app.on_event('shutdown')
async def disconnect_db():
    if not TESTING:
        await db.disconnect()
        re.redis.close()
        await re.redis.wait_closed()


# Test API route
@app.get('/', tags=['Test connection'])
async def test_connection():
    return {'Connection established.'}


# Create admin
@app.post('/user', tags=['Create user or admin.'], status_code=HTTP_201_CREATED)
async def create_new_user(user: UserIn):
    username = user.username
    password = user.password
    role = user.role
    user_in_db = {'username': username, 'hashed_password': get_hashed_password(password), 'is_active': True,
                  'created_at': datetime.utcnow(), 'id': uuid4(), 'role': role}
    try:
        new_user = await db_insert_user(user_in_db)
        print(new_user)
        if new_user is not None:
            return {'response': f"{new_user} {user_in_db['role']} is created"}
    except Exception as e:
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)


# Get token
@app.post('/login', description='Returns JWT token.', tags=['Get access token'])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Todo: refactor login
    username = form_data.username
    password = form_data.password

    redis_key = f'token:{username}, {password}'
    cached_user = await re.redis.get(redis_key)

    if not cached_user:
        user_in = {'username': username, 'password': password}
        user_dict = UserIn(**user_in)
        authenticated_user = await authenticate(user_dict)
        if authenticated_user is None:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
        else:
            token = create_jwt_token(authenticated_user)
            await re.redis.set(redis_key, pickle.dumps(authenticated_user), expire=5 * 60)
            return token
    else:
        return create_jwt_token(pickle.loads(cached_user))


@app.middleware('http')
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    print(request.method)
    if request.method != 'GET' and not str(request.url).__contains__('login'):
        try:
            jwt_token = request.headers['Authorization'].split('Bearer ')[1]
            is_valid = await check_jwt_token(jwt_token)
        except Exception as e:
            is_valid = False
        if not is_valid:
            return Response('Unauthorized', status_code=HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    execution_time = (datetime.utcnow() - start_time).microseconds
    response.headers['x-execution-time'] = str(execution_time)
    return response
