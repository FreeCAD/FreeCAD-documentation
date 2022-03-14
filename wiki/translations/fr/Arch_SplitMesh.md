---
- GuiCommand:/fr
   Name:Arch SplitMesh
   Name/fr:Arch Diviser un maillage
   MenuLocation:Arch → Utilitaires → Diviser un maillage
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Sélection de maillages non-manifold](Arch_SelectNonSolidMeshes/fr.md), [Arch Maillage vers un objet shape](Arch_MeshToShape/fr.md)
---

# Arch SplitMesh/fr

## Description

Cet outil sépare les composants d\'un objet [Mesh](Mesh_Workbench/fr.md) sélectionné.

## Utilisation

1.  Sélectionnez un objet mesh.
2.  Cliquez sur le bouton **<img src="images/Arch_SplitMesh.svg" width=16px>  [Diviser un maillage](Arch_SplitMesh/fr.md)** dans **Arch → Utilitaires → Diviser un maillage**.

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Séparer un objet Mesh est utilisable dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
new_list = splitMesh(obj, mark=True)
```

-   Divise l\'objet maillé donné (`obj`) en composants séparés.

-   Si `mark` est mis à `True`, les composants [Variété non-manifold](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_(g%C3%A9om%C3%A9trie)) seront peints en rouge.

-    `new_list`est une liste de tous les composants individuels qui composent le maillage.

Exemple:


```python
import FreeCAD, Draft, Arch, Mesh, MeshPart

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

Shape = Wall.Shape.copy(False)
Shape.Placement = Wall.getGlobalPlacement()

mesh_obj = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh_obj.Mesh = MeshPart.meshFromShape(Shape=Shape, MaxLength=520)
mesh_obj.ViewObject.DisplayMode = "Flat Lines"

new_list = Arch.splitMesh(mesh_obj)
```





{{Arch_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SplitMesh/fr
