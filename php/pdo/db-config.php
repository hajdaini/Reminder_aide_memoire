<?php
const DB_DSN = 'mysql:host=localhost;dbname=<DATABASE_NAME>';
const DB_USER = "<USERNAME>";
const DB_PASS = "<PASSWORD>";


$options = array(
    PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8", // encodage utf-8
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // gérer les erreurs en tant qu'exception
    PDO::ATTR_EMULATE_PREPARES => false // faire des vrais requêtes préparées et non une émulation
);