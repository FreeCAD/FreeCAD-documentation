---
- GuiCommand:
   Name:Part Line
   Name/pl:Część: Płaszczyzna
   MenuLocation:Część - Utwórz geometrie pierwotne ... - Linia
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Line/pl



## Opis

<img alt="" src=images/Part_Line.svg  style="width:24px;"> **Linia** jest obiektem linii parametrycznej, którą można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). Współrzędne jej punktu początkowego i końcowego odnoszą się do układu współrzędnych zdefiniowanego przez jej właściwość **Umiejscowienie**.

<img alt="" src=images/Part_Line_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Linia wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Wierzchołek 1 - Początek}}

-    **X1|Dystans**: Współrzędna X punktu początkowego linii. Domyślną wartością jest {{Value|0mm}}.

-    **Y1|Dystans**: Współrzędna Y punktu początkowego linii. Domyślną wartością jest {{Value|0mm}}.

-    **Z1|Dystans**: Współrzędna Z punktu początkowego linii. Domyślną wartością jest {{Value|0mm}}.


{{TitleProperty|Vertex 2 - Koniec}}

-    **X2|Distance**: Współrzędna X punktu końcowego linii. Domyślną wartością jest {{Value|0mm}}.

-    **Y2|Distance**: Współrzędna Y punktu końcowego linii. Domyślną wartością jest {{Value|0mm}}.

-    **Z2|Distance**: Współrzędna Z punktu końcowego linii. Domyślną wartością jest {{Value|0mm}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Linia środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
line = FreeCAD.ActiveDocument.addObject("Part::Line", "myLine")
```

-   Gdzie parametr {{Incode|"myLine"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

line = doc.addObject("Part::Line", "myLine")
line.X1 = 1
line.Y1 = 3
line.Z1 = 6
line.X2 = 2
line.Y2 = 3
line.Z2 = 9

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Line/pl
