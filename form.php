<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment 4 Felipe Camargo</title>
</head>

<body>
    <h1 style="text-align: center;">Enter Values for a, b, and c</h1>
    <form action="process.php" method="POST" style="display: flex;
           flex-direction: column;
           gap: 12px;
           padding: 24px;
           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
           max-width: fit-content;
           margin: 50px auto;
           border-radius: 8px;">
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; gap: 8px;">
                <label for="x" style="font-weight: bold; font-size:28px ;">a:</label>
                <input type="number" name="x" id="x" required>
            </div>
            <div style="display: flex; gap: 8px;">
                <label for="y" style="font-weight: bold; font-size:28px ;">b:</label>
                <input type="number" name="y" id="y" required>
            </div>
            <div style="display: flex; gap: 8px;">
                <label for="z" style="font-weight: bold; font-size:28px ;">c:</label>
                <input type="number" name="z" id="z" required>
            </div>
        </div>
        <button type="submit"
            style="padding: 10px; border: none; background-color: #007BFF; color: white; border-radius: 4px; cursor: pointer;">Calculate</button>
    </form>
</body>

</html>