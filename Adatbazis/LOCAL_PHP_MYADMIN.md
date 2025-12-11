# Lokális Adatbázis Gyakorló Környezet
## PHP + MariaDB + phpMyAdmin + Nginx Docker/Podman környezet

---

## 🎯 Mit fogsz kapni?

- **MariaDB** adatbázis szerver
- **phpMyAdmin** webes felület
- **Nginx** webszerver
- **PHP** backend
- Előre telepített gyakorló adatbázisok
- Minden egy gombnyomással indul!

---

## 📋 Előfeltételek

### Fedora telepítés

```bash
# Docker telepítése
sudo dnf install docker docker-compose -y

# Docker elindítása
sudo systemctl start docker
sudo systemctl enable docker

# Felhasználó hozzáadása a docker csoporthoz
sudo usermod -aG docker $USER

# Újra kell jelentkezni, vagy:
newgrp docker
```

### VAGY Podman használata (Fedora-n ajánlott)

```bash
# Podman már telepítve van Fedorán, de biztosra:
sudo dnf install podman podman-compose -y

# Podman-compose telepítése (ha nincs)
pip3 install --user podman-compose
```

---

## 📁 Projekt struktúra

Hozd létre a következő mappákat:

```bash
cd ~/Dokumentumok/Dev/adatbazis
mkdir -p mysql-server/{nginx,php,mariadb,sql-init}
cd mysql-server
```

A végső struktúra:

```
mysql-server/
├── docker-compose.yml
├── Dockerfile.nginx
├── Dockerfile.php
├── nginx/
│   └── default.conf
├── php/
│   └── index.php
├── mariadb/
│   └── (adatbázis fájlok - automatikusan generálódik)
└── sql-init/
    ├── 01-databases.sql
    ├── 02-konyvtar.sql
    ├── 03-filmek.sql
    └── 04-webshop.sql
```

---

## 🐳 Docker Compose konfiguráció

Hozd létre a `docker-compose.yml` fájlt:

```yaml
version: '3.8'

services:
  # MariaDB adatbázis
  mariadb:
    image: mariadb:11.2
    container_name: adatbazis-mariadb
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: gyakorlo_db
      MYSQL_USER: tanulo
      MYSQL_PASSWORD: tanulo123
    ports:
      - "3306:3306"
    volumes:
      - ./mariadb:/var/lib/mysql
      - ./sql-init:/docker-entrypoint-initdb.d
    networks:
      - adatbazis-network

  # phpMyAdmin webes felület
  phpmyadmin:
    image: phpmyadmin:5.2
    container_name: adatbazis-phpmyadmin
    restart: always
    environment:
      PMA_HOST: mariadb
      PMA_PORT: 3306
      PMA_USER: root
      PMA_PASSWORD: rootpassword
      UPLOAD_LIMIT: 50M
    ports:
      - "8080:80"
    depends_on:
      - mariadb
    networks:
      - adatbazis-network

  # PHP-FPM
  php:
    build:
      context: .
      dockerfile: Dockerfile.php
    container_name: adatbazis-php
    restart: always
    volumes:
      - ./php:/var/www/html
    networks:
      - adatbazis-network
    depends_on:
      - mariadb

  # Nginx webszerver
  nginx:
    build:
      context: .
      dockerfile: Dockerfile.nginx
    container_name: adatbazis-nginx
    restart: always
    ports:
      - "8081:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - ./php:/var/www/html
    depends_on:
      - php
    networks:
      - adatbazis-network

networks:
  adatbazis-network:
    driver: bridge

volumes:
  mariadb-data:
```

---

## 🔧 Nginx Dockerfile

Hozd létre a `Dockerfile.nginx` fájlt:

```dockerfile
FROM nginx:alpine

# Nginx alapértelmezett konfigurációjának törlése
RUN rm /etc/nginx/conf.d/default.conf

# Munkakönyvtár beállítása
WORKDIR /var/www/html

# Port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

---

## 🐘 PHP Dockerfile

Hozd létre a `Dockerfile.php` fájlt:

```dockerfile
FROM php:8.2-fpm-alpine

# MariaDB/MySQL PDO driver telepítése
RUN docker-php-ext-install pdo pdo_mysql mysqli

# Munkakönyvtár
WORKDIR /var/www/html

# Port
EXPOSE 9000

CMD ["php-fpm"]
```

---

## ⚙️ Nginx konfiguráció

Hozd létre a `nginx/default.conf` fájlt:

```nginx
server {
    listen 80;
    server_name localhost;
    
    root /var/www/html;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

---

## 🧪 PHP teszt oldal

Hozd létre a `php/index.php` fájlt:

```php
<?php
// Adatbázis kapcsolat tesztelése
$host = 'mariadb';
$db = 'gyakorlo_db';
$user = 'tanulo';
$pass = 'tanulo123';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8mb4", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    echo "<h1>Adatbázis Kapcsolat Sikeres! ✅</h1>";
    echo "<p>MariaDB verzió: " . $pdo->query('SELECT VERSION()')->fetchColumn() . "</p>";
    
    // Adatbázisok listázása
    $stmt = $pdo->query('SHOW DATABASES');
    echo "<h2>Elérhető adatbázisok:</h2><ul>";
    while ($row = $stmt->fetch(PDO::FETCH_NUM)) {
        echo "<li>{$row[0]}</li>";
    }
    echo "</ul>";
    
    // Könyvtár példa
    $stmt = $pdo->query('SELECT * FROM konyvtar.konyvek LIMIT 5');
    echo "<h2>Könyvek (példa):</h2>";
    echo "<table border='1' cellpadding='5'>";
    echo "<tr><th>ID</th><th>Cím</th><th>Szerző</th><th>Ár</th></tr>";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr>";
        echo "<td>{$row['konyv_id']}</td>";
        echo "<td>{$row['cim']}</td>";
        echo "<td>{$row['szerzo']}</td>";
        echo "<td>{$row['ar']} Ft</td>";
        echo "</tr>";
    }
    echo "</table>";
    
} catch(PDOException $e) {
    echo "<h1>Kapcsolódási hiba! ❌</h1>";
    echo "<p>Hiba: " . $e->getMessage() . "</p>";
}
?>

<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adatbázis Gyakorló Környezet</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 { color: #2c3e50; }
        table {
            background: white;
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th {
            background: #3498db;
            color: white;
            padding: 10px;
        }
        td { padding: 8px; }
        .links {
            margin: 30px 0;
            padding: 20px;
            background: white;
            border-radius: 8px;
        }
        .links a {
            display: inline-block;
            margin: 10px;
            padding: 10px 20px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .links a:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="links">
        <h2>🔗 Hasznos linkek:</h2>
        <a href="http://localhost:8080" target="_blank">📊 phpMyAdmin</a>
        <a href="http://localhost:8081" target="_blank">🌐 PHP Teszt Oldal</a>
    </div>
    
    <div class="links">
        <h2>🔐 Belépési adatok:</h2>
        <p><strong>phpMyAdmin:</strong></p>
        <ul>
            <li>Szerver: mariadb</li>
            <li>Felhasználónév: root VAGY tanulo</li>
            <li>Jelszó: rootpassword VAGY tanulo123</li>
        </ul>
    </div>
</body>
</html>
```

---

## 📊 SQL inicializáló fájlok

### 01-databases.sql

```sql
-- Adatbázisok létrehozása
CREATE DATABASE IF NOT EXISTS konyvtar CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS filmek CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS webshop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Jogosultságok
GRANT ALL PRIVILEGES ON konyvtar.* TO 'tanulo'@'%';
GRANT ALL PRIVILEGES ON filmek.* TO 'tanulo'@'%';
GRANT ALL PRIVILEGES ON webshop.* TO 'tanulo'@'%';
FLUSH PRIVILEGES;
```

### 02-konyvtar.sql

```sql
USE konyvtar;

-- Könyvek tábla
CREATE TABLE konyvek (
    konyv_id INT PRIMARY KEY AUTO_INCREMENT,
    cim VARCHAR(200) NOT NULL,
    szerzo VARCHAR(100) NOT NULL,
    kiado VARCHAR(100),
    ev INT,
    ar INT,
    INDEX idx_szerzo (szerzo),
    INDEX idx_ev (ev)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Kölcsönzések tábla
CREATE TABLE kolcsonzesek (
    kolcsonzes_id INT PRIMARY KEY AUTO_INCREMENT,
    konyv_id INT NOT NULL,
    kolcsonzo_nev VARCHAR(100) NOT NULL,
    datum DATE NOT NULL,
    FOREIGN KEY (konyv_id) REFERENCES konyvek(konyv_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Minta adatok
INSERT INTO konyvek (cim, szerzo, kiado, ev, ar) VALUES
('Harry Potter és a bölcsek köve', 'J.K. Rowling', 'Animus', 2000, 3500),
('1984', 'George Orwell', 'Európa', 1949, 2800),
('Egri csillagok', 'Gárdonyi Géza', 'Móra', 1901, 3200),
('A Gyűrűk Ura', 'J.R.R. Tolkien', 'Európa', 1954, 4500),
('Metro 2033', 'Dmitry Glukhovsky', 'Gabo', 2005, 3000),
('A kis herceg', 'Antoine de Saint-Exupéry', 'Móra', 1943, 2500),
('Állatfarm', 'George Orwell', 'Európa', 1945, 2600),
('Pál utcai fiúk', 'Molnár Ferenc', 'Móra', 1906, 2900);

INSERT INTO kolcsonzesek (konyv_id, kolcsonzo_nev, datum) VALUES
(1, 'Kiss Anna', '2024-11-15'),
(3, 'Nagy Péter', '2024-11-20'),
(1, 'Tóth Eszter', '2024-12-01'),
(5, 'Kiss Anna', '2024-12-05'),
(2, 'Szabó Márton', '2024-12-08');
```

### 03-filmek.sql

```sql
USE filmek;

-- Rendezők tábla
CREATE TABLE rendezo (
    rendezo_id INT PRIMARY KEY AUTO_INCREMENT,
    nev VARCHAR(100) NOT NULL,
    szuletesi_ev INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Filmek tábla
CREATE TABLE filmek (
    film_id INT PRIMARY KEY AUTO_INCREMENT,
    cim VARCHAR(200) NOT NULL,
    megjelenes_ev INT,
    ertekeles DECIMAL(3,1),
    INDEX idx_ev (megjelenes_ev)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Film-Rendező kapcsolótábla
CREATE TABLE film_rendezo (
    film_id INT NOT NULL,
    rendezo_id INT NOT NULL,
    PRIMARY KEY (film_id, rendezo_id),
    FOREIGN KEY (film_id) REFERENCES filmek(film_id),
    FOREIGN KEY (rendezo_id) REFERENCES rendezo(rendezo_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Minta adatok
INSERT INTO rendezo (nev, szuletesi_ev) VALUES
('Christopher Nolan', 1970),
('Wachowski testvérek', 1965),
('Quentin Tarantino', 1963),
('Steven Spielberg', 1946);

INSERT INTO filmek (cim, megjelenes_ev, ertekeles) VALUES
('Inception', 2010, 8.8),
('The Matrix', 1999, 8.7),
('Interstellar', 2014, 8.6),
('The Dark Knight', 2008, 9.0),
('Pulp Fiction', 1994, 8.9),
('Kill Bill', 2003, 8.2),
('Schindler listája', 1993, 9.0);

INSERT INTO film_rendezo (film_id, rendezo_id) VALUES
(1, 1), (3, 1), (4, 1),  -- Nolan filmjei
(2, 2),                   -- Wachowski
(5, 3), (6, 3),          -- Tarantino
(7, 4);                   -- Spielberg
```

### 04-webshop.sql

```sql
USE webshop;

-- Ügyfelek tábla
CREATE TABLE ugyfelek (
    ugyfel_id INT PRIMARY KEY AUTO_INCREMENT,
    nev VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    varos VARCHAR(50),
    INDEX idx_varos (varos)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Termékek tábla
CREATE TABLE termekek (
    termek_id INT PRIMARY KEY AUTO_INCREMENT,
    nev VARCHAR(200) NOT NULL,
    kategoria VARCHAR(50),
    ar INT NOT NULL,
    keszlet INT DEFAULT 0,
    INDEX idx_kategoria (kategoria)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Rendelések tábla
CREATE TABLE rendelesek (
    rendeles_id INT PRIMARY KEY AUTO_INCREMENT,
    ugyfel_id INT NOT NULL,
    termek_id INT NOT NULL,
    mennyiseg INT NOT NULL,
    datum DATE NOT NULL,
    FOREIGN KEY (ugyfel_id) REFERENCES ugyfelek(ugyfel_id),
    FOREIGN KEY (termek_id) REFERENCES termekek(termek_id),
    INDEX idx_datum (datum)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Minta adatok
INSERT INTO ugyfelek (nev, email, varos) VALUES
('Kovács János', 'kovacs.janos@email.hu', 'Budapest'),
('Szabó Éva', 'szabo.eva@email.hu', 'Debrecen'),
('Molnár Gábor', 'molnar.gabor@email.hu', 'Budapest'),
('Nagy Petra', 'nagy.petra@email.hu', 'Szeged');

INSERT INTO termekek (nev, kategoria, ar, keszlet) VALUES
('Laptop Dell XPS 13', 'Elektronika', 250000, 15),
('Logitech egér', 'Elektronika', 5000, 50),
('Harry Potter könyv', 'Média', 3500, 30),
('Sony fejhallgató', 'Elektronika', 15000, 25),
('Minecraft játék', 'Média', 5000, 40),
('Samsung monitor', 'Elektronika', 45000, 10);

INSERT INTO rendelesek (ugyfel_id, termek_id, mennyiseg, datum) VALUES
(1, 1, 1, '2024-11-01'),
(1, 2, 2, '2024-11-05'),
(2, 3, 3, '2024-11-10'),
(3, 4, 1, '2024-11-15'),
(1, 4, 2, '2024-12-01'),
(4, 5, 1, '2024-12-05'),
(2, 6, 1, '2024-12-08');
```

---

## 🚀 Indítás

### Docker használatával

```bash
# Konténerek építése és indítása
docker-compose up -d

# Logok megtekintése
docker-compose logs -f

# Leállítás
docker-compose down

# Leállítás és adatok törlése
docker-compose down -v
```

### Podman használatával

```bash
# Podman-compose használata
podman-compose up -d

# Logok
podman-compose logs -f

# Leállítás
podman-compose down

# VAGY Podman pod használata
podman pod create --name adatbazis-pod -p 8080:80 -p 8081:80 -p 3306:3306
```

---

## 🌐 Elérés

Miután elindítottad a konténereket:

- **phpMyAdmin**: http://localhost:8080
- **PHP Teszt Oldal**: http://localhost:8081
- **MariaDB**: `localhost:3306`

### Belépési adatok

**phpMyAdmin (Admin):**
- Felhasználónév: `root`
- Jelszó: `rootpassword`

**phpMyAdmin (Tanuló):**
- Felhasználónév: `tanulo`
- Jelszó: `tanulo123`

**MariaDB CLI kapcsolat:**

```bash
# Docker
docker exec -it adatbazis-mariadb mysql -u root -prootpassword

# Podman
podman exec -it adatbazis-mariadb mysql -u root -prootpassword
```

---

## 🧪 Tesztelés

### 1. phpMyAdmin tesztelés

1. Nyisd meg: http://localhost:8080
2. Jelentkezz be `root` / `rootpassword` adatokkal
3. Nézd meg a bal oldali menüben: `konyvtar`, `filmek`, `webshop` adatbázisokat
4. Futtass egy lekérdezést:

```sql
SELECT * FROM konyvtar.konyvek;
```

### 2. PHP kapcsolat tesztelése

1. Nyisd meg: http://localhost:8081
2. Látnod kell a MariaDB verziót és az adatbázisok listáját
3. Könyvek táblázatot

### 3. CLI tesztelés

```bash
# Belépés a MariaDB-be
docker exec -it adatbazis-mariadb mysql -u tanulo -ptanulo123

# Adatbázisok listázása
SHOW DATABASES;

# Könyvtár adatbázis használata
USE konyvtar;

# Könyvek lekérdezése
SELECT * FROM konyvek;

# Kilépés
EXIT;
```

---

## 🛠️ Hibaelhárítás

### Port foglalt

Ha a port már foglalt:

```bash
# Nézd meg mi használja a portokat
sudo ss -tulpn | grep :8080
sudo ss -tulpn | grep :3306

# docker-compose.yml-ben módosítsd:
ports:
  - "8082:80"  # phpMyAdmin új porton
  - "3307:3306"  # MariaDB új porton
```

### Konténerek nem indulnak

```bash
# Logok ellenőrzése
docker-compose logs mariadb
docker-compose logs phpmyadmin

# Konténerek újraindítása
docker-compose restart

# Teljes újraépítés
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Adatbázis kapcsolati hiba

```bash
# MariaDB állapot ellenőrzése
docker exec -it adatbazis-mariadb mysqladmin -u root -prootpassword ping

# MariaDB újraindítása
docker-compose restart mariadb
```

### Jogosultsági problémák (Fedora/SELinux)

```bash
# SELinux átmeneti kikapcsolása (teszteléshez)
sudo setenforce 0

# VAGY mappák címkézése
sudo chcon -Rt svirt_sandbox_file_t ./mariadb
sudo chcon -Rt svirt_sandbox_file_t ./php
```

---

## 📚 Következő lépések

### 1. Gyakorlás

- Próbáld ki a feladatok prezentációban szereplő SQL lekérdezéseket
- Hozz létre saját táblákat phpMyAdmin-ban
- Módosítsd a PHP oldalt, adj hozzá űrlapokat

### 2. További adatbázisok

Hozz létre saját adatbázist az `sql-init` mappában:

```bash
touch sql-init/05-sajat.sql
```

```sql
CREATE DATABASE IF NOT EXISTS sajat_db;
USE sajat_db;

CREATE TABLE pelda (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nev VARCHAR(100)
);
```

Majd indítsd újra:

```bash
docker-compose down -v
docker-compose up -d
```

### 3. Fejlesztés

- Készíts PHP CRUD alkalmazást
- Implementáld a feladatokat webes formában
- Adj hozzá Bootstrap CSS-t a szebb megjelenéshez

---

## 🔒 Biztonsági megjegyzések

⚠️ **FONTOS**: Ez a környezet csak **TANULÁSI CÉLOKRA** készült!

**NE használd éles környezetben:**
- Gyenge jelszavak
- Root hozzáférés mindenhol
- Nincs SSL/TLS
- Nincs tűzfal konfiguráció
- Nincs rate limiting

**Éles környezethez:**
- Erős jelszavak használata
- SSL/TLS tanúsítvány
- Korlátozott felhasználói jogok
- Tűzfal és biztonságos hálózati konfiguráció
- Rendszeres biztonsági frissítések

---

## 📖 Hasznos parancsok

```bash
# Konténerek listázása
docker ps

# Adatbázis mentése
docker exec adatbazis-mariadb mysqldump -u root -prootpassword --all-databases > backup.sql

# Adatbázis visszatöltése
docker exec -i adatbazis-mariadb mysql -u root -prootpassword < backup.sql

# Konténer bash shell
docker exec -it adatbazis-mariadb bash

# Nginx konfiguráció tesztelése
docker exec adatbazis-nginx nginx -t

# PHP verzió ellenőrzése
docker exec adatbazis-php php -v

# MariaDB teljesítmény statisztika
docker exec -it adatbazis-mariadb mysqladmin -u root -prootpassword status
```

---

## 📝 További források

- **Docker dokumentáció**: https://docs.docker.com/
- **Podman dokumentáció**: https://docs.podman.io/
- **MariaDB dokumentáció**: https://mariadb.org/documentation/
- **phpMyAdmin dokumentáció**: https://docs.phpmyadmin.net/
- **Nginx dokumentáció**: https://nginx.org/en/docs/

---

**Jó gyakorlást! 🚀**
