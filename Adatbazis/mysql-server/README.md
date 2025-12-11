# MySQL/MariaDB Gyakorló Környezet

## 🚀 Gyors indítás

```bash
# Konténerek indítása
docker-compose up -d

# Logok megtekintése
docker-compose logs -f

# Leállítás
docker-compose down
```

## 🌐 Elérés

- **phpMyAdmin**: http://localhost:8080
- **PHP Teszt Oldal**: http://localhost:8081
- **MariaDB**: localhost:3306

## 🔐 Belépési adatok

**Admin:**
- Felhasználónév: `root`
- Jelszó: `rootpassword`

**Tanuló:**
- Felhasználónév: `tanulo`
- Jelszó: `tanulo123`

## 📊 Adatbázisok

- `konyvtar` - könyvek és kölcsönzések
- `filmek` - filmek és rendezők
- `webshop` - ügyfelek, termékek, rendelések

## 🧪 Tesztelés

```bash
# MariaDB CLI
docker exec -it adatbazis-mariadb mysql -u root -prootpassword

# SQL futtatása
docker exec -it adatbazis-mariadb mysql -u tanulo -ptanulo123 -e "SELECT * FROM konyvtar.konyvek;"
```

További információk: `../LOCAL_PHP_MYADMIN.md`
