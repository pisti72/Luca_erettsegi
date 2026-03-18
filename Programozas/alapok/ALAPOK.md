# Python Alapok - Lépésről Lépésre Feladatsor

Itt egy fokozatos nehézségű feladatsor, amely segít a tanítványnak megérteni az algoritmikus gondolkodást. Minden feladat épít az előzőre.

## 1. Alapvető változó kezelés

### 1.1 Számokkal való munka
```python
# 1. Kérj be két számot a felhasználótól és írd ki az összegüket
# 2. Kérj be egy számot és írd ki a kétszeresét
# 3. Kérj be egy számot és mondd meg, páros-e vagy páratlan
```

### 1.2 Szöveggel való munka
```python
# 1. Kérj be a felhasználó nevét és köszönj neki
# 2. Kérj be egy szót és írd ki, hogy hány karakterből áll
# 3. Kérj be egy mondatot és írd ki minden szavát új sorba
```

## 2. Egyszerű elágazások (if-elif-else)

### 2.1 Egyszerű döntések
```python
# 1. Írj egy programot, amely bekér egy számot, majd kiírja, hogy pozitív, negatív vagy nulla
# 2. Kérj be egy életkort, és mondd meg, hogy a személy kiskorú, felnőtt vagy nyugdíjas
# 3. Kérj be egy jegyet (1-5), és írd ki a megfelelő szöveges értékelést
```

### 2.2 Összetettebb feltételek
```python
# 1. Kérj be 3 számot és írd ki a legnagyobbat
# 2. Kérj be egy évszámot és mondd meg, hogy szökőév-e
# 3. Egy tesztversenyen 0-100 pont szerezhető. 50 alatt elégtelen, 50-60 elégséges, 60-70 közepes, 70-85 jó, 85 felett jeles. Írj programot, ami bekér egy pontszámot és kiírja az osztályzatot.
```

## 3. Egyszerű ciklusok (for)

### 3.1 Számláló ciklusok
```python
# 1. Írd ki a számokat 1-től 10-ig
# 2. Írd ki a páros számokat 1 és 20 között
# 3. Kérj be egy számot és írd ki a számokat 0-tól addig a számig

# Segítség: for i in range(kezdőérték, végérték):
```

### 3.2 Szöveg bejárása
```python
# 1. Kérj be egy szót és írd ki betűnként külön sorban
# 2. Kérj be egy szót és számold meg, hány magánhangzó van benne (a, e, i, o, u)
# 3. Kérj be egy mondatot és írd ki szavanként külön sorban
```

## 4. While ciklusok

### 4.1 Feltételes ismétlés
```python
# 1. Kérj be számokat, amíg 0-t nem ír be. A végén írd ki a beírt számok összegét
# 2. Kitalálós játék: A gép "gondol" egy számra 1-10 között (használj random modult), a felhasználó találja ki. Addig kérdezd, amíg nem találja el.
# 3. Jelszó ellenőrző: Addig kérj be jelszót, amíg nem írja be helyesen a "python123"-at
```

## 5. Kombinált feladatok

### 5.1 Összetett algoritmusok
```python
# 1. Prímszám ellenőrző: Kérj be egy számot és mondd meg, hogy prímszám-e
# 2. Fibonacci sorozat: Írj ki n elemet a Fibonacci sorozatból (n-t kérj be)
# 3. Számkitaláló játék fordítva: A felhasználó gondol egy számra 1-100 között, a számítógép találja ki minél kevesebb lépésben
```

### 5.2 Gyakorlati alkalmazások
```python
# 1. Naplóvezető: Addig kérj be napi feladatokat, amíg nem írja be, hogy "vége". Majd írd ki az összes feladatot.
# 2. Egyszerű pénztárca: Lehessen bevinni kiadásokat (leírás, összeg), amíg nem írja be, hogy "kilép". A végén írja ki a teljes kiadást.
# 3. Szavak gyakorisága: Kérj be egy szöveget, majd számold meg, melyik betűből hány darab van benne
```

## Tanítási tippek:

1. **Kezdjük konkrét, kézzel fogható példákkal**:
   - Változó = doboz, amibe rakunk valamit
   - Elágazás = útkereszteződés, döntünk melyik úton megyünk tovább
   - Ciklus = ismétlődő feladat, mint az iskolai napok

2. **Rajzolj folyamatábrát** minden algoritmushoz papíron!

3. **Használjuk a debugging módot** vagy írj ki minden lépésben változók értékét:
   ```python
   print(f"Most i = {i}, összeg = {osszeg}")
   ```

4. **Bontsd részekre a feladatokat**:
   - Először írd meg csak a változódeklarációt
   - Majd a beolvasást
   - Utána a számítást
   - Végül a kiírást

5. **Példák a való életből**:
   - Bevásárlólista = lista változó
   - Kapucsengő = if (ha van otthon, akkor nyiss ajtót)
   - Zuhanyzás = while (amíg nem vagy tiszta, addig dörzsöld magad)
