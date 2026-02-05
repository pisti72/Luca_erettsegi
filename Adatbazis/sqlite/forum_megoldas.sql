-- 2. Lekérdezés segítségével írassa ki a hírfolyamok megnevezését, valamint a moderátoruk 
-- vezeték- és utónevét az e-mail-címükkel együtt! (2felelos) 

SELECT megnevezes, veznev, utonev, email
FROM felhasznalo, hirfolyam
WHERE felhasznalo.id=moderator;

-- 3. Az adatbázis a kerékpáros közlekedéssel kapcsolatos fórum adatait tartalmazza. Lekérdezés 
-- segítségével írassa ki azoknak az üzeneteknek a tartalmát, amelyekben szerepel a „bike”
-- vagy a „bicikli” szó vagy szórészlet! (3hajtas)

SELECT tartalom
FROM uzenet
WHERE tartalom LIKE '%bike%' OR tartalom LIKE '%bicikli%';

-- 4. Adja meg lekérdezéssel a névrokon felhasználók vezeték- és utónevét! A névrokonok 
-- vezeték- és utóneve is azonos, de ők különböző személyek. A listában minden név 
-- ábécésorrendben jelenjen meg, de csak egyszer! (4nevrokon) 

SELECT veznev, utonev
FROM felhasznalo
GROUP BY veznev, utonev
HAVING COUNT(*)>1
ORDER BY veznev, utonev;


SELECT DISTINCT f1.veznev, f1.utonev
FROM felhasznalo AS f1, felhasznalo AS f2
WHERE f1.veznev=f2.veznev AND f1.utonev=f2.utonev AND f1.id<>f2.id
ORDER BY f1.veznev, f1.utonev;

-- 5. Készítsen lekérdezést, amely meghatározza, hogy hírfolyamonként hány üzenet érkezett 
-- a fórumba! A hírfolyamok neve és az üzenetek száma jelenjen meg, utóbbi szerint csökkenő 
-- sorrendben! (5forgalom)

SELECT megnevezes, COUNT(uzenet.id)
FROM uzenet, hirfolyam
WHERE h_id=hirfolyam.id
GROUP BY hirfolyam.id
ORDER BY 2 DESC;

-- 6. Vannak olyan hozzászólások, amelyek bevezető szövege valamelyik hírfolyam címét (nem 
-- feltétlenül azt, amelyikben megjelent) is tartalmazza. Adja meg lekérdezés segítségével az 
-- ilyen üzenetet küldők vezeték- és utónevét, a hozzászólásuk bevezető szövegét és küldési 
-- idejét! (6cimtartalom)

SELECT veznev, utonev, tartalom, kuldido
FROM felhasznalo, uzenet, hirfolyam
WHERE felhasznalo.id=f_id AND tartalom LIKE CONCAT('%',megnevezes,'%');

-- SQLite:

SELECT veznev, utonev, tartalom, kuldido
FROM felhasznalo, uzenet, hirfolyam
WHERE felhasznalo.id=f_id AND tartalom LIKE ('%' || megnevezes || '%');

-- 7. Lekérdezés segítségével írassa ki, hogy a vizsgált napon hány felhasználó szólt hozzá 
-- a fórumhoz! A többször is hozzászólókat csak egyszer vegye figyelembe! (7napiszam) 

SELECT COUNT(DISTINCT f_id)
FROM uzenet;

SELECT COUNT(*)
FROM (
	SELECT f_id
	FROM uzenet
	GROUP BY f_id
	) AS egyedi;

-- 8. A fórumnak vannak olyan tagjai, akik már nem aktívak, azaz régóta nem szóltak hozzá. 
-- Készítsen lekérdezést, amely meghatározza azoknak a vezeték- és utónevét, akik utoljára 
-- 2010 előtt szóltak hozzá, és a vizsgált napon sem küldtek üzenetet! (8inaktivak) 

SELECT veznev, utonev
FROM felhasznalo
WHERE utolso<'2010-01-01' AND
	id NOT IN (SELECT f_id FROM uzenet);

-- 9. Adja meg lekérdezéssel azoknak a felhasználóknak a vezeték- és utónevét, valamint 
-- üzeneteik számát, akik az „e-bike” hírfolyamban írtak ezen a napon 12:00 és 16:00 óra 
-- között, a határokat is beleszámolva! (9elektromos) 

SELECT veznev, utonev, COUNT(*)
FROM felhasznalo, uzenet, hirfolyam
WHERE felhasznalo.id=f_id AND hirfolyam.id=h_id AND megnevezes='e-bike' AND
	kuldido BETWEEN '12:00:00' AND '16:00:00'
GROUP BY uzenet.f_id;

-- 10. Lekérdezés segítségével írassa ki, hogy a vizsgált napi első üzenet írója aznap milyen 
-- időpontban küldte be az utolsó üzenetét! Feltételezhetjük azt, hogy az elsőként érkezett 
-- üzenettel egyidőben másik üzenet nem érkezett. (10kezdo) 

SELECT kuldido
FROM uzenet
WHERE f_id=(
	SELECT f_id
	FROM uzenet
	ORDER BY kuldido
	LIMIT 1
	)
ORDER BY kuldido DESC
LIMIT 1;


SELECT Max(kuldido)
FROM uzenet
WHERE f_id=(
	SELECT f_id
	FROM uzenet
	ORDER BY kuldido
	LIMIT 1
	);


SELECT MAX(uzenet.kuldido)
FROM uzenet
WHERE uzenet.f_id = (SELECT uzenet.f_id
					FROM uzenet
					WHERE uzenet.kuldido =
						(SELECT MIN(uzenet.kuldido)
						FROM uzenet));







