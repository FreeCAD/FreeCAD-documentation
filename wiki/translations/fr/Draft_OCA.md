








{{TOCright}}

## Description

Draft OCA est un module logiciel utilisé par <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Ouvrir](Std_Open/fr.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Importer](Std_Import.md) et <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Exporter](Std_Export.md) pour gérer le [format de fichier OCA](http://groups.google.com/group/open_cad_format).

Le format de fichier OCA est un effort communautaire pour créer un format de fichier CAO gratuit, simple et ouvert. OCA est largement basé sur le format de fichier GCAD généré à partir de [gCAD3D](http://www.gcad3d.org/). Les deux formats peuvent être importés dans FreeCAD et les fichiers OCA exportés par FreeCAD peuvent être ouverts dans gCAD3D.

## Importer

Les objets OCA suivants peuvent être importés:

-   Lignes
-   Arcs et Cercles
-   Surfaces fermées

## Exporter

Les objets FreeCAD suivants peuvent être exportés:

-   Lignes et fils (polylignes)
-   Arcs et cercles
-   Surfaces

## Préférences

Pour plus d\'informations, voir: [Préférences d\'Import Export](Import_Export_Preferences/fr.md).

## Script


**Voir aussi:**

[Draft API](Draft_API/fr.md) et [FreeCAD Script de Base](FreeCAD_Scripting_Basics/fr.md).

Vous pouvez exporter des éléments vers un fichier OCA en utilisant la fonction suivante : 
```python
importOCA.export(exportList, filename)
```

Exemple : 
```python
import FreeCAD, Draft, importOCA

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(1000, 1000, 0)
p3 = FreeCAD.Vector(2200, 1500, 0)
p4 = FreeCAD.Vector(2500, -100, 0)

obj1 = Draft.makeWire([p1, p2, p3, p4])
obj2 = Draft.makeWire([p1, -2.3*p2, -0.8*p3, -1.8*p4])

objects = [obj1, obj2]

importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```





 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
