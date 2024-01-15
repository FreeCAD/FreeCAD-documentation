---
 TutorialInfo:l
   Topic: Analiza MES
   Level: Początkujący
   Time: 10 minut
   Author: http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd
   FCVersion: 0.16.6377 lub nowszy
---

# FEM CalculiX Cantilever 3D/pl







## Wprowadzenie

Ten przykład ma na celu zaprezentowanie jak prosta analiza metodą elementów skończonych *(**MES**)* w [środowisku pracy MES](FEM_Workbench/pl.md) programu FreeCAD wygląda w interfejsie programu i jak można zwizualizować wyniki. Ten przykład ilustruje jak uruchomić analizę i jak zmienić wartość oraz kierunek obciążenia. Ponadto, ponieważ plik przykładu jest dostępny w każdej instalacji programu, jest to przydatne i proste sprawdzenie do uruchomienia dla upewnienia się, że środowisko pracy MES działa prawidłowo.

<img alt="" src=images/FEM_example01_pic10.png  style="width:700px;">



## Wymagania

-   Kompatybilna wersja programu FreeCAD wskazana w tabeli z informacjami o przykładzie.

    :   Użyj opcji **Pomoc → Informacje o FreeCAD** aby sprawdzić jaka wersja programu jest zainstalowana.
-   Nie jest wymagane żadne zewnętrzne oprogramowanie aby załadować plik przykładu, obejrzeć siatkę i geometrię oraz zwizualizować wyniki.
-   Do ponownego uruchomienia obliczeń na komputerze musi być zainstalowany solver CalculiX. Najprawdopodobniej solver ten został już zainstalowany razem z programem FreeCAD. Jeśli tak nie jest, zobacz stronę [Instalacja środowiska MES](FEM_Install/pl.md).



## Przygotuj plik przykładu 



### Załaduj plik przykładu 

-   Uruchom program FreeCAD.
-   Jeśli nie jest aktywna strona startowa, załaduj i otwórz ją.
-   Otwórz przykład \"FemCalculixCantilever3D.FcStd\".

<img alt="" src=images/FEM_example01_pic11.png  style="width:700px;">



### Aktywuj kontener analizy 

-   Do pracy z analizą wymagana jest aktywacja kontenera analizy.
-   W [widoku drzewa](Tree_view/pl.md) kliknij dwukrotnie na obiekcie <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> **Analiza**,
-   lub kliknij prawym przyciskiem myszki na obiekcie <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> **Analiza** i wybierz opcję **Aktywuj analizę**.

<img alt="" src=images/FEM_example01_pic12.png  style="width:700px;">



### Kontener analizy i jego obiekty 

-   Po aktywacji analizy FreeCAD sam zmieni środowisko pracy na MES.
-   Do przeprowadzenia statycznej analizy mechanicznej potrzeba przynajmniej 5 podstawowych obiektów *(lub ich bardziej zaawansowanych odpowiedników)*.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> kontener analizy,

1.  <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> solver,
2.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> materiał,
3.  <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> warunek brzegowy utwierdzenia,
4.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> obciążenie siłą,
5.  <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> siatka MES.

-   W tym przykładzie, wyniki <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> również są uwzględnione.



### Wizualizacja wyników 

1.  Upewnij się, że analiza jest aktywna.
2.  Upewnij się, że analiza nadal zawiera obiekt wyników, jeśli nie to ponownie załaduj plik przykładu.
3.  Dwukrotnie kliknij na obiekcie wyników <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;">bul zaznacz go i wciśnij przycisk <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Pokaż wyniki](FEM_ResultShow/pl.md).
4.  W oknie dialogowym wybierz `Przemieszczenie z`. Pokazuje `-86.93 mm` w kierunku -z. Ma to sens, ponieważ siła też działa w tym kierunku.
5.  Aktywuj pole przy dolnym suwaku do pokazywania przemieszczeń.
6.  Suwaka można użyć do wyświetlenia deformacji siatki w prosty sposób.
7.  Sprawdź różne typy wyników żeby zobaczyć jakie wyniki są dostępne.

<img alt="" src=images/FEM_example01_pic13.png  style="width:400px;">



### Czyszczenie wyników 

1.  Upewnij się, że analiza jest aktywna.
2.  Aby usunąć wyniki: wciśnij przycisk <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Usuń wyniki](FEM_ResultsPurge/pl.md).



### Uruchamianie analizy 

-   W [widoku drzewa](Tree_view/pl.md) kliknij dwukrotnie na obiekcie solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
-   W [panelu zadań](Task_panel/pl.md) obiektu solvera upewnij się, że analiza statyczna jest zaznaczona.
-   Wciśnij przycisk **Zapisz plik .inp** w tym samym panelu zadań. Obserwuj okno wiadomości aż pokaże komunikat \"write completed\".
-   Wciśnij przycisk **Uruchom CalculiX**. Ponieważ analiza jest bardzo mała, powinna trwać mniej niż sekundę.
-   W polu tekstowym powinien się pojawić zielony komunikat \"CalculiX done without error!\" a w następnej linii \"loading result sets \...\"
-   Właśnie ukończyłeś swoją pierwszą analizę MES we FreeCAD jeśli nie było żadnych błędów.
-   Wciśnij przycisk **Zamknij** w oknie dialogowym.
-   Nowy obiekt wyników powinien być utworzony. Wiesz już jak wizualizować wyniki.
-   Jeśli podczas uruchamiania analizy pojawi się błąd *no solver binary* lub zbliżony, zajrzyj na stronę [Instalacja środowiska MES](FEM_Install/pl.md).

<img alt="" src=images/FEM_example01_pic14.png  style="width:400px;">



### Szybkie uruchamianie analizy 

-   W widoku drzewa zaznacz obiekt solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> w obrębie kontenera analizy <img alt="" src=images/FEM_Analysis.svg  style="width:24px;">.
-   Wciśnij przycisk <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Uruchom solver](FEM_SolverRun/pl.md).
-   Plik wejściowy solvera CalculiX zostanie zapisany, CalculiX będzie uruchomiony i pojawi się obiekt wyników.



### Zmienianie wartości i kierunku działania siły 

-   W [widoku drzewa](Tree_view/pl.md) rozwiń <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> CCX_Results i wybierz obiekt <img alt="" src=images/FEM_MeshResult.svg  style="width:24px;"> ResultMesh a następnie wciśnij klawisz **Spacja**.
    -   **Efekt:** Widoczność siatki MES zostanie wyłączona. Model geometryczny jest wciąż widoczny.
-   W [widoku drzewa](Tree_view/pl.md) dwukrotnie kliknij na obiekcie <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> FEMConstraintForce aby otworzyć jego [panel zadań](Task_panel/pl.md)
-   W oknie dialogowym zmień wartość siły na **500000000 N = 500 MN** (**Uwaga:** jednostką siły w oknie dialogowym musi być \[**N**\])
-   Wybierz jedną z długich krawędzi w kierunku x na modelu geometrycznym.
-   Wciśnij przycisk **Kierunek**.
    -   **Efekt:** Czerwone strzałki symbolizujące siłę zmienią kierunek na x, przedstawiając zmianę kierunku działania siły.
-   Ponieważ przyłożone ma być obciążenie rozciągające, należy zaznaczyć pole Odwróć kierunek poprzez kliknięcie na nim.
-   Czerwone strzałki symbolizujące siłę zmienią zwrot.
-   Wciśnij przycisk **OK** w oknie dialogowym.

<img alt="" src=images/FEM_example01_pic15.png  style="width:700px;">

-   Wiesz już jak uruchomić analizę i zwizualizować wyniki.
-   Przemieszczenie w kierunku x powinno wynosić 18.95 mm.

<img alt="" src=images/FEM_example01_pic16.png  style="width:400px;">



## Co dalej? 

-   Ukończyłeś podstawowy przykład dla [środowiska MES](FEM_Workbench/pl.md).
-   Jesteś gotowy na drugi przykład [Poradnik MES](FEM_tutorial/pl.md).
-   Utworzymy belkę wspornikową od zera a wyniki porównamy z teorią belek.


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM CalculiX Cantilever 3D/pl
