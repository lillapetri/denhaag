from enum import Enum


class District(str, Enum):
    centrum: str = "Centrum"
    escamp: str = "Escamp"
    haagse_hout: str = "Haagse Hout"
    laak: str = "Laak"
    leidscheveen_ypenburg: str = "Leidscheveen-Ypenburg"
    loosduinen: str = "Loosduinen"
    scheveningen: str = "Scheveningen"
    segbroek: str = "Segbroek"
