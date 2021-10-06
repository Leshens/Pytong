n=int(input("podaj liczbę"))
d=1
for d in range(1,n+1):
    if n%d == 0:
        print(d)
