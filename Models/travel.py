from datetime import datetime
from pydantic import BaseModel
from typing import List
from Models.covid_factor import CovidFactor


class Travel(BaseModel):
    location: str
    distance_in_km: int
    votes: int = 0
    programs: List[str] = []
    description: str = None
    covid_factor: CovidFactor = 'High risk'
    created_at: datetime = datetime.now()


travel = {"location": "Monster", "distance_in_km": 15}
travel_object = Travel(**travel)
