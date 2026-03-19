# Könyvek feladat megoldása
#
ÉV = 0
NEGYED = 1
EREDET = 2
LEIRAS = 3
PELDANYSZAM = 4

konyvek = []
fajl = open("kiadas.txt",encoding="UTF-8" )
for s in fajl:
    sor = s.strip().split(";")
    konyvek.append(sor)

print("Összesen ennyi könyven van:", len(konyvek))

i = 0
for konyv in konyvek:
    print(konyv[LEIRAS])
    if i%5 == 0:
        print("----------------------",i)
    i += 1

print("2. feladat")
szerző = input("Szerző: ")
darab = 0
for konyv in konyvek:
    if szerző in konyv[LEIRAS]:
        darab += 1
if darab > 0:
    print(darab,"könyvkiadás")
else:
    print("Nem adtak ki")

print("3. feladat")
legnagyobb = 0
hányszor = 0
for konyv in konyvek:
    legnagyobb = max(legnagyobb, int(konyv[PELDANYSZAM]))
for konyv in konyvek:
    if int(konyv[PELDANYSZAM]) == legnagyobb:
        hányszor += 1
print("Legnagyobb példányszám:",legnagyobb,"előfordult",hányszor,"alkalommal.")

print("4. feladat [LUCA megcsinálja]")
