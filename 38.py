x =(input("wpisz słowo "))
lit= {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'a':0,'s':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0,'ą':0,'ę':0,'ó':0,'ś':0,'ł':0,'ż':0,'ź':0,'ć:0','ń':0, }:
litery = {}

for y in x:
    if y in litery:
        litery[y] += 1
    else:
        litery[y] = 1

print(litery)

