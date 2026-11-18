import sqlite3
bdd = sqlite3.connect("ma_bdd.db") 
requete = bdd.cursor() #Création d'un 'curseur' qui permet d'écrire des requètes
requete.executescript("""
DROP TABLE IF EXISTS AUTEURS;
CREATE TABLE AUTEURS
(id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, ann_naissance INTEGER, langue_ecriture TEXT);
INSERT INTO AUTEURS
(id, nom, prenom, ann_naissance, langue_ecriture)
VALUES
(1, 'Orwell', 'George', '1903', 'anglais'),
(2, 'Herbert', 'Franck', '1920', 'anglais'),
(3, 'Asimov', 'Isaac', '1920', 'anglais'),
(4, 'Huxley', 'Aldous', '1894', 'anglais'),
(5, 'Bradbury', 'Ray', 1920, 'anglais'),
(6, 'K.Dick', 'Philip', '1928', 'anglais'),
(7, 'Barjavel', 'René', '1911', 'français'),
(8, 'Boulle', 'Pierre', '1912', 'français'),
(9, 'Van Vogt', 'Alfred Elton', '1912', 'anglais'),
(10, 'Verne', 'Jules', '1828', 'français') ;
   """)
bdd.commit() #On valide dans le fichier de la bdd la requète 


requete.executescript(""" 
DROP TABLE IF EXISTS LIVRES;
CREATE TABLE LIVRES
(id INTEGER PRIMARY KEY, titre TEXT, id_auteur INTEGER, ann_publi INTEGER, note INTEGER);
INSERT INTO LIVRES
(id, titre,id_auteur, ann_publi,note)
VALUES
(1, '1984',1,1949,10),
(2, 'Dune',2, 1965,8),
(3, 'Fondation',3,1951,9),
(4, 'Le meilleur des mondes',4,1931,7),
(5, 'Fahrenheit 451',5,1953,7),
(6, 'Ubik',6,1969,9),
(7, 'Chroniques martiennes',5,1950,8),
(8, 'La nuit des temps',7,1968,7),
(9, 'Blade Runner',6,1968,8),
(10, 'Les Robots',3,1950,9),
(11, 'La Planète des singes', 8, 1963,8),
(12, 'Ravage',7,1943,8),
(13, 'Le Maître du Haut Château',6,1962,8), (14, 'Le monde des Ā',9,1945,7),
(15, 'La Fin de l éternité',3,1955,8),
(16, 'De la Terre à la Lune',10,1865,10);                
                """) 
bdd.commit() 

# A : jointure interne entre LIVRES et AUTEURS.
# Seuls les livres ayant un auteur correspondant sont conservés.
# La condition ON relie LIVRES.id_auteur à AUTEURS.id.
retour1 = requete.execute("""
SELECT nom, titre
FROM LIVRES
INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id
""") #On écrit le contenu de notre requête
resultat1 = retour1.fetchall() #Vu que notre requête est une selection,
#on peut récuperer le resultat avec la methode fetchall sous forme d'un tableau de tuples
print("A:",resultat1) 

# B : la même jointure interne, avec toutes les colonnes des deux tables.
# L'écriture INNER JOIN est explicite : les lignes sans correspondance sont exclues.
retour2 = requete.execute(""" 
SELECT * 
FROM LIVRES 
INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id             
                      """)
resultat2 = retour2.fetchall() 
print("B:",resultat2) 

# C : nouvelle jointure interne identique à B.
# Elle permet de réunir les informations d'un livre et de son auteur sur une ligne.
retour3 = requete.execute(""" 
SELECT * 
FROM LIVRES 
INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id             
                      """)
resultat3 = retour3.fetchall() 
print("C:",resultat3) 

# D : jointure interne avec sélection de colonnes précises.
# Après la jointure, WHERE conserve seulement les livres publiés après 1950.
retour4 = requete.execute(""" 
SELECT titre, nom, prenom  
FROM LIVRES 
INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id
WHERE LIVRES.ann_publi > 1950
                      """)
resultat4 = retour4.fetchall() 
print("D:",resultat4)



bdd.close()      
