import math
n=int(input("podaj liczbę n "))
suma=int(0)
p=int(math.sqrt(n))

p1=int(n/p)

while p>1:

    if n%p==0:
        suma+=p
    else:
        p-=1
        if p1!=p:
            print("p1!=p")
            suma+=p1
            p-=1
        else:
            p-=1


else:
    suma+=1
        if suma==n:
            print("tak")
        else:
             print("nie")