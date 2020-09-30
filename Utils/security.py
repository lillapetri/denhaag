from datetime import datetime, timedelta
from time import time

import jwt
from Models.user import UserIn, UserInDB, UserOut
from Utils.constants import JWT_ALGORITHM, JWT_EXPIRATION_TIME_MINUTES, JWT_SECRET_KEY
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])
oauth_schema = OAuth2PasswordBearer(tokenUrl='/token')

new_user = {
    "username": "test",
    "password": "$2b$12$AsLfTlUy/bzFt2cEanE76uF58mkt.Y6P5UTK3NCoLxY3xtRaFclZO",
    "role": "Admin",
    "is_active": True,
    "created_at": datetime.utcnow()
}

fake_user = UserIn(**new_user)


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        raise e


# Authenticate and give JWT token
def authenticate(username: str, password: str):
    if fake_user.username == username:
        if verify_password(password, fake_user.password):
            return fake_user
    return None


# Create access JWT token
def create_jwt_token(user: UserOut):
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub": user.username, "exp": expiration, "role": user.role}
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM).decode('utf-8')

    return {"access_token": "Bearer " + jwt_token}


# Check whether JWT token is correct
def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get('sub')
        expiration = jwt_payload.get('exp')
        role = jwt_payload.get('role')
        if fake_user.username == username and time() < expiration:
            return final_checks(role)
    except Exception as e:
        return False
    return False


# Last authorization checking and returning the final result
def final_checks(role: str):
    try:
        if role == 'Admin':
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


user1 = {"username": "test", "password": "pass1", "role": "Admin"}
print(check_jwt_token(
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjoxNjAxODEyMjUwfQ.LFcwz_Js13uVprXjDkosdzVst2tJFJUtTBTI6FmXEr8"))
