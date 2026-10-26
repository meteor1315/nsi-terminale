def tet1(liste): 
    listeSdouble=[]
    for i in range (len(liste)): 
        if (liste[i]in listeSdouble)==False:
            listeSdouble.append(liste[i])
        return listeSdouble  
             
"""
On créé une liste vide que l'on va compléter au fur et à mesure.
On parcours la liste "liste". Si l'élément courant n'est pas dans la liste sans double, alors on l'ajoute à la fin. Sinon on ne fait rien.
On continue jusqu'à ce qu'on ait parcouru la liste en entier.
"""

def test2(liste):
    listeSdouble=[]
    for elem in liste :
        if (elem in listeSdouble)==False:   #Cette méthode a l'avantage de ne pas rajouter un compteur. 
            listeSdouble.append(elem)
    return listeSdouble 


""" 
Par soucis de clarté, nous allons également créer une nouvelle fonction uniquement chargée de gérer le cas où l'élément n'est pas dans "listeSdouble".
""" 

liste=[1, 3, 3, 2, 1, 0, 5, 4, 3] 
def ajouter(listeSdouble, elem): 
    listeSdouble.append(elem) 
    return listeSdouble  

def test2_bis(liste):
    listeSdouble=[]
    for elem in liste :
        if (elem in listeSdouble)==False:   #Cette méthode a l'avantage de ne pas rajouter un compteur. 
            listeSdouble.append(elem)
    return listeSdouble 

print(test2_bis(liste)) 
