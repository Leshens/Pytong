import random
n=int(input("podaj liczbę n "))
L=[]
K=[]
for i in range (n):
    L=L+[random.randint(1,30)]
print("Lista pierwotna ", L)
K=L
x=1
while x in range (len(L)):

    if [L[x] % 2]==0:
        K.extend(L[x])
        K.extend(0)
        x+=1
    else:
        K.extend(L[x])
print("Lista zmodyfikowana", K)
