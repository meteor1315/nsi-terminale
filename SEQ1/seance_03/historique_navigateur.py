from collections import deque 

def reculer(historique):
    if historique["back"]: 
        # Ajouter la page actuelle au début de forward
        
        # Retirer la première page back 
        # et le placer dans current 

     return historique 


""" 
État avant relculer(historique): 

{
    "back": deque(["url_D3", "url_C1", "url_A8", "url_A5"]),
    "current": "url_F",
    "forward": deque(["url_Z", "url_alpha1"])
}

État attendu après relculer(historique):

{
    "back": deque(["url_C1", "url_A8", "url_A5"]),
    "current": "url_D3",
    "forward": deque(["url_F", "url_Z", "url_alpha1"])
}

"""