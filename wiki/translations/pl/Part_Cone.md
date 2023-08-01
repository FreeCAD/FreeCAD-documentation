---
- GuiCommand:
   Name:Part Cone
   Name/pl:Część: Stożek
   MenuLocation:Część → Bryła pierwotna → Stożek
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_CreatePrimitives/pl.md)
---

# Part Cone/pl



## Opis

Polecenie <img alt="" src=images/Part_Cone.svg  style="width:24px;"> **Stożek** środowiska pracy Część tworzy parametryczną bryłę stożka. W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie** dolna ściana stożka leży na płaszczyźnie XY, a jej środek jest w punkcie początkowym.

Domyślnie stożek środowiska Części jest ścięty. Można go przekształcić w pełny, nieobcięty stożek, zmieniając jego właściwość **Promień1** lub **Promień2** na zero. Można go przekształcić w fragment stożka, zmieniając jego właściwość **Kąt**.

<img alt="" src=images/Part_Cone_Example.png  style="width:400px;">



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Cone.svg" width=16px> [Stożek](Part_Cone/pl.md)**.
    -   Wybierz z menu opcję **Część → Bryła pierwotna → <img src="images/Part_Cone.svg" width=16px> Stożek**.
2.  Tworzony jest stożek.
3.  Opcjonalnie zmień wymiary i **Umiejscowienie** stożka, wykonując jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt w oknie [widoku drzewa](Tree_view/pl.md):
        1.  Otworzy się panel zadań **Pierwotne bryły parametryczne**.
        2.  Zmień jedną lub więcej właściwości.
        3.  Obiekt jest dynamicznie aktualizowany w oknie [widoku 3D](3D_view/pl.md).
        4.  Naciśnij przycisk **OK**.
    -   Zmień właściwości w [Edytorze właściwości](Property_editor/pl.md).
    -   Zmień **Umiejscowienie** za pomocą narzędzia <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std: Przemieszczenie](Std_TransformManip/pl.md).



## Przykład

![Stożek środowiska pracy Część na przykładzie skryptu](images/Part_Cone_Scripting_Example.png )

Poniżej pokazano obiekt Stożka utworzony za pomocą [przykładowego skryptu](#Tworzenie_skrypt.C3.B3w.md).



## Uwagi

-   Stożek środowiska pracy Część można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Utwórz geometrie pierwotne](Part_Primitives/pl.md). Za jego pomocą można określić wymiary i umiejscowienie w czasie tworzenia.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Stożek wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Stożek}}

-    **Promień1|długość**: Promień dolnej powierzchni stożka. Może mieć wartość {{Value|0mm}}, jeśli parametr **Promień2** jest większy niż {{Value|0mm}}. Wartość domyślna to {{Value|2mm}}.

-    **Promień2|długość**: Promień górnej powierzchni stożka. Może mieć wartość {{Value|0mm}}, jeśli **Promień1** jest większy niż {{Value|0mm}}. Wartość domyślna to {{Value|4mm}}.

-    **Wysokość|długość**: Wysokość stożka. Wartość domyślna to {{Value|10mm}}.

-    **Kąt|kąt**: Kąt łuku okręgu, który definiuje górną i dolną ścianę stożka. Poprawny zakres: {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie jest to {{Value|360°}}. Jeśli wartość jest mniejsza niż {{Value|360°}}, to bryła wynikowa będzie segmentem stożka.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Stożek środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Gdzie parametr {{Incode|"myCone"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

cone = doc.addObject("Part::Cone", "myCone")
cone.Radius1 = 5
cone.Radius2 = 10
cone.Height = 50
cone.Angle = 270
cone.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 60, 15))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/pl
