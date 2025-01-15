---
 GuiCommand:
   Name: Arch SplitMesh
   Name/fr: Arch Diviser un maillage
   MenuLocation: Utilitaires , Diviser un maillage
   Workbenches: BIM_Workbench/fr
   SeeAlso: Arch_SelectNonSolidMeshes/fr, Arch_MeshToShape/fr
---

# Arch SplitMesh/fr

## Description

L\'outil **Arch Diviser un maillage** sépare les composants d\'un objet [Mesh](Mesh_Workbench/fr.md) sélectionné.



## Utilisation

1.  Sélectionnez un objet mesh.
2.  Sélectionnez l\'option **Utilitaires → <img src="images/Arch_SplitMesh.svg" width=16px> Diviser un maillage** du menu.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Diviser un maillage est utilisable dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
new_list = splitMesh(obj, mark=True)
```

-   Divise l\'objet maillé donné (`obj`) en composants séparés.

-   Si `mark` est mis à `True`, les composants [non-manifolds](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_(g%C3%A9om%C3%A9trie)) seront peints en rouge.

-    `new_list`est une liste de tous les composants individuels qui composent le maillage.

Exemple :


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



---
⏵ [documentation index](../README.md) > Arch SplitMesh/fr
