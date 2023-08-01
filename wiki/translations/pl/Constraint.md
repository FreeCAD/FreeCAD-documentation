# Constraint/pl
## Wprowadzenie




W FreeCAD słowo [wiązanie](Constraint/pl.md) jest zwykle używane w odniesieniu do \"reguły\" rysowania kształtów geometrycznych wewnątrz <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicu](Sketch/pl.md) *(klasa `Sketcher::SketchObject`)*. Wiązanie ogranicza położenie pewnego elementu geometrycznego na różne sposoby, na przykład może określać, czy element jest poziomy, pionowy, styczny, równoległy, prostopadły, zbieżny z punktem, współśrodkowy do innego obiektu itp.

Istnieją dwa główne rodzaje wiązań:

-    **Wiązania geometrii**definiują właściwości kształtów bez określania dokładnych wymiarów, np. poziomu, pionu, równoległości, prostopadłości i zbieżności.

-    **Wiązania odniesienia**definiują charakterystykę kształtów poprzez określenie wymiarów, na przykład wymiar długości lub kąta.

Zobacz informacje w środowisku pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md) aby zapoznać się z listą wszystkich więzów, które mogą być zastosowane. Niektóre z nich odnoszą się do linii, niektóre do krzywych, a niektóre do wierzchołków. Zobacz także [Poradnik: Podstawy dla środowiska pracy Szkicownik](Basic_Sketcher_Tutorial/pl.md).

## Użycie

1.  Utwórz szkic albo używając środowiska pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md) lub poprzez środowisko <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).
2.  Naciśnij przycisk:
    -   
        **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Utwórz szkic](Sketcher_NewSketch/pl.md)**
        
        środowiska Szkicownik,

    -   lub **[<img src=images/PartDesign_Body.svg style="width:16px"> [Stwórz zawartość](PartDesign_Body.md)** w środowisku Projekt Części, a następnie **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Utwórz Szkic](PartDesign_NewSketch/pl.md)**.
3.  Kliknij dwukrotnie utworzony szkic, aby przejść do trybu edycji.
4.  Narysuj serię linii używając narzędzia **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Utwórz linię łamaną](Sketcher_CreatePolyline/pl.md)**.
5.  Wybierz jedną z linii i użyj funkcji **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Zwiąż w pionie](Sketcher_ConstrainVertical/pl.md)**.
6.  Wybierz jedną z linii i użyj funkcji **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Zwiąż w poziomie](Sketcher_ConstrainHorizontal/pl.md)**.
7.  Wybierz linię pionową i użyj funkcji **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md)**, przypisz odległość.
8.  Wybierz linię poziomą i użyj funkcji **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md)**, przypisz odległość.

## Uwagi

-   Wiązania są przydatne do tworzenia bardzo precyzyjnych profili, które można przekształcić w bryły wytłaczane za pomocą operacji **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnięcie](PartDesign_Pad/pl.md)** środowiska Projekt Części lub **[<img src=images/Part_Extrude.svg style="width:16px"> [Wyciągnij](Part_Extrude/pl.md)** środowiska Część.
-   Wiązania są używane tylko w [Szkicach](Sketch/pl.md). Inne obiekty 2D, takie jak te utworzone za pomocą środowiska pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) nie rozumieją wiązań. Te ostatnie są po prostu umieszczane w przestrzeni 3D, a ich właściwości określają ich kształt i położenie.


{{Sketcher Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Sketcher](Category_Sketcher.md) > Constraint/pl
