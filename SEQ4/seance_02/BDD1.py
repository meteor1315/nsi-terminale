import sqlite3

bdd = sqlite3.connect("ma_bdd.db") #Création du fichier de base de donnée
requete = bdd.cursor() #Création d'un 'curseur' qui permet d'écrire des requètes
# Création de la table LIVRES avec les informations de chaque livre.
requete.execute("""
CREATE TABLE LIVRES (
    id INTEGER,
    titre TEXT,
    auteur TEXT,
    ann_publi INTEGER,
    note INTEGER)
    """) #La requète que l'on veut éxecuter
bdd.commit() #On valide dans le fichier de la bdd la requète.

# Ajout de plusieurs livres dans la table LIVRES.
requete.execute("""
INSERT INTO LIVRES(id,titre,auteur,ann_publi,note) 
VALUES
(1,'1984','Orwell',1949,10),
(2,'Dune','Herbert',1965,8),
(3,'Fondation','Asimov',1951,9),
(4,'Le meilleur des mondes','Huxley',1931,7),
(5,'Fahrenheit 451','Bradbury',1953,7),
(6,'Ubik','K. Dick',1969,9),
(7,'Chroniques martiennes','Bradbury',1950,8),
(8,'La nuit des temps','Barjavel',1968,7),
(9,'Blade Runner','K. Dick',1968,8),
(10,'Les robots','Asimov',1950,9),
(11,'La planète des singes','Boulle',1963,8),
(12,'Ravage','Barjavel',1943,8),
(13,'Le Maître du Haut Château','K. Dick',1962,8)
    """)
bdd.commit() #On valide dans le fichier de la bdd la requète.   


# Modification de la note du livre « 1984 ».
requete.execute(""" UPDATE LIVRES SET note=5 WHERE titre="1984" """)

# Modification du titre et de l'auteur du livre dont l'identifiant est 9.
requete.execute(""" UPDATE LIVRES SET titre ="Blade runner" AND auteur="Dick" WHERE id=9""")

# Sélection des titres des livres dont la note est supérieure à 7.
requete.execute(""" SELECT titre FROM LIVRES WHERE note>7""") 

# Sélection des titres notés entre 7 et 8, classés par ordre alphabétique.
requete.execute(""" SELECT titre FROM LIVRES WHERE note>=7 AND note <=8 ORDER BY titre""") 

# Suppression des livres écrits par Orwell.
requete.execute(""" DELETE FROM LIVRES WHERE auteur="Orwell" """)