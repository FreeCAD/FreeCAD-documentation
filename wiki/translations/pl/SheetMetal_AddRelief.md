---
 GuiCommand:
   Name: SheetMetal AddRelief
   Name/pl: Arkusz Blachy: Wykonaj podcięcie
   MenuLocation: SheetMetal , Wykonaj podcięcie
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **S** **R**
   SeeAlso: SheetMetal_AddJunction/pl, SheetMetal_AddBend/pl
---

# SheetMetal AddRelief/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **Wykonaj podcięcie** tworzy narożne odciążenia, wycięcia, w punktach, w których spotykają się trzy sekcje *(płyta podstawowa / ściany / kołnierze)* obiektu wykonanego z blachy. Bez tych wycięć obiekt nie będzie mógł zostać rozłożony.

To polecenie jest pierwszym z trzech kroków konwersji obiektu powłoki wykonanego za pomocą środowiska pracy [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) na rozkładany obiekt z blachy:

1.  [Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)
2.  [Wykonaj połączenie](SheetMetal_AddJunction/pl.md)
3.  [Wykonaj zagięcie](SheetMetal_AddBend/pl.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Wykonaj podcięcie - odcięte rogi.*



## Użycie

1.  Wybierz jedną lub więcej krawędzi.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/SheetMetal_AddRelief.svg" width=16px> Wykonaj podcięcie**.
    -   Wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Wykonaj podcięcie** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **Sheet Metal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Wykonaj podcięcie** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **S** + **R**.
3.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Add Corner Relief on Solid** (wprowadzony w wersji 0.5.00).
4.  Opcjonalnie wciśnij przycisk **Wybierz** aby dodać więcej wierzchołków.
    -   Wciśnij przycisk **Podgląd** aby zakończyć wybór i wyświetlić zmiany.
5.  Opcjonalnie dostosuj parametry w panelu zadań.
6.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
7.  Utworzony zostanie obiekt **CornerRelief** składający się z jednego nowego podcięcia dla każdego wskazanego wierzhołka.
8.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;">



## Uwagi

Polecenia <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Wykonaj połączenie](SheetMetal_AddJunction/pl.md)** i <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Wykonaj zagięcie](SheetMetal_AddBend/pl.md)** działają najlepiej z obiektami typu \"wydrążony\" prostopadłościan o stałej grubości i kątach 90° między ścianami.

Obiekty powłoki mogą być tworzone za pomocą poleceń środowisk pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md) lub <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Aby utworzyć półfabrykat za pomocą środowiska pracy [Część](Part_Workbench/pl.md):

1.  Utwórz bryłę za pomocą poleceń:
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Sześcian](Part_Box/pl.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Wyciągnięcie \...](Part_Extrude/pl.md) z:
        -   <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Prostokąt](Draft_Rectangle/pl.md) środowiska Rysunek Roboczy.
        -   <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polilinia](Draft_Wire/pl.md) środowiska Rysunek Roboczy.
        -   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Utwórz szkic](Sketcher_NewSketch/pl.md) środowiska Szkicownik.
2.  Użyj narzędzia <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Grubość](Part_Thickness/pl.md) środowiska Część, aby utworzyć obiekt powłoki z bryły *(zazwyczaj używając wartości grubości blachy)*.

Aby utworzyć półfabrykat za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md):

1.  Utwórz bryłę używając poleceń:
    -   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Addytywny prostopadłościan](PartDesign_AdditiveBox/pl.md).
    -   <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Wyciągnij](PartDesign_Pad/pl.md) ze <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [szkicu](Sketcher_NewSketch/pl.md).
2.  Użyj narzędzia <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [Grubość](PartDesign_Thickness/pl.md), aby utworzyć obiekt powłoki z bryły *(zazwyczaj używając wartości grubości blachy)*.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Podcięcie środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Parametry}}

-    **Obiekt bazowy|LinkSub**: *Obiekt bazowy*. Łącza do narożnych wierzchołków definiujących pozycje podcięcia.

-    **Podcięcie|Length**: *Rozmiar podcięcia*. Wartość domyślna: {{value|2,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddRelief/pl
