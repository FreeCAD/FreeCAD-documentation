---
- GuiCommand   *
   Name   *Draft Shape2DView
   MenuLocation   *Modification → Shape 2D view
   Workbenches   *[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso   *[TechDraw ProjectShape](TechDraw_ProjectShape.md)
---

# Draft Shape2DView/en

## Description

The <img alt="" src=images/Draft_Shape2DView.svg  style="width   *24px;"> **Draft Shape2DView** command creates 2D projections from selected objects, usually 3D solids or [Arch SectionPlanes](Arch_SectionPlane.md). The projections are placed in the [3D view](3D_view.md).

Draft Shape2DView projections can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) command. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own projection commands. But these create projections that are only displayed on the drawing page and not in the [3D view](3D_view.md).

![](images/Draft_Shape2DView_example.jpg ) 
*Projection of solid shapes onto the XY plane*

## Usage

1.  Optionally rotate the [3D view](3D_view.md). The camera direction in the [3D view](3D_view.md) determines the projection vector. For example, a [top view](Std_ViewTop.md) will project onto the XY plane. The projection vector is ignore for projections created from [Arch SectionPlanes](Arch_SectionPlane.md).
2.  Optionally select one or more objects.
3.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_Shape2DView.svg" width=16px> [Draft Shape2DView](Draft_Shape2DView.md)** button.
    -   Select the **Modification → <img src="images/Draft_Shape2DView.svg" width=16px> Shape 2D view** option from the menu.
4.  If you have not yet selected an object   * select an object in the [3D view](3D_view.md).
5.  The projected objects are created on the XY plane.

## How to produce plans and sections with different linewidths 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width   *700px;">

Drawings with different linewidths for viewed and cut lines can easily be produced by using two shape2Dview objects from a same [Arch SectionPlane](Arch_SectionPlane.md). One of the shape2Dview objects has its projection mode set to **Solid**, which renders the viewed lines, and another set to **Cut lines** or **Cut faces** to render the cut lines. The two shape2Dviews are then placed at the same location, one on top of the other.

## Properties

See also   * [Property editor](Property_editor.md).

A Draft Shape2DView object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}

-    **Auto Update|Bool**   * specifies if the projection should be automatically recomputed if the **Base** object changes. Selecting {{False}} can be useful if there are many Draft Shape2DViews in a document or if they are complex. If set to {{False}} the [Std Refresh](Std_Refresh.md) command must be used to update the projection. <small>(v0.20)</small> 

-    **Base|Link**   * specifies the object to be projected.

-    **Face Numbers|IntegerList**   * specifies the indices of the faces to be projected. Only works if **Projection Mode** is {{Value|Individual Faces}}.

-    **Fuse Arch|Bool**   * specifies if [Arch objects](Arch_Workbench.md) of the same type and material are fused or not.

-    **Hidden Lines|Bool**   * specifies if hidden lines are shown or not.

-    **In Place|Bool**   * only works if the selected object is an [Arch SectionPlane](Arch_SectionPlane.md), and **Projection Mode** is {{Value|Cutlines}} or {{Value|Cutfaces}}, specifies if the projection will appear co-planar with the section plane.

-    **Projection|Vector**   * specifies the direction of the projection. Ignored if **Base** is an [Arch SectionPlane](Arch_SectionPlane.md).

-    **Projection Mode|Enumeration**   * specifies the projection mode. The following modes are available   *

    -   
        {{Value|Solid}}
        
           * projects the entire selected object.

    -   
        {{Value|Individual Faces}}
        
           * only projects the faces in the **Face Numbers** list.

    -   
        {{Value|Cutlines}}
        
           * only works if the selected object is an [Arch SectionPlane](Arch_SectionPlane.md), projects only the edges cut by the section plane.

    -   
        {{Value|Cutfaces}}
        
           * only works if the selected object is an [Arch SectionPlane](Arch_SectionPlane.md), projects the areas cut through solids by the section plane as faces.

    -   
        {{Value|Solid faces}}
        
           * projects the entire selected object by cutting faces one by one. Can be used if the {{Value|Solid}} mode gives wrong results. <small>(v0.20)</small> 

-    **Segment Length|Float**   * specifies the size in millimeters of linear segments if **Tessellation** is `True`.

-    **Tessellation|Bool**   * specifies if tessellation should be performed. Tessellation means that curves are replaced by sequences of line segments. This can be computationally intensive if the **Segment Length** is too short.

-    **Visible Only|Bool**   * specifies if the projection should only be recomputed if it is visible.

-    **Exclusion Points|Vector list**   * A list of exclusion points. Any edge passing through any of those points will not be drawn. <small>(v0.20)</small> 

-    **Exclusion Names|String list**   * A list of object names. Any viewed or cut child object with a name in that list will not be drawn. <small>(v1.0)</small> 

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**   * not used.

-    **Pattern Size|Float**   * not used.

## Scripting

See also   * [Autogenerated API documentation](https   *//freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a 2D projection use the `make_shape2dview` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeShape2DView` method.


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```

-    `baseobj`is the object to be projected.

-    `projectionVector`is the projection vector. If not supplied the Z axis is used.

-    `facenumbers`is a list of face numbers (0-based). If supplied only these faces are considered.

-    `shape2dview`is returned with the created 2D projection.

Change the `ProjectionMode` property of the created object if required. It can be   * `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` or `"Solid faces"`.

Example   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part   *   *Box", "Box")
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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/en
