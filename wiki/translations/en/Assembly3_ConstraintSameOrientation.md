---
- GuiCommand:
   Name:Assembly3 ConstraintSameOrientation
   Icon:Assembly_ConstraintSameOrientation.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintSameOrientation/en

## Description

This tool builds a link between two or more objects of an assembly and matches their orientation. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following objects are moved to positions where all ICSs have the same orientation i.e. all z-axes are parallel and all x-axes are parallel (making the y-axes parallel as well).

The offset of their origins in x-, y- and z-direction are not defined. Related to the first object the following objects can still move along the x-, y- and z-axis. This is leaving 3 degrees of freedom (DOFs) for each link unconstrained.

The constraint accepts planar faces.

## Usage

1.  Place two or more objects into an assembly
2.  Select one planar face element of each object
3.  Press the **<img src="images/Assembly_ConstraintSameOrientation.svg" width=16px> [Same orientation](Assembly3_ConstraintSameOrientation.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintSameOrientation/en
