# Seance 02 : piles et files

## Pile

Une pile suit le principe **LIFO** (*Last In, First Out*) : le dernier element ajoute est le premier retire.

Operations principales :

- `empiler` : ajouter un element ;
- `sommet_pile` : consulter le sommet ;
- `depiler` : retirer le sommet.

## File

Une file suit le principe **FIFO** (*First In, First Out*) : le premier element ajoute est le premier retire.

Operations principales :

- `ajouter_file` : ajouter un element en queue ;
- `premier_file` : consulter la tete ;
- `retirer_file` : retirer l'element en tete.

Le module `collections.deque` fournit une implementation pratique avec `append` et `popleft`.
