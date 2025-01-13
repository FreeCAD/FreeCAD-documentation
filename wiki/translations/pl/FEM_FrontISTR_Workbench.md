# <img alt="Ikona środowiska pracy MES FrontISTR" src=images/FrontISTR.svg  style="width:64px;"> FEM FrontISTR Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/FrontISTR.svg  style="width:24px;"> MES FrontISTR to dodatek do programu FreeCAD, który umożliwia korzystanie z FrontISTR, otwartego solvera MES do wielkoskalowych obliczeń równoległych nieliniowych zagadnień mechanicznych.

<img alt="" src=images/FEM_FrontISTR_bikeframe_screenshot.png  style="width:512px;">



### Zamierzony przepływ pracy 

1.  Ustaw analizę w środowisku pracy MES *(tak samo jak dla CalculiX)*.
2.  Przejdź do środowiska pracy **FrontISTR** i utwórz obiekt solvera FrontISTR klikając ikonę <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> na pasku narzędzi.
3.  Dwukrotnie kliknij na obiekcie solvera w drzewie dokumentu i ustaw katalog roboczy.
4.  Wciśnij przycisk **Write input file**
5.  Wciśnij przycisk **Run FrontISTR**
6.  Sprawdź FISTR_Results do postprocessingu.



### Cechy

-   analiza statyczna, sprawdzenie elementów,
-   analiza geometrycznie liniowa/nieliniowa,
-   elementy: czworościany pierwszego/drugiego rzędu,
-   obciążenia: obciążenia mechaniczne skupione i rozłożone, grawitacja,
-   warunki brzegowe: utwierdzenie punktów lub zadane przemieszczenie,
-   kontrola kroku: automatyczna inkrementacja,
-   solver równań liniowych,
    -   iteracyjny,
        -   prekondycjoner: AMG, SSOR, Diagonal, ILU(k)(k=0,1,2),
        -   metoda: CG, BiCGSTAB, GMRES, GPBiCG,
    -   bezpośredni: MUMPS,
-   format plików wyjściowych: AVS, VTK *(wymagane ParaView)*.



### Funkcje planowane do obsługi w przyszłości 

-   analizy: przepływu ciepła, dynamiczne, drgań własnych,
-   materiały *(mechaniczne)*: sprężysto-plastyczne, hipersprężyste, pełzanie, lepkosprężyste,
-   kontakt,
-   MPC(TIE),
-   elementy: pięciościenne, sześciościenne, belkowe, powłokowe, kratownicowe itd.



### Ograniczenia

-   Obiekt FISTR_Results zawiera wyniki tylko dla powierzchni. Jeśli potrzebne Ci są wyniki z wewnątrz modelu, zmień Output File Format na VTK i skorzystaj z ParaView do wizualizacji wyników.
-   Środowisko pracy MES FrontISTR nie wspiera jeszcze analiz termicznych. Sam FISTR może je jednak przeprowadzać i wsparcie dla nich jest planowane w najbliższej przyszłości.
-   Analizy mechaniczne dla różnych materiałów w modelu nie są obecnie wspierane.



### Wyniki testów 

Zobacz <https://github.com/FrontISTR/FEM_FrontISTR/tree/master/sample/benchmarks>.



## Instalacja



## Menadżer dodatków 

FEM_FrontISTR można łatwo zainstalować poprzez <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menedżer dodatków](Std_AddonMgr/pl.md) z menu **Narzędzia → Menedżer dodatków**. FEM_FrontISTR jest aktywnie rozwijany i będzie często zyskiwał nowe funkcje. Zatem powinieneś go regularnie aktualizować w ten sam sposób: **Narzędzia → Menedżer dodatków**. Kod FEM_FrontISTR jest przechowywany i rozwijany [na platformie GitHub](https://github.com/FrontISTR/FEM_FrontISTR).



### Podręcznik

Zobacz [Jak zainstalować dodatkowe środowiska pracy](How_to_install_additional_workbenches/pl.md).



### Wymagania wstępne 

-   FreeCAD 0.19 lub nowszy.
-   [ParaView](https://www.paraview.org/) *(opcjonalne)*.



### Instalacja solvera FrontISTR 

Pliki wykonywalne FrontISTR będą automatycznie pobrane i zainstalowane przy pierwszym uruchomieniu. Jeśli pobieranie się nie powiedzie, wykonaj poniższe kroki aby zainstalować solver.

#### Windows

1.  Pobierz [FrontISTR-latest.zip](https://www.frontistr.com/download/link.php?https://frontistr-commons.gitlab.io/FrontISTR/release/x86_64-w64-mingw32-msmpi/FrontISTR-latest.zip)
2.  Utwórz ścieżkę FEM_FrontISTR/bin
3.  Wypakuj FrontISTR-latest.zip i umieść wszystkie pliki w katalogu FEM_FrontISTR/bin.

#### Linux

W przygotowaniu.

#### Mac

W przygotowaniu.



## Narzędzia

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> **Solver FrontISTR Standard**: Tworzy nowy obiekt solvera FrontISTR dla tej analizy.



## Źródła

-   Autor: kinagaki rigarashi
-   Kod źródłowy: [Github.com](https://github.com/FrontISTR/FEM_FrontISTR)
-   Forum FreeCAD: [58019](https://forum.freecadweb.org/viewtopic.php?t=58019)
-   Poradniki: <https://frontistr-commons.gitlab.io/FEM_FrontISTR/en/>
-   Dokumentacja solvera FrontISTR: <https://manual.frontistr.com/en/>
-   Zgłaszanie błędów: Prosimy o zgłaszanie błędów na stronie [Github.com](https://github.com/FrontISTR/FEM_FrontISTR)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > FEM FrontISTR Workbench/pl
