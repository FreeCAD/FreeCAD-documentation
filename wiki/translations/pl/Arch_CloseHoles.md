---
 GuiCommand:
   Name: Arch CloseHoles
   Name/pl: Architektura: Zamknij otwory
   MenuLocation: Narzędzia , Zamknij otwory
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_Check/pl
---

# Arch CloseHoles/pl



## Opis

Narzędzie to identyfikuje otwory *(okrągłe sekwencje otwartych krawędzi)* w obiekcie [kształtu](Part_Workbench/pl.md) i próbuje je zamknąć poprzez dodanie nowej ściany utworzonej z tej sekwencji krawędzi. Należy jednak upewnić się, że wynikiem jest bryła.



## Użycie

1.  Wybierz obiekt [kształtu](Part_Workbench/pl.md).
2.  Wybierz z menu opcję **Architektura → Narzędzia → <img src="images/Arch_CloseHoles.svg" width=16px> Zamknij otwory**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
solid = closeHole(shape)
```

-   Zamyka otwór w `shape`, który jest `Part.Shape` i zwraca nowy obiekt `solid`.

Przykład: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute() 

solid = Arch.closeHole(Wall.Shape)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch CloseHoles/pl
