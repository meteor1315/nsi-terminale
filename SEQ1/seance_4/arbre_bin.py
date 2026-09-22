"""
Pour implémenter un arbre binaire en python on crée une classe Noeud qui exploitera la nature récursive des arbres binaires.    
""" 

class Noeud :
    def __init__(self,racine):
        self.gauche= None 
        self.racine=racine 
        self.droit= None 
    
    def __repr__(self):
        #f'...'	Crée une f-string, c’est-à-dire une chaîne avec des valeurs insérées
        return f'{self.racine}({str(self.gauche)},{str(self.droit)})' # Renvoie l'arbre sous la forme : racine(gauche,droit)
    
    def hauteur (self): #on ajoute une méthode permettant de calculer récursivement la hauteur d'un arbre
        if self==None : 
            return -1 
        else : 
            hauteur_gauche=self.gauche.hauteur() if self.gauche else -1 
            hauteur_droite=self.droit.hauteur() if self.droit else -1
            return 1+max (hauteur_gauche,hauteur_droite)
        
    # Exercice 1: 
    
    def taille (self, n):
        if n==None :
            return 0
        else : 
            taille_gauche=self.gauche.taille() if self.gauche else 0 
            taille_droite=self.droit.taille() if self.droit else 0           
            return 1+taille_gauche+taille_droite 
        

arbre_G = Noeud ('G')
arbre_Gg = Noeud ('G_g')
arbre_G.gauche = arbre_Gg 
arbre_D = Noeud ('D')
arbre_Dg = Noeud ('D_g')
arbre_Dd = Noeud ('D_d')
arbre_D.gauche = arbre_Dg
arbre_D.droit = arbre_Dd 
arbre_A = Noeud('A')
arbre_A.gauche = arbre_G 
arbre_A.droit = arbre_D

print(arbre_A)
 
