---
- GuiCommand:/cs   Name:Draft_Shape2DView   Name/cs:Kreslení TělesoDo2DPohledu   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> TělesoDo2D---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj umístí do dokumentu 2D objekt, který vznikne zploštěním pohledu vybraného tvaru založeného na objektu [díl](Part_Workbench/cs.md).


</div>

Draft Shape2DView projections can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) command. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own projection commands. But these create projections that are only displayed on the drawing page and not in the [3D view](3D_view.md).

![](images/Draft_Shape2DView_example.jpg ) *Projection of solid shapes onto the XY plane*

## Použití


<div class="mw-translate-fuzzy">

1.  Vyberte objekt, ze kterého chcete extrahovat 2D pohled
2.  Stiskněte tlačítko **<img src="images/Draft_Shape2DView.png" width=16px> [Kreslení TělesoDo2D](Draft_Shape2DView/cs.md)
**


</div>

## How to produce plans and sections with different linewidths {#how_to_produce_plans_and_sections_with_different_linewidths}

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Drawings with different linewidths for viewed and cut lines can easily be produced by using two shape2Dview objects from a same [Arch SectionPlane](Arch_SectionPlane.md). One of the shape2Dview objects has its projection mode set to **Solid**, which renders the viewed lines, and another set to **Cut lines** or **Cut faces** to render the cut lines. The two shape2Dviews are then placed at the same location, one on top of the other.

## Vlastnosti

See also: [Property editor](property_editor.md).

A Draft Shape2DView object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Projection**: Směr projekce.

-    **Projection Mode**: Projekční mód: těleso, individuální plochy nebo řezné čáry.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj TělesoDo2D může být použit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```


<div class="mw-translate-fuzzy">

-   Přidá 2D tvar do dokumentu, tvar je 2D projekce zadaného objektu.
-   Může být specifikován projekční vektor.
-   Vrací vygenerovaný objekt.
-   Může být zadán seznam čísel ploch, které mají být použity.


</div>

Change the `ProjectionMode` property of the created object if required. It can be: `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` or `"Solid faces"`.

Příklad:


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





 
