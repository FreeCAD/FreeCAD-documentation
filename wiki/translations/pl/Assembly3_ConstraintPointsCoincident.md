---
- GuiCommand:
   Name:Assembly3 ConstraintPointsCoincident
   Icon:Assembly_ConstraintPointCoincident.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintPointsCoincident/pl

## Description

This tool builds a link between two objects of an assembly and fixes the distance between them and the orientation to each other. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following object is moved to a position where both ICSs\' origins are in the same place.

Point elements have no stretch in any direction (zero length) and so there\'s no orientation detectable i.e. their ICS are only to match other elements\' settings. The orientation of the ICSs always stays the same as the global coordinate system\'s orientation and can not be used to reduce any degrees of freedom related to rotation.

Related to the first object the following object can still spin around the origin (around all three axes). This is leaving 3 degrees of freedom (DOFs) for each link unconstrained.

## Usage

1.  Place two objects into an assembly
2.  Select one point element of each object
3.  Press the **<img src="images/Assembly_ConstraintPointCoincident.svg" width=16px> [Points coincident](Assembly3_ConstraintPointsCoincident.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintPointsCoincident/pl
