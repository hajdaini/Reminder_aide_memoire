* 1. [Affichage](#Affichage)
* 2. [Variables](#Variables)
	* 2.1. [Les types](#Lestypes)
	* 2.2. [Déclarer une variable](#Dclarerunevariable)
	* 2.3. [constante](#constante)
* 3. [Condition](#Condition)
	* 3.1. [Condition ternaire](#Conditionternaire)
	* 3.2. [switch](#switch)
* 4. [Boucles](#Boucles)
* 5. [Fonction](#Fonction)
	* 5.1. [Retour type stricte](#Retourtypestricte)
	* 5.2. [Paramètres infinie](#Paramtresinfinie)
	* 5.3. [Fonction anonyme](#Fonctionanonyme)
	* 5.4. [Passage par référence](#Passageparrfrence)
* 6. [Tableau](#Tableau)
* 7. [Gestion des erreurs](#Gestiondeserreurs)
* 8. [Lire et écrire dans un fichier](#Lireetcriredansunfichier)
* 9. [Requette POST et GET](#RequettePOSTetGET)
* 10. [Includre des fichiers](#Includredesfichiers)

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

###  2.1. <a name='Lestypes'></a>Les types

Les types de variables les plus connues :

- int
- string
- bool
- double
- array
- NULL
- object
- iterable (variable utilisée dans le foreach)

###  2.2. <a name='Dclarerunevariable'></a>Déclarer une variable

nom de la variable = de préférence Camel case

```php
<?php
$name = "Hatim";
echo "Hello ", $name;

```

###  2.3. <a name='constante'></a>constante

```php
<?php

define("PI",    3.14); // méthode 1
echo PI, "<br>";
const WIDTH = 200; // méthode 2
echo WIDTH;
```

##  3. <a name='Condition'></a>Condition

- != différent de
- !== différent de valeur et de type

**mots-clés :** `if` `elseif` `else`

###  3.1. <a name='Conditionternaire'></a>Condition ternaire

```php
$retVal = (condition) ? a : b ;
```

###  3.2. <a name='switch'></a>switch 

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

- **continue** 
- **break**

```php
while (condition){
    // code...
}
```

```php
for ($i=0; $i < 10; $i++) { 
    // code...
}
```

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

###  5.3. <a name='Fonctionanonyme'></a>Fonction anonyme

```php
<?php

$test = function (){echo "test";};
$test();
```

###  5.4. <a name='Passageparrfrence'></a>Passage par référence

```php
<?php

function ref(&$var){ $var++; }
function noref($var){ $var++; }

$a = 5;

noref($a); echo $a, "<br>"; // 5
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

##  7. <a name='Gestiondeserreurs'></a>Gestion des erreurs

```php
<?php 
try {
    // code ...
} catch (Exception $e) {
    echo 'Exception reçue : ',  $e->getMessage(), "<br>";
}
```

##  8. <a name='Lireetcriredansunfichier'></a>Lire et écrire dans un fichier

Non disponible pour le moment

##  9. <a name='RequettePOSTetGET'></a>Requette POST et GET

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

echo $username;
echo $search;
```

##  10. <a name='Includredesfichiers'></a>Includre des fichiers

La fonction require () est identique à include (), sauf qu'elle traite les erreurs différemment. 

- include() : génère un avertissement lors d'une erreur et le script continue son exécution
- require() : génère une erreur fatale et le script s'arrête


require_once() est identique à require () sauf que PHP vérifie si le fichier a déjà été inclus et dans le cas échéant, elle ne l'inclut pas à nouveau.

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
<?php require("header.php") ?>
<h1>Mon article</h1>
<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit.</p>
<?php require("footer.php") ?>
```
