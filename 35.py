liczby = {0:"zero",1:"jeden",2:"dwa",3:"trzy",4:"cztery",5:"pięć",6:"sześć",7:"siedem",8:"osiem",9:"dziewięć" }
x = int(input("podaj liczbę "))
r = list(liczby.keys())
r.sort()
r.reverse()
lr = ""
y = x
def b():
    for i in r:
        while y <= i:
            lr += liczby[i]
            y += i
    print(lr)
    return print()
print(b())