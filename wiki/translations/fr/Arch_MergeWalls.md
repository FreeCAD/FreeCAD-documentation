---
 GuiCommand:
   Name: Arch MergeWalls
   Name/fr: Arch Fusionner des murs
   MenuLocation: Utilitaires , Fusionner des murs
   Workbenches: BIM_Workbench/fr
   SeeAlso: Arch_Wall/fr
---

# Arch MergeWalls/fr

## Description

L\'outil **Arch Fusionner des murs** fusionne plusieurs [Arch Murs](Arch_Wall/fr.md).



## Utilisation

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez un seul mur avec un ou plusieurs [ajouts](Arch_Add/fr.md) qui sont également des murs.
    -   Sélectionnez deux murs ou plus.
2.  Dans les deux cas, les murs doivent avoir les mêmes propriétés **Height**, **Width** et **Align**.
3.  Sélectionnez l\'option **Utilitaires → <img src="images/Arch_MergeWalls.svg" width=16px> Fusionner des murs** du menu.



## Remarques

-   [Arch Ajouter](Arch_Add/fr.md) peut fusionner des murs même s\'ils ont des hauteurs, des largeurs et des alignements différents.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction :


```python
base = joinWalls(walls, delete=False)
```

Exemple :


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute() 

base = Arch.joinWalls([Wall1, Wall2])
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch MergeWalls/fr
