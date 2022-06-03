---
- GuiCommand   */pl
   Name   *Part Sphere
   Name/pl   *Part   * Kula
   MenuLocation   *Część → Bryła pierwotna → Kula
   Workbenches   *[Part](Part_Workbench/pl.md)
   SeeAlso   *[Bryły pierwotne](Part_CreatePrimitives/pl.md)
---

# Part Sphere/pl

## Opis

Polecenie <img alt="" src=images/Part_Sphere.svg  style="width   *24px;"> Polecenie **Sfera** środowiska pracy Część tworzy parametryczną bryłę sfery. Jest ona wynikiem obracania profilu łuku okręgu wokół osi. W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie** środek kuli jest umieszczony w punkcie początkowym, a jej osią obrotu jest oś Z.

Sfera środowiska pracy Część może być obcięta u góry i/lub u dołu przez zmianę jej właściwości **Kąt1** i/lub **Kąt2**. Można ją przekształcić w segment sfery, zmieniając jej właściwość **Kąt3**.

<img alt="" src=images/Part_Sphere_Example.png  style="width   *400px;">

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia   *
    -   Naciśnij przycisk **<img src="images/Part_Sphere.svg" width=16px> [Sfera](Part_Sphere/pl.md)**.
    -   Wybierz z menu opcję **Część → Bryła pierwotna → <img src="images/Part_Sphere.svg" width=16px> Sfera**.
2.  Sfera zostanie utworzona.
3.  Opcjonalnie zmień wymiary i **Umiejscowienie** sfery, wykonując jedną z poniższych czynności   *
    -   Kliknij dwukrotnie obiekt w oknie [Widoku drzewa](Tree_view/pl.md)   *
        1.  Otworzy się panel zadań **Pierwotne bryły parametryczne**.
        2.  Zmień jedną lub więcej właściwości.
        3.  Obiekt jest dynamicznie aktualizowany w oknie [widoku 3D](3D_view/pl.md).
        4.  Naciśnij przycisk **OK**.
    -   Zmień właściwości w [Edytorze właściwości](Property_editor/pl.md).
    -   Zmień **Umiejscowienie** za pomocą narzędzia <img alt="" src=images/Std_TransformManip.svg  style="width   *16px;"> [Std   * Przemieszczenie](Std_TransformManip/pl.md).

## Przykład

![Sfera środowiska pracy Część na przykładzie skryptu](images/Part_Sphere_Scripting_Example.png )

Poniżej pokazano obiekt Sfera utworzony za pomocą [przykładowego skryptu](#Tworzenie_skrypt.C3.B3w.md).

## Uwagi

-   Sferę środowiska pracy Część można również utworzyć za pomocą narzędzia <img alt="" src=images/Part_Primitives.svg  style="width   *16px;"> [Geometrie pierwotne](Part_Primitives/pl.md). Za jego pomocą można określić wymiary i umiejscowienie w czasie tworzenia.

## Właściwości

Zobacz również stronę   * [Edytor właściwości](Property_editor/pl.md).

Obiekt Sfera wywodzi się z obiektu [Część   * Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości   *

### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part   * Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Kula}}

-    **Promień|długość**   * Promień sfery. Wartość domyślna to {{Value|5mm}}.

-    **Kąt1|kąt**   * Kąt rozpoczęcia profilu łuku okręgu sfery. Poprawny zakres   * {{Value|-90° &lt;&#61; wartość &lt;&#61; 90°}}. Nie może być równy parametrowi **Kąt2**. Domyślnie jest to wartość {{Value|-90°}}.

-    **Kąt2|kąt**   * Kąt końcowy profilu łuku kołowego sfery. Ważny zakres   * {{Value|-90° &lt;&#61; wartość &lt;&#61; 90°}}. Nie może być równy parametrowi **Kąt1**. Wartość domyślna to {{Value|90°}}. Jeśli całkowity kąt profilu łuku jest mniejszy niż {{Value|180°}}, kula zostanie obcięta i będzie miała płaską powierzchnię u góry i / lub u dołu.

-    **Kąt3|kąt**   * Całkowity kąt obrotu sfery. Dozwolony zakres   * {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie jest to wartość {{Value|360°}}. Jeśli wartość jest mniejsza niż {{Value|360°}}, to bryła wynikowa będzie fragmentem kuli.\* **Promień|długość**   * Promień sfery. Wartość domyślna to {{Value|5mm}}.

-    **Kąt1|kąt**   * Kąt rozpoczęcia profilu łuku okręgu sfery. Poprawny zakres   * {{Value|-90° &lt;&#61; wartość &lt;&#61; 90°}}. Nie może być równy parametrowi **Kąt2**. Domyślnie jest to wartość {{Value|-90°}}.

-    **Kąt2|kąt**   * Kąt końcowy profilu łuku kołowego sfery. Ważny zakres   * {{Value|-90° &lt;&#61; wartość &lt;&#61; 90°}}. Nie może być równy parametrowi **Kąt1**. Wartość domyślna to {{Value|90°}}. Jeśli całkowity kąt profilu łuku jest mniejszy niż {{Value|180°}}, kula zostanie obcięta i będzie miała płaską powierzchnię u góry i / lub u dołu.

-    **Kąt3|kąt**   * Całkowity kąt obrotu sfery. Dozwolony zakres   * {{Value|0° &lt; wartość &lt;&#61; 360°}}. Domyślnie jest to wartość {{Value|360°}}. Jeśli wartość jest mniejsza niż {{Value|360°}}, to bryła wynikowa będzie fragmentem kuli.

## Tworzenie skryptów 

Zobacz również   * [Dokumentacja API generowana automatycznie](https   *//freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Sfera środowiska pracy Część jest tworzona za pomocą metody `addObject()`.


```python
sphere = FreeCAD.ActiveDocument.addObject("Part   *   *Sphere", "mySphere")
```

-   Gdzie parametr {{Incode|"mySphere"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład   *


```python
import FreeCAD as App

doc = App.activeDocument()

sphere = doc.addObject("Part   *   *Sphere", "mySphere")
sphere.Radius = 20
sphere.Angle1 = -30
sphere.Angle2 = 45
sphere.Angle3 = 90
sphere.Placement = App.Placement(App.Vector(3, 9, 11), App.Rotation(75, 60, 30))

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/pl
