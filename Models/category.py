from enum import Enum


class Category(str, Enum):
    art: str = "art"
    food: str = "food"
    friends: str = "friends"
    learning: str = "learning"
    party: str = "party"
    sport: str = "sport"
    travel: str = "travel"
