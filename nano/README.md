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

- Mon fichier config dans <i>~/.nanorc</i> est **nanorc**
- Mes fichiers de couleurs des fichiers dans <i>/usr/share/nano/</i> est **nano.zip**

Inspiration des mes fichiers de configs et couleurs :
- Fichier de config : https://manpages.debian.org/unstable/nano/nanorc.5.en.html 
- Couleurs des fichiers : https://github.com/scopatz/nanorc 
 
