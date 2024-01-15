---
 GuiCommand:
   Name: Part Wedge
   Name/pl: Część: Klin
   MenuLocation: Część , Utwórz geometrie pierwotne ... , Klin
   Workbenches: Part_Workbench/pl, OpenSCAD_Workbench/pl
   SeeAlso: Part_Primitives/pl
---

# Part Wedge/pl



## Opis

<img alt="" src=images/Part_Wedge.svg  style="width:24px;"> **Klin** środowiska praczy Część to parametryczna bryła, którą można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). Ma od czterech do sześciu płaskich ścian. Jest on definiowany przez wirtualne przednie i tylne płaszczyzny główne, na których tworzona jest prostokątna ściana *(domyślnie)*, pojedyncza prosta krawędź lub pojedynczy wierzchołek. Te kształty bazowe definiują cztery czworoboczne lub trójkątne ściany, które je łączą. Wynikowa bryła jest prawdziwym klinem tylko wtedy, gdy jeden z kształtów bazowych jest ścianą prostokątną, a drugi krawędzią prostą. W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, wirtualne przednie i tylne główne płaszczyzny klina są równoległe do płaszczyzny XZ, a krawędzie kształtów bazowych są równoległe do osi X lub Z. Wszystkie jego współrzędne odnoszą się do tego układu współrzędnych.

<img alt="" src=images/Part_Wedge_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Klin środowiska pracy Część na przykładzie skryptu](images/Part_Plane_Scripting_Example.png )

Poniżej pokazano obiekt Klina utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Uwagi

-   Wartości współrzędnych klina muszą być takie, aby można było utworzyć prawidłową bryłę. Oznacza to, że przednie i tylne kształty bazowe mogą być pojedynczymi krawędziami, ale nie mogą być równoległe. A jeśli jeden z kształtów bazowych jest wierzchołkiem, drugi kształt musi być ścianą prostokątną.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Klina wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Klin}}

-    **Xmin|Distance**: Najmniejsza współrzędna X ściany czołowej klina. Domyślnie {{Value|0mm}}.

-    **Ymin|Distance**: Współrzędna Y przedniej ściany klina. Domyślnie {{Value|0mm}}.

-    **Zmin|Distance**: Najmniejsza współrzędna Z przedniej ściany klina. Domyślnie {{Value|0mm}}.

-    **X2min|Distance**: Najmniejsza współrzędna X tylnej ściany klina. Domyślnie {{Value|2mm}}.

-    **Z2min|Distance**: Najmniejsza współrzędna Z tylnej ściany klina. Domyślnie {{Value|2mm}}.

-    **Xmax|Distance**: Największa współrzędna X przedniej ściany klina. Domyślnie {{Value|10mm}}.

-    **Ymax|Distance**: Współrzędna Y tylnej ściany klina. Domyślnie {{Value|10mm}}.

-    **Zmax|Distance**: Największa współrzędna Z przedniej ściany klina. Domyślnie {{Value|10mm}}.

-    **X2max|Distance**: Największa współrzędna X tylnej ściany klina. Domyślnie {{Value|8mm}}.

-    **Z2max|Distance**: Największa współrzędna Z tylnej ściany klina. Domyślnie {{Value|8mm}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Klin środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
wedge = FreeCAD.ActiveDocument.addObject("Part::Wedge", "myWedge")
```

-   Gdzie parametr {{Incode|"myWedge"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

wedge = doc.addObject("Part::Wedge", "myWedge")
wedge.Xmin = 1
wedge.Ymin = 2
wedge.Zmin = 3
wedge.X2min = 4
wedge.Z2min = 6
wedge.Xmax = 15
wedge.Ymax = 20
wedge.Zmax = 55
wedge.X2max = 10
wedge.Z2max = 12
wedge.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Wedge/pl
