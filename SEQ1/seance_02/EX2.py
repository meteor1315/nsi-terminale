LEN_FILE = 10     #tableau de longueur LEN_FILE (ici LEN_FILE = 10), 
                #on convient que le caractère ‘_’ «du bas » correspond à vide


def creer_file():
    return {"tableau": ['_'] * LEN_FILE,
            "position_tete": 0,         #entier compris entre 0 et LEN_FILE représentant la position de la tête de la file
            "nombre_elements": 0}       #entier compris entre 0 et LEN_FILE représentant le nombre d’éléments présents dans la file. 


def est_file_vide(file):
    return file["nombre_elements"] == 0

def premier_file(file):
    if est_file_vide(file):
        return None
    else:
        return file["tableau"][file["position_tete"]]
    

def retirer_file(file): 
    if premier_file(file): 
       
    else:  
        return None


