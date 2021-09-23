# Git buildpackage/fr


Les workflows de travail de développement Debian modernes impliquent un [packaging avec Git](https://wiki.debian.org/PackagingWithGit) et l\'outil principal pour le faire est [gbp.html git-buildpackage](http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/). git-buildpackage fournit une commande gbp avec plusieurs options similaires à la commande git elle-même. Beaucoup de ces commandes ne sont elles-mêmes qu\'encapsuleur d\'outils Debian de niveau inférieur. Par conséquent la complexité de l\'apprentissage de l\'empaquetage peut être assez élevée.

Pour contourner cela, voici les étapes courtes et simples pour commencer avec git-buildpackage. Cela devrait fonctionner sur presque toutes les distributions basées sur Debian, mais je recommande de travailler dessus dans un environnement propre et séparé, une machine virtuelle [Debian Unstable](Debian_Unstable/fr.md).

1.  Installez-le avec sudo apt install git-buildpackage
2.  Saisissez les fichiers dot à la fin de cette page. Vous aurez besoin de: ~/.gbp.conf, ~/.pbuilderrc et ~/.quiltrc
3.  La construction du package se fera dans un environnement propre. Créez-le avec sudo git-pbuilder create
4.  Trouvez l\'URL d\'un paquet que vous voulez construire sur <https://salsa.debian.org>, l\'instance GitLab auto-hébergée du projet Debian
5.  Créez-en un clone avec 
6.  Entrez dans le répertoire du dépôt cloné avec cd
7.  Exécutez la construction avec gbp buildpackage -us -uc
8.  Une fois terminé, vos packages seront dans ../build-area/.

##### gbp.conf

Location: ~/.gbp.conf

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.gbp.conf>

##### pbuilderrc

Location: ~/.pbuilderrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.pbuilderrc>

##### quiltrc

Location: ~/.quiltrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.quiltrc>


 

[Category:Packaging](Category:Packaging.md) [Category:Developer Documentation](Category:Developer_Documentation.md)
