# Största primtalsfaktorn i 600851475143

# Gör en lista av primtalen upp till kvadratroten av talet, 
# testa sedan % av primtalen i listan.
# Hitta primtalen genom att testa om varje tal (starta på 2) 
# är delbart med primtalen innan på listan upp till sqrt av talet som ska testas.
# Om det inte är delbart med någon av de är det ett primtal och läggs till i 
# listan av primtal.

import math
from math import sqrt, ceil

talet = 600851475143
rot = sqrt(talet)
primtal = [3, 5, 7, 11, 13, 17] # inkl inte 2 pga testar bara udda tal

#print(rot)

# hitta primtal
j = 0
boo = True

# fixa: for tal = [19:2:ceil(rot)] fast i Python
for tal in range(19, ceil(rot)): # räknar igenom alla tal, startar på 19 upp roten av talet
    while primtal[j] < sqrt(tal): # testar mot primtalen upp till sqrt(tal)
        if tal%primtal[j] == 0: # delbart, inte ett primtal
            boo = False
        else: 
            if not boo: # om boo redan är F, fortsätter den vara F
                boo = False
            else:
                boo = True 
        j += 1 


# kontrollera primtalsfaktorer i talet
i = 0
while primtal[i] < rot:   
    if talet%primtal[i] == 0: # primtalet är en faktor till talet
        primtalsfaktor = primtal[i] # sparar endast den största primtalsfaktorn
        # kan spara alla i lista också
    i += 1 # öka index med 1
