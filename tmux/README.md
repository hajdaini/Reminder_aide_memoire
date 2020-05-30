## Raccourcis de base

Préfix utilisé pour chaque commande 

| Touches  | Action  |
|----------|---------|
| `c` | Créer une nouvelle fenêtre |
| `&` | Supprimer la fenêtre courante |
| `n` | Aller vers la prochaine fenêtre |
| `p` | Aller vers la précédente fenêtre |
| `number` | Choisir une fenêtre spécifique |
| `,` | Renommer la fenêtre courante |
| `w` | Affiche la liste de toutes les fenêtres disponibles |
| `d` | Se détacher de la fenêtre (`tmux a` pour s'y rattacher) |


## Raccourcis dans un Split

| Touches  | Action  |
|----------|---------|
| `"` | Split horizontal du terminal courant |
| `%` | Split vertical du terminal courant |
| `x` | Killer le terminal courant |
| `o` | Switcher de terminal |
| `(flèches directionnelles)` | Se déplacer de terminal en terminal |
| `Alt` + (flèches directionnelles) | Réduire, agrandir le terminal courant |
| `{` | Déplacer le terminal courant vers la gauche |
| `}` | Déplacer le terminal courant vers la droite |
| `!` | Convertir le terminal courant en 1 seul terminal sur une nouvelle fenêtre |
| `z` | Activer/désactiver le zoom sur le terminal courant|

## Commandes tmux

`tmux kill-server` : tuer proprement toutes les sessions ouvertes (et le serveur).
`tmux kill-server -a` : tuer les autres sessions ouvertes et garder la session courante active

Fermer une session spécifique : 

- Utilisez `list-sessions` pour lister les différentes sessions afin d'identifier la session que vous souhaitez tuer
- Puis utilisez `tmux kill-session -t <targetSession>` pour tuer la session spécifique.
