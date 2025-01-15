---
 GuiCommand:
   Name: Arch Add
   Name/pl: Architektura: Połącz obiekty
   MenuLocation: Modyfikacja , Połącz obiekty
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_Remove/pl
---

# Arch Add/pl



## Opis

Narzędzie Add pozwala na wykonywanie 4 rodzajów operacji:

-   Dodawanie obiektów opartych na [kształcie](Part_Workbench/pl.md) do komponentu Architektury, takich jak **<img src="images/Arch_Wall.svg" width=16px> [ściana](Arch_Wall/pl.md)** lub **<img src="images/Arch_Structure.svg" width=16px> [konstrukcja](Arch_Structure/pl.md)**. Obiekty te stają się częścią komponentu Architektonicznego i pozwalają modyfikować jego kształt, zachowując jego podstawowe właściwości, takie jak szerokość i wysokość.
-   Dodawanie komponentów Architektury, takich jak **<img src="images/Arch_Wall.svg" width=16px> [ściana](Arch_Wall/pl.md)** lub **<img src="images/Arch_Structure.svg" width=16px> [konstrukcja](Arch_Structure/pl.md)**, do obiektu Architektonicznego opartego na grupie, takiego jak **<img src="images/Arch_Floor.svg" width=16px> [Piętra](Arch_Floor/pl.md)**.
-   Dodawanie **<img src="images/Arch_Axis.svg" width=16px> [Systemu osi](Arch_Axis/pl.md)** do **<img src="images/Arch_Structure.svg" width=16px> [obiektów konstrukcyjnych](Arch_Structure/pl.md)**.
-   Dodawanie obiektów do **<img src="images/Arch_SectionPlane.svg" width=16px> [płaszczyzny przekroju](Arch_SectionPlane/pl.md)**.

Odpowiednikiem tego narzędzia jest **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> 
*Prostopadłościan dodana do ściany jako komponent.*



## Użycie

1.  Wybierz obiekty, które mają zostać dodane. Ostatni wybrany obiekt będzie głównym obiektem Architektury.
2.  Naciśnij przycisk **<img src="images/Arch_Add.svg" width=16px> '''Połącz obiekty'''** lub użyj narzędzia **Modyfikacja → <img src="images/Arch_Add.svg" width=16px> Połącz obiekty** z menu głównego.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Połącz obiekty** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:

:   
    
```python
    addComponents(objectsList, host)
    
```
    





:   Powyższy fragment kodu dodaje podane obiekty w `objectsList` do podanego obiektu `host`.

**Uwaga:** `objectsList` może być indywidualnym obiektem lub listą obiektów.

Przykład:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Add/pl
