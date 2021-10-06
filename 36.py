n=int(input("podaj liczbę n "))
l=[0,1]
if n>2:
    for i in range(2,n):
        v=l[i-1] + l[i-2]
        l.append(v)
print(l)
