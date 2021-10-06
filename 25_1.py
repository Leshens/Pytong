n=int(input("podaj liczbę"))
m=1
s=0
while n%m==0:
    s+= m
    m+=1
else:
    m+=1
if s==n:
    print("liczba doskonała")
else:
    print("nie")
