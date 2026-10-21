Cahier des charges : 

1. Entrée du programme
Une ligne de calcul contenant des nombres entiers ou réels, les opérations classiques et des parenthèses pour
gérer la priorité des calculs. Aucun espace ne doit être présent, les seuls caractères utilisés devront être les
suivants : 

Opérateurs autorisés (dans l’ordre croissant de priorité) :
+ pour l’addition
- pour la soustraction
* pour la multiplication
/ pour la division
^ pour la puissance 

Symboles utilisés :
( pour ouvrir une parenthèse
) pour fermer une parenthèse
. pour écrire des nombres décimaux (pas de virgules en programmation !!)
0, 1, 2, 3, 4, 5, 6, 7, 8, 9 pour construire des nombre 

Exemples :
1.789^(3-2)+7-(3+(6*7-1))
3*(1-7-(3+7-6)^(1*9-7))*3+7*49/1.2-35984*5695*(6-7*98*(1-12))
Si un autre symbole est présent, le programme créera une erreur d'exécution.
Si une parenthèse ouverte n’est pas fermée, le programme créera une erreur d'exécution.
Si un nombre décimal utilise une virgule et non un point, le programme créera une erreur d'exécution.

2. Sortie du programme
Le résultat du calcul, ni plus ni moins.
Exemple 1:
1.789^(3-2)+7-(3+(6*7-1)) donne la sortie -35.211
Exemple 2:
3*(1-7-(3+7-6)^(1*9-7))*3+7*49/1.2-35984*5695*(6-7*98*(1-12)) donne la sortie - 1547622901384.1667 


#Les outils dont vous aurez besoin 


Fonctions nécessaires : 

is_number(s)
>> Fonction qui sera donnée, elle renvoie True si la chaîne de caractère donnée en argument correspond à un
nombre et False sinon

nettoyer(expression)
>> Son but est d’enlever les parenthèses extérieures inutiles
>> “((((3+7)))” devient ainsi “3+7”
>> “3+((7))” reste “3+((7))” car les parenthèses ne sont pas extérieures

decoupage_selon_operateur(expression, operateur)
>> On lui donne un opérateur et une expression mathématique et elle découpe l’expression en deux sous-
expressions de part et d'autre de l’opérateur
>> Si on appelle la fonction avec l’expression “3+7*8” et l’opérateur “+”, elle renvoie [“3”,”7*8”,”+”]
>> Si on appelle la fonction avec l’expression “3+7*8” et l’opérateur “*”, elle renvoie [“3+7”,”8”,”*”] 

decoupage(expression)
>> Elle réalise le découpage complet et renvoie l’expression formatée correspondante en respectant les
prioritées de calcul
>> Pour l’expression “3+7*8” elle renvoie donc [[3.0, None, 'num'], [[7.0, None, 'num'], [8.0, None, 'num'],'*'], '+']
>> Cette fonction est récursive 

calculer
(expression_formatee)
>> A partir d’une expression formatée elle donne récursivement le résultat

raise Exception("Aucun operateur trouve, ERREUR SYNTAX") #Si on demande à notre programme de chercher un “+” dans l’expression mais qu’il n’y en a pas.
raise Exception("Operateur inconnu, ERREUR SYNTAX") #Si notre programme rencontre un opérateur inconnu ou qu’il y a un problème de parenthèses. 



    
