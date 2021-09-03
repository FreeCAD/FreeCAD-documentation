---
- GuiCommand:
   Name:Surface Filling
   MenuLocation:Surface → Filling
   Workbenches:[Surface](Surface_Workbench.md)
   Version:0.17
---

## Description


**<img src=images/Surface_Filling.svg style="width:16px"> [Surface Filling](Surface_Filling.md)**

creates a surface from a series of connected boundary edges.

The surface can be modified by adding constraint edges and vertices which the surface must pass through.

 <img alt="" src=images/Surface_Filling_example.png  style="width:600px;"> 


*Example of a filled surface, delimited by four edges located in the XY plane; (left) only the four edges, and (right) one additional curve in space that defines the curvature of the surface*

## Usage

1.  Make sure you have at lease three edges or curves in space forming a closed contour. For example, these can be created with tools of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) or the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench.md). Using three edges would create a triangular surface; four edges a quadrilateral surface.
    -   Optionally, curves can be drawn inside the closed contour, not necessarily touching the edges. These curves can be used to control the curvature of the resulting surface.
    -   Likewise, a number of vertices can be used with the same purpose to indicate where the surface must go through.
2.  Press the **<img src=images/Surface_Filling.svg style="width:16px"> [Surface filling](Surface_Filling.md)** button.
3.  Inside the **Boundary** section, press **Add edge**.
4.  Use the pointer to pick the desired edges in the [3D view](3D_view.md); a preview of the final shape will be shown after selecting valid edges that form a closed contour.
    -   Optionally, go to the **Curvature: non-boundary edges** section, press **Add edge**, and pick the desired edges from the [3D view](3D_view.md).
    -   Optionally, go to the **Curvature: non-boundary vertices** section, press **Add vertex**, and pick the desired vertices from the [3D view](3D_view.md).
5.  Press **OK** to complete the operation.

The base edges that form the closed contour, as well as the auxiliary vertices and edges, can belong to 2D curves from <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench.md) or the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench.md), but can also belong to 3D solid objects such as those created with the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) or <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbenches](PartDesign_Workbench.md).

## Options

-    **Boundary**section:

    -   
        **Add edge**
        
        : press once to start picking **Boundary edges** in the <img src=images/Draft_Wire.svg style="width:3D view](3D_view.md). Straight edges such as **[16px"> <img src=images/Sketcher_CreatePolyline.svg style="width:Draft Wires](Draft_Wire.md)** and **[16px"> <img src=images/Draft_BSpline.svg style="width:Sketcher Polylines](Sketcher_CreatePolyline.md)**, or curved edges such as **[16px"> <img src=images/Sketcher_CreateBSpline.svg style="width:Draft BSplines](Draft_BSpline.md)** and **[16px"> <img src=images/PartDesign_Body.svg style="width:Sketcher BSplines](Sketcher_CreateBSpline.md)** can be chosen, as well as any edge from solid objects, like those of **[16px"> <img src=images/Part_Primitives.svg style="width:PartDesign Bodies](PartDesign_Body.md)** and **[16px"> [Part Primitives](Part_Primitives.md)**.

    -   
        **Remove edge**
        
        : press once to start picking edges in the [3D view](3D_view.md); these edges must have been previously picked with **Add edge**.

    -   
        **Right mouse button**
        
        : open the context menu and select **Remove**, or press **Del** in the keyboard, to remove the currently selected edge in the list.

-    **Curvature: non-boundary edges**section; the **Add edge** button is available to pick auxiliary edges (straight lines or B-Splines) to control the curvature of the surface. The surface will be forced to pass through these auxiliary edges. This works best when the auxiliary edges lie inside the region delimited by the **Boundary edges**.

-    **Curvature: non-boundary vertices**section; similar to the non-boundary edges, the user can pick auxiliary vertices to control the curvature. These vertices may be free standing **<img src=images/Draft_Point.svg style="width:16px"> <img src=images/Part_Point.svg style="width:Draft Points](Draft_Point.md)** or **[16px"> [Part Points](Part_Point.md)**, or may belong to any edge (straight lines or B-Splines), or be a corner vertex in a solid object. In this case, the surface will be constrained to pass through these auxiliary points.

-   Press **Cancel** or **Esc** to abort the current operation.

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

## Limitations

The surface code from the internal [OpenCASCADE](OpenCASCADE.md) modelling kernel is fragile, and cannot handle wrong input properly. The following situations may cause problems, and may crash the program, so they should be avoided:

-   Adding **Boundary Edges** to that would result in several closed faces. In this case, those edges should be added as **Unbound Edges** to control the curvature only.
-   Using parametric **Boundary Edges** (for example, **<img src=images/Draft_BSpline.svg style="width:16px"> [Draft BSplines](Draft_BSpline.md)**) that when recomputed fail to produce a closed boundary. That is, the edges to be used as **Boundary Edges** must always form a closed shape, even if their internal properties change.

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

# ---------------------------------------------------------
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# ---------------------------------------------------------
aux_v1 = Draft.make_line(App.Vector(-13, -12, 5),
                         App.Vector(-13, -12, -5))
aux_v2 = Draft.make_line(App.Vector(-3, 18, 5),
                         App.Vector(-3, 18, -5))
doc.recompute()

surf.Points = [(aux_v1, "Vertex2"),
               (aux_v2, "Vertex1")]
doc.recompute()
```




 {{Surface Tools navi}} 
