class ArbreBinaire :
    def __init__(self, valeur) :
        # Chaque noeud contient une cle et deux sous-arbres eventuels.
        self.clé = valeur 
        self.gauche = None 
        self.droit = None 
    def parcours_infixe(self, arbre):
        # Un parcours infixe visite gauche, le noeud, puis droite.
        # Dans un ABR, les cles sont ainsi affichees dans l'ordre croissant.
        # Complexite : O(n), car les n noeuds sont tous visites.
        if arbre != None : 
            self.parcours_infixe(arbre.gauche)
            print(arbre.clé)
            self.parcours_infixe(arbre.droit)

    def est_présent(self, valeur):
        # On compare la valeur cherchee a la cle du noeud courant.
        # Complexite : O(log n) si l'arbre est equilibre, O(n) dans le pire cas.
        if self.clé == valeur:
            return True
        if valeur < self.clé:
            # Une valeur plus petite ne peut se trouver que dans le sous-arbre gauche.
            return self.gauche is not None and self.gauche.est_présent(valeur)
        # Une valeur plus grande ne peut se trouver que dans le sous-arbre droit.
        return self.droit is not None and self.droit.est_présent(valeur)

    def insérer(self, valeur):
        # On descend dans l'arbre jusqu'a trouver une place vide.
        # Complexite : O(log n) si l'arbre est equilibre, O(n) dans le pire cas.
        if valeur < self.clé:
            # Les valeurs plus petites sont placees a gauche.
            if self.gauche is None:
                self.gauche = ArbreBinaire(valeur)
            else:
                self.gauche.insérer(valeur)
        elif valeur > self.clé:
            # Les valeurs plus grandes sont placees a droite.
            if self.droit is None:
                self.droit = ArbreBinaire(valeur)
            else:
                self.droit.insérer(valeur)
        # Si valeur == self.clé, elle est deja presente : on ne l'ajoute pas.

# Construction de l'arbre suivant :
#       5
#      / \
#     2   8
#      \
#       3
a= ArbreBinaire(5) 
a.gauche = ArbreBinaire(2)
a.droit = ArbreBinaire(8) 
a.gauche.droit = ArbreBinaire(3) 

