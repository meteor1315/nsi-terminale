
from collections import deque 
back= deque() #création d'une pile vide
back.appendleft('a')  #empilement par le sommet de 'a'
back.appendleft('b')  #empilement par le sommet de 'b'
back.appendleft('c')  #empilement par le sommet de 'c'
print(back)
top = back.popleft()  #dépilement du sommet et récupération de sa valeur
print(back)
print(top)

