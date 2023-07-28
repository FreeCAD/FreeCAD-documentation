---
- GuiCommand:/pl
   Name:Part Circle
   Name/pl:Part Okrąg
   MenuLocation:Część → Utwórz geometrie pierwotne ... → Okrąg
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Circle/pl



## Opis

<img alt="" src=images/Part_Circle.svg  style="width:24px;"> **Okrąg** środowiska pracy Część to parametryczny kształt, który można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, okrąg leży na płaszczyźnie XY ze środkiem w punkcie początkowym.

Okrąg częściowy jest w rzeczywistości zamkniętym łukiem kołowym w kierunku przeciwnym do ruchu wskazówek zegara, można go przekształcić w łuk, zmieniając jego właściwości **Kąt1** i / lub **Kąt2**.

<img alt="" src=images/Part_Circle_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).

Okrąg środowiska pracy Część można alternatywnie utworzyć, wybierając trzy punkty:

1.  W panelu zadań <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Pierwotne bryły parametryczne](Part_Primitives/pl.md) wybierz opcję **<img src="images/Part_Circle.svg" width=16px> Okrąg** z rozwijanej listy.
2.  Naciśnij przycisk **Z trzech punktów**.
3.  Wybierz trzy wierzchołki w oknie [widoku 3D](3D_view/pl.md). Nie ma potrzeby przytrzymywania klawisza **Ctrl**.
4.  Zostanie utworzony okrąg.
5.  Wybrane wierzchołki są używane tylko w czasie tworzenia do obliczenia parametrów dla właściwości **Promień** i **Umiejscowienie** okręgu.



## Przykład

![Okrąg środowiska pracy Część na przykładzie skryptu](images/Part_Circle_Scripting_Example.png )

Poniżej pokazano obiekt Okrąg utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Okrąg wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Podstawa}}

-    **Promień|Length**: Promień okręgu lub łuku kołowego. Domyślnie {{Value|2mm}}.

-    **Kąt1|Angle**: Kąt początkowy łuku kołowego. Prawidłowy zakres: {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie {{Value|0°}}.

-    **Kąt2|Angle**: Kąt końcowy łuku kołowego. Prawidłowy zakres: {{Value|0° &lt; value &lt;&#61; 360°}}. Domyślnie {{Value|360°}}. Jeśli **Kąt1** i **Kąt2** są równe lub jeśli jeden kąt ma wartość {{Value|0°}}, a drugi {{Value|360°}}, tworzony jest pełny okrąg.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Okrąg środowiska pracy Część jest tworzona za pomocą metody `addObject()`.


```python
circle = FreeCAD.ActiveDocument.addObject("Part::Circle", "myCircle")
```

-   Gdzie parametr {{Incode|"myCircle"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

circle = doc.addObject("Part::Circle", "myCircle")
circle.Radius = 10
circle.Angle1 = 45
circle.Angle2 = 225
circle.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 45, 10))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle/pl
