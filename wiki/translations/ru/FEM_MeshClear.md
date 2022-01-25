---
- GuiCommand:/ru
   Name:FEM MeshClear
   Name/ru:FEM MeshClear
   MenuLocation: Context menu on mesh object → Clear FEM mesh
   Workbenches:[FEM](FEM_Workbench/ru.md)
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM MeshClear/ru


</div>

## Описание

Enables the user to reiniitialize the mesh from the FreeCAD FEM mesh object. The mesh still exists but does not have any vertices, edges, faces or elements. The meshing information, Netgen/Gmsh parameters, mesh regions, mesh groups and mesh boundary layer remain in the Model Tree, which means the mesh can be reproduced later. The main use of this function is to lighten the FreeCAD file, either to improve performance when using FreeCAD, to save disk space or enable easy transfer of files without losing meshing data.

## Использование

1.  Right click on the mesh object in the Model Tree <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md).
2.  Select the <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> Clear FEM mesh.

## Notes

The objects in the Model Tree are maintained because they represent the meshing data, but the mesh is now cleared from the FreeCAD file.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshClear/ru
