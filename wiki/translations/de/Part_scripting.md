# Part scripting/de
{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Die im Modul Part verwendete Hauptdatenstruktur ist der Datentyp [BRep](http://en.wikipedia.org/wiki/Boundary_representation) von OpenCascade. Fast alle Inhalte und Objekttypen des Part Moduls sind per [Python](Python/de.md) Skripten verfügbar. Dazu gehören geometrische Primitive wie Linie und Kreis (oder Bogen) und die gesamte Palette der TopoFormen, wie Knoten, Kanten, Drähte, Flächen, Festkörper und Verbünde. Für jedes dieser Objekte gibt es mehrere Erstellungsmethoden, und für einige von ihnen, insbesondere die TopoFormen, sind auch fortgeschrittene Operationen wie Bool\'sche Vereinigung/Differenz/Überschneidung verfügbar. Entdecke den Inhalt des Part Moduls, wie auf der Seite [FreeCAD Grundlagen SKripten](FreeCAD_Scripting_Basics/de.md) beschrieben, um mehr zu erfahren.


</div>


<div class="mw-translate-fuzzy">

Das grundlegendste Objekt, das erstellt werden kann, ist ein [Part Formelement](Part_Feature/de.md), das eine einfache {{PropertyData/de|Platzierungs}} Eigenschaft und Grundeigenschaften hat, um seine Farbe und sein Aussehen zu definieren.


</div>


<div class="mw-translate-fuzzy">

Ein weiteres einfaches Objekt, das in geometrischen 2D Objekten verwendet wird, ist [Part Part2DObjekt](Part_Part2DObject/de.md), das die Basis von [Skizzierer SkizzeObjekt](Sketcher_SketchObject/de.md) ist. ([Skizzierer](Sketcher_Workbench/de.md)), und die meisten [Entwurfselemente](Draft_Workbench/de.md).


</div>

### Siehe auch 

-   [Topologisches Daten Skripten](Topological_data_scripting/de.md)
-   [OpenCASCADE](OpenCASCADE/de.md)

## Testskript

Teste die Erstellung von [Part Grundelementen](Part_Primitives/de.md) mit einem Skript. <small>(v0.19)</small> 


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Dieses Skript befindet sich im Installationsverzeichnis des Programms und kann untersucht werden, um zu sehen, wie die Basisgrundelemente aufgebaut sind.


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

## Beispiele

### Line


<div class="mw-translate-fuzzy">

Zum erstellen eines Linienelements schalte um zur Python Konsole und gib ein:


</div>


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


<div class="mw-translate-fuzzy">

Lass uns das obige Python Beispiel Schritt für Schritt betrachten:


</div>


```python
import FreeCAD as App
import Part
doc = App.newDocument()
```


<div class="mw-translate-fuzzy">

lädt die Part Modul und erstellt ein neues Dokument


</div>


```python
line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
```

Line ist eigentlich eine Linienabschnitt, folglich der Anfangs- und Endpunkt.


```python
obj = doc.addObject("Part::Feature", "Line")
obj.Shape= line.toShape()
```


<div class="mw-translate-fuzzy">

Dadurch wird dem Dokument ein Part Objekttyp hinzugefügt und weist die Formdarstellung des Liniensegments der \'Form\' Eigenschaft des hinzugefügten Objekts zu. Es ist wichtig, hier zu verstehen, dass wir ein geometrisches Grundelement (das Part.LineSegment) verwendet haben, um daraus eine TopoForm zu erstellen (die toShape() Methode). Nur Formen können dem Dokument hinzugefügt werden. In FreeCAD werden Geometrie Grundelemente als \"Baustrukturen\" für Formen verwendet.


</div>


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

Aktualisiert das Dokument. Damit auch die visuelle Darstellung des neuen Part Objekts.


</div>


<div class="mw-translate-fuzzy">

Beachte, dass ein Liniensegment durch Angabe der Anfangs-und Endpunkt direkt im Konstruktor erstellt werden kann, z.B. Part.LineSegment (Punkt1, Punkt2), oder wir können eine Standardlinie erstellen und seine Eigenschaften anschießend festlegen, wie wir es hier gemacht haben.


</div>


<div class="mw-translate-fuzzy">

Eine Linie kann erstellt werden auch mit:


</div>


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

### Circle

Ein Kreis kann in ähnlicher Weise erstellt werden:


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


<div class="mw-translate-fuzzy">

oder mit:


</div>


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

Alternatively we can create a circle by defining its center, axis and radius:


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

Or by defining three points on its circumference:


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


<div class="mw-translate-fuzzy">

Bemerke wieder, wir verwendeten den Kreis (Geometrie Grundelement), um eine Form daraus zu erstellen. Wir können natürlich noch immer auf unsere Konstruktionsgeometrie später zugreifen, und zwar so:


</div>


```python
shape = obj.Shape
edge = shape.Edges[0]
curve = edge.Curve
```


<div class="mw-translate-fuzzy">

Hier nehmen wir die Form unseres Objekts f, dann nehmen wir die Liste der Kanten. In diesem Fall wird es nur eine geben, weil wir die ganze Form aus einem einzelnen Kreis machten, also nehmen wir nur das erste Element der Kantenliste, und wir nehmen seinen Verlauf. Jede Kante hat einen Verlauf, welches das Geometrie Grundelement ist, worauf der Verlauf basiert ist.


</div>

### Arc

An arc can be created like this:


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

This draws a half circle. The center is at (0, 0, 0). The radius is 10. P1 is the start point on +X axis. P2 is the middle point on +Y axis and P3 is the end point on -X axis.

We can also create an arc from a circle:


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

It needs a circle, and a start angle and end angle in radians.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Part](Part_Workbench.md) > Part scripting/de
