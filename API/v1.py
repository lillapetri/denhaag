from Models.eat import Food, food_object
from Models.entertain import Entertainment, entertainment_object
from Models.learn import Learning, learning_object
from Models.socialize import Social, social_object
from Models.sport import Sport, sport_object
from Models.travel import Travel, travel_object
from fastapi import APIRouter, Body, Header
from starlette.status import HTTP_201_CREATED

app_v1 = APIRouter()


# Retrieve all the data from every category
@app_v1.get('/', tags=['Index'])
async def get_all():
    return {'food': food_object, 'learning': learning_object, 'sport': sport_object, 'social': social_object,
            'entertainment': entertainment_object, 'travel': travel_object}


# Get all data in food category
@app_v1.get('/food', tags=['Food category'])
async def get_food_category():
    return food_object


# Create new food instance
@app_v1.post('/food', tags=['Food category'], status_code=HTTP_201_CREATED)
async def create_food_object(food: Food = Body(..., embed=True), x_custom: str = Header('default')):
    return {"request body": food, "request custom header": x_custom}


# Get all data in learning category
@app_v1.get('/learning', tags=['Learning category'])
async def get_learn_category():
    return learning_object


# Create new learning instance
@app_v1.post('/learning', tags=['Learning category'], status_code=HTTP_201_CREATED)
async def create_learning_object(learning: Learning = Body(..., embed=True)):
    return learning


# Get all data in sport category
@app_v1.get('/sport', tags=['Sport category'])
async def get_sport_category():
    return sport_object


# Create new sport instance
@app_v1.post('/sport', tags=['Sport category'], status_code=HTTP_201_CREATED)
async def create_sport_object(sport: Sport = Body(..., embed=True)):
    return sport


# Get all data in social category
@app_v1.get('/social', tags=['Social category'])
async def get_socialize_category():
    return social_object


# Create new social instance
@app_v1.post('/social', tags=['Social category'], status_code=HTTP_201_CREATED)
async def create_social_object(social: Social = Body(..., embed=True)):
    return social


# Get all data in entertainment category
@app_v1.get('/entertainment', tags=['Entertainment category'])
async def get_entertainment_category():
    return entertainment_object


# Create new entertainment instance
@app_v1.post('/entertainment', tags=['Entertainment category'], status_code=HTTP_201_CREATED)
async def create_entertainment_object(entertainment: Entertainment = Body(..., embed=True)):
    return entertainment


# Get all data in travel category
@app_v1.get('/travel', tags=['Travel category'])
async def get_travel_category():
    return travel_object


# Create new travel instance
@app_v1.post('/travel', tags=['Travel category'], status_code=HTTP_201_CREATED)
async def create_travel_object(travel: Travel = Body(..., embed=True)):
    return travel
