---
- GuiCommand:
   Name:Assembly3 ConstraintArcLineTangent
   Icon:Assembly_ConstraintArcLineTangent.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintArcLineTangent

## Description

The **<img src="images/Assembly_ConstraintArcLineTangent.svg" width=16px> [Arc line tangent](Assembly3_ConstraintArcLineTangent.md)** command builds a link between two objects of an assembly. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

Since I couldn\'t get this tool working here\'s just the statement of the tool tip: Add an \"Arc line tangent\" constraint to make a line tangent to an arc at the start or end point of the arc.

## Usage

1.  Place two objects into an assembly
2.  Select an arc element of one object
3.  Select a line element of the second object
4.  Press the **<img src="images/Assembly_ConstraintArcLineTangent.svg" width=16px> [Arc line tangent](Assembly3_ConstraintArcLineTangent.md)** button.

Depending on the order of the selected lines following **errors** appear:

Constraint "ArcLineTangent" requires the 1st element to be a circular edge
Constraint "ArcLineTangent" requires the 1st element to be an arc edge



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 ConstraintArcLineTangent
