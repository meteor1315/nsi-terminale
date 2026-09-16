"""
Les dictionnaires
====================

A. Structure abstraite d'un dictionnaire
-----------------------------------------

Un dictionnaire est une structure de donnees composee de couples
cle-valeur. Contrairement a une liste, on n'accede pas a une valeur avec
sa position, mais avec une cle. Chaque cle est unique.

Exemple : dans un annuaire, le nom d'une personne est la cle et son numero
de telephone est la valeur.

Les operations principales sont :

- ajout : associer une nouvelle valeur a une nouvelle cle ;
- modif : remplacer la valeur associee a une cle existante ;
- suppr : supprimer une cle et sa valeur ;
- rech : rechercher une valeur a l'aide de sa cle.

B. Implementation en Python
---------------------------

Le dictionnaire est une structure native de Python. Il s'ecrit entre
accolades et chaque couple est ecrit sous la forme cle: valeur.

	contacts = {"Alice": "0600000000"}

Une cle doit etre unique et doit pouvoir etre hachee. Python utilise une
fonction de hachage pour calculer un identifiant associe a la cle. Cette
organisation permet generalement d'acceder rapidement a la valeur.

C. Liste et dictionnaire : comparaison des recherches
------------------------------------------------------

Dans une liste, il faut parcourir les elements et les comparer a la valeur
recherchee. Pour une liste de taille n, le nombre d'operations est de l'ordre
de n : on note cette complexite O(n).

Dans un dictionnaire, la recherche utilise directement une cle. En moyenne,
le nombre d'operations ne depend pas de la taille du dictionnaire : on note
cette complexite O(1).

O(1) signifie un temps moyen constant, et non pas que l'operation ne demande
aucun calcul. Dans certains cas particuliers, une recherche dans un
dictionnaire peut etre moins favorable.

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries
"""


def rechercher_dans_liste(elements, valeur):
	"""Recherche une valeur dans une liste en la parcourant."""
	for element in elements:  # Examine les elements un par un.
		print("Comparaison dans la liste :", element, "avec", valeur)
		if element == valeur:  # Compare l'element courant avec la valeur cherchee.
			return True  # La valeur a ete trouvee.
	return False  # Toute la liste a ete parcourue sans succes.


# Creation d'un dictionnaire : chaque nom est une cle associee a une valeur.
contacts = {
	"Alan Turing": "30 avril 1912",
	"Ada Lovelace": "10 decembre 1815",
	"John von Neumann": "28 decembre 1903",
	"Claude Shannon": "30 avril 1916",
}
print("1. Dictionnaire initial :", contacts)

# Ajout : on associe une nouvelle valeur a une nouvelle cle.
contacts["Grace Hopper"] = "9 decembre 1906"
print("2. Apres l'ajout de Grace Hopper :", contacts)

# Modification : la cle existe deja, seule sa valeur est remplacee.
contacts["Alan Turing"] = "23 juin 1912"
print("3. Apres la modification d'Alan Turing :", contacts)

# Recherche : on utilise la cle pour acceder directement a sa valeur.
date_naissance = contacts["Ada Lovelace"]
print("4. Recherche d'Ada Lovelace :", date_naissance)

# Suppression : del retire la cle et la valeur qui lui est associee.
del contacts["Grace Hopper"]
print("5. Apres la suppression de Grace Hopper :", contacts)

# Test d'appartenance : in verifie si une cle existe dans le dictionnaire.
if "Claude Shannon" in contacts:
	print("6. Claude Shannon est present :", contacts["Claude Shannon"])

# Comparaison avec une liste : la fonction doit parcourir les elements.
noms = ["Alan Turing", "Ada Lovelace", "John von Neumann", "Claude Shannon"]
print("7. Resultat de la recherche dans la liste :", rechercher_dans_liste(noms, "Claude Shannon"))

# Dans un dictionnaire, la recherche se fait avec une cle.
print("8. Recherche directe dans le dictionnaire :", contacts["John von Neumann"])
