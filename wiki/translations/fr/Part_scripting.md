# Part scripting/fr
{{TOCright}}



## Introduction

La structure principale de données utilisée dans le module Part est le type de données [BRep](https://fr.wikipedia.org/wiki/B-Rep) de [OpenCASCADE](OpenCASCADE/fr.md). Presque tous les contenus et types d\'objets du module Part sont disponibles par script en [Python](Python/fr.md). Cela inclut les primitives géométriques, telles que les lignes, les cercles et les arcs, et toute la gamme des TopoShapes, comme les vertex, les arêtes, les fils, les faces, les solides et les composés. Pour chacun de ces objets, plusieurs méthodes de création existent, et pour certains d\'entre eux, notamment les TopoShapes, des opérations avancées telles que l\'union/différence/intersection booléenne sont également disponibles. Explorez le contenu du module Part, comme décrit dans la page [Notions de base sur les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md), pour en savoir plus.

L\'objet le plus simple pouvant être créé est une [Part Feature](Part_Feature/fr.md), qui possède une simple propriété **Placement** et des propriétés de base permettant de définir sa couleur et son apparence.

Un autre objet simple utilisé dans les objets géométriques 2D est un [Part Part2DObject](Part_Part2DObject/fr.md) qui constitue la base des [Sketcher SketchObject](Sketcher_SketchObject/fr.md) et de la plupart des [éléments de Draft](Draft_Workbench/fr.md).



### Voir aussi 

-   [Scripts pour création topologique](Topological_data_scripting/fr.md)
-   [OpenCASCADE](OpenCASCADE/fr.md)



## Script de test 

Testez la création de [Part Primitives](Part_Primitives/fr.md) avec un script.


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Ce script se trouve dans le répertoire d\'installation du programme et peut être examiné pour voir comment les primitives de base sont construites.


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```



## Exemples



### Ligne

Pour créer un élément de ligne, passez dans la [console Python](Python_console/fr.md) et entrez :


```python
import FreeCAD as App
import Part

doc = App.newDocument()

line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
obj = doc.addObject("Part::Feature", "Line")
obj.Shape= line.toShape()

doc.recompute()
```

Passons en revue l\'exemple Python ci-dessus étape par étape :


```python
import FreeCAD as App
import Part
doc = App.newDocument()
```

Ceci charge les modules FreeCAD et Part et crée un nouveau document.


```python
line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
```

La fonction Line décrit en fait un segment de ligne, d\'où le point de départ et le point final.


```python
obj = doc.addObject("Part::Feature", "Line")
obj.Shape= line.toShape()
```

Cette opération ajoute un type d\'objet Part au document et attribue la représentation de la forme du segment de ligne à la propriété {{Incode|Shape}} de l\'objet ajouté. Il est important de comprendre ici que nous utilisons une primitive géométrique ({{Incode|Part.LineSegment}}) pour créer une TopoShape à partir de celle-ci (avec la méthode {{Incode|toShape()}}). Seules les formes peuvent être ajoutées au document. Dans FreeCAD, les primitives géométriques sont utilisées comme \"structures de construction\" pour les formes.


```python
doc.recompute()
```

Met à jour le document. Cela prépare également la représentation visuelle du nouvel objet Part.

Notez qu\'un segment de ligne peut également être créé en spécifiant son point de départ et son point d\'arrivée directement dans le constructeur, par exemple {{Incode|Part.LineSegment(point1, point2)}}, ou nous pouvons créer une ligne par défaut et définir ses propriétés par la suite, comme nous l\'avons fait ici.

Une ligne peut également être créée en utilisant :


```python
import FreeCAD as App
import Part

def my_create_line(pt1, pt2, obj_name):
    obj = App.ActiveDocument.addObject("Part::Line", obj_name)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    App.ActiveDocument.recompute()
    return obj

line = my_create_line((0, 0, 0), (0, 10, 0), "LineName")
```



### Cercle

Un cercle peut être créé de la même manière :


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

circle = Part.Circle() 
circle.Radius = 10.0  
obj = doc.addObject("Part::Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Ou en utilisant :


```python
import FreeCAD as App
import Part

def my_create_circle(rad, obj_name):
    obj = App.ActiveDocument.addObject("Part::Circle", obj_name)
    obj.Radius = rad

    App.ActiveDocument.recompute()
    return obj

circle = my_create_circle(5.0, "CircleName")
```

Nous pouvons également créer un cercle en définissant son centre, son axe et son rayon :


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

center = App.Vector(1, 2, 3)
axis = App.Vector(1, 1, 1)
radius = 10
circle = Part.Circle(center, axis, radius)
obj = doc.addObject("Part::Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Ou en définissant trois points sur sa circonférence :


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(0, 0, 10)
circle = Part.Circle(p1, p2, p3)
obj = doc.addObject("Part::Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Notez qu\'une fois encore, nous avons utilisé le cercle (primitive géométrique) pour construire une forme. Nous pouvons bien sûr toujours accéder à notre géométrie de construction par la suite, en faisant :


```python
shape = obj.Shape
edge = shape.Edges[0]
curve = edge.Curve
```

Ici nous prenons la forme {{Incode|Shape}} de notre objet {{Incode|obj}} et ensuite sa liste de {{Incode|Edges}}. Dans ce cas, il n\'y aura qu\'une seule arête car nous avons créé la forme à partir d\'un seul cercle. Nous ne prenons donc que le premier élément de la liste {{Incode|Edges}}, puis sa courbe. Chaque arête a une {{Incode|Curve}}, qui est la primitive géométrique sur laquelle elle est basée.

### Arc

Un arc peut être créé comme suit :


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
arc = Part.Arc(p1, p2, p3)
obj = doc.addObject("Part::Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

Ceci dessine un demi-cercle. Le centre est à (0, 0, 0). Le rayon est de 10. P1 est le point de départ sur l\'axe +X. P2 est le point central sur l\'axe +Y et P3 est le point final sur l\'axe -X.

On peut aussi créer un arc à partir d\'un cercle :


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
circle = Part.Circle(p1, p2, p3)
arc = Part.ArcOfCircle(circle, 0.0, 0.7854)
obj = doc.addObject("Part::Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

Il faut un cercle, un angle de départ et un angle d\'arrivée en radians.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Part](Part_Workbench.md) > Part scripting/fr
