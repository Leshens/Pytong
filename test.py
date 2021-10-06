import random
n = int(input("Podaj liczbę wierszy: "))
m = int(input("Podaj liczbę kolumn: "))
M = [[0] * m for i in range(n)]
s=0
def macierz():
    for i in range(n):
        for j in range(m):
            M[i][j] = random.randint(0, 9)
        print(M[i])
    return print()
macierz()
def wysmacierz():
    for i in range(0,n):
        for j in range(0,n):
            if M[i][j] <= 5:
                s+=M[i][j]
print("Suma liczb mniejszych od 5 jest równa: ", s)