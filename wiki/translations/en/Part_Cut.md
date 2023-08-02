---
- GuiCommand:
   Name: Part Cut
   MenuLocation: Part -> Boolean -> Cut
   Workbenches: Part_Workbench
   SeeAlso: Part_Boolean, Part_Fuse, Part_Common
---

# Part Cut/en

## Description

Cuts (subtracts) selected Part objects, the last one being subtracted from the first one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)

## Usage

1.  Select two shapes
2.  Invoke the Part Cut command several ways:
    -   Press the **![](images/) '''Cut'''** button in the Part toolbar
    -   Use the **Part → Boolean → Cut** entry from the Part menu

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. For example objects made with the Part, PartDesign or Sketcher workbenches. For meshes there are dedicated Boolean tools in [Mesh Workbench](Mesh_Workbench.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/en
