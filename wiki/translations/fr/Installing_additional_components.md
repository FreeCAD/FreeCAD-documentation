# Installing additional components/fr
{{TOCright}}

# Introduction

Après avoir installé FreeCAD sur votre système d\'exploitation ([Windows](Installing_on_Windows/fr.md), [Linux](Installing_on_Linux/fr.md) ou [Mac](Installing_on_Mac/fr.md)), vous pouvez envisager d\'installer un ou plusieurs des composants supplémentaires suivants.

# Fichiers d\'aide 

La documentation hors ligne n\'est pas fournie avec tous les programmes d\'installation mais elle est disponible sous forme de package distinct. Consultez la page [Installation du fichier d\'aide](Installing_Helpfile/fr.md) pour plus d\'informations.

# Ateliers externes 

Outre les [ateliers](Workbenches/fr.md) par défaut fournis avec FreeCAD, il existe un bon nombre collection d\'[ateliers externes](External_workbenches/fr.md) utiles créés par les membres de la communauté.

# Logiciels tiers 

FreeCAD prend en charge plusieurs progiciels tiers prêts à l\'emploi. Dans de nombreux cas, tout ce que vous avez à faire est d\'installer le logiciel et une fois FreeCAD redémarré, il le trouvera automatiquement et pourra l\'utiliser. Cette section vise à fournir une liste de ces logiciels, ainsi que des informations sur leur utilisation dans FreeCAD et sur les sites de téléchargement.

## Assistance

### GitPython

_ peut utiliser cette bibliothèque. GitPython est inclus dans les programmes d\'installation de FreeCAD pour Windows et Mac.

### GraphViz

_.

### OpenCAMLib

_. Voir la page [OpenCamLib](OpenCamLib/fr.md) pour les instructions d\'installation.

### OpenSCAD

_ dépend de ce logiciel et l\'[atelier Mesh](Mesh_Workbench/fr.md) l\'utilise pour ses outils booléens. Il est également nécessaire pour l\'importation de fichiers SCAD avec l\'outil [Std Importer](Std_Import/fr.md).

## Format des fichiers 

Tous les logiciels de cette section seront utilisés par les outils [Std Importer](Std_Import/fr.md) ou [Std Exporter](Std_Export/fr.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) est une application commerciale permettant d\'échanger divers formats de fichiers CAO. Il existe un [atelier externe](https://github.com/yorikvanhavre/CADExchanger) pour utiliser cette application dans FreeCAD.

### Importateur de DXF 

FreeCAD a un importateur et un exportateur natifs pour les fichiers DXF, programmés en C ++. Actuellement, ils n\'implémentent pas toutes les fonctionnalités du format DXF. Pour ces fonctionnalités, l\'importateur et l\'exportateur Python hérités sont toujours disponibles. Ceux-ci nécessitent la bibliothèque Python _ pour plus d\'informations.

### Convertisseurs DWG 

FreeCAD ne peut pas lire et écrire directement des fichiers DWG. Pour convertir des fichiers DXF en fichiers DWG, et vice-versa, FreeCAD s\'appuie sur des convertisseurs externes. Il existe un support intégré pour les convertisseurs DWG suivants :

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, manque de support pour certaines entités DWG).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (gratuit, mais pas open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). {{Version/fr|0.20}}

Voir [Préférences d\'Import Export](Import_Export_Preferences/fr#DWG.md) et [FreeCAD et l\'importation DWG](FreeCAD_and_DWG_Import/fr.md) pour plus d\'informations.

### IfcOpenShell

_ ({{VersionMinus/fr|0.18}}) et [BIM IfcExplorer](BIM_IfcExplorer/fr.md). IfcOpenShell est inclus dans les programmes d\'installation de FreeCAD pour Windows et Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) est une bibliothèque requise pour l\'exportation au format de fichier IFCJSON. IFCJSON est un nouveau format IFC qui n\'est pas encore pris en charge par de beaucoup d\'applications.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), également connu sous le nom de python-collada, est une bibliothèque Python pour lire et écrire des fichiers Collada (DAE). Pycollada est inclus dans les programmes d\'installation de FreeCAD pour Windows et Mac.

## Rendu

### LuxCoreRender

_. Officiellement, il n\'est pas supporté par l\'_ pour plus d\'informations et les instructions d\'installation.

### LuxRender

_. En 2013, le projet a été redémarré pour devenir _ (prévu comme un futur remplacement de l\'atelier Raytracing) supporte plutôt LuxCoreRender et a abandonné le support de LuxRender. Quoi qu\'il en soit, même s\'il n\'est pas officiellement supporté, [LuxCoreRender](LuxCoreRender/fr.md) peut fonctionner avec l\'atelier Raytracing, il peut être intéressant de l\'essayer. Voir la page [LuxRender](LuxRender/fr.md) pour plus d\'informations et les instructions d\'installation et la page [LuxCoreRender](LuxCoreRender/fr.md) si vous voulez essayer un logiciel plus moderne.

### POV-Ray 

_. Voir la page [POV-Ray](POV-Ray/fr.md) pour plus d\'informations et les instructions d\'installation.

## Eléments finis 

### CalculiX

_.

### Gmsh

_ et [Mesh Tesselation](Mesh_FromPartShape/fr.md).

### Elmer

_.

### FEniCS

_

### Z88

_. FreeCAD nécessite le package open source Z88OS.

### OpenFOAM

_ et _.

# Pages en relation 

-   [Import Export](Import_Export/fr.md)
-   [Préférences d\'Import Export](Import_Export_Preferences/fr.md)
-   [Bibliothèques tierces](Third_Party_Libraries/fr.md)




_

---
[documentation index](../README.md) > Installing additional components/fr
