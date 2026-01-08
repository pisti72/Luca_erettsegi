print("*** Progamozási tételek ***")
számok=[5,6,2,42,1,7,2,2,8]
print("Számok:",számok)

print("--- 0. Iteráció ---")
print("--- érthetőbben ---")
elemek_száma=len(számok)
print("Elemek száma:",elemek_száma)
sorozat = range(elemek_száma) 
print("Ebből egy sorozat: ", sorozat)
for i in sorozat:
    print(számok[i])
# Hibakezelés, ha nincs annyi elem a listában
try:
    print(számok[10])
except IndexError:
    print("Nincs 10. elem a listában.")

print("--- szebben ---")
for szám in számok:
    print(szám)

print("--- 1. Számlálás ---")
számláló = 0
for szám in számok:
    if szám == 2:
        számláló += 1
print("2-esek száma:",számláló)

print("--- 2. Összegzés ---")
összeg=0
for szám in számok:
    összeg+=szám
print("Számok összege:",összeg)

print("--- 3. Eldöntés ---")
van_e_7=False
for szám in számok:
    if szám == 7:
        van_e_7=True
print("Van-e 7-es a számok között?",van_e_7)

print("--- 4. Kiválasztás ---")
kettesek=[]
for szám in számok:
    if szám == 2:
        kettesek.append(szám)
print("2-esek:",kettesek)

print("--- 5. Keresés ---")
pozíció=-1
i=1
for szám in számok:
    i+=1
    if szám == 7:
        pozíció=i
        break
if pozíció != -1:
    print("7-es a(z)",pozíció,". helyen van.")
else:
    print("Nincs 7-es a számok között.")

print("--- 6. Maximum keresés ---")
maximum=számok[0]
for szám in számok:
    if szám > maximum:
        maximum=szám
print("A legnagyobb szám:",maximum)
print("Helye a listában:",számok.index(maximum)+1)

print("--- 7. Minimum keresés ---")
minimum=számok[0]
for szám in számok:
    if szám < minimum:
        minimum=szám
print("A legkisebb szám:",minimum)
print("Helye a listában:",számok.index(minimum)+1)
print("--- 8. Eldöntés (minden elemre) ---")
minden_páros=True
for szám in számok:
    if szám % 2 != 0:
        minden_páros=False
print("Minden szám páros?",minden_páros)