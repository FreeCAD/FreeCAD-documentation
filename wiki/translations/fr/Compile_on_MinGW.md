# Compile on MinGW/fr
{{TOCright}}

Ce guide explique les étapes nécessaires pour compiler FreeCAD sous Windows en utilisant l\'environnement MSYS2/MinGW. Une connaissance de base avec les commandes du shell Bash sera utile pour comprendre ce que fait chaque étape, mais en suivant le guide, vous devriez obtenir une compilation fonctionnelle même si vous ne comprenez pas exactement ce que vous avez fait pour l\'obtenir.

### Avant de commencer 

Téléchargez et installez [MSYS2](https://www.msys2.org) si ce n\'est pas déjà fait. Lorsque vous lancez MSYS2, utilisez le runtime \"MSYS2 MinGW 64-bit\" à moins que vous ne sachiez ce que vous faites et que vous ayez une raison spécifique de ne pas le faire. Si vous utilisez la console UCRT, veillez à adapter votre installation pour utiliser les paquets UCRT à la place.

    pacman -Syu

et ensuite relancer et exécuter

    pacman -Su

avant de poursuivre.

### Installer les outils de développement de base 

Dans toutes les étapes suivantes, lorsque l\'interpréteur de commandes de MSYS2 vous le demande, acceptez les installations par défaut de tous les éléments en appuyant sur \"Entrée\".

Premièrement, installez la chaîne d\'outils GCC mingw-w64 :

    pacman -S --needed base-devel mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja

Cette opération prendra probablement plusieurs minutes, car la chaîne d\'outils du compilateur est assez volumineuse.

Installez git :

    pacman -S git

Fermez votre fenêtre de console en cours et relancez la console MSYS2 MinGW 64 (dans une installation standard, elle se trouve dans votre menu Démarrer dans le dossier MSYS2).

### Vérifier les sources de FreeCAD 

Pour obtenir le code source de FreeCAD, clonez-le depuis le dépôt git principal :

    git clone https://github.com/FreeCAD/FreeCAD

Si vous ne voulez pas compiler le dernier HEAD, une fois que vous avez la source, vous pouvez vérifier une balise spécifique :

    cd FreeCAD
    git checkout tags/1.0 -b releases/FreeCAD-1-0

Ou une demande spécifique (dans cet exemple, PR 1234) :

    cd FreeCAD
    git fetch origin pull/1234/head:pr/1234
    git checkout pr/1234

Notez que toutes les versions ne peuvent pas être compilées sur MSYS2, plusieurs changements ont été nécessaires pour l\'activer et ceux-ci n\'étaient pas présents dans la 0.19 ou les versions antérieures. Par exemple, la balise 0.19.3 ne sera pas compilable.

### Installer les bibliothèques requises 

FreeCAD dépend de nombreuses bibliothèques tierces pour sa fonctionnalité. Elles peuvent être installées individuellement, ou sous la forme d\'une seule commande unifiée.

Maintenant, installez les dépendances requises suivantes en utilisant pacman :

-   mingw-w64-x86_64-opencascade
-   mingw-w64-x86_64-xerces-c
-   mingw-w64-x86_64-qt5
-   mingw-w64-x86_64-med
-   mingw-w64-x86_64-swig
-   mingw-w64-x86_64-qtwebkit
-   mingw-w64-x86_64-coin
-   mingw-w64-x86_64-python-pivy
-   mingw-w64-x86_64-python-ply
-   mingw-w64-x86_64-python-six
-   mingw-w64-x86_64-python-yaml
-   mingw-w64-x86_64-python-numpy
-   mingw-w64-x86_64-python-matplotlib
-   mingw-w64-x86_64-pyside2-qt5
-   mingw-w64-x86_64-python-markdown
-   mingw-w64-x86_64-python-pygit2

Ce qui suit est une commande unique pour installer tout ce qui est dans la liste ci-dessus :

    pacman -S mingw-w64-x86_64-opencascade mingw-w64-x86_64-xerces-c mingw-w64-x86_64-qt5 mingw-w64-x86_64-med mingw-w64-x86_64-swig mingw-w64-x86_64-qtwebkit mingw-w64-x86_64-coin mingw-w64-x86_64-python-pivy mingw-w64-x86_64-pyside2-qt5 mingw-w64-x86_64-python-ply mingw-w64-x86_64-python-six mingw-w64-x86_64-python-yaml mingw-w64-x86_64-python-numpy mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-markdown mingw-w64-x86_64-python-pygit2

### Compiler FreeCAD 

Créez un répertoire pour la compilation : notez que ce n\'est généralement pas un sous-répertoire du répertoire source (il est souvent utile de pouvoir supprimer soit le répertoire source soit le répertoire de compilation).

    mkdir FreeCAD-build
    cd FreeCAD-build

Exécutez cMake :

    cmake ../FreeCAD

Et enfin :

    cmake --build ./



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MinGW/fr
