---
- GuiCommand:
   Name:Part ReverseShapes
   MenuLocation:Part → Reverse shapes
   Workbenches:[Part](Part_Workbench.md)
---

# Part ReverseShapes/pl

## Description

Flips the normals of all faces of the selected object.

## Usage

1.  Select shape.
2.  Select the **Part → <img src="images/Part_ReverseShapes.svg" width=16px> Reverse shapes** option from the menu.
3.  A reversed shape is created as a new separate object.

## Notes

By executing this command, FreeCAD flips the normals of all faces of the shape/solid.

You can verify this by

1.  Making all other objects but the reversed shape invisible.
2.  Selecting the reversed shape.
3.  Change **Lighting** from \"Two side\" to \"One side\".
4.  The shape will turn black, meaning that you are now looking at the back of the faces.

## Properties

## Scripting



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShapes/pl
