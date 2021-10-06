import random
n = int(input("podaj liczbę wierszy "))
m = int(input("podaj liczbę kolumn "))
M=[]
s=0
def macież():
    M = [[0]*m for i in range(n)]
    return M
M = macież()
N = M
def tworzenie():
    for i in range(n):
        for j in range(m):
            M[i][j] = random.randint(0,9)
            print(M[i][j], "", end="")
        print()
    return print()
tworzenie()
for i in range(0,n):
   for j in range(0,m):
       if M[i][j] <= 5:
           s += M[i][j]
print(s)
