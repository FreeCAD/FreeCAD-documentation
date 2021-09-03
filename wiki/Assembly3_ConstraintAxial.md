---
- GuiCommand:
   Name:Assembly3 ConstraintAxial
   Icon:Assembly_ConstraintAxial.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

## Description

This tool builds a link between two or more objects of an assembly and matches their orientation. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following objects are moved to positions where the z-axes are collinear .

The offset of their origins on their common z-axis and the angle between their x-axes (and y-axes as well) are not defined. Related to the first object the following objects can still move along and spin around the z-axis. This is leaving 2 degrees of freedom (DOFs) for each link unconstrained.

The constraint accepts

:   \- straight edges, which become collinear,
:   \- planar faces, which are aligned using their surface normal axis,
:   \- cylindrical faces, which are aligned using the axial direction.

Different types of geometry elements can be mixed.

## Usage

1.  Place two or more objects into an assembly.
2.  Select one element of each object.
3.  Press the **<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Axial Alignment](Assembly3_ConstraintAxial.md)** button.




 
