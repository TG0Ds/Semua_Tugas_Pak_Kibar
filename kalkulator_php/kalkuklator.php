<?php

class Calculator {
    public function add($a, $b) {
        return $a + $b;
    }

    public function subtract($a, $b) {
        return $a - $b;
    }

    public function multiply($a, $b) {
        return $a * $b;
    }

    public function divide($a, $b) {
        if($b == 0) {
            return "Error: Tidak bisa mebagi dengan nol.";
        }

        return $a / $b;
    }
}

    $calculator = new Calculator();

    $result = null;
    
    if(isset($_POST['operation']) && isset($_POST['a']) && isset($_POST['b'])) {
        $operation = $_POST['operation'];
        $result = $calculator->$operation($_POST['a'], $_POST['b']);
    }

?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator</title>
</head>
<body>
    <h1>Kalkulator</h1>
    <?php if($result !== null): ?>
        <p>Hasil: <?php echo $result; ?></p>
    <?php endif; ?>
    <form action="index.php" method="post">
        <div>
            <input type="number" name="a" placeholder="Angka 1" value="<?php echo isset($_POST['a']) ? $_POST['a'] : ''; ?>"> 
        </div>
        <div>
            <input type="number" name="b" placeholder="Angka 2" value="<?php echo isset($_POST['b']) ? $_POST['b'] : ''; ?>">
        </div>
        <br>

        <button type="submit" name="operation" value="add">Tambah</button>
        <button type="submit" name="operation" value="subtract">Kurang</button>
        <button type="submit" name="operation" value="multiply">Kali</button>
        <button type="submit" name="operation" value="divide">Bagi</button>
    </form>
   
</body>
</html>