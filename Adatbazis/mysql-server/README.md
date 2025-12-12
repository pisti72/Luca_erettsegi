# MySQL/MariaDB Gyakorló Környezet

## 🚀 Gyors indítás

### Docker használata (Windows/Mac/Linux)

```bash
# Konténerek indítása
docker-compose up -d

# Logok megtekintése
docker-compose logs -f

# Leállítás
docker-compose down
```

### Podman használata (Linux)

```bash
# Konténerek indítása
podman-compose up -d

# Logok megtekintése
podman-compose logs -f

# Leállítás
podman-compose down

# Teljes törlés (adatbázis adatokkal együtt)
podman-compose down -v
```

**Megjegyzés Podman használóknak:**
- A Podman rootless módban fut, ami biztonságosabb
- Az image-eket a `docker.io` registry-ből tölti le
- A konténerek a `~/.local/share/containers/` mappában tárolódnak

### WSL2 + Podman Windows alatt (AJÁNLOTT!)

**Miért érdemes WSL2-t használni Windows alatt?**
- ✅ Natív Linux környezet Windowson
- ✅ Jobb teljesítmény mint Docker Desktop
- ✅ Nincs szükség licenszre (Docker Desktop fizetős vállalati használatra)
- ✅ Könnyebb hibakeresés és terminál használat
- ✅ Rootless konténerek (biztonságosabb)
- ✅ Kevesebb erőforrás-igény

**WSL2 telepítése Windows 10/11 alatt:**

1. **PowerShell megnyitása rendszergazdaként** és WSL telepítése:
   ```powershell
   wsl --install
   ```
   
2. **Számítógép újraindítása**

3. **Ubuntu indítása** a Start menüből, majd felhasználónév és jelszó beállítása

4. **WSL frissítése** és alapcsomagok telepítése:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y podman podman-compose git
   ```

5. **Projekt klónozása WSL-ben:**
   ```bash
   # Windows fájlok elérése: /mnt/c/Users/...
   cd ~
   git clone https://github.com/pisti72/Luca_erettsegi.git
   cd Luca_erettsegi/Adatbazis/mysql-server
   ```

6. **Konténerek indítása:**
   ```bash
   podman-compose up -d
   ```

7. **Böngészőből elérhető:**
   - phpMyAdmin: http://localhost:8080
   - PHP oldal: http://localhost:8081

**Tipp:** A VS Code-ot használd WSL extensionnel, így közvetlenül a WSL környezetben tudsz dolgozni!

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

### Docker használatával:

```bash
# MariaDB CLI
docker exec -it adatbazis-mariadb mysql -u root -prootpassword

# SQL futtatása
docker exec -it adatbazis-mariadb mysql -u tanulo -ptanulo123 -e "SELECT * FROM konyvtar.konyvek;"
```

### Podman használatával:

```bash
# MariaDB CLI
podman exec -it adatbazis-mariadb mysql -u root -prootpassword

# SQL futtatása
podman exec -it adatbazis-mariadb mysql -u tanulo -ptanulo123 -e "SELECT * FROM konyvtar.konyvek;"

# Konténerek listázása
podman ps -a

# Konténer állapotának ellenőrzése
podman logs adatbazis-mariadb
```

## 🔧 Hibaelhárítás

### Podman alatt nem indul a konténer?

1. **Ellenőrizd, hogy a Podman telepítve van-e:**
   ```bash
   podman --version
   podman-compose --version
   ```

2. **Ellenőrizd a futó konténereket:**
   ```bash
   podman ps -a
   ```

3. **Töröld a régi konténereket és volume-okat:**
   ```bash
   podman-compose down -v
   podman system prune -a
   ```

4. **Újraindítás tiszta lappal:**
   ```bash
   podman-compose up -d --force-recreate
   ```

További információk: `../LOCAL_PHP_MYADMIN.md`
