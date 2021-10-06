n=int(input("podaj liczbę n"))
x=1
y=2
z=1/2

while n>1:
    x+=1
    y+=1
    z+=x/y
    n-=1
print(z)