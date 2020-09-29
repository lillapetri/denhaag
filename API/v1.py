from Models.eat import Food, food_object
from Models.entertain import Entertainment, entertainment_object
from Models.learn import Learning, learning_object
from Models.socialize import Social, social_object
from Models.sport import Sport, sport_object
from Models.travel import Travel, travel_object
from Utils.security import authenticate, create_jwt_token
from fastapi import Body, Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED

app_v1 = FastAPI(root_path='/v1')


# Retrieve all the data from every category
@app_v1.get('/')
async def get_all():
    return {'food': food_object, 'learning': learning_object, 'sport': sport_object, 'social': social_object,
            'entertainment': entertainment_object, 'travel': travel_object}


# Test API route
@app_v1.get('/test')
async def test_connection():
    return {'Connection established.'}


# Get token
@app_v1.post('/login')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user = authenticate(username, password)
    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    else:
        token = create_jwt_token(username)
        return token


# Get all data in food category
@app_v1.get('/food')
async def get_food_category():
    return food_object


# Create new food instance
@app_v1.post('/food')
async def create_food_object(food: Food = Body(..., embed=True)):
    return food


# Get all data in learning category
@app_v1.get('/learning')
async def get_learn_category():
    return learning_object


# Create new learning instance
@app_v1.post('/learning')
async def create_learning_object(learning: Learning = Body(..., embed=True)):
    return learning


# Get all data in sport category
@app_v1.get('/sport')
async def get_sport_category():
    return sport_object


# Create new sport instance
@app_v1.post('/sport')
async def create_sport_object(sport: Sport = Body(..., embed=True)):
    return sport


# Get all data in social category
@app_v1.get('/social')
async def get_socialize_category():
    return social_object


# Create new social instance
@app_v1.post('/social')
async def create_social_object(social: Social = Body(..., embed=True)):
    return social


# Get all data in entertainment category
@app_v1.get('/entertainment')
async def get_entertainment_category():
    return entertainment_object


# Create new entertainment instance
@app_v1.post('/entertainment')
async def create_entertainment_object(entertainment: Entertainment = Body(..., embed=True)):
    return entertainment


# Get all data in travel category
@app_v1.get('/travel')
async def get_travel_category():
    return travel_object


# Create new travel instance
@app_v1.post('/travel')
async def create_travel_object(travel: Travel = Body(..., embed=True)):
    return travel
