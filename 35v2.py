liczby = {'0':"zero",'1':"jeden",'2':"dwa",'3':"trzy",'4':"cztery",'5':"pięć",'6':"sześć",'7':"siedem",'8':"osiem",'9':"dziewięć", '-':"minus" }
x = str(input("podaj liczbę "))
for y in range(len(x)):
    if str(x[y]) in liczby.keys():
        print(liczby[str(x[y])])