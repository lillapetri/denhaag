from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    admin: str = "Admin"
    user: str = "User"


class UserIn(BaseModel):
    username: str
    password: str
    role: UserRole = 'admin'
    is_active: bool = True
    created_at: datetime = datetime.now()


class UserOut(BaseModel):
    username: str
    role: UserRole


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    role: UserRole
    is_active: bool = True
    created_at: datetime

# user = {"username": "test", "password": "pass1", "role": "Admin"}
# user_object = UserIn(**user)
