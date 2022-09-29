from clase_caracterizacion import Caracterizacion
from clase_personaje import Personaje
from enumerations import Genre
from clase_ficha import IFicha


class Humano(Personaje, IFicha):
    race: str
    color_eye: str
    color_hair: str

    def __init__(self, alias: str, real_name: str, height: float, weight: float, genre: Genre, race: str, color_eye:str, color_hair: str, characterizations = [], liga: str = '', enemigo=None):
        super().__init__(alias, real_name, height, weight, genre, characterizations, liga, enemigo)
        self.race = race
        self.color_eye = color_eye
        self.color_hair= color_hair

    
   
    

    def add(self, characterization: Caracterizacion) -> bool:
        try:
            if(isinstance(characterization, Caracterizacion)):
                self.characterizations.append(characterization)
                return True
            else:
                raise ValueError
        except Exception:
            return False

    def liga(self, liga:str) -> bool:
        try:
            self.liga = liga
            return bool
        except Exception:
            return False

    def enemigo(self, enemigo: Personaje):
        try:
            if(isinstance(enemigo, Personaje)):
                self.characterizations.append(enemigo)
                return True
            else:
                raise ValueError
        except Exception:
            return False

    
