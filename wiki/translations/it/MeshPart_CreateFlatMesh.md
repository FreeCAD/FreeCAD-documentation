---
- GuiCommand:
   Name:MeshPart_CreateFlatMesh
   Name/it:Sviluppa una mesh
   Empty:1
   MenuLocation:Mesh → Sviluppa una mesh
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Sviluppa una faccia](MeshPart_CreateFlatFace/it.md)
---

# MeshPart CreateFlatMesh/it


</div>



## Descrizione

The **MeshPart CreateFlatMesh** command creates a flat representation of a mesh object by unwrapping, unfolding, it. The created outline is a [Part Feature](Part_Feature.md).

![](images/MeshPart_CreateFlatMesh_example.png ) 
*A mesh object and, in red, its flat representation*



## Utilizzo

1.  Select a single mesh object. The mesh must be \'unwrappable\'. For example, to unwrap a cylindrical mesh it must have open ends and an open seam. Also curved surfaces must have a relatively fine mesh. Use the [Mesh RemeshGmsh](Mesh_RemeshGmsh.md) command if necessary.
2.  Select the **Meshes → <img src="images/MeshPart_CreateFlatMesh.svg" width=16px> Unwrap Mesh** option from the menu.



## Proprietà

Vedere: [Funzioni Part](Part_Feature/it.md).


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Category_Mesh.md) > [MeshPart](MeshPart_Workbench.md) > MeshPart CreateFlatMesh/it
