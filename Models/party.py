from datetime import datetime
from typing import List

from pydantic import BaseModel

from Models.covid_factor import CovidFactor
from Models.district import District


class Party(BaseModel):
    name: str
    date: str = None
    time: str = None
    ticket_price_in_euro: float = None
    tags: List[str] = []
    district: District = None
    address: str = None
    votes: int = 0
    description: str = None
    covid_factor: CovidFactor = 'High risk'
    url: str = None
    created_at: datetime = datetime.now()
