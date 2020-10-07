from datetime import datetime

from pydantic import BaseModel

from Models.covid_factor import CovidFactor


class Friends(BaseModel):
    name: str
    platform: str
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'High risk'
    url: str = None
    created_at: datetime = datetime.now()
