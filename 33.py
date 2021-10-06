import random
def lista():
    n = int(input("podaj wielkość przedziału "))
    L = []
    for i in range(n):
        L = L + [random.randint(1, 50)]
    return L
L = lista()
print("lista pierwotna ", L)
K = L

for x in list(L):
    if 11<=x<=21:
        L.remove(x)


def druk():
    print("lista zmodyfikowana ", L)
druk()