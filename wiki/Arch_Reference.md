---
 GuiCommand:
   Name: Arch Reference
   MenuLocation: 3D/BIM , Generic 3D tools , External reference
   Workbenches: BIM_Workbench
   SeeAlso: 
---

# Arch Reference

## Description

The **Arch Reference tool** allows you to place an object in the current document that copies its shape and colors from a [Part](Part_Workbench.md)-based object (including [Arch BuildingPart](Arch_BuildingPart.md)) stored in another FreeCAD file. If that FreeCAD file changes, the reference object is marked to be reloaded.

<img alt="" src=images/Arch_reference_screenshot.png  style="width:600px;">

## Usage

1.  Press the **<img src="images/Arch_Reference.svg" width=16px> [External reference](Arch_Reference.md)** button,
2.  Press the \"Choose file\...\" button and select an existing FreeCAD file,
3.  Select one of the included Part-based objects from the drop-down list,
4.  Press **OK**.

## Options

-   The reference object can be moved and rotated, the current position will be retained after reloading the object.
-   If the original object gets moved in containing file, this movement will reflect in the reference object.
-   By right-clicking a Reference object in the tree view, you have the options to reload the original object, or open the containing file.
-   To reference several objects at once, place them inside an [Arch BuildingPart](Arch_BuildingPart.md).
-   When turning off the **Update Colors** view property of the Reference, it won\'t reload the original colors anymore, so you can safely change them.

## Properties

-    **File**: The base file this component is built upon

-    **Part**: The part to use from the base file

-    **Update Colors**: If true, the colors from the linked file will be kept updated

## Scripting

The Reference tool can by used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

 
```python
reference = makeReference([filepath], [partname], [name])
```

Creates a `reference` object named `name` from the object `partname` in the file `filepath`. All arguments are optional.

Example:

 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd", "myPart")
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Reference
