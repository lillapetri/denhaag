from datetime import datetime

from Models.covid_factor import CovidFactor
from Models.district import District
from Models.price_category import PriceCategory
from pydantic import BaseModel


class Part(BaseModel):
    name: str
    price_category: PriceCategory
    category: str = None
    district: District
    address: str = None
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'High risk'
    url: str = None
    created_at: datetime = datetime.now()


party = {"name": "Harry Potter", "price_category": "average", "district": "Centrum",
         "category": "movies"}
party_object = Part(**party)
