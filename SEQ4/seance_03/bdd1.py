import sqlite3

bdd = sqlite3.connect("bdd1-S3.db") #Création du fichier de base de donnée
requete = bdd.cursor() #Création d'un 'curseur' qui permet d'écrire des requètes


#A.1:
requete.execute("""CREATE TABLE IF NOT EXISTS TAB1 (
    Att1 TEXT PRIMARY KEY,
    Att2 INTEGER)
    """) 
bdd.commit()  

#A.2: 
requete.execute("""INSERT INTO TAB1  (Att1, Att2) VALUES ('CODD',1974)""") 
bdd.commit()