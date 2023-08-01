---
- GuiCommand:/pl
   Name:Part Point
   Name/pl:Część: Punkt
   MenuLocation:Część → Utwórz geometrie pierwotne ... → Punkt
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Point/pl



## Opis

<img alt="" src=images/Part_Point.svg  style="width:24px;"> **Punkt** to punkt parametryczny, który można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). Jego współrzędne są względne w stosunku do układu współrzędnych zdefiniowanego przez jego właściwość **Umiejscowienie**.



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Punkt wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Podstawa}}

-    **X|Distance**: Współrzędna X punktu. Domyślną wartością jest {{Value|0mm}}.

-    **Y|Distance**: Współrzędna Y punktu. Domyślną wartością jest {{Value|0mm}}.

-    **Z|Distance**: Współrzędna Z punktu. Domyślną wartością jest {{Value|0mm}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Punkt środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
point = FreeCAD.ActiveDocument.addObject("Part::Vertex", "myPoint")
```

-   Gdzie parametr {{Incode|"myPoint"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

point = doc.addObject("Part::Vertex", "myPoint")
point.X = 1
point.Y = 2
point.Z = 3

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Point/pl
