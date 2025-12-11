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
