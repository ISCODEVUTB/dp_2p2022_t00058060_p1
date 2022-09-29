from clase_caracterizacion import Caracterizacion

class Debilidades(Caracterizacion):
    trigger: str
    duration: float

    def __init__(self, name: str, origen: str, duration: float, trigger: str):
        super().__init__(name, origen)
        self.duration = duration
        self.trigger = trigger

   
    def change_power(self) -> str:
        return f'Decrease power for {self.name}'


    

    
