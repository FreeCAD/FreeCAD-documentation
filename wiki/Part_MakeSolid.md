---
 GuiCommand:
   Name: Part MakeSolid
   MenuLocation: Part , Convert to solid
   Workbenches: Part_Workbench
   SeeAlso: Part_ShapeFromMesh
---

# Part MakeSolid

## Description

The <img alt="" src=images/Part_MakeSolid.svg  style="width:24px;"> **Part MakeSolid** command creates solids from shape objects.

This command is typically used as one of the steps to create a solid from a mesh. See [Part ShapeFromMesh](Part_ShapeFromMesh#Usage.md) for more information.

## Usage

1.  Select one or more shape objects.
2.  Select the **Part → <img src="images/Part_MakeSolid.svg" width=16px> Convert to solid** option from the menu.
3.  For each selected object a solid is created as a separate new object.

## Notes

-   The selected shape objects or not analyzed or validated.
-   It is recommended to use [Part RefineShape](Part_RefineShape.md) before converting to a solid.

## Properties

See also: [Property editor](Property_editor.md).

The created objects are [Part Feature](Part_Feature.md) objects with no additional properties.




 {{Part_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part MakeSolid
