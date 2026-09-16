
"""
On a vu que pour travailler avec une file il est nécessaire de disposer des primitives :

Créer une file vide (creer_file)

Tester si la file est vide (est_vide_file)

Accéder au premier élément de la file (premier_file)

Ajouter un élément dans la file (ajouter_file)

Retirer le premier élément de la file (retirer_file)

l'implémentation choisie pour cette file est un triplet (tableau, position de la tête, nombre d’éléments)""" 


LEN_FILE = 10 

def creer_file(): 
    return {"tableau":['_']*LEN_FILE,
            "position_tete": 0,
            "nombre_element": 0} 
    
    """ ce dictionnaire est constitué :
d’un tableau de longueur LEN_FILE (ici LEN_FILE = 10), on convient que le caractère '_' correspond à vide,

d’un entier compris entre 0 et LEN_FILE représentant la position de la tête de la file,

d’un entier compris entre 0 et LEN_FILE représentant le nombre d’éléments présents dans la file.

    """
    
def est_vide_file(file):
    return file["nombre_element"]==0 
    
    
#def premier_file(file): 
    #return file["position_tete"] 
    """file["position_tete"]  Correction  renvoie l'indice (la position) de la tête dans le tableau, 
    et non l'élément qui s'y trouve. Il faut récupérer l'élément stocké dans file["tableau"] à cet indice
    """ 
def premier_file(file):
    """Retourne l'élément situé en tête de file."""
    assert not est_vide_file(file), 'La file est vide'
    pos = file["position_tete"]
    return file["tableau"][pos]

    
#from collections import deque

#def retirer_file(file): 
 #   file=file.popleft   La méthode .popleft() n'existe pas sur un dictionnaire Python. 
 #   De plus, la sortie d'un élément modifie la tête de file de manière circulaire ((position + 1) % LEN_FILE) et décrémente le nombre d'éléments.
"""Correction :
On libère la case en y remettant le caractère '_'.
On décrémente file["nombre_element"].
On avance la position de la tête en utilisant le modulo % LEN_FILE pour gérer le comportement circulaire du tableau.
"""

def retirer_file(file):
    """Retire l'élément en tête de file et retourne la file mise à jour."""
    assert not est_vide_file(file), 'La file est vide'
    pos = file["position_tete"]
    file["tableau"][pos] = '_'
    file["nombre_element"] -= 1
    file["position_tete"] = (file["position_tete"] + 1) % LEN_FILE
    return file


#   def ajouter_file(file): 
#   file=file.append('x') 
#   return file 
    #La fonction doit prendre en paramètre l'élément à ajouter (element). De plus, l’ajout se fait en queue de file. 
    #L'indice de la queue se calcule grâce à la formule : (position_tete + nombre_element) % LEN_FILE.
""" 
Correction :
On vérifie que la file n'est pas pleine (nombre_element < LEN_FILE).
On calcule l'indice où insérer le nouvel élément.
On insère l'élément et on incrémente file["nombre_element"].  
""" 

def ajouter_file(file, element):
    """Ajoute un élément en queue de file et retourne la file mise à jour."""
    assert file["nombre_element"] < LEN_FILE, 'La file est pleine'
    pos = file["position_tete"]
    nb_elem = file["nombre_element"]
    fin = (pos + nb_elem) % LEN_FILE
    file["tableau"][fin] = element
    file["nombre_element"] += 1
    return file 

