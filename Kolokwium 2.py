import random
n=random.randint(1,20)
for x in range  (n):
    x = int(input("podaj liczbę "))
    if x<n:
        print("za mało")
    elif x>n:
        print("za dużo")
else:
    print("zgadłeś")