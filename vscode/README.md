File > Preferences > Keyboard Shortcuts


## MOVEMENTS

| Shortcuts   | Command |
|:--------:|---------------|
| `ctrl+ù` |  Toggle terminal |
| `ctrl+*` | Switch focus between Terminal and Editor |
| `ctrl+%` | Split Terminal/Editor (depend on the focus) |
| `ctrl+x` | Kill active terminal |
| `alt+[arrow keys]` | Switch terminal/Edtior Splot (depend on the focus) |


## SELECTIONS

**You must install the `Quick and Simple Text Selection` extension to use those shortcuts**

| Shortcuts   | Command |
|:--------:|---------------|
| `ctrl+shift+a` |  Select between html tag (if used again, then it will select the parent element) |
| `ctrl+shift+7` |  Select between ` ` |
| `ctrl+shift+3` |  Select between "" |
| `ctrl+shift+4` |  Select between '' |
| `ctrl+shift+=` |  Select between {} |
| `ctrl+shift+)` |  Select between [] |
| `ctrl+shift+0` |  Select between () |

## REGEX

- Rappel : https://github.com/hajdaini/Reminder_aide_memoire/blob/master/regex/README.md

Exemple pour supprimer tous les attributs des titres de type &lt;h2> :

- **Search** : <span>&lt;h2.&#42;&gt;[\n\s]&#42;(.+)[\n\s]*&lt;/h2&gt;</span><br>
- **Replace** : <span>&lt;h2&gt;$1&lt;/h2&gt;</span><br>

