---
- GuiCommand:
   Name:Part Prism
   Name/pl:Część: Graniastosłup
   MenuLocation:Część → Utwórz geometrie pierwotne ... → Graniastosłup
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Prism/pl



## Opis

<img alt="" src=images/Part_Prism.svg  style="width:24px;"> **Graniastosłup** środowiska praczy Część to parametryczna bryła, którą można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, osie elipsoidy są wyrównane z osiami X, Y i Z, a zatem jej środek znajduje się w punkcie początkowym.

<img alt="" src=images/Part_Prism_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Graniastosłup środowiska pracy Część na przykładzie skryptu](images/Part_Prism_Scripting_Example.png )

Poniżej pokazano obiekt Graniastosłup utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Graniastosłup wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Graniastosłup}}

-    **Wielokąt|IntegerConstraint**: Liczba boków wielokąta. Domyślnie {{Value|6}}.

-    **Circumradius|Length**: Promień okręgu opisującego wielokąt, odległość od środka wielokąta do jednego z jego wierzchołków. Domyślnie {{Value|2mm}}.

-    **Wysokość|Length**: Wysokość wielokąta. Domyślnie {{Value|10mm}}.

-    **Pierwszy Kąt|Angle**: Kąt między kierunkiem wyciągnięcia prostopadłościanu a jego dodatnią osią Z, mierzony wokół jego osi Y. Kąt jest dodatni w kierunku dodatniej osi X. Prawidłowy zakres: {{Value|0° &lt;&#61; value &lt; 90°}}. Wartość domyślna to {{Value|0°}}.

-    **Drugi kąt|Angle**: Kąt między kierunkiem wyciągnięcia prostopadłościanu a jego dodatnią osią Z, mierzony wokół jego osi X. Kąt jest dodatni w kierunku dodatniej osi Y. Prawidłowy zakres: {{Value|0° &lt;&#61; value &lt; 90°}}. Wartość domyślna to {{Value|0°}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Graniastosłup środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
prism = FreeCAD.ActiveDocument.addObject("Part::Prism", "myPrism")
```

-   Gdzie parametr {{Incode|"myPrism"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

prism = doc.addObject("Part::Prism", "myPrism")
prism.Polygon = 5
prism.Circumradius = 10
prism.Height = 50
prism.FirstAngle = 22.5
prism.SecondAngle = 45
prism.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(60, 75, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Prism/pl
