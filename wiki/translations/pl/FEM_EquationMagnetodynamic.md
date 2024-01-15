---
 GuiCommand:
   Name: FEM EquationMagnetodynamic
   Name/pl: Równanie magnetodynamiczne
   MenuLocation: Rozwiąż, Równania elektromagnetyczne , Równanie magnetodynamiczne
   Workbenches: FEM_Workbench
   Version: 0.21
   SeeAlso: FEM_EquationMagnetodynamic2D/pl
---

# FEM EquationMagnetodynamic/pl

To równanie przeprowadza analizę z użyciem [równań Maxwella](https://pl.wikipedia.org/wiki/R%C3%B3wnania_Maxwella).

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Computation of Magnetic Fields in 3D** *(obliczenia pól magnetycznych w 3D)*.

Jeśli możliwe jest przeprowadzenie analizy 2D, prostsze sformułowanie może być uzyte skutkując krótszymi obliczeniami. Do 2D, FreeCAD wspiera [równanie magnetodynamiczne 2D](FEM_EquationMagnetodynamic2D/pl.md) solvera Elmer.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [tym opisem](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania elektromagnetyczne → Równanie magnetodynamiczne** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.
4.  Zalecane jest ustawienie w [ustawieniach solvera dla układu liniowego](FEM_SolverElmer_SolverSettings/pl#Układ_liniowy.md) właściwości **Linear Iterative Method** na **BiCGStabl**, właściwości **BiCGstabl Degree** na **4** zaś właściwości **Linear Preconditioning** na **None**. To zapewnia rozwiązanie równania w większości przypadków. Po uzyskaniu rozwiązania, te parametry można zmienić w razie potrzeby.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie magnetodynamiczne posiada następujące specjalne ustawieniaː



### Układ liniowy 

-    **Linear System Refactorize**: Refaktoryzuje macierz układu.



### Magnetodynamiczne

-    **Angular Frequency**: Częstotliwość wzbudzenia harmonicznego. Używana tylko jeśli **Is Harmonic** jest ustawione na {{true/pl}}.

-    **Automated Source Projection BCs**: Zobacz dokument [Elmer models manual](http://www.elmerfem.org/blog/documentation/), sekcję *Computation of Magnetic Fields in 3D* aby uzyskać więcej informacji.

-    **FixInput Current Density**: Zapewnia zbieżność gęstości prądu.

-    **Is Harmonic**: Czy siła elektromotoryczna jest harmonicznie wzbudzana (prąd stały). Jeśli ta właściwość jest ustawiona na {{true/pl}} to właściwość **Angular Frequency** musi mieć wartość \> 0.

-    **Lagrange Gauge Penalization Coefficient**: Zobacz dokument [Elmer models manual](http://www.elmerfem.org/blog/documentation/), sekcję *Computation of Magnetic Fields in 3D* aby uzyskać więcej informacji.

-    **Quadratic Approximation**: Umożliwia aproksymację drugiego rzędu prądu zasilania.**Uwaga:** Domyślny rząd [siatek Gmsh](FEM_MeshGmshFromShape/pl.md) we FreeCAD to drugi. Przy korzystaniu z siatek drugiego rzędu, konieczne jest ustawienie tej właściwości na Jednak dla większości zastosowań siatki pierwszego rzędu są wystarczające. Wyjątek stanowi przypadek, gdy filtr izokonturowy powinien być użyty do wizualizacji wyników. Wtedy użycie siatki drugiego rzędu, a więc również ustawienie właściwości **Quadratic Approximation** na {{true/pl}} jest zalecane.

-    **Static Conductivity**: Zobacz dokument [Elmer models manual](http://www.elmerfem.org/blog/documentation/), sekcję *Computation of Magnetic Fields in 3D* aby uzyskać więcej informacji.

-    **Use Lagrange Gauge**: Zobacz dokument [Elmer models manual](http://www.elmerfem.org/blog/documentation/), sekcję *Computation of Magnetic Fields in 3D* aby uzyskać więcej informacji.

-    **Use Piola Transform**: Musi być {{true/pl}} jeśli funkcje bazowe do interpolacji elementu krawędziowego są wybrane do bycia członkami rodziny optymalnych krawędzi elementów lub jeśli używana jest aproksymacja drugiego rzędu.

-    **Use Tree Gauge**: Zobacz dokument [Elmer models manual](http://www.elmerfem.org/blog/documentation/), sekcję *Computation of Magnetic Fields in 3D* aby uzyskać więcej informacji. Właściwość ta będzie ignorowana jeśli **Use Piola Transform** jest ustawione na {{true/pl}}.



## Wyniki

-    **Calculate Current Density**: Wyznacza [gęstość prądu elektrycznego](https://pl.wikipedia.org/wiki/G%C4%99sto%C5%9B%C4%87_pr%C4%85du_elektrycznego).

-    **Calculate Electric Field**: Wyznacza [wektorowe pole elektryczne](https://pl.wikipedia.org/wiki/Pole_elektryczne).

-    **Calculate Elemental Fields**: Wyznacza pola elektromagnetyczne w każdym elemencie siatki. Może to być przydatne do poszukiwania nieciągłości w siatkach.**Uwaga**: obecnie FreeCAD nie może poprawnie wyświetlić tego wyniku. Nie ma on więc praktycznego zastosowania na ten moment.

-    **Calculate Harmonic Loss**: Wyznacza liniową i kwadratową harmoniczną utratę mocy. Zobacz dokument [Elmer models manual](https://www.elmerfem.org/blog/documentation/), sekcję *Loss Estimation Using the Fourier Series* aby uzyskać więcej informacji.

-    **Calculate Joule Heating**: Oblicza [grzanie Joule\'a](https://en.wikipedia.org/wiki/Joule_heating).

-    **Calculate Magnetic Strength**: Wyznacza [siłę pola magnetycznego](https://pl.wikipedia.org/wiki/Pole_magnetyczne).

-    **Calculate Maxwell Stress**: Wyznacza pole [tensora naprężeń Maxwella](https://en.wikipedia.org/wiki/Maxwell_stress_tensor).

-    **Calculate Nodal Fields**: Wyznacza pola w każdym węźle siatki. Domyślnie ustawione na {{true/pl}}. Jeśli żadna inna właściwość **Calculate *** nie jest ustawiona na {{true/pl}} to wyznacza tylko gęstość strumienia magnetycznego.

-    **Calculate Nodal Forces**: Wyznacza siły dla każdego węzła siatki. Wyniki mogą być użyte do dalszej analizy mechanicznej.

-    **Calculate Nodal Heating**: Wyznacza pole skalarowe grzania Joule\'a dla każdego węzła siatki.



## Informacje o cechach analizy 

Równanie magnetodynamiczne uwzględnia następujące cechy analizy jeśli są zdefiniowane:

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Warunek brzegowy potencjału elektrostatycznego](FEM_ConstraintElectrostaticPotential/pl.md)
-   <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [Warunek brzegowy gęstości prądu](FEM_ConstraintCurrentDensity/pl.md)
-   <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [Warunek brzegowy magnetyzacji](FEM_ConstraintMagnetization/pl.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Zdefiniuj przenikalność elektryczną próżni](FEM_ConstantVacuumPermittivity/pl.md)



## Wyniki 

Dostępne wyniki zależą od [ustawień solvera](#Ustawienia_solvera.md). Jeśli żadna z właściwości **Calculate *** nie została ustawiona na {{true/pl}} to obliczany jest tylko potencjał elektryczny (nazwany **av** w wynikach). W przeciwnym wypadku dostępne będą też odpowiednie dodatkowe wyniki.

Możliwe wyniki to:

-   Gęstość prądu w $\rm A/m^2$
-   Wartości wektora pola elektrycznego w $\rm V/m$
-   Harmoniczna utrata mocy w $\rm W$
-   Gęstość strumienia magnetycznego w $\rm T$
-   Wartości tensora naprężeń Maxwella w $\rm As/m^3$
-   Siła pola magnetycznego w $\rm A/m$
-   Siła węzłowa w $\rm N$
-   Grzanie Joule\'a w $\rm J$
-   Potencjał w $\rm V$





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationMagnetodynamic/pl
