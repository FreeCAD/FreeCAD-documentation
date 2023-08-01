---
- GuiCommand:
   Name:Part Ellipse
   Name/pl:Część Elipsoida
   MenuLocation:Część - Utwórz geometrie pierwotne ... - Elipsa
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Ellipse/pl



## Opis

<img alt="" src=images/Part_Ellipse.svg  style="width:24px;"> **Elipsa** środowiska pracy Część to parametryczny kształt, który można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, elipsa leży na płaszczyźnie XY ze środkiem w punkcie początkowym. Jej oś główna jest równoległa do osi X.

Elipsa częściowy jest w rzeczywistości zamkniętym łukiem kołowym w kierunku przeciwnym do ruchu wskazówek zegara, można go przekształcić w łuk, zmieniając jego właściwości **Kąt1** i / lub **Kąt2**.

<img alt="" src=images/Part_Ellipse_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Elipsa środowiska pracy Część na przykładzie skryptu](images/Part_Ellipse_Scripting_Example.png )

Poniżej pokazano obiekt Elipsy utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Elipsa wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Podstawa}}

-    **Główny promień|Length**: Główny promień elipsy lub łuku eliptycznego. Domyślnie {{Value|4mm}}.

-    **Mniejszy promień|Length**: Mniejszy promień elipsy lub łuku eliptycznego. Domyślnie {{Value|2mm}}.

-    **Kąt1|Angle**: Kąt początkowy łuku eliptycznego. Prawidłowy zakres: {{Value|0° &lt; value &lt;&#61; 360°}}. Domyślnie {{Value|0°}}.

-    **Kąt2|Angle**: Kąt końcowy łuku eliptycznego. Prawidłowy zakres: {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie {{Value|360°}}. Jeśli **Kąt1** i **Kąt2** są równe lub jeśli jeden kąt ma wartość {{Value|0°}}, a drugi {{Value|360°}}, tworzona jest pełna elipsa.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Elipa środowiska pracy Część jest tworzony za pomocą metody dokumentu `addObject()`.


```python
ellipse = FreeCAD.ActiveDocument.addObject("Part::Ellipse", "myEllipse")
```

-   Gdzie parametr {{Incode|"myEllipse"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

ellipse = doc.addObject("Part::Ellipse", "myEllipse")
ellipse.MajorRadius = 20
ellipse.MinorRadius = 10
ellipse.Angle1 = 45
ellipse.Angle2 = 135
ellipse.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 45, 10))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Ellipse/pl
