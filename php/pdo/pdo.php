<?php 

require 'db-config.php';

function cleanPrint($element){
    echo "<pre>";
    print_r($element);
    echo "</pre>";
}

function select(PDO $PDO){
    $sql = "SELECT * FROM users";
    $result = $PDO->query($sql);

    /**
     * FETCH :
     *      BOTH (par défaut) : retourne tableau avec index et clé (trop lourd)
     *      ASSOC : retourne tableau avec clé
     *      OBJ : retourne un object
     */
    $users = $result->fetchAll(PDO::FETCH_ASSOC);

    $result->closeCursor(); // Ferme le curseur, permettant à la requête d'être de nouveau exécutée

    foreach ($users as $user) {
       cleanPrint($user["username"]);
    }
}

// Protection INJECTION SQL 
function prepareRequest(PDO $PDO, string $username, bool $useParaMethod){
    if($useParaMethod){
        $request = $PDO->prepare("SELECT * FROM users WHERE username = :username"); // Préparation de la requête
        $request->bindValue(":username", $username); // selon une clé && valeur
    }else{
        $request = $PDO->prepare("SELECT * FROM users WHERE username = ?");
        $request->bindValue(1, $username); // selon l'index
    }
   
    $request->execute(); // exécution de la requête
    $result = $request->fetch(PDO::FETCH_ASSOC); // On récupère le 1er résultat
    cleanPrint($result);
}

function update(PDO $PDO){
    $username =  "hatim";
    $request = $PDO->prepare("UPDATE users SET is_admin = :is_admin WHERE username = :username"); 
    $request->bindValue(":username", $username);

     /**
     * Conversion en type SQL
     * 
     * Les types : PDO::PARAM_BOOL | PDO::PARAM_STR | PDO::PARAM_INT | PDO::PARAM_NULL
     */ 
    $request->bindValue(":is_admin", 1, PDO::PARAM_INT); 
    
    $request->execute();
    prepareRequest($PDO, $username, true);
}


try {
   $PDO = new PDO(DB_DSN, DB_USER, DB_PASS, $options);
   echo "Connexion établie";
   prepareRequest($PDO, "admin", false);
   prepareRequest($PDO, "hatim", true);
   update($PDO);
} catch (PDOException $pe) {
    echo 'ERREUR :', $pe->getMessage();
}