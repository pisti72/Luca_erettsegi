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
