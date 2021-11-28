from de import De

class Gobelet() :
    def __init__(self, nbdes : int ):
        self.valeur = 0
        self.des = []
        self.nbdes=nbdes

    #Ajout un certain nombre de dés dans une liste et en retourne une valeur
    def ajoutliste(self):
        var= 0
        for i in range(self.nbdes):
            self.des.append(De())
            self.des[i].lancer()
            var+= self.des[i].get_valeur() 
        return var

    @property   
    def des(self):
        return self._des

    @des.setter 
    def des (self, des):
        self._des=des

    #renvoie la valeur du gobelet
    def get_valeur(self):
        return self.valeur

# lancer = Gobelet(4).lancer()