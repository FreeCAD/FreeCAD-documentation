---
- GuiCommand   */fr
   Name   *Arch MergeWalls
   Name/fr   *Arch Fusionner des murs
   MenuLocation   *Arch → Utilitaires → Fusionner des murs
   Workbenches   *[Arch](Arch_Workbench/fr.md)
   SeeAlso   *[Arch Murs](Arch_Wall/fr.md)
---

# Arch MergeWalls/fr

## Description

L\'outil [Fusionner des Murs](Arch_MergeWalls/fr.md) fusionne deux ou plusieurs **<img src="images/Arch_Wall.svg" width=16px>[Arch Murs](Arch_Wall/fr.md)** sélectionnés.

## Utilisation

1.  Sélectionnez deux ou plusieurs murs.
2.  Appuyez sur le bouton **<img src="images/Arch_MergeWalls.svg" width=16px>** ou utilisez le **Arch** → **Utilitaires** → **<img src="images/Arch_MergeWalls.svg" width=16px> [Fusionner des murs](Arch_MergeWalls/fr.md)** dans le menu supérieur.

## Propriétés

## Limitations

## Script


**Voir aussi    ***

[Arch API](Arch_API.md) et [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Cet outil peut être utilisé dans des [macros](macros.md) et à partir de la console [Python](Python.md) à l\'aide de la fonction suivante    * 
```python
base = joinWalls(walls, delete=False)
```

Exemple   * 
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
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MergeWalls/fr
