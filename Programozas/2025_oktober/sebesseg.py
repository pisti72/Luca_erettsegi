print("3. Sebességes feladat")
print("1. feladat")
f = open("ut.txt")
össz_hossz = float(f.readline())
print("Teljes útszakasz:", össz_hossz, type(össz_hossz))

útszakasz = []
for sor in f:
  adatok = sor.split()
  rekord = {
    "km":   int(adatok[0]),
    "adat": adatok[1]
  }
  útszakasz.append(rekord)

print()
print("2. feladat")
print("A települések neve:")
for sor in útszakasz:
  if len(sor["adat"]) >= 4:
    print(sor["adat"])

print()
print("3. feladat")
# vizsgált = float(input("Adja meg a vizsgált szakasz hosszát km-ben! ")) * 1000
vizsgált = 1.8
minimum = 9999
for sor in útszakasz:
    if sor["km"] > vizsgált:
        break
    # print(sor["km"], "-->", sor["adat"])
    if len(sor["adat"]) == 2:
        minimum = min(int(sor["adat"]), minimum)
    if len(sor["adat"]) >= 4:
        minimum = min(50, minimum)
print(f"Az első {vizsgált/1000} km-en {minimum} km/h volt a legalacsonyabb megengedett sebesség.")

print()
print("4. feladat")
összeg = 0
város_kezdete = 0
for sor in útszakasz:
    if len(sor["adat"]) >= 4:
        város_kezdete = float(sor["km"])
    if sor["adat"] == "]":
        város_vége = float(sor["km"])
        összeg += (város_vége - város_kezdete)
százalék = (összeg/össz_hossz)*100
print(f"Az út {százalék} százaléka vezet településen belül.")

print()
print("5. feladat")
# település = input("Adja meg egy település nevét! ")
település = "Varos010"
megtaláltuk = False
város_kezdete = 0
városon_belül = 0
darab = 0
for sor in útszakasz:
    if sor["adat"] == település:
        megtaláltuk = True
        város_kezdete = int(sor["km"])
    if megtaláltuk == True :
        if len(sor["adat"]) == 2:
            darab += 1
        if sor["adat"] == "]":
            városon_belül = int(sor["km"]) - város_kezdete
            break
print(f"A sebességkorlátozó táblák száma: {darab}")
print(f"Az út hossza a településen belül {városon_belül} méter.")
print()
print("6. feladat")
aktuális_város = ""
megtaláltuk = False
for sor in útszakasz:
    if len(sor["adat"]) > 3:
        aktuális_város = sor["adat"]
    if sor["adat"] == "]":
        előtte_km = int(sor["km"])
        előtte_város = aktuális_város
    if sor["adat"] == település:
        megtaláltuk = True
        előtte_távolság = int(sor["km"]) - előtte_km
print(előtte_távolság)







