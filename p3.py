# Hitta största primtalsfaktorn i 600851475143

from math import sqrt, ceil

talet = 600851475143
rot = sqrt(talet)
primtal = [3, 5, 7, 11, 13, 17] # exkl 2 pga testar bara udda tal
primtalsfaktorer = []

# fixa: for tal = [19:2:ceil(rot)] fast i Python
for tal in range(19, ceil(rot)+1, 2): # räknar igenom alla tal, startar på 19 upp roten av talet
    boo = True
    for p in primtal: # testar mot primtalen upp till sqrt(tal)
        if p > sqrt(tal):
            break
        if tal%p == 0: # delbart, inte ett primtal
            boo = False
            break
    if boo:
        primtal.append(tal) # lägger till primtal i listan
        if talet%tal == 0: # primtalet är en faktor till talet
            primtalsfaktor = tal # sparar endast den största primtalsfaktorn
            primtalsfaktorer.append(tal) # kan spara alla i lista också

print(primtalsfaktor)
print(primtalsfaktorer)
print(talet/primtalsfaktor) # kontroll att det är delbart, ok