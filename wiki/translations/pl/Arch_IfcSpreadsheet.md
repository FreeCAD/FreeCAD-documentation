---
 GuiCommand:
   Name: Arch IfcSpreadsheet
   Name/pl: Architektura: Utwórz arkusz IFC
   MenuLocation: Architektura , Narzędzia , Utwórz arkusz IFC
   Workbenches: BIM_Workbench/pl
   Shortcut: **I** **P**
   SeeAlso: Arch_IFC/pl
---

# Arch IfcSpreadsheet/pl



## Opis

To narzędzie tworzy arkusz kalkulacyjny do przechowywania właściwości [IFC](Arch_IFC/pl.md) obiektu.



## Użycie

1.  Wybierz obiekt.
2.  Wywołaj polecenie przy użyciu jednej z kilku metod:
    -   Wybierz opcję **Narzędzia → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Utwórz arkusz IFC...** z menu.
    -   Użyj skrótu klawiszowego: **I** a następnie **P**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
spreadsheet = makeIfcSpreadsheet(archobj=None)
```

-   Tworzy obiekt `spreadsheet`. Opcjonalnie można podać `archobj`.

Przykład: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

spreadsheet = Arch.makeIfcSpreadsheet(Wall)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch IfcSpreadsheet/pl
