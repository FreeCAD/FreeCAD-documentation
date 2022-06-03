---
- GuiCommand   *
   Name   *Assembly3 ConstraintAlignment
   Icon   *Assembly_ConstraintAlignment.svg
   Workbenches   *[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintAlignment/en

## Description

This tool links two or more objects of an assembly and matches their orientations. The selected elements of each object or more precisely their implicit coordinate systems (ICSs) are used to position one object in relation to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following objects are moved to positions where the x-y-planes of all ICSs are coplanar and the z-axes point in the same direction.

The offset of their z-axes and the angle between their x-axes (and y-axes as well) are not defined. Related to the first object the following objects can still move along the x- and y-direction and spin around the z-axis. This is leaving 3 degrees of freedom (DOFs) for each link unconstrained.

## Usage

1.  Place two or more objects into an assembly.
2.  Select one planar face element of each object.
3.  Press the **<img src="images/Assembly_ConstraintAlignment.svg" width=16px> [Alignment](Assembly3_ConstraintAlignment.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintAlignment/en
