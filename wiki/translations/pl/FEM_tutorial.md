---
- TutorialInfo   */pl
   Topic   * Analiza elementów skończonych
   Level   * początkujący
   Time   * 10 minut + czas Solvera
   Author   *[http   *//freecadweb.org/wiki/index.php?title=User   *Drei Drei]
   FCVersion   *0.16.6700 lub nowszy
---

# FEM tutorial/pl





## Wprowadzenie

Niniejszy poradnik ma na celu zapoznanie czytelnika z podstawowym tokiem pracy środowiska MES, jak również z większością dostępnych narzędzi do przeprowadzania analizy statycznej.

<img alt="" src=images/FEM_tutorial_result.png  style="width   *600px;">

## Wymagania

-   FreeCAD w wersji 0.16.6700 lub nowszej.
-   [Netgen](http   *//sourceforge.net/projects/netgen-mesher/) i / lub [GMSH](http   *//geuz.org/gmsh/) zainstalowany w systemie.
-   W przypadku uzycia GMSH, zainstaluj [makro GMSH](Macro_GMSH.md) z [Menadzera dodatków](Std_AddonMgr/pl.md), zaprojektowane przez [psicofil](https   *//github.com/psicofil/Macros_FreeCAD).
-   [Calculix](http   *//www.calculix.de/) który jest zainstalowany w systemie.
-   Czytelnik powinien posiadać podstawową wiedzę na temat korzystania z Środowisk pracy [Część](Part_Workbench/pl.md) oraz [Projekt Części](PartDesign_Workbench/pl.md).

## Sposób postępowania 

### Modelowanie

W tym przykładzie jako obiekt badania używany jest sześcian, ale zamiast niego mogą być używane modele utworzone w Środowiskach pracy [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md).

1.  Utwórz [nowy dokument](Std_New/pl.md) *(naciśnij na przycisk <img alt="Utwórz nowy pusty dokument" src=images/Std_New.svg  style="width   *24px;">)*,
2.  Aktywuj środowisko pracy <img alt="Projekt Części" src=images/Workbench_Part.svg  style="width   *24px;"> [Część](Part_Workbench/pl.md).
3.  Stwórz sześcian.
4.  Zmień jego **wymiary** na następujące   *
    1.  wysokość   * 1.00mm
    2.  długość   * 8.00mm
    3.  szerokość   * 1.00mm

Teraz mamy model, z którym możemy pracować.

### Tworzenie analizy 

#### Netgen

1.  Zaznacz model.
2.  Kliknij na przycisk <img alt="" src=images/FEM_Analysis.svg  style="width   *16px;"> [Nowa analiza mechaniczna](FEM_Analysis/pl.md) z menu, aby utworzyć analizę dla wybranego obiektu.
3.  W oknie dialogowym meshhing, kliknij **OK**

Możesz także przeciągnąć i upuścić obiekt siatki do analizy mechanicznej, która nie występuje w [widoku drzewa](Tree_view/pl.md).

#### GMSH

Zaleca się korzystanie z makra użytkownika **psicofil** i jest ono stosowane w tym przykładzie.

1.  Uruchom makro.
2.  Wybierz obiekt, którego chcesz użyć, w tym przypadku jest to nasza kostka.
3.  Zaznacz pole **Tworzenie analizy mechanicznej z oczek siatki**.
4.  Kliknij na przycisk **OK**.

Obecnie mamy do czynienia z siatką naszego obiektu i jesteśmy gotowi do dodania wiązań i sił.

### Wiązania i siły 

1.  Ukryj siatkę z widoku drzewa.
2.  Wyświetl oryginalny model.
3.  Wybierz <img alt="Wiązanie stałej geometrii" src=images/FEM_ConstraintFixed.svg  style="width   *24px;"> [Wiązanie stałej geometrii](FEM_ConstraintFixed/pl.md).
4.  Wybierz tylną stronę sześcianu *(strona na osi **YZ**)* i kliknij na przycisk **OK**.
5.  Wybierz <img alt="Utwórz wiązanie siły" src=images/FEM_ConstraintForce.svg  style="width   *24px;"> [Utwórz wiązanie siły](FEM_ConstraintForce/pl.md).
6.  Wybierz przednią ścianę sześcianu *(ściana równoległa do tylnej)* i ustaw wartość \"Obciążenie powierzchniowe\" na {{Value|9000000.00}}.
7.  Ustaw wartość **Kierunek** na **-Z** poprzez wybranie jednej z krawędzi równoległych do tego kierunku.
8.  Kliknij na przycisk **OK**.

Ustaliliśmy teraz ograniczenia i siły dla naszych badań statycznych.

### Przygotowania końcowe 

1.  Wybierz <img alt="" src=images/FEM_MaterialSolid.svg  style="width   *24px;"> [Materiał bryły\...](FEM_MaterialSolid/pl.md) i wybierz Calculix jako materiał.
2.  Kliknij na przycisk **OK**.

### Uruchomienie silnika Rozwiązującego 

#### Procedura typowa 

1.  Wybierz obiekt solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width   *24px;"> zawarty w **Analizie mechanicznej**.
2.  Wybierz z menu <img alt="" src=images/FEM_SolverControl.svg  style="width   *24px;"> [Rozpoczęcie obliczeń](FEM_SolverControl/pl.md)
3.  Wybierz **Zapisz plik wejściowy Calculix**.
4.  Wybierz **Uruchom Calculix**.
5.  Kliknij w przycisk **Zamknij**.

#### Procedura skrócona 

1.  Wybierz obiekt solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width   *24px;"> zawarty w **Analizie mechanicznej**.
2.  Kliknij w przycisk <img alt="" src=images/FEM_SolverRun.svg  style="width   *24px;"> [Uruchom analizę](FEM_SolverRun/pl.md).

### Analizowanie wyników 

1.  W widoku drzewa wybierz obiekt **Wyniki**.
2.  Wybierz <img alt="Pokaż wyniki" src=images/FEM_ResultShow.svg  style="width   *24px;"> [Pokaż wyniki](FEM_ResultShow/pl.md).
3.  Wybierz jeden z dostępnych typów wyników, do przeglądania.
4.  Suwak na dole może być użyty do zmiany wyglądu siatki. Pozwala to na wizualizację deformacji doświadczanej przez obiekt, pamiętając, że jest to wynik przybliżony.
5.  Aby usunąć wyniki wybierz <img alt="Oczyszczanie z wyników" src=images/FEM_ResultsPurge.svg  style="width   *24px;"> [Oczyszczanie z wyników](FEM_ResultsPurge/pl.md).


{{Note|Porównanie wyników do poprzedniej wersji pliku przykładowego|Jeśli wybierzesz typ wyniku '''Przemieszczenie Z'', zobaczysz, że uzyskana wartość jest prawie identyczna jak w przykładzie testowym dostarczonym przez FreeCAD. Różnice mogą pojawić się na skutek zastosowania odmiennej jakości siatki i liczby posiadanych przez nią węzłów.}}

Zakończyliśmy teraz prezentacje podstawowego przepływu pracy dla środowiska [MES](FEM_Workbench/pl.md).


 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [FEM](Category_FEM.md) > FEM tutorial/pl
