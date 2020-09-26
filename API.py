from fastapi import FastAPI
from Models.eat import food_object
from Models.learn import learn_object
from Models.sport import sport_object
from Models.socialize import socialize_object
from Models.entertain import entertain_object
from Models.travel import travel_object

app = FastAPI()
@app.get('/')
async def test():
    return {'food': food_object, 'learning': learn_object, 'sport': sport_object, 'social': socialize_object, 'entertainment': entertain_object, 'travel': travel_object}
@app.get('/test')
async def test():
    return {'Connection estabilished.'}
@app.get('/food')
async def food():
    return food_object
@app.get('/learning')
async def learn():
    return learn_object
@app.get('/sport')
async def sport():
    return sport_object
@app.get('/social')
async def socialize():
    return socialize_object
@app.get('/entertainment')
async def entertain():
    return entertain_object
@app.get('/travel')
async def travel():
    return travel_object