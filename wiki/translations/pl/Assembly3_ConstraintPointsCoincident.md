---
- GuiCommand:
   Name: Assembly3 ConstraintPointsCoincident
   Icon: Assembly_ConstraintPointCoincident.svg
   Workbenches: [Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintPointsCoincident/pl

## Description

The <img alt="" src=images/Assembly_ConstraintPointCoincident.svg  style="width:24px;"> [Assembly3 ConstraintPointsCoincident](Assembly3_ConstraintPointsCoincident.md) command builds a link between two objects of an assembly and fixes the distance between them and the orientation to each other. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following object is moved to a position where both ICSs\' origins are in the same place.

Related to the first object the following object can still spin around the origin (around all three axes). This is leaving 3 degrees of freedom (DOFs) for each link unconstrained.

This constraint accepts any type of element!

## Usage

1.  Place two objects into an assembly
2.  Select one element of each object
3.  Activate the <img alt="" src=images/Assembly_ConstraintPointCoincident.svg  style="width:16px;"> **Assembly3 ConstraintPointsCoincident** command using:
    -   The **<img src="images/Assembly_ConstraintPointCoincident.svg" width=16px> [Create "PointsCoincident" constraint](Assembly3_ConstraintPointsCoincident.md)** button.

## Kinematic Equivalent 

Used in kinematic context this constraint resembles a **ball** (and socket) **joint**.

In real life we cannot handle points and so spherical faces are used to represent the linked points.

<img alt="" src=images/Assembly3_ConstraintPointsCoincident-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintPointsCoincident-02.png  style="width:200px;">



*Constrained objects before and after running the solver*



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPointsCoincident/pl
