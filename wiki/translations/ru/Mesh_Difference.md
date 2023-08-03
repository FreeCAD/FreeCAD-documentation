---
 GuiCommand:
   Name: Mesh Difference
   Name/ru: Mesh Difference
   MenuLocation:  Сетки , Булевы операции , Разность
   Workbenches: Mesh Workbench/ru
   Shortcut: 
   SeeAlso: 
---

# Mesh Difference/ru


</div>

## Description

The **Mesh Difference** command creates a new non-parametric mesh object, a [Mesh Feature](Mesh_Feature.md), that is the difference of two mesh objects: one mesh object is cut from the other.

[OpenSCAD](http://www.openscad.org/) must be installed to use this command, and the path to its executable must be set in the [OpenSCAD preferences](OpenSCAD_Preferences.md).

![](images/Mesh_Difference_example.png ) 
*On the left two mesh objects, on the right the mesh object that is the difference of those objects if the cube is selected as the main object*

## Usage

1.  Select the main mesh object.
2.  Add the mesh object you want to cut from the main object to the selection. The mesh objects must overlap.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Difference.svg" width=16px> [Mesh Difference](Mesh_Difference.md)** button.
    -   Select the **Meshes → Boolean → <img src="images/Mesh_Difference.svg" width=16px> Difference** option from the menu.

## Properties

See: [Mesh Feature](Mesh_Feature.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Difference/ru
