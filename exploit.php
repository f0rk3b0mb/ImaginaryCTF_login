<?php
// Check if the required arguments are provided in the command line
if ($argc !== 2) {
    echo "Usage: php password_hash.php <password>\n";
    exit(1);
}

// Get the password from the command line argument
$password = $argv[1];

// Generate the password hash using password_hash()
$hash = password_hash($password, PASSWORD_DEFAULT);

// Output the generated hash
echo $hash;
