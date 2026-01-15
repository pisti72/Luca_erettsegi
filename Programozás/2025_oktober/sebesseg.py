print("3. Sebességes feladat")
print("1. feladat")
f = open("ut.txt")
össz_hossz = f.readline()
print("Teljes útszakasz:", össz_hossz, type(össz_hossz))

útszakasz = []
for sor in f:
  adatok = sor.split()
  rekord = {
    "km":   adatok[0],
    "adat": adatok[1]
  }
  útszakasz.append(rekord)

print("2. feladat")
print("A települések neve:")
for sor in útszakasz:
  if len(sor["adat"])>=4:
    print(sor["adat"])

print("3. feladat")
vizsgált = input("Adja meg a vizsgált szakasz hosszát km-ben! ")










