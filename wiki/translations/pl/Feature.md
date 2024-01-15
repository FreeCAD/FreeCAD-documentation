# Feature/pl
## Wprowadzenie

W FreeCAD słowo \"[Cecha](Feature/pl.md)\" jest zwykle używane w odniesieniu do obiektu [Cechy](PartDesign_Feature/pl.md) środowiska Projekt Części *(klasa `PartDesign::Feature`)*, którya jest zdefiniowana przez środowiskoa pracy [Projekt Części](PartDesign_Workbench/pl.md). Jest to operacja lub krok modelowania wykonywany w celu utworzenia lub modyfikacji [Kształtu](Shape/pl.md) bryły zgodnie z paradygmatem [Edycja cech](Feature_editing/pl.md).

Więcej informacji na temat tego typu obiektów można znaleźć na stronie [Projekt części: Cecha](PartDesign_Feature/pl.md).



## Użycie

1.  Przełącz się do środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).
2.  Naciśnij przycisk **[<img src=images/PartDesign_Body.svg style="width:16px"> [Utwórz Zawartość](PartDesign_Body/pl.md)**.
3.  Naciśnij przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Utwórz szkic](PartDesign_NewSketch/pl.md)**, aby utworzyć nowy [Szkic](Sketch/pl.md).
4.  Utwórz zamkniętą polilinię, a następnie użyj narzędzia **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnij](PartDesign_Pad/pl.md)** do wyciągnięcia szkicu i utworzenia początkowej bryły. Ta początkowa bryła jest początkową Cechą.
5.  Dodaj więcej szkiców i podkładek oraz użyj innych narzędzi środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md), aby zmodyfikować i przekształcić bryłę początkową. Każdy z tych kroków odpowiada cechom [Zawartości](Body/pl.md).
6.  Alternatywnie, dodaj obiekty pierwotne, takie jak **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Addytywny prostopadłościan](PartDesign_AdditiveBox/pl.md)** i **[<img src=images/PartDesign_SubtractiveCylinder.svg style="width:16px"> [Subtraktywny walec](PartDesign_SubtractiveCylinder/pl.md)**. Dowolna liczba kroków dodawania i odejmowania to funkcje, które są używane do utworzenia ostatecznej objętości.



## Uwagi

W ogólnym znaczeniu, \"Cecha\" może być dowolnym krokiem modelowania używanym do utworzenia ostatecznego [Kształtu](Shape/pl.md), za pomocą dowolnego narzędzia dowolnego [Środowiska pracy](Workbenches/pl.md).

-   Na przykład, w środowisku [Część](Part_Workbench/pl.md), z przepływem pracy [Konstrukcyjnej geometria bryły](Constructive_solid_geometry/pl.md), \"Cechą\" może być dowolna operacja logiczna, taka jak **[<img src=images/Part_Fuse.svg style="width:16px">. [Połączenie](Part_Fuse/pl.md)**, **[<img src=images/Part_Cut.svg style="width:16px"> [Wycięcie](Part_Cut/pl.md)**, lub **[<img src=images/Part_Common.svg style="width:16px"> [Część wspólna](Part_Common/pl.md)**.

W bardziej szczegółowym znaczeniu, \"Cecha\" jest krokiem modelowania używanym wewnątrz [Zawartości](PartDesign_Body/pl.md).

-   Na przykład **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [Addytywny walec](PartDesign_AdditiveCylinder/pl.md)**, **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [Uzupełnienie wyciągnięciem przez rofile](PartDesign_AdditiveLoft/pl.md)**, **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [Kieszeń](PartDesign_Pocket/pl.md)**, **[<img src=images/PartDesign_SubtractiveCone.svg style="width:16px">[Subtraktywny stożek](PartDesign_SubtractiveCone/pl.md)**, itp. wszystkie są \"Cechami\".


{{PartDesign Tools navi

}}  {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Feature/pl
