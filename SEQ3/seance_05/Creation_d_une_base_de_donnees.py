from pathlib import Path
import sqlite3


chemin_bdd = Path(__file__).resolve().parents[2] / "ma_bdd.db"
bdd = sqlite3.connect(chemin_bdd)
requete = bdd.cursor()
requete.execute("""
CREATE TABLE IF NOT EXISTS LIVRES (
    id INTEGER,
    titre TEXT,
    auteur TEXT,
    ann_publi INTEGER, 
    note INTEGER)                                
""")
bdd.commit()

""" 
Que doit on écrire dans Executer le SQL, pour créer une relation ESSAI ayant pour attributs ?
    - Un identifiant numérique nommé id
    - Une année nommé annee
    - Un nom nommé nom
"""

requete.execute("""
CREATE TABLE IF NOT EXISTS ESSAI (
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
CREATE TABLE IF NOT EXISTS AUTEURS  (
    id INT PRIMARY KEY, 
    nom TEXT NOT NULL CHECK (length(nom) BETWEEN 1 AND 25), 
    prenom TEXT CHECK (length(prenom) <= 10))
""")   
bdd.commit()

""" 
On désire créer une base de données nommée BASE2. Puis on souhaite créer une relation NOTES d’attributs :

    - Matière nommé mat qui est une chaîne d’au plus 15 caractères et non vide
    - Note nommé note qui est un réel non vide
    - Identifiant nommé id qui est un entier, non vide et clé primaire.
"""  
requete.execute("""
CREATE TABLE IF NOT EXISTS NOTES (
    mat TEXT NOT NULL CHECK (length(mat) BETWEEN 1 AND 15),
    note REAL NOT NULL,
    id INTEGER NOT NULL PRIMARY KEY)
""")  
bdd.commit()
bdd.close()
