from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    admin: str = "admin"
    user: str = "user"


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
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
    role: UserRole
