# Sketcher SketchObject/de
{{TOCright}}



## Einleitung

<img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;">

Ein [Sketcher SketchObject](Sketcher_SketchObject/de.md), oder formal ein `Sketcher::SketchObject`, ist das Basiselement für die Erstellung von 2D-Objekten mit der Arbeitsumgebung [Sketcher](Sketcher_Workbench/de.md).

Das `Sketcher::SketchObject` ist vom [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet, d.h. es ist ein [Part Feature](Part_Feature/de.md)-Objekt spezialisiert auf 2D-Geometrie. Wie das Part2DObject, kann das SketchObject Ebenen und Flächen zugeordnet werden. Zusätzlich kann das SketchObject mit geometrischen Randbedingungen arbeiten.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*



## Anwendung

1.  Zum Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) wechseln.

2.  Die Schaltfläche **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NeueSkizze](Sketcher_NewSketch/de.md)** drücken.

3.  Eine **Skizzenorientierung** auswählen: XY-Ebene, XZ-Ebene, oder YZ-Ebene. Wahlweise die **Umgekehrte Richtung** aktivieren, und einen **Offset**-Wert eingeben.

4.  
    **OK**drücken.

Auch wenn das Sketch-Objekt eigenständig verwendet werden kann, um auf einer Fläche zu zeichnen, wird es meistens in Verbindung mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) verwendet um extrudierte Volumenkörper zu erstellen.

1.  Zum Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) wechseln.

2.  Die Schaltfläche **[<img src=images/PartDesign_Body.svg style="width:16px"> [Körper erstellen](PartDesign_Body/de.md)** drücken.

3.  Die Schaltfläche **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Skizze erstellen](PartDesign_NewSketch/de.md)** drücken.

4.  
    **Element auswählen**: XY_Plane (Basis-Ebene), XZ_Plane (Basis-Ebene), oder YZ_Plane (Basis-Ebene).

5.  
    **OK**drücken.



## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Das [Sketcher Sketch-Objekt](Sketcher_SketchObject/de.md) (`Sketcher::SketchObject`-Klasse) ist von dem [Part Part2DObject](Part_Part2DObject/de.md) (`Part::Part2DObject`-Klasse) abgeleitet und erbt all seine Eigenschaften.

Das Sketcher Sketch-Objekt hat außerdem die folgenden zusätzlichen Eigenschaften im [Eigenschafteneditor](Property_editor/de.md). Ausgeblendete Eigenschaften können mit dem Befehl **Alle anzeigen** im Kontextmenü des [Eigenschafteneditors](Property_editor.md) angezeigt werden.



### Daten


{{TitleProperty|Sketch}}

-    {{PropertyData/de|Geometry|GeometryList|Hidden}}: Eine Liste von Part-Geometrien die in der Skizze enthalten sind.

-    {{PropertyData/de|Constraints|}}: Benannte Randbedingungen, wenn welche vorhanden sind, andernfalls eine leere Liste `[]`.

-    {{PropertyData/de|External Geometry|LinkSubList}}: Eine Liste von Part-Geometrien außerhalb dieser Skizze, die als Referenz verwendet werden.

-    {{PropertyData/de|Fully Constrained|Bool|Hidden}}: Nicht änderbar (read-only). Wird `True` angezeigt, ist die Skizze vollständig bestimmt.



### Ansicht


{{TitleProperty|Auto Constraints}}

-    {{PropertyView/de|Autoconstraints|Bool}}: Wenn `True`, werden Randbedingungen automatisch hinzugefügt, während Geometrien gezeichnet werden.

-    {{PropertyView/de|Avoid Redundant|Bool}}: Wenn `True`, werden überflüssige automatische Randbedingungen vermieden.


{{TitleProperty|Grid}}

-    {{PropertyView/de|Grid Auto Size|Bool|Hidden}}: Wenn `True`, wird die Größe eines Rasters auf Basis der Boundingbox der Geometrie einer Skizze angepasst.

-    {{PropertyView/de|Grid Size|Length}}: Der Wert für den Abstand der lokalen Rasterlinien in der [3D-Ansicht](3D_view/de.md); Standardwert ist {{value|10 mm}}.

-    {{PropertyView/de|Grid Snap|Bool}}: Wenn `True`, kann das Raster zum Fangen von Punkten verwendet werden.

-    {{PropertyView/de|Grid Style|Enumeration}}: Linienart der Rasterlinien; {{value|Dashed}} (Standard) oder {{value|Light}}.

-    {{PropertyView/de|Show Grid|Bool}}: Wenn `True`, wird in der [3D-Ansicht](3D_view/de.md) örtlich am Objekt ein Raster angezeigt. Dieses Raster ist unabhängig vom [Draft Raster](Draft_ToggleGrid/de.md).

-    {{PropertyView/de|Show Only In Edit Mode|Bool}}: Wenn `True`, wird das Raster nur angezeigt, während die Skizze bearbeitet wird.

-    {{PropertyView/de|Tight Grid|Bool}}: Wenn `True`, wird das örtliche Raster nur in der nähe des Ursprungs der Form dargestellt, andernfalls wird es weiter ausgedehnt.

-    {{PropertyView/de|max Number Of Lines|Integer}}: Die maximale Anzahl an Linien in einem Raster.


{{TitleProperty|Visibility automation}}

-    {{PropertyView/de|Editing Workbench|String}}: Name des Arbeitsbereiches, der aktiviert wird, wenn eine Skizze bearbeitet wird; Standardwert ist {{value|SketcherWorkbench}}.

-    {{PropertyView/de|Force Ortho|Bool}}: Wenn `True`, wird die Kamera in den Modus [Orthoggonale Ansicht](Std_OrthographicCamera/de.md) gezwungen, wenn die Skizze geöffnet wird.

-    {{PropertyView/de|Hide Dependent|Bool}}: Wenn `True`, werden alle Objekte ausgeblendet, die von dieser Skizze abhängen, wenn die Skizze geöffnet wird.

-    {{PropertyView/de|Restore Camera|Bool}}: Wenn `True`, wird die Kameraposition gesichert, bevor die Skizze geöffnet wird und wiederhergestellt, nachdem die Skizze geschlossen wurde.

-    {{PropertyView/de|Section View|Bool}}: Wenn `True`, sind nur (Teile von) Objekte(n) hinter der Skizzenebene sichtbar, während die Skizze bearbeitet wird.

-    {{PropertyView/de|Show Links|Bool}}: Wenn `True`, werden alle Objekte angezeigt, die zur Verknüpfung mit externer Geometrie verwendet werden, wenn die Skizze geöffnet wird.

-    {{PropertyView/de|Show Support|Bool}}: Wenn `True`, werden alle Objekte dargestellt, mit denen diese Skizze verknüpft ist, wenn die Skizze geöffnet wird.

-    {{PropertyView/de|Tempo Vis|PythonObject|Hidden}}: Eine mit diesem Objekt verbundene angepasste Klasse, die das Ein- und Ausblenden anderer Objekte regelt, während die Skizze geöffnet oder geschlossen wird.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.

Ein Sketch-Objekt wird mit der `addObject()` Methode des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObject", "Sketch")
obj.Label = "Custom label"
```

Für die Instanziierung von Unterklassen mit [Python](Python/de.md) sollte ein `Sketcher::SketchObjectPython`-Objekt erstellt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher_Tools_navi

}} {{Document_objects_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/de
