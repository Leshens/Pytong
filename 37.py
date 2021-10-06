n=str(input("wpisz słowo "))
n=n.casefold()
m=reversed(n)
if list(n)==list(m):
    print('jest paindromem')
else:
    print('nie jest paindromem')