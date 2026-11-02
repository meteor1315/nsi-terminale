import sqlite3 
bdd = sqlite3.connect("ma_bdd.db") #création du fichier de base de données
requete = bdd.cursor() #création d'un 'curseur' qui permet d'écrire des requêtes
requete.execute("""
CREATE TABLE LIVRES (
    id INTEGER,
    titre TEXT,
    auteur TEXT,
    ann_publi INTEGER, 
    note INTEGER)                                
""") #la requête que l'on veut exécuter
bdd.commit() #on valide dans le fichier de la BDD, la requête.

""" 
Que doit on écrire dans Executer le SQL, pour créer une relation ESSAI ayant pour attributs ?
    - Un identifiant numérique nommé id
    - Une année nommé annee
    - Un nom nommé nom
"""

requete.execute("""
CREATE TABLE ESSAI (
    id INTEGER,
    annee INTEGER,
    nom TEXT)                                
""") 
bdd.commit() 

""" 
On désire créer une relation AUTEURS ayant pour attributs :

    - Un identifiant numérique entier nommé id
    - Un nom d’au plus 25 caractères et non vide nommé nom
    - Un prénom d’au plus 10 caractères nommé prenom
    - La clé primaire sera id.
""" 

requete.execute("""
CREATE TABLE AUTEURS  (
    id INT PRIMARY KEY, 
    nom CHAR(25) NOT NULL, 
    prenom CHAR(10))
""")   

""" 
On désire créer une base de données nommée BASE2. Puis on souhaite créer une relation NOTES d’attributs :

    - Matière nommé mat qui est une chaîne d’au plus 15 caractères et non vide
    - Note nommé note qui est un réel non vide
    - Identifiant nommé id qui est un entier, non vide et clé primaire.
"""  
requete.execute(""" 
CREATE DATABASE BASE2
CREATE TABLE Notes  (
    mat CHAR(15) NOY NULL, 
    note REAL NOT NULL, 
    id INTEGER NOT NULL PRIMARY KEY)
""")  
