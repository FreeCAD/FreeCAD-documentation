---
- GuiCommand:/es
   Name:Draft Shape2DView
   Name/es:Draft Shape2DView
   MenuLocation:Boceto → Vista de forma 2D
   Workbenches:[Boceto](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
---

# Draft Shape2DView/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta coloca en el documento un objeto 2D que es una vista aplanada de un objeto seleccionado [Shape](Part_Workbench/es.md), proyectado a lo largo de la dirección de vista actual.


</div>

Draft Shape2DView projections can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) command. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own projection commands. But these create projections that are only displayed on the drawing page and not in the [3D view](3D_view.md).

![](images/Draft_Shape2DView_example.jpg ) 
*Projection of solid shapes onto the XY plane*

## Utilización


<div class="mw-translate-fuzzy">

1.  Selecciona el objeto que quieres extraer a una vista 2D
2.  Presiona el botón **<img src="images/Draft_Shape2DView.png" width=16px> [Vista de forma 2D](Draft_Shape2DView/es.md)
**


</div>

## How to produce plans and sections with different linewidths 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Drawings with different linewidths for viewed and cut lines can easily be produced by using two shape2Dview objects from a same [Arch SectionPlane](Arch_SectionPlane.md). One of the shape2Dview objects has its projection mode set to **Solid**, which renders the viewed lines, and another set to **Cut lines** or **Cut faces** to render the cut lines. The two shape2Dviews are then placed at the same location, one on top of the other.

## Propiedades

See also: [Property editor](property_editor.md).

A Draft Shape2DView object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Projection**: La dirección de la proyección

-    **Projection Mode**: El modo de la proyección: sólido, caras individuales o líneas de corte.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta de vista 2D de forma se puede utilizar en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```


<div class="mw-translate-fuzzy">

-   Añade una forma 2D al documento, la cual es una proyección 2D del objeto dado.
-   Se puede indicar un vector de proyección específico.
-   Devuelve el objeto generado.
-   También puedes proporcionar una lista de números de caras a considerar.


</div>

Change the `ProjectionMode` property of the created object if required. It can be: `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` or `"Solid faces"`.

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/es
