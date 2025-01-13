# FEM SolverElmer SolverSettings/pl
Ta strona opisuje ustawienia dla [solvera Elmer](FEM_SolverElmer/pl.md).



# Ogólne

Elmer jest solverem do zagadnień sprzężonych. Możesz więc używać wielu głównych równań do przeprowadzania analiz. Poszczególne równania są wymienione na stronie przedstawiającej [Solver Elmer](FEM_SolverElmer/pl#Równania.md).

Dostępne są ustawienia solvera wspólne dla wszystkich równań. Zostały opisane tutaj. Ustawienia dostępne tylko dla danego równania są opisane na stronie tego równania.

Elmer oferuje [typy analiz](#Typy.md) *steady-state* *(stan ustalony)* i *transient* *(stan nieustalony)* oraz dwa główne systemy rozwiązywania, [liniowy](#Układ_liniowy.md) i [nieliniowy](#Układ_nieliniowy.md). Układ nieliniowy jest używany do <img alt="" src=images/FEM_EquationFlow.svg  style="width:24px;"> [równania przepływu](FEM_EquationFlow/pl.md) i <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [równania ciepła](FEM_EquationHeat/pl.md).



# Edycja ustawień 

Ustawienia solvera można znaleźć w [edytorze właściwości](Property_editor/pl.md) po kliknięciu na równaniu w [widoku drzewa](Tree_view/pl.md). Możesz je tam edytować bezpośrednio, jak każdą inną właściwość.

## Solver



### Układ współrzędnych 

Domyślny układ współrzędnych to *Cartesian 3D* *(kartezjański 3D)*. Niektóre równania nie mogą korzystać ze wszystkich układów współrzędnych. Jest to opisane na stronach Wiki odpowiednich równań.



### Przyrosty czasowe *(analizy stanu nieustalonego)* 

**Uwaga**: FreeCAD 0.20.x ma już następujące ustawienia, ale zapisywane są wyniki tylko dla ostatniej chwili czasowej. Od FreeCAD 0.21 wyniki są zapisywane dla różnych chwil czasowych.

Dla analiz stanu nieustalonego należy zdefiniować przyrosty czasowe. Jest to robione przy pomocy następujących ustawień:

-    **BDFOrder**: Rząd metody *BDF* ([Backward Differentiation Formula](https://en.wikipedia.org/wiki/Backward_differentiation_formula)). Zalecane jest używanie domyślnej wartości *2*.

-    **Output Intervals**: Szereg interwałów. Wyniki będą zapisywane zgodnie z tymi interwałami. Przykładowo, jeśli wyniki mają być zapisywane co trzeci krok czasowy, należy ustawić *3*. Szereg odpowiada właściwości **Timestep Intervals**.
    **Uwaga:** Pierwszy wynik będzie zawsze dla pierwszego kroku czasowego. Aby np. uzyskać wyniki po 25 % całkowitego czasu i jeśli ostatni wynik ma być dla końcowego czasu, należy ustawić **Output Intervals** na *5* a **Timestep Intervals** na *21*. {{Version/pl|0.21}}

-    **Timestep Intervals**: Szereg interwałów czasowych. Solver będzie przeliczał jeden interwał po drugim. Przykładowo, jeśli solver ma przeliczyć pierwsze 10 sekund w krokach po 0.1 sekund a następnie 50 sekund w krokach po 1 sekundzie i się zatrzymać to należy ustawić interwały czasowe \[100, 50\] i interwały rozmiaru kroków \[0.1, 1.0\].

-    **Timestep Sizes**: Szereg rozmiarów kroków czasowych. Jednostką czasu jest sekunda. Szereg odpowiada właściwości **Timestep Intervals**.

**Uwaga:** Chociaż używane są pojęcia \"chwile czasowe\" i \"sekundy\", chwile czasowe są właściwie postępami solvera jeśli analiza nie jest zależna od czasu.

Aby zobaczyć jak wizualizować wyniki, sprawdź stronę [Elmer wizualizacja](FEM_SolverElmer/pl#Wizualizacja.md).



### Typ

-    **Simulation type**: Czy analiza jest *Steady state* *(stan ustalony)*, *Transient* *(stan nieustalony)* czy po prostu *Scanning* *(skanowanie)*. Stan nieustalony oznacza, że liczona jest ewolucja układu w czasie. Zobacz sekcję [Przyrosty czasowe](#Przyrosty_czasowe_''(analizy_stanu_nieustalonego)''.md) aby sprawdzić wymagane ustawienia.

-    **Steady State Max Iterations**: Maksymalna liczba iteracji solvera stanu ustalonego.

-    **Steady State Min Iterations**: Minimalna liczba iteracji solvera stanu ustalonego.



## Równanie



### Podstawa

Wszystkie równania mają te właściwości:

-    **Label**: Nazwa równania w widoku drzewa.

-    **Priority**: Liczba określająca priorytet tego równania w stosunku do innych równań w analizie. Równanie z najwyższą liczbą będzie rozwiązywane jako pierwsze. Jeśli dwa równania mają tą samą liczbę, to której jest pierwsze w widoku drzewa będzie rozwiązywane najpierw.

-    **Stabilize**: Jeśli ta właściwość jest ustawiona na {{true/pl}} to solver będzie korzystał ze stabilizowanej metody elementów skończonych podczas rozwiązywania równania ciepła z członem konwekcyjnym. Jeśli ta właściwość jest ustawiona na {{false/pl}}, zamiast tego będzie używana stabilizacja Residual Free Bubble *(RFB)*. Jeśli dominuje konwekcja, stabilizacja jest konieczna do rozwiązania równania.



### Układ liniowy 

Ten układ ma następujące właściwości:

-    **BiCGstabl Degree**: Rząd wielomianu dla iteracyjnej metody solvera *BiCGStabl*. Ma to efekt tylko jeśli właściwość **Linear Solver Type** jest ustawiona na *Iterative* a właściwość **Linear Iterative Method** jest ustawiona na *BiCGStabl*. Na początek zalecane jest użycie domyślnej wartości {{Value|2}}.

-    **Idrs Parameter**: Parametr dla iteracyjnej metody solvera *Idrs*. Ma to efekt tylko jeśli właściwość **Linear Solver Type** jest ustawiona na *Iterative* a właściwość **Linear Iterative Method** jest ustawiona na *Idrs*. Na początek zalecane jest użycie domyślnej wartości {{Value|2}}. Ustawienie wartości {{Value|3}} może zwiększyć trochę szybkość obliczeń. Dla analiz przepływu metoda *Idrs* jest do 30 % szybsza niż domyślna metoda *BiCGStab*.

-    **Linear Direct Method**: Metoda używana do rozwiązywania bezpośredniego. Ma to efekt tylko jeśli właściwość Możliwe metody to *Banded*, *MUMPS* i *Umpfpack*. Zauważ, że *MUMPS* zwykle wymaga instalacji przed użyciem.**Uwaga**: przy używaniu więcej niż jednego rdzenia procesora dla solvera ({{Version/pl|0.21}}) można używać tylko *MUMPS*. [MUMPS](https://mumps-solver.org/) musi być zainstalowane ręcznie dla solvera Elmer. Dostępne jest do pobrania tylko po wysłaniu prośby mailem.

-    **Linear Iterations**: Maksymalna liczba iteracji dla solvera iteracyjnego. Ma to efekt tylko jeśli właściwość **Linear Solver Type** jest ustawiona na *Iterative*.

-    **Linear Iterative Method**: Metoda używana do rozwiązywania iteracyjnego. Ma to efekt tylko jeśli właściwość **Linear Solver Type** jest ustawiona na *Iterative*.

-    **Linear Preconditioning**: Metoda używana do prekondycjonowania. Więcej informacji na ten temat można znaleźć w prezentacji [Linear Solvers of Elmer in serial & parallel](http://www.nic.funet.fi/index/elmer/slides/ElmerLinearSolvers.pdf) *(strona 8)*.

-    **Linear Solver Type**: Czy rozwiązywanie jest *Direct* *(bezpośrednie)* czy *Iterative* *(iteracyjne)*.

-    **Linear System Solver Disabled**: Wyłącza solvera liniowy. Należy tego używać tylko w szczegółnych przypadkach.Można tego użyć do tymczasowego wyłączenia równania, ponieważ nie jest ono wtedy rozwiązywane. Są jednak przypadki gdy solver zamiast tego trafia na nieskończoną pętlę

-    **Linear Tolerance**: Tolerancja do zatrzymania solvera. Jeśli błąd jest mniejszy niż tolerancja, praca solvera zostanie zakończona. W innym wypadku, przeprowadzona zostanie pełna liczba iteracji określona przez właściwość W dzienniku pracy solvera Elmer można zobaczyć jak błąd jest minimalizowany podczas działania solvera. *(Zobacz w dzienniku na końcu każdej iteracji solvera wartość za*Relative Change*)*. Jeśli nie spada to poniżej konkretnej wartości, ale osiąga wartość powyżej aktualnej tolerancji, która jest dla Ciebie akceptowalna, możesz zwiększyć tolerancję.



### Układ nieliniowy 

Ten układ jest iteracyjny i ma następujące właściwości:

-    **Nonlinear Iterations**: Maksymalna liczba iteracji.

-    **Nonlinear Newton After Iterations**: Solver nieliniowy zaczyna obliczenia z niezawodnym algorytmem*Picard*. Po kilku iteracjach algorytm jest zmieniany na *Newton*, który zbiega się szybciej, ale jest mniej niezawodny jeśli wyniki chwilowo się rozbiegają *(mogą występować oscylacje)*. Ta właściwość ustawia liczbę iteracji, po których nastąpi zmiana algorytmu z *Picard* na *Newton*.
    **Uwaga**: zmiana jest dokonywana po tym gdy jedna z tych właściwości zostanie osiągnięta pierwsza: **Nonlinear Newton After Iterations** lub **Nonlinear Newton After Tolerance**.

-    **Nonlinear Newton After Tolerance**: Analogicznie jak **Nonlinear Newton After Iterations**, ale tutaj ustawiana jest tolerancja. Jest to norma nieliniowego residuum. Jeśli to zostanie osiągnięte, nastąpi zmiana algorytmu z *Picard* na *Newton*.

-    **Nonlinear Tolerance**: Tolerancja do zatrzymania solvera. Jeśli błąd jest mniejszy niż tolerancja, praca solvera zostanie zakończona. W innym wypadku, przeprowadzona będzie pełna liczba iteracji określonych przez właściwość **Nonlinear Iterations**.
    W dzienniku pracy solvera Elmer można zobaczyć jak błąd jest minimalizowany podczas pracy solvera. Jeśli nie schodzi on poniżej określonej wartości, która jest akceptowalna, ale jest powyżej aktualnej tolerancji, możesz zwiększyć tolerancję.

-    **Relaxation Factor**: To jest najważniejsze ustawienie w przypadku gdy solver się nie zbiega:



#### Współczynnik relaksacji 

Jeśli wyniki iteracji solvera oscylują numerycznie, wtedy nie mogą się zbiec do finalnej, stabilnej wartości. Aby tego uniknąć, obliczona zmienna $T_{i}$ i-tej iteracji nie jest brana jako wejście do następnej iteracji, ale wykorzystywana jest wartość $T_{i}^{'}$, która jest \"tłumiona\" z wynikiem poprzedniej iteracji. Współczynnik relaksacji $\lambda$ jest więc definiowany jako:

$\quad
T_{i}^{'} = \lambda T_{i}+\left(1-\lambda\right)T_{i-1}$

Zatem przy domyślnej wartości 1.0 nie jest używane tłumienie. Im mniejsza wartość $\lambda$, tym większe tłumienie i dłuższy czas osiąganie zbieżności. Więc jeśli solver się nie zbiega, zacznij zmieniać współczynnik relaksacji do 0.9, następnie do 0.8 itd. Wartości poniżej 0.3 są nietypowe i jeśli ich potrzebujesz, powinieneś przyjrzeć się bliżej podstawom matematycznym Twojej analizy. Dla przypadków gdzie uzyskujesz prawidłową zbieżność, możesz ustawić $\lambda$ powyżej 1.0 aby przyspieszyć osiąganie zbieżności.



### Stan ustalony 

Ta część ustawień ma tylko jedną właściwość:

-    **Steady State Tolerance**: Określona tolerancja stanu ustalonego lub układu sprzężonego. Solvery wszystkich równań muszą spełnić własne tolerancje dla zmiennej $\omega^2$, którą liczą zanim cały układ zostanie uznany za zbieżny. Kryterium tolerancji to:

$\quad
\left\Vert u_{i}-u_{i-1}\right\Vert <\epsilon\left\Vert u_{i}\right\Vert$

podczas gdy $\epsilon$ jest tolerancją stanu ustalonego a $u_{i}$ jest obliczaną zmienną w i-tej iteracji.


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverElmer SolverSettings/pl
