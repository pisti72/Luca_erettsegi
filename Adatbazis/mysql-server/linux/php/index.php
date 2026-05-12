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
    echo "Öcsém, sikerült kapcsolódni a MariaDB adatbázishoz! 🎉";
    echo "<p>MariaDB verzió: " . $pdo->query('SELECT VERSION()')->fetchColumn() . "</p>";
    
    // Adatbázisok listázása
    $stmt = $pdo->query('SHOW DATABASES');
    echo "<h2>Elérhető adatbázisok:</h2><ul>";
    while ($row = $stmt->fetch(PDO::FETCH_NUM)) {
        echo "<li>{$row[0]}</li>";
    }
    echo "</ul>";
    
    // Könyvtár példa
    $pdo->exec("USE konyvtar");
    $stmt = $pdo->query('SELECT * FROM konyvek LIMIT 5');
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
    echo "<p>Várj pár másodpercet, amíg a MariaDB elindul, majd frissítsd az oldalt!</p>";
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
        tr:nth-child(even) { background: #f2f2f2; }
        .links {
            margin: 30px 0;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
        <a href="http://localhost:8081" target="_blank">🌐 PHP Teszt Oldal (ez az oldal)</a>
    </div>
    
    <div class="links">
        <h2>🔐 Belépési adatok:</h2>
        <p><strong>phpMyAdmin:</strong></p>
        <ul>
            <li>Szerver: mariadb</li>
            <li>Felhasználónév: <code>root</code> VAGY <code>tanulo</code></li>
            <li>Jelszó: <code>rootpassword</code> VAGY <code>tanulo123</code></li>
        </ul>
        
        <p><strong>Adatbázisok:</strong></p>
        <ul>
            <li>📚 <strong>konyvtar</strong> - könyvek és kölcsönzések</li>
            <li>🎬 <strong>filmek</strong> - filmek és rendezők</li>
            <li>🏪 <strong>webshop</strong> - ügyfelek, termékek, rendelések</li>
        </ul>
    </div>
</body>
</html>
