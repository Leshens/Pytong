x=int(input("podaj liczbę "))

def liczenie(x):
     b10 = 0
     b5 = 0
     b2 = 0
     b1 = 0
     y=x
     while y//10 >= 1:
          b10 += 1
          y -= 10
     if b10>0:
      print(b10, " banknotów 10zł")
     while y//5 >=1:
          b5+=1
          y-=5
     if b5>0:
          print(b5," monet 5zł")
     while y//2 >=1:
          b2+=1
          y-=2
     if b2>0:
          print(b2," monet 2zł")
     while y//1 >=1:
          b1+=1
          y-=1
     if b1>0:
          print(b1," monet 1zł")