# Developer hub/fr
![150](images/Crystal_Clear_app_tutorials.png )

Vous êtes ici à l\'endroit idéal pour vous documenter, si vous voulez contribuer au développement du logiciel FreeCAD.

Ces pages sont au début de leurs développements. Si vous ne trouvez pas l\'information que vous recherchez, ou vous avez trouvé des informations utiles, et qui ne sont pas liées ici, alors s\'il vous plaît laissez un commentaire sur le [forum de discussion](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) et quelqu\'un s\'en occupera, (ou, pourquoi ne pas modifier vous même directement cette page, ou la documentation de FreeCAD !).

## Documentation pour les développeurs 

La documentation pour les développeurs comprend les sections suivantes :

### Compiler FreeCAD 

-   _
-   [Compiler avec Docker](Compile_on_Docker/fr.md)
-   [Compiler sous Windows](Compile_on_Windows/fr.md)
-   [Compiler sous Linux](Compile_on_Linux/fr.md)
-   [Compiler sous Mac OS](Compile_on_MacOS/fr.md)
-   [Détails de licence](Licence/fr.md) à propos des licences de FreeCAD
-   [Bibliothèques tierces](Third_Party_Libraries/fr.md)
-   [D\'autres outils](Third_Party_Tools/fr.md)
-   [Configuration de démarrage](Start_up_and_Configuration/fr.md)
-   [Documentation du code source](Source_documentation/fr.md)
-   Utilisez le [traqueur de bogue](Tracker/fr.md) lorsque vous avez un problème ou pensez avoir trouvé un bogue

### Empaquetage

Le [Packaging](Packaging.md) consiste à prendre les fichiers binaires compilés et les fichiers sources Python de FreeCAD, puis à les distribuer pour les utiliser dans un système particulier.

-   [Linux packaging](Linux_packaging.md)
    -   [Debian development](Debian_development.md)
    -   [Debian Unstable](Debian_Unstable.md)
    -   [Git buildpackage](Git_buildpackage.md)
-   [Windows packaging](Windows_packaging.md)
-   [MacOS packaging](MacOS_packaging.md)

### Outils de support à la compilation 

-   Les [outils de compilation de FreeCAD](FreeCAD_Build_Tool/fr.md)
    -   [Création d\'atelier](Workbench_creation/fr.md) dans FreeCAD
-   [Débugger](Debugging/fr.md) FreeCAD
-   [Tester](Testing/fr.md) FreeCAD
-   [Compilation (accélération)](Compiling_(Speeding_up)/fr.md) FreeCAD
-   [Intégration continue](Continuous_Integration/fr.md)

### Modifier FreeCAD 

-   Compréhension du [code source de FreeCAD](The_FreeCAD_source_code/fr.md)
-   [Soumettre des patchs](Tracker#Submitting_patches.md)
-   Ajouter des [Fonctionnalités](Gui_Command/fr.md) à FreeCAD ou a un atelier
-   [Image de marque](Branding/fr.md) ou *comment donner un look unique à FreeCAD*
-   [Graphisme](Artwork/fr.md) créé pour FreeCAD, que vous pouvez réutiliser librement
-   [Recommandations pour la charte graphique](Artwork_Guidelines/fr.md), normes pour les icônes
-   [Traduire FreeCAD](Localisation/fr.md)
-   [Modules supplémentaires](Extra_python_modules/fr.md) ou *comment étendre les fonctionnalités de FreeCAD avec Python*
-   [Google Summer of Code](Google_Summer_of_Code.md) participer via les programmes étudiants de Google
-   [Fine-tuning/fr](Fine-tuning/fr.md) affiche différentes options et commutateurs de paramètres permettant de résoudre les problèmes.
-   [Wrapping a C++ class in Python](Wrapping_a_Cplusplus_class_in_Python.md) montre comment créer le wrapper Python d\'une classe C++.

-   [Traduction et ateliers externes](Translating_an_external_workbench/fr.md)

### Le guide du développeur de module 

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) est un livre électronique en cours d\'écriture sur github, veuillez soumettre votre requête pour contribuer.

Chapitres :

-   Vue d\'ensemble et architecture logicielle
-   Structure du code source
-   Modules Base et App
-   Module Gui
-   Encapsulation Python
-   Conception modulaire
-   Analyse du module Fem (mélange C++ et Python)
-   Développement du module CFD (pure Python)
-   Test et débogage de module
-   Contribution au développement avec git

La dernière version pdf peut être téléchargée à partir de [pdf folder](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf) de ce repo git

### Intégration

#### Documentation OpenCascade 

OpenCascade est une plate-forme de développement logiciel pour la modélisation 3D de surfaces et de solides, l\'échange de données CAO et la visualisation, principalement sous la forme de bibliothèques C++.

-   [Tutoriels Roman Lygin\'s](http://opencascade.wikidot.com/romansarticles)
-   [Documentation en ligne complète](https://dev.opencascade.org/doc/overview/html/index.html)
-   [Manuel de référence](https://dev.opencascade.org/doc/refman/html/index.html)
-   [Le wiki openCascade](http://opencascade.wikidot.com) (contiendrait actuellement ?? du spam Chinois\...)

#### Formats de fichiers 

[File Format FCStd](File_Format_FCStd.md). Les fichiers créés avec FreeCAD sont des fichiers `.zip` contenant la géométrie [BREP](https://fr.wikipedia.org/wiki/B-Rep) ainsi que des données XML décrivent le document.

#### Solveur Sketcher 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (fil de discussion), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) dans GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) dans le code source de FreeCAD ; Les fichiers importants sont [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) et [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

Le solveur Sketcher n'est pas parfait, car il existe des problèmes de précision numérique lors de l'utilisation de grandes valeurs. Voir [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

Le développement d\'une nouvelle architecture de solveur pourrait améliorer la façon dont le solveur est utilisé à la fois dans [l\'atelier Sketcher](Sketcher_Workbench/fr.md) et pour l\'assemblage de corps 3D. [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Feuille de route 

FreeCAD, bien qu\'utilisable dans certains domaines, n\'est qu\'au début d\'un long chemin vers le grand public de la CAO. Il y a encore beaucoup à faire pour atteindre un état où nous pourrons rivaliser avec les logiciels commerciaux.

[0.20 Development Cycle](0.20_Development_Cycle.md)

## Communauté

-   [IRC channel](irc://chat.freenode.net/freecad) synchronisé avec [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecadweb.org/viewforum.php?f=6)

-   [Feuille de route du développement](Development_roadmap/fr.md)

## Crédits

[Contributeurs](Contributors/fr.md)




_ _

---
[documentation index](../README.md) > [Hubs](Category_Hubs.md) > Developer hub/fr
