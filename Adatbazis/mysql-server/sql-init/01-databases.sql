-- Adatbázisok létrehozása
CREATE DATABASE IF NOT EXISTS konyvtar CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS filmek CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS webshop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Jogosultságok
GRANT ALL PRIVILEGES ON konyvtar.* TO 'tanulo'@'%';
GRANT ALL PRIVILEGES ON filmek.* TO 'tanulo'@'%';
GRANT ALL PRIVILEGES ON webshop.* TO 'tanulo'@'%';
FLUSH PRIVILEGES;
