"""
Les donnees : elements de l'ensemble V.

Operations primitives :

- creer_graphe() : cree un graphe vide ;
- est_dans(G, v) : indique si v est un sommet du graphe G ;
- ajouter_sommet(G, v) : ajoute le sommet v au graphe G ;
- supprimer_sommet(G, v) : supprime le sommet v du graphe G ;
- ajouter_arc(G, v1, v2) : ajoute un arc de v1 vers v2 ;
- supprimer_arc(G, v1, v2) : supprime l'arc de v1 vers v2 ;
- voisins(G, v) : retourne les sommets adjacents a v ;
- successeurs(G, v) : retourne les extremites terminales des arcs partant de v.
"""


"""
Implementation A : les sommets sont les cles d'un dictionnaire et chaque
sommet est associe a une liste de couples (sommet voisin, poids).

Exemple : un graphe de transport non oriente et pondere.
"""
transport = {
    'Paris': [('Strasbourg', 490), ('Brest', 592), ('Lyon', 546)],
    'Brest': [('Paris', 592), ('Nantes', 295)],
    'Nantes': [('Brest', 295)],
    'Lyon': [('Paris', 546)],
    'Strasbourg': [('Paris', 490)],
}

"""Un graphe dont les aretes portent des coefficients est un graphe pondere.
Dans cette representation, voici deux operations primitives."""

def est_dans(G, v):
    """Indique si v est un sommet de G."""
    return v in G

def voisins(G, v):
    """Retourne les sommets voisins de v, sans leurs poids."""
    if not est_dans(G, v):
        return []
    return [sommet for sommet, poids in G[v]]

"""Si l'on souhaite conserver les poids, on utilise cette variante."""

def voisins_avec_poids(G, v):
    """Retourne les couples (sommet voisin, poids) de v."""
    if not est_dans(G, v):
        return []
    return G[v]


# Exercice 1 : liste des successeurs d'un graphe oriente.

"""Graphe = {
    '1': ['2', '5', '8'],
    '2': ['3'],
    '3': ['1', '4'],
    '4': ['8'],
    '5': ['6'],
    '6': [],
    '7': ['6'],
    '8': ['7'],
}"""

# Correction :

graphe = {
    '1': ['2', '5', '8'],
    '2': ['3'],
    '3': ['1', '4'],
    '4': ['8'],
    '5': ['6'],
    '6': [],
    '7': ['6'],
    '8': ['7'],
}



"""Matrice d'adjacence : un tableau de tableaux, comme etudie en premiere.
Ici, graph_proba est une matrice de probabilites ; ses valeurs non nulles
indiquent les arcs du graphe."""

graph_proba=[[0.1,0.5,0.4],[0,0.35,0.65],[0.8,0,0.2]]


"""Passage d'une representation a une autre pour un graphe oriente."""

def matrice_vers_listes_succ(matrice):
    """Transforme une matrice d'adjacence en listes de successeurs."""
    listes_succ = {i: [] for i in range(len(matrice))}

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] != 0:
                listes_succ[i].append(j)

    return listes_succ

def listes_succ_to_matrice(listes_succ):
    """Transforme des listes de successeurs en matrice d'adjacence.

    Les sommets doivent etre numerotes de 0 a n - 1.
    """
    n = len(listes_succ)
    matrice = [[0] * n for _ in range(n)]
    for i in listes_succ:
        for j in listes_succ[i]:
            matrice[i][j] = 1
    return matrice