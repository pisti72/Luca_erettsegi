SELECT ingatlan.kozterulet 
FROM ingatlan 
GROUP BY kozterulet 
ORDER BY kozterulet ASC;
-----

-- Lekérdezés segítségével adja meg, hogy az „Agyagos utca” ingatlanjait milyen áron 
-- hirdették meg! Jelenítse meg a házszámot és a meghirdetéskor megadott árat! (3agyagos)
SELECT hazszam, ar 
FROM hirdetes, ingatlan
WHERE ingatlanid = ingatlan.id
AND kozterulet LIKE "%Agyagos%";
----

--Készítsen lekérdezést, amely megadja, hogy a közvetítő cég az itt szereplő ingatlanok 
-- eladásából mennyi bevételre tett szert 2021-ben, ha az eladási ár 1,5 százalékát mint 
--közvetítői díjat megkapta! (4dij) 
SELECT SUM(hirdetes.ar) * 1.5 / 100 AS "kozvetitoi dij"
FROM hirdetes
WHERE YEAR(hirdetes.datum) = 2021;

---

-- Lekérdezés segítségével adja meg, hogy a legdrágábban meghirdetett ingatlan ára 
-- hányszorosa volt a legolcsóbban meghirdetett ingatlan árának! Az árváltozásokat és 
-- az eladásokat ne vegye figyelembe! Adja meg az arányt kerekítés nélkül! (5arany) 

SELECT MAX(hirdetes.ar)/MIN(hirdetes.ar) AS "hányszorosa" 
FROM hirdetes;

---

SELECT kozterulet, hazszam, datum
FROM ingatlan, hirdetes
WHERE ingatlan.id=ingatlanid
GROUP BY ingatlan.id
HAVING Count(hirdetes.id)=1
ORDER BY datum
LIMIT 1;
