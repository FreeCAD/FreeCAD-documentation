---
- GuiCommand:
   Name: Assembly3 ConstraintSymmetricVertical
   Icon: Assembly_ConstraintGeneral.svg
   Workbenches: [Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintSymmetricVertical

## Description

This tool builds a link between two objects of an assembly. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position the objects to each other.

Based on one planar element\'s ICS both other elements\' ICSs\' origins are positioned to have identical x- and z-coordinates and the same y-offset in opposite directions.

## Usage

1.  Place two objects into an assembly
2.  Select two point elements, two line elements or two planar elements of one object
3.  Select a planar element of the other object
4.  Press the **<img src="images/Assembly_ConstraintGeneral.svg" width=16px> [Symmetric vertical](Assembly3_ConstraintSymmetricVertical.md)** button.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintSymmetricVertical
