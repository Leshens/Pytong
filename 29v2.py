x=int(input("podaj liczbę "))
y=0
c=0
o=x
def liczenie(o,y,c):
     while o//y >= 1:
          c += 1
          o -= 10
     if c>0:
          print(c, " nominału",y,"zł")
     return 0

liczenie(o,10,c)
liczenie(o,5,c)
liczenie(o,2,c)
liczenie(o,1,c)