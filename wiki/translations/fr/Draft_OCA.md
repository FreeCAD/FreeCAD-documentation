# Draft OCA/fr
## Description

Draft OCA est un module utilisé par <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Ouvrir](Std_Open/fr.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Importer](Std_Import/fr.md) et <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Exporter](Std_Export/fr.md) pour gérer le [format de fichier OCA](http://groups.google.com/group/open_cad_format).

Le format de fichier OCA est un effort communautaire pour créer un format de fichier CAO gratuit, simple et ouvert. OCA est largement basé sur le format de fichier GCAD généré à partir de [gCAD3D](http://www.gcad3d.org/). Les deux formats peuvent être importés dans FreeCAD et les fichiers OCA exportés par FreeCAD peuvent être ouverts dans gCAD3D.



## Importer

Les objets OCA suivants peuvent être importés :

-   Lignes
-   Arcs et cercles
-   Surfaces fermées



## Exporter

Les objets FreeCAD suivants peuvent être exportés :

-   Lignes et polylignes
-   Arcs et cercles
-   Surfaces



## Préférences

Voir : [Préférences Importer/Exporter](Import_Export_Preferences/fr.md).



## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour exporter des objets au format OCA, utilisez la méthode `export` du module importOCA.


```python
importOCA.export(exportList, filename)
```

-   Pour le système d\'exploitation Windows : utilisez un **/** (barre oblique) comme séparateur de chemin dans {{Incode|filename}}.

Exemple :


```python
import FreeCAD as App
import Draft
import importOCA

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```



---
⏵ [documentation index](../README.md) > [File Formats](Category_File%20Formats.md) > [Draft](Draft_Workbench.md) > Draft OCA/fr
