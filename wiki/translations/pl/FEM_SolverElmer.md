---
 GuiCommand:
   Name: FEM SolverElmer
   Name/pl: Solver Elmer
   MenuLocation: Solver , Solver Elmer
   Workbenches: FEM_Workbench/pl
   Shortcut: **S** **E**
   SeeAlso: FEM_SolverElmer_SolverSettings/pl, FEM_SolverCalculixCxxtools/pl, FEM_SolverZ88/pl, FEM_tutorial/pl
---

# FEM SolverElmer/pl



## Opis

[Elmer](https://www.elmerfem.org) to otwarto źródłowy solver do symulacji z różnych dziedzin fizyki, opracowywany głównie przez IT Center for Science *(CSC)*. Rozwój Elmera rozpoczął się w 1995 r. we współpracy z fińskimi uniwersytetami, instytutami badawczymi i przemysłem. Po publikacji kodu źródłowego w 2005 r., Elmera zaczęto używać i rozwijać globalnie.

Elmer posiada modele fizyczne m.in. mechaniki płynów, mechaniki ciał stałych, elektromagnetyzmu, przepływu ciepła i akustyki. Są one opisane równaniami różniczkowymi cząstkowymi, które [Elmer](https://www.csc.fi/web/elmer) rozwiązuje przy pomocy metody elementów skończonych *(MES)*.

Utworzenie obiektu SolverElmer w kontenerze analizy we FreeCAD daje dostęp do równań Elmera dla analiz pojedynczych zagadnień fizycznych lub zagadnień sprzężonych.

Ponieważ FreeCAD wspiera już intensywnie <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:24px;"> [solver Calculix](FEM_SolverCalculixCxxtools/pl.md) i <img alt="" src=images/FEM_SolverZ88.svg  style="width:24px;"> [solver Z88](FEM_SolverZ88/pl.md) do analiz mechanicznych i termomechanicznych, Elmer jest preferowany do symulacji z zakresu mechaniki płynów *(CFD)*, przepływu ciepła, elektrostatyki i elektrodynamiki. Może być również używany do analiz mechanicznych dzięki równaniu elastyczności lub dowolnej kombinacji wyżej wymienionych równań. Ta kombinacja sprawia, że Elmer jest preferowany do analiz sprzężonych.



## Instalacja

Elmer wymaga dwóch komponentów do powiązania z FreeCADː

-   ElmerGrid to interfejs obsługujący siatki,
-   ElmerSolver obsługuje obliczenia.

Istnieją niezależne programy do obu tych zastosowań, ale ich instalacja i użycie są poza zakresem integracji z FreeCAD.

1.  Pobierz i zainstaluj wersję najbardziej pasującą do Twojego systemu operacyjnego *([Windows](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/windows/) lub [Linux](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/linux/Readme1st.txt))*. Zalecana jest instalacja wersji `mpi`, aby móc skorzystać ze wsparcia dla obliczeń równoległych ({{Version/pl|0.21}}).
2.  We FreeCAD przejdź do **Edycja → Preferencje ... → MES → Elmer**
3.  We [właściwościach MES](FEM_Preferences/pl#Elmer.md) ustaw poprawną ścieżkę dla `ElmerGrid` i `ElmerSolver`, lub {{VersionPlus/pl|0.21}}: ustaw ścieżkę dla `ElmerSolver_mpi` zamiast `ElmerSolver` aby Elmer korzystał ze wszystkich dostępnych rdzeni procesora.

    :   ![Zakładka Elmera w preferencjach MES](images/Preferences-ElmerPath.png )

    :   
        
*Menu dialogowe Elmera pokazujące pola do zlokalizowania ważnych plików wykonywalnych Elmera dla systemu Windows*
        

Elmer jest gotowy do użycia we FreeCAD.


{{VersionMinus/pl|0.19}}

: Uruchom FreeCAD i zmień układ jednostek na **MKS** w [preferencjach](Preferences_Editor/pl#Ogólne_2.md). Zobacz [Uwagi](#Uwagi.md).



## Użycie

1.  Przełącz się na <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [środowisko pracy MES](FEM_Workbench/pl.md)
2.  Utwórz [kontener analizy](FEM_Analysis/pl.md) poprzez wciśnięcie przycisku <img alt="" src=images/FEM_Analysis.svg  style="width:22px;">.
3.  Dodaj solver Elmer, wciskając przycisk <img alt="" src=images/FEM_SolverElmer.svg  style="width:22px;">.
    -   Uwaga: Poprawnie zdefiniowana analiza wymaga co najmniej Modelu *(2D lub 3D)*, Materiału *([płynu](FEM_MaterialFluid/pl.md) lub [ciała stałego](FEM_MaterialSolid/pl.md))*,[siatki](FEM_MeshGmshFromShape.md), równań i warunków brzegowych.

    :   ![](images/Elmer_typical_file_tree.png )

    :   
        
*Przykład [widoku drzewa](Tree_view/pl.md) po dodaniu solvera Elmer*
        
        .
4.  Edytuj parametry solvera w [edytorze właściwości](Property_editor/pl.md), w zakładce **Dane** obiektu SolverElmer w [widoku drzewa](Tree_view/pl.md).
5.  Dwukrotnie kliknij na obiekcie **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** aby przygorować analizę do uruchomienia.

    :   <img alt="" src=images/ElmerSolver_TaskPanel.png  style="width:300px;">

    :   
        
*Okno dialogowe do uruchomienia analizy przy pomocy solvera Elmer.*
        
6.  Wybierz ścieżkę do zapisania analizy wciskając przycisk **...**.
7.  Wciśnij przycisk **Zapisz** aby zapisać pliki analizy w wybranym wcześniej katalogu.
8.  Wciśnij przycisk **Uruchom** aby rozpocząć obliczenia.



## Równania

-   Aby przeprowadzić analizę danego typu zjawiska fizycznego, potrzebne jest równanie *(przepływowe, cieplne, elektrostatyczne\...)*.
-   Uściślenie: Określenie *równanie* jest używane we FreeCAD do pisania różnych zjawisk fizycznych, określenie *Solver* jest używane we wszystkich dokumentach Elmera. Więc jeśli używane jest \"równanie przepływu\" to w rzeczywistości Elmer korzysta z \"solvera przepływowego\" do znalezienia rozwiązania równań Naviera-Stokesa.
-   Można używać jednego lub wielu równań jednocześnie poprzez dodanie obiektu równania pod obiektem SolverElmer, co skutkuje przeprowadzeniem analizy sprzężonej:

1.  Wciśnij przycisk **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** w [widoku drzewa](Tree_view/pl.md)
2.  Wybierz jedno lub wiele dostępnych równań:
    -   <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [równanie deformacji](FEM_EquationDeformation/pl.md).
    -   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [równanie elastyczności](FEM_EquationElasticity/pl.md).
    -   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [równanie siły elektrostatycznej](FEM_EquationElectricforce/pl.md).
    -   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [równanie elektrostatyczne](FEM_EquationElectrostatic/pl.md).
    -   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [równanie przepływu](FEM_EquationFlow/pl.md).
    -   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [równanie strumienia](FEM_EquationFlux/pl.md).
    -   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [równanie ciepła](FEM_EquationHeat/pl.md).
    -   <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [równanie magnetodynamiczne](FEM_EquationMagnetodynamic/pl.md).
    -   <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [równanie magnetodynamiczne 2D](FEM_EquationMagnetodynamic2D/pl.md).



### Ustawienia solvera 

-   W zależności od używanych równań, musisz zmienić domyślne ustawienia solvera. Są one opisane na stronie [Ustawienia solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).
-   Solver będzie domyślnie przeprowadzał analizę stanu ustalonego. Aby przeprowadzić analizę stanu nieustalonego *(jak model zachowuje / zmienia się w czasie)* zobacz sekcję *Timestepping (transient analyses)* na stronie [Ustawienia solvera Elmer](FEM_SolverElmer_SolverSettings/pl#Timestepping_(transient_analyses).md).



### Wizualizacja

Wyniki obliczeń solvera Elmer są zapisywane w obiektach [prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). ([Obiekty wyników](FEM_ResultShow/pl.md) nie są dostępne.)


{{Version/pl|0.21}}

W przypadku analiz stanu nieustalonego uzyskiwany jest obiekt prezentacji graficznej wyników dla każdego kroku czasowego wyników. Aby edytować wszystkie te obiekty naraz, zaznacz je w [widoku drzewa](Tree_view/pl.md) i ustaw parametry w [edytorze właściwości](Property_editor/pl.md). Aby stworzyć animację zmiany wyników w czasie, obecnie najlepiej:

-   Ukryć pierwszy obiekt wyników.
-   Zaznaczyć wybrany obiekt w widoku drzewa, ale nie obiekt prezentacji graficznej wyników.
-   Przesunąć myszką po obiektach prezentacji graficznej wyników.

Uzyskuje się animację taką jak ta:

![](images/ElmerSolver_TransientAnalysis.gif )



## Uwagi

-   **Ważne**: aby uzyskać rozsądne wyniki i móc wymieniać pliki wejściowe solvera Elmer *(nazwane*case.sif*)* z innymi, wszystkie wartości w plikach wejściowych powinny być podane w jednostkach SI. W wersji FreeCAD 0.19 i wcześniejszych jest tak tylko jeśli system jednostek **MKS** jest wybrany w [preferencjach](Preferences_Editor/pl#Ogólne_2.md).
-   Parametry dla solvera i dla równań są niezależnie ustawiane poprzez zakładkę **Dane** [edytora właściwości](Property_editor/pl.md) odpowiednich obiektów w [widoku drzewa](Tree_view/pl.md).
-   Każde równanie będzie miało priorytet, przykładowo, chcąc zobaczyć wpływ konwekcyjnego przepływu gorącego powietrza, równanie przepływu powinno być rozwiązane z wyższym priorytetem niż równanie ciepła, inaczej solver będzie najpierw rozwiązywał przepływ ciepła przez przewodzenie a dopiero potem przepływ płynu.
-   Przypadki 2D vs 3D: Elmer może być używany do analiz 2D i 3D cases. Jednak w przypadkach 2D ściany muszą leżeć na płaszczyźnie XY, inaczej solver będzie próbował obliczyć przypadek 3D na powierzchni a wektory normalne będą niezdefiniowane. Więcej informacji można znaleźć na forum: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48175>



## Dokumentacja

Następujący link daje dostęp do pełnej [dokumentacji solvera Elmer](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/). W jej skład wchodzą instrukcje obsługi i poradniki. Dokumenty i pliki z dopiskiem \"GUI\" oznaczają użycie interfejsu Elmer GUI a nie implementację Elmera we FreeCAD.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverElmer/pl
