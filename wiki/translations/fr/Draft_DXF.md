# Draft DXF/fr










{{TOCright}}

## Description

Draft DXF est un module logiciel utilisé par <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Ouvrir](Std_Open/fr.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Importer](Std_Import/fr.md) et <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Exporter](Std_Export/fr.md) pour gérer le format de fichier DXF.

![](images/Screenshot_qcad.jpg ) *Qcad plan exporté en DXF qui est ensuite ouvert dans FreeCAD*

## Importation

L\'importateur a deux modes, réglables sous **Édition → Préférences → Import/Export → DXF** : l\'un est intégré, basé sur C++ et rapide, l\'autre est hérité, codé en Python, plus lent et nécessite l\'installation d\'un module complémentaire, mais peut parfois mieux gérer certaines entités et créer des objets FreeCAD plus raffinés. Les deux prennent en charge toutes les versions DXF à partir de R12.

Les objets 3D à l\'intérieur d\'un fichier DXF sont stockés sous un blob binaire ACIS/SAT, qui ne peut actuellement pas être lu par FreeCAD. Les entités plus simples comme les 3DFACE, cependant, sont prises en charge.

Les objets DXF suivants peuvent être importés :

-   lignes
-   polylignes et (lwpolylignes)
-   cercles
-   arcs
-   splines
-   ellipse
-   calques
-   textes and Mtextes (textes multi-lignes)
-   dimensions
-   blocs (géométrie seulement. Les textes, dimensions et attributs à l\'intérieur des blocs seront ignorés)
-   points
-   repères (flêchés)
-   objets spatiaux en papier

## Exportation

Les fichiers sont exportés au format R14 DXF qui peut être géré par de nombreuses applications.

Les objets FreeCAD suivants peuvent être exportés :

-   toute la géométrie 2D de FreeCAD telle que les objets Draft ou les esquisses
-   des objets 3D sont exportés sous forme de vue 2D aplatie
-   des objets composés sont exportés sous forme de blocs
-   des textes
-   Les couleurs sont mappées des couleurs RVB des objets à l\'index de couleurs Autocad (ACI). Le noir sera toujours \"par couche\"
-   les calques sont mappés à partir des noms de groupe. Lorsque des groupes sont imbriqués, le groupe le plus profond donne le nom de la couche.
-   dimensions, qui sont exportées avec un style \"standard\".

## Installation

Pour des raisons de licence, les bibliothèques d\'importation/exportation [DXF](DXF/fr.md) requises par la version héritée de l\'importateur ne font pas partie du code source de FreeCAD. Pour plus d\'informations, voir : [FreeCAD et l\'importation de DXF](FreeCAD_and_DXF_Import/fr.md).

## Préférences

Pour plus d\'informations, voir : [Préférences d\'Import Export](Import_Export_Preferences/fr.md).

## Script


**Voir aussi :**

[Draft API](Draft_API/fr.md) et [FreeCAD Scripts de base](FreeCAD_Scripting_Basics/fr.md).

Vous pouvez exporter des éléments vers un fichier DXF en utilisant la fonction suivante : 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Exemple : 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```





 

[Category:File Formats](Category:File_Formats.md)
