---
 GuiCommand:
   Name: FEM CreateElementsSet
   MenuLocation: Mesh , Erase Elements
   Workbenches: FEM_Workbench
   Version: 1.0
   SeeAlso: FEM_tutorial
---

# FEM CreateElementsSet/en

## Description

Hides the elements selected by a polygon from the FEM mesh or results mesh, making it possible to remove the selected parts of the mesh from the view and see the elements inside the mesh.

## Usage

1.  Select a FEM mesh (created by Netgen/Gmsh or imported) or the results mesh in the tree.
2.  Select the **Mesh → <img src="images/FEM_CreateElementsSet.svg" width=16px> Erase Elements** option from the menu.
3.  Optionally, enter the name of the tool\'s object that will be created in the tree.
4.  Press the **Poly** button and click on a few arbitrary locations in the 3D view to define the selection polygon.
5.  Right-click and select *Inner* or *Outer* (to choose whether the elements inside the selection polygon should be erased or the ones outside of it) or *Cancel* if you want to quit the polygonal selection tool.
6.  The selected elements will be hidden from the mesh while the number of hidden and kept elements will be shown in the Report view.
7.  Click the **OK** button. You will notice new objects in the tree - one named as specified (*ElementSet* by default) and one named *NewFemMesh* or *NewResultMesh* depending on the input. In the case of the results mesh, there will also be a copy of the original mesh named *StartResultMesh*. The *ElementSet* object can be used to access the tool again.
8.  To remove the new objects from the tree and keep only the original mesh, double-click on the *ElementSet* object and press the **Restore** button. The original mesh won\'t be automatically brought back to visibility.

## Notes

-   To hide more elements from the same FEM mesh after the initial use of the tool, you have to manually select the new (modified) mesh. This is not the case with the results meshes.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM CreateElementsSet/en
