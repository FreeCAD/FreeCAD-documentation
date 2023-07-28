---
- GuiCommand:/pl
   Name:Part Spiral
   Name/pl:Część: Spirala
   MenuLocation:Część → Utwórz geometrie pierwotne ... → Spirala
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Spiral/pl



## Opis

<img alt="" src=images/Part_Spiral.svg  style="width:24px;"> **Spirala** środowiska Część to parametryczny kształt, który można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, spirala leży na płaszczyźnie XY ze środkiem w punkcie odniesienia położenia i punktem początkowym na osi X. Poszerza się, gdy obraca się w kierunku przeciwnym do ruchu wskazówek zegara.

<img alt="" src=images/Part_Spiral_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Spirala środowiska pracy Część na przykładzie skryptu](images/Part_Spiral_Scripting_Example.png )

Poniżej pokazano obiekt Spirala utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Spirala wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Spirala}}

-    **Przyrost|Length**: Odległość między dwoma kolejnymi zwojami spirali. Domyślna wartość to {{Value|1mm}}.

-    **Promień|Length**: Promień początkowy spirali, odległość między jej środkiem a punktem początkowym. Może być {{Value|0mm}}. Domyślna wartość to {{Value|1mm}}.

-    **Rotacje|QuantityConstraint**: Liczba obrotów spirali. Domyślnie {{Value|2}}.

-    **Segment Length|QuantityConstraint**: Liczba obrotów na poddział spirali. Domyślną wartością jest {{Value|1}}, co oznacza, że każdy pełny obrót spirali jest oddzielnym segmentem. Użyj wartości {{Value|0}}, aby pominąć podział.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Spirala środowiska pracy Część jest tworzona za pomocą metody `addObject()`.


```python
spiral = FreeCAD.ActiveDocument.addObject("Part::Spiral", "mySpiral")
```

-   Gdzie parametr {{Incode|"mySpiral"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

spiral = doc.addObject("Part::Spiral", "mySpiral")
spiral.Growth = 2
spiral.Radius = 3
spiral.Rotations = 4
spiral.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Spiral/pl
