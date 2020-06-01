## Navigation

| Touches  | Action  |
|----------|---------|
|`left` ou `h`| Gauche|
|`$` | fin de la ligne|
|`0`|  début de la ligne|
|`^^`| début de la phrase |
|`gg`|	Aller la la première ligne du document|
|`G`| Aller la la dernière ligne du document|
|`w`| Aller au mot suivant|
|`W`| Aller au mot sans espace suivant|
|`b`| Aller au mot précédent|
|`B`| Aller au mot sans espace précédent|
|`e`| Aller à la fin du mot|
|`E`| Aller à la fin du MOT (un mot ici est un ensemble de caractère sans espace)|
|`pagedown`| Scroll down par page|
|`pageup` | Scroll up par page|
|`Ctrl+u` |Scroll up à moitié de page|
|`Ctrl+d` |Scroll down à moitié de page|

## Les modes

| Touches  | Action  |
|----------|---------|
| `A` | Basculer en mode Insertion en fin de ligne|
| `i` | Basculer en mode Insertion|
| `I` | Basculer en mode Insertion en début de ligne|
| `v` | Basculer en mode visuel (sélection)|
| `V` | Basculer en mode visuel (sélection par ligne)|
| `:` | Basculer en mode commande |
| `/` |	Rechercher |


## Mode normal

> **Astuces** : remplacer le `d` par `c` pour effectuer la même action et se retrouver directement en mode insertion

| Touches  | Action  |
|----------|---------|
| `dd` | Supprime la ligne entière |
| `D` |	Supprime du curseur jusqu’à la fin de la ligne |
| `d/[pattern]` |	Supprime du curseur  jusqu’au pattern |
| `di [char]` | Supprime les mots entre le [char] |
| `dit` | Supprime les mots entre le un tag html |
| `dt [char]` | Supprime les mots qui se trouve après le curseur jusqu'à rencontrer [char] |
| `dT [char]` | Supprime les mots qui se trouve avant le curseur jusqu'à rencontrer [char] |
| `df [char]` | même chose que `dt` avec [char] inclus |
| `dF [char]` | même chose que `dT` avec [char] inclus |
| `x` |	Couper (supprimer) le caractère qui se trouve sous le curseur |
| `X` |	Couper (supprimer) le caractère qui se trouve avant le curseur |
| `y` |	Copie le caractère sous le curseur |
| `yy` | Copier la ligne de texte qui se trouve sous le curseur|
| `Y` |	Copier jusqu’en fin de ligne |
| `p` |	Coller |
| `P` |	Coller avant le curseur / la ligne |
| `s` |	Substitue le caractère et bascule en mode insertion |
| `S` |	Substitue la ligne et bascule en mode insertion |
| `r` |	Substitue le caractère et sans basculer en mode insertion |
| `o` |	Ajouter une nouvelle ligne après la position du curseur et se placer en mode insertion au début de cette nouvelle ligne |
| `O` |	Ajouter une nouvelle ligne avant la position du curseur et se placer en mode insertion au début de cette nouvelle ligne |
| `J` |	Joint la ligne suivante à la fin de la ligne courante |
| `u` |	Annuler |
| `Ctrl+r ou U` | Refaire (annuler l’annulation) |
| `Ctrl+g` | Afficher des informations sur son positionnement |
| `>>` |	Indenter la ligne| 
| `> [up ou down]` | Indenter la ligne du dessus/dessous |
| `<<` |	Désindenter la ligne| 
| `< [up ou down]` | Désindenter la ligne du dessus/dessous |
| `.` |	Répéter le dernier changement| 
| `gg + =G` | Indenter tout le fichier |
| `==` | Aligne la ligne courante par rapport à la précédente|  

## Macros

1. Création de la macro sur l'enregistrement 1 `q1`
2. Lancer les commandes à enregistrer
3. Quitter l'enregistrement 1 `q`
4. Utiliser la macro de l'enregistrement 1 `@1`

> **Astuces** : allé à la ligne suivante lors de la fin de votre enregistrement pour pouvoir utiliser votre macro sur les prochaines lignes ex `20@1`

## Mode insertion


| Touches  | Action  |
|----------|---------|
| `Ctrl+d` | Désindenter |
| `Ctrl+w` |Supprimer le mot avant le curseur|

## Bonus

| Touches  | Action  |
|----------|---------|
| `Ctrl+a` | incrémenter un nombre |
| `Ctrl+x` | décrémenter un nombre |

Executer un script python ouvert avec vim :

```
:w
:! clear python3 file.py
```

ou

```
:w | ! clear; python3 test.py
```


Pour répéter la commande précente : `:!!`

Rechercher et remplacer un mot 

```shell
:%s/mot1/mot2/g
```
