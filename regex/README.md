# REGEX

## Début, Fin et choix

| Regex      | Traduction    |
|:----------:|---------------|
| `^Bonjour` | Texte commençant par "Bonjour" |
| `revoir$`  | Texte finissant par revoir |
| <code>Bonjour&#124;revoir</code> | toutes les occurrences de "Bonjour" ou "revoir" |
| <code>^Bonjour&#124;revoir$</code> | "Bonjour" au début ou "revoir" en fin de texte |

## Les ensembles de caractères

| Regex      | Traduction    |
|:----------:|---------------|
| `[A-Z]`    | Lettres majuscules de A à Z |
| `[a-z]`    | Lettres minuscules de a à z |
| `[0-9]` ou `\d`    | Chiffres de 0 à 9 |
| `[a-z0-9]` | Lettres minuscules de a à z ou chiffres de 0 à 9 |
| `.`        |	Absolument n'importe quel charactère |
| `\w`       |	[a-zA-Z0-9_] |
| `\n`       |	Un retour à la ligne |
| `\t`       |	Une tabulation |
| `\s`       |	Espace |


## Les ensembles de caractères

| Regex  | Traduction    |
|:------:|---------------|
| `*`    | 0 ou plusieurs répétitions |
| `+`    | +	1 ou plusieurs répétitions |
| `?`    | 0 ou 1 répétition |
| `[a-zA-Z]{6}`| 6 lettres consécutives |
| `[0-9]{2,4}` | 2 et 4 chiffres consécutifs |

Bonus

Les parenthèses permettent de créer un groupe de regex et de les stocker en mémoire afin de les réutiliser avec les références `$1`, `$2` etc ...
