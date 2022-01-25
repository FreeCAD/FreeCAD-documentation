---
- GuiCommand:/pl
   Name:Part CreatePrimitives
   Name/pl:Część: Bryła pierwotna
   MenuLocation:Część → Utwórz bryły pierwotne ...
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Konstruktor kształtu](Part_Builder/pl.md)
---

# Part Primitives/pl

## Opis

Narzędzie [Bryły pierwotne](Part_Primitives/pl.md) otwiera okno dialogowe do tworzenia dowolnych parametrycznych geometrycznych elementów pierwotnych zdefiniowanych w środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).

<img alt="" src=images/Part_Primitives_example.png  style="width:800px;"> 
*Kształty pierwotne, które mogą być tworzone za pomocą środowiska pracy [Część](Part_Workbench/pl.md).*

## Użycie

Aby stworzyć bryłę pierwotną:

\#\* naciśnij przycisk na pasku narzędzi **<img src="images/Part_Primitives.svg" width=24px> '''Tworzenie pierwotnych brył parametrycznych'''**.

\#\* wybierz z paska menu polecenie **Część → Utwórz bryły pierwotne ...**.

1.  W wyświetlonym oknie dialogowym wybierz typ bryły, ustaw jej parametry i położenie, a następnie naciśnij przycisk **Utwórz**.

Okno dialogowe pozostanie otwarte, abyś mógł później tworzyć kolejne prymitywy.

By edytować bryły dostępne są 2 sposoby:

Używanie okna dialogowego: {{Version/pl|0.19}}

1.  Zaznacz bryłę w drzewie i kliknij na nią dwukrotnie.
2.  Otworzy się to samo okno dialogowe, które zostało użyte do utworzenia tego elementu pierwotnego. Zmień w nim parametry, a otrzymasz podgląd na żywo zmienionego kształtu prymitywu.
3.  Aby zakończyć edycję naciśnij **OK**.

Używając [edytora właściwości](Property_editor/pl.md):

1.  Zaznacz bryłę pierwotną w [widoku drzewa](tree_view/pl.md).
2.  Edytuj jej właściwości w tabeli Właściwości.

## Geometryczne elementy pierwotne 

Można utworzyć następujące bryły pierwotne::

:   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Powierzchnia](Part_Plane/pl.md): tworzy płaszczyznę.
:   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Sześcian](Part_Box/pl.md): tworzy sześcian. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Box.svg  style="width:32px;">. [Utwórz sześcian](Part_Box/pl.md).
:   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Walec](Part_Cylinder/pl.md): tworzy walec. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Cylinder.svg  style="width:32px;">. [Utwórz walec](Part_Cylinder/pl.md).
:   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Stożek](Part_Cone/pl.md): tworzy stożek. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Cone.svg  style="width:32px;">. [Utwórz stożek](Part_Cone/pl.md).
:   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Sfera](Part_Sphere/pl.md): tworzy sferę. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Sphere.svg  style="width:32px;">. [Utwórz sferę](Part_Sphere/pl.md).
:   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Elipsoida](Part_Ellipsoid/pl.md): tworzy elipsoidę.
:   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Torus](Part_Torus/pl.md): tworzy torus. Ten obiekt może być również utworzony za pomocą narzędzia <img alt="" src=images/Part_Torus.svg  style="width:32px;">. [Utwórz torus](Part_Torus/pl.md)
:   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Graniastosłup](Part_Prism/pl.md): tworzy graniastosłup.
:   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Klin](Part_Wedge/pl.md): tworzy klin.
:   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helisa](Part_Helix/pl.md): tworzy helisę.
:   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirala](Part_Spiral/pl.md): tworzy spiralę.
:   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Okrąg](Part_Circle/pl.md): tworzy okrągłą krawędź.
:   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Elipsa](Part_Ellipse/pl.md): tworzy eliptyczną krawędź.
:   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punkt](Part_Point/pl.md): tworzy punkt *(wierzchołek)*.
:   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line/pl.md): tworzy odcinek linii prostej *(krawędź)*.
:   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Wielokąt foremny](Part_RegularPolygon/pl.md): tworzy wielokąt foremny.

## Tworzenie skryptów 


**Zobacz również:**

[skrypty dla detali](Part_scripting/pl.md)

Przetestuj tworzenie elementów pierwotnych za pomocą skryptu. {{Version/pl|0.19}}

Można to uruchomić z [konsoli Python](Python_console/pl.md). 
```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Skrypt ten znajduje się w katalogu instalacyjnym programu i może być badany w celu sprawdzenia, jak budowane są podstawowe elementy pierwotne. 
```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

Można go również wykorzystać jako dane wejściowe do programu. 
```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/pl
