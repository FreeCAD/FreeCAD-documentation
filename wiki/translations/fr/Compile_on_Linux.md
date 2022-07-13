# Compile on Linux/fr
**Il existe un conteneur Docker FreeCAD expérimental qui est testé pour le développement FreeCAD. En savoir plus à ce sujet sur [Compiler sur Docker](Compile_on_Docker/fr.md)**


{{TOCright}}

## Présentation

Sous les distributions GNU/Linux récentes, FreeCAD est généralement facile à compiler, puisque toutes les dépendances sont fournies par le gestionnaire de paquets. Cela se fait en 3 étapes    *

1.  Obtenir le code source de FreeCAD
2.  Obtenir les dépendances ou les paquets dont FreeCAD dépend
3.  Configurer avec `cmake` et compiler avec `make`

Vous trouverez ci-dessous des instructions détaillées du processus complet, quelques [scripts de compilation](#Scripts_de_compilation_automatiques.md) et des particularités que vous pourriez rencontrer. Si vous constatez des informations erronées ou désuètes (les distributions Linux changent régulièrement), ou si vous utilisez une distribution qui n\'est pas listée, pour les discussion voir sur le [forum](https   *//forum.freecadweb.org/index.php), votre aide pour corriger le tout sera appréciée.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width   *800px;">



*Processus général pour compiler FreeCAD à partir des sources. Les dépendances tierces doivent être dans le système, ainsi que le code source de FreeCAD lui-même. CMake configure le système de manière à ce que le projet entier soit compilé avec une seule instruction make.*

## Obtenir le code source 

### Git

Le meilleur moyen d'obtenir le code est de cloner le [dépôt Git](https   *//github.com/FreeCAD/FreeCAD) en lecture seule. Pour cela, vous avez besoin du programme `git` qui peut être installé dans la plupart des distributions Linux. Il peut également être obtenu sur le [site officiel](http   *//git-scm.com/).

Git peut être installé via la commande suivante    *


{{Code|lang=bash|code=
sudo apt install git
}}

La commande suivante placera une copie de la dernière version du code source de FreeCAD dans un nouveau répertoire appelé `freecad-source`.


{{Code|lang=bash|code=
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
}}

Pour plus d\'informations sur l\'utilisation de Git et sur la contribution de code au projet, voir [gestion du code source](Source_code_management/fr.md).

### Source sous forme archive 

Vous pouvez aussi télécharger la [source sous forme d\'archive](https   *//github.com/FreeCAD/FreeCAD/releases/latest), fichier `.zip` ou `.tar.gz` et décompresser cela dans le dossier voulu.

## Obtenir les dépendances 

Pour compiler FreeCAD, vous devez installer les dépendances requises mentionnées dans les [Bibliothèques externes](Third_Party_Libraries/fr.md) ; les packages contenant ces dépendances sont répertoriés ci-dessous pour différentes distributions Linux. Veuillez noter que les noms et la disponibilité des bibliothèques dépendront de votre distribution particulière. Si votre distribution est ancienne, certains paquets peuvent ne pas être disponibles ou avoir un nom différent. Dans ce cas, consultez la section [Anciennes distributions et distributions non-conventionnelles](#Distributions_anciennes_et_non-conventionnelles.md) ci-dessous.

Une fois que vous avez toutes les dépendances installées procédez à la [Compilation de FreeCAD](#Compiler_FreeCAD.md).

Veuillez noter que le code source de FreeCAD est d'environ 500 Mo ; il peut être trois fois plus gros si vous clonez le référentiel Git avec son historique de modifications complet. Obtenir toutes les dépendances peut nécessiter le téléchargement de 500 Mo ou plus de nouveaux fichiers ; Lorsque ces fichiers sont décompressés, ils peuvent nécessiter 1500 Mo ou plus d'espace. Notez également que le processus de compilation peut générer jusqu\'à 1500 Mo de fichiers supplémentaires lorsque le système copie et modifie le code source complet. Par conséquent, assurez-vous de disposer de suffisamment d'espace libre sur votre disque dur, au moins 4 Go, lors de la tentative de compilation.


<div class="mw-collapsible mw-collapsed toccolours">

### Debian et Ubuntu 


<div class="mw-collapsible-content">

Sous les systèmes basés sur Debian (Debian, Ubuntu, LinuxMint, etc\...) , il est très facile d\'installer toutes les dépendances requises. La plupart des bibliothèques sont disponibles via `apt`, le gestionnaire de paquets Synaptic, ou le gestionnaire de paquets de votre choix.

Si vous avez déjà installé FreeCAD depuis les dépôts officiels, vous pouvez installer ses dépendances de compilation à l\'aide de cette unique ligne de commande dans un terminal    *


```python
sudo apt build-dep freecad
```

Cependant, si la version de FreeCAD dans les référentiels est ancienne, les dépendances peuvent être mauvaises pour compiler une version récente de FreeCAD. Par conséquent, vérifiez que vous avez installé les packages suivants.

Ces packages sont essentiels à la réussite de toute compilation    *

-    `build-essential`, installe les compilateurs C et C++ et les librairies C.

-    `cmake`, un outil indispensable pour configurer la source de FreeCAD. Vous pouvez également souhaiter installer `cmake-gui` et `cmake-curses-gui` pour une option graphique.

-    `libtool`, des outils essentiels pour produire des librairies partagées.

-    `lsb-release`, l\'utilitaire reporting de base standard est normalement déjà installé sur un système Debian et vous permet de distinguer, par programme, entre une installation Debian pure et une variante, telle que Ubuntu ou Linux Mint. Ne supprimez pas ce paquet, car de nombreux autres paquets système peuvent en dépendre.

La compilation de FreeCAD utilise le langage Python, et est également utilisé au moment de l\'exécution en tant que script. Si vous utilisez une distribution basée sur Debian, l\'interpréteur Python est normalement déjà installé.

-    `python3`
    

-    `swig`, l\'outil qui crée des interfaces entre le code C++ et Python.

Veuillez vérifier que vous avez installé Python 3. Python 2 étant obsolète en 2019, les nouveaux développements dans FreeCAD ne sont pas testés avec cette version du langage.

Les librairies Boost doivent être installées    *

-    `libboost-dev`
    

-    `libboost-date-time-dev`
    

-    `libboost-filesystem-dev`
    

-    `libboost-graph-dev`
    

-    `libboost-iostreams-dev`
    

-    `libboost-program-options-dev`
    

-    `libboost-python-dev`
    

-    `libboost-regex-dev`
    

-    `libboost-serialization-dev`
    

-    `libboost-thread-dev`
    

Les librairies Coin doivent être installées    *

-    `libcoin80-dev`, pour Debian Jessie, Stretch, Ubuntu 16.04 à 18.10, ou

-    `libcoin-dev`, pour Debian Buster, Ubuntu 19.04 et suivants, ainsi que pour Ubuntu 18.04/18.10 avec les [PPAs freecad-stable/freecad-daily](Installing_on_Linux/fr#Dépôt_officiel_Ubuntu.md) ajoutés à vos sources logicielles.

Plusieurs librairies traitant des mathématiques, des surfaces triangulées, du tri, des maillages, de la vision par ordinateur, des projections cartographiques, de la visualisation 3D, du système X11 Window, de l\'analyse XML et de la lecture de fichiers Zip    *

-    `libeigen3-dev`
    

-    `libgts-bin`
    

-    `libgts-dev`
    

-    `libkdtree++-dev`
    

-    `libmedc-dev`
    

-    `libopencv-dev`or `libcv-dev`

-    `libproj-dev`
    

-    `libvtk7-dev`or `libvtk6-dev`

-    `libx11-dev`
    

-    `libxerces-c-dev`
    

-    `libzipios++-dev`
    


<div class="mw-collapsible mw-collapsed" style="background-color   *#e0e0e0">

#### Python 2 et Qt4 

Ceci n\'est pas recommandé pour les nouvelles installations comme Python 2 et Qt4 sont obsolètes. À partir de la version 0.20, Freecad ne les maintient plus.


<div class="mw-collapsible-content">

Pour compiler FreeCAD pour Debian Jessie, Stretch, Ubuntu 16.04, en utilisant Python 2 et Qt4, installez les dépendances suivantes.

-    `qt4-dev-tools`
    

-    `libqt4-dev`
    

-    `libqt4-opengl-dev`
    

-    `libqtwebkit-dev`
    

-    `libshiboken-dev`
    

-    `libpyside-dev`
    

-    `pyside-tools`
    

-    `python-dev`
    

-    `python-matplotlib`
    

-    `python-pivy`
    

-    `python-ply`
    

-    `python-pyside`
    


</div>


</div>

#### Python 3 et Qt5 

Pour compiler FreeCAD avec Debian Buster, Ubuntu 19.04 et ultérieures, ainsi que Ubuntu 18.04/18.10 avec l\'un ou l\'autre des [dépôts PPA freecad-stable/freecad-daily](Installing_on_Linux/fr#Dépôt_officiel_Ubuntu.md) ajouté à vos sources de logiciels, installez les dépendances suivantes.

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `libqt5webkit5-dev`or `qtwebengine5-dev`

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

-    `python3-pivy`
    

-    `python3-ply`
    

-    `python3-pyside2.qtcore`
    

-    `python3-pyside2.qtgui`
    

-    `python3-pyside2.qtsvg`
    

-    `python3-pyside2.qtwidgets`
    

-    `python3-pyside2.qtnetwork`
    

-    `python3-pyside2.qtwebengine`
    

-    `python3-pyside2.qtwebenginecore`
    

-    `python3-pyside2.qtwebenginewidgets`
    

-    `python3-pyside2.qtwebchannel`
    

-    `python3-pyside2uic`
    

#### Noyau OpenCascade 

Le noyau OpenCascade est la librairie graphique principale pour créer des formes 3D. Il existe dans une version officielle OCCT et une version communautaire OCE. La version communautaire n\'est plus recommandée car elle est obsolète.

Pour Debian Buster, Ubuntu 18.10 et versions ultérieures, ainsi que pour Ubuntu 18.04 avec les [freecad-stable/freecad-daily PPAs](Installing_on_Linux/fr#Dépôt_officiel_Ubuntu.md) ajoutés à vos sources de logiciels, installez les paquets officiels.

-    `libocct*-dev`-   
        `libocct-data-exchange-dev`
        

    -   
        `libocct-draw-dev`
        

    -   
        `libocct-foundation-dev`
        

    -   
        `libocct-modeling-algorithms-dev`
        

    -   
        `libocct-modeling-data-dev`
        

    -   
        `libocct-ocaf-dev`
        

    -   
        `libocct-visualization-dev`
        

-    `occt-draw`
    

Pour Debian Jessie, Stretch, Ubuntu 16.04 et plus récente, installez les paquetages Édition Communautaire.

-    `liboce*-dev`-   
        `liboce-foundation-dev`
        

    -   
        `liboce-modeling-dev`
        

    -   
        `liboce-ocaf-dev`
        

    -   
        `liboce-ocaf-lite-dev`
        

    -   
        `liboce-visualization-dev`
        

-    `oce-draw`
    

Vous pouvez installer toutes les librairies individuellement ou en utilisant l'extension astérisque. Changez `occ` par `oce` si vous voulez installer les librairies de la communauté.


```python
sudo apt install libocct*-dev
```

#### Paquets optionnels 

Vous pouvez éventuellement installer ces paquets supplémentaires    *

-    `libsimage-dev`, pour que Coin prenne en charge d\'autres formats de fichier image.

-    `doxygen`et `libcoin-doc` (ou `libcoin80-doc` pour d\'anciens systèmes), si vous avez l'intention de générer de la documentation sur le code source.

-    `libspnav-dev`, pour la prise en charge des [Périphériques d\'entrée 3D](3D_input_devices/fr.md), comme \"Space Navigator\" ou \"Space Pilot\".

-    `checkinstall`, si vous avez l\'intention d\'enregistrer vos fichiers installés dans le gestionnaire de paquets de votre système, afin de pouvoir les désinstaller ultérieurement.

-    `python3-markdown`, pour que le gestionnaire d\'addons affiche nativement les fichiers README.md au format Markdown.

-    `python3-git`, pour que le gestionnaire d\'addons utilise git pour récupérer et mettre à jour les ateliers et les macros.

#### Commande unique pour Qt5 et Python 3 

Requiert Pyside2, disponible sous Debian Buster et les [freecad-stable/freecad-daily PPAs](Installing_on_Linux/fr#Dépôt_officiel_Ubuntu.md).


{{Code|lang=bash|code=
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev libqt5webkit5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig
}}

REMARQUE    * Sur certaines versions d\'Ubuntu et certaines versions de Qt, vous obtiendrez une erreur indiquant que python3-pyside2uic est introuvable \-- sur ces systèmes, vous pouvez l\'omettre sans risque. Sur Ubuntu 20.04, vous devrez ajouter `pyqt5-dev-tools`. Vous trouverez plus d\'informations dans [cette discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color   *#e0e0e0">

#### Commande unique pour Python 2 et Qt4 

Ceci n'est pas recommandé pour les nouvelles installations car Python 2 et Qt4 sont obsolètes.


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
}}

Utilisateurs de Ubuntu 16.04, veuillez aussi consulter la discussion sur la compilation dans le forum [Compiler sur Linux (Kubuntu)   * CMake ne peut pas trouver VTK](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Suivez les mêmes étapes que pour Debian et Ubuntu.

Des problèmes ont été signalés lors de la tentative de compilation en Raspbian avec Python 3 et Qt5. La combinaison Python 3 et Qt4 semble fonctionner pour les anciennes versions de FreeCAD.

Pour les versions plus récentes de FreeCAD, la compilation avec Py3/Qt5 réussit si le système d\'exploitation installé est Ubuntu 20.04.

En raison de différents problèmes avec Qt, dans cette version, les outils PySide normaux ne seront pas trouvés. {{Code|lang=bash|code=
E   * Unable to locate package python3-pyside2uic
}}

Dans ce cas, nous pouvons installer les packages depuis PyQt et créer des liens symboliques vers les outils nécessaires. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

La compilation peut maintenant se poursuivre. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

L\'option `-j` de `make` ne doit pas dépasser 3 car le Raspberry Pi a une mémoire limitée. La compilation prendra plusieurs heures, il est donc préférable de le faire pendant la nuit.

Plus d\'informations, [FreeCAD et Raspberry Pi 4](https   *//forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

Il y a un bogue dans cmake distribué par Fedora 34/35 qui fait que cmake ne trouve pas les bibliothèques d\'opencascade. Ceci peut être facilement corrigé en faisant un changement mineur au fichier cmake de niveau supérieur d\'opencascade installé sur Fedora. Plus de détails ici    * <https   *//bugzilla.redhat.com/show_bug.cgi?id=2083568>.

Vers le haut du fichier **OpenCASCADEConfig.cmake**, changez la ligne suivante pour utiliser {{Incode|REAL_PATH()}}. Ceci corrige un bogue introduit par l\'utilisation d\'un lien symbolique de {{Incode|/lib}} à {{Incode|/usr/lib}} de Fedora, qui fait échouer cmake.

Ce fichier est généralement installé dans **/usr/lib64/cmake/opencascade/OpenCASCADEConfig.cmake**.


{{Code|lang=bash|code=
get_filename_component (OpenCASCADE_INSTALL_PREFIX "${OpenCASCADE_INSTALL_PREFIX}" PATH)
}}

changez cela en    *


{{Code|lang=bash|code=
file (REAL_PATH ${OpenCASCADE_INSTALL_PREFIX} OpenCASCADE_INSTALL_PREFIX)
}}

Ce changement trivial doit être fait dans le répertoire de compilation une fois que cmake a été lancé et a échoué. Une nouvelle exécution de cmake détectera alors correctement les bibliothèques OCCT de la manière habituelle.

Vous avez besoin des paquets suivants    *

-   gcc-c++ (or possibly another C++ compiler?)
-   cmake
-   doxygen
-   swig
-   gettext
-   dos2unix
-   desktop-file-utils
-   libXmu-devel
-   freeimage-devel
-   mesa-libGLU-devel
-   OCE-devel
-   python
-   python-devel
-   python-pyside-devel
-   pyside-tools
-   boost-devel
-   tbb-devel
-   eigen3-devel
-   qt-devel
-   qt-webkit-devel
-   qt5-qtxmlpatterns
-   qt5-qttools-static
-   ode-devel
-   xerces-c
-   xerces-c-devel
-   opencv-devel
-   smesh-devel
-   Coin3
-   Coin3-devel

(Avril 2021, Coin4 et Coin4-devel sont disponibles) (si coin2 est la dernière disponible pour votre version de Fedora, utilisez les paquets à partir de <http   *//www.zultron.com/rpm-repo/>)

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk-devel
-   med
-   med-devel

Et éventuellement    *

-   libspnav-devel (pour le support des périphériques 3Dconnexion comme le Space Navigator ou le Space Pilot)
-   python3-pivy (https   *//bugzilla.redhat.com/show\_bug.cgi?id=458975 Pivy n\'est pas obligatoire mais nécessaire pour l\'atelier Draft)
-   python3-markdown (pour que le gestionnaire d\'addons affiche le markdown natif)
-   python3-git (pour que le gestionnaire d\'addons utilise git pour vérifier et mettre à jour les ateliers et les macros)


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Le moyen le plus facile de vérifier quels paquets sont nécessaires pour compiler FreeCAD et de vérifier via portage    *

emerge -pv freecad

Ceci devrait vous donner une superbe liste de paquets supplémentaires que devez avoir installés sur votre système.

Si FreeCAD n\'est pas disponible sur portage, il est disponible sur la [waebbl overlay](https   *//github.com/waebbl/waebbl-gentoo). Le suivi des problèmes sur le recouvrement waebbl Github peut vous aider à résoudre certains problèmes que vous pourriez rencontrer. La superposition fournit freecad-9999, que vous pouvez choisir de compiler ou simplement utiliser pour obtenir les dépendances.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

Les commandes suivantes installeront les packages nécessaires à la construction de FreeCAD avec Qt5 et Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

La commande suivante installera Qt Creator et le débogueur de projet GNU.


```pythonzypper in libqt5-creator gdb```

S\'il manque des packages, vous pouvez vérifier le fichier Tumbleweed [\"FreeCAD.spec\"](https   *//build.opensuse.org/package/view_file/openSUSE   *Factory/FreeCAD/FreeCAD.spec) sur [Open Build Service](https   *//build.opensuse.org/package/show/openSUSE   *Factory/FreeCAD).

Vérifiez également s'il existe des correctifs à appliquer (tels que [0001-find-openmpi2-include-files.patch](https   *//build.opensuse.org/package/view_file/openSUSE   *Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

S\'il existe une différence entre les packages disponibles sur Tumbleweed et Leap, alors vous pouvez lire le lien [\"FreeCAD.spec\"](https   *//build.opensuse.org/package/view_file/openSUSE   *Leap   *15.0/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https   *//build.opensuse.org/) pour déterminer les paquets requis.

Voir [piano\_jonas unofficial \"Compile On openSUSE\" guide](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

Vous aurez besoin des bibliothèques suivantes des référentiels officiels   *

-   boost
-   curl
-   desktop-file-utils
-   glew
-   hicolor-icon-theme
-   jsoncpp
-   libspnav
-   opencascade
-   shiboken2
-   xerces-c
-   pyside2
-   python-matplotlib
-   python-netcdf4
-   qt5-svg
-   qt5-webkit
-   qt5-webengine
-   cmake
-   eigen
-   git
-   gcc-fortran
-   pyside2-tools
-   swig
-   qt5-tools
-   shared-mime-info
-   coin
-   python-pivy
-   med


```python
sudo pacman -S boost curl desktop-file-utils glew hicolor-icon-theme jsoncpp libspnav opencascade shiboken2 xerces-c pyside2 python-matplotlib python-netcdf4 qt5-svg qt5-webkit qt5-webengine cmake eigen git gcc-fortran pyside2-tools swig qt5-tools shared-mime-info coin python-pivy med
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Distributions anciennes et non-conventionnelles 


<div class="mw-collapsible-content">

Sous d\'autres distributions, nous n\'avons que très peu de retours des utilisateurs, il pourrait être plus difficile de trouver les paquets requis.

Essayez d'abord de localiser les bibliothèques requises mentionnées dans [third party libraries/fr\|bibliothèques tierces](Third_Party_Libraries.md) dans votre gestionnaire de paquets. Attention, certains d\'entre eux pourraient avoir un nom de paquet légèrement différent; recherchez `name`, mais aussi `libname`, `name-dev`, `name-devel` et similaire. Si ce n\'est pas possible, essayez de compiler vous-même ces bibliothèques.

FreeCAD requiert une version du compilateur GNU g++ supérieure ou égale à la version 3.0.0, car FreeCAD est principalement écrit en C++. Lors de la compilation, certains scripts Python sont exécutés. L\'interpréteur Python doit donc fonctionner correctement. Pour éviter tout problème d'éditeur de liens, il est également conseillé d'avoir les chemins de bibliothèque dans la variable `LD_LIBRARY_PATH` ou dans le fichier `ld.so.conf`. Cela est déjà fait dans les distributions Linux modernes, mais il faudra peut-être le configurer dans les anciennes.


</div>


</div>

### Pivy

[Pivy](Pivy/fr.md) (les wrappers Python sous Coin3d) n\'est pas nécessaire pour construire FreeCAD ni pour le démarrer, mais il est nécessaire en tant que dépendance d\'exécution par l\'[atelier Draft](Draft_Workbench/fr.md). Si vous n\'utilisez pas cet atelier, vous n\'aurez pas besoin de Pivy. Cependant, notez que l\'atelier Draft est utilisé en interne par d\'autres ateliers, tels que [Arch](Arch_Workbench/fr.md) et [BIM](BIM_Workbench/fr.md), aussi Pivy doit-il être installé pour pouvoir également utiliser ces ateliers.

Depuis novembre 2015, la version obsolète de Pivy incluse dans le code source de FreeCAD n\'est plus compilée sur de nombreux systèmes. Ce n\'est pas un gros problème car normalement vous devriez obtenir Pivy depuis le gestionnaire de paquets de votre distribution ; si vous ne trouvez pas Pivy, vous devrez peut-être le compiler vous-même, voir les [instructions de compilation de Pivy](Extra_python_modules/fr#Pivy.md).

### Symboles de débogage 

Afin de résoudre les pannes dans FreeCAD, il est utile de disposer des symboles de débogage d\'importantes bibliothèques de dépendances telles que Qt. Pour cela, essayez d\'installer les packages de dépendance se terminant par `-dbg`, `-dbgsym`, `-debuginfo` ou similaire, selon votre distribution Linux.

Pour Ubuntu, vous devrez peut-être activer les dépôts spéciaux pour pouvoir voir et installer ces paquets de débogage avec le gestionnaire de paquets. Voir [Paquets de symboles de débogage](https   *//wiki.ubuntu.com/Debug_Symbol_Packages) pour plus d\'informations.

## Compiler FreeCAD 


**La compilation avec Python 2 et Qt 4 n'est plus bien prise en charge et à partir de 0.20 n'est plus supportée du tout. Vous devrez compiler avec Python 3 et Qt 5. La 0.20 nécessite au moins Python 3.6 et Qt 5.9.**

FreeCAD utilise CMake comme système de construction principal, qui est un système de compilation disponible sur tous les principaux systèmes d\'exploitation. Compiler avec CMake est généralement très simple et se fait en deux étapes.

1.  CMake vérifie que tous les programmes et toutes les bibliothèques nécessaires sont présents sur votre système et génère un `Makefile` qui est configuré pour la deuxième étape. FreeCAD a le choix entre plusieurs options de configurations. Certaines alternatives sont détaillées ci-dessous.
2.  La compilation elle-même, effectuée avec le programme `make`, génère les exécutables FreeCAD.

FreeCAD étant une application volumineuse, la compilation de tout le code source peut durer de 10 minutes à une heure, en fonction de votre CPU et du nombre de cœurs de CPU utilisés pour la compilation.

Vous pouvez générer le code dans ou hors du répertoire source. La construction hors source est généralement la meilleure option.

### Compilation out-of-source 

Construire (build) dans un dossier séparé est plus pratique que de construire dans le même répertoire que celui où se trouve le code source, car chaque fois que vous mettez à jour le code source, CMake peut déterminer de manière intelligente les fichiers modifiés et recompiler uniquement ce qui est nécessaire. Ceci est très utile lorsque vous testez différentes branches de Git, car vous ne confondez pas le système de construction.

Pour construire out-of-source, créez simplement un répertoire de construction (`freecad-build`) distinct de votre dossier source FreeCAD (`freecad-source`) ; ensuite depuis le dossier de compilation pointez `cmake` comme dossier source. Vous pouvez également utiliser `cmake-gui` ou `ccmake` au lieu de `cmake` dans les instructions ci-dessous. Une fois que `cmake` a fini de configurer l'environnement, utilisez `make` pour lancer la nouvelle compilation.


{{Code|lang=bash|code=
mkdir freecad-build
cd freecad-build
cmake ../freecad-source
make -j$(nproc --ignore=2)
}}

Remarque   * Si vous compilez la branche de version 0.19, vous devez explicitement spécifier que vous compilez avec Qt5 et Python 3 - Remplacez la commande CMAKE ci-dessus par   * {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

L\'option `-j` de `make` contrôle le nombre de jobs (fichiers) compilés en parallèle. Le programme `nproc` retourne le nombre de cœurs de processeur de votre système utilisés avec l\'option `-j`, vous pouvez choisir de procéder sur autant de fichiers que vous avez de cœurs afin d\'accélérer la compilation. Dans l\'exemple ci-dessus, il sera utilisé tous les cœurs de votre système sauf deux ; Cela permettra à votre ordinateur de rester réactif pour d\'autres usages pendant la compilation en arrière-plan. L\'exécutable FreeCAD apparaîtra éventuellement dans le dossier `freecad-build/bin`. Voir aussi [Compilation (accélération)](Compiling_(Speeding_up)/fr.md) pour améliorer la vitesse de compilation.

### Résoudre les problèmes de cmake 

Si vous avez déjà effectué une construction hors source et que vous êtes bloqué par une dépendance qui n\'est pas reconnue ou qui ne semble pas pouvoir être résolue, essayez ce qui suit    *

-   Supprimez le contenu du répertoire de construction avant de relancer cmake. FreeCAD est une cible qui évolue rapidement, vous pouvez rencontrer des informations de cmake en cache qui pointent vers une version plus ancienne que celle que la nouvelle tête de dépôt peut utiliser. Vider le cache peut permettre à cmake de récupérer et de reconnaître la version dont vous avez réellement besoin.

-   Si cmake se plaint qu\'il manque un fichier spécifique, utilisez un outil tel que \"apt-file search\" ou son équivalent dans d\'autres systèmes de paquets, pour découvrir à quel paquetage appartient ce fichier et l\'installer. Gardez à l\'esprit que vous aurez probablement besoin de la version -dev du paquetage qui contient les fichiers d\'en-tête ou de configuration nécessaires à FreeCAD pour utiliser le paquetage.

### Compiler avec GNU libc 2.34 et versions ultérieures 

GNU libc 2.34 introduit un changement dans la bibliothèque qui peut faire échouer les builds sur certains systèmes Linux avec une erreur du type    *


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

Pour résoudre ce problème, un lien symbolique doit être créé manuellement à partir de libdl.so.\* (maintenant vide) installé sur le système vers l\'emplacement où votre compilateur indique qu\'il recherche le fichier. Par exemple (si la copie réellement installée de libdl.so sur votre système est /usr/lib/x86\_64-linux-gnu/libdl.so.2)    *


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Adaptez la commande à la structure de votre système en recherchant libdl.so\* et en le liant à l\'emplacement approprié.

### Compilation in-source 

Les compilations in-source conviennent si vous voulez compiler rapidement une version de FreeCAD et que vous n'avez pas l'intention de mettre à jour souvent le code source. Dans ce cas, vous pouvez supprimer le programme compilé et la source en supprimant simplement un seul dossier.

Allez dans le répertoire source et pointez `cmake` dans le répertoire actuel (désigné par un simple point)    *


{{Code|lang=bash|code=
cd freecad-source
cmake . -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
make -j$(nproc --ignore=2)
}}

L'exécutable FreeCAD se trouvera alors dans le répertoire `freecad-source/bin`.

### Comment réparer votre répertoire du code source 

Si vous avez accidentellement effectué une compilation dans le répertoire du code source, ou ajouté des fichiers étranges, et souhaitez restaurer le contenu uniquement du code source d\'origine, vous pouvez effectuer les étapes suivantes.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

La première ligne efface le fichier `.gitignore`. Cela garantit que les commandes de nettoyage et de réinitialisation suivantes s\'appliqueront à tout le contenu du répertoire et n\'ignoreront pas les éléments correspondant aux expressions contenues dans `.gitignore`. La deuxième ligne supprime tous les fichiers et répertoires qui ne sont pas suivis par le référentiel git, puis la dernière commande réinitialisera toutes les modifications apportées aux fichiers suivis, y compris la première commande effaçant le fichier `.gitignore`.

Si vous n\'effacez pas le répertoire source, les exécutions ultérieures de `cmake` risquent de ne pas intégrer les nouvelles options sur le système si le code change.

### Configuration

En appliquant différentes options à `cmake`, vous pouvez modifier la manière dont FreeCAD est compilé. La syntaxe est la suivante.


```python
cmake -D <var>   *<type>=<value> $SOURCE_DIR
```

Où `$SOURCE_DIR` est le répertoire qui contient le code source. Le `<type>` peut être omis dans la plupart des cas. L\'espace après l\'option `-D` peut également être omis.

Par exemple, pour éviter de construire le [module FEM](FEM_Workbench/fr.md)    *


{{Code|lang=bash|code=
cmake -D BUILD_FEM   *BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

Toutes les variables possibles sont répertoriées dans le fichier `InitializeFreeCADBuildOptions.cmake`, situé dans le dossier `cMake/FreeCAD_Helpers`. Dans ce fichier, recherchez le mot `option` pour obtenir toutes les variables pouvant être définies et voir leurs valeurs par défaut.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Vous pouvez également utiliser la commande `cmake -LH` pour répertorier la configuration actuelle, ainsi que toutes les variables pouvant être modifiées. Vous pouvez également installer et utiliser `cmake-gui` pour lancer une interface graphique affichant toutes les variables pouvant être modifiées. Dans les sections suivantes, nous énumérons certaines des options les plus pertinentes que vous souhaiterez peut-être utiliser.

#### Pour une compilation de Debogage 

Créez une version `Debug` pour résoudre les pannes dans FreeCAD. Attention, avec cette construction, l\'atelier [Sketcher](Sketcher_Workbench/fr.md) devient très lent avec des esquisses complexes.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}

#### Pour une compilation \"Release\" 

Créez une version `Release` pour tester que le code qui ne plante pas. Une `Release` sera beaucoup plus rapide qu\'une version `Debug`.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}

#### Compiler en s\'appuyant sur Python 3 et Qt5 

Par défaut, FreeCAD 0.19 et les versions antérieures sont compilées pour Python 2 et Qt4. Comme ces deux paquets sont obsolètes, il est préférable de compiler pour Python 3 et Qt5. Le support de Python 2 et Qt4 a été supprimé dans FreeCAD 0.20 et il n\'est pas nécessaire d\'activer explicitement Qt5 et Python 3 si vous compilez les dernières versions de développement.

Dans une distribution Linux moderne, il suffit de fournir deux variables spécifiant l\'utilisation de Qt5 et le chemin d\'accès à l\'interpréteur Python.

Pour la 0.19   * {{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Pour la 0.20\_dev   * {{Code|lang=bash|code=
cmake ../freecad-source
}}

Remarquez que lorsque vous passez de la version 0.19 à la version 0.20, il peut être nécessaire de supprimer CMakeCache.txt avant d\'exécuter cmake.

#### Compiler pour une version spécifique de Python 

Si l\'exécutable `python` par défaut de votre système est un lien symbolique vers Python 2, `cmake` essaiera de configurer FreeCAD pour cette version. Vous pouvez choisir une autre version de Python en donnant le chemin d\'un exécutable spécifique    *


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Si cela ne fonctionne pas, vous devrez peut-être définir des variables supplémentaires pointant sur les bibliothèques Python souhaitées et les répertoires inclus    *


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

Il est possible d\'avoir plusieurs versions indépendantes de Python dans le même système. Par conséquent, l\'emplacement et le numéro de version de vos fichiers Python dépendent de votre distribution Linux. Utilisez `python3 -V` pour afficher la version de Python que vous utilisez actuellement. Seuls les deux premiers chiffres sont nécessaires ; Par exemple, si le résultat est `Python 3.6.8`, vous devez spécifier les répertoires associés à la version 3.6. Si vous ne connaissez pas les bons répertoires, essayez de les rechercher avec la commande `locate`.


```python
locate python3.6
```

Vous pouvez utiliser `python3 -m site` dans un terminal pour déterminer les répertoires `site-package` ou `dist-package` sur les systèmes Debian.

Certains composants de FreeCAD, comme PySide, essaient de détecter automatiquement la version la plus récente de Python installée sur votre système, ce qui peut échouer si elle est différente de celle que vous avez entrée ci-dessus. L\'ajout de l\'option cMake suivante pourrait résoudre le problème    *


{{Code|lang=bash|code=
-DPython3_FIND_STRATEGY=LOCATION
}}

#### Compiler avec Qt Creator en s\'appuyant sur Python 3 and Qt5 

1\. Lancez Qt Creator.

2\. Cliquez sur **Open Project**.

3\. Accédez au répertoire où se trouve le code source `freecad-source/` et choisissez le fichier `CMakeLists.txt` le plus haut.

4\. En sélectionnant le fichier, il s\'exécutera automatiquement sur `cmake`, mais il peut échouer si les options appropriées ne sont pas correctement définies.

5\. Accédez à **Projects → Build & Run → Imported Kit → Build → Build Settings → CMake**. Définissez le répertoire de construction approprié, `freecad-build/`.

6\. Définissez les variables appropriées dans la boîte de dialogue Valeur-clé, de types `String` et `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
BUILD_QT5=ON
```

7\. Si les variables ne chargent pas correctement le projet, vous devrez peut-être accéder à **Projects → Manage Kits → Kits → Default (ou Imported Kit ou similaire) → CMake Configuration**. Appuyez ensuite sur **Change** et ajoutez la configuration appropriée comme décrit ci-dessus. Vous devrez peut-être ajouter plus de variables sur les chemins Python, si le système Python n\'est pas trouvé. 
```python
PYTHON_EXECUTABLE   *STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR   *STRING=/usr/include/python3.7m
PYTHON_LIBRARY   *STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH   *STRING=/usr/lib/python3.7/site-packages
BUILD_QT5   *BOOL=ON
```

7.1. Appuyez sur **Apply**, puis sur **OK**.

7.2. Assurez-vous que les autres options sont correctement définies, par exemple, **Qt version** doit être une version actuelle installée dans le système, comme `Qt 5.9.5 dans PATH (qt5)`.

Appuyez sur **Apply** puis sur **OK** pour fermer la configuration.

Le programme `cmake` devrait s\'exécuter de nouveau automatiquement et il devrait remplir la boîte de dialogue Valeur-clé entière avec toutes les variables qui peuvent être configurées.

8\. Allez à **Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration** et choisissez `FreeCADMain` pour compiler la version graphique de FreeCAD ou `FreeCADMainCMD` pour ne compiler que la version en ligne de commande.

9\. Enfin, allez dans le menu **Build → Build Project "FreeCAD"**. S\'il s\'agit d\'une nouvelle compilation, cela devrait prendre plusieurs minutes, voire heures, selon le nombre de processeurs dont vous disposez.

#### Plugin Qt designer 

Si vous souhaitez développer des éléments de code Qt pour FreeCAD, vous aurez besoin du plugin Qt Designer qui fournit tous les widgets personnalisés de FreeCAD.

Allez dans un répertoire auxiliaire du code source, lancez `qmake` avec le fichier de projet indiqué pour créer un `Makefile` ; puis lancez `make` pour compiler le plugin.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Si vous compilez pour Qt5, assurez-vous que le code binaire `qmake` est celui de cette version, afin que `Makefile` résultant contienne les informations nécessaires pour Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

Où `$QT_DIR` est le répertoire qui stocke les bibliothèques binaires Qt, par exemple, `/usr/lib/x86_64-linux-gnu/qt5`.

La librairie créée est `libFreeCAD_widgets.so`, qui doit être copiée dans `$QTDIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}

#### Pivy interne ou externe 

Auparavant, une version de Pivy était incluse dans le code source de FreeCAD (interne). Si vous souhaitez utiliser la copie de Pivy (externe) de votre système, vous devez utiliser -DFREECAD_USE_EXTERNAL_PIVY=1.

L\'utilisation externe de Pivy est devenue la valeur par défaut à partir du développement de FreeCAD 0.16 ; cette option n\'a donc plus besoin d\'être définie manuellement.

#### Documentation Doxygen 

Si vous avez installé Doxygen, vous pouvez créer la documentation du code source. Voir la [documentation source](source_documentation/fr.md) pour les instructions.

### Documentation complémentaire 

Le code source de FreeCAD est très complet et avec CMake, il est possible de configurer de nombreuses options. Apprendre à utiliser pleinement CMake peut être utile pour choisir les bonnes options pour vos besoins particuliers.

-   [Documentation de référence CMake](https   *//cmake.org/documentation/) par Kitware.
-   [Comment construire un projet basé sur CMake](https   *//preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) en s\'appuyant sur la programmation.
-   [le langage de script de CMake en 15 minutes](https   *//preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/Apprenez) (blog) en s\'appuyant sur la programmation.

### Construire un paquet Debian 

Si vous envisagez de construire un paquet Debian voici les sources que vous devez d'abord installer certains paquets    *


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Allez dans le répertoire FreeCAD et appelez


{{Code|lang=bash|code=
debuild
}}

Une fois que le paquet est construit, vous pouvez utiliser `lintian` pour vérifier si le paquet contient des erreurs


{{Code|lang=bash|code=
lintian freecad-package.deb
}}

## Mettre à jour le code source 

Le système CMake vous permet de mettre à jour intelligemment le code source et de ne recompiler que ce qui a changé, ce qui accélère les compilations ultérieures.

Déplacez-vous à l\'emplacement où le code source FreeCAD a été téléchargé pour la première fois et récupérez le nouveau code    *


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Puis déplacez-vous dans le répertoire de construction où le code a été initialement compilé, et lancez `cmake` spécifiant le répertoire actuel (indiqué par un point), puis déclenchez la recompilation avec `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}

## Dépannage

### Pour les systèmes 64 bits 

Pour la compilation de FreeCAD en 64 bits, il y a un problème connu avec le paquet OpenCASCADE (OCCT) 64 bits. Pour que FreeCAD fonctionne correctement, vous devrez peut-être exécuter le script `configure` et définir des `CXXFLAGS` supplémentaires    *


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

Pour les systèmes basés sur Debian, cette option n'est pas nécessaire lors de l'utilisation des packages OpenCASCADE pré-construits, car ceux-ci définissent le bon `CXXFLAGS` en interne.

## Scripts de compilation automatiques 

Voici tout ce dont vous avez besoin pour une compilation complète de FreeCAD. C\'est une approche en un script qui fonctionne sur une distribution Linux récemment installée. Les commandes demanderont le mot de passe root pour l\'installation des packages et des nouveaux référentiels en ligne. Ces scripts doivent fonctionner sur les versions 32 et 64 bits. Ils sont écrits pour différentes versions, mais sont également susceptibles de fonctionner sur une version ultérieure avec ou sans modifications majeures.

Si vous avez un tel script pour votre distribution préférée, veuillez en discuter sur le [forum FreeCAD](https   *//forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134) afin que nous puissions l\'intégrer.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

Ces scripts constituent un moyen fiable d'installer le bon ensemble de dépendances requises pour créer et exécuter FreeCAD sur Ubuntu. Ils utilisent les PPA (personal package archives) et devraient fonctionner sur toute version d\'Ubuntu ciblée par le PPA. Le PPA [freecad-daily](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) cible les versions récentes d\'Ubuntu, tandis que le PPA [freecad-stable](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) cible les versions officiellement prises en charge d\'Ubuntu.

Ce script installe l'aperçu instantané de la compilation quotidiennement de FreeCAD et ses dépendances. Il ajoute le référentiel quotidien, obtient les dépendances pour construire cette version et installe les packages requis. Ensuite, il extrait le code source dans un répertoire particulier, crée un répertoire de construction et y apporte des modifications, configure l\'environnement de compilation avec `cmake` et finalement construit l\'ensemble du programme avec `make`. Enregistrez le script dans un fichier, rendez-le exécutable et exécutez-le, mais n\'utilisez pas `sudo`; les privilèges de super-utilisateur ne seront demandés que pour les commandes sélectionnées.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa   *freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

Si vous le souhaitez, vous pouvez désinstaller la version pré-compilée de FreeCAD (`freecad-daily`) en laissant les dépendances en place. Toutefois, laisser ce paquet installé permettra au gestionnaire de paquets de garder ses dépendances à jour également ; Cela est surtout utile si vous souhaitez suivre le développement de FreeCAD et mettre à jour et compiler en permanence les sources à partir du référentiel Git.

Le script précédent suppose que vous souhaitiez compiler la dernière version de FreeCAD, vous utilisez donc le référentiel \"quotidien\" pour obtenir les dépendances. Cependant, vous pouvez préférer obtenir les dépendances de construction de la version \"stable\" pour la version actuelle d\'Ubuntu. Si tel est le cas, remplacez la partie supérieure du script précédent par les instructions suivantes. Pour Ubuntu 12.04, omettez `--enable-source` de la commande.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa   *freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Une fois que vous avez installé le paquet `freecad` à partir du référentiel `freecad-stable`, il remplacera l\'exécutable FreeCAD disponible à partir du référentiel Universe Ubuntu. L\'exécutable s\'appellera simplement `freecad`, et non pas `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">

Aucun dépôt externe n\'est nécessaire pour compiler FreeCAD. Cependant, il y a une incompatibilité avec python3-devel qui doit être supprimée. FreeCAD peut être compilé à partir de GIT.


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone https   *//github.com/FreeCAD/FreeCAD.git free-cad
 
# Now you will have a subfolder in this location called free-cad. It contains the source
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build1
cd FreeCAD-Build1 
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}

Après avoir utilisé git, la prochaine fois que vous souhaiterez recompiler vous même, vous n\'aurez pas à tout cloner, il vous suffira d\'extraire de git et de recompiler une nouvelle fois.


{{Code|lang=bash|code=
# go into free-cad dir created earlier
cd free-cad
 
# pull
git pull
 
# get back to previous dir
cd ..
 
# Now repeat last few steps from before.
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build2
cd FreeCAD-Build2
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
# Note   * to speed up build use all CPU cores   * make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Debian Squeeze 


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
# get the needed tools and libs
sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
libqt4-dev qt4-dev-tools python2.5-dev \
libsimage-dev libopencascade-dev \
libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
libtool autotools-dev automake gfortran
 
# checkout the latest source
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note   * to speed up build use all CPU cores   * make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora 27/28/29 


<div class="mw-collapsible-content">

Vous pouvez poster à l\'utilisateur [http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) sur le forum.


{{Code|lang=bash|code=
#!/bin/bash

ARCH=$(arch)

MAIN_DIR=FreeCAD
BUILD_DIR=build

#FEDORA_VERSION=27
#FEDORA_VERSION=28
FEDORA_VERSION=29

PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
 freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"

FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"

if [ "$FEDORA_VERSION" = "29" ]; then
    PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
fi

echo "Installing packages required to build FreeCAD"
sudo dnf -y install $PACKAGES
cd ~
mkdir $MAIN_DIR <nowiki>||</nowiki> { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
cd $MAIN_DIR
git clone https   *//github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch utilise AUR 


<div class="mw-collapsible-content">

[Arch User Repository (AUR)](https   *//aur.archlinux.org/) est une collection de recettes faites par les utilisateurs pour construire des packages qui ne sont pas officiellement supportés par les responsables de la distribution / la communauté. Ils sont généralement en sécurité. Vous pouvez voir qui gère le colis et pendant combien de temps il l\'a fait. Il est recommandé de vérifier les fichiers de construction. Des logiciels non-open source sont également disponibles dans cette zone même s\'ils sont gérés par la société propriétaire.

Prérequis    * git

Étapes    *

1.  Ouvrez un terminal. Créez éventuellement un répertoire, par exemple `mkdir git`. Éventuellement changer de répertoire par exemple `cd git`.
2.  Cloner le référentiel AUR    * `git clone http   *//aur.archlinux.org/packages/freecad-git`
3.  Entrez le dossier du référentiel AUR    * `cd freecad-git`
4.  Compiler en utilisant [Arch makepkg](https   *//wiki.archlinux.org/index.php/Makepkg)    * `makepkg -s`. Les flag -s ou \--syncdeps installeront également les dépendances requises.
5.  Installer le paquet créé    * `makepkg --install` ou double-cliquez sur pkgname-pkgver.pkg.tar.xz dans votre navigateur de fichiers.

Pour mettre à jour FreeCAD vers la dernière version, recommencez à partir de l\'étape 3. Mettez à jour le référentiel AUR en cas de modifications importantes de la recette ou de nouvelles fonctionnalités à l\'aide de `git checkout -f` dans le dossier.







[Category   *Developer\_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/fr
