from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Set
from Models.district import District
from Models.covid_factor import CovidFactor
from Models.price_category import PriceCategory
import enum


class Category(str, enum.Enum):
    eat_in: str = "eat in"
    order: str = "order"
    take_away: str = "take away"
    cook: str = "cook"

class Food(BaseModel):
    name: str
    price_category: PriceCategory
    category: Set[Category]
    district: District
    address: str = None
    cuisine: str
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'Moderate risk'
    url: str = None
    created_at: datetime = datetime.now()


food = {"name": "L'oro di Napoli", "price_category": "average", "district": "Segbroek",
        "cuisine": "Italian", "category": {"eat in", "order", "take away"}}
food_object = Food(**food)
