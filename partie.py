class Partie :
    def __init__(self, joueurs, nb_tours) -> None:
        self.joueurs = joueurs
        self.nb_tours = nb_tours
    
    @property
    def joueurs(self):
        return self._joueurs

    @joueurs.setter 
    def joueurs (self, joueurs):
        self._joueurs=joueurs
    
    @property
    def nb_tours(self):
        return self._nb_tours

    @nb_tours.setter 
    def nb_tours (self, nb_tours):
        self._nb_tours=nb_tours

    #permet d'inscrire des joueurs dans la partie
    def initialiser():
        pass
    
    #lance la partie : chaque joueur joue à tour de rôle 
    #pendant les n tours. Une fois la partie terminée, affiche le gagnant.
    def lancer():
        pass

    #compare les scores des joueurs et affiche le gagnant.
    def afficher_gagnant():
        pass