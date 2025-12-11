# Adatbázis tananyagok és prezentációk

Ez a mappa tartalmazza az adatbázisokkal kapcsolatos prezentációkat, példákat és tananyagokat középiskolás diákok számára.

## 📚 Tartalom

- **adatbazis_ppt.md** - Átfogó prezentáció az adatbázisokról 10-11. osztályos diákoknak
  - Relációs adatbázisok alapjai
  - SQL alapműveletek (CRUD)
  - Táblák közötti kapcsolatok
  - Gyakorlati példák és alkalmazások

## 🔄 Markdown → PowerPoint konvertálás

### 1. Pandoc használata (ajánlott)

**Telepítés:**
```bash
# Fedora
sudo dnf install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# macOS (Homebrew)
brew install pandoc

# Windows (Chocolatey)
choco install pandoc
```

**Konvertálás:**
```bash
pandoc adatbazis_ppt.md -o adatbazis_ppt.pptx
```

**Sablon használatával:**
```bash
pandoc adatbazis_ppt.md -o adatbazis_ppt.pptx --reference-doc=template.pptx
```

### 2. Online eszközök

- **[CloudConvert](https://cloudconvert.com/md-to-pptx)** - Ingyenes online konverter
- **[AnyConv](https://anyconv.com/md-to-pptx-converter/)** - Egyszerű webes megoldás
- **[OnlineConvert](https://www.online-convert.com/)** - További formátumokkal

### 3. Marp használata

**Telepítés (VS Code extension):**
1. Telepítsd a "Marp for VS Code" kiterjesztést
2. Nyisd meg az .md fájlt
3. `Ctrl+Shift+P` → "Marp: Export Slide Deck"
4. Válaszd ki a PPTX formátumot

**CLI használat:**
```bash
npm install -g @marp-team/marp-cli
marp adatbazis_ppt.md --pptx -o adatbazis_ppt.pptx
```

### 4. Reveal.js + decktape (fejlett)

```bash
# Telepítés
npm install -g reveal-md decktape

# HTML generálás
reveal-md adatbazis_ppt.md --static _site

# PDF export (majd konvertálás PowerPointba)
decktape reveal adatbazis_ppt.md adatbazis_ppt.pdf
```

## 💡 Tippek a jobb eredményhez

1. **Diák elválasztás**: A `---` jelöli az új diát
2. **Címek**: Használj `##` szintű címeket a dia címekhez
3. **Képek**: Relatív elérési útvonalakkal hivatkozz rájuk
4. **Kódblokkok**: A \`\`\`sql\`\`\` blokkokat megtartja a formázást
5. **Táblázatok**: Markdown táblázatok automatikusan konvertálódnak

## 🛠️ Szerkesztés

A markdown fájlokat bármilyen szövegszerkesztővel módosíthatod:
- **VS Code** (ajánlott) - Markdown preview támogatással
- **Typora** - WYSIWYG markdown szerkesztő
- **Obsidian** - Jegyzetek és dokumentáció készítéséhez

## 👀 Markdown megjelenítés offline

### VS Code beépített preview (ajánlott)
1. Nyisd meg a `.md` fájlt VS Code-ban
2. Nyomd meg: `Ctrl+Shift+V` (vagy `Cmd+Shift+V` macOS-en)
3. Vagy kattints a jobb felső sarokban a 📖 ikonra ("Open Preview to the Side")

### Markdown → HTML konvertálás böngészőhöz
```bash
# Pandoc használatával
pandoc adatbazis_ppt.md -o adatbazis_ppt.html --standalone

# Nyisd meg böngészőben
firefox adatbazis_ppt.html
# vagy
google-chrome adatbazis_ppt.html
```

### Dedikált Markdown megjelenítők
- **Typora** - Élő előnézet szerkesztés közben (fizetős, de ingyenes próbaverzió)
  ```bash
  # Fedora (Flatpak)
  flatpak install flathub io.typora.Typora
  ```

- **Mark Text** - Nyílt forráskódú, ingyenes alternatíva
  ```bash
  # Fedora (Flatpak)
  flatpak install flathub com.github.marktext.marktext
  ```

- **Obsidian** - Jegyzetek kezeléséhez, kiváló preview
  ```bash
  # Fedora (Flatpak)
  flatpak install flathub md.obsidian.Obsidian
  ```

- **ReText** - Egyszerű, könnyű markdown szerkesztő
  ```bash
  sudo dnf install retext
  ```

### Böngésző kiegészítők
- **Markdown Viewer** (Chrome/Edge) - Közvetlenül nyisd meg a .md fájlokat
- **Markdown Preview Plus** (Firefox) - Automatikus renderelés

### Grip - GitHub-szerű megjelenítés
```bash
# Telepítés
pip install grip

# Futtatás (helyi szerver indul)
grip adatbazis_ppt.md

# Böngészőben megnyílik: http://localhost:6419
```

**Legjobb választás kezdőknek:** VS Code `Ctrl+Shift+V` - gyors, egyszerű, telepítés nélkül!

## 📖 További források

- [Pandoc dokumentáció](https://pandoc.org/MANUAL.html)
- [Marp hivatalos oldal](https://marp.app/)
- [Markdown szintaxis](https://www.markdownguide.org/)

---

**Utolsó frissítés:** 2025. december 6.