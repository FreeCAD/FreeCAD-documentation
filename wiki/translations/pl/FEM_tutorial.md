---
 TutorialInfo:l
   Topic:  Analiza elementów skończonych
   Level:  początkujący
   Time:  10 minut + czas Solvera
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.17 lub nowszy
---

# FEM tutorial/pl







## Wprowadzenie

Niniejszy poradnik ma na celu zapoznanie czytelnika z podstawowym tokiem pracy środowiska MES, jak również z większością dostępnych narzędzi do przeprowadzania analizy statycznej.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">



## Wymagania

-   FreeCAD w wersji 0.17 lub nowszej.
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) i / lub [GMSH](http://geuz.org/gmsh/) zainstalowany w systemie *(dołączony do instalacji FreeCAD)*.
-   [Calculix](http://www.calculix.de/) który jest zainstalowany w systemie *(dołączony do instalacji FreeCAD)*.
-   Czytelnik powinien posiadać podstawową wiedzę na temat korzystania z Środowisk pracy [Część](Part_Workbench/pl.md) oraz [Projekt Części](PartDesign_Workbench/pl.md).



## Sposób postępowania 



### Modelowanie

W tym przykładzie jako obiekt badania używany jest sześcian, ale zamiast niego mogą być używane modele utworzone w środowiskach pracy [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md).

1.  Naciśnij przycisk <img alt="Utwórz nowy pusty dokument" src=images/Std_New.svg  style="width:24px;"> aby utworzyć nowy dokument.
2.  Aktywuj środowisko pracy <img alt="Projekt Części" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).
3.  Stwórz sześcian.
4.  Zmień jego **wymiary** na następujące:
    1.  długość: {{Value|8.00mm}}
    2.  szerokość: {{Value|1.00mm}}
    3.  wysokość: {{Value|1.00mm}}

Teraz mamy model, z którym możemy pracować.



### Tworzenie analizy 

1.  Uruchom środowisko pracy <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [MES](FEM_Workbench/pl.md).
2.  Wybierz z menu **Model → <img src="images/FEM_Analysis.svg" width=16px> Kontener analizy‏‎
**



### Wiązania i siły 

1.  Ukryj siatkę z widoku drzewa.
2.  Wyświetl oryginalny model.
3.  Wybierz <img alt="Warunek brzegowy utwierdzenia" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> [Warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md).
4.  Wybierz tylną stronę sześcianu *(strona na osi **YZ**)* i kliknij na przycisk **OK**.
5.  Wybierz <img alt="Obciążenie siłą" src=images/FEM_ConstraintForce.svg  style="width:24px;"> [Obciążenie siłą](FEM_ConstraintForce/pl.md).
6.  Kliknij w przycisk **Dodaj** wybierz przednią ścianę sześcianu *(ściana równoległa do tylnej)* i ustaw wartość \"Obciążenie \[N\]\" na {{Value|9000000.00}}.
7.  Ustaw wartość **Kierunek** na **-Z** poprzez wybranie jednej z krawędzi równoległych do tego kierunku.
8.  Kliknij na przycisk **OK**.

Ustaliliśmy teraz ograniczenia i siły dla naszych badań statycznych.



### Materiał

1.  Wybierz <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> [Materiał bryły \...](FEM_MaterialSolid/pl.md) i wybierz Calculix-Steel jako materiał.
2.  Kliknij na przycisk **OK**.



### Tworzenie siatki 

Zaleca się wykonanie siatki jako ostatni etap przygotowań do analizy ze względu na skojarzenie z geometrią w programie FreeCAD. W zależności od instalacji programu FreeCAD mogą występować generatory siatek Netgen lub GMSH, można użyć dowolnego z nich.



#### Netgen

1.  Zaznacz model.
2.  Kliknij na przycisk <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:24px;"> [Siatka MES z kształtu przy pomocy generatora Netgen](FEM_MeshNetgenFromShape/pl.md) aby utworzyć siatkę Netgen modelu dla analizy MES.
3.  W oknie dialogowym **Tworzenie siatki**, kliknij przyciski **Zastosuj** oraz **OK**

Możesz także przeciągnąć i upuścić obiekt siatki do analizy mechanicznej, która nie występuje w [widoku drzewa](Tree_view/pl.md).



#### GMSH

1.  Zaznacz model
2.  Kliknij na przycisk <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [Siatka MES z kształtu przy pomocy generatora Gmsh](FEM_MeshGmshFromShape/pl.md): aby utworzyć siatkę Gmsh modelu dla analizy MES.
3.  W oknie dialogowym *\'Tworzenie siatki* kliknij przycisk **Apply** oraz **OK**.

Obecnie mamy do czynienia z siatką naszego obiektu i jesteśmy gotowi do dodania wiązań i sił.



### Uruchomienie solvera 



#### Procedura typowa 

1.  Wybierz obiekt solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> zawarty w kontenerze **Analiza**.
2.  Wybierz z menu <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Kontrola pracy solvera](FEM_SolverControl/pl.md)
3.  Wybierz **Zapisz plik wejściowy .inp**.
4.  Wybierz **Uruchom Calculix**.
5.  Kliknij w przycisk **OK**.



#### Procedura skrócona 

1.  Wybierz obiekt solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> zawarty w kontenerze **Analiza**.
2.  Kliknij w przycisk <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Uruchom analizę](FEM_SolverRun/pl.md).



### Analizowanie wyników 

1.  W widoku drzewa wybierz obiekt **CCX_Wyniki**.
2.  Wybierz <img alt="Pokaż wyniki" src=images/FEM_ResultShow.svg  style="width:24px;"> [Pokaż wyniki](FEM_ResultShow/pl.md).
3.  Wybierz jeden z dostępnych typów wyników, do przeglądania.
4.  Suwak na dole może być użyty do zmiany wyglądu siatki. Pozwala to na wizualizację deformacji doświadczanej przez obiekt, pamiętając, że jest to wynik przybliżony.
5.  Aby usunąć wyniki wybierz <img alt="Oczyszczanie z wyników" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Usuń wyniki](FEM_ResultsPurge/pl.md).


{{Note|Porównanie wyników do poprzedniej wersji pliku przykładowego|Jeśli wybierzesz typ wyniku '''Przemieszczenie Z'', zobaczysz, że uzyskana wartość jest prawie identyczna jak w przykładzie testowym dostarczonym przez FreeCAD. Różnice mogą pojawić się na skutek zastosowania odmiennej jakości siatki i liczby posiadanych przez nią węzłów.}}

Zakończyliśmy teraz prezentacje podstawowego przepływu pracy dla środowiska [MES](FEM_Workbench/pl.md).


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM tutorial/pl
