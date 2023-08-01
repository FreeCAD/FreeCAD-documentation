# Part Part2DObject/de
{{TOCright}}



## Einführung

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Ein [Part Part2DObject](Part_Part2DObject/de.md), oder formal ein `Part::Part2DObject`, ist ein einfaches Element mit einer [topologischen Form](Part_TopoShape/de.md), das in der [3D-Ansicht](3D_view/de.md) angezeigt werden kann.

Das `Part::Part2DObject` ist von dem [Part Formelement](Part_Feature/de.md) abgeleitet, ist aber auf 2D-Geometrie spezialisiert, da seine Form auf einer Ebene liegen wird. Diese Ebene wird durch die {{PropertyData/de|Placement}} definiert (Position, Normale und Rotation). Die Ebene kann aber auch durch unterstützende geometrische Elemente definiert werden, wie z.B. die Ebene, die durch drei beliebige Knoten erzeugt wird, oder eine Fläche eines Volumenkörpers.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*



## Anwendung

Das [Part2DObject](Part_Part2DObject/de.md) ist ein internes Objekt, kann also nicht von der grafischen Oberfläche aus erzeugt werden, sondern nur von der [Python-Konsole](Python_console/de.md), wie im Abschnitt [Scripten](#Scripten.md) beschrieben.

Das `Part::Part2DObject` ist im Arbeitsbereich [Part](Part_Workbench/de.md) festgelegt, kann aber als Basisklasse für [skriptgenerierte Objekte](scripted_objects/de.md) in allen [Arbeitsbereichen](Workbenches/de.md) die geometrische 2D-Formen erzeugen, verwendet werden. Beispielsweise ist sie das Basisobjekt für Skizzen ([Sketcher SketchObjekt](Sketcher_SketchObject/de.md)), und für die meisten Objekte, die mit dem Arbeitsbereich [Draft](Draft_Workbench/de.md) erstellt werden.

Arbeitsbereiche können diesem Grundelement weitere Eigenschaften hinzufügen, um ein Objekt mit komplexem Verhalten zu erzeugen.



## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Das [Part Part2DObjekt](Part_Part2DObject/de.md) (Klasse `Part:: Part2DObject`) wird von einem [Part Formelement](Part_Feature/de.md) (Klasse`Part::Feature`) abgeleitet und erbt alle seiner Eigenschaften.

Das Part Part2DObjekt hat außerdem die folgenden zusätzlichen Eigenschaften im [Eigenschafteneditor](property_editor/de.md). Ausgeblendete Eigenschaften können unter Verwendung des Befehls **Alles anzeigen** im Kontextmenü des [Eigenschaftseditors](Property_editor/de.md) angezeigt werden.



### Daten


{{TitleProperty|Attachment}}

-    <div id="Property_Attacher_Type">
    </div>
    **Attacher Type|String|Hidden**: class name of the attach engine object driving the attachment. It defaults to `Attacher::AttachEnginePlane`.

-    <div id="Property_Support">
    </div>
    **Support|LinkSubList**: it is the plane or face supporting the 2D geometry. It defaults to an empty list `[]`.

-    <div id="Property_Map_Mode">
    </div>
    **Map Mode|Enumeration**: {{value|Deactivated}} by default. This property determines a plane which the object will use as reference for 2D geometry. Clicking on the ellipsis **...** (three dots), to the right of the entry field starts the [Part EditAttachment](Part_EditAttachment.md) command that allows selecting the supporting plane by picking different elements in the [3D view](3D_view.md). The different modes are: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

-    <div id="Property_Map_Reversed">
    </div>
    **Map Reversed|Bool**: it defaults to `False`; if it is `True` the Z direction will be reversed. For example, a [sketch](sketch.md) will be flipped upside down. Hidden if **Map Mode** is {{value|Deactivated}}.

-    <div id="Property_Map_Path">
    </div>
    **Map Path Parameter|Float|Hidden**: sets point of curve to map a [sketch](sketch.md) to. It goes from {{value|0}} to {{value|1}}, which corresponds to the {{value|start}} and {{value|end}}. It defaults to {{value|0}}.

-    <div id="Property_Attachment_Offset">
    </div>
    **Attachment Offset|Placement**: the position of the object in the [3D view](3D_view.md), with respect to the attachment object\'s placement. The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md). Hidden if **Map Mode** is {{value|Deactivated}}.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelemente](Part_Feature/de.md) zu allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Ein Teil2DObjekt wird mit der `addObject()` Methode des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Für [Python](Python/de.md)-Subclassing sollte ein `Part::Part2DObjectPython`-Objekt erstellt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/de
