---
 GuiCommand:
   Name: Assembly3 ConstraintAxial
   Icon: Assembly_ConstraintAxial.svg
   Workbenches: Assembly3_Workbench
---

# Assembly3 ConstraintAxial

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
3.  Activate the <img alt="" src=images/Assembly_ConstraintAxial.svg  style="width:16px;"> **Assembly3 ConstraintAxial** command using:
    -   The **<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Create "AxialAlignment" constraint](Assembly3_ConstraintAxial.md)** button.

## Kinematic Equivalent 

Used in kinematic context this constraint resembles a **cylindrical joint**.

In real life we cannot handle axes and so cylindrical faces are used to represent the linked axes.

 <img alt="" src=images/Assembly3_ConstraintAxial-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintAxial-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintAxial-03.png  style="width:200px;"> 



*Constrained objects before and after running the solver and then slid along the axis*



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintAxial
