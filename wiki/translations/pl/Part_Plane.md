---
- GuiCommand:
   Name:Part Plane
   Name/pl:Część: Płaszczyzna
   MenuLocation:Część → Utwórz geometrie pierwotne ... → Płaszczyzna
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Plane/pl



## Opis

<img alt="" src=images/Part_Plane.svg  style="width:24px;"> **Płaszczyzna** środowiska praczy Część to parametryczna prostokątna płaszczyzna, którą można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, płaszczyzna leży na płaszczyźnie XY, z przednim lewym narożnikiem w punkcie początkowym i przednią krawędzią równoległą do osi X.

<img alt="" src=images/Part_Plane_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Płaszczyzna środowiska pracy Część na przykładzie skryptu](images/Part_Plane_Scripting_Example.png )

Poniżej pokazano obiekt Płaszczyzny utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Płaszczyzna wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Płaszczyzna}}

-    **Długość|Length**: Długość płaszczyzny. Jest to wymiar w kierunku X. Domyślnie {{Value|10mm}}.

-    **Szerokość|Length**: Szerokość płaszczyzny. Jest to wymiar w kierunku Y. Domyślnie {{Value|10mm}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Płaszczyzna środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
plane = FreeCAD.ActiveDocument.addObject("Part::Plane", "myPlane")
```

-   Gdzie parametr {{Incode|"myPlane"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

plane = doc.addObject("Part::Plane", "myPlane")
plane.Length = 4
plane.Width = 8
plane.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(20, 75, 60))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/pl
