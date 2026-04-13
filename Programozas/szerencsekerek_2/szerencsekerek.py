from random import randint

file = open("mondasok.txt", encoding = "UTF-8")
mondasok = []
for sor in file:
    mondasok.append(sor.strip())
hanyadik = randint(0, len(mondasok)-1)
mondat = mondasok[hanyadik]
# print(mondat)
kiir = ""
for b in mondat:
    if b == " ":
        kiir += b
    else:
        kiir += "🎁"
print(kiir)
tippek = []
ciklusban_maradok = True
élet = 8
while ciklusban_maradok:
    print("Életek:","❤️"*élet)
    tipp = input("Kérem a tippedet: ")
    tippek.append(tipp)
    print(tippek)
    kiir = ""
    ciklusban_maradok = False
    eltaláltam = False
    for b in mondat:
        if b == " ":
            kiir += b
        elif b.lower() in tippek:
            kiir += b
            if b.lower() == tippek[-1]:
                eltaláltam = True
        else:
            kiir += "🎁"
            ciklusban_maradok = True
    if eltaláltam == False:
        élet -= 1
        if élet == 0:
            ciklusban_maradok = False
    print(kiir.upper())
if élet == 0:
    print("☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️")
    print("☠️☠️☠️ Vesztettél! ☠️☠️☠️")
    print("☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️")
    print(mondat.upper())
else:
    print("Gratulálok! 🏆🏆🏆 Megfejtetted!!!!")






