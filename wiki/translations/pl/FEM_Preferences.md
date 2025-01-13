# FEM Preferences/pl
## Wprowadzenie

Ekran preferencji środowiska pracy <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [MES](FEM_Workbench/pl.md) znajduje się w [Edytorze ustawień](Preferences_Editor/pl.md). W menu wybierz **Edycja → Preferencje ...** a następnie **<img src="images/Workbench_FEM.svg" width=16px> MES**. Ta grupa jest dostępna tylko gdy środowisko pracy MES zostało wczytane w bieżącej sesji programu FreeCAD.

Dostępnych jest siedem stron: [Ogólne](#General/pl.md), [Gmsh](#Gmsh/pl.md), [CalculiX](#CalculiX/pl.md), [Elmer](#Elmer/pl.md), [Mystran](#Mystran/pl.md), [Z88](#Z88/pl.md) i [Netgen](#Netgen/pl.md). Wszystkie strony poza pierwszą dotyczą interakcji środowiska pracy MES z zewnętrznymi generatorami siatki i solverami.

Obecnie obsługiwane są następujące solvery zewnętrzne:

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [CalculiX](FEM_SolverCalculixCxxtools/pl.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/pl.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Mystran](FEM_SolverMystran/pl.md)
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Z88](FEM_SolverZ88/pl.md)



## Ogólne

<img alt="" src=images/Preferences_FEM_Page_General.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                                                                             | Opis                                                                                                                                                  |
+===================================================================================================+=======================================================================================================================================================+
|                                                                                    | Miejsce w systemie plików gdzie powinny być przechowywane pliki siatki i solvera.                                                                     |
| **Katalog roboczy**                                                                   |                                                                                                                                                       |
|                                                                                                |                                                                                                                                                       |
+++
|                                                                                    | Jeśli istnieje kilka siatek, zostaną one pogrupowane.                                                                                                 |
| **Utwórz grupy siatki dla kształtów referencyjnych analizy (wysoce eksperymentalne)** |                                                                                                                                                       |
|                                                                                                |                                                                                                                                                       |
+++
|                                                                                    | Istniejące obiekty [wyników](FEM_ResultShow/pl.md) zostaną zachowane, w przeciwnym razie zostaną nadpisane przez nowy przebieg solvera.       |
| **Zachowanie wyników przy ponownym uruchomieniu obliczeń**                            |                                                                                                                                                       |
|                                                                                                |                                                                                                                                                       |
+++
|                                                                                    | Jeżeli opcja jest zaznaczona, to okno dialogowe [Pokaż wyniki](FEM_ResultShow/pl.md) zostanie otwarte z ostatnio używanymi ustawieniami okna. |
| **Przywróć ustawienia okna dialogowego wyników**                                      |                                                                                                                                                       |
|                                                                                                |                                                                                                                                                       |
+++
|                                                                                    | Cechy analizy zostaną ukryte w widoku modelu, gdy otwarte zostanie okno dialogowe [Pokaż wyniki](FEM_ResultShow/pl.md).                       |
| **Ukryj cechy analizy przy otwartym oknie dialogowym wyników**                        |                                                                                                                                                       |
|                                                                                                |                                                                                                                                                       |
+++
|                                                                                    | Domyślne użyty solver podczas dodawania nowej [Analizy](FEM_Analysis/pl.md). ({{Version/pl|0.21}})                              |
| **Ustawienia domyślne solvera**                                                       |                                                                                                                                                       |
|                                                                                                |                                                                                                                                                       |
+++

## Gmsh

<img alt="" src=images/Preferences_FEM_Page_Gmsh.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

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
|                                        | Poziom szczegółowości logów: Ciche, Błędy, Ostrzeżenia, Bezpośrednie, Informacje, Status lub Debugowanie. {{Version/pl|1.1}}  |
| **Szczegółowość logów**                   |                                                                                                                                             |
|                                                    |                                                                                                                                             |
+++

## CalculiX

<img alt="" src=images/Preferences_FEM_Page_CalculiX.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                                       | Opis                                                                                                                                                                                                                              |
+=============================================================+===================================================================================================================================================================================================================================+
|                                              | Jeśli zaznaczone, FreeCAD będzie szukał pliku wykonywalnego solvera [CalculiX](FEM_SolverCalculixCxxtools/pl.md) w znanych (standardowych) lokalizacjach                                                                  |
| **Szukaj w znanych katalogach bin**             |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Ścieżka do pliku wykonywalnego solvera [CalculiX](FEM_SolverCalculixCxxtools/pl.md)                                                                                                                                       |
| **Ścieżka do pliku binarnego Calculix**         |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Jeśli zaznaczone, wbudowany edytor plików \*.inp z kolorowaniem składni będzie używany podczas edycji plików wejściowych solvera CalculiX.                                                                                        |
| **Użyj wewnętrznego edytora plików *.inp**      |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Ścieżka do zewnętrznego edytora plików \*.inp.                                                                                                                                                                                    |
| **Zewnętrzny edytor**                           |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Jeśli zaznaczone, zapisanych będzie kilka plików \*.inp a główny plik wejściowych będzie korzystał ze słów kluczowych \*INCLUDE jako odniesień do pozostałych plików. Jeśli odznaczone, zapisywany będzie jeden duży plik \*.inp. |
| **Podziel zapis pliku *.inp**                   |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Domyślny typ analizy: Statyczna, Częstotliwość, Termo mechanika, Sprawdź siatkę lub Wyboczenie.                                                                                                                                   |
| **Typ**                                         |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Liczba fizycznych rdzeni procesora do użycia do obliczeń równoległych.                                                                                                                                                            |
| **Liczba rdzeni CPU do użycia**                 |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Domyślny solver macierzowy: Domyślne, PaStiX, Pardiso, Solver Spooles, Solver iteracyjny typu scaling lub Solver iteracyjny Cholesky.                                                                                             |
| **Solver macierzy**                             |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Jeśli zaznaczone, domyślnie uwzględniania jest nieliniowość geometryczna.                                                                                                                                                         |
| **Geometria nieliniowa**                        |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Jeśli zaznaczone, używa niestandardowych ustawień solvera (niezalecane w większości przypadków).                                                                                                                                  |
| **Parametr kontroli przyrostów czasu**          |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Maksymalna liczba przyrostów w kroku analizy.                                                                                                                                                                                     |
| **Maksymalna liczba iteracji**                  |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Początkowy rozmiar przyrostu czasu (może być zmieniony przez solver jeśli używana jest automatyczna inkrementacja).                                                                                                               |
| **Początkowy krok czasu**                       |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Całkowity symulowany czas.                                                                                                                                                                                                        |
| **Koniec czasu**                                |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Minimalny dozwolony rozmiar przyrostu czasu.                                                                                                                                                                                      |
| **Minimalny krok czasu**                        |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Maksymalny dozwolony rozmiar przyrostu czasu.                                                                                                                                                                                     |
| **Maksymalny krok czasu**                       |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Jeśli zaznaczone, wyniki dla elementów 1D i 2D są domyślnie wyświetlane przy pomocy reprezentacji 3D.                                                                                                                             |
| **Format 3D wyników dla belek i powłok**        |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Jeśli zaznaczone, analizy termomechaniczne są domyślnie przeprowadzane dla stanu ustalonego.                                                                                                                                      |
| **Typ analizy (stan nieustalony lub ustalony)** |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Domyślna liczba żądanych postaci drgań własnych w analizach częstotliwościowych.                                                                                                                                                  |
| **Numer postaci własnej**                       |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Domyślna górna granica wyznaczanych częstotliwości drgań własnych w analizach częstotliwościowych.                                                                                                                                |
| **Górna granica częstotliwości**                |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++
|                                              | Domyślna dolna granica wyznaczanych częstotliwości drgań własnych w analizach częstotliwościowych.                                                                                                                                |
| **Dolna granica częstotliwości**                |                                                                                                                                                                                                                                   |
|                                                          |                                                                                                                                                                                                                                   |
+++

## Elmer

<img alt="" src=images/Preferences_FEM_Page_Elmer.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

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
|                                                     | Jeśli zaznaczone, używany jest binarny format wyników. W przeciwnym wypadku, używany jest format ASCII. Format binarny może powodować brak wyników przez występujący błąd. {{Version/pl|1.1}}                                                                                   |
| **Używaj formatu binarnego**                           |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++
|                                                     | Jeśli zaznaczone, identyfikatory obiektów geometrii są zapisywane w wynikach. {{Version/pl|1.1}}                                                                                                                                                                                |
| **Zapisuj identyfikatory geometrii**                   |                                                                                                                                                                                                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                               |
+++

## Mystran

<img alt="" src=images/Preferences_FEM_Page_Mystran.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                                  | Opis                                                                                                                                       |
+========================================================+============================================================================================================================================+
|                                         | Jeśli jest zaznaczone, FreeCAD będzie szukał pliku binarnego [Mystran](FEM_SolverMystran/pl.md) w znanych *(zwykłych)* katalogach. |
| **Szukaj w znanych katalogach binarnych**  |                                                                                                                                            |
|                                                     |                                                                                                                                            |
+++
|                                         | Ścieżka do pliku binarnego [Mystran](FEM_SolverMystran/pl.md).                                                                     |
| **Ścieżka do pliku binarnego Gmsh**        |                                                                                                                                            |
|                                                     |                                                                                                                                            |
+++
|                                         |                                                                                                                                            |
| **Zapisz komentarze do pliku wejściowego** |                                                                                                                                            |
|                                                     |                                                                                                                                            |
+++

## Z88

<img alt="" src=images/Preferences_FEM_Page_Z88.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

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

## Netgen

<img alt="" src=images/Preferences_FEM_Page_Netgen.png  style="width:350px;">

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                        | Opis                                                                                                                                                                                                                                                                                                                                            |
+==============================================+=================================================================================================================================================================================================================================================================================================================================================+
|                               | Jeśli zaznaczone, środowisko pracy MES używa starszej implementacji [Netgen](FEM_MeshNetgenFromShape/pl.md). To może być konieczne dla użytkowników (głównie ze starszymi komputerami i systemem Windows), którzy nie mogą zainstalować bibliotek Pythona potrzebnych do nowej implementacji Netgen. ({{Version/pl|1.0}}) |
| **Starsza implementacja Netgen** |                                                                                                                                                                                                                                                                                                                                                 |
|                                           |                                                                                                                                                                                                                                                                                                                                                 |
+++





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/pl
