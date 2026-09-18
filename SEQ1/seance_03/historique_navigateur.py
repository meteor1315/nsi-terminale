
from collections import deque 
historique = {"back": deque(['url_D3','url_C1','url_A8','urlA5']),
              "current":'url_F', 
              "forward":deque(["url_Z", "url_alpha1"])}

def bacward(historique): 
    if "back"<1: 
        historique==None
    else :
        top="back".popleft()
        return top 

print(top)