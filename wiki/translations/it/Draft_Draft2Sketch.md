---
- GuiCommand:/it
   Name:Draft Draft2Sketch
   Name/it:Da Draft a Sketch
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Da Draft a Sketch
   SeeAlso:[Sketcher](Sketcher_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md)
---

# Draft Draft2Sketch/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:16px;"> [Da Draft a Sketch ](Draft_Draft2Sketch/it.md) converte gli [oggetti di Draft](Draft_Workbench/it.md) in [oggetti di Sketcher](Sketcher_Workbench/it.md), e viceversa.


</div>

![](images/Draft_Draft2Sketch_example.png )


<div class="mw-translate-fuzzy">



*Conversione di forme Draft in forme di Sketcher con vincoli*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto di Draft o di Sketcher.
2.  Premere il pulsante **<img src="images/Draft_Draft2Sketch.svg" width=16px> Da Draft a Sketcher**.


</div>

## Notes


<div class="mw-translate-fuzzy">

### Limitazioni

La conversione di un oggetto che non può essere rappresentato con una combinazione di linee rette, archi e B-Spline di solito fallisce, cioè l\'oggetto non appare nello schizzo.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Convertire oggetti in schizzo:


</div>


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


<div class="mw-translate-fuzzy">

Convertire oggetti in Draft:


</div>


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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Draft2Sketch/it
