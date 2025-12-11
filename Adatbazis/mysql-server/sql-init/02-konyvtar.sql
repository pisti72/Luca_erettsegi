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
