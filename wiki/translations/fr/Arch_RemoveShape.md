---
- GuiCommand:
   Name:Arch RemoveShape
   Name/fr:Arch Supprimer la forme
   MenuLocation:Arch → Utilitaires → Supprimer la forme
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Séparer un objet Mesh](Arch_SplitMesh/fr.md), [Arch Maillage vers une forme](Arch_MeshToShape/fr.md)
---

# Arch RemoveShape/fr

## Description

Cet outil vise à supprimer la forme cubique intérieure d\'un **<img src="images/Arch_Wall.svg" width=16px>[Arch Mur](Arch_Wall/fr.md)** ou d\'une **<img src="images/Arch_Structure.svg" width=16px>[Arch Structure](Arch_Structure/fr.md)** et ajuste ses propriétés, la rendant totalement paramétriques. Cet outil ne fonctionne que si le shape sous-jacent est cubique (exactement 6 faces, tous les coins ont seulement des angles droits).



## Utilisation

1.  Selectionnez un **<img src="images/Arch_Wall.svg" width=16px>[Arch Mur](Arch_Wall/fr.md)** ou une **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.
2.  Cliquez le bouton **<img src="images/Arch_RemoveShape.svg" width=16px> [Supprimer la forme](Arch_RemoveShape/fr.md)** ou par le menu **Arch** → **Utilitaires** → **<img src="images/Arch_RemoveShape.svg" width=16px> [Supprimer la forme](Arch_RemoveShape/fr.md)**.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction : 
```python
removeShape(objs, mark=True)
```

-   Prend une liste d\'objets Arch (`objs`) construits sur une forme cubique et supprime la forme interne, en conservant la longueur, la largeur et la hauteur comme propriétés de l\'objet Arch.
    -   
        `objs`
        
        est un objet unique, [mur Arch](Arch_Wall/fr.md) ou [Arch Structure](Arch_Structure/fr.md) ou une liste d\'entre eux.
-   Si `mark` est mis à `True`, les objets qui ne peuvent pas être traités par cette fonction deviennent rouges.


```python
import FreeCAD, Draft, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(Box)
FreeCAD.ActiveDocument.recompute()

Arch.removeShape(Structure)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/fr
