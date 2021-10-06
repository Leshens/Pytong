import random
a = int(input("podaj liczbę a listy "))
b = int(input("podaj liczbe b listy "))
n=20
L = []
for i in range(n):
    L =L + [random.randint(a,b)]
print(L)
suma=0
l1=L[0]
l2=L[0]
for j in range (0,n-1):
    if suma < L[j] + L[j+1]:
        suma = L[j] + L[j+1]
        l1=L[j]
        l2=L[j+1]
print(suma)
print(l1," ",l2)