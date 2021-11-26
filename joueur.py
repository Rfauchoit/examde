from gobelet import Gobelet


class Joueur:
    def __init__(self,nom) -> None:
        self.nom = nom
        self._score = 0

    @property
    def nom(self):
        return self._nom

    @nom.setter 
    def nom (self, nom):
        self._nom=nom
    
    @property
    def score(self):
        return self._score

    @score.setter 
    def score (self, score):
        self._score=score

    # renvoie le nom du joueur
    def get_nom(self):
        return self._nom

    # renvoie le score du joueur
    def get_score(self) :
        return self._score
    
    # prend en paramètre le gobelet de la partie, lance le gobelet
    # met à jour le score du joueur en fonction du résultat du lancer
    def jouer(self, gobelet:Gobelet):
        self._score += gobelet.ajoutliste()
    

    #affiche en console le score du joueur
    def afficher_score(self):
        print(f"Le score est de {self.score}")

joueur = Joueur("Randy")
joueur.jouer(Gobelet(4))
joueur.afficher_score()
