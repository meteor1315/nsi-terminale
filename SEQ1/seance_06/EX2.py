


class aliment : 
    def __init__(self, nom, energie, lipide, glucide, fibre, proteine, sel):
        self.nom=nom
        self.energie=energie 
        self.lipide=lipide
        self.glucide=glucide
        self.fibre=fibre
        self.proteine=proteine
        self.sel=sel 
    def __repr__(self):
        return f'Intitule :{self.nom}\nEnergie:{self.energie!r}kJ\nLipides:{self.lipide}g\nGlucides:{self.glucide!r}g\n Fibres:{self.fibre!r}g\nProtein:{self.proteine!r}g\nSel{self.sel!r}g'
    
riz=aliment 

 


