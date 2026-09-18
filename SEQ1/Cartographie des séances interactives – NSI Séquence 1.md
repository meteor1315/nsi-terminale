# Cartographie des séances interactives — NSI Terminale
## Séquence 1 – Structures de données – 1

Source : [Espace de formation CNED, cours 7-NI06, section Séquences](https://eformation.cned.fr/course/view.php?id=12450&section=2)

Cette séquence contient deux séances au format interactif (SCORM) dans la Partie 1 :
- **Séance 1 – Rappels sur les dictionnaires** (26 écrans)
- **Séance 3 – Construction d'un historique à l'aide de piles** (13 écrans)

Les séances 2, 4 et 5 sont des fichiers PDF (non interactifs) et ne sont donc pas détaillées ici.

---

## Séance 1 – Rappels sur les dictionnaires

[Lien direct](https://eformation.cned.fr/mod/scorm/view.php?id=1634460) — Module : *Structures de données : rappels* > *Rappels de Première*

**Résumé de la séance :** les exercices sont partiellement issus des cours de Première ; ils constituent une synthèse des pré-requis à maîtriser pour aborder les structures de données en Terminale.

**Objectif :** réviser les notions de Première concernant les structures de données.

### Sommaire (26 pages)

| # | Titre de l'écran | Contenu clé |
|---|---|---|
| 1 | Introduction | Résumé et objectifs de la séance |
| 2 | I – Les dictionnaires – définition 1 | Le type `dict` en Python : `x = {}`, `type(x)` → `<class 'dict'>`, équivalent `x = dict()` |
| 3 | I – Les dictionnaires – définition 2 | Définition mathématique d'un dictionnaire comme application \(f: A \to B\), exemple avec \(A=\{0,1,\dots,9\}\) et \(f(x)=x^2\) |
| 4 | II – Ajouter des clés et valeurs dans un dictionnaire | Construction pas à pas de `fonction_carree = {}` avec `fonction_carree[0]=0`, etc. ; tableau clé/valeur à compléter |
| 5 | III – Dictionnaire comme banque de mot de passe - 1 | Exercice : compléter `mon_dictionnaire` avec les pseudos/mots de passe (Alain, Bernard, Claude, Didier) puis ajouter l'entrée "Emile" / "5978" |
| 6 | III – Dictionnaire comme banque de mot de passe - 2 | Lecture d'une valeur via sa clé : `print(mon_dictionnaire["Didier"])` → exercice pour afficher le mot de passe d'Alain |
| 7 | IV – Dictionnaire comme tableau de valeurs | Construction du dictionnaire `polynome` pour \(f(n)=n^2+2n-4\), à compléter pour n de 0 à 9 |
| 8 | V – Dictionnaire comme base de données - 1 | Création de `MonDico` (nom → prénom) à partir d'une liste d'élèves, exercice à trous |
| 9 | V – Dictionnaire comme base de données - 2 | Création du dictionnaire `course` (fruit → quantité) : Abricot, Banane, Fraise |
| 10 | V – Dictionnaire comme base de données - 3 | Modification de valeurs existantes : `course["Abricot"] = 10`, puis modifier Banane (5) et Fraise (30) |
| 11 | V – Dictionnaire comme base de données - 4 | Récapitulatif du dictionnaire `course` rempli, introduction à l'idée de boucler sur les valeurs |
| 12 | V – Dictionnaire comme base de données - 5 | Exercice avec boucle `while` pour décrémenter `course["Abricot"]` jusqu'à 0 et compter les itérations (`nA`, résultat attendu = 10) |
| 13 | VI – L'échiquier - 1 | Introduction à un dictionnaire dont les clés sont des tuples de coordonnées (représentation d'un échiquier) |
| 14 | VI – L'échiquier - 2 | Dictionnaire `echiquier` avec clés-tuples `('a',1)`, `('b',1)`, etc. et valeurs (pièces) ; exercice : déplacer le cavalier blanc avec `del` et une nouvelle affectation |
| 15 | Les dictionnaires, rappels - 1 | Définition générale : collection non ordonnée, mutable, indexée ; exemple `famille = {"Père": "Robert", "Mère": "Cersei", ...}` |
| 16 | Les dictionnaires, rappels - 2 | Accès à une valeur par sa clé : `print(famille["Fils"])` |
| 17 | Les dictionnaires, rappels - 3 | Modification d'une valeur : `famille["Père"] = "Jaime"` |
| 18 | La méthode values() | `famille.values()` et boucle `for cle in famille.values(): print(cle)` — parcours des valeurs |
| 19 | La méthode keys() | `famille.keys()` et boucle `for value in famille.keys(): print(value)` — parcours des clés |
| 20 | La méthode items() | `famille.items()` et boucle `for elem in famille.items(): print(elem)` — parcours des couples (clé, valeur) |
| 21 | Exercice 1 - 1 | Créer un dictionnaire en compréhension pour \(f(x)=x^2+4x-1\), x de -5 à 2 |
| 22 | Exercice 1 - 2 | Afficher séparément les valeurs de x (clés) puis de f(x) (valeurs) du dictionnaire précédent |
| 23 | Exercice 1 - 3 | Calculer la somme des abscisses (`somme_x`) et la somme des ordonnées (`somme_y`) |
| 24 | Exercice 1 - 4 | Calculer `somme_z` = numérateur de la moyenne pondérée \( \sum (x \times f(x)) \) |
| 25 | Exercice 1 - 5 | Calcul final de la moyenne : `moyenne = round(somme_z / somme_x, 2)` |
| 26 | Synthèse | Écran de fin : "Ces exercices de révision sont à présent terminés." |

---

## Séance 3 – Construction d'un historique à l'aide de piles

[Lien direct](https://eformation.cned.fr/mod/scorm/view.php?id=1634462) — Module : *Structures de données* > *Construction d'un historique*

**Résumé de la séance :** les navigateurs web permettent de « reculer d'une page » ou « avancer d'une page ». La séance guide vers l'écriture d'un programme simulant ce comportement à l'aide de piles. Un éditeur de code est nécessaire tout au long de la séance.

**Objectif :** réaliser un programme simulant le déplacement dans l'historique récent d'un navigateur à l'aide de piles.

### Sommaire (13 pages)

| # | Titre de l'écran | Contenu clé |
|---|---|---|
| 1 | Introduction | Résumé et objectifs de la séance |
| 2 | Quelques explications et une illustration (1/4) | Icônes « reculer »/« avancer » et barre d'adresse d'un navigateur (illustration Firefox) |
| 3 | Quelques explications et une illustration (2/4) | Modélisation : une pile `back` (pages précédentes), une pile `forward` (pages suivantes), une variable `current` (adresse en cours) |
| 4 | Quelques explications et une illustration (3/4) | Exemple d'état à un instant t : page actuelle « url_F », précédente « url_D3 » (sommet de `back`), suivante « url_Z » (sommet de `forward`) |
| 5 | Quelques explications et une illustration (4/4) | Effet du clic sur « reculer » : `url_F` empilé dans `forward`, `url_D3` dépilé de `back`, `current` devient `url_D3` |
| 6 | Structures de données et fonctions | Modélisation retenue : dictionnaire `historique` = {pile `back`, chaîne `current`, pile `forward`} ; trois fonctions à écrire : `avancer`, `reculer`, `nouvelle_adresse` |
| 7 | Utilisation de « deque » de la bibliothèque collections | Prise en main de `deque` : `from collections import deque`, `appendleft`, `popleft`, et création avec taille maximale (`maxlen`) |
| 8 | Énoncé du mini-projet : première partie (1/2) | Dictionnaire `historique` fourni en exemple (`back`, `current`, `forward` en `deque`) ; consigne : écrire la fonction `reculer(historique)` en gérant le cas où `back` est vide |
| 9 | Énoncé du mini-projet : première partie (2/2) | Consignes : écrire `avancer` et `nouvelle_url(historique, url)` ; tester avec des séquences d'instructions données ; imaginer des jeux de tests pour les cas de pile vide |
| 10 | Énoncé du mini-projet : seconde partie (1/3) | Constat : chaque onglet de navigateur a son propre historique (illustration Firefox, nouvel onglet) |
| 11 | Énoncé du mini-projet : seconde partie (2/3) | Consigne : créer une classe `Historique` avec attributs `back`, `current`, `forward` et méthodes `__init__`, `reculer`, `avancer`, `nouvelle_url`, `__repr__` |
| 12 | Énoncé du mini-projet : seconde partie (3/3) | Consigne : instancier trois objets `hist_A`, `hist_B`, `hist_C` pour trois onglets et créer un jeu de tests |
| 13 | Synthèse | Écran de fin : "Vous avez réalisé un mini-projet permettant d'appliquer les notions de piles, de dictionnaires et de classes." |

---

## Autres ressources de la séquence (non interactives)

| Ressource | Type | Lien |
|---|---|---|
| Séance 2 – Interface et implémentations | PDF (39,1 Mo) | [Ouvrir](https://eformation.cned.fr/mod/resource/view.php?id=1634461) |
| Séance 4 – Structures de données hiérarchiques : les arbres | PDF (876,6 ko) | [Ouvrir](https://eformation.cned.fr/mod/resource/view.php?id=1634464) |
| Séance 5 – Structures de données relationnelles : les graphes | PDF (3,5 Mo) | [Ouvrir](https://eformation.cned.fr/mod/resource/view.php?id=1634465) |
| Séance 6 – Entraînement au bac | PDF (1 Mo) | [Ouvrir](https://eformation.cned.fr/mod/resource/view.php?id=1634467) |
| Fiche de synthèse de la séquence | PDF (58 ko) | [Ouvrir](https://eformation.cned.fr/mod/resource/view.php?id=1634469) |
