---
- GuiCommand:
   Name:Assembly3 ConstraintMultiParallel
   Icon:Assembly_ConstraintMultiParallel.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintMultiParallel/pl

## Description

This tool builds a link between two or more objects of an assembly and matches their orientation. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following objects are moved to positions where all z-axes point in the same direction i.e. all z-axes are parallel.

The offset of their origins in x-, y- and z-direction and the angles between the x-axes (and y-axes as well) are not defined. Related to the first object the following objects can still move along the x-, y- and z-axis and spin around the z-axis. This is leaving 4 degrees of freedom (DOFs) for each link unconstrained.

The constraint accepts straight edges and planar faces, which become parallel.

## Usage

1.  Place two or more objects into an assembly.
2.  Select one straight edge element or one planar face element of each object.
3.  Press the **<img src="images/Assembly_ConstraintMultiParallel.svg" width=16px> [Multi parallel](Assembly3_ConstraintMultiParallel.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintMultiParallel/pl
