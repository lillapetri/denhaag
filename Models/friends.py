from datetime import datetime

from Models.covid_factor import CovidFactor
from pydantic import BaseModel


class Friends(BaseModel):
    name: str
    platform: str
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'High risk'
    url: str = None
    created_at: datetime = datetime.now()
