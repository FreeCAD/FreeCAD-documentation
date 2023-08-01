# Part Revolve/sv
---
- GuiCommand:/sv   Name:Part Revolve   Name/sv:Part Revolve/sv   MenuLocation:Part → Revolve   Workbenches:[[Part_Workbench/sv   Part]], Complete|SeeAlso:---


</div>

## Description

Revolves the selected object around a given axis. The following shape types are allowed, and lead to the listed output shapes:

  Input shape   Output shape
   
  Vertex        Edge
  Edge          Face
  Wire          Shell
  Face          Solid
  Shell         Compound solid (Compsolid)

A [Sketch](Sketcher_Workbench.md) can be used as well. Solids or compound solids are not allowed as input shapes. Normal compounds are currently not allowed either.


<div class="mw-translate-fuzzy">

![](images/Dialog-revolve.jpg )


</div>

The Angle argument specifies how far the object is to be turned. The coordinates move the origin of the axis of revolving, relative to the origin of the coordinate system.

If you select a user defined axis, the numbers define the direction of the revolving axis with respect to the coordinate system: If the Z coordinate is 0 and the Y and X coordinate are non-zero, then the axis will lie in the X-Y-plane. Its angle is such that its tangent is the ratio of the given X and Y coordinates.

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types can also be used as shapes and to specify the axis. <small>(v0.20)</small> 
-   If the object to revolve intersects the rotation axis the operation will fail in most cases.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/sv
