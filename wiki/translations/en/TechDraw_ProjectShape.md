---
- GuiCommand:
   Name:TechDraw ProjectShape
   MenuLocation:TechDraw - TechDraw Views - Project shape...
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Shortcut:
   Version:0.20
   SeeAlso:[Draft Shape2DView](Draft_Shape2DView.md)
---

# TechDraw ProjectShape/en

## Description

The **TechDraw ProjectShape** tool creates projections of shapes. The projections are created in the [3D view](3D_view.md), and not on a [TechDraw Page](TechDraw_PageDefault.md).

![](images/ProjectShape1_it.png )

## Usage

1.  Optionally rotate the [3D view](3D_view.md). The objects will be projected onto a plane parallel to the screen i.e. along the 3D view\'s camera direction, which is used as the default **Direction** property.
2.  Select one or more objects. For each object a separate projection will be created.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ProjectShape.svg" width=16px> [Project shape...](TechDraw_ProjectShape.md)** button.
    -   Select the **TechDraw → TechDraw Views → <img src="images/TechDraw_ProjectShape.svg" width=16px> Project shape...** option from the menu.
4.  The **Project shapes** task panel opens. See [Properties](#Properties.md).
5.  Set the desired options.
6.  The selected options should not result in an empty projection as this will cause an error. For example, for an object with only sharp edges such as a [Part Box](Part_Box.md), the **Visible sharp edges** and/or **Hidden sharp edges** option must be checked.
7.  Press the **OK** button.
8.  The projection is placed on the XY plane.
9.  Optionally change the **Placement** property and/or **Direction** property of the projection.

## Properties

A Projection object is derived from a [Part Feature](Part_Feature.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Projection}}

-    **Source|Link**: The shape to project.

-    **Direction|Vector**: The direction of the projection. This is the normal vector of the projection plane.

-    **VCompound|Bool**: If `True`, visible sharp edges are shown. Example: all edges of a [Part Box](Part_Box.md).

-    **Rg1 Line VCompound|Bool**: If `True`, visible smooth edges are shown. Example: the edges between a fillet and its adjoining faces.

-    **Rg NLine VCompound|Bool**: If `True`, visible sewn edges are shown. Example: the seam of a 360° cylindrical face.

-    **Out Line VCompound|Bool**: If `True`, visible outline edges (that are not sharp) are shown. Example: the side view of a [Part Cylinder](Part_Cylinder.md) has two such edges.

-    **Iso Line VCompound|Bool**: If `True`, visible isoparameters are shown. Does not work currently.

-    **HCompound|Bool**: If `True`, hidden sharp edges are shown.

-    **Rg1 Line HCompound|Bool**: If `True`, hidden smooth edges are shown

-    **Rg NLine HCompound|Bool**: If `True`, hidden sewn edges are shown.

-    **Out Line HCompound|Bool**: If `True`, hidden outline edges are shown.

-    **Iso Line HCompound|Bool**: If `True`, hidden isoparameters are shown. Does not work currently.

## Notes

This tool was previously available in the Drawing Workbench.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectShape/en
