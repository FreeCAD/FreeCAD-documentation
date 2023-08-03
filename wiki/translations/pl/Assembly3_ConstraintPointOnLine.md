---
 GuiCommand:
   Name: Assembly3 ConstraintPointOnLine
   Icon: Assembly_ConstraintPointOnLine.svg
   Workbenches: Assembly3_Workbench
---

# Assembly3 ConstraintPointOnLine/pl

## Description

This tool builds a link between two objects of an assembly and fixes the distance between them and the orientation to each other. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following object is moved to a position where the point elements\'s origin lies on the line element\'s z-axis.

Point elements have no stretch in any direction (zero length) and so there\'s no orientation detectable i.e. their ICS are only to match other elements\' settings. The orientation of the ICSs always stays the same as the global coordinate system\'s orientation and can not be used to reduce any degrees of freedom related to rotation. Straight elements have an origin and a direction which is represented by the ICS\'s z-axis. A direction of the x- and y-axis is not detectable and so rotation around the z-axis can not be used to reduce DOFs. (It doesn\'t apply in combination with point elements anyway\...)

Related to the first object the following object can still move along the z-axis and spin around all three axes. This is leaving 4 degrees of freedom (DOFs) for each link unconstrained.

## Usage

1.  Place two objects into an assembly.
2.  Select one point element of one object and one straight edge element of the other object.
3.  Press the **<img src="images/Assembly_ConstraintPointOnLine.svg" width=16px> [Point on line](Assembly3_ConstraintPointOnLine.md)** button.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPointOnLine/pl
