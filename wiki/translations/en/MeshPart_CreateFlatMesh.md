---
 GuiCommand:
   Name: MeshPart CreateFlatMesh
   MenuLocation: Meshes , Unwrap Mesh
   Workbenches: Mesh_Workbench
   Version: 0.19
   SeeAlso: MeshPart_CreateFlatFace
---

# MeshPart CreateFlatMesh/en

## Description

The **MeshPart CreateFlatMesh** command creates a flat representation of a mesh object by unwrapping, unfolding, it. The created outline is a [Part Feature](Part_Feature.md).

![](images/MeshPart_CreateFlatMesh_example.png ) 
*A mesh object and, in red, its flat representation*

## Usage

1.  Select a single mesh object. The mesh must be \'unwrappable\'. For example, to unwrap a cylindrical mesh it must have open ends and an open seam. Also curved surfaces must have a relatively fine mesh. Use the [Mesh RemeshGmsh](Mesh_RemeshGmsh.md) command if necessary.
2.  Select the **Meshes → <img src="images/MeshPart_CreateFlatMesh.svg" width=16px> Unwrap Mesh** option from the menu.

## Properties

See: [Part Feature](Part_Feature.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Category_Mesh.md) > [MeshPart](MeshPart_Workbench.md) > MeshPart CreateFlatMesh/en
