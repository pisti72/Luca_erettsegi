print("Hello world")
f = open("ut.txt")
i = 0
ossztáv = f.readline()
lista =  []
for sor in f:
    # print(i, "-->", sor)
    sor_lista = sor.split()
    rekord =  {
        km:  sor_lista[0],
        adat:sor_lista[1]
    }
    lista.append(rekord)
    i += 1
for sor in lista:
    if len(sor["adat"]) > 4:
        print(sor.adat)


