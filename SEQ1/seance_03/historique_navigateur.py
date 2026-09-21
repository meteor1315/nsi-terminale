from collections import deque 

def creer_historique():
    return {
    "back": deque(["url_D3", "url_C1", "url_A8", "url_A5"]),
    "current": "url_F",
    "forward": deque(["url_Z", "url_alpha1"])
    }






def reculer(historique):
    if historique["back"]:
        historique["forward"].appendleft(historique["current"])
        historique["current"] = historique["back"].popleft() 
    
    return historique 


hist = creer_historique()

print("Avant :", hist)
print("Après :", reculer(hist))



"""
Avant :
{
  "back": deque(["url_D3", "url_C1", "url_A8", "url_A5"]),
  "current": "url_F",
  "forward": deque(["url_Z", "url_alpha1"])
}

Après :
{
  "back": deque(["url_C1", "url_A8", "url_A5"]),
  "current": "url_D3",
  "forward": deque(["url_F", "url_Z", "url_alpha1"])
}
"""