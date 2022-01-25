# Draft Draft2Sketch/cs
---
- GuiCommand:/cs   Name:Draft_Draft2Sketch   Name/cs:Kreslení Kreslení2Náčrt   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> Nákres do Náčrtu---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Tento nástroj konvertuje [objekty Kreslení](Draft_Workbench/cs.md) do [objektu Náčrt](Sketcher_Workbench/cs.md) a naopak.


</div>

![](images/Draft_Draft2Sketch_example.png )


<div class="mw-translate-fuzzy">

![\|480px](images/Draft_Draft2Sketch_example.jpg )


</div>

## Usage


<div class="mw-translate-fuzzy">

## Použití

1.  Vyberte objekt Kreslení nebo Náčrt
2.  Stiskněte tlačítko **<img src="images/Draft_Draft2Sketch.png" width=16px> [Kreslení2Náčrt](Draft_Draft2Sketch/cs.md)
**


</div>

## Notes

-   Non-Draft objects that are totally planar can also be converted.
-   The command can only handle objects made up out of straight lines, circular arcs, elliptical arcs, B-Splines and Bézier curves.
-   [Draft BezCurves](Draft_BezCurve.md) will be approximated by [Sketcher BSplines](Sketcher_CreateBSpline.md).
-   The external [KicadStepUp Workbench](KicadStepUp_Workbench.md) contains a command to convert a [Draft BSpline](Draft_BSpline.md) into a series of [Sketcher Arcs](Sketcher_CreateArc.md). For more information see the forum topic [BSplines to Shape2DView and Sketcher](https://forum.freecadweb.org/viewtopic.php?f=9&t=25082).
-   [This other forum topic](https://forum.freecadweb.org/viewtopic.php?f=3&t=58781#p505207) contains a macro for such a conversion.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Není dostupné, podívejte se na dokumentaci [Modulu Náčrt](Sketcher_Workbench/cs.md) jak vytvořit náčrt pomocí skriptování.


</div>

To convert objects to a sketch use the `make_sketch` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeSketch` method.


```python
sketch = make_sketch(objects_list, autoconstraints=False, addTo=None, delete=False, name="Sketch", radiusPrecision=-1, tol=1e-3)
```

-    `objects_list`contains the objects to be converted. It is either a single object or a list of objects. `Draft` objects, `Part::Feature` objects and `Part.Shape` objects are supported.

-   If `autoconstraints` is `True` coincident constraints are added to nodes belonging to the same source object.

-    `addTo`is the existing sketch object the geometry is added to. If not supplied a new sketch is created.

-   If `delete` is `True` the source objects are deleted.

-    `name`is the name for the new sketch.

-    `radiusPrecision`indicates how radius constraints should be handled:

    -   Use `-1` to disable radius constraints.
    -   Use `0` to add individual radius constraints.
    -   Use a positive number to round radii according to this precision, and to add equal constraints between curves with equal radii.

-    `tol`is the tolerance used to check if shapes are planar and co-planar. Use `-1` for a strict analysis.

-    `sketch`is returned with the sketch object.

To convert a sketch to Draft objects use the `draftify` method of the Draft module.


```python
draftify(objectslist, makeblock=False, delete=True)
```

-    `objectslist`contains the objects to be converted. It is either a single object or a list of objects.

-   If `makeblock` is `True` the converted objects are grouped in a `Part::Part2DObject`.

-   If `delete` is `True` the source objects are deleted.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(2000, 1000)
circle = Draft.make_circle(500)
doc.recompute()

sketch_from_draft = Draft.make_sketch([rectangle, circle], autoconstraints=True, delete=False, radiusPrecision=0)
doc.recompute()

draft_from_sketch = Draft.draftify(sketch_from_draft, delete=False)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Draft2Sketch/cs
