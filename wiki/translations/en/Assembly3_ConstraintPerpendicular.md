---
- GuiCommand   *
   Name   *Assembly3 ConstraintPerpendicular
   Icon   *Assembly_ConstraintPerpendicular.svg
   Workbenches   *[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintPerpendicular/en

## Description

This tool builds a link between two objects of an assembly and matches their orientation. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following object is moved to a position where both z-axes are perpendicular.

The offset of their origins in x-, y- and z-direction and the angles between the x-, and y-axes are not defined. Related to the first object the following object can still move along the x-, y- and z-axis and spin around both z-axes. This is leaving 5 degrees of freedom (DOFs) for each link unconstrained.

The constraint accepts straight edges and planar faces.

## Usage

1.  Place two objects into an assembly.
2.  Select one straight edge element or one planar face element of each object.
3.  Press the **<img src="images/Assembly_ConstraintPerpendicular.svg" width=16px> [Perpendicular](Assembly3_ConstraintPerpendicular.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintPerpendicular/en
