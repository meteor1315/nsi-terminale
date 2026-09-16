""" Cours Piles Files """ 

#1 implémentation d'une pile LIFO  (Last In First Out) 

pile = ['a','b','c']
print(pile) 
print('ajout nouvel élément')
pile.append('d')# empilage 
print(pile)

while pile: 
    print('dépliage de', pile.pop()) 
    print('pile contient maintenant', pile)
    
#2 implémentation d'une pile FIFO  (First In First Out) 

pile = ['c','b','a']
print(pile) 
print('ajout nouvel élément')
pile.insert(0,'d')# enfilage 
print(pile)

while pile: 
    print('défilage de', pile.pop()) 
    print('pile contient maintenant', pile) 
    
# Implémentation spécialisée 

from collections import deque # le type deque de la bibliothèque implémente les méthode appendleft() et popleft()
#append() <- entrées (enfilage)
#popleft() <- sorties (défilage) 
file_attente=deque((['Alice','Charles']))
print(file_attente)

file_attente.append('Paul') # ajoute à la file d'attente 
print(file_attente)

premier_sorti = file_attente.popleft() # sortie de la file d'attente 
print(premier_sorti)

