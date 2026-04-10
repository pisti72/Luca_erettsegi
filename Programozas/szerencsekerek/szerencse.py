from random import randint 

file = open("100_mondas.txt", encoding="UTF-8")
sorok = []
for sor in file:
    sorok.append(sor.strip())

mondat = sorok[randint(0,len(sorok))]
tippek = []
élet = 5
def megfejtes():
    kiir = ""
    eltalalta = False
    done = True
    for b in mondat:
        if b == " ":
            kiir += " "
        elif b.lower() in tippek:
            kiir += b
            if b.lower() == tippek[-1]:
                eltalalta = True
        else:
            kiir += "#"
            done = False
    print(kiir.upper())
    return [done, eltalalta]
megfejtes()
while True:
    print("Életek:",élet)
    tipp = input("Kérem a tippedet! ")
    tippek.append(tipp.lower()[0])
    result = megfejtes()
    if result[0]:
        break
    if not result[1]:
        élet -= 1
        if élet == 0:
            break
if élet == 0:
    print("EZ MOST NEM SIKERŰLT!!! 😳")
    print(mondat.upper())
else:
    print("GRATULÁLOK! 🏆 🏆 🏆")
