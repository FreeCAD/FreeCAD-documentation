---
 GuiCommand:
   Name: Arch Remove
   Name/pl: Architektura: Usuń komponent
   MenuLocation: Modyfikacja , Usuń komponent
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_CutPlane/pl, Arch_Add/pl
---

# Arch Remove/pl



## Opis

Narzędzie **Usuń komponent** pozwala na wykonanie 2 rodzajów operacji:

-   Usunięcie komponentu podrzędnego z obiektu Architektury, na przykład usunięcie prostopadłościanu, który został dodany do ściany, jak w **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**.
-   Odjęcie obiektu opartego na [kształcie](Part_Workbench/pl.md) od komponentu Architektury, takiego jak **<img src="images/Arch_Wall.svg" width=16px> [ściana](Arch_Wall/pl.md)** lub **<img src="images/Arch_Structure.svg" width=16px> [konstrukcja](Arch_Structure/pl.md)**.

Odpowiednikiem tego narzędzia jest **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*Prostopadłościan odjęty od ściany, pozostawiający w niej dziurę.*



## Użycie

1.  Wybierz komponent podrzędny wewnątrz obiektu Architektury.
2.  Naciśnij przycisk **<img src="images/Arch_Remove.svg" width=16px> '''Połącz obiekty'''** lub **Modyfikacja → <img src="images/Arch_Remove.svg" width=16px> Połącz obiekty** z menu głównego.

lub

1.  Wybierz obiekty do odjęcia, ostatni wybrany obiekt musi być obiektem Architektury, od którego zostaną odjęte pozostałe obiekty.
2.  Naciśnij przycisk **<img src="images/Arch_Remove.svg" width=16px> '''Usuń komponent'''** lub **Modyfikacja → <img src="images/Arch_Remove.svg" width=16px> Usuń komponent** z menu głównego.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Usuń komponent** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
removeComponents(objectsList, host=None)
```

-   Usuwa podane obiekty w `objectsList` z ich obiektów nadrzędnych.
-   Jeśli podano obiekt `host`, funkcja ta spróbuje dodać obiekty w `objectsList` jako otwory do `host`.

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
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Remove/pl
