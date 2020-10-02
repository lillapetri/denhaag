from uuid import uuid4

from Models.food import Food
from Models.learning import Learning
from Models.sport import Sport
from Models.travel import Travel
from Utils.db_functions import db_fetch_category, db_insert_food, db_insert_learning, db_insert_sport, db_insert_travel
from fastapi import APIRouter, Body, HTTPException, Header
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

app_v1 = APIRouter()


# # Retrieve all the data from every category
# @app_v1.get('/', tags=['Index'])
# async def get_all():
#     return categories


# Get all data in chosen category
@app_v1.get('/{category}', tags=['Get any category'], description='Categories are: art, food, friends, learning, '
                                                                  'party, price_category, sport and travel.')
async def get_category(category):
    fetched_category = await db_fetch_category(category)
    return fetched_category


# Create new food instance
@app_v1.post('/food', tags=['Add instance to database'], description='Only available for admins.',
             status_code=HTTP_201_CREATED)
async def create_food_object(food: Food = Body(..., embed=True), x_custom: str = Header('default')):
    try:
        food_to_db = dict(food)
        food_to_db['id'] = str(uuid4())
        new_food_instance = await db_insert_food(food_to_db)
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
        new_learning_instance = await db_insert_learning(learning_to_db)
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
        new_sport_instance = await db_insert_sport(sport_to_db)
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
        new_travel_instance = await db_insert_travel(travel_to_db)
        if new_travel_instance is not None:
            return {'response': f"{new_travel_instance} is created"}
    except Exception as e:
        print(e)
        detail = 'Something went wrong. Please try again.'
        if hasattr(e, 'detail'):
            detail = e.detail
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)
    return HTTPException(status_code=500)
