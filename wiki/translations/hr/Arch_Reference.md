# Arch Reference/hr
---
- GuiCommand:/hr   Name:Arch Reference   Name/hr:Arch Reference   Workbenches:[MenuLocation:Arch → Reference   Shortcut:   SeeAlso:[[Arch BuildingPart](Arch_Workbench___Arch]].md)---


</div>

## Description

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">

The Reference tool allows you to place an object in the current document that copies its shape and colors from an [Part](Part_Workbench.md)-based object (including [Arch BuildingPart](Arch_BuildingPart.md)) stored in another FreeCAD file. If that FreeCAD file changes, the reference object is marked to be reloaded.

## Usage

1.  Press the **<img src="images/Arch_Reference.svg" width=16px> '''Arch Reference'''** button,
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

The Reference tool can by used in [macros](macros.md) and from the python console by using the following function: 
```python
makeReference ([file_path,object_name])
```

creates a Reference object from the given object in the given file.

Primjer: 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd","myPart")
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Reference/hr
