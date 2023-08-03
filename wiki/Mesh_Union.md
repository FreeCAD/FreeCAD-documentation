---
 GuiCommand:
   Name: Mesh Union
   MenuLocation: Meshes , Boolean , Union
   Workbenches: Mesh_Workbench
   SeeAlso: Mesh_Intersection, Mesh_Difference
---

# Mesh Union

## Description

The **Mesh Union** command creates a new non-parametric mesh object, a [Mesh Feature](Mesh_Feature.md), that is the union (fusion) of two mesh objects.

[OpenSCAD](http://www.openscad.org/) must be installed to use this command, and the path to its executable must be set in the [OpenSCAD preferences](OpenSCAD_Preferences.md).

 ![](images/Mesh_Union_example.png )  
*On the left two mesh objects, on the right the mesh object that is the union of those objects*

## Usage

1.  Select two mesh objects that partially overlap.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Union.svg" width=16px> [Mesh Union](Mesh_Union.md)** button.
    -   Select the **Meshes → Boolean → <img src="images/Mesh_Union.svg" width=16px> Union** option from the menu.

## Properties

See: [Mesh Feature](Mesh_Feature.md).




 {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Union
