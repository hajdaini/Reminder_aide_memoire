# Makefile

[Documentation](https://www.gnu.org/software/make/manual/make.html)

Syntax Makefile :

```Makefile
cible: prerequis1 prerequis2
    command1
    command2
```

Si cible est plus récent prérequis alors la tâche ne se lance pas 

## Commandes

> **Attention !** les commandes doivent être précédée d'une tabulation et non des espaces !

```Makefile
.PHONY: install update ## crée une "fausse" cible

.DEFAULT_GOAL= help ## cible lancer par défaut si on spécifie rien

PORT=8000

CURRENT_DIR=$(shell pwd) ## possibilité d'utiliser le shell dans une variable

composer.lock: composer.json
    composer update

vendor: composer.lock ## install les dépendances
    composer install

test: install ## Lance les tests unitaire
    php ./vendor/bin/phpunit --stop-on-failure

install: vendor

server: install ## Lance le serveur interne de PHP
    php -S localhost:$(PORT) -t public/ -d display_errors=1
```

Explication : 

- Si le fichier composer.json est plus récent que le fichier composer.lock on met à jour les dépendances via la commande composer update

- Si le fichier composer.lock est plus récent que le dossier vendor alors on installe les dépendances.

- Si on lance la commande `make install` sans avoir préinstallé les dépendances, make le détectera et commencera par exécuter les cibles nécessaires

- Surcharger la variable PORT

  ```sh
  make server PORT=9000
  ```

- Astuce : Possible d'afficher une sorte de documentation (à condition de mettre un double #) avec 

  ```Makefile
  # code ...
  
  help: 
    @grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-10s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

  #  code ...
  ```
  
  ```sh
  > make help ou make
  
  install          Installe les dépendances
  ...
  server           Lance le serveur interne de PHP
  ```

| types<br>d'affectation | Description|
|:------------------:|---|
| = | permet de lier la variable à une valeur (agit comme un pointeur) | 
| := | permet une affectation par valeur |
| ?= | permet de définir une valeur à une variable uniquement si elle n’est pas déjà défini |
| += | permet une affectation par concaténation. Elle suppose que la macro existe déjà |


Différence entre **:=** et **=**

```Makefile
VAL = foo
VARIABLE = $(VAL)
VAL = bar

test:
        @echo VAL : $(VAL) # résultat : bar
        @echo VARIABLE : $(VARIABLE) # résultat : bar

VAL = foo
VARIABLE := $(VAL)
VAL = bar

test2:
        @echo VAL : $(VAL) # résultat : bar
        @echo VARIABLE : $(VARIABLE) # résultat : foo
```


| variables<br>internes | Description|
|:------------------:|---|
| $@ | Le nom de la cible | 
| $< | Le nom de la première dépendance |
| $^ | La liste des dépendances |
| $? | La liste des dépendances plus récentes que la cible |
| $* | Le nom du fichier (la cible) sans extension |

| Condition          | Description         |
|--------------------|---------------------|
| ifeq (arg1,arg2)   | Egalité de arg1 et arg2 | 
| ifneq (arg1,arg2)	 | Inégalité de arg1 et arg2 |
| ifdef variable     | Existence de variable |
| ifndef variable	 | Inexistence de variable |

exemple : 

```Makefile
OS=Linux

ifeq ($(OS),Linux)
    echo "Linux"
else ifeq($(OS),Windows)
    echo "Windows"
else
    echo "autre"
endif
```

Il ya' possibilité d'inclure un fichier

- .env

  ```Makefile
  PORT=8000
  ```

- Makefile

  ```Makefile
  include .env

  test:
    @echo PORT : $(PORT)
  ```

Il est aussi possible de définir des motifs de règles grâce au symbole **%** :

```Makefile
images/optimized/%.jpg: images/raw/%.jpg
    mkdir -p images/optimized
    guetzli --quality 85 --verbose $< $@
```

```sh
> make images/optimized/test.jpg

guetzli --quality 85 --verbose images/raw/test.jpg images/optimized/test.jpg
```

En combinant l'utilisation de variables et de [fonctions](https://www.gnu.org/software/make/manual/make.html#toc-Functions-for-Transforming-Text) il est possible de créer des tâches plus complexes, exemple pour optimiser toutes les images JPG disponible dans un dossier :

```Makefile
RAW_IMAGES=$(subst images/raw/,images/optimized/,$(wildcard images/raw/*.jpg))

images/optimized/%.jpg: images/raw/%.jpg
    mkdir -p images/optimized
    guetzli --quality 85 --verbose $< $@

images: $(SRC)
```


Il est aussi possible, grâce au drapeau -j de paralléliser les tâches.

```sh
make -j4 images # lancer 4 jobs
```


## Bonus

Afficher des couleurs

```Makefile
PHP=php
PORT?=8000
HOST?=127.0.0.1

COM_COLOR   = \033[0;34m
OBJ_COLOR   = \033[0;36m
OK_COLOR    = \033[0;32m
ERROR_COLOR = \033[0;31m
WARN_COLOR  = \033[0;33m
NO_COLOR    = \033[m

server: install ## Lance le serveur interne de PHP
    echo -e "Lancement du serveur sur $(OK_COLOR)http://$(HOST):$(PORT)$(NO_COLOR)"
    ENV=dev $(PHP) -S $(HOST):$(PORT) -t public/ -d display_errors=1
```
