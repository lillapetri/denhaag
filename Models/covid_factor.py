from enum import Enum


class CovidFactor(str, Enum):
    safe: str = "safe"
    moderate_risk: str = "moderate risk"
    high_risk: str = "high risk"
    forbidden: str = "forbidden"
