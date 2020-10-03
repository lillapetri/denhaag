import enum
from datetime import datetime

from Models.covid_factor import CovidFactor
from Models.district import District
from pydantic import BaseModel


class Category(str, enum.Enum):
    eat_in: str = "eat in"
    order: str = "order"
    take_away: str = "take away"
    cook: str = "cook"


class Food(BaseModel):
    name: str
    address: str = None
    cuisine: str
    votes: int = 0
    description: str = None
    url: str = None
    created_at: datetime = datetime.now()
    covid_factor: CovidFactor = 'Moderate risk'
    district: District
    price_category: str = None
    id: str = None
    # category: Set[Category] = None
