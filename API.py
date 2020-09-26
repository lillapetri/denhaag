from fastapi import FastAPI, Body
from Models.eat import food_object, Food
from Models.learn import learning_object, Learning
from Models.sport import sport_object, Sport
from Models.socialize import social_object, Social
from Models.entertain import entertainment_object, Entertainment
from Models.travel import travel_object, Travel

app = FastAPI()


# Retrieve all the data from every category
@app.get('/')
async def get_all():
    return {'food': food_object, 'learning': learning_object, 'sport': sport_object, 'social': social_object,
            'entertainment': entertainment_object, 'travel': travel_object}


# Test API route
@app.get('/test')
async def test_connection():
    return {'Connection established.'}


# Get all data in food category
@app.get('/food')
async def get_food_category():
    return food_object


# Create new food instance
@app.post('/food')
async def create_food_object(food: Food = Body(..., embed=True)):
    return food


# Get all data in learning category
@app.get('/learning')
async def get_learn_category():
    return learning_object


# Create new learning instance
@app.post('/learning')
async def create_learning_object(learning: Learning = Body(..., embed=True)):
    return learning


# Get all data in sport category
@app.get('/sport')
async def get_sport_category():
    return sport_object


# Create new sport instance
@app.post('/sport')
async def create_sport_object(sport: Sport = Body(..., embed=True)):
    return sport


# Get all data in social category
@app.get('/social')
async def get_socialize_category():
    return social_object


# Create new social instance
@app.post('/social')
async def create_social_object(social: Social = Body(..., embed=True)):
    return social


# Get all data in entertainment category
@app.get('/entertainment')
async def get_entertainment_category():
    return entertainment_object


# Create new entertainment instance
@app.post('/entertainment')
async def create_entertainment_object(entertainment: Entertainment = Body(..., embed=True)):
    return entertainment


# Get all data in travel category
@app.get('/travel')
async def get_travel_category():
    return travel_object


# Create new travel instance
@app.post('/travel')
async def create_travel_object(travel: Travel = Body(..., embed=True)):
    return travel
