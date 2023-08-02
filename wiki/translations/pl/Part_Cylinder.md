---
- GuiCommand:
   Name: Part Cylinder
   Name/pl: Część: Walec
   MenuLocation: Część -> Bryła pierwotna -> Walec
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_CreatePrimitives/pl
---

# Part Cylinder/pl



## Opis

Narzędzie <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> **Walec** środowiska Część, tworzy parametryczną bryłę walca. Powstaje ona w wyniku wyciągnięcia łuku koła wzdłuż prostej ścieżki. W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie** kolista ścieżka torusa leży na płaszczyźnie XY, a jej środek znajduje się w punkcie odniesienia położenia.

Walec środowiska pracy Część można przekształcić w fragment walca, zmieniając jego właściwość **Kąt**.

<img alt="" src=images/Part_Cylinder_Example.png  style="width:400px;">



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Cylinder.svg" width=16px> [Part Cylinder](Part_Cylinder.md)**.
    -   Wybierz opcję z menu **Część → Bryła pierwotna → <img src="images/Part_Cylinder.svg" width=16px> Walec**.
2.  Zostanie utworzony walec.
3.  Opcjonalnie zmień wymiary i **Umiejscowienie** walca, wykonując jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt w oknie [widoku drzewa](Tree_view/pl.md):
        1.  Otworzy się panel zadań **Pierwotne bryły geometryczne**.
        2.  Zmień jedną lub więcej właściwości.
        3.  Obiekt jest dynamicznie aktualizowany w oknie [widoku 3D](3D_view/pl.md).
        4.  Naciśnij przycisk **OK**.
    -   Zmień właściwości w [Edytorze właściwości](Property_editor/pl.md).
    -   Zmień **Umiejscowienie** za pomocą <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std: Przemieszczenie](Std_TransformManip/pl.md).



## Przykład

![Walec środowiska pracy Część na przykładzie skryptu](images/Part_Cylinder_Scripting_Example.png )

Poniżej pokazano obiekt Walca utworzony za pomocą [przykładowego skryptu](#Tworzenie_skrypt.C3.B3w.md).



## Uwagi

-   Walec środowiska pracy Część można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Utworz geometrie pierwotne](Part_Primitives/pl.md). Za jego pomocą można określić wymiary i umiejscowienie w czasie tworzenia.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Walec wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Walec}}

-    **Promień|długość**: Promień łuku okręgu, który definiuje walec. Wartość domyślna to {{Value|2mm}}.

-    **Wysokość|długość**: Wysokość walca. Wartość domyślna to {{Value|10mm}}.

-    **Kąt|kąt**: Kąt łuku okręgu, który definiuje walec. Poprawny zakres: {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie jest to {{Value|360°}}. Jeśli jest ona mniejsza niż {{Value|360°}}, bryła wynikowa będzie wycinkiem walca.


{{TitleProperty|Graniastosłup}}

-    **Kąt pierwszy|kąt**: Kąt między kierunkiem wyciągania walca a jego dodatnią osią Z, mierzony wokół jego osi Y. Kąt jest dodatni w kierunku dodatniej osi X. Poprawny zakres: {{Value|0° &lt;&#61; wartość &lt; 90°}}. Wartość domyślna to {{Value|0°}}. <small>(v0.20)</small> 

-    **Kąt drugi|kąt**: Kąt między kierunkiem wyciągania walca a jego dodatnią osią Z, mierzony wokół jego osi X. Kąt jest dodatni w kierunku dodatniej osi Y. Poprawny zakres: {{Value|0° &lt;&#61; wartość &lt; 90°}}. Wartość domyślna to {{Value|0°}}. {{Version/pl|0.20}}



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Walec środowiska pracy Część jest tworzony za pomocą metody dokumentu `addObject()`.


```python
cylinder = FreeCAD.ActiveDocument.addObject("Part::Cylinder", "myCylinder")
```

-   Gdzie parametr {{Incode|"myCylinder"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

cylinder = doc.addObject("Part::Cylinder", "myCylinder")
cylinder.Radius = 10
cylinder.Height = 50
cylinder.Placement = App.Placement(App.Vector(5, 10, 15), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/pl
