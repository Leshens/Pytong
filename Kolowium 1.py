a=int(input("Podaj liczbę A "))
b=int(input("Podaj liczbę B "))
c=int(input("Podaj liczbę C "))

if a==c+b:
    print("A=B+C")
elif b==a+c:
    print("B=A+C")
elif c==a+b:
    print("C=A+B")
else:
    print("jedna liczba nie jest sumą pozostałych")