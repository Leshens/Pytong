import math

n = int(input("Podaj liczbę"))
suma = 0
p = int(math.sqrt(n))

while p > 1:
    if n % p == 0:
        suma = suma + p
        p1 = n / p
        if p1 != p:
            suma = suma + p1
    p = p - 1

suma = suma + 1
if suma == n:
    print("Liczba Doskonała")
else:
    print("Liczba nie jest Doskonała")