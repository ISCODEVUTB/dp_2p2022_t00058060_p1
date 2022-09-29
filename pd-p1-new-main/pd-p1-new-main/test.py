import unittest
from clase_armas import Armas
from clase_humano import Humano
from clase_alien import Alien
from clase_artificial import Artificial
from clase_superhumano import Superhumano
from clase_debilidad import Debilidades
from clase_personalidad import Personalidad
from enumerations import Genre, Morality, Identity, Personality, Character

class testing(unittest.TestCase):
    personalidad = Personalidad("Inteligencia", "Desarrollada", Personality.EXTROVERT, Character.IMPASSIONED)
    armas = Armas("pistola", "herencia", "0.80")
    human = Humano("StanLee", "Unknown", 1.78, 73.0, Genre.MALE, "black", "green", "white")
    alien = Alien("E.T", "ET", "1.54", "65", Genre.MALE, "Jupiter")
    superhuman = Superhumano("SuperMAN", "Clark", 1.92, 78.4, Genre.MALE, Morality.HERO, Identity.SECRET)    
    artificial = Artificial("Ultron", "Ultron", "1.90", "80", Genre.MALE, "Tony Stark" ) 
    debilidad = Debilidades("Kriptonita", "ENEMIGOS", 2.4, "soledad")
    # Tests Clase superhumano
    def test_add_superhumano(self):
        self.assertTrue(self.superhuman.add(self.debilidad))

    def test_enemigo_superhumano(self):
        self.assertTrue(self.superhuman.enemigo(self.human))

    def test_liga_superhumano(self):
        self.assertTrue(self.superhuman.liga("marvel"))

    # Tests clase humano
    def test_enemigo_humano(self):
        self.assertTrue(self.human.enemigo(self.superhuman))

    def test_add_humano(self):
        self.assertTrue(self.human.add(self.personalidad))

    # Tests clase Alien
    def test_add_alien(self):
        self.assertTrue(self.alien.add(self.armas))

    def test_enemigo_alien(self):
        self.assertTrue(self.alien.enemigo(self.artificial))

    # Tests clase Artificial
    def test_add_artificial(self):
        self.assertTrue(self.artificial.add(self.personalidad))

    def test_enemigo_artificial(self):
        self.assertTrue(self.artificial.enemigo(self.alien))
  
    #Tests Caracterizaciones methods

    def testWeaponss(self):
        evaluar = self.armas.change_power()
        self.assertEqual(evaluar, 'Increase power for pistola')

if __name__ == '__main__':
    unittest.main()