from enum import Enum

class Genre(Enum):
   
    MALE = 1
    FEMALE = 2
    NO_BINARY = 3
    NONE = 4
class Morality(Enum):
   
    HERO = 1
    VILLAIN = 2
    ANTIHEREO = 3
    AMBIVALENT = 4
class Character(Enum):
    IMPASSIONED = 1
    NERVOUS = 2
    SENTIMENTAL = 3
    EASY_GOING = 4

class Personality(Enum):
    INTROVERT = 0
    EXTROVERT = 1

class Identity(Enum):

    SECRET = 1
    PUBLIC = 2

