---
- GuiCommand:
   Name:Part Tube
   Name/pl:Część: Rura
   MenuLocation:Część → Bryła pierwotna → Utwórz rurę
   Workbenches:[Część](Part_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Utwórz geometrie pierwotne](Part_Primitives/pl.md)
---

# Part Tube/pl



## Opis

Polecenie <img alt="" src=images/Part_Tube.svg  style="width:24px;"> **Rura** środowiska pracy Część tworzy parametryczną bryłę rury. W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie** dolna ściana stożka leży na płaszczyźnie XY, a jej środek jest w punkcie początkowym.

<img alt="" src=images/Part_Tube_Example.png  style="width:400px;">



## Użycie



### Tworzenie

1.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Tube.svg" width=16px> '''Utwórz rurę'''**.
    -   Wybierz z menu opcję **Część → Bryła pierwotna → <img src="images/Part_Tube.svg" width=16px> Utwórz rurę**.
2.  Otworzy się panel zadań **Rura**, a podgląd rury zostanie wyświetlony w oknie [widoku 3D](3D_view/pl.md).
3.  Określ wymiary.
4.  Podgląd jest dynamicznie aktualizowany.
5.  Naciśnij przycisk **OK**.
6.  Rura zostanie utworzona.
7.  Opcjonalnie zmień **Umiejscowienie** rury funkcją [Edytor właściwości](Property_editor/pl.md) lub za pomocą polecenia <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Przemieszczenie](Std_TransformManip/pl.md).



### Edycja

1.  Kliknij dwukrotnie rurę w oknie [Widok Drzewa](Tree_view/pl.md).
2.  Otworzy się panel zadań **Rura**.
3.  Zmień jeden lub więcej wymiarów.
4.  Rura jest dynamicznie aktualizowana w oknie [widoku 3D](3D_view/pl.md).
5.  Naciśnij przycisk **OK**.



## Przykład

![Rura środowiska Część z przykładu skryptu](images/Part_Tube_Scripting_Example.png )

Poniżej przedstawiono obiekt Rury utworzony za pomocą przykładu [tworzenie skryptów](#Tworzenie_skryptów.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Rura wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Rura}}

-    **Wysokość|Length**: Wysokość rury. Domyślnie {{Value|10mm}}.

-    **Promień wewnętrzny|Length**: Wewnętrzny promień rury. Musi być mniejszy niż **Promień zewnętrzny**. Może mieć wartość {{Value|0}}. Domyślnie {{Value|2mm}}.

-    **Promień zewnętrzny|Length**: Zewnętrzny promień rury. Musi być większy niż **Promień wewnętrzny**. Domyślnie {{Value|5mm}}.



## Tworzenie skryptów 

Poniżej przedstawiono obiekt Part Tube utworzony za pomocą przykładu [tworzenia skryptów](#Tworzenie_skryptów.md).

Obiekt Rura można utworzyć za pomocą metody {{Incode|addTube()}} ({{Version/pl|0.20}}) modułu Kształty:


```python
tube = Shapes.addTube(FreeCAD.ActiveDocument, "myTube")
```

-   Gdzie parametr {{Incode|"myTube"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App
from BasicShapes import Shapes

doc = App.activeDocument()

tube = Shapes.addTube(FreeCAD.ActiveDocument, "myTube")
tube.Height = 20
tube.InnerRadius = 2
tube.OuterRadius = 3
tube.Placement = App.Placement(App.Vector(2, 4, 5), App.Rotation(60, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Tube/pl
