# Import OpenSCAD code/pl
{{TutorialInfo/pl
|Topic= Importowanie kodu OpenSCAD
|Level= Początkujący
|Time= 30 minut
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Wprowadzenie

OpenSCAD, podobnie jak FreeCAD, jest oprogramowaniem typu open source 3D CAD. Ale podczas gdy FreeCAD działa w oparciu o model graficzny, OpenSCAD wykorzystuje interfejs programowania do wykonywania operacji 3D. Środowisko pracy w OpenSCAD może być używane do importowania kodu obiektowego OpenSCAD oraz do wykonywania niektórych działań związanych z siatką modelu.

## Instalacja OpenSCAD 

-   Użytkownicy Linuksa mogą przeprowadzić instalację z repozytoriów odpowiednich dystrybucji, takich jak Debian, openSUSE, Mint, Unbuntu, itd. lub ze strony [domowej OpenSCAD](http://www.openscad.org/).
-   Użytkownicy komputerów Mac mogą pobrać binaria z [Strona główna OpenSCAD](http://www.openscad.org/).
-   Użytkownicy Windows mogą pobrać program ze strony [domowej OpenSCAD](http://www.openscad.org/). Ponieważ dla FreeCAD jest potrzebny tylko plik wykonywalny OpenSCAD, użytkownicy Windows, jeśli chcą mogą zainstalować wersję portable.

## Konfiguracja Środowiska pracy OpenSCAD we FreeCAD 

-   Otwórz aplikację FreeCAD.
-   Przełącz Środowisko pracy na [OpenSCAD](OpenSCAD_Workbench/pl.md).
-   Wybierz Edytuj → Preferencje → OpenSCAD z menu głównego.
    -   Pokaż FreeCAD program wykonywały OpenSCAD. *(sekcja: Ogólne ustawienia OpenSCAD)*
    -   wszystkie pozostałe wartości na stronie ustawień FreeCAD mogą być pozostawione bez zmian.

## Przykładowy model 

Tutaj użyjemy pliku example005.scad ze starych przykładów OpenSCAD, ale możesz użyć dowolnego pliku scad, który ci się podoba.

<img alt="" src=images/TutorialOpenSCAD_SampleFile.jpg  style="width:800px;">

## Importowanie modelu do FreeCAD 

-   We FreeCAD wybierz po prostu **Plik** → **Otwórz** i wybierz plik .scad, który chcesz zaimportować.
-   Nie jest ważne, które Środowisko pracy jest aktywne, same Środowisko pracy OpenSCAD jest potrzebne tylko gdy będziesz chciał użyć specjalne funkcje do modyfikacji twojego modelu.
-   FreeCAD zaimportuje plik OpenSCAD i zbuduje drzewo z operacjami podstawowymi i logicznymi.
-   Ćwiczenie dobiegło do końca.

<img alt="" src=images/TutorialOpenSCAD_ImportFile.jpg  style="width:800px;">

## Powiązane

-   [FreeCAD jak Importować, Eksportować](FreeCAD_Howto_Import_Export.md)
-   [Import i Eksport preferencji](Import_Export_Preferences/pl.md)

_

---
[documentation index](../README.md) > [OpenSCAD](Category_OpenSCAD.md) > [Import](Import_Workbench.md) > Import OpenSCAD code/pl
