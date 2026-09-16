
"""  
    Implémentation d'une fille en Python 
    
    primitives : 
    
        - créer une file vide (creer_file)
        - tester si la file est vide (est_vide_file)
        - Accéder au premier élément dans la file (ajouter_file)
        - Retirer le premier élément de la file (retirer_file) 
    
    On écrira donc une fonction pour chaque primitive 
    l’implémentation choisie pour une file est un triplet :
    (tableau, position de la tête, nombre d’éléments)


""" 

LEN_FILE = 10 


def creer_file():  # Construit une file vide de taille fixe LEN_FILE.
    return {"tableau": ['_' * LEN_FILE],  # '_' représente une case vide.
            "position_tête" : 0,  # Position initiale de la tête de la file.
            "nombre_element" : 0}  # Nombre d'éléments présents dans la file.
    
def est_vide_file(file):  # Retourne True si la file est vide, False sinon.
    return file["nombre_element"]==0,  # La file est vide si elle contient 0 élément.

def premier_file(file):  # Retourne l'élément situé en tête de la file.
    assert not(est_vide_file(file)), 'la file est vide'  # Vérifie que la file n'est pas vide.
    pos = file["position_tete"]  # Récupère la position de la tête.
    return file["tableau"][pos]  # Retourne l'élément situé à cette position.

def retirer_file(file):  # Retire l'élément situé en tête de la file.
    assert not(est_vide_file(file)), 'la file est vide'  # Vérifie que la file n'est pas vide.
    pos = file["position_tete"]  # Récupère la position de la tête.
    file["tableau"][pos]='_'  # Remplace l'élément retiré par une case vide.
    file["nombre_element"]-=1  # Diminue le nombre d'éléments de la file.
    file["position_tête"]=(file["position_tête"+1])%LEN_FILE  # Avance la tête et revient à 0 après la dernière position.
    return  # La file a été modifiée directement et aucune valeur n'est renvoyée.

def ajouter_file(file, element):  # Ajoute un élément à la queue de la file.
    """Retourne la file mise à jour après l'ajout d'un élément."""
    assert file["nombre_element"]<LEN_FILE, 'la file est pleine' # Vérifie que la file possède encore une place disponible.
    pos = file["position_tete"]  # Récupère la position de la tête de la file.
    nb_element = file["nombre_element"]  # Récupère le nombre actuel d'éléments.
    fin = (pos+nb_element)%LEN_FILE  # Calcule la position de la queue avec un retour circulaire.
    file["tableau"][fin]=element  # Place le nouvel élément à la position calculée.
    file["nombre_element"]+=1  # Augmente le nombre d'éléments de la file.
    return file  # Renvoie la file mise à jour.

"""
    Implémentation d'une pille en Python:
    
        -créer une file vide (creer_file)
        -tester si la file est vide (est_vide_file)
        -accéder au premier élément de la file (premier_file)
        -ajouter un élément dans la file (ajouter_file)
        -retirer le premier élément de la file (retirer_file)

    On écrira donc une fonction pour chaque primitive 
    l’implémentation choisie pour une file est un triplet :
    (tableau, position de la tête, nombre d’éléments)
    
    """ 

LEN_PILE = 10  # Définit la taille maximale de la pile.


def creer_pile():  # Construit une pile vide de taille fixe LEN_PILE.
    return {"tableau": ['_'] * LEN_PILE,  # '_' représente une case vide.
            "position_sommet": -1}  # -1 indique que la pile est vide.


def est_vide_pile(pile):  # Retourne True si la pile est vide, False sinon.
    return pile["position_sommet"] == -1  # La pile est vide si son sommet vaut -1.


def sommet_pile(pile):  # Retourne l'élément situé au sommet de la pile.
    assert not(est_vide_pile(pile)), 'la pile est vide'  # Vérifie que la pile n'est pas vide.
    return pile["tableau"][pile["position_sommet"]]  # Retourne l'élément au sommet.


def empiler(pile, element):  # Ajoute un élément au sommet de la pile.
    """Met à jour la pile après l'empilement d'un élément au sommet."""
    assert not(pile["position_sommet"] >= LEN_PILE - 1), 'la pile est pleine'  # Vérifie qu'il reste une place.
    pile["tableau"][pile["position_sommet"] + 1] = element  # Place l'élément au-dessus du sommet actuel.
    pile["position_sommet"] += 1  # Déplace le sommet vers la nouvelle position.
    return pile  # Renvoie la pile mise à jour.


def depiler(pile):  # Retire l'élément situé au sommet de la pile.
    """Met à jour la pile après le dépilement de son sommet."""
    assert not(est_vide_pile(pile)), 'la pile est vide'  # Vérifie que la pile n'est pas vide.
    pile["tableau"][pile["position_sommet"]] = '_'  # Remplace l'élément retiré par une case vide.
    pile["position_sommet"] -= 1  # Déplace le sommet vers la position précédente.
    return pile  # Renvoie la pile mise à jour.


"""
Synthèse : files et piles
==========================

Une file et une pile sont des structures de données qui permettent de
stocker plusieurs éléments et de les manipuler selon un ordre précis.

La file fonctionne selon le principe FIFO (First In, First Out), c'est-à-dire
« premier entré, premier sorti ». Un élément est ajouté en queue avec
ajouter_file et le premier élément est consulté ou retiré en tête avec
premier_file et retirer_file. Une file peut être représentée par un tableau,
la position de sa tête et le nombre d'éléments présents.

La pile fonctionne selon le principe LIFO (Last In, First Out), c'est-à-dire
« dernier entré, premier sorti ». Un élément est ajouté au sommet avec
empiler et le dernier élément ajouté est consulté ou retiré avec sommet_pile
et depiler. Une pile peut être représentée par un tableau et la position de
son sommet. La valeur -1 indique que la pile est vide.

Notions clés à retenir :

- Une file utilise une tête et une queue ; une pile utilise un sommet.
- FIFO correspond aux files ; LIFO correspond aux piles.
- est_vide_file et est_vide_pile testent si la structure ne contient aucun
    élément.
- Il faut vérifier qu'une structure n'est pas vide avant de consulter ou de
    retirer un élément.
- Il faut vérifier qu'une structure n'est pas pleine avant d'ajouter un
    élément lorsque sa taille est fixe.
- Dans un tableau circulaire, l'opérateur modulo (%) permet de revenir au
    début du tableau après sa dernière position.
- Les opérations d'ajout et de retrait modifient directement le dictionnaire
    représentant la file ou la pile.

Pourquoi utiliser un dictionnaire plutôt que deque ?

Le dictionnaire est utilisé dans ce cours pour comprendre la représentation
interne d'une file. Il permet de stocker le tableau, la position de la tête
et le nombre d'éléments, puis de programmer soi-même les opérations de la
file. On découvre ainsi le fonctionnement d'une file et d'un tableau
circulaire.

Dans un programme réel, deque du module collections est souvent plus simple
et plus pratique à utiliser. Les détails de fonctionnement sont alors gérés
par Python : append ajoute un élément en queue et popleft retire l'élément
en tête. Le dictionnaire sert donc surtout à apprendre, tandis que deque est
adapté à une utilisation courante.
"""

from collections import deque  # Importe la structure de file prête à l'emploi.

file_deque = deque()  # Crée une file vide.
file_deque.append("A")  # Ajoute l'élément "A" en queue.
file_deque.append("B")  # Ajoute l'élément "B" en queue.
premier = file_deque[0]  # Consulte le premier élément sans le retirer.
element = file_deque.popleft()  # Retire et récupère le premier élément.




