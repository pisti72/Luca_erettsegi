RSZÁM = 0
ÓRA = 1
PERC = 2
KMH = 3
file = open("jeladas.txt", encoding = "UTF-8")
jelek = []
for j in file:
    jelek.append(j.strip().split())
print("2. feladat")
ido = jelek[-1][ÓRA] + ":" + jelek[-1][PERC]
rszám = jelek[-1][RSZÁM] 
print("Az utolsó jeladás időpontja", ido,"a jármű rendszáma", rszám)

print("3. feladat")
rszám = jelek[0][RSZÁM]
print("Az első jármű:", rszám)
idok = ""
for j in jelek:
    if j[RSZÁM] == rszám:
        idok += j[ÓRA] + ":" + j[PERC] + " "
print("Jeladásainak időpontjai:", idok)

print("4. feladat")
#óra = input("Kérem, adja meg az órát:")
#perc = input("Kérem, adja meg a percet:")
óra = "6"
perc = "54"
db = 0
for j in jelek:
    if j[ÓRA] == óra and j[PERC] == perc:
        db += 1
print("A jeladások száma:", db)

print("5. feladat")
print("6. feladat") 
print("7. feladat")
rendszamok = {}
for j in jelek:
    rsz = j[RSZÁM]
    if rsz in rendszamok:
        rendszamok[rsz][2] = j[ÓRA]
        rendszamok[rsz][3] = j[PERC]
    else:
        rendszamok[rsz] = [j[ÓRA], j[PERC], "semmi", "semmi" ]
file = open("ido.txt","wt",encoding = "UTF-8")
txt = ""
for key in rendszamok:
    txt += key + " " + rendszamok[key][0] + " " + rendszamok[key][1] + " " + rendszamok[key][2] + " " + rendszamok[key][3]
    txt += "\n"
print(txt)
file.write(txt)
file.close()
