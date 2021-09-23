---
- GuiCommand:
   Name:FEM MeshClear
   MenuLocation:Context menu on mesh object → Clear FEM mesh
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM MeshClear/en

## Description

Enables the user to reiniitialize the mesh from the FreeCAD FEM mesh object. The mesh still exists but does not have any vertices, edges, faces or elements. The meshing information, Netgen/Gmsh parameters, mesh regions, mesh groups and mesh boundary layer remain in the Model Tree, which means the mesh can be reproduced later. The main use of this function is to lighten the FreeCAD file, either to improve performance when using FreeCAD, to save disk space or enable easy transfer of files without losing meshing data.

## Usage

1.  Right click on the mesh object in the Model Tree <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md).
2.  Select the <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> Clear FEM mesh.

## Notes

The objects in the Model Tree are maintained because they represent the meshing data, but the mesh is now cleared from the FreeCAD file.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM MeshClear/en
