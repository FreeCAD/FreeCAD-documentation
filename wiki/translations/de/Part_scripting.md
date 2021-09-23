# Part scripting/de



{{TOCright}}

## Einführung

Die im Modul Part verwendete Hauptdatenstruktur ist der Datentyp [BRep](http://en.wikipedia.org/wiki/Boundary_representation) von OpenCascade. Fast alle Inhalte und Objekttypen des Part Moduls sind per [Python](Python/de.md) Skripten verfügbar. Dazu gehören geometrische Primitive wie Linie und Kreis (oder Bogen) und die gesamte Palette der TopoFormen, wie Knoten, Kanten, Drähte, Flächen, Festkörper und Verbünde. Für jedes dieser Objekte gibt es mehrere Erstellungsmethoden, und für einige von ihnen, insbesondere die TopoFormen, sind auch fortgeschrittene Operationen wie Bool\'sche Vereinigung/Differenz/Überschneidung verfügbar. Entdecke den Inhalt des Part Moduls, wie auf der Seite [FreeCAD Grundlagen SKripten](FreeCAD_Scripting_Basics/de.md) beschrieben, um mehr zu erfahren.

Das grundlegendste Objekt, das erstellt werden kann, ist ein [Part Formelement](Part_Feature/de.md), das eine einfache {{PropertyData/de|Platzierungs}} Eigenschaft und Grundeigenschaften hat, um seine Farbe und sein Aussehen zu definieren.

Ein weiteres einfaches Objekt, das in geometrischen 2D Objekten verwendet wird, ist [Part Part2DObjekt](Part_Part2DObject/de.md), das die Basis von [Skizzierer SkizzeObjekt](Sketcher_SketchObject/de.md) ist. ([Skizzierer](Sketcher_Workbench/de.md)), und die meisten [Entwurfselemente](Draft_Workbench/de.md).

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

Zum erstellen eines Linienelements schalte um zur Python Konsole und gib ein:


```python
import Part,PartGui 
doc=App.newDocument()  
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute()
```

Lass uns das obige Python Beispiel Schritt für Schritt betrachten:


```python
import Part,PartGui
doc=App.newDocument()
```

lädt die Part Modul und erstellt ein neues Dokument


```python
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
```

Line ist eigentlich eine Linienabschnitt, folglich der Anfangs- und Endpunkt.


```python
doc.addObject("Part::Feature","Line").Shape=l.toShape()
```

Dadurch wird dem Dokument ein Part Objekttyp hinzugefügt und weist die Formdarstellung des Liniensegments der \'Form\' Eigenschaft des hinzugefügten Objekts zu. Es ist wichtig, hier zu verstehen, dass wir ein geometrisches Grundelement (das Part.LineSegment) verwendet haben, um daraus eine TopoForm zu erstellen (die toShape() Methode). Nur Formen können dem Dokument hinzugefügt werden. In FreeCAD werden Geometrie Grundelemente als \"Baustrukturen\" für Formen verwendet.


```python
doc.recompute()
```

Aktualisiert das Dokument. Damit auch die visuelle Darstellung des neuen Part Objekts.

Beachte, dass ein Liniensegment durch Angabe der Anfangs-und Endpunkt direkt im Konstruktor erstellt werden kann, z.B. Part.LineSegment (Punkt1, Punkt2), oder wir können eine Standardlinie erstellen und seine Eigenschaften anschießend festlegen, wie wir es hier gemacht haben.

Eine Linie kann erstellt werden auch mit:


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

Ein Kreis kann in ähnlicher Weise erstellt werden:


```python
import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=10.0  
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

oder mit:


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

Bemerke wieder, wir verwendeten den Kreis (Geometrie Grundelement), um eine Form daraus zu erstellen. Wir können natürlich noch immer auf unsere Konstruktionsgeometrie später zugreifen, und zwar so:


```python
s = f.Shape
e = s.Edges[0]
c = e.Curve
```

Hier nehmen wir die Form unseres Objekts f, dann nehmen wir die Liste der Kanten. In diesem Fall wird es nur eine geben, weil wir die ganze Form aus einem einzelnen Kreis machten, also nehmen wir nur das erste Element der Kantenliste, und wir nehmen seinen Verlauf. Jede Kante hat einen Verlauf, welches das Geometrie Grundelement ist, worauf der Verlauf basiert ist.

Gehe auf die Seite [Topologisches Datenskripting](Topological_data_scripting/de.md), wenn du mehr wissen möchtest.


{{Powerdocnavi

}}  

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
