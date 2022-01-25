# Third Party Libraries/fr
{{TOCright}}

## Vue d\'ensemble 

Ce sont des bibliothèques que FreeCAD utilise comme dépendances tierces lors de la compilation. Ils sont généralement [bibliothèques liées dynamiquement](https://en.wikipedia.org/wiki/Dynamic_loading) et ont une extension `.so` sous Linux/MacOS et `.dll` sous Windows, et sont accompagnés de leurs fichiers d'en-tête `.h` ou `.hpp` ou similaire. Si une bibliothèque modifiée est nécessaire, ou si une classe wrapper est nécessaire, le code de la bibliothèque modifiée, ou du wrapper, doit faire partie du code source de FreeCAD et être compilé avec ce dernier.

Les dépendances doivent être installées dans le système avant de procéder à la compilation. Voir [Compiler sous Linux](Compile_on_Linux/fr.md), [Compiler sous Windows](Compile_on_Windows/fr.md) et [Compiler sous MacOS](Compile_on_MacOS/fr.md) pour plus d\'informations.

Si voulez compiler en utilisant Windows, pensez à utiliser le [LibPack](#LibPack.md) au lieu d\'essayer d\'installer individuellement des librairies.

## Liens

++++
| Nom de la librairie | Version needed        | Link to get it                                                                |
+=====================+=======================+===============================================================================+
| Python              | \>= 3.6               | <http://www.python.org/>                                                      |
++++
| Boost               | \>= 1.33              | <http://www.boost.org/>                                                       |
++++
| OpenCASCADE         | \>= 7.3               | <http://www.opencascade.org>                                                  |
++++
| Qt                  | \>= 5.4               | <https://www.qt.io/>                                                          |
++++
| Shiboken2           |        | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **comme Qt** |                                                                               |
|                     |                    |                                                                               |
++++
| PySide2             |        | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **comme Qt** |                                                                               |
|                     |                    |                                                                               |
++++
| Coin3D              | \>= 3.x               | <https://github.com/coin3d/coin>                                              |
++++
| SoQt (deprecated)   | \>= 1.2               | <https://github.com/coin3d/soqt>                                              |
++++
| Quarter             | \>= 1.0               | <https://github.com/coin3d/quarter>                                           |
++++
| Pivy                | \>= 0.6.5             | <https://github.com/coin3d/pivy/>                                             |
++++
| FreeType            | \>= XXX               | XXX                                                                           |
++++
| PyCXX               | \>= XXX               | XXX                                                                           |
++++
| KDL                 | \>= XXX               | XXX                                                                           |
++++
| Point Cloud Library | \>= XXX               | XXX                                                                           |
++++
| Salome SMESH        | \>= XXX               | XXX                                                                           |
++++
| VTK                 | \>= 6.0               | XXX                                                                           |
++++
| Ply                 | \>= 3.11              | <https://www.dabeaz.com/ply/>                                                 |
++++
| Xerces-C++          | \>= 3.0               | <https://xerces.apache.org/xerces-c/>                                         |
++++
| Eigen3              | \>= 3.0               | <http://eigen.tuxfamily.org/index.php?title=Main_Page>                        |
++++
| Zipios++            | \>= 0.1.5             | <https://snapwebsites.org/project/zipios>, <https://github.com/Zipios/Zipios> |
++++
| Zlib                | \>= 1.0               | <http://www.zlib.net/>, <https://github.com/madler/zlib>                      |
++++
| libarea             | \>= 0.0.20140514-1    | <https://github.com/danielfalck/libarea>                                      |
++++
|                     |                       |                                                                               |
++++

## Details

### Python

**Version :** 3.3 ou plus

**Licence :** Python 3.3 licence


**Python 2 est devenu obsolète en 2019. Le développement ultérieur de FreeCAD utilisera exclusivement Python 3 ; la compatibilité avec Python 2 ne sera pas testée. Par conséquent, les anciens ateliers et macros utilisant cette version devront être mis à jour ou risquent de ne plus fonctionner. Veuillez poster sur le [https://forum.freecadweb.org/ Forum FreeCAD] si vous rencontrez des problèmes avec Python 3.**

Python est un langage de script polyvalent populaire largement utilisé sous Linux et dans les logiciels open source. Dans FreeCAD, Python est utilisé de différentes manières lors de la compilation et lors de l\'exécution. C\'est utilisé

-   écrire des scripts de test pour tester différentes conditions, telles que des fuites de mémoire, afin de garantir la fonctionnalité du logiciel après les modifications, pour les vérifications après la construction et les tests de couverture,
-   pour écrire [macros](macros/fr.md) et l\'enregistrement de macros,
-   implémenter la logique d\'application pour les packages standard,
-   pour implémenter des outils auxiliaires tels que le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md),
-   mettre en place des ateliers complets comme [Draft](Draft_Workbench/fr.md) et [Arch](Arch_Workbench/fr.md),
-   charger dynamiquement des paquets,
-   mettre en place des règles de conception (des connaissances en ingénierie),
-   faire des interactions Internet fantaisistes comme des groupes de travail et PDM

Sous Linux, Python est généralement déjà installé dans votre distribution. Pour Windows, vous pouvez utiliser le source ou le binaire pré compilées de [Python.org](http://www.python.org/) ou utiliser [ActiveState Python](http://www.activestate.com/) bien qu'il soit un peu difficile d'obtenir les bibliothèques de débogage de ce dernier.

Python a été choisi comme langage de script pour FreeCAD pour différentes raisons:

-   Il est plus orienté objet que Perl et Tcl.
-   Le code est plus lisible que Perl et Visual Basic.
-   Il est plus facile d\'intégrer une autre application, contrairement à Java.

En résumé, Python est bien documenté et il est facile à intégrer et à étendre dans une application C++. Il est également bien testé et bénéficie du soutien de la communauté open source. Pour en savoir plus sur Python et parcourir la documentation officielle voyez à l\'adresse [Python.org](http://www.python.org).

### Boost

**Version :** 1.33 ou plus

**License :** Boost Software License - Version 1.0

Les bibliothèques Boost C++ sont des collections de bibliothèques open source révisées par des pairs qui étendent les fonctionnalités de C++. Elles sont destinés à être largement utilisées dans un grand nombre d\'applications et à bien fonctionner avec la bibliothèque standard C++. La licence Boost est conçue pour encourager son utilisation dans les projets open source et sources propriétaires.

En raison de leur popularité et de leur stabilité, de nombreuses bibliothèques Boost ont été acceptées pour être incorporées dans la norme C++11 et d'autres sont prévues pour être intégrées dans les normes C++ suivantes.

Afin d\'assurer l\'efficacité et la flexibilité, Boost fait un usage intensif de modèles (templates). Boost a été une source de travail, et, de recherches approfondies dans la programmation générique, et, méta-données en C++. Vous en saurez plus sur Boost en visitant la page [Boost homepage](http://www.boost.org/).

### OpenCasCade Technologie 

**Version :** 6.7 ou plus

**Licence :** version 6.7.0 et les versions ultérieures sont régies par [GNU Lesser General Public License (LGPL) version 2.1 with additional exception](https://www.opencascade.com/content/licensing). Les versions antérieures utilisent une licence légèrement différente : [Open CASCADE Technology Public License](https://www.opencascade.com/content/occt-public-license).

La technologie OpenCASCADE (OCCT) est un noyau CAO complet de qualité professionnelle. Il a été développé en 1993 et s\'appelait à l\'origine CAS.CADE par Matra Datavision en France pour les applications Strim (Styler) et Euclid Quantum. En 1999, il a été publié en tant que logiciel open source, et depuis lors, il s\'appelle OpenCASCADE.

**[OCC](http://www.opencascade.org/)** est un noyau complet **CAD**. A l\'origine, il a été développé en France par **Matra Datavision**, pour la **Strim (Styler)** et **Euclide applications quantiques**, et, plus tard fait pour l\'Open Source. C\'est une bibliothèque vraiment énorme, et, faire en premier lieu une application de CAO libre est possible, en fournissant certains paquets, qui seraient difficiles, ou impossibles à mettre en œuvre dans un projet Open Source :

-   Un noyau géométrique complet conforme à **STEP**.
-   Un modèle topologique de données et toutes les fonctions nécessaires pour travailler sur les (coupes, fusion, extrusion, etc \...)
-   Import-standard/exportation des processeurs comme [STEP](http://fr.wikipedia.org/wiki/STEP-NC), [IGES](http://fr.wikipedia.org/wiki/Initial_Graphics_Exchange_Specification), [VRML](http://fr.wikipedia.org/wiki/Virtual_Reality_Markup_Language).
-   Visionneuse 2D et 3D avec le soutien de la sélection.
-   Une structure de document, et, données de projet, avec le soutien de, sauvegarde et restauration, de liaison externe des documents, de recalcul de l\'historique du dessin (modélisation paramétrique) et d\'un centre de chargement de nouveaux types de données, comme un module d\'extension dynamique.

Il existe deux versions principales d\'OpenCASCADE dans différentes distributions Linux. L\'un est distribué par les développeurs d\'origine ; il est appelé OCCT et est regroupé sous les noms `occ` ou `occt`. L\'autre version est \"l\'édition communautaire\", en abrégé OCE, et se trouve normalement sous le nom `oce`. FreeCAD peut être compilé avec l\'une ou l\'autre version, cependant, depuis 2016, FreeCAD recommande de compiler avec les bibliothèques officielles de l\'OCCT plutôt que celles de l\'OCE. La raison en est que l\'édition de la communauté manque d\'importantes corrections de bogues et de fonctions qui améliorent l\'utilisation de FreeCAD.

Pour en savoir plus sur OpenCascade visitez la page [OpenCASCADE website](http://www.opencascade.org).

### Qt

**Version :** 4.1 ou plus

**Licence** : GPL v2.0/v3.0 ou commerciale ; (à partir de la version 4.5 aussi sur v2.1 LPGL).

Qt est l\'une des boîtes à outils d\'interface graphique (GUI) les plus populaires disponibles dans le monde open source. FreeCAD utilise cette boîte à outils pour dessiner l\'interface du programme. Pour cela, l\'application Qt Designer est très utile, car elle permet aux développeurs de dessiner rapidement les boîtes de dialogue et les fenêtres, de les exporter sous forme de fichiers de ressources XML, puis de charger ces interfaces au moment de l\'exécution.

Vous trouverez de plus amples informations sur la librairie Qt et une très bonne documentation en ligne sur la documentation [Qt](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 

Shiboken est le générateur de liaison Python utilisé par Qt pour créer le module PySide pour être utilisé par Python. En d\'autres termes, c\'est le système utilisé pour exposer l\'API Qt C++ au langage Python.

Les paquets originaux Shiboken et PySide devaient être utilisés avec Python 2 et Qt4 ; étant donné que ces deux versions sont considérées obsolètes en 2019, veuillez utiliser Shiboken2 et PySide2, qui fonctionnent avec Python 3 et Qt5. Les nouveaux développements de FreeCAD sont réalisés avec Python 3 et Qt5. Par conséquent, la compatibilité avec Python 2 et Qt4 n'est plus garantie après FreeCAD 0.18.

Pour en savoir plus sur Shiboken et Pyside voyez sur la page [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).

### Coin3D

**Version :** 3.0 ou plus

**License :** BSD 3-clause license

Coin3D est une bibliothèque graphique 3D de haut niveau avec une interface de programmation d\'applications C++. Il utilise des structures de données scenegraph pour rendre les graphiques en temps réel adaptés à tout type d\'applications de visualisation scientifique et technique.

Coin3D est basé sur la bibliothèque de rendu en mode immédiat OpenGL, standard du secteur, et ajoute des abstractions pour les primitives de niveau supérieur, fournit une interactivité 3D et contient de nombreuses fonctionnalités d\'optimisation complexes pour le rendu rapide, transparentes pour le programmeur d\'application.

Coin3D est compatible avec l\'API Open Inventor 2.1 de SGI. Cette API est devenue l\'interface graphique standard de facto pour la visualisation 3D dans la communauté scientifique et technique. Il a fait ses preuves depuis l\'an 2000 en tant que pierre angulaire de milliers d\'applications d\'ingénierie dans le monde.

Coin3D (Open Inventor) est utilisé comme visualiseur 3D dans FreeCAD car le visualiseur OpenCASCADE (AIS et Graphics3D) présente des limitations et des goulots d\'étranglement en termes de performances, notamment avec le rendu technique à grande échelle ; d\'autres éléments tels que les textures ou le rendu volumétrique ne sont pas entièrement pris en charge par le visualiseur OpenCASCADE.

Coin3D est portable sur une large gamme de plates-formes : systèmes d\'exploitation UNIX, Linux, BSD, MacOS X et Microsoft Windows. Pour en savoir plus sur cette bibliothèque, visitez [Coin3D homepage](https://github.com/coin3d/coin).

#### SoQt (déprécié) 

**Version :** 1.2.0 ou plus

**License :** BSD 3-clause license

SoQt est la liaison Coin3D (Open Inventor) à la boîte à outils de l\'interface graphique Qt.

SoQt n\'est plus utilisé dans FreeCAD, il a été remplacé par Quarter, une liaison Qt plus récente.

#### Quarter

**Version :** 1.0 ou plus

**License :** BSD 3-clause license

Quarter est une nouvelle liaison Coin3D à la boîte à outils Qt. Une version de celle-ci est incluse dans le code source de FreeCAD, elle est donc compilée avec elle.

#### Pivy

**Version :** 0.6.3 or higher

**License :** BSD 3-clause license

[Pivy](Pivy/fr.md) est une bibliothèque qui enveloppe la bibliothèque Coin3d pour une utilisation dans [Python](Python/fr.md). Il n\'est pas nécessaire de construire FreeCAD ou de le démarrer, mais il est nécessaire en tant que dépendance d\'exécution par [Draft Workbench](Draft_Workbench/fr.md), et par d\'autres établis qui l\'utilisent en interne, comme [Arch](Arch_Workbench/fr.md) et [BIM](BIM_Workbench/fr.md).

Si vous n\'utilisez pas ces établis, vous n\'aurez pas besoin de Pivy.

### Ply

**Version :** 3.11 ou plus

**License :** BSD 3-clause licence

Ply est l\'analyseur Python-Lex-Yacc. Il est utilisé comme dépendance d\'exécution par le [OpenSCAD Workbench](OpenSCAD_Workbench/fr.md). Si vous n\'utilisez pas cet établi, vous n\'aurez peut-être pas besoin de ce package.

Pour plus d\'informations, voir [Ply homepage](https://www.dabeaz.com/ply/)

### Xerces-C++ 

**Version :** 3.0 ou plus

**License :** Apache Software License Version 2.0

Xerces-C++ est un analyseur XML de validation écrit dans un sous-ensemble portable de C++. Xerces-C++ facilite la possibilité pour votre application de lire et d'écrire des données XML. Une bibliothèque partagée est fournie pour analyser, générer, manipuler et valider des documents XML. Xerces-C++ est fidèle à la recommandation XML 1.0 et aux normes associées.

L\'analyseur est utilisé pour enregistrer et restaurer les paramètres dans FreeCAD. Pour plus d\'informations, voir [Xerces-C++ homepage](https://xerces.apache.org/xerces-c/).

### Eigen3

**Version :** 3.0 or higher

**Licence :** À partir de la version 3.1.1, il est sous licence [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Les versions précédentes étaient concédées sous la licence [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen est une bibliothèque de modèles C++ pour l'algèbre linéaire: matrices, vecteurs, solveurs numériques et algorithmes associés.

Si vous souhaitez simplement utiliser Eigen, vous pouvez utiliser les fichiers d'en-tête immédiatement. Il n\'y a pas de bibliothèque binaire à lier, ni de fichier d\'en-tête configuré. Eigen est une bibliothèque de modèles pure définie dans les en-têtes.

Eigen est utilisé dans FreeCAD pour de nombreuses opérations vectorielles dans l\'espace 3D. Pour en savoir plus, visitez [Eigen homepage](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Version :** 0.1.5 ou plus

**License :** GNU Lesser General Public License 2.1

Zipios++ est une bibliothèque C++ pour la lecture et l'écriture de fichiers `.zip`. L\'accès aux entrées individuelles est fourni via iostream C++ standard. Un système de fichiers virtuel simple en lecture seule qui monte des répertoires normaux et des fichiers `.zip` est également fourni. La structure et l\'interface publique de Zipios ++ sont basées sur le paquet `java.util.zip` de Java.

Le format de fichier natif de FreeCAD `.FCstd` est en réalité un fichier `.zip` qui stocke et compresse d\'autres types de données qu\'il contient, tels que les fichiers BREP et XML. Par conséquent, Zipios++ est utilisé pour enregistrer et ouvrir des archives compressées, y compris des fichiers FreeCAD.

Une copie de Zipios++ est incluse dans le code source de FreeCAD et est donc compilée avec celui-ci. Si vous souhaitez utiliser une bibliothèque Zipios++ externe, fournie par votre système d\'exploitation, vous pouvez définir -DFREECAD_USE_EXTERNAL_ZIPIOS = ON avec `cmake`.

Zipios++ utilise la bibliothèque Zlib pour effectuer la décompression réelle des fichiers.

#### Zlib

**Version :** 1.0 ou plus

**License :** zlib licence

Zlib est conçu pour être une bibliothèque de compression de données gratuite, polyvalente et sans perte, utilisable sur tout matériel informatique et système d\'exploitation. Il implémente l\'algorithme de compression `DEFLATE` couramment utilisé dans les fichiers `.zip` et `.gzip`.

Une copie de cette bibliothèque est incluse dans le code source de FreeCAD, elle est donc compilée avec elle.

### libarea

**Version :** 0.0.20140514-1 ou plus

**Licence :** BSD 3-clause license

Libarea est une bibliothèque de logiciels permettant de calculer les opérations de profil et de poche utilisées dans les logiciels de fabrication assistée par ordinateur (FAO). Il a été créé par Dan Heeks pour son projet HeeksCNC.

Une copie de la bibliothèque est incluse avec le code source de l\'atelier [Path](Path_Workbench/fr.md). Elle est donc compilée avec celle-ci.

## LibPack

LibPack est un paquet pratique qui regroupe les dépendances de construction de FreeCAD. Cela n\'est nécessaire que si vous compilez FreeCAD sous Windows avec Visual Studio 2015 et versions ultérieures. Vous pouvez trouver le dernier LibPack sur la page [releases page](https://github.com/FreeCAD/FreeCAD/releases).

Si vous travaillez sous Linux, vous n'avez pas besoin de LibPack, car vous pouvez obtenir les dépendances dans les dépôts de votre distribution, comme indiqué à la page [Compiler sous Linux](Compile_on_Linux/fr.md).

### FreeCAD 12.1.2 

Voir l\'annonce dans le forum : [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

Cela inclut entre autres : Boost 1,67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salomé, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2 11



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/fr
