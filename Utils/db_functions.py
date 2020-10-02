from Utils.db import execute, fetch
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def db_check_user(user):
    query = """select hashed_password from users where username = :username"""
    values = {'username': user.username}
    response = await fetch(query, True, values)
    if response is not None:
        result = verify_password(user.password, response['hashed_password'])
        if result is True:
            return True
    else:
        return False


async def db_check_username(username):
    query = """select * from users where username = :username"""
    values = {'username': username}
    result = await fetch(query, True, values)
    if result is None:
        return False
    else:
        return True


async def db_insert_user(user):
    query = "insert into users values(:username, :hashed_password, :is_active, :created_at, :id, :role) returning username"
    values = dict(user)
    result = await execute(query, False, values)
    return result
