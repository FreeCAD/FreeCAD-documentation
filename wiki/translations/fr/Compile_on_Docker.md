# Compile on Docker/fr
{{TOCright}}

## Présentation

Parmi les options de compilation et d\'installation de FreeCAD, il existe la possibilité d\'utiliser Docker. Cette méthode est principalement utile pour les développeurs FreeCAD, utilisant des ordinateurs Linux ou Mac OS.

### Avantages

Toutes les dépendances de FreeCAD sont déjà installées, compatibles les unes avec les autres et configurées de manière appropriée, ce qui vous permet de commencer à développer très rapidement.

-   Les dépendances sont contenues dans le conteneur de docker, empêchant tout paquet indésirable de contaminer votre poste de travail et empêchant toute version en conflit.
-   Le code source et les répertoires de construction sont en dehors du conteneur docker. Cela vous permet d\'utiliser vos éditeurs, systèmes de versionnage, outils de développement, etc. préférés, sans avoir à les configurer dans le conteneur Docker. Vous pouvez simplement les utiliser comme d\'habitude, directement depuis votre poste de travail. (En outre, cela signifie que vous n\'avez pas à reconstruire le conteneur Docker chaque fois que vous souhaitez créer FreeCAD.)
-   Pour ceux qui utilisent des distributions \*nix obscures, les [instructions ne sont pas disponibles](Compile_on_Linux/fr#Obtenir_les_d.C3.A9pendances.md) pour récupérer les dépendances, tout ce dont vous avez besoin pour installer sur votre poste de travail est docker, qui est généralement disponible dans de nombreuses distributions.
-   Fournit un environnement de développement statique et immuable. Personnellement, je trouve cela utile lors du développement pour réduire le nombre de variables potentielles qui pourraient causer un problème. Vous savez que vous n\'avez pas modifié quelque chose d\'ésotérique dans l\'environnement entre les versions. Pour les développeurs collaborant et utilisant tous les deux le même conteneur Docker, vous pouvez être sûr que vous travaillez tous les deux à partir du même environnement, ce qui réduit les erreurs de communication causées par les différences d\'environnement.

## Dépôt Docker 

-   Source: <https://gitlab.com/daviddaish/freecad_docker_env>
-   Officiel: <https://GitHub.com/FreeCAD/Docker>

## Prérequis

-   10 GB de mémoire libre
-   Docker

## Installation

### Charger les sources 

La meilleure façon d\'obtenir le code source de FreeCAD est de cloner le [dépôt Git](https://github.com/FreeCAD/FreeCAD). Pour cela, vous avez besoin du programme `git` qui peut être facilement installé dans la plupart des distributions Linux et Mac OS, et il peut également être obtenu sur le [site officiel](http://git-scm.com/).

Ceci créera une copie de la dernière version du code source de FreeCAD dans un nouveau répertoire nommé `freecad-source`.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git ~/my_code/freecad_source
}}

Pour plus d\'informations sur l\'utilisation de Git et sur la contribution de code au projet, voir [gestion du code source](Source_code_management/fr.md).

#### Source sous forme archive 

Vous pouvez alternativement télécharger la [source sous forme d\'archive](https://github.com/FreeCAD/FreeCAD/releases/latest), en fichier `.zip` ou `.tar.gz`, et décompresser cela dans le dossier voulu.

### Créer le répertoire de compilation 

Créez un répertoire pour contenir votre source FreeCAD compilée.


{{Code|lang=bash|code=
mkdir ~/my_code/freecad_build
}}

### Récupérer l\'image Docker 

Récupérez l\'image Docker. (Image officielle à venir.)


{{Code|lang=bash|code=
docker pull registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}

### Autoriser l\'accès à votre gestionnaire de fenêtres 

Pour que FreeCAD lance son interface graphique à partir du conteneur Docker, vous devez donner des autorisations d\'accès Docker à votre gestionnaire de fenêtres. Dans la plupart des distributions Linux, il s\'agit du système X window. Vous pouvez utiliser la commande ci-dessous pour autoriser l\'accès général à X, jusqu\'à ce que vous redémarriez ou déconnectiez votre ordinateur.


{{Code|lang=bash|code=
xhost +
}}

Si vous êtes connecté à des systèmes non approuvés, par exemple par `ssh`, cela vous rendra vulnérable au code malveillant. Fermez toutes les connexions `ssh` ou recherchez des autorisations xhost plus sécurisées, ce qui est hors de la portée de ce didacticiel.

#### Utilisateurs de Mac OS 

Pour ceux qui utilisent Mac OS, le système X Window peut ne pas être installé. Le projet XQuartz est un projet open source de longue durée qui vous permettra de l\'ajouter à votre ordinateur. [Vous pouvez le trouver ici](https://www.xquartz.org/).

### Lancer l\'image Docker 

Attribuez des variables d\'environnement afin que le conteneur Docker monte le code source de FreeCAD et crée le répertoire. De plus, vous pouvez monter un répertoire supplémentaire pour contenir tous les fichiers que vous souhaitez utiliser à des fins de test. Dans l\'extrait ci-dessous, nous l\'avons laissé comme répertoire personnel par défaut.


{{Code|lang=bash|code=
fc_source=~/my_code/freecad_source
fc_build=~/my_code/freecad_build
other_files=~/
}}

Lancez l\'image Docker.


{{Code|lang=bash|code=
docker run -it --rm \
-v $fc_source:/mnt/source \
-v $fc_build:/mnt/build \
-v $other_files:/mnt/files \
-e "DISPLAY" -e "QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}

### Compiler FreeCAD 

Vous pouvez compiler FreeCAD en utilisant le script de compilation installé ou en utilisant votre méthode préférée.


{{Code|lang=bash|code=
/root/build_script.sh
}}

### Lancer FreeCAD 

Une fois que FreeCAD a été compilé, il peut être exécuté normalement.


{{Code|lang=bash|code=
/mnt/build/bin/FreeCAD
}}

Vous pouvez trouver les répertoires joints dans le répertoire `/mnt`.

## Discussion

-   [Docker env build container](https://forum.freecadweb.org/viewtopic.php?f=4&t=42954)
-   [VSCode setup with Docker (1)](https://forum.freecadweb.org/viewtopic.php?f=10&t=48266)
-   [VSCode setup with Docker (2)](https://forum.freecadweb.org/viewtopic.php?p=427812#p427812)

## En relation 

-   [AppImage](AppImage/fr.md)







_ _

---
[documentation index](../README.md) > [Developer](Category_Developer.md) > Compile on Docker/fr
