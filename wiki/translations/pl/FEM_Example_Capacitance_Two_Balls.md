---
 TutorialInfo:l
   Topic: Analiza metodą elementów skończonych
   Level: Początkujący
   Time: 30 min
   Author: https://wiki.freecadweb.org/User:Sudhanshu_Dubey Sudhanshu Dubey
   FCVersion: 0.19 lub nowszy
   Files: Tworzone automatycznie
---

# FEM Example Capacitance Two Balls/pl







## Wprowadzenie

Ten przykład pokazuje jak zasymulować przypadek 6 z dokumentu [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf), **Electrostatic equation -- Capacitance of two balls** (Równanie elektrostatyczne -- Pojemność elektryczna dwóch kul) przy pomocy [Przykładów MES](FEM_Examples/pl.md). Wyjaśnia jak ustawić przykład, przeanalizować jego różne części, rozwiązać używając [solvera Elmer](FEM_SolverElmer/pl.md) i zwizualizować wyniki za pomocą [filtra przycinania](FEM_PostFilterClipRegion/pl.md).

<img alt="" src=images/Two_balls_result_2.png  style="width:1000px;"> 
*Wynik końcowy tego przykładu*



## Wymagania

-   Kompatybilna wersja programu FreeCAD wskazana w opisie przykładu.

    :   Użyj opcji **Pomoc → Informacje o FreeCAD** aby sprawdzić jaka wersja programu jest zainstalowana
-   Do wczytania przykładu, obejrzenia siatki i geometrii oraz wizualizacji wyników nie jest wymagane żadne zewnętrzne oprogramowanie.
-   Do przeprowadzenia analizy metodą elementów skończonych (MES), solver ELmer musi być zainstalowany na komputerze. Zobacz [tę stronę](FEM_SolverElmer/pl#Instalacja.md) aby dowiedzieć się jak zainstalować solver Elmer.



## Ustaw przykład 



### Załaduj środowisko pracy MES 

-   Uruchom FreeCAD, moduł Start powinien być załadowany
-   Przełącz się na <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [środowisko pracy MES](FEM_Workbench/pl.md).



### Załaduj plik przykładu 

-   Idź do **Narzędzia → [<img src=images/FEM_Examples.svg style="width:24px"> Otwórz przykłady**.
-   Gdy otworzy się okno dialogowe, znajdź i otwórz przykład \"Electrostatics Capacitance Two Balls\". Możesz go łatwo znaleźć w kategoriach **All** lub **Solvers → Elmer**. Aby otworzyć przykład, kliknij na nim dwukrotnie lub zaznacz go i wciśnij przycisk **Setup**.

<img alt="" src=images/Two_balls_selection.png  style="width:300px;">



## Zrozumienie przypadku obliczeniowego 

Ten przypadek przedstawia rozwiązanie pojemności elektrycznej doskonale przewodzących kul w wolnej przestrzeni. Różnica napięć między kulami wywołuje ładunek elektryczny w układzie. Kule mają też własną pojemność elektryczną, która wynika z różnicy napięć z dalekim otoczeniem. Zatem rozwiązania musi być symetryczna macierz 2 x 2 pojemności elektrycznej. Pojemności mogą być obliczone z dwóch różnych konfiguracji napięć.



## Zrozumienie modelu 

-   Model zawiera trzy kule.

1.  Dwie mniejsze są doskonale przewodzące.
2.  Większa symuluje otaczające powietrze.

-   Dwie mniejsze kule są ze sobą scalone a następnie wycięte z większej kuli.

<img alt="" src=images/Two_balls_model_full.png  style="width:1000px;"> 
*Początkowy model*



### Kontener analizy i jego obiekty 

Obiekty używane w tej analizie elektrostatycznej:

1.  <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> Kontener analizy
2.  <img alt="" src=images/FEM_SolverElmer.svg  style="width:24px;"> SolverElmer
3.  <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> Electrostatic, równanie elektrostatyczne
4.  <img alt="" src=images/FEM_MaterialFluid.svg  style="width:24px;"> FemMaterial, materiał płynu reprezentujący otaczające powietrze
5.  <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> ElectrostaticPotential, warunki brzegowe (trzy)
6.  <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> ConstantVaccumPermittivity, opcjonalne
7.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> Mesh, siatka [Gmsh](FEM_MeshGmshFromShape/pl.md)
8.  <img alt="" src=images/FEM_MeshRegion.svg  style="width:24px;"> MeshRegion, obszar siatki dla mniejszych kul

![](images/Two_balls_analysis.png ) 
*Obiekty w [widoku drzewa](Tree_view/pl.md)*



### Uruchamianie analizy 

-   W [widoku drzewa](Tree_view/pl.md) dwukrotnie kliknij na obiekcie solvera <img alt="" src=images/FEM_SolverElmer.svg  style="width:24px;">.
-   Wciśnij przycisk **Zapisz** w tym samym panelu zadań. Obserwuj okno dziennika aż pojawi się w nim komunikat \"write completed.\" Możesz zignorować ewentualne ostrzeżenie o przenikalności elektrycznej próżni.
-   Wciśnij przycisk **Uruchom**. Jest to mała analiza, więc powinna trwać tylko kilka sekund. Poczekaj aż zbaczysz komunikat \"ELMER SOLVER FINISHED AT\".
-   Wciśnij przycisk **Zamknij** w panelu zadań po zakończeniu analizy.
-   W widoku drzewa utworzone zostaną dwa nowe obiekty wyników, <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult oraz <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput.

Jeśli podczas uruchamiania analizy pojawi się błąd o pliku wykonywalnym solvera lub zbliżony, sprawdź [instalację](FEM_SolverElmer/pl#Instalacja.md) solvera Elmer.



### Wizualizacja wyników 

-   Upewnij się, że siatka jest niewidoczna. Jeśli tak nie jest, wybierz <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> obiekt siatki i wciśnij klawisz **Spacja** aby przełączyć widoczność.
-   Upewnij się też, że obiekt Cut jest niewidoczny.
-   Dwukrotnie kliknij na obiekcie <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult aby otworzyć jego okno dialogowe.
-   Zmień \"Pole\" na \"potential\" i kliknij **OK**.
-   Zobaczysz, że kula zmieniła kolor na niebieski a gradient po prawej stronie pokazuje wartości od 0 do 1. Powinno to wyglądać mniej więcej tak:

<img alt="" src=images/Two_balls_potential.png  style="width:1000px;">



## Obróbka wyników 

-   Chociaż poprawnie zwizualizowaliśmy wyniki potencjału, widzimy tylko zerowy potencjał powietrza otaczającego dwie kule. Aby zobaczyć potencjał na kulach, musimy zastosować [filtr przycinania](FEM_PostFilterClipRegion/pl.md).
-   W widoku drzewa wybierz obiekt <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult i kliknij przycisk **<img src="images/FEM_PostFilterClipRegion.svg" width=20px> Filtr przycięcia obszaru** na pasku narzędzi.
-   Otworzy to okno z konfiguracjami filtra. Kliknij w nim przycisk **<img src="images/list-add.svg" width=16px> Utwórz** i wybierz <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> Płaszczyzna. Dodaje to płaszczyznę przecinającą siatkę wyników przez środek kuli. Aby wygładzić powierzchnię cięcia, zaznacz opcję **Wytnij komórki**. W końcu kliknij **Zastosuj**.

<img alt="" src=images/Two_balls_postcreate.png  style="width:300px;">

-   W widoku drzewa jest nowy obiekt o nazwie Functions. Zawiera utworzoną <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> Płaszczyznę. Schowaj go wciskając klawisz **Spacja**.
-   Dwukrotnie kliknij na obiekcie <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:24px;"> filtra przycinania w widoku drzewa.
-   Zmień \"Pole\" na \"potential\" i kliknij **OK**.
-   Przełącz widoczność obiektu <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult używając klawisza **Spacja** a powinieneś zobaczyć coś takiego:

<img alt="" src=images/Two_balls_result.png  style="width:1000px;">

Teraz wyraźnie widzimy rozkład potencjału w i dookoła kul.

Zauważ, że gdyby opcja <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:24px;"> [Zastosuj zmiany](FEM_PostApplyChanges.md) była włączona, mógłbyś wybrać \"Pole\" w oknie dialogowym filtra przycinania bezpośrednio a nie musiałbyś otwierać go ponownie po utworzeniu płaszczyzny.



## Znalezienie poejmności 

-   Naszym faktycznym celem jest znalezienie pojemności, która jest zawarta w dokumencie <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput.
-   Dwukrotnie kliknij na dokumencie <img alt="" src=images/TextDocument.svg  style="width:32px;"> SolverElmerOutput aby go otworzyć. Przewiń w dół aż znajdziesz:




    StatElecSolve: Capacitance matrix computation performed (i,j,C_ij)
    StatElecSolve:   1  1    5.07016E+00
    StatElecSolve:   1  2    1.69328E+00
    StatElecSolve:   2  2    5.07201E+00

-   Tutaj naszym poszukiwanym wynikiem jest C~12~ = 1.69328. Ta wartość jest zbliżona do wartości `1.691` podanej w dokumencie [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf). Możemy uzyskać jeszcze dokładniejszy wynik poprzez użycie większego [zagęszczenia siatki](FEM_MeshRegion/pl.md), ale to pozostawiamy użytkownikowi. Zalecamy też przetestowanie [filtra przycinania](FEM_PostFilterClipRegion/pl.md) aby uzyskać wizualny wynik podobny do pierwszego rysunku w tym przykładzie.


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Example Capacitance Two Balls/pl
