from enum import Enum

class PriceCategory(str, Enum):
    free: str = "free"
    cheap: str = "cheap"
    average: str = "average"
    expensive: str = "expensive"
