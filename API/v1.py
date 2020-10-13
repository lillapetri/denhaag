import pickle
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, Header
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

import Utils.db_functions as db
import Utils.redis_object as re
from Models.art import Art
from Models.category import Category
from Models.food import Food
from Models.friends import Friends
from Models.learning import Learning
from Models.party import Party
from Models.sport import Sport
from Models.travel import Travel

app_v1 = APIRouter()


# Get filtered category
@app_v1.get('/{category}/{column}={value}')
async def get_filtered_category(category: Category, column, value):
    try:
        filtered_category = await db.fetch_filtered_category(category, column, value)
        return filtered_category
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)


# Get all data in chosen category
@app_v1.get('/{category}', tags=['Get any category'], description='Categories are: art, food, friends, learning, '
                                                                  'party, sport and travel.')
async def get_category(category: Category):
    redis_key = str(category)
    cached_result = await re.redis.get(redis_key)
    if cached_result:
        print('cached')
        return pickle.loads(cached_result)
    else:
        fetched_category = await db.fetch_category(category)
        category_to_cache = pickle.dumps(fetched_category)
        await re.redis.set(redis_key, category_to_cache, expire=4)
        print('not cached')
        return fetched_category


# Update category instance partially
@app_v1.patch('/{category}/{uuid}')
async def update_category_instance(category: Category, uuid: str, query=Body(..., embed=True)):
    column = [*query][0]
    value = query[column]
    try:
        updated_instance = await db.update_category(category, uuid, column, value)
        return {'response': f'{updated_instance} was updated successfully. {column} was changed to {value}'}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)


# Delete category instance
@app_v1.delete('/{category}/{uuid}')
async def delete_category_instance(category: Category, uuid: str):
    try:
        deleted_instance = await db.delete_instance(category, uuid)
        return {'response': f'{deleted_instance} was deleted successfully'}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)


# Create new food instance
@app_v1.post('/food', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_food_object(food: Food = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        food_to_db = dict(food)
        food_to_db['id'] = str(uuid4())
        new_food_instance = await db.insert_food(food_to_db)
        if new_food_instance is not None:
            return {'response': f"{new_food_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)


# Create new learning instance
@app_v1.post('/learning', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_learning_object(learning: Learning = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        learning_to_db = dict(learning)
        learning_to_db['id'] = str(uuid4())
        new_learning_instance = await db.insert_learning(learning_to_db)
        if new_learning_instance is not None:
            return {'response': f"{new_learning_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)


# Create new sport instance
@app_v1.post('/sport', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_sport_object(sport: Sport = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        sport_to_db = dict(sport)
        sport_to_db['id'] = str(uuid4())
        new_sport_instance = await db.insert_sport(sport_to_db)
        if new_sport_instance is not None:
            return {'response': f"{new_sport_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)


# Create new travel instance
@app_v1.post('/travel', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_travel_object(travel: Travel = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        travel_to_db = dict(travel)
        travel_to_db['id'] = str(uuid4())
        new_travel_instance = await db.insert_travel(travel_to_db)
        if new_travel_instance is not None:
            return {'response': f"{new_travel_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)


# Create new travel instance
@app_v1.post('/friends', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_friends_object(friends: Friends = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        friends_to_db = dict(friends)
        friends_to_db['id'] = str(uuid4())
        new_friends_instance = await db.insert_friends(friends_to_db)
        if new_friends_instance is not None:
            return {'response': f"{new_friends_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)


# Create new travel instance
@app_v1.post('/art', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_art_object(art: Art = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        art_to_db = dict(art)
        art_to_db['id'] = str(uuid4())
        new_art_instance = await db.insert_art(art_to_db)
        if new_art_instance is not None:
            return {'response': f"{new_art_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)


# Create new travel instance
@app_v1.post('/party', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_party_object(party: Party = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        party_to_db = dict(party)
        party_to_db['id'] = str(uuid4())
        new_party_instance = await db.insert_party(party_to_db)
        if new_party_instance is not None:
            return {'response': f"{new_party_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)
