---
 GuiCommand:
   Name: Arch Fence
   Name/pl: Architektura: Ogrodzenie
   MenuLocation: 3D / BIM , Ogrodzenie
   Workbenches: BIM_Workbench/pl
   Version: 0.19
---

# Arch Fence/pl



## Opis

Narzędzie **Ogrodzenie** jest obiektem, który buduje ogrodzenie poprzez powtarzanie pojedynczego słupka i sekcji wzdłuż danej ścieżki.

<img alt="" src=images/Arch_Fence_description_example.png  style="width:600px;">



## Użycie



### Tworzenie od podstaw 

1.  Użyj wybranego środowiska pracy, aby utworzyć pojedynczy słupek ogrodzenia i pojedynczą sekcję.
2.  Stwórz ścieżkę, którą ma podążać ogrodzenie, używając środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md) lub [Rysunek Roboczy](Draft_Workbench/pl.md).
3.  Przełącz się z powrotem do środowiska [BIM](BIM_Workbench.md).
4.  Wybierz sekcję, słupek i ścieżkę dokładnie w tej kolejności.
5.  Naciśnij przycisk **<img src="images/Arch_Fence.svg" width=16px> '''Ogrodzenie'''**.



## Opcje

Na razie narzędzie przyjmuje następujące założenia

1.  Ścieżka jest rysowana na płaszczyźnie XY.
2.  Przekrój i słupek są rysowane w punkcie początkowym, tak aby stały pionowo w widoku z przodu.



## Właściwości



### Dane

-    **Ścieżka**: Ścieżka, którą powinno podążać ogrodzenie.

-    **Słupek**: Pojedynczy słupek ogrodzenia do powtórzenia.

-    **Sekcja**: Pojedyncza sekcja do powtórzenia.

-    **lLiczba słupków**: Całkowita liczba słupków użytych do budowy ogrodzenia. Jest ona obliczana automatycznie.

-    **lLiczba sekcji**: Całkowita liczba sekcji użytych do budowy ogrodzenia. Jest ona obliczana automatycznie.



### Widok

-    **Używaj oryginalnych kolorów**: Po ustawieniu na {{True/pl}} ogrodzenie użyje kolorów z oryginalnej sekcji i słupka. W przeciwnym razie do pokolorowania ogrodzenia zostanie użyty Kolor Kształtu ogrodzenia.



## Uwagi

-   Obiekt Ogrodzenie został wprowadzony w FC v0.19 przez użytkownika furti.
-   [Wątek na forum](https://forum.freecadweb.org/viewtopic.php?t=36149) omawiający funkcjonalność Ogrodzenia.



## Tworzenie skryptów 

Narzędzie **Ogrodzenie** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Fence = buildFence(section, post, path)
```

Przykład:


```python
import FreeCAD
import Part
import Arch

parts = []

parts.append(Part.makeBox(2000, 50, 30, FreeCAD.Vector(0, 0, 1000 - 30)))
parts.append(Part.makeBox(2000, 50, 30))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(0, 15, 30)))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(1980, 15, 30)))

for i in range(8):
    parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector((2000 / 9 * (i + 1)) - 10, 15, 30)))

Part.show(Part.makeCompound(parts), "Fence_section")
fence_section = FreeCAD.ActiveDocument.Fence_section

sketch = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject", "Path")
sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(20000, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(20000, 0, 0), FreeCAD.Vector(20000, 20000, 0)), False)

post = Part.makeBox(100, 100, 1000, FreeCAD.Vector(0, 0, 0))
Part.show(post, "Post")
post = FreeCAD.ActiveDocument.Post

Fence = Arch.buildFence(fence_section, post, sketch)
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Fence/pl
