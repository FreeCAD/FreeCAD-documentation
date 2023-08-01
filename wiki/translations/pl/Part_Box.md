---
- GuiCommand:
   Name:Part Box
   Name/pl:Część: Sześcian
   MenuLocation:Część → Bryła pierwotna → Sześcian
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_Primitives/pl.md)
---

# Part Box/pl



## Opis

Polecenie <img alt="" src=images/Part_Box.svg  style="width:24px;"> **Sześcian** środowiska pracy Część tworzy parametryczną bryłę prostopadłościanu [regularny prostopadłościan](https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie** dolna ściana prostopadłościanu leży na płaszczyźnie XY, jej lewy przedni narożnik znajduje się w punkcie odniesienia położenia, a przednia krawędź jest równoległa do osi X.

<img alt="" src=images/Part_Box_Example.png  style="width:400px;">



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Box.svg" width=16px> '''Sześcian'''**.
    -   Wybierz z menu opcję **Część → Bryła pierwotna → <img src="images/Part_Box.svg" width=16px> Sześcian**.
2.  Prostopadłościan zostanie utworzony.
3.  Opcjonalnie zmień wymiary i **Umiejscowienie** prostopadłościanu, wykonując jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt w oknie [Widok drzewa](Tree_view/pl.md):
        1.  Otworzy się panel zadań **Pierwotne bryły geometryczne**.
        2.  Zmień jedną lub więcej właściwości.
        3.  Obiekt jest dynamicznie aktualizowany w oknie [widoku 3D](3D_view/pl.md).
        4.  Naciśnij przycisk **OK**.
    -   Zmień właściwości w [Edytorze właściwości](Property_editor/pl.md).
    -   Zmień **Umiejscowienie** za pomocą <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std: Przemieszczenie](Std_TransformManip/pl.md).



## Przykład

![Sześcian środowiska pracy Część na przykładzie skryptu](images/Part_Box_Scripting_Example.png )

Poniżej pokazano obiekt Sześcian utworzony za pomocą [przykładowego skryptu](#Tworzenie_skrypt.C3.B3w.md).



## Uwagi

-   Prostopadłościan środowiska pracy Część można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). Za jego pomocą można określić wymiary i umiejscowienie w czasie tworzenia.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Prostopadłościan wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Sześcian}}

-    **Długość|długość**: Długość sześcianu. Jest to wymiar w kierunku X. Wartość domyślna to {{Value|10mm}}.

-    **Szerokość|długość**: Szerokość sześcianu. Jest to wymiar w kierunku Y. Wartość domyślna to {{Value|10mm}}.

-    **Wysokość|długość**: Wysokość sześcianu. Jest to wymiar w kierunku Z. Wartość domyślna to {{Value|10mm}}.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Sześcian środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Gdzie parametr {{Incode|myBox}} jest etykietą dla obiektu prostopadłościanu.
-   Zwraca nowo utworzony obiekt typu prostopadłościan.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

box = doc.addObject("Part::Box", "myBox")
box.Length = 4
box.Width = 8
box.Height = 12
box.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/pl
