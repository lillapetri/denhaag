from datetime import datetime
from pydantic import BaseModel
from Models.district import District
from Models.covid_factor import CovidFactor
from Models.price_category import PriceCategory


class Social(BaseModel):
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


social = {"name": "Tiki Vavoom", "price_category": "average", "district": "Centrum", "category": "bar"}
social_object = Social(**social)