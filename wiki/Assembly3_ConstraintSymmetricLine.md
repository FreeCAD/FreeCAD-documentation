---
- GuiCommand:
   Name: Assembly3 ConstraintSymmetricLine
   Icon: Assembly_ConstraintSymmetricLine.svg
   Workbenches: [Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintSymmetricLine

## Description

This tool builds a link between two or three objects of an assembly. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position the objects to each other.

Based on one line element\'s ICS both other elements\' ICSs\' origins are positioned to have identical z-coordinates and the same x- and y-offsets in opposite directions.

## Usage

1.  Place two objects into an assembly
2.  Select two point elements of one object
3.  Select a straight line element of the other object
4.  Press the **<img src="images/Assembly_ConstraintSymmetricLine.svg" width=16px> [Symmetric line](Assembly3_ConstraintSymmetricLine.md)** button.

Or

1.  Place three objects into an assembly
2.  Select one point element of the first two objects
3.  Select a straight line element of the third object
4.  Press the **<img src="images/Assembly_ConstraintSymmetricLine.svg" width=16px> [Symmetric line](Assembly3_ConstraintSymmetricLine.md)** button.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintSymmetricLine
