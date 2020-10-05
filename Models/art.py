from datetime import datetime

from Models.covid_factor import CovidFactor
from Models.district import District
from Models.price_category import PriceCategory
from pydantic import BaseModel


class Art(BaseModel):
    name: str
    price_category: PriceCategory = None
    type: str = None
    district: District = None
    address: str = None
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'Moderate risk'
    url: str = None
    created_at: datetime = datetime.now()
