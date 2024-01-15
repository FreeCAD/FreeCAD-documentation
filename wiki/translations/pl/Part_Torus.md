---
 GuiCommand:
   Name: Part Torus
   Name/pl: Część: Torus
   MenuLocation: Część  , Bryła pierwotna , Torus
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_Primitives/pl
---

# Part Torus/pl



## Opis

Narzędzie <img alt="" src=images/Part_Torus.svg  style="width:24px;"> **Torus** środowiska Część, tworzy parametryczną bryłę torusa, kształt zbliżony do pierścienia. Powstaje ona w wyniku przeciągnięcia profilu kolistego wokół okrągłej ścieżki. W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie** kolista ścieżka torusa leży na płaszczyźnie XY, a jej środek znajduje się w punkcie odniesienia położenia.

Torus środowiska Część można przekształcić w fragment torusa, zmieniając jego właściwość **Kąt3**. Zmieniając właściwości **Kąt1** i / lub **Kąt2**, profil pochylony może stać się fragmentem okręgu.

<img alt="" src=images/Part_Torus_Example.png  style="width:400px;">



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Torus.svg" width=16px> [Part Torus](Part_Torus/pl.md)**.
    -   Wybierz z menu opcję **Część → Bryła pierwotna → <img src="images/Part_Torus.svg" width=16px> Torus**.
2.  Tworzony jest torus.
3.  Opcjonalnie zmień wymiary i **Umiejscowienie** torusa, wykonując jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt w oknie [Widok drzewa](Tree_view/pl.md):
        1.  Otworzy się panel zadań **Geometric Primitives**.
        2.  Zmień jedną lub więcej właściwości.
        3.  Obiekt jest dynamicznie aktualizowany w oknie [widoku 3D](3D_view.md).
        4.  Naciśnij przycisk **OK**.
    -   Zmień właściwości w [Edytor właściwości](Property_editor/pl.md).
    -   Zmień **Umiejscowienie** za pomocą narzędzia <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std: Przemieszczenie](Std_TransformManip/pl.md).



## Przykład

![Torus środowiska pracy Część na przykładzie skryptu](images/Part_Torus_Scripting_Example.png )

Poniżej pokazano obiekt Torusa utworzony za pomocą [przykładowego skryptu](#Tworzenie_skrypt.C3.B3w.md).



## Uwagi

-   Torus środowiska pracy Część można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Utwórz geometrie pierwotne](Part_Primitives/pl.md). Za jego pomocą można określić wymiary i umiejscowienie w czasie tworzenia.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Torus wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Torus}}

-    **Promień1|długość**: Promień kolistej ścieżki torusa. Wartość domyślna to {{Value|10mm}}.

-    **Promień2|długość**: Promień okrągłego profilu torusa. Wartość domyślna to {{Value|2mm}}.

-    **Kąt 1|Kąt **: Kąt rozpoczęcia profilu kołowego. Prawidłowy zakres: {{Value|-180° &lt;&#61; wartość &lt;&#61; 180°}}. Wartość domyślna to {{Value|-180°}}.

-    **Kąt 2|Kąt **: Kąt zakończenia profilu kołowego. Prawidłowy zakres: {{Value|-180° &lt;&#61; wartość &lt;&#61; 180°}}. Wartość domyślna to {{Value|180°}}. Jeśli całkowity kąt profilu kołowego jest mniejszy niż {{Value|360°}}, profil będzie miał kształt tortu.

-    **Kąt 3|Kąt **: Kąt ścieżki kołowej torusa. Poprawny zakres: {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie jest to {{Value|360°}}. Jeśli wartość jest mniejsza niż {{Value|360°}}, to bryła wynikowa będzie odcinkiem torusa.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Torus środowiska pracy Część jest tworzony za pomocą metody dokumentu `addObject()`.


```python
torus = FreeCAD.ActiveDocument.addObject("Part::Torus", "myTorus")
```

-   Gdzie parametr {{Incode|"myTorus"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

torus = doc.addObject("Part::Torus", "myTorus")
torus.Radius1 = 20
torus.Radius2 = 10
torus.Angle1 = -90
torus.Angle2 = 45
torus.Angle3 = 270
torus.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 45, 10))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Torus/pl
