---
- GuiCommand:
   Name:Part RegularPolygon
   Name/pl:Część: Wielokąt foremny
   MenuLocation:Część → Utwórz geometrie pierwotne ... → Wielokąt foremny
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   Version:0.14
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part RegularPolygon/pl



## Opis

<img alt="" src=images/Part_RegularPolygon.svg  style="width:24px;"> **Wielokąt foremny** to parametryczny obiekt kształtu, który można utworzyć za pomocą <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> polecenia [Part Primitives](Part_Primitives.md) [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, wielokąt leży na płaszczyźnie XY ze środkiem w punkcie początkowym i jednym z wierzchołków na osi X.

<img alt="" src=images/Part_RegularPolygon_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Wielokąt foremny środowiska pracy Część na przykładzie skryptu](images/Part_RegularPolygon_Scripting_Example.png )

Poniżej pokazano obiekt Wielokąt foremny utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Wielokąt foremny wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Wielokąt foremny}}

-    **Wielokąt|IntegerConstraint**: Liczba boków wielokąta. Domyślną wartością jest {{Value|6}}.

-    **Circumradius|Length**: Promień okręgu opisującego wielokąt, odległość od środka wielokąta do jednego z jego wierzchołków. Domyślną wartością jest {{Value|2mm}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Wielokąt foremny środowiska pracy Część jest tworzony za pomocą metody dokumentu `addObject()`.


```python
poly = FreeCAD.ActiveDocument.addObject("Part::RegularPolygon", "myPolygon")
```

-   Gdzie parametr {{Incode|"myPolygon"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

poly = doc.addObject("Part::RegularPolygon", "myPolygon")
poly.Polygon = 5
poly.Circumradius = 8
poly.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(60, 30, 15))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RegularPolygon/pl
