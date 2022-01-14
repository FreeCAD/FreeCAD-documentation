# Part scripting/fr
{{TOCright}}

## Introduction

La structure principale des données utilisée dans le module Part est le type de données [BRep](https://fr.wikipedia.org/wiki/B-Rep) d\'OpenCascade. Presque tous les contenus et types d\'objets du module Part sont disponibles par script [Python](Python/fr.md). Cela inclut les primitives géométriques, telles que Ligne et Cercle (ou Arc), et toute la gamme de TopoShapes, comme les sommets, les arêtes, les fils, les faces, les solides et les composés. Pour chacun de ces objets, plusieurs méthodes de création existent, et pour certaines d\'entre elles, en particulier les TopoShapes, des opérations avancées comme l\'union booléenne/différence/intersection sont également disponibles. Pour en savoir plus, explorez le contenu du module Part, comme décrit dans la page [Notions de base sur les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'objet le plus simple pouvant être créé est une [Part Feature](Part_Feature/fr.md), qui possède une simple propriété {{PropertyData/fr|Placement}} et des propriétés de base permettant de définir sa couleur et son apparence.

Un autre objet simple utilisé dans les objets géométriques 2D est [Part2DObject](Part_Part2DObject/fr.md) qui constitue la base des [Sketcher SketchObject](Sketcher_SketchObject/fr.md) ([atelier Sketcher](Sketcher_Workbench/fr.md)) et la plupart des [éléments Draft](Draft_Workbench/fr.md).

### Voir aussi 

-   [Scripts pour création topologique](Topological_data_scripting/fr.md)
-   [OpenCASCADE](OpenCASCADE/fr.md)

## Script de test 

Testez la création de [Part Primitives](Part_Primitives/fr.md) avec un script. {{Version/fr|0.19}}


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Ce script se trouve dans le répertoire d\'installation du programme et peut être examiné pour voir comment les primitives de base sont construites. 
```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

## Exemples

Pour créer un élément ligne, passer à la console Python et taper :


```python
import Part,PartGui 
doc=App.newDocument()  
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute()
```

Passons en revue l\'exemple Python ci-dessus étape par étape :


```python
import Part,PartGui
doc=App.newDocument()
```

Charge l\'atelier Part et crée un nouveau document


```python
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
```

La fonction Line décrit en fait un segment de ligne, d\'où le point de départ et le point final.


```python
doc.addObject("Part::Feature","Line").Shape=l.toShape()
```

Cette commande ajoute un objet de type Part (Pièce) au document et affecte la représentation de forme du segment de ligne à la propriété \'Shape\' (\'forme\') de l\'objet ajouté. Il est important de comprendre ici que nous avons utilisé une primitive géométrique (Part.LineSegment) pour créer un TopoShape à partir de celle-ci (la méthode toShape()). Seules les formes peuvent être ajoutées au document. Dans FreeCAD, les primitives géométriques sont utilisées comme des \"structures de base\" pour construire les formes.


```python
doc.recompute()
```

Met à jour le document. Cela prépare également la représentation visuelle du nouvel objet Part.

Notez qu\'une Line Segment (segment de ligne) peut être créée en spécifiant son point de départ et son point final directement dans le constructeur, par ex. Part.LineSegment(point1, point2) ou nous pouvons créer une ligne par défaut et définir ses propriétés après, comme nous l\'avons fait ici.

Une ligne peut également être créée en utilisant :


```python
import FreeCAD
import Part
DOC = FreeCAD.newDocument()

def mycreateLine(pt1, pt2, objName):
    obj = DOC.addObject("Part::Line", objName)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    DOC.recompute()
    return obj

line = mycreateLine((0,0,0), (0,10,0), "LineName")
```

Un cercle peut être créé de la même manière:


```python
import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=10.0  
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

ou en utilisant :


```python
import FreeCAD
import Part
DOC = FreeCAD.newDocument()

def mycreateCircle(rad, objName):
    obj = DOC.addObject("Part::Circle", objName)
    obj.Radius = rad

    DOC.recompute()
    return obj

circle = mycreateCircle(5.0, "CircleName")
```

ou créer un cercle défini par son centre, son axe et son rayon en utilisant :


```python
import Part
doc = App.activeDocument()
center = App.Vector(1,2,3)
axis = App.Vector(1,1,1)
radius = 10
c=Part.Circle(center,axis,radius)
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

ou créer un cercle défini par trois points en utilisant :


```python
import Part
doc = App.activeDocument()
p1 = App.Vector(10,0,0)
p2 = App.Vector(0,10,0)
p3 = App.Vector(0,0,10)
c = Part.Circle(p1,p2,p3)
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

Notez qu\'une fois encore, nous avons utilisé le cercle (primitive géométrique) pour construire une forme. Nous pouvons bien sûr toujours accéder à notre géométrie de construction par la suite, en faisant:


```python
s = f.Shape
e = s.Edges[0]
c = e.Curve
```

Ici on prend la forme de notre objet f, puis nous prenons la liste de ses arêtes. Dans ce cas il y aura une seule arête parce que nous avons fait toute la forme à partir d\'un cercle unique, c\'est pourquoi nous ne prenons que le premier élément de la liste des arêtes, et puis nous récupérons sa courbe. Chaque arête a une courbe, qui est la géométrie primitive, sur laquelle elle est basée.

Rendez-vous sur la page [Scripts pour création topologique](Topological_data_scripting/fr.md) si vous voulez en savoir plus.





{{Powerdocnavi

}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Part](Part_Workbench.md) > Part scripting/fr
