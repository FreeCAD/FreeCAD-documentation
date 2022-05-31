# Sketcher SketchObject/pl
{{TOCright}}

## Wprowadzenie

<img alt="" src=images/Sketcher_Sketch.svg  style="width   *32px;">

Obiekt [SketchObject](Sketcher_SketchObject/pl.md), lub formalnie `Sketcher   *   *SketchObject`, jest podstawowym elementem do tworzenia obiektów 2D za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).

Obiekt `Sketcher   *   *SketchObject` wywodzi się z obiektu [Part2DObject](Part_Part2DObject/pl.md), co oznacza, że jest to obiekt [Cecha](Part_Feature/pl.md) wyspecjalizowany dla geometrii 2D. Podobnie jak obiekt Part2DObject, obiekt SketchObject może być dołączany do płaszczyzn i powierzchni. Ponadto obiekt SketchObject może obsługiwać wiązania geometryczne.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*

## Użycie

1.  Przejdź do środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).
2.  Naciśnij przycisk **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Utwórz szkic](Sketcher_NewSketch/pl.md)**.
3.  Wybierz **orientację szkicu** jako   * Płaszczyzna XY, Płaszczyzna XZ lub Płaszczyzna YZ. Opcjonalnie wybierz także opcję **Odwróć kierunek** i podaj wartość **Odsunięcia**.
4.  Naciśnij przycisk **OK**.

Although the SketchObject can be used by itself to draw on a plane, it is most commonly used in conjunction with the [PartDesign Workbench](PartDesign_Workbench.md) to create extruded solids.

1.  Switch to the [PartDesign Workbench](PartDesign_Workbench.md).

2.  Press **[<img src=images/PartDesign_Body.svg style="width   *16px"> [PartDesign Body](PartDesign_Body.md)**.

3.  Press **[<img src=images/PartDesign_NewSketch.svg style="width   *16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**.

4.  
    **Select feature**   * XY\_Plane (Base plane), XZ\_Plane (Base plane), or YZ\_Plane (Base plane).

5.  Press **OK**.

## Properties

See [Property](Property.md) for all property types that scripted objects can have.

The [Sketcher SketchObject](Sketcher_SketchObject.md) (`Sketcher   *   *SketchObject` class) is derived from the [Part Part2DObject](Part_Part2DObject.md) (`Part   *   *Part2DObject` class) and inherits all its properties.

The Sketcher SketchObject also has the following additional properties in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Sketch}}

-    **Geometry|GeometryList|Hidden**   * a list of Part geometries that exist inside the sketch.

-    **Constraints|**   * named constraints, if they exist; otherwise it is an empty list `[]`.

-    **External Geometry|LinkSubList**   * a list of Part geometries outside this Sketch that are used for reference.

-    **Fully Constrained|Bool|Hidden**   * (read-only) if `True` the sketch is fully constrained.

### View


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

## Tworzenie skryptów 


**Zobacz również   ***

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część   * właściwość](Part_Feature/pl.md).

Obiekt *SketchObject* jest tworzony za pomocą metody dokumentu `addObject()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher   *   *SketchObject", "Sketch")
obj.Label = "Custom label"
```

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `Sketcher   *   *SketchObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher   *   *SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher_Tools_navi

}} {{Document_objects_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/pl
