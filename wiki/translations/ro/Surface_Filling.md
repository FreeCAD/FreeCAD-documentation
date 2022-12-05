# Surface Filling/ro
---
- GuiCommand:   Icon:Filling.svg   Name:Surface Filling   MenuLocation:Surface → Filling...   Workbenches:[Surface](Surface_Workbench.md)|---


</div>

## Descriere


**[<img src=images/Surface_Filling.svg style="width:16px"> [Surface Filling](Surface_Filling.md)**

creates a surface from a series of connected boundary edges. The curvature of the surface can be additionally controlled by non-boundary edges and vertices, and a support surface.

The base geometry can belong to curves created with the [Draft Workbench](Draft_Workbench.md) or the [Sketcher Workbench](Sketcher_Workbench.md), but can also belong to solid objects such as those created with the [Part Workbench](Part_Workbench.md) or the [PartDesign Workbench](PartDesign_Workbench.md).

<img alt="" src=images/Surface_Filling_example.png  style="width:600px;"> 
*Two filled surfaces delimited by four edges located on the XY plane. The surface on the right is additionally controlled by a non-boundary edge.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  apăsați butonul **[<img src=images/Filling.svg style="width:24px"> '''Surface filling...'''** button.
2.  Detalierea pașilor este necesară.
3.  Definiți opțiunile și apăsați **OK**.


</div>

## Opţiuni

-   In the **Boundaries** section a support surface and boundary edges can specified:
    -   Press the **Support surface** button and select a face in the [3D view](3D_view.md) to add a support surface.
        -   Click the <img alt="" src=images/Edit-cleartext.svg  style="width:16px;"> icon to remove the support surface.
    -   Press the **Add edge** button once to start selecting boundary edges in the [3D view](3D_view.md).
    -   There are several ways to deselect boundary edges:
        -   Press the **Remove edge** button once to start deselecting edges in the [3D view](3D_view.md).
        -   Select an edge in the list and press **Delete**.
        -   Right-click an edge in the list and select **Remove** from the context menu.

-   In the **Edge constraints** section non-boundary edges can be specified:
    -   The selection options are similar to those for boundary edges.

-   In the **Vertex constraints** section non-boundary vertices can be specified:
    -   The selection options are similar to those for boundary edges.

-   Press **Esc** or the **Cancel** button to abort the operation.

## Example

The **Support surface** acts as an additional constraint for the surface. The following simple example will give you an idea how this works:

1.  In the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) create a <img alt="" src=images/Part_Cylinder.svg  style="width:16px;">[cylinder](Part_Cylinder.md) and set its **Angle** to {{Value|180°}}.
2.  Switch to the <img alt="" src=images/Workbench_Surface.svg  style="width:16px;"> [Surface Workbench](Surface_Workbench.md) and press the **[<img src=images/Surface_Filling.svg style="width:16px"> [Filling](Surface_Filling.md)** button.
3.  Select the two semi-circular edges and the two straight edges that connect them.
4.  The result matches the four boundary edges, but the inner shape is quite different from the cylindrical face.
5.  Edit the Surface object and for the **Support surface** select the cylindrical face.
6.  The modified shape matches the cylindrical face much more closely.

## Proprietăți

A [Surface Filling](Surface_Filling.md) (`Surface::Filling` class) is derived from the basic [Part Feature](Part_Feature.md) (`Part::Feature` class, through the `Part::Spline` subclass), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Surface Filling has the following properties in the [property editor](Property_editor.md).

### Data


{{TitleProperty|Filling}}


<div class="mw-translate-fuzzy">

-    **Property**: descrierea proprietăților

-    **Property**: descrierea proprietăților


</div>

### View


{{TitleProperty|Base}}

-    **Control Points|Bool**: it defaults to `False`; if set to `True`, it will show an overlay with the control points of the surface.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Surface Filling tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by adding the `Surface::Filling` object.

-   The edges to be used to define the surface must be assigned as a [LinkSubList](LinkSubList.md) to the `BoundaryEdges` property of the object.
-   Auxiliary edges and vertices must be assigned as a [LinkSubLists](LinkSubList.md) to the `UnboundEdges` and `Points` properties of the object.
-   All objects with edges need to be computed before they can be used as input for the properties of the Filling object.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-20, -20, 0)
b = App.Vector(-18, 25, 0)
c = App.Vector(60, 26, 0)
d = App.Vector(33, -20, 0)

points1 = [a, App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), b]
obj1 = Draft.make_bspline(points1)

points2 = [b, App.Vector(0, 25, 0), c]
obj2 = Draft.make_bspline(points2)

points3 = [c, App.Vector(37, 4, 0), d]
obj3 = Draft.make_bspline(points3)

points4 = [d, App.Vector(-2, -18, 0), a]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Filling", "Surface")
surf.BoundaryEdges = [(obj1, "Edge1"),
                      (obj2, "Edge1"),
                      (obj3, "Edge1"),
                      (obj4, "Edge1")]
doc.recompute()

# 
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# 
aux_v1 = Draft.make_line(App.Vector(-13, -12, 5),
                         App.Vector(-13, -12, -5))
aux_v2 = Draft.make_line(App.Vector(-3, 18, 5),
                         App.Vector(-3, 18, -5))
doc.recompute()

surf.Points = [(aux_v1, "Vertex2"),
               (aux_v2, "Vertex1")]
doc.recompute()
```





{{Surface Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Filling/ro
