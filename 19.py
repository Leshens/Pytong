x=int(input("podaj liczbę całkowitą"))
while x<=0:
    print("podałeś liczbę ujemną")
    x = int(input("podaj liczbę całkowitą"))
    if x>=1:
        print(x," jest liczbą dodatnią")