---
 GuiCommand:
   Name: Arch MergeWalls
   Name/it: Unisci Muri
   MenuLocation: Arch , Utilità , Unisci Muri
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch_Wall/it
---

# Arch MergeWalls/it



## Descrizione

Lo strumento [Unisci pareti](Arch_MergeWalls/it.md) fonde due o più **<img src="images/_Arch_Wall.svg" width=16px> [Pareti](Arch_Wall/it.md)** selezionate.



## Utilizzo

1.  Selezionare due o più muri.
2.  Premere il pulsante **<img src="images/Arch_MergeWalls.svg" width=16px>**, o utilizzare **Arch** → **Utilità** → **<img src="images/Arch_MergeWalls.svg" width=16px> [Unisci pareti](Arch_MergeWalls/it.md)** dal menu principale.



## Proprietà



## Limitazioni



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
base = joinWalls(walls, delete=False)
```

Esempio: 
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
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MergeWalls/it
