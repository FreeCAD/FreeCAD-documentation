---
- GuiCommand:
   Name:Surface GeomFillSurface
   MenuLocation:Surface → Fill boundary curves
   Workbenches:[Surface](Surface_Workbench.md)
   Version:0.17
---

# Surface GeomFillSurface/de

## Beschreibung


**<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Surface GeomFillSurface](Surface_GeomFillSurface.md)**

creates a parametric surface from two, three, or four boundary edges, trying to create a smooth transition between them.

<img alt="" src=images/Surface_GeomFillSurface_4_edges.png  style="width:330px;"> <img alt="" src=images/Surface_GeomFillSurface_4_edges_example.png  style="width:330px;">

<img alt="" src=images/Surface_GeomFillSurface_3_edges.png  style="width:330px;"> <img alt="" src=images/Surface_GeomFillSurface_3_edges_example.png  style="width:330px;">

<img alt="" src=images/Surface_GeomFillSurface_2_edges.png  style="width:330px;"> <img alt="" src=images/Surface_GeomFillSurface_2_edges_example.png  style="width:330px;">



*Left: edges that are used to generate a surface with the [GeomFillSurface](Surface_GeomFillSurface.md) tool, 4 connected edges, 3 connected edges, and 2 disconnected edges. Right: resulting surface from using the 4, 3, and 2 edges, respectively.*

## Anwendung

1.  Press the **<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Fill boundary curves](Surface_GeomFillSurface.md)** button.
2.  Select edges in the [3D view](3D_view.md). The edges must connect together so that they formed a closed profile.
3.  Press **OK**.


**Note:**

once created, it is not possible to apply additional constraints to the created surface.

## Optionen


**Fill type**

: {{RadioButton|TRUE|Stretch}}, {{RadioButton|TRUE|Coons}}, or {{RadioButton|TRUE|Curved}}.

## Eigenschaften

A _ (`Part::Feature` class, through the `Part::Spline` subclass), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Surface Filling has the following properties in the [property editor](Property_editor.md).

### Daten


{{TitleProperty|Base}}

-    **Fill Type|Enumeration**: the applied filling algorithm; Stretch, the style with the flattest patches; [{{Value|Coons}}](https://en.wikipedia.org/wiki/Coons_patch), a rounded style with less depth than Curved; Curved, the style with the most rounded patches.

-    **Boundary List|LinkSubList**: a list of edges that will be used to build the surface.

-    **Reversed List|BoolList|(hidden)**:

### Ansicht


{{TitleProperty|Base}}

-    **Control Points|Bool**: it defaults to `False`; if set to `True`, it will show an overlay with the control points of the surface.

## Twisting of the surface 

The shape of the surface depends on the direction of the chosen edges; if edges are selected and the result is a surface that \"twists\" on itself, one of the edges may need its list of vertices in the reverse order. A surface that twists on itself will probably have self-intersections, and thus will be an invalid <img src=images/Part_CheckGeometry.svg style="width:Shape](Part_TopoShape.md); this can be verified with **[16px"> [Part CheckGeometry](Part_CheckGeometry.md)**.

For example, if two curves have the points 
```python
curve1 = [a, b, c, d]
curve2 = [e, f, g]
``` and the resulting surface after using **<img src=images/Surface_GeomFillSurface.svg style="width:16px"> <img src=images/Surface_Sections.svg style="width:GeomFillSurface](Surface_GeomFillSurface.md)** or **[16px"> [Sections](Surface_Sections.md)** is a twisted surface, you may create a third curve that is equal to one of the two original curves but with a reversed list of points.

Either 
```python
curve1 = [a, b, c, d]
curve3 = [g, f, e]
```

or 
```python
curve3 = [d, c, b, a]
curve2 = [e, f, g]
``` should work to generate a surface that doesn\'t twist.

In practical terms this means that all edges used to generate a surface should be created preferably in the same clockwise or anti-clockwise direction. Following this simple rule usually guarantees that the surface will follow the smoothest direction and won\'t twist.

When the surface\'s **Lighting** property is {{Value|One side}}, a face will be painted completely black if its normal direction points into the [3D view](3D_view.md) (away from the current viewer), indicating a flipped face with respect to the other colored faces.

<img alt="" src=images/Surface_twisting_example_smooth.png  style="width:330px;"> <img alt="" src=images/Surface_twisting_example_twisted.png  style="width:330px;"> 
*Left: the boundary edges are oriented in the same direction, and thus the generated surface is smooth. Right: the boundary edges have opposite directions, and thus the generated surface twists on itself, resulting in self-intersections.*

## Skripten


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Surface GeomFillSurface tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by adding the `Surface::GeomFillSurface` object.

-   The edges to be used to define the surface must be assigned as a [LinkSubList](LinkSubList.md) to the `BoundaryList` property of the object.
-   The type of algorithm must be assigned like a string to the `FillType` property.
-   All objects with edges need to be computed before they can be used as input for the properties of the GeomFillSurface object.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-140, -100, 0)
b = App.Vector(175, -108, 0)
c = App.Vector(200, 101, 0)
d = App.Vector(-135, 107, 70)

points1 = [a, App.Vector(-55, -91, 65), App.Vector(35, -85, -5), b]
obj1 = Draft.make_bspline(points1)

points2 = [b, App.Vector(217, -45, 55), App.Vector(217, 35, -15), c]
obj2 = Draft.make_bspline(points2)

points3 = [c, App.Vector(33, 121, 55), App.Vector(0, 91, 15), App.Vector(-80, 121, -40), d]
obj3 = Draft.make_bspline(points3)

points4 = [d, App.Vector(-140, 0, 45), a]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::GeomFillSurface", "Surface")
surf.BoundaryList = [(obj1, "Edge1"),
                     (obj2, "Edge1"),
                     (obj3, "Edge1"),
                     (obj4, "Edge1")]
doc.recompute()
```





{{Surface Tools navi

}}

---
[documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface GeomFillSurface/de
