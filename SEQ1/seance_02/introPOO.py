class Point:  # Définit la classe Point, c'est-à-dire le modèle des objets Point.
    """Représente un point du plan muni d'un repère."""

    def __init__(self, x, y,col):  # Constructeur appelé lors de la création d'un point.
        self.abscisse = x  # self désigne l'objet créé ; on mémorise son abscisse.
        self.ordonnee = y  # On mémorise son ordonnée dans un attribut de l'objet.
        self.couleur = col 
        
    def deplace(self, dx, dy):  # Déplace le point de dx horizontalement et dy verticalement.
        self.abscisse += dx  # Ajoute dx à l'abscisse actuelle.
        self.ordonnee += dy  # Ajoute dy à l'ordonnée actuelle.

    def rotation180(self):  # Effectue une rotation de 180 degrés autour de l'origine.
        self.abscisse = -self.abscisse  # Change le signe de l'abscisse.
        self.ordonnee = -self.ordonnee  # Change le signe de l'ordonnée.

    def __repr__(self):  # Méthode spéciale utilisée pour représenter l'objet sous forme de texte.
        return f'({self.abscisse!r}; {self.ordonnee!r};couleur:{self.couleur})'  # f-string avec les valeurs des attributs. 

        


"""
Explication des syntaxes importantes
=====================================

Une classe est un modèle qui permet de créer des objets. Un objet Point est
une instance de la classe Point.

Le mot self représente l'objet lui-même. Il permet d'accéder à ses attributs
avec la notation self.abscisse ou self.ordonnee.

La méthode __init__ est appelée automatiquement lors de la création d'un
objet, par exemple avec Point(2, 3). Elle initialise les attributs de l'objet.

La méthode __repr__ est une méthode spéciale. Elle est utilisée pour obtenir
une représentation textuelle de l'objet, notamment dans la console Python ou
avec print.

La notation f'...' crée une f-string. Les expressions placées entre accolades
sont remplacées par leur valeur. Par exemple, {self.abscisse!r} insère la
représentation de self.abscisse dans la chaîne.

L'opérateur += est une écriture raccourcie : self.abscisse += dx équivaut à
self.abscisse = self.abscisse + dx.

Le symbole !r dans une f-string demande d'utiliser repr() pour représenter la
valeur. Le point-virgule et les parenthèses dans la chaîne sont simplement du
texte destiné à l'affichage.
"""

"""Illustration:"""

"""A=Point(3,4)
print(type(A))
print(A)
A.deplace(0,10)
print(A)"""

"""Comme on peut le constater, pour appliquer une méthode à un objet on utilise ce que l’on appelle la notation
« pointée » objet.methode(avec ou sans argument). """


cx = 12  # Définit l'abscisse du point à transformer.
cy = 8  # Définit l'ordonnée du point à transformer.

def rotation180_coordonnees(cx, cy):  # Transforme les coordonnées par une rotation de 180 degrés.
    cx = -cx  # Change le signe de l'abscisse.
    cy = -cy  # Change le signe de l'ordonnée.
    return cx, cy  # Retourne les nouvelles coordonnées.

#print(rotation180_coordonnees(cx, cy))  # Affiche (-12, -8).

# Utilisation de la méthode de la classe Point.
#point = Point(12, 8)  # Crée un point de coordonnées (12, 8).
#point.rotation180()  # Applique la rotation directement à cet objet.
#print(point)  # Affiche (-12; -8).


# Idée à compléter : une couleur ne se définit pas avec « def ... in range ».
# def couleur in range (000000, FFFFFF):


