# Érettségi

## Megoszlás

1A Dokumentumkészítés                   35 pont
1B Táblázatkezelés
2  Adatbázis-kezelés                    35 pont
3  Algoritmizálás és programozás        50 pont
------------------------------------------------
Összesen:                              120 pont



## 3. Sebesség 

Ha közúti járművel utazunk, figyelemmel kísérhetjük a sofőr tevékenységét, aki az 
útviszonyoknak megfelelően és a KRESZ szabályait követve hol lassítja, hol gyorsítja az autót. 
Személygépjármű esetén a KRESZ szabályai a következők: lakott településen 50 km/h, azon 
kívül 90 km/h a megengedett sebesség. Ezt az általános szabályt felülírhatják a közúti 
jelzőtáblák, így egy veszélyes kanyarnál alacsonyabb sebességet is előírhatnak, lakott területen 
belül pedig akár magasabb sebességet is engedélyezhetnek. A jelzőtábla által megadott 
maximális sebességet egy másik jelzőtábla, de egy útkereszteződés is törli, visszaállítva ezzel 
az alapértelmezett sebességhatárt. 

105601
1111 70
1242 #
1803 #
2520 Varos301
3900 60
4100 40
5300 %
5830 ]
5900 30
6110 #
6921 Varos702
7120 ]
13505 Varos403

Az __ut.txt__ fájl egy autóutat és autópályát nem tartalmazó útszakasz sebességhatárt 
megszabó adatait tartalmazza. A fájl első sora azt a méterben kifejezett távolságot adja meg, 
amilyen hosszát figyeltük az útnak. A további, legfeljebb 2000 sor mindegyike két értéket 
tartalmaz. Az első a megfigyelés kezdetétől mért, méterben kifejezett távolság, az attól 
szóközzel elválasztott második pedig többféle lehet: 
    * számérték: sebességkorlátozó táblát jelöl, megadja, hogy attól a ponttól ennyi 
         a sebességhatár (értéke 10 és 90 közötti egész lehet); 
    * legalább négy-, legfeljebb harminckarakteres szöveg: azon a ponton a megadott 
         nevű település kezdődik; 
    * záró szögletes zárójel (]) karakter: a település végét jelzi; 
    * kettőskereszt (#): bekötőutat vagy útkereszteződést jelöl; 
    * százalékjel (%): a sebességkorlátozás feloldását jelzi. 
Az adatok a távolság szerint növekvő sorrendben rendezettek. 

Egymást követően több sebességkorlátozó tábla is előfordulhat feloldó tábla nélkül. Feloldó 
tábla előtt közvetlenül biztosan sebességkorlátozó tábla van. 
Tudjuk, hogy a megfigyelés kezdete és vége az út településen kívüli pontja, valamint az út 
minden települést csak egyszer érint.

Készítsen programot, ami az alábbi kérdésekre válaszol! A program forráskódját mentse 
sebesseg néven! A program megírásakor a felhasználó által megadott adatok helyességét, 
érvényességét nem kell ellenőriznie. Ha nem egész számot kell beolvasnia vagy megjelenítenie, 
a tizedespont és a tizedesvessző használata egyaránt elfogadott. 

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre 
a feladat sorszámát (például: 2. feladat)! Ha a felhasználótól kér be adatot, jelenítse meg 
a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott. 
   1. Olvassa be és tárolja el az ut.txt állományban lévő adatokat! 
   2. Írja ki az úton található települések nevét! Minden település neve új sorban jelenjen meg! 
   3. Kérjen be a felhasználótól egy valós számot, amely megadja, hogy az út első hány km-es 
        szakaszát vizsgáljuk! Adja meg, hogy mi volt ezen a szakaszon a legalacsonyabb 
        sebességhatár! Figyeljen arra, hogy sebességhatárt nem csak sebességkorlátozó tábla 
        szabhat meg! Megoldását az 1, 2, …, 5 km-t megadva is tesztelje! 
   4. Adja meg, hogy a bemeneti fájlban rögzített út hány százaléka vezet településen belül! Az út 
       teljes hossza a bemeneti fájl első sorában található. Az eredményt kéttizedes pontossággal 
       írja a képernyőre! 
   5. Olvassa be egy település nevét, és adja meg, hogy a településen belül… 
       * … hány sebességkorlátozó tábla van; 
       * … milyen hosszan vezet az út!
   6. Adja meg a beolvasott településhez legközelebb eső település nevét! (Két település 
       távolsága alatt az úton korábbi település végének és a későbbi település kezdetének 
       különbségét értjük.) Ha a két szomszédos település távolsága egyezik, akkor a megfigyelés 
       kezdőpontjához közelebbit adja meg! Ügyeljen arra, hogy az első és az utolsó településnek 
       csak egy szomszédja van! Feltételezheti, hogy az út bemeneti fájl által leírt része legalább 
       két településen áthalad.

Minta a szöveges kimenetek kialakításához: 
	2. feladat 
	A települések neve: 
	Varos301 
	Varos702 
	Varos403 
	… 
	Varos513 
	Varos214 
	Varos115 
	3. feladat 
	Adja meg a vizsgált szakasz hosszát km-ben! 1.8 
	Az első 1.8 km-en 70 km/h volt a legalacsonyabb megengedett sebesség. 
	4. feladat 
	Az út 22.38 százaléka vezet településen belül. 
	5. feladat   
	Adja meg egy település nevét! Varos010 
	A sebességkorlátozó táblák száma: 4 
	Az út hossza a településen belül 2000 méter. 
	6. feladat 
	A legközelebbi település: Varos609
