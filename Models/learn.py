from datetime import datetime
from pydantic import BaseModel
from Models.covid_factor import CovidFactor
from Models.price_category import PriceCategory


class Learning(BaseModel):
    language: str = 'English'
    price_category: PriceCategory = None
    subject: str = None
    platform: str
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'Safe'
    url: str = None
    created_at: datetime = datetime.now()


learning = {"language": "Dutch", "price_category": "average", "subject": "language", "platform": "online"}
learning_object = Learning(**learning)
