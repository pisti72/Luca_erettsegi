---
title: "Programozási feladatgyűjtemény középiskolások részére"
author: "Szalontai István"
date: "2026-03-18"
---

# Programozási feladatgyűjtemény középiskolások részére

Írta: Szalontai István
Dátum: 2026.03.18.

## Előszó

A 21. században a programozási ismeretek egyre fontosabb szerepet játszanak nemcsak az informatika, hanem szinte minden tudományterület fejlődésében. Az algoritmikus gondolkodás képessége ma már alapvető kompetencia, amely segít a mindennapi problémák strukturált megközelítésében és megoldásában.

Ezt a feladatgyűjteményt azzal a céllal írtam, hogy gyakorlati segítséget nyújtsak a programozást tanuló diákoknak és tanáraiknak. Évek óta tapasztalom, hogy bár matematikából, fizikából és kémiából rengeteg jól strukturált feladatgyűjtemény áll rendelkezésre, a programozás területén sajnos hiánycikk egy olyan mű, amely fokozatosan építkezve, egyszerű példákon keresztül vezeti be a kezdőket az algoritmikus gondolkodás világába.

Meggyőződésem, hogy a programozást – mint minden gyakorlati készséget – leghatékonyabban konkrét feladatok megoldásán keresztül lehet elsajátítani. A könyv célja, hogy lépésről lépésre építse fel a szükséges tudást, minden fejezet az előző ismeretekre alapozva vezesse tovább az olvasót.

### A könyv felépítése

A feladatgyűjtemény logikus haladást követ az alapoktól a komplexebb témákig:

**Alapműveletek:** Először a programozás alapjaival ismerkedünk meg: az adatok beolvasásával és kiírásával, a konzollal való kommunikáció alapelveivel.

**Változók és adattípusok:** Ezt követően a változók világába merülünk, megismerjük a különböző adattípusokat, azok metódusait, valamint az adattípusok közötti konverziós lehetőségeket.

**Elágazások:** A feltételes szerkezetek fejezet bemutatja az összehasonlítások, logikai vizsgálatok működését, a logikai feltételek kapcsolatát, valamint az egymásba ágyazott feltételes szerkezetek használatát.

**Ciklusok:** A ciklusokkal foglalkozó részben mind a `for`, mind a `while` ciklusok működését gyakoroljuk, beleértve a `break` és `continue` vezérlési utasítások használatát is.

**Összetett adatszerkezetek:** Megismerkedünk a listákkal, a többdimenziós adatstruktúrákkal és ezek gyakorlati alkalmazásával.

**Fájlkezelés:** A fájlműveletekkel foglalkozó fejezet bemutatja, hogyan olvashatunk be adatokat fájlokból, és hogyan menthetünk el eredményeket tartós tárolásra.

**Sorozatok kezelése:** Megtanuljuk, hogyan dolgozhatunk hatékonyan nagy mennyiségű adattal, hogyan végezhetünk műveleteket adatsorozatokon.

**Függvények:** Megismerjük a saját függvények létrehozásának módját, a kód újrafelhasználhatóságának elvét, valamint a beépített függvénykönyvtárak (matematikai, szöveges és egyéb) használatát.

**Grafikus felhasználói felület:** A könyv végén betekintést nyerünk a grafikus programozás alapjaiba a tkinter könyvtár segítségével.

### Miért Python?

A feladatok megoldásait Python programozási nyelven adom meg, mivel ez jelenleg a középiskolai informatikai oktatásban a legszélesebb körben használt nyelv. A Python egyszerű szintaxisa, olvashatósága és széles körű alkalmazhatósága ideálissá teszi a programozás tanulásának megkezdéséhez.

Remélem, ez a feladatgyűjtemény hasznos társad lesz a programozás elsajátításának útján. Minden feladat egy újabb lépés az algoritmikus gondolkodás fejlesztésében – légy kitartó, és élvezd a felfedezés örömét!

Szalontai István  
2026. március

## Adatok beolvasása és kiiratása

### 1. Feladat: Köszöntés

Írj olyan programot, amelyik beolvassa a nevedet, majd az életkorodat. Ha például tégedet Péternek hívnak és ha 20 év alatti vagy, akkor úgy köszönt, hogy "Szia Péter!", ha 21 és 40 év közötti vagy akkor "Jó napot Péter!",  ha pedig már 41 éves elmúltál akkor úgy köszönt, hogy "Tiszteletem Péter!".

### 1.b Feladat: Köszöntés és hány éves vagy

Írj egy olyan Python programot, ami bekéri a nevedet, a születési évedet és a mostani évet.
Majd köszönt téged és kiírja, hogy te hány éves vagy.

Példa a működésre:

Hogy hívnak? Aladár
Melyik évben születtél? 2008
Milyen évet írunk most? 2026
Üdvözöllek Aladár! Te 18 éves vagy.


### 2. Feladat: Számológép

Készíts egy egyszerű számológép programot, amely beolvas két számot, majd megkérdezi a felhasználót, hogy milyen műveletet szeretne elvégezni (+, -, *, /). A program végezze el a kért műveletet és írja ki az eredményt! Osztásnál figyeljen arra, hogy nullával való osztás esetén írjon ki hibaüzenetet!

### 3. Feladat: Mozijegy ár

Írj programot, amely kiszámítja a mozijegy árát! A program kérje be a néző életkorát. A jegyárak a következők:
- 14 év alatt: 800 Ft (gyerekjegy)
- 14-65 év között: 1500 Ft (normál jegy)
- 65 év felett: 1000 Ft (nyugdíjas jegy)

A program írja ki a jegy árát és a kategóriát is!

### 4. Feladat: Hőmérséklet átváltó

Készíts hőmérséklet átváltó programot! A program kérdezze meg a felhasználót, hogy milyen mértékegységben adja meg a hőmérsékletet (C - Celsius, F - Fahrenheit). Ezután olvassa be a hőmérséklet értékét, váltsa át a másik mértékegységre, és írja ki az eredményt! A képletek:
- Celsius → Fahrenheit: F = C × 1.8 + 32
- Fahrenheit → Celsius: C = (F - 32) / 1.8

### 5. Feladat: Testtömegindex (BMI) számítás

Írj programot, amely kiszámítja a felhasználó testtömegindexét (BMI)! A program kérje be a felhasználó testsúlyát kilogrammban és testmagasságát centiméterben. Számítsa ki a BMI értékét a következő képlettel: BMI = testsúly / (testmagasság_méterben)². 

A program értékelje is a BMI értékét:
- 18.5 alatt: sovány
- 18.5-25 között: normál testsúly
- 25-30 között: túlsúlyos
- 30 felett: elhízott

A program írja ki a BMI értékét két tizedesjegyre kerekítve és a kategóriát is!

## Megoldás

### 1. Feladat

Ebben a feladatban a köszöntést egymásután következő elágazások szerint határozzuk meg az adatok beolvasását követően.

```python
név = input("Hogy hívnak? ")
kor = int(input("Hány éves vagy? "))

if kor < 20:
    print(f"Szia {név}!")
elif kor < 40:
    print(f"Jó napot {név}!")
else:
    print(f"Tiszteletem {név}!")
```

**Megjegyzés:** Figyeljük meg, hogy az életkort `int()`-tel számmá alakítjuk, különben szövegként kezelné a program.

### 1.b Feladat

Ebben a feladatban beolvassuk a nevet, a születési évet és az aktuális évet. Az életkort az aktuális és a születési év különbsége alapján számítjuk ki.

```python
név = input("Hogy hívnak? ")
szuletesi_eve = int(input("Melyik évben születtél? "))
jelenlegi_ev = int(input("Milyen évet írunk most? "))

kor = jelenlegi_ev - szuletesi_eve

print(f"Üdvözöllek {név}! Te {kor} éves vagy.")
```

**Megjegyzés:** Az éveket `int()`-tel alakítjuk számmá, hogy matematikai műveletet végezhetünk velük. Az f-string formázás `f"..."` szintaxisával egyszerűen beilleszthetjük a változók értékeit a szövegbe.

### 2. Feladat

Ebben a feladatban először beolvassuk a két számot, majd a műveleti jelet. Az elágazások segítségével eldöntjük, melyik műveletet kell elvégeznünk.

```python
szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))
muvelet = input("Milyen műveletet végezzek? (+, -, *, /): ")

if muvelet == "+":
    eredmeny = szam1 + szam2
    print(f"{szam1} + {szam2} = {eredmeny}")
elif muvelet == "-":
    eredmeny = szam1 - szam2
    print(f"{szam1} - {szam2} = {eredmeny}")
elif muvelet == "*":
    eredmeny = szam1 * szam2
    print(f"{szam1} * {szam2} = {eredmeny}")
elif muvelet == "/":
    if szam2 != 0:
        eredmeny = szam1 / szam2
        print(f"{szam1} / {szam2} = {eredmeny}")
    else:
        print("Hiba: Nullával nem lehet osztani!")
else:
    print("Érvénytelen művelet!")
```

**Megjegyzés:** A `float()` használatával tizedes számokat is kezelhetünk. Az osztásnál egymásba ágyazott `if` vizsgálja, hogy nem próbálunk-e nullával osztani.

### 3. Feladat

A feladat megoldásához beolvassuk az életkort, majd elágazásokkal meghatározzuk a megfelelő jegyárat és kategóriát.

```python
kor = int(input("Add meg az életkorodat: "))

if kor < 14:
    ar = 800
    kategoria = "gyerekjegy"
elif kor <= 65:
    ar = 1500
    kategoria = "normál jegy"
else:
    ar = 1000
    kategoria = "nyugdíjas jegy"

print(f"A jegy ára: {ar} Ft ({kategoria})")
```

**Megjegyzés:** A `<=` operátorral vizsgáljuk, hogy a kor kisebb vagy egyenlő-e egy adott értékkel.

### 4. Feladat

Először megkérdezzük a mértékegységet, majd a megfelelő átváltást végezzük el.

```python
mertek = input("Milyen mértékegységben adod meg a hőmérsékletet? (C/F): ")
homerseklet = float(input("Add meg a hőmérsékletet: "))

if mertek.upper() == "C":
    fahrenheit = homerseklet * 1.8 + 32
    print(f"{homerseklet}°C = {fahrenheit}°F")
elif mertek.upper() == "F":
    celsius = (homerseklet - 32) / 1.8
    print(f"{homerseklet}°F = {celsius}°C")
else:
    print("Érvénytelen mértékegység! Csak C vagy F lehet.")
```

**Megjegyzés:** Az `.upper()` metódus nagybetűssé alakítja a bemenet karakterét, így mindegy, hogy a felhasználó kis- vagy nagybetűt ír.

### 5. Feladat

A BMI számítás során ügyelni kell arra, hogy a magasságot centiméterből méterre váltsuk.

```python
suly = float(input("Add meg a testsúlyodat (kg): "))
magassag_cm = float(input("Add meg a magasságodat (cm): "))

# Magasság átváltása méterre
magassag_m = magassag_cm / 100

# BMI számítás
bmi = suly / (magassag_m ** 2)

# Kategória meghatározása
if bmi < 18.5:
    kategoria = "sovány"
elif bmi < 25:
    kategoria = "normál testsúly"
elif bmi < 30:
    kategoria = "túlsúlyos"
else:
    kategoria = "elhízott"

print(f"A BMI értéked: {bmi:.2f}")
print(f"Kategória: {kategoria}")
```

**Megjegyzés:** A `** 2` hatványozást jelent. A `{bmi:.2f}` formázás két tizedesjegyre kerekít. A program először méterre váltja a magasságot, majd kiszámítja a BMI-t, végül kategorizálja az eredményt.