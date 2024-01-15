---
 GuiCommand:
   Name: FEM EquationMagnetodynamic2D
   Name/pl: Równanie magnetodynamiczne 2D
   MenuLocation: Rozwiąż , Równania elektromagnetyczne , Równanie magnetodynamiczne 2D
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_EquationMagnetodynamic/pl
---

# FEM EquationMagnetodynamic2D/pl

To równanie przeprowadza wersję 2D analizy [równań Maxwella](https://pl.wikipedia.org/wiki/R%C3%B3wnania_Maxwella) gdy niewiadomą jest składowa z (lub φ).

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Computation of Magnetic Fields in 2D** *(obliczenia pól magnetycznych w 2D)*.

Do bardziej ogólnych analiz za pomocą równań Maxwella w 3D FreeCAD wspiera [równanie magnetodynamiczne](FEM_EquationMagnetodynamic/pl.md). Jednak jeśli możliwe jest przeprowadzenie analizy w 2D to jest to zalecane, ponieważ sformułowanie jest prostsze, a więc obliczenia trwają krócej.



## Użycie

1.  Po dodaniu solvera Elmer zgdonie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania elektromagnetyczne → Równanie magnetodynamiczne 2D** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie magnetodynamiczne 2D posiada następujące specjalne ustawienia:

-    **Angular Frequency**: Częstotliwość wzbudzenia harmonicznego. Używana tylko jeśli **Is Harmonic** jest ustawione na {{true/pl}}.

-    **Calculate Current Density**: Wzynacza [gęstość prądu](https://pl.wikipedia.org/wiki/G%C4%99sto%C5%9B%C4%87_pr%C4%85du_elektrycznego).

-    **Calculate Electric Field**: Wyznacza [wektorowe pole elektryczne](https://pl.wikipedia.org/wiki/Pole_elektryczne).

-    **Calculate Elemental Fields**: Wyznacza pola elektromagnetyczne w każdym elemencie siatki. Może to być przydatne do poszukiwania nieciągłości w siatkach.**Uwaga**: obecnie FreeCAD nie może poprawnie wyświetlić tego wyniku. Nie ma on więc praktycznego zastosowania na ten moment.

-    **Calculate Harmonic Loss**: Wyznacza liniową i kwadratową harmoniczną utratę mocy. Zobacz dokument [Elmer models manual](https://www.elmerfem.org/blog/documentation/), sekcję *Loss Estimation Using the Fourier Series* aby uzyskać więcej informacji.

-    **Calculate Joule Heating**: Oblicza [grzanie Joule\'a](https://en.wikipedia.org/wiki/Joule_heating).

-    **Calculate Magnetic Strength**: Wyznacza [siłę pola magnetycznego](https://pl.wikipedia.org/wiki/Pole_magnetyczne).

-    **Calculate Maxwell Stress**: Wyznacza pole [tensora naprężeń Maxwella](https://en.wikipedia.org/wiki/Maxwell_stress_tensor).

-    **Calculate Nodal Fields**: Wyznacza pola w każdym węźle siatki. Domyślnie ustawione na {{true/pl}}. Jeśli żadna inna właściwość **Calculate *** nie jest ustawiona na {{true/pl}} to wyznacza tylko gęstość strumienia magnetycznego.

-    **Calculate Nodal Forces**: Wyznacza siły dla każdego węzła siatki. Wyniki mogą być użyte do dalszej analizy mechanicznej.

-    **Calculate Nodal Heating**: Wyznacza pole skalarowe grzania Joule\'a dla każdego węzła siatki.

-    **Is Harmonic**: Czy siła elektromotoryczna jest harmonicznie wzbudzana (prąd stały). Jeśli ta właściwość jest ustawiona na {{true/pl}} to właściwość **Angular Frequency** musi mieć wartość \> 0.



## Informacje o cechach analizy 

Równanie magnetodynamiczne 2D uwzględnia następujące cechy analizy jeśli są zdefiniowane:

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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationMagnetodynamic2D/pl
