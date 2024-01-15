---
 GuiCommand:
   Name: FEM EquationElasticity
   Name/pl: Równanie elastyczności
   MenuLocation: Rozwiąż , Równania mechaniczne , Równanie elastyczności
   Workbenches: FEM_Workbench/pl
   Version: 0.17
   SeeAlso: FEM_EquationDeformation/pl, FEM_tutorial/pl
---

# FEM EquationElasticity/pl



## Opis

To równanie opisuje właściwości mechaniczne ciał stałych.

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Linear Elasticity** *(liniowa sprężystość)*.



## Użycie

1.  Po dodaniu solvera ELmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationElasticity.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania mechaniczne → Równanie elastyczności** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.

**Uwaga**: Do analiz z nieliniową sprężystością musisz skorzystać z <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [równania deformacji](FEM_EquationDeformation/pl.md) *({{Version/pl|0.21}})*. Równanie elastyczności służy tylko do liniowej sprężystości.

**Uwaga**: Jeśli używasz więcej niż jednego rdzenia procesora dla solvera *({{Version/pl|0.21}})*, nie możesz korzystać z domyślnych ustawień solvera. Używanie tylko jednego rdzenia i domyślnych ustawień solvera jest często szybsze niż używanie wielu rdzeni, ponieważ solver elastyczności jest szybki tylko gdy właściwość **Linear Solver Type** jest ustawiona na *Direct* *(domyślne ustawienie, opisane [tutaj](FEM_SolverElmer_SolverSettings/pl#Układ_liniowy.md))*. Do obliczeń na wielu rdzeniach można używać tylko właściwości **Linear Direct Method** ustawionej na *MUMPS*. Jednak MUMPS nie jest dostępne za darmo do bezpośredniego pobrania.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie elastyczności posiada następujące specjalne ustawienia:

-    **Calculate Pangle**: Czy kąty główne mają być wyznaczone.

-    **Calculate Principal**: Czy wszystkie naprężenia mają być wyznaczone.

-    **Calculate Strains**: Czy odkształcenia mają być wyznaczone. Wyznaczy też naprężenia, nawet jeśli **Calculate Principal** lub **Calculate Stresses** jest ustawione na {{false/pl}}.

-    **Calculate Stresses**: Czy naprężenia mają być wyznaczone. W porównaniu z **Calculate Principal**, naprężenia zredukowane wg kryterium Tresci i naprężenia główne nie zostaną wyznaczone.

-    **Constant Bulk System**: Zobacz instrukcję Elmera aby uzyskać więcej informacji.

-    **Displace Mesh**: Czy siatka może być zdeformowana. Domyślnie jest to ustawione na {{true/pl}} i musi być zmienione na {{false/pl}} do analiz częstotliwości drgań własnych.

-    **Fix Displacement**: Czy przemieszczenia lub siły są ustawione. Tym samym **Model Lumping** jest automatycznie używane.

-    **Geometric Stiffness**: Uwzględnia sztywność geometryczną ciała.

-    **Incompressible**: Obliczanie materiału nieściśliwego w połączeniu z modelem lepkosprężystym Maxwella i niestandardową wartością **Variable**.

-    **Maxwell Material**: Oblicza lepkosprężysty model materiału.

-    **Model Lumping**: Korzysta z [modelu jednowymiarowego](https://en.wikipedia.org/wiki/Lumped-element_model).

-    **Model Lumping Filename**: Plik do zapisu wyników z modelu jednowymiarowego.

-    **Stability Analysis**: Jeśli ta właściwość ma wartość {{true/pl}} to **Eigen Analysis** staje się analizą stateczności (wyboczenia). W innym wypadku przeprowadzana jest analiza modalna (częstotliwości drgań własnych).

-    **Update Transient System**: Zobacz instrukcję solvera Elmer aby uzyskać więcej informacji.

-    **Variable**: Zmienna dla równania elastyczności. Należy to zmieniać tylko jeśli właściwość **Incompressible** jest ustawiona na {{true/pl}} zgodnie z dokumentacją Elmera.

Wartości własne:

-    **Eigen Analysis**: Czy analiza problemu własnego ma być przeprowadzona (wyznaczanie postaci i częstotliwości drgań własnych).

-    **Eigen System Complex**: Ta właściwość powinna być ustawiona na {{true/pl}} jeśli układ własny jest zespolony. Musi być ustawiona na {{false/pl}} dla analiz drgań własnych z tłumieniem.

-    **Eigen System Compute Residuals**: Oblicza residua układu wartości własnych.

-    **Eigen System Damped**: Ustawia tłumioną analizę drgań własnych. Może być używane tylko gdy właściwość **[Linear Solver Type](FEM_SolverElmer_SolverSettings/pl#Układ_liniowy.md)** jest ustawiona na *Iterative*.

-    **Eigen System Select**: Wybór które wartości własne mają być wyznaczone. Zauważ, że wybór *Largest\** *(najwyższe)* powoduje, że analiza trwa w nieskończoność *(aktualne w sierpniu 2022 r.)*.

-    **Eigen System Tolerance**: Tolerancja zbieżności dla solvera iteracyjnego układu własnego. Domyślna wartość to 100 razy **[Linear Tolerance](FEM_SolverElmer_SolverSettings/pl#Układ_liniowy.md)**.

-    **Eigen System Values**: Numer najwyższej postaci drgań własnych jaka ma być wyznaczona.

Równanie:

-    **Plane Stress**: Wyznacza rozwiązanie zgodnie z teorią płaskiego stanu naprężeń. Stosowane tylko do geometrii 2D.



## Informacje o cechach analizy 

Równanie elastyczności uwzględnia następujące cechy analizy jeśli są zdefiniowane:

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md)
-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Warunek brzegowy przemieszczenia](FEM_ConstraintDisplacement/pl.md)
-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Obciążenie siłą](FEM_ConstraintForce/pl.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Warunek początkowy temperatury](FEM_ConstraintInitialTemperature/pl.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md)
-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Obciążenie grawitacją](FEM_ConstraintSelfWeight/pl.md)
-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Sprężyna](FEM_ConstraintSpring/pl.md)



### Uwaga

-   Oprócz analiz 2D, dla wszystkich cech analizy istotne jest żeby były zdefiniowane dla ścian. Cechy w 3D przypisane do linii i wierzchołków nie są rozpoznawane przez solver Elmer.



## Analiza drgań własnych 

Aby przeprowadzić analizę drgań własnych *(wyznaczanie postaci i częstotliwości drgań własnych)* należy:

1.  Ustawić **Eigen Analysis** na {{true/pl}}.
2.  Ustawić **Displace Mesh** na {{false/pl}}.
3.  Ustawić **Eigen System Values** na najwyższy numer postaci drgań własnych jaką chcesz uzyskać. Im mniejsza ta liczba, tym szybsze obliczenia, ponieważ wyższe postaci drgań własnych mogą być pominięte.
4.  Dodać [warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md) i ustawić przynajmniej jedną ścianę ciała jako utwierdzoną.
5.  Uruchomić solver.

Wysoce zalecane jest ustawianie **Linear Solver Type** na *Direct* *(domyślne)*, ponieważ przyspiesza to znacząco obliczenia i zwiększa dokładność wyników.



## Analiza wyboczenia 

Aby przeprowadzić liniową analizę wyboczeniową należy zrobić to samo co w przypadku [Analizy drgań własnych](#Analiza_drgań_własnych.md) i dodatkowo:

-   Ustawić **Stability Analysis** na {{true/pl}}



## Wyniki

Dostępne wyniki zależą od [ustawień solvera](#Ustawienia_solvera.md). Jeśli żadna z właściwości **Calculate *** nie została ustawiona na {{true/pl}} to obliczone zostaną tylko przemieszczenia. W przeciwnym wypadku dostępne będą też odpowiednie dodatkowe wyniki. Jeśli właściwość **Eigen Analysis** została ustawiona na {{true/pl}} to wszystkie wyniki będą dostępne dla każdej obliczonej postaci drgań własnych.

Jeśli właściwość **Eigen Analysis** została ustawiona na {{true/pl}} to częstotliwości drgań własnych będą zapisane na końcu dziennika solvera w jego oknie dialogowym i w dokumencie **SolverElmerOutput**, który zostanie utworzony w widoku drzewa po zakończeniu pracy solvera.

**Uwaga:** Wektor przemieszczenia postaci własnej $\vec{d}$ ma niefizyczną wartość, ponieważ wynik jest

$\quad
\vec{d} = c\cdot\vec{u}$

podczas gdy $\vec{u}$ jest wektorem własnym zaś $c$ jest liczbą zespoloną.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElasticity/pl
