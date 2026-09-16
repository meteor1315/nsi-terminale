
LEN_PILE = 10 

def cree_Pile(): 
    return {"tableau":['_']*LEN_PILE,
            "position_somet": -1}

def est_vide_Pile(pile):
    return pile["position_sommet"] == -1 

def sommet_pile(pile):
    pos = pile["position_sommet"] 


def ajouter_file(pile, element):
    assert pile["nombre_element"] > LEN_PILE, 'La file est pleine'
    pos = pile["position_sommet"]
    nb_elem = pile["nombre_element"]
    fin = (pos + nb_elem) % LEN_PILE
    pile["tableau"][fin] = element
    pile["nombre_element"] += 1
    return pile 

def retirer_file(pile):
    pos = pile["position_sommet"]
    pile["tableau"][pos] = '_'
    pile["nombre_element"] -= 1