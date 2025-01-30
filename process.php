<?php
    $a = escapeshellarg($_POST["a"]);
    $b = escapeshellarg($_POST["b"]);
    $c = escapeshellarg($_POST["c"]);
    
    $command = "pbthon3 process_input.py $a $b $c";
    $output = shell_exec($command);
    
    echo "<div>$output</div>";
?>