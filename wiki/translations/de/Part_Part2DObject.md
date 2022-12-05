# Part Part2DObject/de
{{TOCright}}

## Einführung

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Ein [Part Part2DObject](Part_Part2DObject/de.md), oder formal ein `Part::Part2DObject`, ist ein einfaches Element mit einer [topologischen Form](Part_TopoShape/de.md), das in der [3D-Ansicht](3D_view/de.md) angezeigt werden kann.

Das `Part::Part2DObject` ist von dem [Part Formelement](Part_Feature/de.md) abgeleitet, ist aber auf 2D-Geometrie spezialisiert, da seine Form auf einer Ebene liegen wird. Diese Ebene wird durch die {{PropertyData/de|Placement}} definiert (Position, Normale und Rotation). Die Ebene kann aber auch durch unterstützende geometrische Elemente definiert werden, wie z.B. die Ebene, die durch drei beliebige Knoten erzeugt wird, oder eine Fläche eines Volumenkörpers.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*

## Anwendung


<div class="mw-translate-fuzzy">

Das [Part2DObject](Part_Part2DObject/de.md) ist ein internes Objekt, kann also nicht von der grafischen Oberfläche aus erzeugt werden, sondern nur von der [Python Konsole](Python_console/de.md), wie im Abschnitt [Scripting](Part_Part2DObject#Scripting.md) beschrieben.


</div>


<div class="mw-translate-fuzzy">

Das `Part::Part2DObject` ist im [Part Arbeitsbereich](Part_Workbench/de.md) festgelegt, kann aber als Basisklasse für [geskriptete Objekte](scripted_objects/de.md) in allen [Arbeitsbereichen](Workbenches/de.md) die geometrische 2D Formen erzeugen, verwendet werden. Beispielsweise ist sie das Basisobjekt für Skizzen ([Skizzierer SkizzeObjekt](Sketcher_SketchObject/de.md)), und für die meisten Objekte, die mit der [Draft Workbench](Draft_Workbench/de.md) erstellt werden.


</div>

Arbeitsbereiche können diesem Grundelement weitere Eigenschaften hinzufügen, um ein Objekt mit komplexem Verhalten zu erzeugen.

## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.


<div class="mw-translate-fuzzy">

Ein [Part Teil2DObjekt](Part_Part2DObject/de.md) (`PartDesign::Body` Klasse) wird von einem [Part Formelement](Part_Feature/de.md) (`Part::Feature` Klasse) abgeleitet, daher teilt sie alle Eigenschaften der letzteren.


</div>


<div class="mw-translate-fuzzy">

Zusätzlich zu den in [Part Formelement](Part_Feature/de.md) beschriebenen Eigenschaften hat das Part Teil2DObjekt im [Eigenschaftseditor](property_editor/de.md) die folgenden Eigenschaften. Ausgeblendete Eigenschaften können unter Verwendung des {{MenuCommand/de|Alles anzeigen}} Befehl im Kontextmenü des [Eigenschaftseditor](property_editor/de.md) angezeigt werden.


</div>

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


<div class="mw-translate-fuzzy">


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).


</div>

Siehe [Part Formelemente](Part_Feature/de.md) zu allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Ein Teil2DObjekt wird mit der `addObject()` Methode des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```


<div class="mw-translate-fuzzy">

Daher solltest du für [Python](Python/de.md) subclassing das Objekt `Part::Part2DObjectPython` erstellen.


</div>


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/de
