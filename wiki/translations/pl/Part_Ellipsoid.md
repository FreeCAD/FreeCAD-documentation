---
- GuiCommand:
   Name:Part Ellipsoid
   Name/pl:Część Elipsoida
   MenuLocation:Część - Utwórz geometrie pierwotne ... - Elipsoida
   Workbenches:[Część](Part_Workbench/pl.md), [OpenSCAD](OpenSCAD_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Ellipsoid/pl



## Opis

<img alt="" src=images/Part_Ellipsoid.svg  style="width:24px;"> **Elipsoida** środowiska praczy Część to parametryczna bryła, którą można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, osie elipsoidy są wyrównane z osiami X, Y i Z, a zatem jej środek znajduje się w punkcie początkowym.

Elipsoida środowiska pracy Część może być obcięta u góry i/lub u dołu przez zmianę jej właściwości **Kąt1** i/lub **Kąt2**. Można ją przekształcić w segment sfery, zmieniając jej właściwość **Kąt3**.

<img alt="" src=images/Part_Ellipsoid_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Elipsoida środowiska pracy Część na przykładzie skryptu](images/Part_Ellipsoid_Scripting_Example.png )

Poniżej pokazano obiekt Elipsoidy utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Elipsoida wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Elipsoida}}

-    **Promień1|Length**: Promień elipsoidy w kierunku Z. Domyślnie {{Value|2mm}}.

-    **Promień2|Length**: Promień elipsoidy w kierunku X. Domyślnie {{Value|4mm}}.

-    **Promień3|Length**: Promień elipsoidy w kierunku Y. Domyślnie {{Value|4mm}}.

-    **Kąt1|Angle**: Kąt początkowy eliptycznych boków elipsoidy. Prawidłowy zakres: {{Value|-90° &lt;&#61; value &lt; 90°}}. Musi być mniejsza niż **Kąt2**. Domyślnie {{Value|-90°}}.

-    **Kąt2|Angle**: Kąt końcowy eliptycznych boków elipsoidy. Prawidłowy zakres: {{Value|-90° &lt; value &lt;&#61; 90°}}. Wartość ta musi być większa niż **Kąt1**. Wartością domyślną jest {{Value|90°}}. Jeśli całkowity kąt boków elipsy jest mniejszy niż {{Value|180°}}, elipsoida zostanie obcięta i będzie miała płaską ścianę na górze i/lub na dole.

-    **Kąt3|Angle**: Całkowity kąt elipsoidy w jej płaszczyźnie XY. Prawidłowy zakres: {{Value|0° &lt; value &lt;&#61; 360°}}. Domyślna wartość to {{Value|360°}}. Jeśli wartość jest mniejsza niż {{Value|360°}}, wynikowa bryła będzie segmentem elipsoidy.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Elipsoida środowiska pracy Część jest tworzony za pomocą metody dokumentu `addObject()`.


```python
ellipsoid = FreeCAD.ActiveDocument.addObject("Part::Ellipsoid", "myEllipsoid")
```

-   Gdzie parametr {{Incode|"myEllipsoid"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

ellipsoid = doc.addObject("Part::Ellipsoid", "myEllipsoid")
ellipsoid.Radius1 = 2
ellipsoid.Radius2 = 4
ellipsoid.Radius3 = 6
ellipsoid.Angle1 = -90
ellipsoid.Angle2 = 50
ellipsoid.Angle3 = 300
ellipsoid.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(15, 0, 20))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Ellipsoid/pl
