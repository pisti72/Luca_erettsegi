---
marp: true
theme: gaia
paginate: true
backgroundColor: #ffa
---

<!-- _class: lead -->

# 📚 Programozási Tételek

**Érettségi felkészítés**
*Alapvető algoritmusok és mintapéldák*
*Készítette: Szalontai István*
*Dátum:2026-01-08*

---

## 📋 Tartalom

1. **Összegzés** tétel
2. **Megszámlálás** tétel
3. **Eldöntés** tétel
4. **Kiválasztás** tétel
5. **Keresés** tétel
6. **Maximum/Minimum kiválasztás** tétel
7. **Másolás** és **Kiválogatás** tétel
8. **Szétválogatás** tétel

---

# 1️⃣ Összegzés Tétel

*Sorozat elemeinek összege*

---

## Összegzés - Feladat

**Cél:** Számoljuk össze egy tömb elemeinek összegét!

**Példa:**
- Tömb: `[5, 12, 3, 8, 15]`
- Eredmény: `43`

**Alkalmazás:**
- Számok összeadása
- Átlagszámítás előkészítése
- Pontszámok összegzése

---

## Összegzés - Algoritmus

```python
def osszegzes(tomb):
    osszeg = 0
    
    for elem in tomb:
        osszeg += elem
    
    return osszeg

# Példa:
szamok = [5, 12, 3, 8, 15]
print(osszegzes(szamok))  # 43

# Beépített megoldás:
print(sum(szamok))  # 43
```

---

# 2️⃣ Megszámlálás Tétel

*Feltételnek megfelelő elemek száma*

---

## Megszámlálás - Feladat

**Cél:** Számoljuk meg, hány elem felel meg egy feltételnek!

**Példa:**
- Tömb: `[5, 12, 3, 8, 15, 7]`
- Feltétel: páros számok
- Eredmény: `2` (12 és 8)

**Alkalmazás:**
- Pozitív/negatív számok száma
- Bizonyos feltételnek megfelelő elemek

---

## Megszámlálás - Algoritmus

```python
def megszamlalas(tomb):
    darabszam = 0
    
    for szam in tomb:
        paros_e = (szam % 2 == 0)  # Feltétel: páros szám?
        if paros_e:
            darabszam = darabszam + 1
    
    return darabszam

# Példa:
szamok = [5, 12, 3, 8, 15, 7]
paros_szamok_darabja = megszamlalas(szamok)
print(paros_szamok_darabja)  # 2

# Kompakt megoldás:
print(sum(1 for x in szamok if x % 2 == 0))  # 2
```

---

# 3️⃣ Eldöntés Tétel

*Van-e a sorozatban adott tulajdonságú elem?*

---

## Eldöntés - Feladat

**Cél:** Van-e a tömbben olyan elem, ami megfelel egy feltételnek?

**Példa:**
- Tömb: `[5, 12, 3, 8, 15]`
- Feltétel: 10-nél nagyobb?
- Eredmény: `true` (12 és 15)

**Alkalmazás:**
- Van-e negatív szám?
- Tartalmaz-e a tömb nullát?

---

## Eldöntés - Algoritmus

```python
def eldontes(tomb):
    index = 0
    van_e = False
    
    # Keresünk amíg nem találunk vagy véget nem ér a tömb
    while index < len(tomb) and not van_e:
        nagyobb_mint_10 = (tomb[index] > 10)  # Feltétel
        if nagyobb_mint_10:
            van_e = True
        else:
            index = index + 1
    
    return van_e

# Példa:
szamok = [5, 12, 3, 8, 15]
van_nagyobb = eldontes(szamok)
print(van_nagyobb)  # True

# Pythonos megoldás:
print(any(x > 10 for x in szamok))  # True
```

---

# 4️⃣ Kiválasztás Tétel

*Mely elem felel meg a feltételnek?*

---

## Kiválasztás - Feladat

**Cél:** Melyik elem felel meg a feltételnek? (Tudjuk, hogy van ilyen!)

**Példa:**
- Tömb: `[5, 12, 3, 8, 15]`
- Feltétel: 10-nél nagyobb
- Eredmény: `12` (első ilyen elem indexe: 1)

**⚠️ Előfeltétel:** Biztosan van ilyen elem!

**Alkalmazás:**
- Első páros szám megtalálása
- Adott feltételű elem indexe

---

## Kiválasztás - Algoritmus

```python
def kivalasztas(tomb):
    index = 0
    megfelelo_e = False
    
    # Keresünk amíg nem találjuk meg (tudjuk, hogy VAN ilyen!)
    while not megfelelo_e:
        nagyobb_mint_10 = (tomb[index] > 10)  # Feltétel
        if nagyobb_mint_10:
            megfelelo_e = True
        else:
            index = index + 1
    
    return index  # visszaadjuk a talált elem indexét

# Példa:
szamok = [5, 12, 3, 8, 15]
talalt_index = kivalasztas(szamok)
talalt_ertek = szamok[talalt_index]
print(f"Index: {talalt_index}, Érték: {talalt_ertek}")
# Index: 1, Érték: 12
```

---

# 5️⃣ Keresés Tétel

*Van-e és ha igen, melyik?*

---

## Keresés - Feladat

**Cél:** Van-e olyan elem, ami megfelel a feltételnek, és ha igen, melyik?

**Különbség a többi tételtől:**
- **Eldöntés:** csak azt mondja meg, van-e
- **Kiválasztás:** tudjuk, hogy van, megkeresi
- **Keresés:** megnézi, van-e ÉS ha van, megkeresi

**Alkalmazás:**
- Elem keresése tömbben
- Biztonságos keresés

---

## Keresés - Algoritmus

```python
def kereses(tomb):
    index = 0
    van_e = False
    
    # Keresünk amíg nem találunk VAGY véget nem ér a tömb
    while index < len(tomb) and not van_e:
        nagyobb_mint_20 = (tomb[index] > 20)  # Feltétel
        if nagyobb_mint_20:
            van_e = True
        else:
            index = index + 1
    
    # Visszaadjuk az eredményt
    if van_e:
        return {"van_e": True, "index": index}
    else:
        return {"van_e": False, "index": -1}

# Példa:
szamok = [5, 12, 3, 8, 15]
eredmeny = kereses(szamok)
print(eredmeny)  # {'van_e': False, 'index': -1}
```

---

# 6️⃣ Maximum/Minimum Kiválasztás

*Legnagyobb/legkisebb elem megkeresése*

---

## Maximum kiválasztás - Feladat

**Cél:** Keressük meg a legnagyobb elemet!

**Példa:**
- Tömb: `[5, 12, 3, 18, 15]`
- Eredmény: `18` (index: 3)

**Algoritmus lépései:**
1. Első elem legyen a maximum
2. Végigmegyünk a tömbön
3. Ha találunk nagyobbat, azt tekintjük maximumnak

---

## Maximum kiválasztás - Algoritmus

```python
def min_kivalasztas(tomb):
    legkisebb_index = 0  # Első elem az aktuális minimum
    
    # Végigmegyünk a többi elemen
    for i in range(1, len(tomb)):
        aktualis_szam = tomb[i]
        legkisebb_szam = tomb[legkisebb_index]
        
        kisebb_e = (aktualis_szam < legkisebb_szam)
        if kisebb_e:
            legkisebb_index = i  # Új minimum találva!
    
    return legkisebb_index

# Példa:
szamok = [5, 12, 3, 18, 15]
min_index = min_kivalasztas(szamok)
min_ertek = szamok[min_index]
print(f"Min index: {min_index}, Min érték: {min_ertek}")
# Min index: 2, Min érték: 3
```

---

# 7️⃣ Másolás

*Tömb átalakítása, transzformációja*

---

## Másolás - Feladat

**Cél:** Másoljuk át egy tömb elemeit egy másik tömbbe (esetleg transzformációval)!

**Példa 1 - egyszerű másolás:**
- Eredeti: `[5, 12, 3, 8]`
- Másolat: `[5, 12, 3, 8]`

**Példa 2 - transzformációval:**
- Eredeti: `[1, 2, 3, 4]`
- Duplázva: `[2, 4, 6, 8]`

---

## Másolás - Algoritmus

```python
def masolas_transzformacioval(tomb):
    uj_tomb = []
    
    for szam in tomb:
        duplazott_szam = szam * 2  # Transzformáció: duplázás
        uj_tomb.append(duplazott_szam)
    
    return uj_tomb

# Példa:
szamok = [1, 2, 3, 4]
duplazott_szamok = masolas_transzformacioval(szamok)
print(duplazott_szamok)  # [2, 4, 6, 8]
```

---

## Kiválogatás - Feladat

**Cél:** Válasszuk ki egy tömből a feltételnek megfelelő elemeket!

**Példa:**
- Eredeti: `[5, 12, 3, 8, 15, 7]`
- Feltétel: páros számok
- Eredmény: `[12, 8]`

**Alkalmazás:**
- Szűrés
- Feltételnek megfelelő elemek gyűjtése

---

## Kiválogatás - Algoritmus

```python
def kivalogatas(tomb):
    paros_szamok = []
    
    for szam in tomb:
        paros_e = (szam % 2 == 0)  # Feltétel: páros?
        if paros_e:
            paros_szamok.append(szam)
    
    return paros_szamok

# Példa:
szamok = [5, 12, 3, 8, 15, 7]
parosok = kivalogatas(szamok)
print(parosok)  # [12, 8]

# Rövid megoldás (list comprehension):
parosok2 = [szam for szam in szamok if szam % 2 == 0]
print(parosok2)  # [12, 8]
```

---

# 8️⃣ Szétválogatás

*Tömb szétválasztása több tömbre feltétel szerint*

---

## Szétválogatás - Feladat

**Cél:** Osszuk szét egy tömböt két (vagy több) tömbre valamilyen feltétel szerint!

**Különbség a kiválogatástól:**
- **Kiválogatás:** csak a feltételnek megfelelő elemek
- **Szétválogatás:** MINDEN elem bekerül valamelyik tömbbe

**Példa:**
- Eredeti: `[5, 12, 3, 8, 15, 7]`
- Párosok: `[12, 8]`
- Páratlanok: `[5, 3, 15, 7]`

---

## Szétválogatás - Algoritmus

```python
def szetvalogatas(tomb):
    paros_szamok = []
    paratlan_szamok = []
    
    for szam in tomb:
        paros_e = (szam % 2 == 0)  # Feltétel: páros?
        
        if paros_e:
            paros_szamok.append(szam)
        else:
            paratlan_szamok.append(szam)
    
    return {"parosok": paros_szamok, "paratlanok": paratlan_szamok}

# Példa:
szamok = [5, 12, 3, 8, 15, 7]
eredmeny = szetvalogatas(szamok)
print("Párosok:", eredmeny["parosok"])        # [12, 8]
print("Páratlanok:", eredmeny["paratlanok"])  # [5, 3, 15, 7]
```

---

## Szétválogatás - Gyakorlati példa

**Pozitív/negatív számok szétválogatása:**
```python
def szet_pozitiv_negativ(tomb):
    pozitiv_szamok = []
    negativ_szamok = []
    
    for szam in tomb:
        nem_negativ_e = (szam >= 0)  # Feltétel
        
        if nem_negativ_e:
            pozitiv_szamok.append(szam)
        else:
            negativ_szamok.append(szam)
    
    return {"pozitivak": pozitiv_szamok, "negativak": negativ_szamok}

# Példa:
szamok = [5, -3, 12, -8, 0, 15, -1]
eredmeny = szet_pozitiv_negativ(szamok)
print("Nem negatívak:", eredmeny["pozitivak"])  # [5, 12, 0, 15]
print("Negatívak:", eredmeny["negativak"])      # [-3, -8, -1]
```

---

# 📊 Összefoglaló Táblázat

---

## Programozási tételek áttekintése

| Tétel | Bemenet | Kimenet | Előfeltétel |
|-------|---------|---------|-------------|
| **Összegzés** | Sorozat | Szám (összeg) | - |
| **Megszámlálás** | Sorozat, feltétel | Szám (darab) | - |
| **Eldöntés** | Sorozat, feltétel | Logikai | - |
| **Kiválasztás** | Sorozat, feltétel | Index | ✅ Van ilyen elem |
| **Keresés** | Sorozat, feltétel | Van-e? + Index | - |
| **Max/Min** | Sorozat | Index | Nem üres tömb |
| **Kiválogatás** | Sorozat, feltétel | Új sorozat | - |
| **Szétválogatás** | Sorozat, feltétel | 2 új sorozat | - |

---

# 🎯 Gyakorló Feladatok

---

## Gyakorló feladatok

1. **Írj függvényt**, ami egy tömb páratlan számainak összegét számolja!

2. **Írj függvényt**, ami megmondja, van-e negatív szám egy tömbben!

3. **Írj függvényt**, ami megkeresi az első 100-nál nagyobb számot!

4. **Írj függvényt**, ami kiválogatja a 3-mal osztható számokat!

5. **Írj függvényt**, ami megkeresi a második legnagyobb számot!

---

## Megoldási ötletek

**1. feladat:** Összegzés + megszámlálás kombinációja
- Feltétel: `x % 2 !== 0`

**2. feladat:** Eldöntés tétel
- Feltétel: `x < 0`

**3. feladat:** Keresés tétel
- Feltétel: `x > 100`

**4. feladat:** Kiválogatás tétel
- Feltétel: `x % 3 === 0`

**5. feladat:** Maximum kiválasztás kétszer
- Első maximum eltávolítása után

---

# ✅ Tippek az Érettségihez

---

## Érettségi tippek

### ✏️ Mit kell tudni:

1. **Minden tétel alapalgoritmusát** (ciklus, feltétel)
2. **Mikor melyik tételt kell használni**
3. **Kombináció:** több tétel összekapcsolása
4. **Pszeudokód olvasása és írása**

### 🎯 Gyakorlati tippek:

- Írj **kommenteket** a kódodba!
- **Tesztelj** példaadatokkal!
- Figyelj a **speciális esetekre** (üres tömb, 1 elemű tömb)
- **Beszédes változónevek**!

---

<!-- _class: lead -->

# 🎓 Sikeres Érettségit!

**Kérdések?**
**Gyakorlás, gyakorlás, gyakorlás! 💪**

