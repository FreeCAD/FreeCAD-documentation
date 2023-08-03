---
 GuiCommand:
   Name: Assembly3 ConstraintPointOnCircle
   Icon: Assembly_ConstraintPointOnCircle.svg
   Workbenches: Assembly3_Workbench
---

# Assembly3 ConstraintPointOnCircle/en

## Description

This tool builds a link between two objects of an assembly and fixes the distance between them and the orientation to each other. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following object is moved to a position where the point element\'s origin lies on the circular element\'s xy-plane with an offset from the z-axis (matching x and y values according to the radius).

Point elements have no stretch in any direction (zero length) and so there\'s no orientation detectable i.e. their ICS are only to match other elements\' settings. The orientation of the ICSs always stays the same as the global coordinate system\'s orientation and can not be used to reduce any degrees of freedom related to rotation.

The position on the circular element (arc length from the start point) is not defined. Related to the first object the following object can still spin around the origin (around all three axes). This is leaving 4 degrees of freedom (DOFs) for each link unconstrained.

## Usage

1.  Place two objects into an assembly.
2.  Select one point element of one object and one circular face or edge element of the other object.
3.  Press the **<img src="images/Assembly_ConstraintPointOnCircle.svg" width=16px> [Point on circle](Assembly3_ConstraintPointOnCircle.md)** button.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPointOnCircle/en
