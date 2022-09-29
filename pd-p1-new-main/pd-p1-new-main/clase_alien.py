from clase_caracterizacion import Caracterizacion
from clase_personaje import Personaje
from enumerations import Genre


class Alien(Personaje):
    planet: str

    def __init__(self, alias: str, real_name: str, height: float, weight: float, genre: Genre, planet: str, characterizations = [], liga: str = '', enemigo=None):
        super().__init__(alias, real_name, height, weight, genre, characterizations, liga, enemigo)
        self.planet = planet



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

