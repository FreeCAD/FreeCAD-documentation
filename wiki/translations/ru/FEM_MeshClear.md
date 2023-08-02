---
- GuiCommand:
   Name: FEM MeshClear
   Name/ru: FEM MeshClear
   MenuLocation:  Context menu on mesh object -> Clear FEM mesh
   Workbenches: FEM_Workbench/ru
   SeeAlso: FEM_tutorial/ru
---

# FEM MeshClear/ru


</div>

## Описание

Enables the user to reiniitialize the mesh from the FreeCAD FEM mesh object. The mesh still exists but does not have any vertices, edges, faces or elements. The meshing information, Netgen/Gmsh parameters, mesh regions, mesh groups and mesh boundary layer remain in the Model Tree, which means the mesh can be reproduced later. The main use of this function is to lighten the FreeCAD file, either to improve performance when using FreeCAD, to save disk space or enable easy transfer of files without losing meshing data.

## Применение

1.  Right-click a <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [Netgen](FEM_MeshNetgenFromShape.md) or <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [Gmsh](FEM_MeshGmshFromShape.md) FEM mesh object in the [Tree view](Tree_view.md).
2.  Select the **<img src="images/FEM_MeshClear.svg" width=16px> Clear FEM mesh** option from the context menu.

## Notes

The objects in the Model Tree are maintained because they represent the meshing data, but the mesh is now cleared from the FreeCAD file.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshClear/ru
