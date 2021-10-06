
def fun():
    n = int(input("podaj liczbe n "))
    x = 1
    suma = 0
    while x<=n:
        if x%2==0:
            suma -= x
            x += 1
        else:
            suma += x
            x += 1
    print(suma)
fun()


