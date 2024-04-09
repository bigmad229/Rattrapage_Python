#BANKOLE Nathanaël, Master 1 IA
from collections import UserString

class Mystring(UserString):
    def head(self, n=1):
        # Renvoie les n premières lettres
        return self.data[:n]

    def tail(self, n=1):
        # Renvoie les n dernières lettres
        return self.data[-n:]
    
    def to_upper(self):
        # Met tout en majuscule
        return self.data.upper()
    
    def capitalize_first(self):
        # Met la première lettre en majuscule et le reste en minuscules
        return self.data.capitalize()

ms = Mystring("prepa big data")
print(ms.data)  # affiche: prepa big data
print(ms.head())  # affiche: p
print(ms.head(2))  # affiche: pr
print(ms.tail())  # affiche: a
print(ms.tail(3))  # affiche: ata
print(ms.to_upper())
print(ms.capitalize_first())