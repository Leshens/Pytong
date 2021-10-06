a=int(input("podaj pierwszą liczbę"))
b=int(input("podaj drugą liczbę"))

while a<=20:
    if b<=20:
        if a==b:
            print(2*a)
            break
        else:
            a = int(input("podaj pierwszą liczbę"))
            b = int(input("podaj drugą liczbę"))

    else:
        print("podaj liczbę z przedziału  0-20")
        break
