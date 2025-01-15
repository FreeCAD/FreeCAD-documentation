---
 GuiCommand:
   Name: Arch RemoveShape
   Name/pl: BIM: Usuń kształt
   MenuLocation: Narzędzia , Usuń kształt z Architektury
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_SplitMesh/pl,  Arch_MeshToShape/pl
---

# Arch RemoveShape/pl



## Opis

Narzędzie **Usuń kształt z Architektury** próbuje usunąć wewnętrzny sześcienny kształt [ściany](Arch_Wall/pl.md) lub [konstrukcji](Arch_Structure/pl.md) i dostosowanie jego właściwości, czyniąc go całkowicie parametrycznym. Narzędzie to będzie działać tylko wtedy, gdy kształt bazowy jest sześcienny *(dokładnie 6 ścian, wszystkie narożniki mają tylko kąty proste)*.



## Użycie

1.  Wybierz obiekt **<img src="images/Arch_Wall.svg" width=16px> [ściany](Arch_Wall/pl.md)** lub **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)**.
2.  Naciśnij przycisk **Narzędzia → <img src="images/Arch_RemoveShape.svg" width=16px> Usuń kształt z Architektury** z menu głównego.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
removeShape(objs, mark=True)
```

-   Pobiera listę obiektów Architektury (`objs`) zbudowanych na sześciennym kształcie i usuwa wewnętrzny kształt, zachowując długość, szerokość i wysokość jako właściwości obiektu Architektury.
    -   
        `objs`
        
        jest pojedynczym obiektem, [ściany](Arch_Wall/pl.md) lub [konstrukcji](Arch_Structure/pl.md), lub ich listą.
-   Jeśli właściwość `mark` ma wartość `True`, obiekty, które nie mogą zostać przetworzone przez tę funkcję, zostaną zaznaczone na czerwono.


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
⏵ [documentation index](../README.md) > Arch RemoveShape/pl
