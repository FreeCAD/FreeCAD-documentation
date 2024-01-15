# Onboarding FEM Devs/pl
## Opis

Na tej stronie nowi programiści dowiedzą się, jak skonfigurować swoje środowiska programistyczne, aby kodować w środowisku pracy MES.



## Konfiguracja środowiska deweloperskiego 

Do opracowania.



### Wymagania wstępne 

-   Netgen



### Zalecane

-   Paraview



### Kompilacja ze źródła 

Do opracowania.



### Kompilacja przez Docker 

Do opracowania.



## Zarządzanie kodem źródłowym 

Utrzymanie aktualności FreeCAD jest udokumentowane na stronie [Zarządzanie kodem źródłowym](Source_code_management/pl.md). Wraz z przydatnymi wskazówkami `git`.



## Infrastruktura kodu MES 

Kod MES znajduje się w `src/Mod/Fem`.

-    `App/`aplikacja w trybie konsoli, definiuje podstawowe struktury i klasy bazowe dla obiektów dokumentów, które są używane przez moduły do tworzenia własnych.

-    `Gui/`Aplikacja w trybie GUI, definiuje [widok 3D](3D_view/pl.md), narzędzia/funkcje używane przez środowisko pracy do interakcji z interfejsem użytkownika i widokiem 3D, definiuje klasy bazowe dla [dostawcy widoków](Viewprovider/pl.md).

-    `femcommands/`
    

-    `fem.dox`
    

-    `femexamples/`
    

-    `femguiobjects/`
    

-    `femguiutils/`
    

-    `feminout/`
    

-    `femmesh/`
    

-    `femobjects/`
    

-    `femresult/`
    

-    `femsolver/`
    

-    `femtaskpanels/`
    

-    `femtest/`
    

-    `femtools/`
    

-    `femviewprovider/`
    

-    `InitGui.py`
    

-    `Init.py`
    

-    `ObjectsFem.py`
    

-    `TestFemApp.py`
    

-    `TestFemGui.py`
    



### Konwencja kodowania 

Zobacz plik [coding_conventions.md](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Fem/coding_conventions.md) w repozytorium FreeCAD.



## Dodawanie nowych solwerów MES 

Nowy solver MES wymaga następujących elementów:

-   Eksporter siatki,
-   Importer wyników,
-   Obiekt Solver *(wymaga zmian w ustawieniach solvera, testach jednostkowych, modułach ObjectsFem)*,
-   Moduł zadań i zapisu *(tutaj odbywa się główny zapis danych wejściowych solvera)*,
-   Narzędzie GUI do tworzenia solvera,
-   Zakładka preferencji GUI do ustawiania ścieżki binarnej solvera,
-   Test jednostkowy zapisu danych wejściowych solvera. Najlepiej skorzystać ze wspornika ccx. Jest on dostępny dla wszystkich typów elementów siatki,
-   Jedno lub dwa piwa \...

Zobacz także:

-   [Rozszerzenie modułu FEM](Extend_FEM_Module/pl.md)
-   Wysiłki związane z implementacją solvera [oofem](https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem).
-   Wysiłki związane z implementacją solvera \[<https://github.com/FreeCAD/FreeCAD/compare/a03eb6b9625ba>\...dfc01ec949525 myStran\].



## Pisanie testów jednostkowych 

Do opracowania.



## Informacje dodatkowe 

-   [Zawijanie klasy C++ w środowisku Python](Wrapping_a_Cplusplus_class_in_Python/pl.md)
-   [Dodawanie równań w środowisku MES](Add_FEM_Equation_Tutorial/pl.md)
-   [Dodaj przycisk do paska narzędzi MES](Add_Button_to_FEM_Toolbar_Tutorial/pl.md)



## Powiązane

-   Błędy MES w [FreeCAD bugtracker](https://github.com/FreeCAD/FreeCAD/issues)
-   Otwarte komentarze do MES [FIXME](https://github.com/FreeCAD/FreeCAD/search?q=FIXME+AND+fem) w kodzie źródłowym FreeCAD
-   Otwarte komentarze do MES [TODO](https://github.com/FreeCAD/FreeCAD/search?q=TODO+AND+fem) w kodzie źródłowym FreeCAD
-   [Oryginalna dyskusja w wątku](https://forum.freecadweb.org/viewtopic.php?f=18&t=60574) dla tej strony wiki
-   [środowisko pracy MES](FEM_Workbench/pl.md)



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Onboarding FEM Devs/pl
