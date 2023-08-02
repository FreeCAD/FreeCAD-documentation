---
- GuiCommand:
   Name: Draft Array
   Workbenches: Draft_Workbench, Arch_Workbench
   SeeAlso: Draft_OrthoArray, Draft_PolarArray, Draft_CircularArray
---

# Draft Array/en

## Description

The <img alt="" src=images/Draft_Array.svg  style="width:24px;"> **Draft Array** command creates an orthogonal (3-axes) array from a selected object. The created array can be turned into a [polar array](Draft_PolarArray.md) or a [circular array](Draft_CircularArray.md) by changing its **Array Type** property.

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage

1.  To use this command in FreeCAD version 0.19 and later you need to add a button to a custom toolbar. See [Interface Customization](Interface_Customization.md).
2.  Optionally select one object.
3.  Press the **<img src="images/Draft_Array.svg" width=16px> [Draft Array](Draft_Array.md)** button.
4.  If you have not yet selected an object: select one object.
5.  The array is created.
6.  Optionally change its [properties](Draft_OrthoArray#Properties.md).

## Properties

See [Draft OrthoArray](Draft_OrthoArray#Properties.md).

## Scripting

See [Draft OrthoArray](Draft_OrthoArray#Scripting.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/en
