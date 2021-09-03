---
- GuiCommand:
   Name:Mesh RemeshGmsh
   MenuLocation:Meshes → Refinement...
   Workbenches:[Mesh](Mesh_Workbench.md)
   Version:0.19
   SeeAlso:[Mesh FromPartShape](Mesh_FromPartShape.md)
---

## Description

The **Mesh RemeshGmsh** command remeshes a mesh object using the [Gmsh](https://gmsh.info/) mesher. The new mesh can be finer or coarser.

## Usage

1.  Select a single mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_RemeshGmsh.svg" width=16px> [Mesh RemeshGmsh](Mesh_RemeshGmsh.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Refinement...** option from the menu.
3.  The **Remesh by gmsh** task panel opens.
4.  Specify the required settings. See the [Gmsh mesher settings](Mesh_FromPartShape#Gmsh_mesher.md) of the [Mesh FromPartShape](Mesh_FromPartShape.md) command.
5.  Press the **Apply** button to remesh the mesh object.
6.  Optionally change one or more settings and again press the **Apply** button until the new mesh is to your liking.
7.  Press the **Close** button to close the task panel and finish the command.

## Notes

-   In some cases this command will produce a mesh with flipped normals. The [Mesh FlipNormals](Mesh_FlipNormals.md) command can be used to correct this.

## Properties

See: [Mesh Feature](Mesh_Feature.md).




 {{Mesh Tools navi}}  
