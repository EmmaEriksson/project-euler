summa = 0
fib = 1
fib_old = 0
tmp = 0

while fib < 4000000:
    
    if fib%2 == 0:
        summa += fib 
    
    tmp = fib
    fib = fib + fib_old 
    fib_old = tmp

print(summa)

