from abc import ABC, abstractmethod

class Caracterizacion(ABC):
 
    name: str
    origen: str

    def __init__(self, name: str, origen: str):
        self.name = name
        self.origen = origen

    
    @abstractmethod
    def change_power(self) -> str:
        pass

    
