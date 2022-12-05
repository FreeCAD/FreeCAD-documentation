# FEM Install/fr
{{TOCright}}

## Introduction

Pour pouvoir effectuer une analyse par éléments finis (FEA) dans l\'**<img src="images/Workbench_FEM.svg" width=24px> [atelier FEM](FEM_Workbench/fr.md)**, FreeCAD utilise deux programmes externes: l'un est utilisé pour générer le [FEM Mesh](FEM_Mesh/fr.md), l'autre pour la résolution numérique du analyse réelle. Vous pouvez tester si votre installation FreeCAD est prête pour une FEA en exécutant l'exemple [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/fr.md) fourni avec l\'installation de FreeCAD depuis la v0.17.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;"> 
*Workflow de l'atelier FEM; le plan de travail appelle deux programmes externes pour effectuer le maillage d'un objet solide et pour résoudre le problème des éléments finis*

### Solveur FEM 

Le solveur par défaut pour effectuer des calculs par éléments finis est [CalculiX](FEM_CalculiX/fr.md), un solveur simple pour l\'analyse de structures. FreeCAD écrit un fichier d\'entrée CalculiX, lance le solveur et lit le résultat qui peut ensuite être présenté visuellement dans la fenêtre d\'affichage. Cela signifie que le binaire CalculiX est autonome et indépendant de FreeCAD. Etant donné que de nombreux programmes peuvent générer un maillage, il est recommandé d'installer le solveur et de s'assurer qu'il fonctionne en premier.

Si le solveur est correctement installé, vous pouvez exécuter la commande unique `ccx` dans le terminal pour obtenir une réponse simple:


{{SystemInput|User@PC:~$ ccx}}


```python
Usage: CalculiX.exe -i jobname
```

Si le solveur est installé, assurez-vous que l\'atelier FEM est capable de trouver le binaire. Allez à **Edition → Préférences → FEM → CalculiX → Search in known binary directories**. Si vous avez compilé le solveur vous-même, décochez l\'option et donnez le chemin correct au fichier binaire. Pour les autres solveurs pouvant être utilisés avec FreeCAD, voir [FEM Solveur](FEM_Solver/fr.md).

### Générateur de maillage FEM 

Afin de créer un [maillage FEM](FEM_Mesh/fr.md), FreeCAD utilise [Gmsh](http://gmsh.info/) comme mailleur par défaut. En fonction de votre système d\'exploitation et de votre installation de FreeCAD, Gmsh est inclus ou non dans les binaires d\'installation de FreeCAD. S\'il n\'est pas intégré, vous pouvez l\'installer séparément de FreeCAD et ensuite utiliser le menu **Edition → Préférences → FEM → Gmsh** pour définir le chemin vers le *gmsh.exe*.

Si le programme est correctement installé, vous pouvez exécuter la commande `gmsh` dans le terminal pour lancer l\'interface graphique du programme. Cette interface n'est pas utilisée par FreeCAD mais montre que le programme est installé.


{{SystemInput|User@PC:~$ gmsh -info}}


```python
Version          : 3.0.6
License          : GNU General Public License
Build OS         : Linux64
Build date       : 20171107
Build host       : lgw01-amd64-034
Build options    : 64Bit Ann Bamg Bfgs Blas(Generic) Blossom C++11 Cgns Chaco DIntegration Dlopen Fltk Gmm Jpeg Kbipack Lapack(Generic) LinuxJoystick MPI MathEx Med Mesh Mmg3d Mpeg NativeFileChooser Netgen ONELAB ONELABMetamodel OpenCASCADE OpenGL OptHom Parser Plugins Png Post Python Solver TetGen/BR Tetgen Voro3D Zlib
FLTK version     : 1.3.4
OCC version      : 6.9.1
MED version      : 3.0.6
Packaged by      : buildd
Web site         : http://gmsh.info
Mailing list     : gmsh@onelab.info
```

Si le mailleur est installé, assurez-vous que l\'atelier FEM est capable de trouver le binaire. Allez à **Edition → Préférences → FEM → Gmsh → Search in known binary directories**. Si vous avez compilé le mailleur vous-même, décochez l\'option et donnez le chemin correct au fichier binaire. Voir [FEM Mesh](FEM_Mesh/fr.md) pour les différentes possibilités d\'obtenir un maillage valide pour l\'analyse.

### Netgen


**Note: le mailleur Netgen a été désactivé en mars 2017, lorsque FreeCAD est passé à l'utilisation de OCCT 7.1. Modifiez ces informations si Netgen est à nouveau utilisable avec la version stable de FreeCAD.**

Dans les versions précédentes de FreeCAD, [Netgen](https://sourceforge.net/projects/netgen-mesher/) était le mailleur par défaut. Pour fonctionner avec l\'atelier FEM, FreeCAD devait être lié aux bibliothèques Netgen au moment de la compilation. Alors que FreeCAD passait de OCE 0.17 à OCCT 7.1, Netgen 4.9.13 n\'a pas réussi à établir de liaison avec cette version d\'OCCT. Il a donc été décidé de supprimer le support Netgen dans [Atelier FEM](FEM_Workbench/fr.md) (le bouton [Netgen button](FEM_MeshNetgenFromShape.md) a été enlevé). Néanmoins, peu après, certains utilisateurs ont signalé qu\'ils avaient réussi à appliquer une correction à Netgen 5.3.1, qui fonctionnait donc avec OCCT 7.x et FreeCAD.

Pour référence historique, voir les discussions:

-   [(Ubuntu Daily PPA) Transitioning to OCCT7, VTK7\...](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501)
-   [Ubuntu Daily Builds PPA now using OCC 7.1.0](https://forum.freecadweb.org/viewtopic.php?t=21246)
-   [patching Netgen 5.3.1](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&start=200#p165769) to work with OCCT 7.1
-   [Troubles with gmsh in FEM wb (netgen nostalgy)](https://forum.freecadweb.org/viewtopic.php?t=28368)

Bien que Netgen ne soit pas disponible à partir de [Atelier FEM](FEM_Workbench/fr.md), il peut toujours être utilisé seul pour produire des maillages pouvant être importés.

Si le programme est correctement installé, vous pouvez exécuter la commande `netgen` dans le terminal pour lancer l\'interface graphique du programme.


{{SystemInput|User@PC:~$ netgen -V}}


```python
NETGEN-6.2-dev
Developed by Joachim Schoeberl at
2010-xxxx Vienna University of Technology
2006-2010 RWTH Aachen University
1996-2006 Johannes Kepler University Linz
Including OpenCascade geometry kernel
Run parallel Netgen with 'mpirun -np xy netgen'
NETGENDIR = .
Tcl header version = 8.6.8
Tcl runtime version = 8.6.8 
using internal Tcl-script
optfile ./ng.opt does not exist - using default values
togl-version : 2
OCC module loaded
```

## Installation sous Windows 

Les paquets FreeCAD disponibles à partir de la page [Téléchargements](Download/fr.md) incluent déjà Netgen et CalculiX, donc aucun logiciel supplémentaire ne doit être installé. Quelques liens pour obtenir un meilleur exécutable Calculix que celui inclus dans FreeCAD peuvent être trouvés ici [alternative ccx executables](https://forum.freecadweb.org/viewtopic.php?f=18&t=58792&start=10#p506164).


<div class="mw-collapsible mw-collapsed toccolours">

## Installation sous Linux 

Les distributions Linux ont différentes manières d\'installer un logiciel. De nombreuses distributions ont des référentiels de logiciels et des gestionnaires de paquets; avant de compiler le code source, recherchez dans votre gestionnaire de paquets pour `netgen`, `gmsh`, `calculix-ccx` ou `ccx` et installez-les d\'après les instructions de votre propre distribution.


<div class="mw-collapsible-content">

### PPA Ubuntu 

Les versions PPA (personal package archives) [stable de Freecad](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) et [développement de Freecad](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) fournissent une version de FreeCAD plus récente que celle disponible dans les dépôts officiels d\'Ubuntu. Ces PPA incluent également les derniers `netgen`, `gmsh` et `calculix-ccx`. Voir [Installation sous Linux](Installing_on_Linux/fr.md) pour plus d\'informations sur la configuration des référentiels.

Si un PPA est déjà ajouté à votre système, installez les packages comme suit


```python
sudo apt-get install netgen
sudo apt-get install gmsh
sudo apt-get install calculix-ccx
```

Le PPA [freecad-community](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) fournit également les `netgen`, `gmsh` et `calculix-ccx` paquets à tester. S\'ils sont suffisamment stables, ils peuvent être ajoutés aux référentiels quotidiens ou stables. Les binaires pour ccx 2.14 fonctionnent sur Debian Stretch mais pas sur Debian Buster en raison de problèmes de dépendance.


**Note:**

le fil [Ubuntu Repository](http://forum.freecadweb.org/viewtopic.php?f=18&t=10393) traite de la création des packages PPA Ubuntu. Au moment de sa rédaction, CalculiX n\'était pas inclus dans les référentiels Debian. Il y avait donc plusieurs paquets personnels dans Launchpad. Un seul paquet doit être installé.

### Arch Linux 

Récupérez le package CalculiX à partir de [AUR repository](https://aur.archlinux.org/packages/calculix/).

### Debian

-   Debian 9 Buster: les paquets [dépôts](https://packages.debian.org/buster/calculix-ccx) sont obsolètes, mais vous pouvez utiliser les paquets du PPA Ubuntu (`freecad-community`). Voir [Gmsh 4 package available for testing in Community Extras PPA](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p279925) (post de forum).
-   Debian 8 Stretch: les paquets [dépôts](https://packages.debian.org/stretch/calculix-ccx) sont obsolètes, mais vous pouvez utiliser les packages de la PPA Ubuntu (`freecad-community`). Voir [Gmsh 4 package available for testing in Community Extras PPA](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&p=279925#p260872) (post de forum).
-   Debian 7 Jessie: installez les paquets à partir de Debian 8 Stretch en utilisant `dpkg`. Voir [http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&p=110597#p110597 Debian source package for Calculix](http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&p=110597#p110597_Debian_source_package_for_Calculix.md) (message sur le forum).

### openSUSE

-   [openSUSE:Science Math](https://en.opensuse.org/openSUSE:Science_Math#Mesh_Generation_and_Related_Tools)
-   [netgen Automatic 3D tetrahedral mesh generator](https://software.opensuse.org/package/netgen)
-   [gmsh A three-dimensional finite element mesh generator](https://software.opensuse.org/package/gmsh)
-   [ccx An open source finite element package](https://software.opensuse.org/package/ccx)

Les paquets supplémentaires sont généralement installés avec YAST (abbr. Yet another Setup Tool), l\'outil d\'installation et de configuration du système d\'exploitation Linux ou dans n\'importe quel terminal/console (droits root requis) avec :

:   
    
```python
    zypper install netgen
    zypper install gmsh
    zypper install ccx
    
```
    

### Binaire CalculiX 

Les auteurs CalculiX fournissent un binaire Linux précompilé du solveur. Il peut être téléchargé à partir du [site web des auteurs](http://www.dhondt.de/). Cependant, étant donné que les différentes distributions Linux ont des chemins de bibliothèque différents, ce binaire ne fonctionnera probablement pas sans certains ajustements.

Pour utiliser le binaire avec Fedora 21, voir le fil [Making FEM run on linux fedora 21](http://forum.freecadweb.org/viewtopic.php?f=18&t=10140). Pour les versions plus récentes de Fedora, vous devez compiler CalculiX vous-même.

Si vous utilisez ce binaire, vérifiez que le binaire est exécutable, qu\'il se trouve dans l\'exécutable `$PATH` de votre système et que vous disposez de la version nécessaire des bibliothèques (`libgfortran`, `liblapack`, `libblas`, etc.) pour lequel il a été compilé. Ceci est mentionné dans le message du forum [FEM WB](http://forum.freecadweb.org/viewtopic.php?f=3&t=11830&start=20#p95741).

Utilisez la commande `ldd` pour voir les bibliothèques liées par le binaire. Installez les dépendances manquantes.


{{SystemInput|User@PC:~$ ldd /usr/bin/ccx}}


```python
linux-vdso.so.1 (0x00007fffbabdc000)
 libspooles.so.2.2 => /usr/lib/x86_64-linux-gnu/libspooles.so.2.2 (0x00007fe9bd042000)
 libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe9bce23000)
 libarpack.so.2 => /usr/lib/x86_64-linux-gnu/libarpack.so.2 (0x00007fe9bcbd9000)
 liblapack.so.3 => /usr/lib/x86_64-linux-gnu/liblapack.so.3 (0x00007fe9bc353000)
 libgfortran.so.4 => /usr/lib/x86_64-linux-gnu/libgfortran.so.4 (0x00007fe9bbf74000)
 libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe9bbbd6000)
 libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe9bb7e5000)
 libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe9bb5cd000)
 libmpi.so.20 => /usr/lib/x86_64-linux-gnu/libmpi.so.20 (0x00007fe9bb2db000)
 /lib64/ld-linux-x86-64.so.2 (0x00007fe9bdaa9000)
 libblas.so.3 => /usr/lib/x86_64-linux-gnu/libblas.so.3 (0x00007fe9bb080000)
 libopenblas.so.0 => /usr/lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007fe9b8dda000)
 libquadmath.so.0 => /usr/lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fe9b8b9a000)
 libopen-rte.so.20 => /usr/lib/x86_64-linux-gnu/libopen-rte.so.20 (0x00007fe9b8912000)
 libopen-pal.so.20 => /usr/lib/x86_64-linux-gnu/libopen-pal.so.20 (0x00007fe9b8660000)
 librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fe9b8458000)
 libhwloc.so.5 => /usr/lib/x86_64-linux-gnu/libhwloc.so.5 (0x00007fe9b821b000)
 libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe9b8017000)
 libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fe9b7e14000)
 libnuma.so.1 => /usr/lib/x86_64-linux-gnu/libnuma.so.1 (0x00007fe9b7c09000)
 libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007fe9b79ff000)
```

### Compiler CalculiX 

CalculiX étant une application autonome, vous pouvez installer un fichier binaire empaqueté pour votre distribution ou le compiler vous-même. A partir de la version 2.7.x, CalculiX devrait fonctionner avec FreeCAD. Etant donné que le code n\'a pas beaucoup changé depuis des années, des versions plus basses que la version 2.7.x peuvent également fonctionner.

Compiler CalculiX est une tâche pour des utilisateurs expérimentés, nécessitant la modification des Makefiles et des options de construction de différentes plates-formes. Voir les informations suivantes:

-   Debian: [Debian source package for Calculix](http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&start=10), [Gmsh 4 package available for testing in Community Extras PPA](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p260506), [Compiling CalculiX ccx on fedora, ubuntu and debian](https://forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Fedora 27, 28, 29: [Compiling CalculiX ccx on fedora, ubuntu and debian](https://forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Il existe une version CMake du paquet source dans un [github repository](https://github.com/ricortiz/CalculiX-cmake), mais sur les forums FreeCAD, personne n\'a signalé si ce paquet fonctionnait.

### Compiler Netgen 

Netgen était initialement lié par FreeCAD lorsque FreeCAD a utilisé OCE, le fork de la communauté d\'OpenCascade (OCCT). Alors que OCE accusait un retard de développement par rapport à OCCT, FreeCAD est revenu à OCCT. Cela a rompu la liaison de Netgen, qui ne pouvait se lier qu\'à OCCT 6.9 ou à OCE 0.18 et au-dessous. Les versions OCCT 7.x améliorant la fonctionnalité de base de FreeCAD, il a été décidé de supprimer le support Netgen au profit de Gmsh.

Depuis lors, quelques succès ont été obtenus en corrigeant et en liant les nouvelles versions de Netgen avec OCCT 7.x. Néanmoins, l\'inclusion de Netgen avec FreeCAD reste problématique.


</div>


</div>

## Installation sous Mac OSX 


**Ces informations peuvent être obsolètes. Si vous êtes un utilisateur OSX, veuillez tester et corriger cette section**

Les packages de développement OSX [development packages](https://github.com/FreeCAD/FreeCAD/releases) de FreeCAD peuvent inclure Netgen mais ne peuvent pas inclure CalculiX.

Voir cet article du forum [FEM on Mac OSX](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&p=198652#p198642) pour plus d\'informations sur l\'installation de CalculiX et un [updated post](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p273746) pour des informations plus récentes.

CalculiX :

-   [installer CalculiX avec brew](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p508724)

Les articles suivants peuvent être dépassés :

-   [FEM on Mac OSX, post 1](http://forum.freecadweb.org/viewtopic.php?f=18&t=10979)
-   [MacPorts users: CalculiX port test request](http://forum.freecadweb.org/viewtopic.php?f=8&t=14497)

## Plus d\'informations 

L\'[atelier FEM](FEM_Workbench/fr.md) est en développement constant. Les informations les plus récentes se trouvent sur le [Forum FreeCAD](http://www.forum.freecadweb.org/).

Si vous rencontrez des problèmes pour installer Netgen, Gmsh ou CalculiX, ou un autre outil externe, commencez par rechercher le forum correspondant:

-   [netgen site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=netgen+site:forum.freecadweb.org)
-   [gmsh site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=gmsh+site:forum.freecadweb.org)
-   [calculix site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=calculix+site:forum.freecadweb.org)


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Install/fr
