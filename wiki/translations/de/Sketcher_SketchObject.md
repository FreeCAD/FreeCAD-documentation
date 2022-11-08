# Sketcher SketchObject/de
{{TOCright}}

## Einleitung

<img alt="" src=images/Sketcher_Sketch.svg  style="width   *32px;">

Ein [Sketcher SketchObject](Sketcher_SketchObject/de.md), oder formal ein `Sketcher   *   *SketchObject`, ist das Basiselement für die Erstellung von 2D-Objekten mit der Arbeitsumgebung [Sketcher](Sketcher_Workbench/de.md).

Das `Sketcher   *   *SketchObject` ist vom [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet, d.h. es ist ein [Part Feature](Part_Feature/de.md)-Objekt spezialisiert auf 2D-Geometrie. Wie das Part2DObject, kann das SketchObject Ebenen und Flächen zugeordnet werden. Zusätzlich kann das SketchObject mit geometrischen Randbedingungen arbeiten.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*

## Anwendung

1.  Zum Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) wechseln.

2.  Die Schaltfläche **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Sketcher NeueSkizze](Sketcher_NewSketch/de.md)** drücken.

3.  Eine {{MenuCommand/de|Skizzenorientierung}} auswählen   * XY-Ebene, XZ-Ebene, oder YZ-Ebene. Wahlweise die {{MenuCommand/de|Umgekehrte Richtung}} aktivieren, und einen **Offset**-Wert eingeben.

4.  
    **OK**drücken.

Auch wenn das Sketch-Objekt eigenständig verwendet werden kann, um auf einer Fläche zu zeichnen, wird es meistens in Verbindung mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) verwendet um extrudierte Volumenkörper zu erstellen.

1.  Zum Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) wechseln.

2.  Die Schaltfläche **[<img src=images/PartDesign_Body.svg style="width   *16px"> [Körper erstellen](PartDesign_Body/de.md)** drücken.

3.  Die Schaltfläche **[<img src=images/PartDesign_NewSketch.svg style="width   *16px"> [PartDesign Skizze erstellen](PartDesign_NewSketch/de.md)** drücken.

4.  
    **Element auswählen**   * XY_Plane (Basis-Ebene), XZ_Plane (Basis-Ebene), oder YZ_Plane (Basis-Ebene).

5.  
    **OK**drücken.

## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Das [Sketcher Sketch-Objekt](Sketcher_SketchObject/de.md) (`Sketcher   *   *SketchObject`-Klasse) ist von dem [Part Part2DObject](Part_Part2DObject/de.md) (`Part   *   *Part2DObject`-Klasse) abgeleitet und erbt all seine Eigenschaften.

Das Sketcher Sketch-Objekt hat außerdem die folgenden zusätzlichen Eigenschaften im [Eigenschafteneditor](Property_editor/de.md). Ausgeblendete Eigenschaften können mit dem Befehl {{MenuCommand/de|Alle anzeigen}} im Kontextmenü des [Eigenschafteneditors](Property_editor.md) angezeigt werden.

### Daten


{{TitleProperty|Sketch}}

-    **Geometry|GeometryList|Hidden**   * a list of Part geometries that exist inside the sketch.

-    **Constraints|**   * named constraints, if they exist; otherwise it is an empty list `[]`.

-    **External Geometry|LinkSubList**   * a list of Part geometries outside this Sketch that are used for reference.

-    **Fully Constrained|Bool|Hidden**   * (read-only) if `True` the sketch is fully constrained.

### Ansicht


{{TitleProperty|Auto Constraints}}

-    **Autoconstraints|Bool**   * if `True` constraints are automatically added when geometry is drawn.

-    **Avoid Redundant|Bool**   * if `True` redundant auto-constraints are avoided.


{{TitleProperty|Grid}}

-    **Grid Auto Size|Bool|Hidden**   * if `True` the grid is resized based on the boundingbox of the geometry of the sketch.

-    **Grid Size|Length**   * the size of the spacing of the local grid lines in the [3D view](3D_view.md); it defaults to {{value|10 mm}}.

-    **Grid Snap|Bool**   * if `True` the grid can be used to snap points.

-    **Grid Style|Enumeration**   * the style of the grid lines; {{value|Dashed}} (default) or {{value|Light}}.

-    **Show Grid|Bool**   * if `True` a grid local to the object will be displayed in the [3D view](3D_view.md). This grid is independent of the [Draft Grid](Draft_ToggleGrid.md).

-    **Show Only In Edit Mode|Bool**   * if `True` the grid is only displayed while the sketch is being edited.

-    **Tight Grid|Bool**   * if `True` the local grid will be localized around the origin of the shape, otherwise it will extend itself more.

-    **max Number Of Lines|Integer**   * the maximum number of lines in the grid.


{{TitleProperty|Visibility automation}}

-    **Editing Workbench|String**   * name of the workbench to activate when editing the sketch; it defaults to {{value|SketcherWorkbench}}.

-    **Force Ortho|Bool**   * if `True` the camera will be forced to [orthographic view mode](Std_OrthographicCamera.md) when the sketch is opened.

-    **Hide Dependent|Bool**   * if `True` all objects that depend on the sketch are hidden when the sketch is opened.

-    **Restore Camera|Bool**   * if `True` the camera position is saved before opening the sketch, and is restored after closing it.

-    **Section View|Bool**   * if `True` only (parts of) objects behind the sketch plane are visible while the sketch is being edited.

-    **Show Links|Bool**   * if `True` all objects used in links to external geometry are shown when the sketch is opened.

-    **Show Support|Bool**   * if `True` all objects this sketch is attached to are shown when the sketch is opened.

-    **Tempo Vis|PythonObject|Hidden**   * a custom class associated with this object, that handles hiding and showing other objects when opening and closing the sketch.

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.

Ein Sketch-Objekt wird mit der `addObject()` Methode des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher   *   *SketchObject", "Sketch")
obj.Label = "Custom label"
```

For [Python](Python.md) subclassing you should create the `Sketcher   *   *SketchObjectPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher   *   *SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher_Tools_navi

}} {{Document_objects_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/de
