from de import De

class Gobelet() :
    def __init__(self, nbdes : list ):
        self.valeur = 0
        self.des = []
        self.nbdes=nbdes
        self.ajoutliste()

    #Ajout un certain nombre de dés dans une liste
    def ajoutliste(self):
        for i in range(self.nbdes):
            (self.des).append(i)

    @property   
    def des(self):
        return self._des

    @des.setter 
    def des (self, des):
        self._des=des

    #renvoie la valeur du gobelet
    def get_valeur(self):
        return self.valeur
    
    #change la valeur des dés du gobelet ; met à jour la valeur du gobelet
    def lancer(self):
        jet = De().lancer() 
        self.valeur = self.valeur + jet

    #affiche en console le score du dernier lancer de gobelet
    def afficher_score(self):
        print(self.valeur)

lancer = Gobelet(4).afficher_score()