---
- GuiCommand:
   Name:Part PointsFromMesh‎
   MenuLocation:Part → Create points object from mesh
   Workbenches:[Part](Part_Workbench.md)
   Version:0.19
   SeeAlso:[Part ShapeFromMesh](Part_ShapeFromMesh.md), [Part ConvertToSolid](Part_MakeSolid.md), [Part RefineShape](Part_RefineShape.md)
---

# Part PointsFromMesh/pl

## Description

The **<img src="images/Part_PointsFromMesh.svg" width=16px> [Part PointsFromMesh](Part_PointsFromMesh.md)
** tool creates a shape starting from a [mesh object](Glossary#Mesh.md) imported or produced from the **<img src="images/Workbench_Mesh.svg" width=16px> [Mesh Workbench](Mesh_Workbench.md)**

The resulting shape is a collection of vertices or points, which can be used as reference to further create lines, sketches and faces with other tools, like those from the **<img src="images/Workbench_Sketcher.svg" width=16px> [Sketcher](Sketcher_Workbench.md)** or the **<img src="images/Workbench_Draft.svg" width=16px> [Draft](Draft_Workbench.md)** workbenches.

## Usage

1.  Select the mesh object.
2.  Go to **Part → <img src="images/Part_PointsFromMesh.svg" width=24px> Create points object from mesh**.
3.  A shape from the mesh object is created as a separate new object.

There will be no analyzing or validating of the mesh object. Analyzing and repairing of the mesh should be done manually before conversion, if needed. Appropriate tools are available in the **<img src="images/Workbench_Mesh.svg" width=24px> [Mesh Workbench](Mesh_Workbench.md)
**

## Notes

## Properties

## Limitations

## Scripting



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part PointsFromMesh/pl
