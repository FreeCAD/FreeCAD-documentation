---
 GuiCommand:
   Name: Part Primitives
   Name/pl: Część: Utwórz geometrie pierwotne
   MenuLocation: Część , Utwórz geometrie pierwotne ...
   Workbenches: Part_Workbench/pl, OpenSCAD_Workbench/pl
   SeeAlso: Part_Builder/pl
---

# Part Primitives/pl



## Opis

Narzędzie <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> **Utwórz geometrie pierwotne \...** otwiera okno dialogowe do tworzenia jednego lub więcej prymitywów parametrycznych. Dostępnych jest 16 typów brył pierwotnych.

<img alt="" src=images/Part_Primitives_example.png  style="width:600px;"> 
*Geometrie pierwotne, które mogą być tworzone za pomocą tego narzędzia*



## Użycie



### Tworzenie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Primitives.svg" width=16px> [Utwórz geometrie pierwotne](Part_Primitives/pl.md)**.
    -   Wybierz polecenie z menu **Część → <img src="images/Part_Primitives.svg" width=16px> Utwórz geometrie pierwotne ...**.
2.  Otworzy się panel zadań **Pierwotne bryły geometryczne**.
3.  Wybierz typ elementu pierwotnego z listy rozwijanej.
4.  Określ właściwości.
5.  Naciśnij przycisk **Utwórz**.
6.  Zostanie utworzony element pierwotny.
7.  Zauważ, że panel zadań pozostaje otwarty.
8.  Opcjonalnie utwórz dodatkowe prymitywy.
9.  Naciśnij przycisk **Zamknij**, aby zamknąć panel zadań i zakończyć polecenie.



### Edycja

1.  Kliknij dwukrotnie obiekt pierwotny w oknie [widoku drzewa](Tree_view/pl.md).
2.  Otworzy się panel zadań **Pierwotne bryły geometryczne**.
3.  Zmień jedną lub więcej właściwości.
4.  Obiekt jest dynamicznie aktualizowany w oknie [widoku 3D](3D_view/pl.md).
5.  Naciśnij przycisk **OK**.

Właściwości elementu pierwotnego można również zmienić w [Edytorze właściwości](Property_editor/pl.md), a jego **Umiejscowienie** można również zmienić za pomocą narzędzia <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std: Przemieszczenie](Std_TransformManip/pl.md).



## Geometryczne elementy pierwotne 

Można utworzyć następujące elementy pierwotne:

-   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Płaszczyzna](Part_Plane/pl.md): Tworzy płaszczyznę.
-   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Sześcian](Part_Box/pl.md): Tworzy prostopadłościan regularny. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Utwórz sześcian](Part_Box/pl.md).
-   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Walec](Part_Cylinder/pl.md): Tworzy walec. Ten obiekt może być również utworzony za pomocą <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Utwórz walec](Part_Cylinder/pl.md).
-   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Stożek](Part_Cone/pl.md): Tworzy stożek. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Utwórz stożek](Part_Cone/pl.md).
-   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Sfera](Part_Sphere/pl.md): Tworzy sferę. Ten obiekt może być również utworzony za pomocą <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Utwórz sferę](Part_Sphere/pl.md).
-   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Elipsoida](Part_Ellipsoid/pl.md): Tworzy elipsoidę.
-   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Torus](Part_Torus/pl.md): Tworzy torus. Ten obiekt może być również utworzony za pomocą <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Utwórz torus](Part_Torus/pl.md).
-   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Graniastosłup](Part_Prism/pl.md): Tworzy graniastosłup.
-   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Klin](Part_Wedge/pl.md): Tworzy klin.
-   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helisa](Part_Helix/pl.md): Tworzy helisę.
-   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirala](Part_Spiral/pl.md): Tworzy spiralę.
-   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Okrąg](Part_Circle/pl.md): Tworzy łuki okręgów.
-   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Elipsa](Part_Ellipse/pl.md): Tworzy łuk eliptyczny.
-   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punkt](Part_Point/pl.md): Tworzy punkt.
-   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linia](Part_Line/pl.md): Tworzy linię.
-   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Wielokąt foremny](Part_RegularPolygon/pl.md): Tworzy wielokąt foremny.



## Uwagi

-   Polecenie Utwórz geometrie pierwotne środowiska Część nie tworzy <img alt="" src=images/Part_Tube.svg  style="width:16px;"> [Rury](Part_Tube/pl.md).



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Istnieje skrypt środowiska Python do testowania tworzenia elementów pierwotnych. Można go uruchomić z [konsoli Python](Python_console/pl.md):


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Skrypt ten znajduje się w katalogu instalacyjnym programu i może być badany w celu sprawdzenia, jak budowane są geometrie pierwotne:


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

Można go także wykorzystać do wprowadzenia danych do programu:


```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/pl
