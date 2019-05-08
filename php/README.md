* 1. [Affichage](#Affichage)
* 2. [Variables](#Variables)
* 3. [Condition](#Condition)
* 4. [Boucles](#Boucles)
* 5. [Fonction](#Fonction)
	* 5.1. [Retour type stricte](#Retourtypestricte)
	* 5.2. [Paramètres infinie](#Paramtresinfinie)
	* 5.3. [Fonction utilis­ateur](#Fonctionutilisateur)
	* 5.4. [Fonction anonyme](#Fonctionanonyme)
	* 5.5. [Passage par référence](#Passageparrfrence)
* 6. [Tableau](#Tableau)
* 7. [Lire et écrire dans un fichier](#Lireetcriredansunfichier)
* 8. [Requête POST et GET](#RequtePOSTetGET)
* 9. [Inclure des fichiers](#Incluredesfichiers)
* 10. [Les Cookies](#LesCookies)
* 11. [Les sessions](#Lessessions)
* 12. [Les classes](#Lesclasses)
	* 12.1. [static](#static)
	* 12.2. [Héritage](#Hritage)
	* 12.3. [classe abstraite](#classeabstraite)
* 13. [Les interfaces](#Lesinterfaces)


# PHP Basic cheat

##  1. <a name='Affichage'></a>Affichage

```php
<?php
echo "hello " , "world<br>";
echo "hello " . "world 2<br>";
?>
<?= "hello " , "world 3" ?>
```

##  2. <a name='Variables'></a>Variables

|       Action           |     Code                     |
|------------------------|-------------------------------|
| Déclarer une variable  | `$nomVa­riable = 5;`|
| Afficher une variable  | `echo "var : " .$nomVa­riable;`|
| Déclarer une constante | <li>Méthode 1 : `define("PI", 3.14);`</li><li>Méthode 1 : `const WIDTH = 200;`</li>|
| Afficher une constante | `echo WIDTH;`|
| Caster une variable    | `$var = (string) $var;`|

##  3. <a name='Condition'></a>Condition

|       Action                    |     Code                          |
|---------------------------------|-----------------------------------|
| différent de                    | `!=`|
| différent de valeur et de type  | `!==`|
| mots-clés                       | `if` `elseif` `else` |
| condition ternaire              | `$retVal = (condition) ? a : b ;` |


**switch :**

```php
<?php

$menu = 1;

switch ($menu) {
    case 1:
        echo "Big mac !";
        break;
    default:
        echo "Rien";
        break;
}
```

##  4. <a name='Boucles'></a>Boucles

Possibilité d'utiliser les mots clés :

|       Action                    |     Code                          |
|---------------------------------|-----------------------------------|
| for                    | `for ($i=0; $i < 10; $i++) {/* code ... */}`|
| while  | `while (condition){ /* code ...*/ }`|
| mots-clés possible                   | `continue` `break` `else` |


##  5. <a name='Fonction'></a>Fonction

```php
<?php
function maFonction($test, int $age, bool $mort = true){
    // code...
    return [$test, $age, $mort];
}
```

###  5.1. <a name='Retourtypestricte'></a>Retour type stricte

```php
<?php
function maFonction($test){ : bool
    // code...
    return $test;
}
```

###  5.2. <a name='Paramtresinfinie'></a>Paramètres infinie

```php
<?php

function infinie(...$suite){
    var_dump($suite);
}

infinie(1, 2, 3);
infinie(1, 2, 3, 4);
```

###  5.3. <a name='Fonctionutilisateur'></a>Fonction utilis­ateur

```php
function multip­­li­er(­­$arg1, $arg2)
{
return $arg1 * $arg2;
}

$resultat = multip­­li­er(­­1, 2);
echo $resultat
```

###  5.4. <a name='Fonctionanonyme'></a>Fonction anonyme

```php
<?php

$test = function (){echo "test";};
$test();
```

###  5.5. <a name='Passageparrfrence'></a>Passage par référence

```php
<?php

function ref(&$var){ $var++; }
function noref($var){ $var++; }

$a = 5;

noref($a); echo $a. "<br>"; // 5
ref($a); echo $a; // 6
```

##  6. <a name='Tableau'></a>Tableau


```php
<?php

$tab = array(); // méthode 1
$tab2 = []; // méthode 2

// sans clé
$animaux = [ "chat", "chien", "ours"];
echo($animaux[0]. "<br>"); // chat

//avec clé
$notes= [ "Robert" => 12, "Alex" => 14];
echo($notes["Robert"]); // 12

$notes["Hatim"] = 20; //ajouter une valeur avec clé
array_push($animaux, "lion"); //ajouter une valeur sans clé


array_pop($animaux); // supprime le dernier élement
array_shift($animaux); // supprime le 1er element

unset($notes["Robert"]); // supprimer par clé

$pizza  = "piece1 piece2 piece3 piece4 piece5 piece6";
$pieces = explode(" ", $pizza); // string to array
```

##  7. <a name='Lireetcriredansunfichier'></a>Lire et écrire dans un fichier

Non disponible pour le moment

##  8. <a name='RequtePOSTetGET'></a>Requête POST et GET

index.php

```php
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Mon formulaire</title>
</head>
<body>
    <form action="validation.php" method="post">
        <label for="username">Nom</label>
        <input type="text" id="username" name="username">
        <input type="submit" value="Valider" name="valid_form">
    </form> 

    <br>
    
    <form action="validation.php" method="get">
        <label for="search">Rechercher</label>
        <input type="search" id="search" name="search">
        <input type="submit" value="Rechercher">
    </form>
</body>
</html>
```

validation.php

```php
<?php

function getCleanData(string $element, bool $post) : string{
    if($post){
        if(isset($_POST[$element]) && !empty($_POST[$element])){
            return htmlspecialchars($_POST[$element]);
        }
    }else{
        if(isset($_GET[$element]) && !empty($_GET[$element])){
            return htmlspecialchars($_GET[$element]);
        }    
    }
    return "";
}

$username = getCleanData("username", true);
$search = getCleanData("search", false);

echo $username; echo $search;
```

##  9. <a name='Incluredesfichiers'></a>Inclure des fichiers

La fonction **require()** est identique à **include()**, sauf qu'elle traite les erreurs différemment. 

- **include()** : génère un avertissement lors d'une erreur et le script continue son exécution
- **require()** : génère une erreur fatale et le script s'arrête


**require_once()** est identique à **require ()** sauf que PHP vérifie si le fichier a déjà été inclus et dans le cas échéant, elle ne l'inclut pas à nouveau (**include_once()** existe aussi).

header.php

```php
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Mon formulaire</title>
</head>
<body>
```

footer.php

```php
<hr>
<footer>
    <p>&copy; Copyright monsite.com tout droit reservé</p>
</footer>

</body>
</html>
```

index.php

```php
<?php require("header.php"); ?>
<h1>Mon article</h1>
<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit.</p>
<?php require("footer.php"); ?>
```

##  10. <a name='LesCookies'></a>Les Cookies

Un cookie n'est pas fait pour stocker des données sensibles style mdp, il peut être utilisé pour stocker par exemple les préférences utilisateurs

```php
<?php 
if(!isset($_COOKIE["lang"]) && empty($_COOKIE["lang"])){
    setcookie( // TOUJOURS CETTE INSTRUCTION AU DEBUT (avant tout code html) !
        "lang", // nom du cookie
        "fr", // valeur par défaut
        time() + 3600 * 24 * 365, // expiration du cookie (ici 1 année)
        null,
        "localhost", // mettre son nom de domaine
        false, // envoyer le cookie que depuis un HTTPS (le faire si votre site est en https) 
        true // l'accès au cookie ne se fera que par HTML et non Javascript
    );

    $_COOKIE["lang"] = "fr"; // prendre immediattement les changements
}
?>

<?php require("header.php"); ?>
<p><?= htmlspecialchars($_COOKIE["lang"]) ?></p>
<?php require("footer.php"); ?>
```

**Détruitre un cookie**

Pour détruire un cookie il faut le unset et lui attribuer ensuite une expiration négatif 

```php
<?php
unset($_COOKIE["lang"]);
setcookie("lang", "", time() - 10);
```

##  11. <a name='Lessessions'></a>Les sessions

profile.php

```php
<?php 
    session_start(); // TOUJOURS CETTE INSTRUCTION AU DEBUT (avant tout code html) ! 
    $_SESSION["username"] = "Hatim"; // création d'une session username
?>

<?php require("header.php"); ?>
<p><?php echo "Bonjour " .htmlspecialchars($_SESSION["username"]) ?></p>
<input type="button" onclick="window.location='deconnexion.php'"  value="Deconnexion"/>
<?php require("footer.php"); ?>
```

deconnexion.php

```php
<?php
session_destroy(); // destruction de la session
header("Location: index.php");
```

index.php

```php
<?php require("header.php"); ?>
<h1>Page d accueil</h1>
<?php require("footer.php"); ?>
```

##  12. <a name='Lesclasses'></a>Les classes

```php
<?php 

class Utilisateur {

    private $username = 0;

    // constructeur
    public function __construct(int $username)
    {
        $this->username = $username;
    }

    // getter
    public function getUsername()
    {
        return $this->username;
    }

    // setter
    public function setUsername($username)
    {
        $this->username = $username;
    }
}

$user = new Utilisateur(10);
$user->setUsername("Hatim");
echo $user->getUsername();
```

###  12.1. <a name='static'></a>static

```php
<?php 

class Database {

    public static $databaseName = "madatabase";

    public static function connect(){
        echo "Je suis connectés à la db<br>";
    }
}

Database::connect();
echo "Nom database : " .Database::$databaseName;
```

###  12.2. <a name='Hritage'></a>Héritage

```php
<?php 

class Personnage {

    private $vie, $name;

    public function __construct($vie, $name)
    {
        $this->vie = $vie;
        $this->name = $name;
    }

    public function presentation(){
        echo "vie : " .$this->vie. " | name : " .$this->name;
    }
}

class Mage extends Personnage{

    private $soin = 0; // imaginons que seul le mage a le droit de soin

    public function __construct($vie, $name, $soin)
    {
        parent::__construct($vie, $name); // équivalant au super sur Java
        $this->soin = $soin;
    }

    public function presentation(){
        parent::presentation();
        echo " | soin : " .$this->soin;
    }
}

$mage = new Mage(10, "zozo", 30);
$mage->presentation();
```

###  12.3. <a name='classeabstraite'></a>classe abstraite 

Une classe abstraite est avant tout une classe. Rien ne l’oblige à posséder des méthodes abstraites ! Les méthodes abstraites 
sont des signatures de méthodes qui permettent de définir la structure d'une classe fille.

- Seules les fonctions membres de votre classe abstraite peuvent être abstraites, jamais les propriétés
- Une classe abstraite ne s’instancie pas

```php
<?php 

abstract class Mere {
    abstract protected function presentation();
    abstract protected function parler($message);
}

class Fille extends Mere{

    public function presentation(){
        echo "Hello je m'appelle Barbara<br>";
    }

    public function parler($message){
        echo "Barbara : " .$message;
    }
}

$fille = new Fille();
$fille->presentation();
$fille->parler("salut !");
```

##  13. <a name='Lesinterfaces'></a>Les interfaces

Contrairement aux classes abstraites les interfaces autorisent l'héritage multiple.

```php
<?php 

interface Mere {
    const MAJEUR = 12; // possibilité d'implémenter des constantes
    public function presentation();
    public function parler($message);
}

interface Education {
    public function nePasInsulter();
    public function nePasFrapper();
}

class Fille implements Mere, Education{

    public function presentation(){
        echo "Hello je m’appelle Barbara<br>";
    }

    public function parler($message){
        echo "Barbara : " .$message. "<br>";
    }

    public function nePasFrapper()
    {
        echo "Je ne frappe pas les autres.<br>";
    }
    
    public function nePasInsulter()
    {
        echo "Je n'insulte pas les autres.";
    }
}

$fille = new Fille();
$fille->presentation();
$fille->parler("salut !");
$fille->nePasFrapper();
$fille->nePasInsulter();
echo Fille::MAJEUR; // Appel de la constante
```

# Les exceptions


```php
<?php 

class DivisionZero extends Exception{
    
}

$divider = 5;

function checkDivider(int $divider){
    if($divider == 0){
        throw new DivisionZero("Impossible de diviser par 0", 1);
        
    }elseif ($divider < 0) {
        throw new DivisionZero("Impossible de diviser par un nombre négative");
    }
}

try {
    checkDivider($divider);
    echo "10/" .$divider. " = " .(10/$divider);
} catch (DivisionZero $e) {
    echo $e->getMessage();
}
```
