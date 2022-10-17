---
- GuiCommand   *
   Name   *Assembly3 ConstraintAttachment
   Icon   *Part_Attachment.svg
   Workbenches   *[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintAttachment/en

## Description

This tool builds a link between two objects of an assembly and fixes the distance between them and their orientation to each other. The selected elements of each object or more precisely their element coordinate systems (ECS) are used to reposition the objects relative to each other.

This link leaves no degree of freedom (DOF) unconstrained.

## Usage

1.  Place two objects into an assembly.
2.  Select one element of each object.
3.  Press the **<img src="images/Part_Attachment.svg" width=16px> [Create "Attachment" constraint](Assembly3_ConstraintAttachment.md)** button.
4.  The objects are rearranged so that their ECSs share the same origin and have the same orientation.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintAttachment/en
