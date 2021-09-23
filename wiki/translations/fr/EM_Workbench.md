# EM Workbench/fr
 <img alt="" src=images/EMWorkbench.svg  style="width:240px;"> 
*align=center|Icône atelier externe FreeCAD Electromagnétique*

## Introduction


{{TOCright}}

L\'atelier ElectroMagnetic (EM) fournit l'interface front-end de CAO à certains solveurs libres et open source. Actuellement, il prend en charge le résolveur d\'impédance magnétoquasistatique 3D [FastHenry](https://www.fastfieldsolvers.com/software.htm#fasthenry2) (c\'est-à-dire l\'extraction d\'inductance et de résistance à des \"basses\" fréquences). La prise en charge du résolveur de capacité électrostatique 3D [FasterCap](https://www.fastfieldsolvers.com/software.htm#fastercap) est en cours.

<img alt="" src=images/Screenshot_EM_window.png  style="width:600px;">

## Installation

L\'atelier [EM](EM_Workbench/fr.md) est un [Addon FreeCAD](External_workbenches/fr.md) qui peut être installé avec <img alt="" src=images/AddonManager.svg  style="width:24px;"> [AddonManager](AddonManager/fr.md). ceci peut être fait à partir de 
**Outils → Addon Manager**

Les solveurs électromagnétiques FastHenry2 et FasterCap doivent être installés séparément. Leurs codes binaires ainsi que les sources sont disponibles gratuitement sur [FastFieldSolvers](https://www.fastfieldsolvers.com).

## Utilisation

### FastHenry

FastHenry est un logiciel de calcul du self dépendant de la fréquence et des inductances et résistances mutuelles d\'une structure conductrice tridimensionnelle générique, dans l\'approximation magnétoquasistatique. Il peut également générer des modèles de circuit équivalent à fréquences multiples compatibles Spice.

La connaissance de FastHenry est une condition préalable à l'utilisation efficace de l'atelier ElectroMagnetic pour FastHenry. Nous vous suggérons de lire le [FastHenry User\'s Manual](https://www.fastfieldsolvers.com/documentation.htm) d\'origine et de lire un peu les exemples de fichiers fournis avec l\'installation.

### FasterCap

FasterCap est un puissant programme d\'extraction de capacités en trois et deux dimensions.

La connaissance de FasterCap est une condition préalable à l\'utilisation efficace de l\'ElectroMagnetic Workbench for FasterCap. Nous vous suggérons de lire le fichier [FasterCap original](https://www.fastfieldsolvers.com/documentation.htm) et de lire un peu les exemples de fichiers fournis avec l\'installation.

## FastHenry Tools 

Voici les outils utilisés pour interagir avec FastHenry:

-   <img alt="" src=images/EM_FHNode.svg  style="width:32px;"> [FHNode](EM_FHNode/fr.md): Crée un objet FastHenry Node
-   <img alt="" src=images/EM_FHSegment.svg  style="width:32px;"> [FHSegment](EM_FHSegment/fr.md): Crée un objet FastHenry Segment
-   <img alt="" src=images/EM_FHPath.svg  style="width:32px;"> [FHPath](EM_FHPath/fr.md): Crée un objet FastHenry Path
-   <img alt="" src=images/EM_FHPlane.svg  style="width:32px;"> [FHPlane](EM_FHPlane/fr.md): Crée un objet plat conducteur uniforme FastHenry
-   <img alt="" src=images/EM_FHPlaneHole.svg  style="width:32px;"> [FHPlaneHole](EM_FHPlaneHole/fr.md): Crée un objet Trou uniforme uniforme de FastHenry
-   <img alt="" src=images/EM_FHPlaneAddRemoveNodeHole.svg  style="width:32px;"> [FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md): Ajouter ou supprimer un nœud ou un trou de/vers un plan conducteur
-   <img alt="" src=images/EM_FHEquiv.svg  style="width:32px;"> [FHEquiv](EM_FHEquiv/fr.md): Crée un objet d\'équivalence de noeud FastHenry
-   <img alt="" src=images/EM_FHPort.svg  style="width:32px;"> [FHPort](EM_FHPort/fr.md): Crée un objet FastHenry Port
-   <img alt="" src=images/EM_FHSolver.svg  style="width:32px;"> [FHSolver](EM_FHSolver/fr.md): Crée un objet FastHenry Solver
-   <img alt="" src=images/EM_FHInputFile.svg  style="width:32px;"> [FHInputFIle](EM_FHInputFile/fr.md): Crée un fichier d\'entrée FastHenry

## Outils FasterCap 

À l'heure actuelle, FasterCap est pris en charge via certaines macros du fichier {{FileName|Export_mesh.py}} disponible dans le [code source d'ElectroMagnetic Workbench GitHub](https://github.com/ediloren/EM-Workbench-for-FreeCAD).

## API

Les outils EM peuvent être utilisés dans [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de l\'API EM.

## Tutoriels

Certains tutoriels vidéo sont disponibles pour les versions bêta de l\'atelier EM:

-   [FreeCAD ElectroMagnetic Workbench tutorial - Getting started](https://www.youtube.com/watch?v=h6Pp-_ovLZM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 1](https://www.youtube.com/watch?v=5pSzPizw4e8)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 2](https://www.youtube.com/watch?v=BeBNtfH25rM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 3](https://www.youtube.com/watch?v=BtgdJOf-ql0)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 1](https://www.youtube.com/watch?v=CRqDuEtbdds)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 2](https://www.youtube.com/watch?v=slsLdLoF2OI)

## Ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), il y a beaucoup de gens qui développent des établis supplémentaires en dehors des développeurs principaux de FreeCAD.

La page [ateliers externes](External_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux, et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables. depuis FreeCAD.

De nouveaux ateliers sont en développement, restez à l\'écoute!


{{EM Tools navi

}}  

[Category:External Workbenches](Category:External_Workbenches.md)
