from datetime import datetime, timedelta
from time import time

import jwt
from Models.user import UserIn, UserInDB, UserOut
from Utils.constants import JWT_ALGORITHM, JWT_EXPIRATION_TIME_MINUTES, JWT_SECRET_KEY
from Utils.db_functions import db_check_user, db_check_username
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])
oauth_schema = OAuth2PasswordBearer(tokenUrl='/token')


def get_hashed_password(password):
    return pwd_context.hash(password)


# Authenticate and give JWT token
async def authenticate(user):
    is_valid = await db_check_user(user)
    if is_valid:
        return user
    return None


# Create access JWT token
def create_jwt_token(user: UserOut):
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub": user.username, "exp": expiration, "role": user.role}
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM).decode('utf-8')

    return {"access_token": "Bearer " + jwt_token}


# Check whether JWT token is correct
async def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get('sub')
        expiration = jwt_payload.get('exp')
        role = jwt_payload.get('role')
        if time() < expiration:
            is_valid = await db_check_username(username)
            if is_valid:
                return final_checks(role)
    except Exception as e:
        print(e)
        return False
    return False


# Last authorization checking and returning the final result
def final_checks(role: str):
    try:
        if role.lower() == 'admin':
            return True
    except Exception as e:
        return False
    return False


def save_user(user_in: UserIn):
    hashed_password = get_hashed_password(user_in.password)
    saved_user = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print(saved_user)
    return saved_user

