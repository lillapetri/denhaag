from API.v1 import app_v1
from fastapi import FastAPI

app = FastAPI()
app.mount('/v1', app_v1)
