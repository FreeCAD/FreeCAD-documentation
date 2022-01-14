# PCB Workbench/pl
## Wprowadzenie


{{TOCright}}

[Obwody drukowane](https://en.wikipedia.org/wiki/Printed_circuit_board) środowisko pracy dla FreeCAD *(PCB)*

Środowisko pracy dla elastycznych obwodów drukowanych dla FreeCAD *(FPCB)*

Moduł pozwala na importowanie/tworzenie płytek PCB w programie FreeCAD. Zakres modułu:

-   wsparcie dla wielu różnych warstw,
-   możliwość wyboru kolorów, przezroczystości i nazw dla każdej warstwy,
-   moduł pozwala na import modeli IGES/STP z kolorami,
-   możliwość niezależnego pokazywania otworów/szczelin.

## Bibliografia

-   Autor: marmni
-   Strona domowa projektu: <https://sourceforge.net/projects/eaglepcb2freecad/>
-   Źródła kodu na Github: <https://github.com/marmni/FreeCAD-PCB>

## Przybory

Szczegółowy opis pracy w środowisku roboczym znajduje się w pliku **index.pdf** w kodzie źródłowym lub [podręczniku](https://raw.githubusercontent.com/marmni/FreeCAD-PCB/master/index.pdf).

Pasek narzędzi

![](images/PCB-menu-orizz.png )

Menu rozwijane

![](images/PCB-export-BOM.png ) ![](images/PCB-export-hole.png ) ![](images/PCB-create-new.png ) ![](images/PCB-explode.png ) ![](images/PCB-bounding-box.png )

## Instalacja

### Instalacja automatyczna 

Można je zainstalować z [Menadżera dodatków](Std_AddonMgr/pl.md).

### Z GitHub\'a 

**Wymagania wstępne**

FreeCAD-PCB wymaga programu FreeCAD w wersji 0.18 lub wyższej oraz środowiska Python w wersji 2.7 lub wyższej.

**Instrukcja instalacji systemu Linux** *(z GitHub)*

Rozpakuj pobrany plik zip i skopiuj wypakowany folder do katalogu, w którym zainstalowany jest FreeCAD *(folder podrzędny Mod)*.

Przykład:

-   ścieżka do FreeCAD:

~/Programs/FreeCAD

-   Więc skopiuj mod do folderu

~/Programs/FreeCAD/Mod

-   Możesz również skopiować pliki do folderu

~/.FreeCAD/Mod .

-   Następnie zmień uprawnienia do odczytu/zapisu na 777. Proszę nie zapomnieć o parametrze -R!

Przykład:

chmod 777 -R PCB

**Instrukcja instalacji systemu Windows** *(z GitHub)*

Rozpakuj pobrany plik zip i skopiuj wypakowany folder do katalogu, w którym zainstalowany jest FreeCAD *(folder podrzędny Mod)*.

Przykład:

-   ścieżka do FreeCAD:

C:/Program Files/FreeCAD-0.18

-   Więc skopiuj mod do folderu

C:/Program Files/FreeCAD-0.18/Mod

-   Następnie zmień uprawnienia do odczytu/zapisu dla wszystkich użytkowników. Kliknij prawym przyciskiem myszy na folderze PCB i wybierz Właściwości → Bezpieczeństwo → Edycja → Użytkownicy i zaznacz wszystkie pola wyboru w opcji \'Zezwalaj\'.

Zabezpieczenia → Edytuj → Użytkownicy i zaznacz wszystkie pola wyboru w opcji \'Zezwalaj\'.

**Instrukcja instalacji systemu MacOS** *(z GitHub)*

## Odnośniki do środowiska pracy FreeCAD-PCB 

-   Wiki środowiska: [Zewnętrzne środowiska pracy](https://wiki.freecadweb.org/External_workbenches)
-   Wiki FreeCAD: [strona główna Wiki](https://wiki.freecadweb.org/Main_Page)
-   Forum FreeCAD: [Importer EaglePCB dla FreeCAD](http://forum.freecadweb.org/viewtopic.php?f=9&t=5107)
-   Poradniki:
-   Wideo: [EaglePCB\_2\_FreeCAD - FreeCAD odczyt plików brd z programu Eagle](https://www.youtube.com/watch?v=81NsljRJx8c&feature=youtu.be)
-   Files: [PCB library](https://github.com/marmni/FreeCAD-PCB-library)
-   Zgłaszanie błędów: Proszę zgłaszać błędy na stronie <https://github.com/marmni/FreeCAD-PCB/issues>

## Inne użyteczne odnośniki 

-   [EaglePCB na sourceforge](https://sourceforge.net/projects/eaglepcb2freecad/)
-   [Przepisy na makropolecenia](Macros_recipes/pl.md)
-   [Pobieranie programu FreeCAD](Download/pl.md)
-   [Portal społeczności FreeCADl](FreeCAD_Community_Portal.md)



[<img src="images/Property.png" style="width:16px"> Sandbox](Category_Sandbox.md) [<img src="images/Property.png" style="width:16px"> User Documentation](Category_User_Documentation.md) [<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md)

---
[documentation index](../README.md) > [Sandbox](Category_Sandbox.md) > PCB Workbench/pl
