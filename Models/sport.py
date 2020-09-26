from datetime import datetime
from pydantic import BaseModel
from Models.district import District
from Models.covid_factor import CovidFactor
from Models.price_category import PriceCategory


class Sport(BaseModel):
    name: str
    type: str
    price_category: PriceCategory = 'average'
    environment: str = None
    district: District
    address: str = None
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'Moderate risk'
    url: str = None
    created_at: datetime = datetime.now()


sport = {"type": "climbing", "name": "Klimmuur Hollands Spoor", "environment": "indoor", "district": "Centrum"}
sport_object = Sport(**sport)
