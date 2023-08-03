---
 GuiCommand:
   Name: Part Common
   MenuLocation: Part , Boolean , Common
   Workbenches: Part_Workbench
   SeeAlso: Part_Boolean, Part_Cut, Part_Fuse
---

# Part Common

## Description

Extracts the common part (intersection) between selected Part objects. This operation is fully parametric and the components can be modified and the result recomputed.

## Usage

1.  Select two shapes
2.  Press the **![](images/)_[Common](Part_Common.md)** button.

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. Examples: stuff made with Part, PartDesign, Sketcher workbenches. Not meshes (unless those were converted to shapes) - for meshes, there are specific Boolean tools in MeshDesign workbench.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Common
