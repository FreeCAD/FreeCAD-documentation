---
- GuiCommand:/fr
   Name:Arch 3Views
   Name/fr:Arch 3 Vues depuis un maillage
   MenuLocation: Arch → Utilitaires → 3 vues depuis un maillage
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Séparer un objet Mesh](Arch_SplitMesh/fr.md), [Arch Maillage vers une forme](Arch_MeshToShape/fr.md)
---

# Arch 3Views/fr

## Description


**Cette commande n'est pas utilisée actuellement.**

Elle servira à générer des vues planes, basées sur des formes, à partir d\'un objet [Atelier Mesh](Mesh_Workbench/fr.md), à utiliser par l\'outil **<img src="images/Arch_Equipment.svg" width=24px> [Arch Equipement](Arch_Equipment/fr.md)**.



## Utilisation

-   Sélectionnez un objet Mesh
-   Sélectionnez le bouton **<img src="images/Arch_3Views.svg" width=16px>** ou par le menu du haut **Arch** → **Utilitaires** → **<img src="images/Arch_3Views.svg" width=16px> [3 vues depuis un maillage](Arch_3Views/fr.md)**.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction : 
```python
shape = createMeshView(obj, direction=FreeCAD.Vector(0, 0, -1), outeronly=False, largestonly=False)
```

-   Crée un `shape` plan qui est la projection de l\'objet maillé donné (`obj`) dans la `direction` donnée.
-   Si `outeronly` est `True`, seul le contour extérieur est pris en compte, en ignorant les trous intérieurs.
-   Si `mostonly` est `True`, seul le plus grand segment du maillage donné sera utilisé.

Utilisez `Part.show()` pour afficher la forme plane résultante.

Exemple: 
```python
import FreeCAD, Draft, Arch, Mesh, MeshPart

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

Shape = Wall.Shape.copy(False)
Shape.Placement = Wall.getGlobalPlacement()

mesh_obj = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh_obj.Mesh = MeshPart.meshFromShape(Shape=Shape, MaxLength=520)
mesh_obj.ViewObject.DisplayMode = "Flat Lines"
FreeCAD.ActiveDocument.recompute()

XAxis = FreeCAD.Vector(1, 0, 0)
YAxis = FreeCAD.Vector(0, 1, 0)
ZAxis = FreeCAD.Vector(0, 0, -1)

s1 = Arch.createMeshView(mesh_obj, ZAxis)
s2 = Arch.createMeshView(mesh_obj, XAxis)
s3 = Arch.createMeshView(mesh_obj, YAxis)

Part.show(s1)
Part.show(s2)
Part.show(s3)

Wall.ViewObject.Visibility = False
mesh_obj.ViewObject.Visibility = False
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch 3Views/fr
