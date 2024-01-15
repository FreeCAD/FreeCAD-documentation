# Datum/pl
## Wprowadzenie

W FreeCAD słowo \"[Odniesienie położenia](Datum/pl.md)\" jest zwykle używane w odniesieniu do geometrii pomocniczej w środowisku pracy [Projekt Części](PartDesign_Workbench/pl.md). Te elementy geometryczne nie będą stanowić części ostatecznego [Kształtu](Shape/pl.md) [Zawartości](Body/pl.md), ale mogą być używane jako odniesienia i podpory dla [Szkiców](Sketch/pl.md) i innych typów [Cech](Feature/pl.md).

Następujące elementy odpowiadają elementom wywodzącym się z klasy `Part::Datum`, która sama wywodzi się z [Część: Cecha](Part_Feature/pl.md):

-   [Projekt Części: Punkt odniesienia](PartDesign_Point/pl.md)
-   [Projekt Części: Linia odniesienia](PartDesign_Line/pl.md)
-   [Projekt Części: Płaszczyzna odniesienia](PartDesign_Plane/pl.md)
-   [Projekt Części: Lokalny układ współrzędnych](PartDesign_CoordinateSystem/pl.md)

Następujące elementy pochodzą bezpośrednio z obiektu [Część: Cecha](Part_Feature/pl.md):

-   [Projekt Części: Łącznik kształtu](PartDesign_ShapeBinder/pl.md)
-   [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md)



## Użycie

1.  Przełącz się do środowiska pracy [Projekt części](PartDesign_Workbench/pl.md).
2.  Naciśnij przycisk **[<img src=images/PartDesign_Body.svg style="width:16px"> [Utwórz zawartość](PartDesign_Body/pl.md)**.
3.  Wybierz odniesienie położenia bryły i ustaw ją jako widoczną, naciskając klawisz **Spacja** na klawiaturze.
4.  Naciśnij **[<img src=images/PartDesign_Plane.svg style="width:16px"> [Utwórz płaszczyznę odniesienia](PartDesign_Plane/pl.md)**, aby otworzyć [panel zadań](Task_panel/pl.md) płaszczyzny.
5.  W oknie [widoku 3D](3D_view/pl.md) kliknij jedną ze standardowych płaszczyzn, na przykład płaszczyznę XY. Następnie naciśnij **OK**, aby zamknąć panel zadań.
6.  Teraz w [widoku drzewa](Tree_view/pl.md) wybierz nowo utworzoną Płszczyznę odniesienia, a następnie naciśnij przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Utwórz szkic](PartDesign_NewSketch/pl.md)**.
7.  Utwórz zamkniętą polilinię, a następnie użyj **[<img src=images/PartDesign_Pad.svg style="width:16px"> [wyciągnięcia](PartDesign_Pad/pl.md)** do wyciągnięcia szkicu i utworzenia początkowej bryły.

Teraz możesz dowolnie przesuwać i obracać Płaszczyzne odniesienia, zmieniając jej właściwości w [edytorze właściwości](Property_editor/pl.md), a Szkic i Wyciągnięcie będą podążać za jej nowym [umiejscowieniem](Placement/pl.md).

Można dodać inne typy układów odniesienia, które będą używane z innymi szkicami i funkcjami.



## Uwagi

Odkąd pojawiły się w wersji 0.17, obiekty odniesienia miały być używane wewnątrz [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części. Ponieważ jednak są one użytecznymi obiektami \"referencyjnymi\" z różnymi metodami [dołączenia](Part_EditAttachment/pl.md), zaproponowano, aby były one dostępne poza środowiskiem pracy [Projekt Części](PartDesign_Workbench/pl.md). W ten sposób będą one użyteczne we wszystkich środowiskach roboczych jako geometria pomocnicza, szczególnie w kontekście tworzenia [złożeń](Assembly/pl.md).

-   [Tworzenie i wyświetlanie lokalnego układu współrzędnych](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Obiekty układu odniesienia w App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Pasek narzędzi struktury i układy odniesienia](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Lokalny układ współrzędnych nie może być użyty w środowisku pracy Projekt Części](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Datum/pl
