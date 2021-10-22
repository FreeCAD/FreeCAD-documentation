# Part Part2DObject/de
## Einführung

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Ein _, das in der [3D Ansicht](3D_view/de.md) angezeigt werden kann.

Das `Part::Part2DObject` ist von einem [Part Formelement](Part_Feature/de.md) abgeleitet, ist aber auf 2D Geometrie spezialisiert, da seine Form auf einer Ebene liegen wird. Diese Ebene wird durch die {{PropertyData/de|Platzierung}} Eigenschaft definiert (Position, Normale und Rotation). Die Ebene kann aber auch durch unterstützende geometrische Elemente definiert werden, wie z.B. die Ebene, die durch drei beliebige Knoten erzeugt wird, oder eine Fläche eines Volumenkörpers.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die Klasse `Part::Part2DObject* ist auf 2D Formen spezialisiert, so dass sie die Basisklasse für planare Objekte ist, die mit den Werkbänken Draft und Sketcher erstellt werden. Sie enthält eine Erweiterung, mit der sie an Flächen und Ebenen angehängt werden kann.`

## Anwendung

Das [Part2DObject](Part_Part2DObject/de.md) ist ein internes Objekt, kann also nicht von der grafischen Oberfläche aus erzeugt werden, sondern nur von der [Python Konsole](Python_console/de.md), wie im Abschnitt [Scripting](Part_Part2DObject#Scripting.md) beschrieben.

Das `Part::Part2DObject` ist im [Part Arbeitsbereich](Part_Workbench/de.md) festgelegt, kann aber als Basisklasse für [geskriptete Objekte](scripted_objects/de.md) in allen [Arbeitsbereichen](Workbenches/de.md) die geometrische 2D Formen erzeugen, verwendet werden. Beispielsweise ist sie das Basisobjekt für Skizzen ([Skizzierer SkizzeObjekt](Sketcher_SketchObject/de.md)), und für die meisten Objekte, die mit der [Draft Workbench](Draft_Workbench/de.md) erstellt werden.

Arbeitsbereiche können diesem Grundelement weitere Eigenschaften hinzufügen, um ein Objekt mit komplexem Verhalten zu erzeugen.

## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Ein _ (`Part::Feature` Klasse) abgeleitet, daher teilt sie alle Eigenschaften der letzteren.

Zusätzlich zu den in [Part Formelement](Part_Feature/de.md) beschriebenen Eigenschaften hat das Part Teil2DObjekt im [Eigenschaftseditor](property_editor/de.md) die folgenden Eigenschaften. Ausgeblendete Eigenschaften können unter Verwendung des {{MenuCommand/de|Alles anzeigen}} Befehl im Kontextmenü des [Eigenschaftseditor](property_editor/de.md) angezeigt werden.

### Daten


{{TitleProperty|Attachment}}

-    **Map Mode|Enumeration**: {{value|Deactivated}} by default. This property determines a plane which the object will use as reference for 2D geometry. Clicking on the ellipsis **...** (three dots), to the right of the entry field opens the [Part EditAttachment](Part_EditAttachment.md) [task panel](task_panel.md) that allows selecting the supporting plane by picking different elements in the [3D view](3D_view.md). The different modes are: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

See [Part EditAttachment](Part_EditAttachment.md) for more information on all mapping modes.

The following two properties are normally hidden. They become visible once **Map Mode** is something other than {{value|Deactivated}}.

-    **Map Reversed|Bool**: it defaults to `False`; if it is `True` the Z direction will be reversed. For example, a [sketch](sketch.md) will be flipped upside down.

-    **Attachment Offset|Placement**: the position of the object in the [3D view](3D_view.md), with respect to the attachment object\'s placement. The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

#### Ausgeblendete Dateneigenschaften 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Part_Part2DObject#Scripting.md).


{{TitleProperty|Attachment}}

-    **Attacher Type|String**: class name of the attach engine object driving the attachment. It defaults to `Attacher::AttachEnginePlane`.

-    **Support|LinkSubList**: it is the plane or face supporting the 2D geometry. It defaults to an empty list `[]`.

-    **Map Path Parameter|Float**: sets point of curve to map a [sketch](sketch.md) to. It goes from {{value|0}} to {{value|1}}, which corresponds to the {{value|start}} and {{value|end}}. It defaults to {{value|0}}.

### Ansicht


{{TitleProperty|Grid}}

-    **Grid Size|Length**: the size of the spacing of the local grid lines in the [3D view](3D_view.md); it defaults to {{value|10 mm}}.

-    **Grid Snap|Bool**: it defaults to `False`; if `True` the grid can be used to snap points.

-    **Grid Style|Enumeration**: the style of the grid lines; {{value|Dashed}} (default) or {{value|Light}}.

-    **Show Grid|Bool**: it defaults to `False`; if `True` a grid local to the object will be displayed in the [3D view](3D_view.md). This grid is independent of the [Draft Grid](Draft_ToggleGrid.md).

-    **Tight Grid|Bool**: if `True` (default) the local grid will be localized around the origin of the shape, otherwise it will extend itself more.

#### Ausgeblendete Eigenschaften Ansicht 


{{TitleProperty/de|Grundlage}}

-    **Proxy|PythonObject**: eine benutzerdefinierte Providerklasse, die mit diesem Objekt verknüpft ist. Das gibt es nur für die [Python](Python/de.md) Version. Siehe [Skripten](Std_Group/de#Skripten.md).

Alle anderen Ansichtseigenschaften, einschließlich ausgeblendeter Eigenschaften, sind die des [Part Formelement](Part_Feature/de.md) Basisobjekts.

## Skripten


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).

Siehe [Part Formelemente](Part_Feature/de.md) zu allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Ein Teil2DObjekt wird mit der `addObject()` Methode des Dokuments erstellt. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Diese grundlegende `Part::Part2DObject` hat kein Proxyobjekt, sodass es vollständig für sub-classing verwendet werden kann.

Daher solltest du für [Python](Python/de.md) subclassing das Objekt `Part::Part2DObjectPython` erstellen.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```

Beispielsweise, die meisten Werkzeuge aus dem [Entwurf Arbeitsbereich](Draft_Workbench/de.md), wie [Entwurf Linie](Draft_Line/de.md), [Entwurf Rechteck](Draft_Rectangle/de.md), [Entwurf Polygon](Draft_Polygon/de.md), usw., sind `Part::Part2DObjectPython` Objekte mit einem benutzerdefinierten Symbol und zusätzliche Eigenschaften.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/de
