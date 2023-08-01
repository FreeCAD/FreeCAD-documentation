---
- GuiCommand:
   Name:Surface Filling
   MenuLocation:Surface - Filling
   Workbenches:[Surface](Surface_Workbench.md)
   Version:0.17
---

# Surface Filling/pl

## Description


**[<img src=images/Surface_Filling.svg style="width:16px"> [Surface Filling](Surface_Filling.md)**

creates a surface from a series of connected boundary edges. The curvature of the surface can be additionally controlled by non-boundary edges and vertices, and a support surface.

The base geometry can belong to curves created with the [Draft Workbench](Draft_Workbench.md) or the [Sketcher Workbench](Sketcher_Workbench.md), but can also belong to solid objects such as those created with the [Part Workbench](Part_Workbench.md) or the [PartDesign Workbench](PartDesign_Workbench.md).

<img alt="" src=images/Surface_Filling_example.png  style="width:600px;"> 
*Two filled surfaces delimited by four edges located on the XY plane. The surface on the right is additionally controlled by a non-boundary edge.*

## Usage

1.  Press the **[<img src=images/Surface_Filling.svg style="width:16px"> [Filling](Surface_Filling.md)** button.
2.  The **Boundaries** task panel opens. See [Options](#Options.md).
3.  Select two or more edges in the [3D view](3D_view.md):
    -   There is no need to press the **Add edge** button in the **Boundaries** section at this time.
    -   The edges must be selected in consecutive order.
    -   The edges must be connected, but the complete boundary need not be closed.
    -   The complete boundary should not self-intersect.
    -   For a 360° circular boundary two semicircular edges can be selected.
4.  A preview of the final shape will be shown once enough valid geometry has been selected.
5.  Optionally select a **Support surface**. See [Example](#Example.md).
6.  Optionally select one or more **Edge constraints**.
7.  Optionally select one or more **Vertex constraints**.
8.  Press **OK** button.

## Options

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

## Properties

A [Surface Filling](Surface_Filling.md) (`Surface::Filling` class) is derived from the basic [Part Feature](Part_Feature.md) (`Part::Feature` class, through the `Part::Spline` subclass), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Surface Filling has the following properties in the [property editor](Property_editor.md).

### Data


{{TitleProperty|Filling}}

-    **Boundary Edges|LinkSubList**: boundary edges; C0 is required for edges without a corresponding face.

-    **Boundary Faces|StringList**:

-    **Boundary Order|IntegerList**: order of constraint on boundary faces; {{Value|0}}, {{Value|1}}, and {{Value|2}} are possible.

-    **Unbound Edges|LinkSubList**: unbound constraint edges; C0 is required for edges without a corresponding face.

-    **Unbound Faces|StringList**:

-    **Unbound Order|IntegerList**: order of constraint on unbound faces; {{Value|0}}, {{Value|1}}, and {{Value|2}} are possible.

-    **Free Faces|LinkSubList**: free constraint on a face.

-    **Free Order|IntegerList**: order of constraint on free faces.

-    **Points|LinkSubList**: constraint points on surface.

-    **Initial Face|LinkSub**: initial surface to use.

-    **Degree|Integer**: starting degree, it defaults to {{Value|3}}.

-    **Points On Curve|Integer**: number of points on an edge for constraint.

-    **Iterations|Integer**: number of iterations, it defaults to {{Value|2}}.

-    **Anisotropy|Bool**: it defaults to `False`.

-    **Tolerance2d|Float**: 2D tolerance, it defaults to {{Value|0.0}}.

-    **Tolerance3d|Float**: 3D tolerance, it defaults to {{Value|0.0}}.

-    **Tol Angular|Float**: G1 tolerance, it defaults to {{Value|0.01}}.

-    **Tol Curvature|Float**: G2 tolerance, it defaults to {{Value|0.10}}.

-    **Maximum Degree|Integer**: maximum curve degree, it defaults to {{Value|8}}.

-    **Maximum Segments|Integer**: maximum number of segments, it defaults to {{Value|9}}.

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
![](images/Button_right.svg) [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Filling/pl
