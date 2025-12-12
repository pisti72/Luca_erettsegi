# Konténerek
## Modern alkalmazások futtatása

---

## Mi az a konténer?

### Definíció
- **Konténer**: egy elszigetelt, hordozható futtatási környezet alkalmazások számára
- Tartalmazza az alkalmazást és az összes szükséges függőséget
- Könnyűsúlyú virtualizációs technológia

### Miért hasznos?
- ✅ "Nálam működött!" probléma megoldása
- ✅ Gyors telepítés és indítás
- ✅ Erőforrás-hatékonyság
- ✅ Konzisztens környezet (fejlesztés → teszt → éles)

---

## Konténer vs Virtuális gép

### Virtuális gép (VM)
```
┌─────────────────────────────┐
│      Alkalmazás A           │
│  ┌──────────────────────┐   │
│  │   Vendég OS          │   │
│  └──────────────────────┘   │
│      Hypervisor             │
│      Gazda OS               │
│      Hardver                │
└─────────────────────────────┘
```

### Konténer
```
┌─────────────────────────────┐
│    Konténer A │ Konténer B  │
│  ┌──────────┐ │ ┌─────────┐ │
│  │   App    │ │ │   App   │ │
│  │ Libs     │ │ │ Libs    │ │
│  └──────────┘ │ └─────────┘ │
│   Container Runtime         │
│      Gazda OS               │
│      Hardver                │
└─────────────────────────────┘
```

---

## Konténer vs VM - Különbségek

| Tulajdonság | Virtuális gép | Konténer |
|------------|---------------|----------|
| **Méret** | GB-ok | MB-ok |
| **Indítási idő** | Percek | Másodpercek |
| **Erőforrás** | Több (teljes OS) | Kevesebb (megosztott kernel) |
| **Elszigeteltség** | Teljes | Folyamat szintű |
| **Teljesítmény** | Lassabb | Közel natív |
| **Hordozhatóság** | Korlátozott | Magas |

---

## Konténer használati esetek

### Fejlesztés
- Egységes fejlesztői környezet minden csapattagnak
- Gyors környezet felállítás új fejlesztőknek
- Több verzió párhuzamos futtatása

### Tesztelés
- Konzisztens tesztkörnyezet
- Gyors CI/CD pipeline-ok
- Izolált tesztek

### Éles környezet
- Mikroszolgáltatások (microservices)
- Skálázhatóság
- Egyszerű frissítések és visszaállítás

---

## Docker - A legnépszerűbb platform

### Mi az a Docker?
- A legelterjedtebb konténerplatform
- 2013-ban indult
- Egyszerűvé teszi a konténerek használatát

### Docker komponensek
- **Docker Engine**: konténerek futtatása
- **Docker Hub**: képfájlok tárolója (registry)
- **Docker Compose**: több konténer kezelése
- **Dockerfile**: képfájl leírása

---

## Docker alapfogalmak

### Image (Képfájl)
- Sablonok konténerek létrehozásához
- Rétegekből épül fel (layers)
- Nem változtatható (immutable)
- Példa: `nginx:latest`, `mysql:8.0`, `python:3.11`

### Container (Konténer)
- Image futó példánya
- Módosítható, de változások elvesznek leállításkor
- Lehet elindítani, leállítani, törölni

### Volume (Kötet)
- Adatok tartós tárolása
- Megmarad a konténer törlése után

---

## Dockerfile példa

```dockerfile
# Alapképfájl kiválasztása
FROM python:3.11-slim

# Munkamappa beállítása
WORKDIR /app

# Függőségek másolása
COPY requirements.txt .

# Függőségek telepítése
RUN pip install --no-cache-dir -r requirements.txt

# Alkalmazás fájljainak másolása
COPY . .

# Port megnyitása
EXPOSE 5000

# Indítási parancs
CMD ["python", "app.py"]
```

---

## Docker alapparancsok

### Képfájlok kezelése
```bash
docker pull nginx              # Képfájl letöltése
docker images                  # Helyi képfájlok listázása
docker build -t myapp:1.0 .   # Képfájl építése
docker rmi nginx               # Képfájl törlése
```

### Konténerek kezelése
```bash
docker run -d -p 80:80 nginx   # Konténer indítása
docker ps                      # Futó konténerek
docker ps -a                   # Összes konténer
docker stop my-container       # Konténer leállítása
docker rm my-container         # Konténer törlése
```

---

## Docker Compose

### Mi az?
- Több konténeres alkalmazások definiálása és futtatása
- YAML formátumú konfigurációs fájl
- Egyetlen paranccsal indítható az egész alkalmazás

### docker-compose.yml példa
```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
  
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: titkos123
    volumes:
      - db-data:/var/lib/mysql

volumes:
  db-data:
```

---

## Docker Compose parancsok

```bash
# Szolgáltatások indítása
docker compose up -d

# Naplók megtekintése
docker compose logs -f

# Szolgáltatások leállítása
docker compose down

# Újraépítés és indítás
docker compose up -d --build

# Futó szolgáltatások listázása
docker compose ps
```

---

## Podman - Docker alternatíva

### Mi az a Podman?
- **Pod Manager** - konténerkezelő eszköz
- Red Hat által fejlesztett
- Docker-kompatibilis parancsok
- Nyílt forráskódú

### Miért Podman?
- 🔒 **Daemonless**: nincs központi daemon folyamat
- 🔒 **Rootless**: futtatható normál felhasználóként
- 🔒 **Biztonságosabb** alapértelmezett beállítások
- 🐧 Jobban integrálódik Linux rendszerekkel

---

## Docker vs Podman

| Tulajdonság | Docker | Podman |
|------------|--------|--------|
| **Daemon** | Szükséges (dockerd) | Nincs daemon |
| **Root jogosultság** | Általában szükséges | Rootless mode |
| **Architektúra** | Client-Server | Fork-exec |
| **Podok támogatása** | ❌ | ✅ |
| **Systemd integráció** | Korlátozott | Natív |
| **Docker Compose** | Natív | podman-compose |
| **Kompatibilitás** | Docker API | Docker-kompatibilis |

---

## Podman alapparancsok

### Szinte ugyanazok, mint Docker!
```bash
# Képfájl letöltése
podman pull nginx

# Konténer futtatása
podman run -d -p 8080:80 nginx

# Futó konténerek
podman ps

# Konténer leállítása
podman stop my-container

# Képfájlok listázása
podman images
```

💡 **Tipp**: `alias docker=podman` - és ugyanúgy használható!

---

## Podman egyedi funkciók

### Podok (Pods)
- Több konténer egy csoportban
- Kubernetes-szerű koncepció
- Közös hálózati névtér

```bash
# Pod létrehozása
podman pod create --name mypod -p 8080:80

# Konténerek hozzáadása a podhoz
podman run -d --pod mypod nginx
podman run -d --pod mypod redis
```

### Systemd integráció
```bash
# Systemd service generálása
podman generate systemd --name mycontainer > mycontainer.service

# Service telepítése
sudo cp mycontainer.service /etc/systemd/system/
sudo systemctl enable --now mycontainer
```

---

## Rootless konténerek

### Mi az a rootless mode?
- Konténerek futtatása root jogosultság **nélkül**
- Nagyobb biztonság
- Csökkentett támadási felület

### Előnyök
- ✅ Nem kell sudo/root jogosultság
- ✅ Jobb izoláció
- ✅ Kisebb biztonsági kockázat
- ✅ Multi-user környezetekben ideális

### Podman rootless
```bash
# Automatikusan rootless módban fut
podman run -d nginx

# Rootless konténerek portjai
# 0-1023 portok nem érhetők el közvetlenül
podman run -d -p 8080:80 nginx  # ✅ OK
```

---

## Konténer registry-k

### Képfájlok tárolása és megosztása

| Registry | Leírás |
|----------|--------|
| **Docker Hub** | Hivatalos Docker registry (hub.docker.com) |
| **GitHub Container Registry** | GitHub-integrált (ghcr.io) |
| **Google Container Registry** | Google Cloud (gcr.io) |
| **Red Hat Quay** | Vállalati registry (quay.io) |
| **Privát registry** | Saját szerveren futtatott |

```bash
# Bejelentkezés registry-be
docker login

# Képfájl feltöltése
docker push username/myapp:1.0

# Letöltés más registry-ből
podman pull quay.io/podman/hello
```

---

## Konténer hálózatok

### Hálózati módok
- **Bridge**: Alapértelmezett, privát hálózat
- **Host**: Gazda hálózatát használja
- **None**: Nincs hálózat
- **Custom**: Egyedi hálózat létrehozása

```bash
# Egyedi hálózat létrehozása
docker network create mynetwork

# Konténer csatlakoztatása
docker run -d --network mynetwork --name app1 nginx
docker run -d --network mynetwork --name app2 alpine

# Hálózatok listázása
docker network ls
```

---

## Biztonság konténerekben

### Legjobb gyakorlatok
- 🔐 Ne futtass root felhasználóként
- 🔐 Használj hivatalos képfájlokat
- 🔐 Tartsd naprakészen a képfájlokat
- 🔐 Szkenneld a képfájlokat sebezhetőségekre
- 🔐 Korlátozd az erőforrásokat
- 🔐 Secrets kezelése környezeti változókkal vagy vault-tal

```dockerfile
# Jó példa - nem root felhasználó
FROM node:18-alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
WORKDIR /app
COPY --chown=appuser:appgroup . .
CMD ["node", "server.js"]
```

---

## Konténer monitoring

### Erőforrás-használat
```bash
# Konténer statisztikák
docker stats

# Egy konténer részletes információi
docker inspect mycontainer

# Logok megtekintése
docker logs -f mycontainer

# Konténerbe belépés
docker exec -it mycontainer /bin/bash
```

### Monitoring eszközök
- **Portainer**: Webes GUI konténerek kezeléséhez
- **cAdvisor**: Google konténer monitoring
- **Prometheus + Grafana**: Részletes metrikák

---

## Gyakorlati példa: Webszerver

```bash
# 1. Nginx konténer indítása
docker run -d \
  --name webserver \
  -p 8080:80 \
  -v $(pwd)/html:/usr/share/nginx/html:ro \
  nginx:alpine

# 2. HTML fájl létrehozása
echo '<h1>Hello Docker!</h1>' > html/index.html

# 3. Böngészőben: http://localhost:8080

# 4. Logok megtekintése
docker logs -f webserver

# 5. Leállítás és törlés
docker stop webserver
docker rm webserver
```

---

## Gyakorlati példa: Adatbázis

```bash
# MySQL konténer indítása
docker run -d \
  --name mysql-db \
  -e MYSQL_ROOT_PASSWORD=titkos123 \
  -e MYSQL_DATABASE=teszt_db \
  -v mysql-data:/var/lib/mysql \
  -p 3306:3306 \
  mysql:8.0

# Csatlakozás az adatbázishoz
docker exec -it mysql-db mysql -uroot -ptitkos123

# Adatbázis mentés
docker exec mysql-db mysqldump -uroot -ptitkos123 teszt_db > backup.sql

# Volume megmarad a konténer törlése után!
```

---

## Mikroszolgáltatások (Microservices)

### Konténerek ideálisak mikroszolgáltatásokhoz!

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │────▶│   API       │────▶│  Database   │
│  (Nginx)    │     │  (Python)   │     │  (MySQL)    │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                    │
       └───────────────────┴────────────────────┘
              docker compose network
```

### Előnyök
- Független fejlesztés és telepítés
- Könnyű skálázás
- Hibatűrés
- Technológiai függetlenség

---

## CI/CD és konténerek

### Continuous Integration/Deployment

```yaml
# GitHub Actions példa
name: Build and Push
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Push to registry
        run: docker push myapp:${{ github.sha }}
      - name: Deploy
        run: kubectl apply -f deployment.yml
```

---

## Kubernetes és konténerek

### Mi az a Kubernetes (K8s)?
- Konténer orchestráció platform
- Automatikus skálázás
- Self-healing
- Load balancing

### Podman → Kubernetes
```bash
# Kubernetes YAML generálása
podman generate kube mycontainer > deployment.yml

# Telepítés Kubernetes-be
kubectl apply -f deployment.yml
```

---

## Konténerizáció előnyei

### ✅ Fejlesztőknek
- Gyors környezet felállítás
- "Works on my machine" probléma megoldása
- Egyszerű függőség kezelés

### ✅ Üzemeltetőknek
- Konzisztens telepítés
- Gyors skálázás
- Egyszerű visszaállítás
- Jobb erőforrás-kihasználás

### ✅ Vállalkozásoknak
- Gyorsabb piacra jutás
- Költségcsökkentés
- Modern DevOps gyakorlatok
- Cloud-native alkalmazások

---

## Gyakori hibák és megoldások

### Probléma: Port már használatban
```bash
# Hiba: Port 80 already in use
# Megoldás: Másik port használata
docker run -p 8080:80 nginx
```

### Probléma: Nincs hely a lemezen
```bash
# Nem használt konténerek törlése
docker container prune

# Nem használt képfájlok törlése
docker image prune -a

# Minden nem használt erőforrás törlése
docker system prune -a --volumes
```

---

## Hasznos erőforrások

### 📚 Dokumentáció
- Docker: https://docs.docker.com
- Podman: https://docs.podman.io
- Docker Hub: https://hub.docker.com

### 🎓 Tanulás
- Docker Labs: https://labs.play-with-docker.com
- Katacoda: Interaktív Docker oktatóanyagok
- YouTube: hivatalos Docker és Podman csatornák

### 🛠️ Eszközök
- Portainer: Vizuális konténer kezelés
- Docker Desktop: GUI macOS-hez és Windows-hoz
- Podman Desktop: Podman GUI

---

## Összefoglalás

### Kulcsfontosságú pontok
1. **Konténerek** = könnyűsúlyú, hordozható alkalmazáscsomag
2. **Docker** = legelterjedtebb konténer platform
3. **Podman** = biztonságosabb, daemon nélküli alternatíva
4. **Mindkettő** használható hasonló módon
5. Ideális **fejlesztéshez, teszteléshez, production**-höz

### Következő lépések
- Próbáld ki a Docker/Podman alapparancsokat
- Készíts saját Dockerfile-t
- Építs multi-container alkalmazást
- Fedezd fel a Kubernetes-t

---

## Kérdések?

### 🐳 Köszönöm a figyelmet!

**Gyakorlati gyakorlás:**
```bash
# Kezdd ezzel:
docker run hello-world
podman run hello-world
```

**További segítség:**
- Docker Discord: discord.gg/docker
- Podman GitHub: github.com/containers/podman
- Stack Overflow: #docker #podman
