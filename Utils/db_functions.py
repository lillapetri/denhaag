from Utils.db import execute, fetch
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def db_fetch_category(category):
    query = f'select * from {category}'
    result = await fetch(query, False)
    return result


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
    query = '''select * from users where username = :username'''
    values = {'username': username}
    result = await fetch(query, True, values)
    if result is None:
        return False
    else:
        return True


async def db_insert_user(user):
    query = '''insert into users values(:username, :hashed_password, :is_active, :created_at, :id, :role) returning 
    username '''
    values = dict(user)
    result = await execute(query, False, values)
    return result


async def db_insert_food(food):
    query = '''insert into food values(:name, :address, :cuisine, :votes, :description, :url, :created_at, :covid_factor, 
    :district, :id, :price_category, :services) returning name '''
    values = dict(food)
    result = await execute(query, False, values)
    return result


async def db_insert_learning(learning):
    query = '''insert into learning values(:name, :language, :price_category, :subject, :platform, :votes, 
    :description, :covid_factor, :url, :created_at, :id) returning name '''
    values = dict(learning)
    result = await execute(query, False, values)
    return result


async def db_insert_sport(sport):
    query = '''insert into sport values(:name, :type, :price_category, :environment, :district, :address, :votes, 
    :description, :covid_factor, :url, :created_at, :id) returning name '''
    values = dict(sport)
    result = await execute(query, False, values)
    return result


async def db_insert_travel(travel):
    query = '''insert into travel values(:name, :distance_in_km, :votes, :programs, :description, :covid_factor, 
    :url, :created_at, :id) returning name '''
    values = dict(travel)
    result = await execute(query, False, values)
    return result


async def db_insert_friends(friends):
    query = '''insert into friends values(:name, :platform, :votes, :description, :covid_factor, :url, :created_at, :id) 
    returning name '''
    values = dict(friends)
    result = await execute(query, False, values)
    return result


async def db_insert_art(art):
    query = '''insert into art values(:name, :price_category, :type, :district, :address, :votes, 
    :description, :covid_factor, :url, :created_at, :id) returning name '''
    values = dict(art)
    result = await execute(query, False, values)
    return result


async def db_insert_party(party):
    query = '''insert into party values(:name, :date, :time, :ticket_price_in_euro, :tags, :district, :address, :votes, 
    :description, :covid_factor, :url, :created_at, :id) returning name '''
    values = dict(party)
    result = await execute(query, False, values)
    return result
