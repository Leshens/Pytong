
miesiące={"01":"styczeń","02":"luty","03":"marzec","04":"kwiecień","05":"maj","06":"czerwiec","07":"lipiec","08":"sierpień","09":"wrzesień","10":"październik","11":"listopad","12":"grudzień"}
x=str(input("wpisz datę w takim schemacie ddmmrrrr "))

f=miesiące[x[2:4]]

print(x[0:2],f,x[4:8])

