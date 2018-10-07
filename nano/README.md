## Centos

Lien de téléchargement de nano : https://www.nano-editor.org/download.php

``` 
wget http://lien/ nano-x.y.z.tar.gz 
tar -zxvf nano-x.y.z.tar.gz
yum install gcc
yum install ncurses-devel
cd nano-x.y.z/
./configure --prefix=/usr
make
make install
``` 

### Utilisation :

- Renommer le fichier de config **nanorc** en **.nanorc** et le mettre dans <i>~/</i> 
- Dezipper et deplacer les fichiers de coloration syntaxique de **nano.zip** dans <i>/urs/share/nano/</i> 

### Inspiration et Doc :

- Fichier de config : https://manpages.debian.org/unstable/nano/nanorc.5.en.html 
- Coloration syntaxique : https://github.com/scopatz/nanorc 
 
### Screenshot

<img src="looking.jpg">
