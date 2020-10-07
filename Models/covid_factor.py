from enum import Enum


class CovidFactor(str, Enum):
    safe: str = "Safe"
    moderate_risk: str = "Moderate risk"
    high_risk: str = "High risk"
    forbidden: str = "Forbidden"
