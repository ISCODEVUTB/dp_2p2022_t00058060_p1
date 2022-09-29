from abc import abstractmethod
from clase_caracterizacion import Caracterizacion
from enumerations import Genre


class Personaje():
    alias: str
    real_name: str
    genre: Genre
    height: float
    weight: float
    characterizations = []
    liga = ''
    enemigo = None


    def __init__(self, alias:str, real_name:str, height:float, weight:float, genre: Genre, characterizations = [], liga: str = '', enemigo = None):
        self.alias = alias
        self.real_name = real_name
        self.height = height
        self.weight = weight
        self.genre = genre


