# Könyvek feladat megoldása
#
# 1. feladat 6 pont
# 2. feladat 6 pont
# 3. feladat 5 pont
# 4. feladat 5 pont
# 5. feladat 17 pont (8+9 pont)
# 6. feladat 11 pont
# ================================
#  Összesen: 50 pont
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
for konyv in konyvek:
    if int(konyv[PELDANYSZAM]) >= 40000 and konyv[EREDET] == "kf":
        print(f"{konyv[ÉV]}/{konyv[NEGYED]}. {konyv[LEIRAS]} --> {konyv[PELDANYSZAM]}" )
        break

print("5. feladat")
        
statisztika = {}
for konyv in konyvek:
    statisztika[konyv[ÉV]]=[0,0,0,0]
for konyv in konyvek:
    if konyv[EREDET]=="ma":
        statisztika[konyv[ÉV]][0] += 1
        statisztika[konyv[ÉV]][1] += int(konyv[PELDANYSZAM])
    elif konyv[EREDET]=="kf":
        statisztika[konyv[ÉV]][2] += 1
        statisztika[konyv[ÉV]][3] += int(konyv[PELDANYSZAM])
print("Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
for sor in statisztika:
    ma_db = statisztika[sor][0]
    ma_pld = statisztika[sor][1]
    kf_db = statisztika[sor][2]
    kf_pld = statisztika[sor][3]
    print(f"{sor}\t{ma_db}\t\t{ma_pld}\t\t\t{kf_db}\t\t{kf_pld}")

file = open("tabla.html","wt")

txt = "<table border=\"1\">\n"
txt += "<tr>\n"
txt += "<th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi kiadás</th><th>Külföldi példányszám</th>\n"
txt += "</tr>\n"
for sor in statisztika:
    ma_db = statisztika[sor][0]
    ma_pld = statisztika[sor][1]
    kf_db = statisztika[sor][2]
    kf_pld = statisztika[sor][3]
    txt +="<tr>\n"
    txt += f"<td>{sor}</td><td>{ma_db}</td><td>{ma_pld}</td><td>{kf_db}</td><td>{kf_pld}</td>\n"
    txt +="</tr>\n"
txt += "</table>"

file.write(txt)
file.close()

print("6. feladat [TBD]")

# 6. feladat: 
# Legalább kétszer, nagyobb példányszámban újra kiadott könyvek: 
# Bosnyák Viktória: A sirály a király? 
# Owens, Delia: Ahol a folyami rákok énekelnek 
