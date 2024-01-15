---
 GuiCommand:
   Name: FEM EquationFlow
   Name/pl: MES: Równanie przepływu
   MenuLocation:  Rozwiąż , Równanie przepływu
   Workbenches: FEM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# FEM EquationFlow/pl

To równanie analizuje przepływ płynów lepkich przy pomocy [równań Naviera-Stokesa](https://pl.wikipedia.org/wiki/R%C3%B3wnania_Naviera-Stokesa).

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Navier-Stokes Equations** *(równania Naviera-Stokesa)*.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationFlow.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równanie przepływu** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie przeplywu posiada następujące specjalne ustawienia:

-    **Div Discretization**: Do ustawienia na {{true/pl}} w przypadku przepływu nieściśliwego dla bardziej stabilnej dyskretyzacji gdy rośnie [liczba Reynoldsa](https://pl.wikipedia.org/wiki/Liczba_Reynoldsa).

-    **Flow Model**: Model przepływu jaki powinien być użyty. Domyślne *Full* uwzględnia człony konwekcji i pochodnych po czasie w modelu. *No convection* wyłącza człony konwekcyjne zaś *Stokes* wyłącza człony konwekcyjne i (jawne) człony pochodnych po czasie.

-    **Gradp Discretization**: Jeśli ustawione na {{true/pl}}, może być użyty ciśnieniowy [warunek brzegowy Dirichleta](https://pl.wikipedia.org/wiki/Warunek_brzegowy_Dirichleta). Ponadto, strumień masy jest dostępny jako naturalny warunek brzegowy.

-    **Variable**: Opcjonalne tylko do analiz 2D: Możesz zmienić domyślną wartość *3* na *2*.**Uwaga**: W takim wypadku żaden z warunków brzegowych przepływu nie może mieć wprowadzonej składowej z.

Równanie:

-    **Convection**: Typ konwekcji do użycia w <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [równaniu ciepła](FEM_EquationHeat/pl.md).**Uwaga**: Do przepływów termicznych musi być ustawiony na *Computed* (domyślne).

-    **Magnetic Induction**: Jeśli ustawione na {{true/pl}}, równanie indukcji magnetycznej będzie rozwiązywane razem z [równaniami Naviera-Stokesa](https://pl.wikipedia.org/wiki/R%C3%B3wnania_Naviera-Stokesa).



### Uwagi dotyczące zbieżności 

Jeśli analiza z użyciem tego solvera się nie zbiega, można wypróbować następujące podejścia (w podanej kolejności)ː

1.  Zmniejszyć wartość **Relaxation Factor**, zobacz [ustawienia układu nieliniowego](FEM_SolverElmer_SolverSettings/pl#Współczynnik_relaksacji.md).
2.  Zwiększyć wartość **Nonlinear Newton After Iterations**, zobacz [ustawienia układu nieliniowego](FEM_SolverElmer_SolverSettings/pl#Układ_nieliniowy.md).
3.  Zmniejszyć liczbę używanych rdzeni procesora, zobacz [preferencje MES](FEM_Preferences/pl#Elmer.md).
4.  Zwiększyć gęstość siatki.



## Informacje o cechach analizy 

Równanie przepływu uwzględnia następujące cechy analizy jeśli są zdefiniowane:

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Warunek brzegowy prędkości przepływu](FEM_ConstraintFlowVelocity/pl.md)
-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Warunek początkowy prędkości przepływu](FEM_ConstraintInitialFlowVelocity/pl.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md)
-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Warunek początkowy ciśnienia](FEM_ConstraintInitialPressure/pl.md) ({{Version/pl|0.21}})



### Uwagi

-   Poza analizami 2D, dla wszystkich powyższych warunków brzegowych ważne jest to, żeby działały na ścianie lub objętości. Warunki brzegowe w 3D przypisane do linii lub wierzchołków nie będą rozpoznane przez solver Elmer.
-   Ponieważ <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md) może być zadane tylko na ściany, obciążenia ciśnieniem nie mogą być używane do analiz 2D.
-   Jeśli nie ma ustawionego żadnego <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [obciążenia ciśnieniem](FEM_ConstraintPressure/pl.md), <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [warunek początkowy ciśnienia](FEM_ConstraintInitialPressure/pl.md) będzie brany pod uwagę tylko jeśli właściwość **Gradp Discretization** jest ustawiona na {{true/pl}}.



## Wyniki

Wynikiem są prędkość w $\rm m/s$ i ciśnienie w $\rm Pa$. Jeśli nie ma ustawionego żadnego <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [warunku początkowego ciśnienia](FEM_ConstraintInitialPressure/pl.md) ani <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [obciążenia ciśnieniem](FEM_ConstraintPressure/pl.md), wynik ciśnienia będzie względny. Ponieważ ciśnienie musi działać na ścianie, bezwzględnych wyników ciśnienia nie da się uzyskać w przypadku analiz 2D.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationFlow/pl
