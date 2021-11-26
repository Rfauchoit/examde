import random

class De:
    def __init__(self) -> None:
        self.valeur = 0

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter 
    def valeur (self, valeur):
        self._valeur=valeur

    #renvoie la valeur du dé
    def get_valeur(self):
        return self._valeur

    # Lancement d'un dé avec une valeur aléatoire entre 1 et 6   
    def lancer(self):
        self._valeur = random.randint(1,6)
        print (f"La valeur du dé est {self._valeur}")
    
# lancerde = De()
# lancerde.lancer()

