
prenoms=["Emile", "Didier", "Chistophe", "Bob", "Alain"] 
prenoms.sort()
print("Prenoms ordre alpha :", prenoms) 

notes=[5, 10, 12, 18, 20] 
notes.sort()
print("Notes ordre croissant:", notes)




eleves=[['Alains', 5, 10],
        ['Emilie', 15, 8],
        ['Didier', 12, 15],
        ['Christophe', 18, 12],
        ['Bob', 13, 20]]

print("liste de liste :",eleves) 

"""
La liste créée est une liste de liste (ou nested list en anglais)
Chaque sous liste possède 3 valeurs, une de type 'str' et deux de type 'int'.
""" 

eleves.sort()
print("sort: ",eleves) 
print("sorted : ",sorted(eleves))

""" 
eleves.sort() trie la liste en place puis la modifie
sorted(eleves) créé et renvoie une nouvelle liste sans modifier la liste eleves.
"""



eleves_sorted=sorted(eleves ,key=lambda colonnes:colonnes[1]) #ordre croissant 
print(eleves_sorted)

""" 
Le but est de pouvoir trier selon la note 1, c’est-à-dire la colonne 2. Nous allons utiliser une méthode qui utilise la fonction lambda :
Dans eleves_sorted, on met la liste triée (sorted) à partir de la liste "eleves"
Nous allons trier par rapport à une clé de tri qui sera la colonne et nous choisirons la deuxième colonne (indice 1)
""" 

eleves_sorted=sorted(eleves ,key=lambda colonnes:colonnes[1], revers=True) #ordre décroissant 
print(eleves_sorted)
