---
 GuiCommand:
   Name: Arch MergeWalls
   Name/pl: Architektura: Połącz ściany
   MenuLocation: Narzędzia , Połącz ściany
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_Wall/pl
---

# Arch MergeWalls/pl



## Opis

Narzędzie **Połącz ściany** łączy [ściany](Arch_Wall/pl.md).



## Użycie

Wykonaj jedną z poniższych czynności:

#\* Wybierz pojedynczą ścianę z jednym lub wieloma [połączonymi obiektami](Arch_Add/pl.md), które również są ścianami.

#\* Wybierz dwie lub więcej ścian.

1.  W obu przypadkach ściany muszą mieć te same właściwości **Wysokość**, **Szerokość** i **Wyrównanie**.
2.  Wybierz polecenie **Narzędzia → <img src="images/Arch_MergeWalls.svg" width=16px> Połącz ściany** z menu.



## Uwagi

-   Narzędzie [Połącz obiekty](Arch_Add/pl.md) może łączyć ściany, nawet jeśli mają one różne wysokości, szerokości i wyrównania.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
base = joinWalls(walls, delete=False)
```

Przykład:


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
⏵ [documentation index](../README.md) > Arch MergeWalls/pl
