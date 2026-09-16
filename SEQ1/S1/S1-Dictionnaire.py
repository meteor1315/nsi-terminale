#[] #listes 
#{} #dicionnaire 
#() Tuple 


dictionnaire={"test" : "b"}

print(dictionnaire["test"]) 

x=dict() 

x["alix"]="bb" # ajout clef valeur dans un dictionaire 

print(x["alix"]) 



y={} #def dictionaire 

y["alix"]=1   # ajout clef valeur dans un dictionaire  


z={"spagueti" : 4 , "bolognaise":10}  

print(z["spagueti"],z["bolognaise"])

course={}
course["Abricot"]=10
course["Banane"]=3
course["Fraise"]=20

print(course)


course["Banane"]=5
course["Fraise"]=30

print(course)

nA=0
while course["Abricot"]!=0:
  course["Abricot"]-=1
  print("Abricot = ",course["Abricot"]) 
  nA+=1
  print("nA = ",nA)
  
print(nA)	


""" Association clef valeur avec un tuple comme valeur """
echiquier = {}
echiquier[('a', 1)] = "tour blanche"           
echiquier[('b', 1)] = "cavalier blanc" 
echiquier[('c', 1)] = "fou blanc" 
echiquier[('d', 1)] = "reine blanche" 
echiquier[('a', 2)] = "pion blanc" 
echiquier[('b', 2)] = "pion blanc"

print(echiquier)

del echiquier[('b', 1)]

print(echiquier) 


echiquier[('c', 3)] = "cavalier blanc" 


print(echiquier)

print(echiquier.values()) 
print(echiquier.keys()) 

for cle in echiquier.values():
   print(cle)

print(echiquier.items())

for element in echiquier.items():
    print(element) 
    




""" Créer la somme des abscisses et la somme des ordonnées :
dico={x:x**2+4*x-1 for x in range ( -5, 3)}

somme_x=0
for cle in dico.keys():
    somme_x=x+x
print(dico[x]) 
   
somme_y=0

for cle in dico.keys():
    somme_y=y+y
print(dico[y])  """ 

"""Corection :
Créer la somme des abscisses et la somme des ordonnées : """

dico={x:x**2+4*x-1 for x in range ( -5, 3)}

somme_x=0
for cle in dico.keys():
    somme_x=somme_x+cle 
print("somme des abscisses =",somme_x) 
   
somme_y=0
for valeur in dico.values():
    somme_y=somme_y+valeur
print("somme des ordonnées =",somme_y) 

"""calculer la moyenne""" 


dico={x:x**2+4*x-1 for x in range ( -5, 3)}

somme_x=0
for value in dico.keys():
    somme_x=somme_x+value  

somme_z=0
 
"""for elem in dico.values():
    somme_z=somme_z+elem[0]*elem[1] """

for elem in dico.items():
    somme_z=somme_z+elem[0]*elem[1]
print("valeur moyenne=", somme_z) 

moyenne=round(somme_z/somme_x,2) 
print("moyenne=", moyenne)





