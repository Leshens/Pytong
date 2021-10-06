import random
a = int(input("podaj liczbę a listy "))
b = int(input("podaj liczbe b listy "))
n=20
L = []
for i in range(n):
    L =L + [random.randint(a,b)]
print(L)

x=0
z=0
v=0
c=x+1
while x <= 19:
    z = L[x]
    if z > L[c]:
        if z > v:
            x += 1
            v = z

        else:
            x += 1
    else:
        x += 1
print(v)
