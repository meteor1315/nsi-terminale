"""
 
    Il est important de noter que le type List proposé nativement par le langage Python n’est pas une
    implémentation de la structure de données abstraite de liste (voir EX4.txt).
    Pour implémenter la structure de données liste on peut par exemple utiliser les tuples.

""" 

def creer_liste():  # Crée et retourne une liste vide.
    return None  # None représente la liste vide.

def ajouter_en_tete(x, L):  # Ajoute l'élément x en tête de la liste L.
    return (x,L)  # Retourne un tuple contenant la tête et le reste de la liste.

def queue(L):  # Retourne la liste privée de son premier élément.
    return L[1]  # Le deuxième élément du tuple correspond à la queue.

def tete(L):  # Retourne le premier élément de la liste L.
    return L[0]  # Le premier élément du tuple correspond à la tête.

def est_vide(L):  # Vérifie si la liste L est vide.
    return L == None  # Retourne True si L vaut None, sinon False.

    """
    À partir de l’implémentation ci-dessous, écrire une fonction nombre_element qui prend en argument une liste
    et retourne son nombre d’éléments.
    Écrire une fonction val(i, L) qui parcourt une liste L et retourne l’élément de L au rang i avec i compris entre
    0 et le nombre d’éléments de la liste moins 1 (on pourra utiliser des « assert » pour tester cette pré-
    condition).

    """ 

def nombre_element(L):
    if est_vide(L):
        return L==0  # Erreur : L vaut None ; il faut retourner le nombre 0.
    else :
        return L[0]+L[1]  # Erreur : L[0] est la tête et L[1] la queue, pas deux nombres.


"""
Correction commentée
====================

Une liste vide vaut None et contient donc zéro élément. Pour une liste non
vide, on compte un élément pour la tête, puis on recommence avec la queue.
"""


def nombre_element_corrige(L):  # Retourne le nombre d'éléments de la liste L.
    if est_vide(L):  # Cas de base : la liste vide contient zéro élément.
        return 0
    return 1 + nombre_element_corrige(queue(L))  # Compte la tête puis la queue.



def val(i, L):  # Retourne l'élément situé au rang i dans la liste L.
    assert 0 <= i < nombre_element_corrige(L), 'rang invalide'  # Vérifie que le rang existe.
    if i == 0:  # Au rang 0, l'élément recherché est la tête.
        return tete(L)
       
    return val(i - 1, queue(L))  # Parcourt la queue avec un rang diminué de 1.
    

    
"""
    Combien d’étapes sont nécessaires pour parcourir la liste jusqu’à l’élément de rang i ?
        il faut i etape pout parcourire la liste jusqu’à l’élément de rang i
        # Cette réponse est correcte : il faut utiliser queue i fois.

    On donne la fonction est_dans définie ci-dessous qui retourne vrai si x est un élément de L et faux
    sinon. Décrire comment cette fonction procède pour déterminer si une valeur est dans la liste ou non ? 

        Pour vérifié si une valeur est dans la liste ou non la fonction vérifie dans un premier temps si la liste est vide ce qui condition les autrs etapes.
        # Idée correcte : une liste vide donne directement False.
        Si la liste n'est pas vide alors la vonction vérifie dans un premier temps a l'aide d'un booléen "True" si x est a la tete de la liste.
        # La fonction compare x à la tête ; elle ne crée pas elle-même un booléen True.
        Si x n'est pas la tete de la liste donc "False", alors x est "False" ou est un élément de queue(L)
        # Correction : si x n'est pas la tête, la recherche continue dans queue(L).
    
    Combien d’étapes dans le pire des cas sont nécessaires pour obtenir une réponse de la fonction
    est_ dans(x, L)?
    
    Dans le pire des quas le nombre d'étape nécessaires pour obtenir une réponse de la fonction est_ dans(x, L) est du nombre d'élément dans la liste -1 (soit moins sa tête)"
    # Erreur : dans le pire cas, il faut examiner tous les éléments, pas n - 1.
        
"""

def est_dans(x, L):
    if est_vide(L):
        return False
    else : 
        if x== tete(L) : 
            return True 
        else :
            return False or est_dans(x, queue(L))


"""
Correction commentée
====================

La fonction est_dans commence par tester si la liste est vide. Si c'est le
cas, x n'est pas dans la liste et la fonction renvoie False. Sinon, elle
compare x avec la tête. Si les deux valeurs sont égales, elle renvoie True.
Sinon, elle recommence la recherche dans la queue de la liste.

Dans le pire des cas, x n'est pas dans la liste ou se trouve en dernière
position. La fonction doit alors comparer x avec les n éléments de la liste.
Le nombre de comparaisons est donc n, où n est le nombre d'éléments.
Si l'on compte aussi le dernier appel qui rencontre la liste vide, il y a
n + 1 appels récursifs.
"""


def est_dans_corrige(x, L):  # Retourne True si x appartient à L, sinon False.
    if est_vide(L):  # Une liste vide ne contient aucun élément.
        return False
    if x == tete(L):  # Vérifie si x est l'élément situé en tête.
        return True
    return est_dans_corrige(x, queue(L))  # Continue la recherche dans la queue.


"""
Correction du cours - Exercice 5
================================

La fonction nombre_element peut être écrite de manière récursive. Le nombre
d'éléments d'une liste non vide est égal à 1 plus le nombre d'éléments de sa
queue. Une liste vide contient zéro élément.

Pour accéder à l'élément de rang i, il faut parcourir la queue i fois. Il
faut donc i étapes pour atteindre l'élément de rang i.

La fonction est_dans procède également de manière récursive. Si la liste est
vide, la réponse est False. Sinon, la fonction compare x avec la tête de la
liste. Si x et la tête sont identiques, elle retourne True. Sinon, elle
continue la recherche dans la queue de la liste.

Dans le pire des cas, x est le dernier élément ou n'appartient pas à une
liste de n éléments. La fonction compare alors x avec les n éléments. Il faut
donc n comparaisons, ou n + 1 appels récursifs si l'on compte l'appel final
sur la liste vide.
"""


        
