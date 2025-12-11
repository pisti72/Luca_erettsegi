# Adatbázis SQL Feladatok
## Gyakorlati példák és megoldások

---

## Tartalom

### Feladattípusok
1. 📚 **Könyvtár adatbázis** - Alapműveletek
2. 🎬 **Film adatbázis** - JOIN gyakorlatok
3. 🎮 **Játékgyűjtemény** - GROUP BY és összesítések
4. 👥 **Diák-Tantárgy adatbázis** - Komplex lekérdezések
5. 🏪 **Webshop adatbázis** - Valós feladatok

### Nehézségi szintek
- ⭐ Kezdő
- ⭐⭐ Haladó
- ⭐⭐⭐ Profi

---

## 📚 Könyvtár adatbázis - Adatstruktúra

### Táblák

**Konyvek tábla:**


| Konyv_ID | Cim | Szerzo | Kiado | Ev | Ar |
|----------|-----|--------|-------|-----|-----|
| 1 | Harry Potter | J.K. Rowling | Animus | 2000 | 3500 |
| 2 | 1984 | George Orwell | Európa | 1984 | 2800 |
| 3 | Egri csillagok | Gárdonyi Géza | Móra | 1901 | 3200 |
| 4 | A Gyűrűk Ura | J.R.R. Tolkien | Európa | 1954 | 4500 |
| 5 | Metro 2033 | Dmitry Glukhovsky | Gabo | 2005 | 3000 |

**Kolcsonzesek tábla:**


| Kolcsonzes_ID | Konyv_ID | Kolcsonzo_nev | Datum |
|---------------|----------|---------------|--------|
| 1 | 1 | Kiss Anna | 2024-11-15 |
| 2 | 3 | Nagy Péter | 2024-11-20 |
| 3 | 1 | Tóth Eszter | 2024-12-01 |

---

## 📚 Feladat 1 - Alapműveletek ⭐

### Feladatok

**1.1** Listázd ki az összes könyv címét és szerzőjét!

**1.2** Kérdezd le azokat a könyveket, amelyek 2000 után jelentek meg!

**1.3** Rendezd a könyveket ár szerint csökkenő sorrendbe!

**1.4** Hány könyv van az adatbázisban összesen?

---

## 📚 Megoldás 1.1 - Címek és szerzők

### Feladat
Listázd ki az összes könyv címét és szerzőjét!

### Megoldás
```sql
-- MS Access és MySQL/PostgreSQL is ugyanaz
SELECT Cim, Szerzo 
FROM Konyvek;
```

### Eredmény


| Cim | Szerzo |
|-----|--------|
| Harry Potter | J.K. Rowling |
| 1984 | George Orwell |
| Egri csillagok | Gárdonyi Géza |
| A Gyűrűk Ura | J.R.R. Tolkien |
| Metro 2033 | Dmitry Glukhovsky |

### Magyarázat
- `SELECT Cim, Szerzo` - csak ezeket az oszlopokat kérjük
- `FROM Konyvek` - a Konyvek táblából

---

## 📚 Megoldás 1.2 - Könyvek 2000 után

### Feladat
Kérdezd le azokat a könyveket, amelyek 2000 után jelentek meg!

### Megoldás
```sql
SELECT * 
FROM Konyvek
WHERE Ev > 2000;
```

### Eredmény


| Konyv_ID | Cim | Szerzo | Kiado | Ev | Ar |
|----------|-----|--------|-------|-----|-----|
| 5 | Metro 2033 | Dmitry Glukhovsky | Gabo | 2005 | 3000 |

### Magyarázat
- `WHERE Ev > 2000` - csak azokat a sorokat, ahol az év nagyobb mint 2000
- `*` - minden oszlopot megjelenítünk

---

## 📚 Megoldás 1.3 - Rendezés ár szerint

### Feladat
Rendezd a könyveket ár szerint csökkenő sorrendbe!

### Megoldás
```sql
SELECT Cim, Szerzo, Ar
FROM Konyvek
ORDER BY Ar DESC;
```

### Eredmény


| Cim | Szerzo | Ar |
|-----|--------|-----|
| A Gyűrűk Ura | J.R.R. Tolkien | 4500 |
| Harry Potter | J.K. Rowling | 3500 |
| Egri csillagok | Gárdonyi Géza | 3200 |
| Metro 2033 | Dmitry Glukhovsky | 3000 |
| 1984 | George Orwell | 2800 |

### Magyarázat
- `ORDER BY Ar DESC` - csökkenő sorrend (legdrágább elöl)
- `ASC` lenne a növekvő sorrend (alapértelmezett)

---

## 📚 Megoldás 1.4 - Könyvek száma

### Feladat
Hány könyv van az adatbázisban összesen?

### Megoldás
```sql
SELECT COUNT(*) AS Konyvek_szama
FROM Konyvek;
```

### Eredmény


| Konyvek_szama |
|---------------|
| 5 |

### Magyarázat
- `COUNT(*)` - megszámolja az összes sort
- `AS Konyvek_szama` - átnevezzük az oszlopot (alias)

---

## 📚 Feladat 2 - Haladó ⭐⭐

### Feladatok

**2.1** Listázd ki azokat a könyveket, amelyek címe tartalmazza a "Gyűrű" szót!

**2.2** Számold ki a könyvek átlagárát!

**2.3** Kérdezd le a legdrágább könyv adatait!

**2.4** Listázd ki a kiadókat és hogy hány könyvük van! (GROUP BY)

---

## 📚 Megoldás 2.1 - Keresés mintára

### Feladat
Listázd ki azokat a könyveket, amelyek címe tartalmazza a "Gyűrű" szót!

### Megoldás
```sql
-- MS Access
SELECT * 
FROM Konyvek
WHERE Cim LIKE '*Gyűrű*';

-- MySQL/PostgreSQL
SELECT * 
FROM Konyvek
WHERE Cim LIKE '%Gyűrű%';
```

### Eredmény


| Konyv_ID | Cim | Szerzo | Kiado | Ev | Ar |
|----------|-----|--------|-------|-----|-----|
| 4 | A Gyűrűk Ura | J.R.R. Tolkien | Európa | 1954 | 4500 |

### Magyarázat
- `LIKE` - mintaillesztés
- `*` (Access) vagy `%` (MySQL) - bármennyi karakter
- `*Gyűrű*` - bármi előtte és utána is lehet

---

## 📚 Megoldás 2.2 - Átlagár

### Feladat
Számold ki a könyvek átlagárát!

### Megoldás
```sql
SELECT AVG(Ar) AS Atlagar
FROM Konyvek;
```

### Eredmény


| Atlagar |
|---------|
| 3400 |

### Magyarázat
- `AVG(Ar)` - átlag függvény az Ar oszlopon
- Más hasznos függvények: `SUM()`, `MIN()`, `MAX()`

---

## 📚 Megoldás 2.3 - Legdrágább könyv

### Feladat
Kérdezd le a legdrágább könyv adatait!

### Megoldás
```sql
-- MS Access
SELECT TOP 1 *
FROM Konyvek
ORDER BY Ar DESC;

-- MySQL/PostgreSQL
SELECT *
FROM Konyvek
ORDER BY Ar DESC
LIMIT 1;
```

### Eredmény


| Konyv_ID | Cim | Szerzo | Kiado | Ev | Ar |
|----------|-----|--------|-------|-----|-----|
| 4 | A Gyűrűk Ura | J.R.R. Tolkien | Európa | 1954 | 4500 |

### Magyarázat
- Csökkenő sorrendbe rendezzük ár szerint
- Az első rekordot kérjük le (`TOP 1` vagy `LIMIT 1`)

---

## 📚 Megoldás 2.4 - Kiadók és könyveik

### Feladat
Listázd ki a kiadókat és hogy hány könyvük van!

### Megoldás
```sql
SELECT Kiado, COUNT(*) AS Konyvek_szama
FROM Konyvek
GROUP BY Kiado
ORDER BY Konyvek_szama DESC;
```

### Eredmény


| Kiado | Konyvek_szama |
|-------|---------------|
| Európa | 2 |
| Animus | 1 |
| Móra | 1 |
| Gabo | 1 |

### Magyarázat
- `GROUP BY Kiado` - kiadónként csoportosítunk
- `COUNT(*)` - megszámoljuk a könyveket csoportonként
- `ORDER BY Konyvek_szama DESC` - legtöbb könyvvel rendelkező elöl

---

## 🎬 Film adatbázis - Adatstruktúra

### Táblák

**Filmek tábla:**


| Film_ID | Cim | Megjelenes_ev | Ertekeles |
|---------|-----|---------------|-----------|
| 1 | Inception | 2010 | 8.8 |
| 2 | The Matrix | 1999 | 8.7 |
| 3 | Interstellar | 2014 | 8.6 |
| 4 | The Dark Knight | 2008 | 9.0 |

**Rendezo tábla:**


| Rendezo_ID | Nev | Szuletesi_ev |
|------------|-----|--------------|
| 1 | Christopher Nolan | 1970 |
| 2 | Wachowski testvérek | 1965 |

**Film_Rendezo tábla:**


| Film_ID | Rendezo_ID |
|---------|------------|
| 1 | 1 |
| 3 | 1 |
| 4 | 1 |
| 2 | 2 |

---

## 🎬 Feladat 3 - JOIN műveletek ⭐⭐

### Feladatok

**3.1** Listázd ki az összes film címét és rendezőjét!

**3.2** Kérdezd le Christopher Nolan filmjeit!

**3.3** Számold meg, hogy melyik rendezőnek hány filmje van!

**3.4** Listázd ki azokat a filmeket, amelyek értékelése 8.7 felett van, rendezővel együtt!

---

## 🎬 Megoldás 3.1 - Filmek és rendezők

### Feladat
Listázd ki az összes film címét és rendezőjét!

### Megoldás - WHERE módszer
```sql
SELECT Filmek.Cim, Rendezo.Nev
FROM Filmek, Film_Rendezo, Rendezo
WHERE Filmek.Film_ID = Film_Rendezo.Film_ID 
  AND Film_Rendezo.Rendezo_ID = Rendezo.Rendezo_ID;
```

### Megoldás - INNER JOIN módszer
```sql
SELECT Filmek.Cim, Rendezo.Nev
FROM Filmek
INNER JOIN Film_Rendezo ON Filmek.Film_ID = Film_Rendezo.Film_ID
INNER JOIN Rendezo ON Film_Rendezo.Rendezo_ID = Rendezo.Rendezo_ID;
```

### Eredmény


| Cim | Nev |
|-----|-----|
| Inception | Christopher Nolan |
| The Matrix | Wachowski testvérek |
| Interstellar | Christopher Nolan |
| The Dark Knight | Christopher Nolan |

---

## 🎬 Megoldás 3.2 - Nolan filmjei

### Feladat
Kérdezd le Christopher Nolan filmjeit!

### Megoldás
```sql
SELECT Filmek.Cim, Filmek.Megjelenes_ev, Filmek.Ertekeles
FROM Filmek
INNER JOIN Film_Rendezo ON Filmek.Film_ID = Film_Rendezo.Film_ID
INNER JOIN Rendezo ON Film_Rendezo.Rendezo_ID = Rendezo.Rendezo_ID
WHERE Rendezo.Nev = 'Christopher Nolan'
ORDER BY Filmek.Megjelenes_ev;
```

### Eredmény


| Cim | Megjelenes_ev | Ertekeles |
|-----|---------------|-----------|
| The Dark Knight | 2008 | 9.0 |
| Inception | 2010 | 8.8 |
| Interstellar | 2014 | 8.6 |

### Magyarázat
- JOIN-okkal összekapcsoljuk a táblákat
- WHERE-rel szűrünk a rendező nevére
- ORDER BY-jal rendezzük megjelenés szerint

---

## 🎬 Megoldás 3.3 - Rendezők filmszáma

### Feladat
Számold meg, hogy melyik rendezőnek hány filmje van!

### Megoldás
```sql
SELECT Rendezo.Nev, COUNT(*) AS Filmek_szama
FROM Rendezo
INNER JOIN Film_Rendezo ON Rendezo.Rendezo_ID = Film_Rendezo.Rendezo_ID
GROUP BY Rendezo.Nev
ORDER BY Filmek_szama DESC;
```

### Eredmény


| Nev | Filmek_szama |
|-----|--------------|
| Christopher Nolan | 3 |
| Wachowski testvérek | 1 |

### Magyarázat
- `GROUP BY Rendezo.Nev` - rendezőnként csoportosítunk
- `COUNT(*)` - filmek számolása csoportonként
- JOIN szükséges a kapcsolótábla miatt

---

## 🎬 Megoldás 3.4 - Legjobb filmek

### Feladat
Listázd ki azokat a filmeket, amelyek értékelése 8.7 felett van, rendezővel együtt!

### Megoldás
```sql
SELECT Filmek.Cim, Filmek.Ertekeles, Rendezo.Nev
FROM Filmek
INNER JOIN Film_Rendezo ON Filmek.Film_ID = Film_Rendezo.Film_ID
INNER JOIN Rendezo ON Film_Rendezo.Rendezo_ID = Rendezo.Rendezo_ID
WHERE Filmek.Ertekeles > 8.7
ORDER BY Filmek.Ertekeles DESC;
```

### Eredmény


| Cim | Ertekeles | Nev |
|-----|-----------|-----|
| The Dark Knight | 9.0 | Christopher Nolan |
| Inception | 8.8 | Christopher Nolan |

### Magyarázat
- WHERE szűrés az értékelésre (> 8.7)
- JOIN-okkal hozzákapcsoljuk a rendező nevét
- Csökkenő sorrendbe rendezzük értékelés szerint

---

## 🎮 Játékgyűjtemény - Adatstruktúra

### Táblák

**Jatekok tábla:**


| Jatek_ID | Cim | Platform | Mufaj | Ar | Kiadasev |
|----------|-----|----------|-------|-----|----------|
| 1 | The Witcher 3 | PC | RPG | 8000 | 2015 |
| 2 | FIFA 24 | PS5 | Sport | 15000 | 2023 |
| 3 | Minecraft | PC | Sandbox | 5000 | 2011 |
| 4 | GTA V | PC | Action | 7000 | 2013 |
| 5 | The Witcher 3 | PS5 | RPG | 9000 | 2015 |
| 6 | Cyberpunk 2077 | PC | RPG | 12000 | 2020 |
| 7 | FIFA 24 | Xbox | Sport | 15000 | 2023 |

---

## 🎮 Feladat 4 - Csoportosítás és szűrés ⭐⭐

### Feladatok

**4.1** Hány játék van platformonként?

**4.2** Mi a játékok átlagára műfajonként?

**4.3** Listázd ki azokat a műfajokat, ahol az átlagár több mint 8000 Ft!

**4.4** Melyik a legdrágább játék platformonként?

---

## 🎮 Megoldás 4.1 - Játékok platformonként

### Feladat
Hány játék van platformonként?

### Megoldás
```sql
SELECT Platform, COUNT(*) AS Jatekok_szama
FROM Jatekok
GROUP BY Platform
ORDER BY Jatekok_szama DESC;
```

### Eredmény


| Platform | Jatekok_szama |
|----------|---------------|
| PC | 4 |
| PS5 | 2 |
| Xbox | 1 |

### Magyarázat
- `GROUP BY Platform` - platformonként csoportosítunk
- `COUNT(*)` - játékok száma csoportonként
- `ORDER BY` - rendezés a legtöbb játékkal rendelkező platform elöl

---

## 🎮 Megoldás 4.2 - Átlagár műfajonként

### Feladat
Mi a játékok átlagára műfajonként?

### Megoldás
```sql
SELECT Mufaj, AVG(Ar) AS Atlag_ar, COUNT(*) AS Darab
FROM Jatekok
GROUP BY Mufaj
ORDER BY Atlag_ar DESC;
```

### Eredmény


| Mufaj | Atlag_ar | Darab |
|-------|----------|-------|
| Sport | 15000 | 2 |
| RPG | 9667 | 3 |
| Action | 7000 | 1 |
| Sandbox | 5000 | 1 |

### Magyarázat
- `AVG(Ar)` - átlagár számítása műfajonként
- `COUNT(*)` - hány játék van az adott műfajban
- RPG átlag: (8000 + 9000 + 12000) / 3 = 9667

---

## 🎮 Megoldás 4.3 - HAVING szűrés

### Feladat
Listázd ki azokat a műfajokat, ahol az átlagár több mint 8000 Ft!

### Megoldás
```sql
SELECT Mufaj, AVG(Ar) AS Atlag_ar
FROM Jatekok
GROUP BY Mufaj
HAVING AVG(Ar) > 8000
ORDER BY Atlag_ar DESC;
```

### Eredmény


| Mufaj | Atlag_ar |
|-------|----------|
| Sport | 15000 |
| RPG | 9667 |

### Magyarázat
- `HAVING AVG(Ar) > 8000` - szűrés csoportosítás **után**
- WHERE nem működne itt, mert az csoportosítás előtt szűr
- HAVING-et aggregált függvényekkel használjuk

**FONTOS:** WHERE vs HAVING
- **WHERE** = egyedi sorok szűrése (csoportosítás előtt)
- **HAVING** = csoportok szűrése (csoportosítás után)

---

## 🎮 Megoldás 4.4 - Legdrágább játék platformonként

### Feladat
Melyik a legdrágább játék platformonként?

### Megoldás
```sql
SELECT Platform, MAX(Ar) AS Legdragabb_ar
FROM Jatekok
GROUP BY Platform
ORDER BY Legdragabb_ar DESC;
```

### Eredmény


| Platform | Legdragabb_ar |
|----------|---------------|
| PS5 | 15000 |
| Xbox | 15000 |
| PC | 12000 |

### Bónusz - A játék címével együtt (Access)
```sql
SELECT Platform, Cim, Ar
FROM Jatekok
WHERE Ar IN (SELECT MAX(Ar) FROM Jatekok GROUP BY Platform);
```

---

## 👥 Diák-Tantárgy - Adatstruktúra

### Táblák

**Diakok tábla:**


| Diak_ID | Nev | Osztaly |
|---------|-----|---------|
| 1 | Kiss Anna | 10.A |
| 2 | Nagy Péter | 10.B |
| 3 | Tóth Eszter | 10.A |

**Tantargyak tábla:**

| Tantargy_ID | Nev |
|-------------|-----|
| 101 | Matematika |
| 102 | Informatika |
| 103 | Történelem |

**Jegyek tábla:**

| Jegy_ID | Diak_ID | Tantargy_ID | Jegy | Datum |
|---------|---------|-------------|------|--------|
| 1 | 1 | 101 | 5 | 2024-11-10 |
| 2 | 1 | 102 | 4 | 2024-11-15 |
| 3 | 2 | 101 | 3 | 2024-11-12 |
| 4 | 2 | 103 | 5 | 2024-11-20 |
| 5 | 3 | 101 | 5 | 2024-11-11 |
| 6 | 3 | 102 | 5 | 2024-11-16 |
| 7 | 1 | 101 | 4 | 2024-12-01 |

---

## 👥 Feladat 5 - Komplex lekérdezések ⭐⭐⭐

### Feladatok

**5.1** Listázd ki minden diák átlagát!

**5.2** Kik azok a diákok, akiknek az átlaga 4.5 felett van?

**5.3** Tantárgyanként mennyi a jegyek átlaga?

**5.4** Listázd ki minden diák nevét, tantárgyát és jegyét!

**5.5** Ki kapta a legtöbb ötöst?

---

## 👥 Megoldás 5.1 - Diákok átlaga

### Feladat
Listázd ki minden diák átlagát!

### Megoldás
```sql
SELECT Diakok.Nev, AVG(Jegyek.Jegy) AS Atlag
FROM Diakok
INNER JOIN Jegyek ON Diakok.Diak_ID = Jegyek.Diak_ID
GROUP BY Diakok.Nev
ORDER BY Atlag DESC;
```

### Eredmény

| Nev | Atlag |
|-----|-------|
| Tóth Eszter | 5.00 |
| Kiss Anna | 4.33 |
| Nagy Péter | 4.00 |

### Magyarázat
- JOIN összekapcsolja a Diakok és Jegyek táblákat
- GROUP BY Diakok.Nev - diákonként csoportosítunk
- AVG(Jegyek.Jegy) - átlag számítása diákonként
- Kiss Anna: (5+4+4)/3 = 4.33

---

## 👥 Megoldás 5.2 - Jó átlagú diákok

### Feladat
Kik azok a diákok, akiknek az átlaga 4.5 felett van?

### Megoldás
```sql
SELECT Diakok.Nev, AVG(Jegyek.Jegy) AS Atlag
FROM Diakok
INNER JOIN Jegyek ON Diakok.Diak_ID = Jegyek.Diak_ID
GROUP BY Diakok.Nev
HAVING AVG(Jegyek.Jegy) > 4.5
ORDER BY Atlag DESC;
```

### Eredmény

| Nev | Atlag |
|-----|-------|
| Tóth Eszter | 5.00 |

### Magyarázat
- HAVING AVG(Jegyek.Jegy) > 4.5 - szűrés az átlag után
- WHERE nem működne, mert az átlag csak csoportosítás után számítódik ki
- Csak Tóth Eszter felel meg a feltételnek (5.0 > 4.5)

---

## 👥 Megoldás 5.3 - Átlag tantárgyanként

### Feladat
Tantárgyanként mennyi a jegyek átlaga?

### Megoldás
```sql
SELECT Tantargyak.Nev, AVG(Jegyek.Jegy) AS Atlag, COUNT(*) AS Jegyek_szama
FROM Tantargyak
INNER JOIN Jegyek ON Tantargyak.Tantargy_ID = Jegyek.Tantargy_ID
GROUP BY Tantargyak.Nev
ORDER BY Atlag DESC;
```

### Eredmény

| Nev | Atlag | Jegyek_szama |
|-----|-------|--------------|
| Történelem | 5.00 | 1 |
| Informatika | 4.50 | 2 |
| Matematika | 4.25 | 4 |

### Magyarázat
- Tantárgyanként csoportosítunk
- Matematika: (5+3+5+4)/4 = 4.25
- Informatika: (4+5)/2 = 4.5
- Történelem: 5/1 = 5.0

---

## 👥 Megoldás 5.4 - Teljes lista

### Feladat
Listázd ki minden diák nevét, tantárgyát és jegyét!

### Megoldás
```sql
SELECT Diakok.Nev, Tantargyak.Nev AS Tantargy, Jegyek.Jegy, Jegyek.Datum
FROM Jegyek
INNER JOIN Diakok ON Jegyek.Diak_ID = Diakok.Diak_ID
INNER JOIN Tantargyak ON Jegyek.Tantargy_ID = Tantargyak.Tantargy_ID
ORDER BY Diakok.Nev, Jegyek.Datum;
```

### Eredmény (részlet)
| Nev | Tantargy | Jegy | Datum |
|-----|----------|------|--------|
| Kiss Anna | Matematika | 5 | 2024-11-10 |
| Kiss Anna | Informatika | 4 | 2024-11-15 |
| Kiss Anna | Matematika | 4 | 2024-12-01 |
| Nagy Péter | Matematika | 3 | 2024-11-12 |
| ... | ... | ... | ... |

### Magyarázat
- Két JOIN: Diakok és Tantargyak csatlakoztatása
- AS Tantargy - átnevezés, hogy ne legyen két "Nev" oszlop
- Rendezés név, majd dátum szerint

---

## 👥 Megoldás 5.5 - Legtöbb ötös

### Feladat
Ki kapta a legtöbb ötöst?

### Megoldás
```sql
-- MS Access
SELECT TOP 1 Diakok.Nev, COUNT(*) AS Otosok_szama
FROM Diakok
INNER JOIN Jegyek ON Diakok.Diak_ID = Jegyek.Diak_ID
WHERE Jegyek.Jegy = 5
GROUP BY Diakok.Nev
ORDER BY Otosok_szama DESC;

-- MySQL/PostgreSQL
SELECT Diakok.Nev, COUNT(*) AS Otosok_szama
FROM Diakok
INNER JOIN Jegyek ON Diakok.Diak_ID = Jegyek.Diak_ID
WHERE Jegyek.Jegy = 5
GROUP BY Diakok.Nev
ORDER BY Otosok_szama DESC
LIMIT 1;
```

### Eredmény

| Nev | Otosok_szama |
|-----|--------------|
| Tóth Eszter | 2 |

---

## 🏪 Webshop - Adatstruktúra

### Táblák

**Ugyfelek tábla:**

| Ugyfel_ID | Nev | Email | Varos |
|-----------|-----|-------|-------|
| 1 | Kovács János | kovacs@email.hu | Budapest |
| 2 | Szabó Éva | szabo@email.hu | Debrecen |
| 3 | Molnár Gábor | molnar@email.hu | Budapest |

**Termekek tábla:**

| Termek_ID | Nev | Kategoria | Ar |
|-----------|-----|-----------|-----|
| 1 | Laptop | Elektronika | 250000 |
| 2 | Egér | Elektronika | 5000 |
| 3 | Könyv | Média | 3500 |
| 4 | Fejhallgató | Elektronika | 15000 |

**Rendelesek tábla:**

| Rendeles_ID | Ugyfel_ID | Termek_ID | Mennyiseg | Datum |
|-------------|-----------|-----------|-----------|--------|
| 1 | 1 | 1 | 1 | 2024-11-01 |
| 2 | 1 | 2 | 2 | 2024-11-05 |
| 3 | 2 | 3 | 3 | 2024-11-10 |
| 4 | 3 | 4 | 1 | 2024-11-15 |
| 5 | 1 | 4 | 2 | 2024-12-01 |

---

## 🏪 Feladat 6 - Valós feladatok ⭐⭐⭐

### Feladatok

**6.1** Mennyi bevételt hozott összesen a webshop?

**6.2** Ki költötte a legtöbb pénzt?

**6.3** Melyik kategóriából adtak el a legtöbbet?

**6.4** Kik azok a vásárlók, akik több mint 100 000 Ft-ért rendeltek összesen?

**6.5** Listázd ki városonként az összes vásárlást!

---

## 🏪 Megoldás 6.1 - Összbevétel

### Feladat
Mennyi bevételt hozott összesen a webshop?

### Megoldás
```sql
SELECT SUM(Termekek.Ar * Rendelesek.Mennyiseg) AS Ossz_bevetel
FROM Rendelesek
INNER JOIN Termekek ON Rendelesek.Termek_ID = Termekek.Termek_ID;
```

### Eredmény

| Ossz_bevetel |
|--------------|
| 300500 |

### Számítás
- Laptop: 250000 × 1 = 250000
- Egér: 5000 × 2 = 10000
- Könyv: 3500 × 3 = 10500
- Fejhallgató: 15000 × 1 = 15000
- Fejhallgató: 15000 × 2 = 30000
- **Összesen: 315500** (javított!)

---

## 🏪 Megoldás 6.2 - Legnagyobb vásárló

### Feladat
Ki költötte a legtöbb pénzt?

### Megoldás
```sql
-- MS Access
SELECT TOP 1 Ugyfelek.Nev, 
       SUM(Termekek.Ar * Rendelesek.Mennyiseg) AS Osszeg
FROM Rendelesek
INNER JOIN Ugyfelek ON Rendelesek.Ugyfel_ID = Ugyfelek.Ugyfel_ID
INNER JOIN Termekek ON Rendelesek.Termek_ID = Termekek.Termek_ID
GROUP BY Ugyfelek.Nev
ORDER BY Osszeg DESC;
```

### Eredmény

| Nev | Osszeg |
|-----|--------|
| Kovács János | 290000 |

### Számítás
- Kovács János: 250000 + 10000 + 30000 = 290000
- Szabó Éva: 10500
- Molnár Gábor: 15000

---

## 🏪 Megoldás 6.3 - Legjobb kategória

### Feladat
Melyik kategóriából adtak el a legtöbbet?

### Megoldás
```sql
SELECT Termekek.Kategoria, 
       SUM(Termekek.Ar * Rendelesek.Mennyiseg) AS Bevetel,
       SUM(Rendelesek.Mennyiseg) AS Darab
FROM Rendelesek
INNER JOIN Termekek ON Rendelesek.Termek_ID = Termekek.Termek_ID
GROUP BY Termekek.Kategoria
ORDER BY Bevetel DESC;
```

### Eredmény

| Kategoria | Bevetel | Darab |
|-----------|---------|-------|
| Elektronika | 305000 | 6 |
| Média | 10500 | 3 |

### Magyarázat
- Elektronika: Laptop + Egér + Fejhallgató (kétszer)
- Média: csak a Könyv

---

## 🏪 Megoldás 6.4 - Nagy vásárlók

### Feladat
Kik azok a vásárlók, akik több mint 100 000 Ft-ért rendeltek összesen?

### Megoldás
```sql
SELECT Ugyfelek.Nev, 
       SUM(Termekek.Ar * Rendelesek.Mennyiseg) AS Ossz_vasarlas
FROM Rendelesek
INNER JOIN Ugyfelek ON Rendelesek.Ugyfel_ID = Ugyfelek.Ugyfel_ID
INNER JOIN Termekek ON Rendelesek.Termek_ID = Termekek.Termek_ID
GROUP BY Ugyfelek.Nev
HAVING SUM(Termekek.Ar * Rendelesek.Mennyiseg) > 100000
ORDER BY Ossz_vasarlas DESC;
```

### Eredmény

| Nev | Ossz_vasarlas |
|-----|---------------|
| Kovács János | 290000 |

### Magyarázat
- HAVING szűrés a csoportosított összeg alapján
- Csak Kovács János lépte túl a 100 000 Ft-ot

---

## 🏪 Megoldás 6.5 - Vásárlások városonként

### Feladat
Listázd ki városonként az összes vásárlást!

### Megoldás
```sql
SELECT Ugyfelek.Varos, 
       COUNT(*) AS Rendelesek_szama,
       SUM(Termekek.Ar * Rendelesek.Mennyiseg) AS Ossz_bevetel
FROM Rendelesek
INNER JOIN Ugyfelek ON Rendelesek.Ugyfel_ID = Ugyfelek.Ugyfel_ID
INNER JOIN Termekek ON Rendelesek.Termek_ID = Termekek.Termek_ID
GROUP BY Ugyfelek.Varos
ORDER BY Ossz_bevetel DESC;
```

### Eredmény

| Varos | Rendelesek_szama | Ossz_bevetel |
|-------|------------------|--------------|
| Budapest | 4 | 305000 |
| Debrecen | 1 | 10500 |

### Magyarázat
- Budapest: Kovács János + Molnár Gábor
- Debrecen: Szabó Éva

---

## 💡 Tippek és trükkök

### Gyakori hibák

**1. WHERE vs HAVING**
```sql
-- ❌ ROSSZ - aggregált függvény WHERE-ben
SELECT Osztaly, AVG(Jegy) 
FROM Diakok 
WHERE AVG(Jegy) > 4;

-- ✅ JÓ - aggregált függvény HAVING-ben
SELECT Osztaly, AVG(Jegy) 
FROM Diakok 
GROUP BY Osztaly
HAVING AVG(Jegy) > 4;
```

**2. GROUP BY minden nem aggregált oszlopra**
```sql
-- ❌ ROSSZ
SELECT Nev, Osztaly, COUNT(*) 
FROM Diakok 
GROUP BY Osztaly;

-- ✅ JÓ
SELECT Nev, Osztaly, COUNT(*) 
FROM Diakok 
GROUP BY Nev, Osztaly;
```

---

## 💡 Tippek és trükkök 2

### Hasznos technikák

**3. Aliasok használata**
```sql
-- Olvashatóbb lekérdezés
SELECT 
    d.Nev AS Diak_neve,
    t.Nev AS Tantargy_neve,
    j.Jegy
FROM Diakok AS d
INNER JOIN Jegyek AS j ON d.Diak_ID = j.Diak_ID
INNER JOIN Tantargyak AS t ON j.Tantargy_ID = t.Tantargy_ID;
```

**4. COUNT vs COUNT(oszlop)**
```sql
-- COUNT(*) - minden sort számol (NULL-okkal együtt)
SELECT COUNT(*) FROM Diakok;

-- COUNT(oszlop) - csak a nem NULL értékeket
SELECT COUNT(Email) FROM Diakok;
```

---

## 💡 Tippek és trükkök 3

### Optimalizálási tippek

**5. Csak a szükséges oszlopokat kérd le**
```sql
-- ❌ Lassabb, több adat
SELECT * FROM Diakok;

-- ✅ Gyorsabb, kevesebb adat
SELECT Nev, Osztaly FROM Diakok;
```

**6. Index használata**
- Elsődleges kulcsok automatikusan indexeltek
- Gyakran használt WHERE feltételekhez érdemes index
- JOIN-okban szereplő oszlopok indexelése gyorsít

**7. LIMIT/TOP használata nagy táblákban**
```sql
-- Első 100 rekord gyors lekérdezése
SELECT TOP 100 * FROM NagyTabla;  -- Access
SELECT * FROM NagyTabla LIMIT 100; -- MySQL
```

---

## 📝 Gyakorló feladatok - Próbáld ki!

### Könyvtár adatbázis

**1.** Listázd ki az Európa kiadó könyveit!

**2.** Melyik szerző könyvei a legdrágábbak átlagosan?

**3.** Hányszor kölcsönözték ki a "Harry Potter" című könyvet?

### Film adatbázis

**4.** Melyik a legrégebbi film az adatbázisban?

**5.** Listázd ki az éveket és hogy hány film jelent meg akkor!

### Játékgyűjtemény

**6.** Melyik platformon a legolcsóbb a játékok átlagára?

**7.** Hány RPG játék került ki 2015 után?

---

## 🎯 Bónusz feladat - Mindent egyben! ⭐⭐⭐

### Összetett feladat

Készíts egy lekérdezést, amely:
- Listázza ki azokat a **diákokat**, akiknek
- **Matematikából** az átlaga legalább **4.0**
- ÉS legalább **2 jegyük** van ebből a tantárgyból
- Rendezd őket átlag szerint csökkenő sorrendbe!

### Megoldás a következő dián...

---

## 🎯 Bónusz feladat - Megoldás

### Lekérdezés
```sql
SELECT 
    Diakok.Nev,
    AVG(Jegyek.Jegy) AS Matek_atlag,
    COUNT(*) AS Jegyek_szama
FROM Diakok
INNER JOIN Jegyek ON Diakok.Diak_ID = Jegyek.Diak_ID
INNER JOIN Tantargyak ON Jegyek.Tantargy_ID = Tantargyak.Tantargy_ID
WHERE Tantargyak.Nev = 'Matematika'
GROUP BY Diakok.Nev
HAVING AVG(Jegyek.Jegy) >= 4.0 AND COUNT(*) >= 2
ORDER BY Matek_atlag DESC;
```

### Eredmény

| Nev | Matek_atlag | Jegyek_szama |
|-----|-------------|--------------|
| Kiss Anna | 4.5 | 2 |

### Magyarázat
- WHERE szűri a tantárgyat
- GROUP BY diákonként csoportosít
- HAVING szűri az átlagot ÉS a jegyek számát
- Csak Kiss Anna felel meg (2 matek jegy: 5 és 4, átlag 4.5)

---

## Összefoglalás

### Mit gyakoroltunk?

✅ **Alapműveletek**: SELECT, WHERE, ORDER BY  
✅ **Aggregált függvények**: COUNT, AVG, SUM, MIN, MAX  
✅ **Csoportosítás**: GROUP BY, HAVING  
✅ **Összekapcsolások**: INNER JOIN, többszörös JOIN  
✅ **Szűrések**: WHERE, HAVING, LIKE  
✅ **Rendezés**: ORDER BY ASC/DESC  
✅ **Korlátozás**: TOP, LIMIT

### Következő lépések
1. 🔄 Gyakorold újra ezeket a feladatokat
2. 💡 Gondolj ki saját példákat
3. 🎓 Próbáld ki MS Access-ben vagy MySQL-ben
4. 🏆 Készíts saját adatbázist egy hobbiról

---

## Köszönöm a figyelmet!

### Jó gyakorlást! 💪

**Hasznos források:**
- W3Schools SQL: w3schools.com/sql
- SQLZoo: sqlzoo.net
- HackerRank SQL: hackerrank.com/domains/sql

**Ne feledd:**
- A gyakorlás a legfontosabb! 🎯
- Hibázni emberi - tanulj belőle! 📚
- Kérdezz, ha elakadtál! 🙋

---
