# Draft DXF/fr
{{TOCright}}

## Description

Draft DXF est un module logiciel utilisé par <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ et <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Exporter](Std_Export/fr.md) pour gérer le format de fichier DXF.

![](images/Screenshot_qcad.jpg ) *Qcad plan exporté en DXF qui est ensuite ouvert dans FreeCAD*

## Importation

Deux importateurs sont disponibles, celui qui est utilisé peut être spécifié sous **Édition → Préférences... → Importer-Exporter → DXF**. L\'un est intégré, basé sur C++ et rapide, l\'autre est hérité, codé en Python, plus lent et nécessite l\'installation d\'un module complémentaire, mais peut mieux gérer certaines entités et créer des objets FreeCAD plus raffinés. Les deux prennent en charge toutes les versions DXF à partir de R12.

Les solides 3D à l\'intérieur d\'un fichier DXF sont stockés sous un blob binaire ACIS/SAT, qui ne peut actuellement pas être lu par FreeCAD.

### L\'importateur C++ 

Cet importateur peut importer les objets DXF suivants :

-   lignes
-   polylignes (et lwpolylines)
-   arcs
-   cercles
-   ellipses
-   splines
-   points
-   textes et mtextes
-   dimensions
-   chefs
-   blocs (seuls la géométrie, les textes, les dimensions et les attributs à l\'intérieur des blocs sont ignorés)
-   calques
-   objets de l\'espace papier

### L\'importateur historique 

Cet importateur peut importer les objets DXF suivants :

-   lignes
-   polylignes (et lwpolylines)
-   arcs
-   cercles
-   ellipses
-   splines
-   Visages 3D
-   textes et mtextes
-   leaders
-   calques

## Exportation

Il existe également deux exportateurs. L\'exportateur traditionnel exporte au format R12 DXF, l\'exportateur C++ au format R14 DXF. Les deux formats peuvent être traités par de nombreuses applications.

### L\'exportateur C++ 

Voici quelques-unes des caractéristiques et des limites de cet exportateur :

-   Toute la géométrie 2D de FreeCAD est exportée, sauf [Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md), [Draft Courbe de Bézier](Draft_BezCurve/fr.md) et [Draft Points](Draft_Point/fr.md).
-   Les arêtes droites des faces des objets 3D sont exportées, mais les arêtes courbes uniquement si elles se trouvent sur un plan parallèle au plan XY du système de coordonnées global. Notez qu\'un DXF créé à partir d\'objets 3D contiendra des lignes dupliquées.
-   Les textes et les dimensions ne sont pas exportés.
-   Les couleurs sont ignorées.
-   Les calques sont mappés à partir des noms d\'objets.

### L\'exportateur historique 

Voici quelques-unes des caractéristiques et des limites de cet exportateur :

-   Toute la géométrie 2D de FreeCAD est exportée, sauf [Draft Points](Draft_Point/fr.md), mais les ellipses, les B-splines et les courbes de Bézier ne sont pas exportées correctement.
-   Les objets 3D sont exportés sous forme de vues 2D aplaties.
-   Les objets composés sont exportés sous forme de blocs.
-   Les textes et les dimensions sont exportés.
-   Les couleurs dans le DXF sont basées sur la couleur des lignes des objets. Le noir est mappé sur \"ByBlock\", les autres couleurs sont mappées en utilisant les couleurs ACI (AutoCAD Color Index).
-   Les calques sont mappées à partir des noms de calques et de groupes. Lorsque les groupes sont imbriqués, le groupe le plus profond donne le nom du calque.

## Installation

Pour des raisons de licence, les bibliothèques d\'importation/exportation _.

## Préférences

Voir : [Préférences d\'Import Export](Import_Export_Preferences/fr.md).

## Script

Voir aussi: _.

Pour exporter des objets au format DXF, utilisez la méthode `export` du module importDXF.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   Pour le système d\'exploitation Windows : utilisez un {{FileName|/}} (barre oblique) comme séparateur de chemin dans {{Incode|filename}}.

Exemple :


```python
import FreeCAD as App
import Draft
import importDXF

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```





 

_

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/fr
