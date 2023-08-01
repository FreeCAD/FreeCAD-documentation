# FEM Preferences/pl
{{TOCright}} Ekran preferencji środowiska pracy [MES](EM_Workbench/pl.md) znajduje się w [Edytorze ustawień](Preferences_Editor/pl.md), **Edycja → Preferencje ... → MES**.

W preferencjach środowiska pracy MES znajduje się kilka zakładek, poczynając od **Ogólnej** konfiguracji środowiska. Pozostałe zakładki określają sposób współpracy MES z obsługiwanymi zewnętrznymi solverami.

Obecnie obsługiwane są następujące solvery zewnętrzne:

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [CalculiX](FEM_SolverCalculixCxxtools/pl.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/pl.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Mystran](FEM_SolverMystran/pl.md) 
*({{Version/pl|0.20}})*
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Z88](FEM_SolverZ88/pl.md)



## Ogólne

W zakładce *Ogólne* można wybrać następujące opcje:

+++
| Nazwa                                                                  | Opis                                                                                                                                                  |
+========================================================================+=======================================================================================================================================================+
|                                                         | Miejsce w systemie plików gdzie powinny być przechowywane pliki siatki i solvera.                                                                     |
| **Katalog roboczy**                                        |                                                                                                                                                       |
|                                                                     |                                                                                                                                                       |
+++
|                                                         | Jeśli istnieje kilka siatek, zostaną one pogrupowane.                                                                                                 |
| **Utwórz grupy siatek**                                    |                                                                                                                                                       |
|                                                                     |                                                                                                                                                       |
+++
|                                                         | Istniejące obiekty [wyników](FEM_ResultShow/pl.md) zostaną zachowane, w przeciwnym razie zostaną nadpisane przez nowy przebieg solvera.       |
| **Zachowanie wyników przy ponownym uruchomieniu obliczeń** |                                                                                                                                                       |
|                                                                     |                                                                                                                                                       |
+++
|                                                         | Jeżeli opcja jest zaznaczona, to okno dialogowe [Pokaż wyniki](FEM_ResultShow/pl.md) zostanie otwarte z ostatnio używanymi ustawieniami okna. |
| **Przywróć ustawienia okna dialogowego wyników**           |                                                                                                                                                       |
|                                                                     |                                                                                                                                                       |
+++
|                                                         | Wiązania zostaną ukryte w widoku modelu, gdy otwarte zostanie okno dialogowe [Pokaż wyniki](FEM_ResultShow/pl.md).                            |
| **Ukryj wiązania przy otwartym oknie dialogowym wyników**  |                                                                                                                                                       |
|                                                                     |                                                                                                                                                       |
+++
|                                                         | Domyślne użyty solver podczas dodawania nowej [Analizy](FEM_Analysis/pl.md). ({{Version/pl|0.21}})                              |
| **Ustawienia domyślne solvera**                            |                                                                                                                                                       |
|                                                                     |                                                                                                                                                       |
+++

![](images/Preference_Fem_Tab_01.png )

## Gmsh

W zakładce *Gmsh* można wybrać następujące opcje:

+++
| Nazwa                                                 | Opis                                                                                                                                        |
+=======================================================+=============================================================================================================================================+
|                                        | Jeśli jest zaznaczone, FreeCAD będzie szukał pliku binarnego [Gmsh](FEM_MeshGmshFromShape/pl.md) w znanych *(zwykłych)* katalogach. |
| **Szukaj w znanych katalogach binarnych** |                                                                                                                                             |
|                                                    |                                                                                                                                             |
+++
|                                        | Ścieżka do pliku binarnego [Gmsh](FEM_MeshGmshFromShape/pl.md).                                                                     |
| **Ścieżka do pliku binarnego Gmsh**       |                                                                                                                                             |
|                                                    |                                                                                                                                             |
+++

![](images/Preference_Fem_Tab_03.png )

## CalculiX

W zakładce *CalculiX* można wybrać następujące opcje:

![](images/Preference_Fem_Tab_02.png )

## Elmer

W zakładce *Elmer* można wybrać następujące opcje:

+++
| Nazwa                                                              | Opis                                                                                                                                                                                                                                                                                          |
+====================================================================+===============================================================================================================================================================================================================================================================================================+
|                                                     | Jeśli opcja ta jest zaznaczona, FreeCAD będzie szukał plików binarnych narzędzia do zapisu siatki [Elmer](FEM_SolverElmer/pl.md) w znanych *(zwykłych)* katalogach.                                                                                                                   |
| **ElmerGrid: Szukaj w znanych katalogach binarnych**   |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++
|                                                     | Ścieżka do pliku binarnego narzędzia do tworzenia siatki [Elmer](FEM_SolverElmer/pl.md).                                                                                                                                                                                              |
| **Ścieżka pliku binarnego ElmerGrid**                  |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++
|                                                     | Jeśli opcja ta jest zaznaczona, FreeCAD będzie szukał plików binarnych solvera [Elmer](FEM_SolverElmer/pl.md) w znanych *(zwykłych)* katalogach.                                                                                                                                      |
| **ElmerSolver: Szukaj w znanych katalogach binarnych** |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++
|                                                     | Ścieżka do binarnego solvera [Elmer](FEM_SolverElmer/pl.md).                                                                                                                                                                                                                          |
| **Ścieżka pliku binarnego ElmerSolver**                |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++
|                                                     | Liczba rdzeni CPU, które zostaną użyte do wykonania rozwiązania. *\'Ważne:* Elmer dzieli siatkę na porcje. Liczba porcji jest równa liczbie używanych rdzeni procesora. Może to skutkować efektami ubocznymi:                                                                                 |
| **Liczba rdzeni procesora, do użycia**                 |                                                                                                                                                                                                                                                                                               |
|                                                                 | -   W zależności od złożoności Twojej siatki mniejsza liczba rdzeni procesora może działać szybciej niż użycie większej liczby rdzeni.                                                                                                                                                        |
|                                                                    | -   W niektórych przypadkach użycie np. 12 rdzeni nie zapewnia zbieżności, podczas gdy 8 rdzeni będzie działać dobrze. Powodem jest to, że w pewnym momencie części siatki stają się zbyt małe.                                                                                               |
|                                                                    |                                                                                                                                                                                                                                                                                               |
|                                                                    | Tak więc często konieczne jest dostosowanie liczby rdzeni, w zależności od siatki.                                                                                                                                                                                                            |
|                                                                    |                                                                                                                                                                                                                                                                                               |
|                                                                    | **Znane ograniczenia:** Dla niektórych typów symulacji trzeba najpierw zainstalować moduły Elmera, aby umożliwić wielowątkowość. Sprawdź raport Elmera, aby uzyskać informacje na ten temat. Typowym przypadkiem jest to, że do rozwiązywania bezpośredniego trzeba zainstalować moduł MUMPS. |
+++
|                                                     | Regiony objętości siatki przetwarzane przez każdy rdzeń procesora zostaną połączone, aby uczynić granice objętości niewidocznymi.                                                                                                                                                             |
| **Wyniki filtrowania**                                 |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++

![](images/Preference_Fem_Tab_05.png )

## Mystran

W zakładce *Mystran* można wybrać następujące opcje:

+++
| Nazwa                                                 | Opis                                                                                                                                       |
+=======================================================+============================================================================================================================================+
|                                        | Jeśli jest zaznaczone, FreeCAD będzie szukał pliku binarnego [Mystran](FEM_SolverMystran/pl.md) w znanych *(zwykłych)* katalogach. |
| **Szukaj w znanych katalogach binarnych** |                                                                                                                                            |
|                                                    |                                                                                                                                            |
+++
|                                        | Ścieżka do pliku binarnego [Mystran](FEM_SolverMystran/pl.md).                                                                     |
| **Ścieżka do pliku binarnego Gmsh**       |                                                                                                                                            |
|                                                    |                                                                                                                                            |
+++

![](images/Preference_Fem_Tab_Mystran.png )

## Z88

W zakładce *Z88* można wybrać następujące opcje:

+++
| Nazwa                                                         | Opis                                                                                                                                                                                                                                                                 |
+===============================================================+======================================================================================================================================================================================================================================================================+
|                                                | Jeśli jest zaznaczone, FreeCAD będzie szukał pliku binarnego [solvera Z88](FEM_SolverZ88/pl.md) w znanych *(zwykłych)* katalogach.                                                                                                                           |
| **Szukaj w znanych katalogach binarnych**         |                                                                                                                                                                                                                                                                      |
|                                                            |                                                                                                                                                                                                                                                                      |
+++
|                                                | Ścieżka do pliku binarnego [solvera Z88](FEM_SolverZ88/pl.md).                                                                                                                                                                                               |
| **Ścieżka do pliku binarnego Gmsh**               |                                                                                                                                                                                                                                                                      |
|                                                            |                                                                                                                                                                                                                                                                      |
+++
|                                                | Metoda solvera używana przez [solver Z88](FEM_SolverZ88/pl.md) dla nowych symulacji.                                                                                                                                                                         |
| **Metoda Solvera**                                |                                                                                                                                                                                                                                                                      |
|                                                            |                                                                                                                                                                                                                                                                      |
+++
|                                                | Jest to istotne, gdy używana jest metoda solvera **Simple Cholesky**. Po uruchomieniu solvera może pojawić się informacja, że należy zwiększyć wartość parametru **MAXGS**. W takim przypadku należy zwiększyć maksymalną liczbę miejsc i ponownie uruchomić solver. |
| **Maksymalna ilość miejsc w macierzy sztywności** |                                                                                                                                                                                                                                                                      |
|                                                            |                                                                                                                                                                                                                                                                      |
+++
|                                                | Jest to istotne, gdy używana jest jedna z metod iteracyjnych solvera. Po uruchomieniu solvera może pojawić się informacja o konieczności zwiększenia wartości **MAXKOI**. W takim przypadku należy zwiększyć maksymalną liczbę miejsc i ponownie uruchomić solver.   |
| **Maksymalna ilość miejsc w wektorze zbieżności** |                                                                                                                                                                                                                                                                      |
|                                                            |                                                                                                                                                                                                                                                                      |
+++

![](images/Preference_Fem_Tab_04.png )



## Materiał

W zakładce *Materiał* można wybrać następujące opcje:

+++
| Nazwa                                                                                                            | Opis                                                                                                                                                                                                                    |
+==================================================================================================================+=========================================================================================================================================================================================================================+
|                                                                                                   | Karty wbudowane w program FreeCAD zostaną wyświetlone jako dostępne.                                                                                                                                                    |
| **Użyj materiałów dołączonych**                                                                      |                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                         |
+++
| \\AppData\\Roaming\\FreeCAD\\Material* |
| **Użyj materiałów z katalogu programu FreeCAD - "Materials" w preferowanej lokalizacji użytkownika** |                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                         |
+++
|                                                                                                   | Karty materiałowe z określonego katalogu również będą wyświetlane jako dostępne.                                                                                                                                        |
| **Użyj materiałów z katalogu zdefiniowanego przez użytkownika**                                      |                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                         |
+++
|                                                                                                   | Duplikaty kart zostaną usunięte z wyświetlanej listy kart materiałowych.                                                                                                                                                |
| **Usuń duplikaty kart**                                                                              |                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                         |
+++
|                                                                                                   | Karty materiałów będą wyświetlane posortowane według ich źródeł *(lokalizacji)*. Jeśli opcja ta nie zostanie zaznaczona, będą one sortowane według nazwy.                                                               |
| **Sortuj według katalogów**                                                                          |                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                         |
+++

![](images/Preference_Fem_Tab_Material.png )


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/pl
