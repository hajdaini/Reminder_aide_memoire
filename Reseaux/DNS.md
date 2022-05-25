# Différents types d’enregistrements DNS

- **A :** « A » signifie adresse, c’est le type de syntaxe DNS le plus simple. Il indique à un domaine une adresse IP (ipv4)
  <br>*Exemple:    www.domaine.net.   IN   A   212.27.35.185*

- **AAAA :** Permet de faire la correspondance entre un nom DNS et une adresse IP (ipv6)
  <br>*Exemple:    irc.domaine.com.    IN     AAAA     2a01:ecb:1:f:2e0:b7ff:fea9:4da8*

- **CNAME :** L’enregistrement « CNAME » signifie nom canonique, et son rôle est de rendre un domaine alias d’un autre domaine.CNAME est souvent utilisé pour associer les nouveaux sous-domaines avec l’enregistrement A d’un domaine existant. (ne fournit PAS d'adresse IP)
  <br>*Exemple:    sql.domaine.ext.     IN     CNAME     mysql1.autredomaine.ext.*

- **MX :** L'enregistrement « MX » ou Mail Exchange est principalement une liste de serveurs de messagerie qui doit être utilisée pour le domaine.
  <br>*Exemple:    domaine.net.    IN    MX  10   domaine.net.*
  <br>*Le nom DNS doit être du type A et vous ne pouvez pas utiliser une IP ou un CNAME.*
  <br>*La priorité est l’ordre dans lequel les serveurs de mail seront contactés si il y en a plusieurs.*

- **TXT :** « TXT » pour Texte. Cette syntaxe DNS permet aux administrateurs d’insérer à l’enregistrement DNS n’importe quel texte de leur choix.Il est souvent utilisé pour indiquer des faits ou des informations concernant le domaine (1024 caractères au maximum).

- **URL Redirect :** Cet enregistrement permet la redirection de votre domaine, ou d’un sous domaine vers une autre adresse web.

- **URL Frame :** Cet enregistrement tout comme l’URL Redirect effectue la redirection vers le site web indiqué mais affiche dans la barre d’URL le nom de domaine redirigé``
