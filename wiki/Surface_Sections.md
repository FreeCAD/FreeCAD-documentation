---
- GuiCommand:
   Name:Surface Sections
   MenuLocation:Surface → Sections
   Workbenches:[Surface](Surface_Workbench.md)
   Version:0.19
---

# Surface Sections

## Description


**<img src=images/Surface_Sections.svg style="width:16px"> [Surface Sections](Surface_Sections.md)**

is used to create a surface from edges that represent transversal sections of a surface.

 <img alt="" src=images/Surface_Sections_edges_example.png  style="width:" height="250px;"> <img alt="" src=images/Surface_Sections_example.png  style="width:" height="250px;"> 



*Left: control edges (transversal sections). Right: surface produced from these edges.*

## Usage

1.  Make sure you have at lease two edges or curves in space. For example, these can be created with tools of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _.
2.  Press the **<img src=images/Surface_Sections.svg style="width:16px"> [Surface sections](Surface_Sections.md)** button.
3.  Press **Add edge**.
4.  Use the pointer to pick the desired edges in the [3D view](3D_view.md); a preview of the final shape will be shown after selecting two valid edges.
5.  Press **OK** to complete the operation.

## Options

-    **Add edge**: press once to start picking edges in the <img src=images/Draft_BSpline.svg style="width:3D view](3D_view.md). Individual lines such as **_** can be chosen, as well as any edge from solid objects, like those of **[16px"> <img src=images/Part_Primitives.svg style="width:PartDesign Bodies](PartDesign_Body.md)** and **[16px"> [Part Primitives](Part_Primitives.md)**.

-    **Remove edge**: press once to start picking edges in the [3D view](3D_view.md); these must be edges that were previously picked with **Add edge**.

-    **Right mouse button**: open the context menu and select **Remove**, or press **Del** in the keyboard, to remove the currently selected edge in the list.

-    **Drag**: drag the currently selected element in the list in order to change the order in which it will be processed; the list is processed from top to bottom.

-   Press **Cancel** or **Esc** to abort the current operation.

## Properties

A _ (`Part::Feature` class, through the `Part::Spline` subclass), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Surface Sections has the following properties in the [property editor](property_editor.md).

### Data


{{TitleProperty|Sections}}

-    **NSections|LinkSubList**: a list of edges that will be used to build the surface.

### View


{{TitleProperty|Base}}

-    **Control Points|Bool**: it defaults to `False`; if set to `True`, it will show an overlay with the control points of the surface.

## Twisting of the surface 

The shape of the surface depends on the direction of the chosen edges; if edges are selected and the result is a surface that \"twists\" on itself, one of the edges may need its list of vertices in the reverse order. See the information in **<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [GeomFillSurface](Surface_GeomFillSurface.md)** for a more complete explanation.

 <img alt="" src=images/Surface_twisting_example_smooth.png  style="width:330px;"> <img alt="" src=images/Surface_twisting_example_twisted.png  style="width:330px;"> 

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Surface Sections tool can be used in [macros](macros.md) and from the [Python](Python.md) console by adding the `Surface::Sections` object.

-   The edges to be used to define the surface must be assigned as a [LinkSubList](LinkSubList.md) to the `NSections` property of the object.
-   All objects with edges need to be computed before they can be used as input for the properties of the Sections object.

 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pl1 = App.Placement()
obj1 = Draft.make_circle(50, placement=pl1, face=False, startangle=0, endangle=180)

pl2 = App.Placement(App.Vector(0, 0, 25), App.Rotation())
obj2 = Draft.make_circle(30, placement=pl2, face=False, startangle=0, endangle=180)

points3 = [App.Vector(18, -10, 50),
           App.Vector(12, 10, 50),
           App.Vector(-12, 10, 50),
           App.Vector(-18, -10, 50)]
obj3 = Draft.make_bspline(points3)

points4 = [App.Vector(15, -20, 100),
           App.Vector(0, 6, 100),
           App.Vector(-15, -20, 100)]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Sections", "Surface")
surf.NSections = [(obj1, "Edge1"),
                  (obj2, "Edge1"),
                  (obj3, "Edge1"),
                  (obj4, "Edge1")]
doc.recompute()
```




 {{Surface Tools navi}}

---
[documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Sections
