# <img alt="Icône de l\'atelier externe EM" src=images/EMWorkbench.svg  style="width:64px;"> EM Workbench/fr


{{TOCright}}

## Introduction

L\'atelier EM (ElectroMagnetic) fournit l'interface front-end de CAO à certains solveurs libres et open source. Pour le moment, il prend en charge le solveur d\'impédance magnétoquasistatique 3D [FastHenry](https://www.fastfieldsolvers.com/software.htm#fasthenry2) (c\'est-à-dire l\'extraction d\'inductance et de résistance aux \"basses\" fréquences). La prise en charge du solveur de capacité électrostatique 3D [FasterCap](https://www.fastfieldsolvers.com/software.htm#fastercap) est en cours.

<img alt="" src=images/Screenshot_EM_window.png  style="width:600px;">

## Installation

L\'_. Ceci peut être fait à partir du menu **Outils → Gestionnaire d'Addon**.

Les solveurs électromagnétiques FastHenry2 et FasterCap doivent être installés séparément. Leurs codes binaires ainsi que les sources sont disponibles gratuitement sur [FastFieldSolvers](https://www.fastfieldsolvers.com).

## Utilisation

### FastHenry

FastHenry est un logiciel permettant de calculer les inductances et résistances propres et mutuelles, en fonction de la fréquence, d\'une structure conductrice tridimensionnelle générique, dans l\'approximation magnétoquasistatique. Il peut également générer des modèles de circuits équivalents multifréquences compatibles avec Spice.

La connaissance de FastHenry est une condition préalable à une utilisation efficace de l\'ElectroMagnetic Workbench pour FastHenry. Nous vous suggérons de lire le manuel d\'utilisation du logiciel [FastHenry User\'s manual](https://www.fastfieldsolvers.com/documentation.htm) et de jouer un peu avec les fichiers d\'exemple qui sont fournis avec l\'installation.

### FasterCap

FasterCap est un puissant programme d\'extraction de capacité tri et bidimensionnelle.

La connaissance de FasterCap est une condition préalable à l\'utilisation efficace de l\'atelier ElectroMagnetic pour FasterCap. Nous vous suggérons de lire le [fichier d\'utilisation de FasterCap](https://www.fastfieldsolvers.com/documentation.htm) et de jouer un peu avec les fichiers d\'exemple qui sont fournis avec l\'installation.

## Outils FastHenry 

Voici les outils utilisés pour interagir avec FastHenry:

-   <img alt="" src=images/EM_FHNode.svg  style="width:32px;"> [Noeud FH](EM_FHNode/fr.md): Crée un objet FastHenry de type Noeud.
-   <img alt="" src=images/EM_FHSegment.svg  style="width:32px;"> [Segment FH](EM_FHSegment/fr.md): Crée un objet FastHenry de type Segment.
-   <img alt="" src=images/EM_FHPath.svg  style="width:32px;"> [Chemin FH](EM_FHPath/fr.md): Crée un objet FastHenry de type Chemin.
-   <img alt="" src=images/EM_FHPlane.svg  style="width:32px;"> [Plan FH](EM_FHPlane/fr.md): Crée un objet FastHenry de type Plan conducteur uniforme.
-   <img alt="" src=images/EM_FHPlaneHole.svg  style="width:32px;"> [Trou FH](EM_FHPlaneHole/fr.md): Crée un objet FastHenry de type Trou dans un plan conducteur uniforme.
-   <img alt="" src=images/EM_FHPlaneAddRemoveNodeHole.svg  style="width:32px;"> [Bascule noeud trou FH](EM_FHPlaneAddRemoveNodeHole/fr.md): Ajoute ou supprime un nœud ou un trou de/vers un plan conducteur.
-   <img alt="" src=images/EM_FHEquiv.svg  style="width:32px;"> [Equivalence FH](EM_FHEquiv/fr.md): Crée un objet FastHenry de type Equivalence de noeud.
-   <img alt="" src=images/EM_FHPort.svg  style="width:32px;"> [Port FH](EM_FHPort/fr.md): Crée un objet FastHenry de type Port.
-   <img alt="" src=images/EM_FHSolver.svg  style="width:32px;"> [Solveur FH](EM_FHSolver/fr.md): Crée un objet FastHenry de type Solveur.
-   <img alt="" src=images/EM_FHInputFile.svg  style="width:32px;"> [Fichier entrée FH](EM_FHInputFile/fr.md): Crée un fichier FastHenry d\'entrée.

## Outils FasterCap 

À l'heure actuelle, FasterCap est pris en charge via certaines macros du fichier {{FileName|Export_mesh.py}} disponible dans le [code source de l\'atelier ElectroMagnetic sous GitHub](https://github.com/ediloren/EM-Workbench-for-FreeCAD).

## API

Les outils EM peuvent être utilisés dans [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de l\'API EM.

## Tutoriels

Certains tutoriels vidéo sont disponibles pour les versions bêta de l\'atelier EM:

-   [FreeCAD ElectroMagnetic Workbench tutorial - Getting started](https://www.youtube.com/watch?v=h6Pp-_ovLZM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 1](https://www.youtube.com/watch?v=5pSzPizw4e8)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 2](https://www.youtube.com/watch?v=BeBNtfH25rM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 3](https://www.youtube.com/watch?v=BtgdJOf-ql0)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 1](https://www.youtube.com/watch?v=CRqDuEtbdds)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 2](https://www.youtube.com/watch?v=slsLdLoF2OI)


{{EM Tools navi

}} 

_

---
[documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > EM Workbench/fr
