---
- GuiCommand:
   Name:Arch SectionPlane
   MenuLocation:Arch → Section Plane
   Workbenches:[Arch](Arch_Workbench.md)
   Shortcut:**S** **P**
   SeeAlso:[Draft Shape2DView](Draft_Shape2DView.md), [TechDraw ArchView](TechDraw_ArchView.md)
---

# Arch SectionPlane

## Description

This tool places in the current document a section plane \"thing\", which defines a section or view plane. The \"thing\" takes its placement according to the current [Draft Working Plane](Draft_SelectPlane.md) and can be relocated and reoriented by moving and rotating it, until it describes the 2D view you want to obtain. The Section plane object will only consider a certain set of objects. Objects that are selected when you create a Section Plane will be added to that set automatically. Other objects can later be added or removed from a SectionPlane object with the [Arch Add component](Arch_Add.md) and [Arch Remove component](Arch_Remove.md) tools, or by double-clicking the Section Plane in the tree view.

The Section Plane alone won\'t create any view of its objects set. For that, you must create a [TechDraw ArchView](TechDraw_ArchView.md) to create a view in a [TechDraw page](TechDraw_Workbench.md).

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">

## Usage

1.  Optionally, set the [Draft Working Plane](Draft_SelectPlane.md) to reflect the plane where you want to place the Section Plane.
2.  Select objects you want to be included in your section view.
3.  Press the **<img src="images/Arch_SectionPlane.svg" width=16px> [Section Plane](Arch_SectionPlane.md)** button or press **S** then **P** keys.
4.  [Move](Draft_Move.md)/[rotate](Draft_Rotate.md) the Section Plane into correct position if needed.
5.  Select the Section Plane if not selected already.
6.  Use either [Draft Shape2DView](Draft_Shape2DView.md) or [TechDraw ArchView](TechDraw_ArchView.md) to create a view.

## Options

-   The Section plane object will only consider a certain set of objects, not all the objects of the document. Objects can be added or removed from a SectionPlane object by using the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools, or by double-clicking the Section Plane in the tree view, selecting objects either in the list of in the 3D scene, and pressing the **add** or **remove** buttons.

-   With a section plane object selected, use the [Draft Shape2DView](Draft_Shape2DView.md) tool to create a shape object representing the section view in the document

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Create [Drawing DraftViews](Draft_Drawing.md) if you are working with the [Drawing Workbench](Drawing_Workbench.md), or [TechDraw ArchView](TechDraw_ArchView.md) if you are using the [TechDraw Workbench](TechDraw_Workbench.md).

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   The Section Plane can also be used to show the entire 3D view cut by an infinite plane. This is only visual, and won\'t affect the geometry of the objects being cut.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">

## Properties

-    **Only Solids**: If this is True, non-solid objects in the set will be disregarded

-    **Display Length**: The length of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Display Height**: The height of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Arrow Size**: The size of the arrows of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Cut View**: If this is `True`, the whole 3D view will be cut at the location of this section plane.

-    **Clip view**: if this is `True`, it will clip the view to the display height and length of the section plane. This effectively turns the section plane into an orthographic camera, limiting the field of view. <small>(v0.19)</small> 

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App::PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements. <small>(v0.19)</small> 

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The SectionPlane tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:

 
```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Creates a `Section` object from `objectslist`, which is a list of objects.

Example:

 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SectionPlane
