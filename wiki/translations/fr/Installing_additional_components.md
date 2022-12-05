# Installing additional components/fr
{{TOCright}}

# Introduction

Après avoir installé FreeCAD sur votre système d\'exploitation ([Windows](Installing_on_Windows/fr.md), [Linux](Installing_on_Linux/fr.md) ou [Mac](Installing_on_Mac/fr.md)), vous pouvez envisager d\'installer un ou plusieurs des composants supplémentaires suivants.

# Fichiers d\'aide 

Voir [Installation du fichier d\'aide](Installing_Helpfile/fr.md).

# Ateliers externes 

Outre les [ateliers](Workbenches/fr.md) par défaut fournis avec FreeCAD, il existe un bon nombre collection d\'[ateliers externes](External_workbenches/fr.md) utiles créés par les membres de la communauté.

# Logiciels tiers 

FreeCAD prend en charge plusieurs progiciels tiers prêts à l\'emploi. Dans de nombreux cas, tout ce que vous avez à faire est d\'installer le logiciel et une fois FreeCAD redémarré, il le trouvera automatiquement et pourra l\'utiliser. Cette section vise à fournir une liste de ces logiciels, ainsi que des informations sur leur utilisation dans FreeCAD et sur les sites de téléchargement.

## Assistance

### GitPython

[GitPython](https://github.com/gitpython-developers/GitPython) est une bibliothèque pour interagir avec les référentiels Git. Le [Gestionnaire des extensions](Std_AddonMgr/fr.md) peut utiliser cette bibliothèque. GitPython est inclus dans les programmes d\'installation de FreeCAD pour Windows et Mac.

### GraphViz

[GraphViz](https://www.graphviz.org) est un logiciel de visualisation de graphes open source. Il est utilisé par l\'outil [Std Graphique de dépendance](Std_DependencyGraph/fr.md).

### OpenCAMLib

[OpenCAMLib](http://www.anderswallin.net/CAM) est une bibliothèque open source d\'algorithmes de fabrication assistée par ordinateur (FAO). Il est utilisé dans [atelier Path](Path_Workbench/fr.md). Voir la page [OpenCamLib](OpenCamLib/fr.md) pour les instructions d\'installation.

### OpenSCAD

[OpenSCAD](https://www.openscad.org) est un modeleur 3D solide. L\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md) dépend de ce logiciel et l\'[atelier Mesh](Mesh_Workbench/fr.md) l\'utilise pour ses outils booléens. Il est également nécessaire pour l\'importation de fichiers SCAD avec l\'outil [Std Importer](Std_Import/fr.md).

## Format des fichiers 

Tous les logiciels de cette section seront utilisés par les outils [Std Importer](Std_Import/fr.md) ou [Std Exporter](Std_Export/fr.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) est une application commerciale permettant d\'échanger divers formats de fichiers CAO. Il existe un [atelier externe](https://github.com/yorikvanhavre/CADExchanger) pour utiliser cette application dans FreeCAD.

### Importateur de DXF 

FreeCAD a un importateur et un exportateur natifs pour les fichiers DXF, programmés en C ++. Actuellement, ils n\'implémentent pas toutes les fonctionnalités du format DXF. Pour ces fonctionnalités, l\'importateur et l\'exportateur Python hérités sont toujours disponibles. Ceux-ci nécessitent la bibliothèque Python [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-importer). Voir la page [FreeCAD et importation DXF](FreeCAD_and_DXF_Import/fr.md) pour plus d\'informations.

### Convertisseurs DWG 

FreeCAD ne peut pas lire et écrire directement des fichiers DWG. Pour convertir des fichiers DXF en fichiers DWG, et vice-versa, FreeCAD s\'appuie sur des convertisseurs externes. Il existe un support intégré pour les convertisseurs DWG suivants :

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, manque de support pour certaines entités DWG).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (gratuit, mais pas open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). {{Version/fr|0.20}}

Voir [Préférences d\'Import Export](Import_Export_Preferences/fr#DWG.md) et [FreeCAD et l\'importation DWG](FreeCAD_and_DWG_Import/fr.md) pour plus d\'informations.

### IfcOpenShell

[IfcOpenShell](http://ifcopenshell.org) est une bibliothèque permettant de travailler avec le format de fichier IFC (Industry Foundation Classes) utilisé dans la conception architecturale. La bibliothèque est également utilisée par les outils [Arch IfcExplorer](Arch_IfcExplorer/fr.md) ({{VersionMinus/fr|0.18}}) et [BIM IfcExplorer](BIM_IfcExplorer/fr.md). IfcOpenShell est inclus dans les programmes d\'installation de FreeCAD pour Windows et Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) est une bibliothèque requise pour l\'exportation au format de fichier IFCJSON. IFCJSON est un nouveau format IFC qui n\'est pas encore pris en charge par de beaucoup d\'applications.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), également connu sous le nom de python-collada, est une bibliothèque Python pour lire et écrire des fichiers Collada (DAE). Pycollada est inclus dans les programmes d\'installation de FreeCAD pour Windows et Mac.

## Rendu

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) est un moteur de rendu, un redémarrage du projet [LuxRender](LuxRender/fr.md). Officiellement, il n\'est pas supporté par l\'[atelier Raytracing](Raytracing_Workbench/fr.md) mais cela peut valoir la peine de l\'essayer. Il est officiellement pris en charge par le nouvel [atelier Render](https://github.com/FreeCAD/FreeCAD-render) destiné à remplacer l\'atelier Raytracing. Consultez la page [LuxCoreRender](LuxCoreRender/fr.md) pour plus d\'informations et les instructions d\'installation.

### LuxRender

[LuxRender](https://luxcorerender.org/history/) est l\'un des deux moteurs de rendu supportés par l\'[atelier Raytracing](Raytracing_Workbench.md). En 2013, le projet a été redémarré pour devenir [LuxCoreRender](LuxCoreRender/fr.md) avec une réécriture majeure du code et des changements de compatibilité. Officiellement, l\'atelier Raytracing ne supporte que la version abandonnée de [LuxRender](LuxRender/fr.md). (la dernière version est la 1.6, 2017-12-28), tandis que le nouvel [https://github.com/FreeCAD/FreeCAD-render atelier Render](https://github.com/FreeCAD/FreeCAD-render_atelier_Render.md) (prévu comme un futur remplacement de l\'atelier Raytracing) supporte plutôt LuxCoreRender et a abandonné le support de LuxRender. Quoi qu\'il en soit, même s\'il n\'est pas officiellement supporté, [LuxCoreRender](LuxCoreRender/fr.md) peut fonctionner avec l\'atelier Raytracing, il peut être intéressant de l\'essayer. Voir la page [LuxRender](LuxRender/fr.md) pour plus d\'informations et les instructions d\'installation et la page [LuxCoreRender](LuxCoreRender/fr.md) si vous voulez essayer un logiciel plus moderne.

### POV-Ray 

[POV-Ray](https://www.povray.org) est un traceur de rayons bien connu qui peut rendre des images photoréalistes. Il s\'agit de l\'un des deux moteurs de rendu actuellement pris en charge par l\'[atelier Raytracing](Raytracing_Workbench/fr.md). Voir la page [POV-Ray](POV-Ray/fr.md) pour plus d\'informations et les instructions d\'installation.

## Eléments finis 

### CalculiX

[CalculiX](http://calculix.de) est une suite de deux packages d\'éléments finis: CalculiX CrunchiX, un solveur FEM, et CalculiX GraphiX, une interface graphique. Seul le solveur est pris en charge par FreeCAD. Il est utilisé par l\'outil [FEM Solveur CalculiX experimental](FEM_SolverCalculiX/fr.md).

### Gmsh

[Gmsh](http://gmsh.info) est un générateur automatique de maillage par éléments finis. il est utilisé par les outils [FEM FEM Maillage à partir d\'une forme avec Gmsh](FEM_MeshGmshFromShape/fr.md) et [Mesh Tesselation](Mesh_FromPartShape/fr.md).

### Elmer

[Elmer](https://www.csc.fi/web/elmer) est un logiciel de simulation multi-physique, qui a été ouvert en 2005. Dans FreeCAD, ses modules Grid et Solver sont utilisés par l\'outil [FEM Solveur Elmer](FEM_SolverElmer/fr.md).

### FEniCS

[FEniCS](https://fenicsproject.org) est une plate-forme informatique pour résoudre les équations aux dérivées partielles (Partial Differential Equations = PDE), largement utilisées pour résoudre des problèmes FEM. Il est utilisé par l\'[atelier FEM](FEM_Workbench/fr.md)

### Z88

[Z88](https://en.z88.de) est un autre programme FEM, contenant un mailleur, un solveur et des convertisseurs. Il est utilisé par l\'outil [FEM Solveur Z88](FEM_SolverZ88/fr.md). FreeCAD nécessite le package open source Z88OS.

### OpenFOAM

[OpenFOAM](https://openfoam.org) est une collection de bibliothèques pour les simulations en dynamique des fluides (Computational Fluid Dynamics = CFD). OpenFOAM est utilisé par [atelier Cfd](Cfd_Workbench/fr.md) et [CfdOF](https://github.com/jaheyns/CfdOF) [ateliers externes](external_workbenches/fr.md).

# Pages en relation 

-   [Import Export](Import_Export/fr.md)
-   [Préférences d\'Import Export](Import_Export_Preferences/fr.md)
-   [Bibliothèques tierces](Third_Party_Libraries/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing additional components/fr
