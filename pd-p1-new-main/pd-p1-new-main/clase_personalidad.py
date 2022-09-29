from enumerations import Personality, Character
from clase_caracterizacion import Caracterizacion


class Personalidad(Caracterizacion):
    personality_type: Personality
    character: Character
    
    def __init__(self, name: str, origen: str, personality_type: Personality, character: Character):
        super().__init__(name, origen)
        self.personality_type = personality_type
        self.character = character

    def change_power(self) -> str:
        return f'Decrease power for {self.name}'

   


    