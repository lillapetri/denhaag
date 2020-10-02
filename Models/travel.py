from datetime import datetime
from typing import List

from Models.covid_factor import CovidFactor
from pydantic import BaseModel


class Travel(BaseModel):
    name: str
    distance_in_km: int
    votes: int = 0
    programs: List[str] = []
    description: str = None
    covid_factor: CovidFactor = 'High risk'
    url: str = None
    created_at: datetime = datetime.now()


travel = {"name": "Monster", "distance_in_km": 15}
travel_object = Travel(**travel)
