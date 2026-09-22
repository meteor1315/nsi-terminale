from collections import deque

class Historique:
    def __init__(self):
        self.back = deque()
        self.current = ""
        self.forward = deque()

    def reculer(self):
        if self.back:
            self.forward.appendleft(self.current)
            self.current = self.back.popleft()

    def avancer(self):
        if self.forward:
            self.back.appendleft(self.current)
            self.current = self.forward.popleft()

    def nouvelle_url(self, nouvelle_url):
        self.back.appendleft(self.current)
        self.current = nouvelle_url
        self.forward.clear()

    def __repr__(self):
        return f"Back: {list(self.back)}, Current: {self.current}, Forward: {list(self.forward)}"

# Créer les objets historique pour chaque onglet
hist_A = Historique()
hist_B = Historique()
hist_C = Historique()

# Instructions pour l'onglet A
print("\nOnglet A :")
hist_A.nouvelle_url('url_A1')
hist_A.avancer()
hist_A.nouvelle_url('url_A2')
print(hist_A)

# Instructions pour l'onglet B
print("\nOnglet B :")
hist_B.nouvelle_url('url_B1')
hist_B.nouvelle_url('url_B2')
hist_B.nouvelle_url('url_B3')
hist_B.nouvelle_url('url_B4')
hist_B.reculer()
hist_B.reculer()
print(hist_B)

# Instructions pour l'onglet C
print("\nOnglet C :")
hist_C.nouvelle_url('url_C1')
hist_C.avancer()
hist_C.avancer()
hist_C.reculer()
hist_C.nouvelle_url('url_C2')
print(hist_C)
