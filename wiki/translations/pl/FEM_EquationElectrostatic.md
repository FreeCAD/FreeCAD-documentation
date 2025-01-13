---
 GuiCommand:
   Name: FEM EquationElectrostatic
   Name/pl: Równanie elektrostatyczne
   MenuLocation: Rozwiąż , Równania elektromagnetyczne , Równanie elektrostatyczne
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_EquationElectricforce/pl, FEM_Example_Capacitance_Two_Balls/pl
---

# FEM EquationElectrostatic/pl



## Opis

To równanie służy do przeprowadzania analiz elektrostatycznych przy pomocy [prawa Gaussa](https://pl.wikipedia.org/wiki/Prawo_Gaussa_(elektryczno%C5%9B%C4%87)).

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Electrostatics** *(elektrostatyka)*.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania elektromagnetyczne → Równanie elektrostatyczne** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie elektrostatyczne posiada następujące specjalne ustawienia:

-    **Calculate Capacitance Matrix**: Wyznacza macierz pojemności elektrycznej. Macierz ta zawiera ładunki punktowe węzłów siatki.

-    **Calculate Electric Energy**: Wyznacza [potencjalną energię elektryczną](https://en.wikipedia.org/wiki/Electric_potential_energy).

-    **Calculate Electric Field**: Wyznacza [pole elektryczne](https://pl.wikipedia.org/wiki/Pole_elektryczne).

-    **Calculate Electric Flux**: Wyznacza [strumień pola elektrycznego](https://pl.wikipedia.org/wiki/Strumie%C5%84_pola_elektrycznego).

-    **Calculate Surface Charge**: Wyznacza [ładunek powierzchniowy](https://en.wikipedia.org/wiki/Surface_charge).

-    **Capacitance Matrix Filename**: Plik, w którym zapisywana jest macierz pojemności elektrycznej. Używane tylko jeśli właściwość **Calculate Capacitance Matrix** jest ustawiona na {{true/pl}}.

-    **Constant Weights**: Czy używane jest stałe ważenie wyników.

-    **Potential Difference**: Różnica potencjałów w Voltach, dla której liczona jest pojemność elektryczna. Używane tylko jeśli właściwość **Calculate Capacitance Matrix** jest ustawiona na {{false/pl}}. Zatem w praktyce to ustawienie określa napięcie między elektrodami prostego kondensatora. Zauważ, że podane napięcie musi być zgodne z potencjałami zdefiniowanymi w warunku brzegowym.



## Informacje o cechach analizy 

Równanie elektrostatyczne uwzględnia następujące cechy analizy jeśli są zdefiniowane:

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Warunek brzegowy potencjału elektrostatycznego](FEM_ConstraintElectrostaticPotential/pl.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Zdefiniuj przenikalność elektryczną próżni](FEM_ConstantVacuumPermittivity/pl.md)



### Uwaga

Oprócz analiz 2D, dla <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [warunków brzegowych potencjału elektrostatycznego](FEM_ConstraintElectrostaticPotential/pl.md) ważne jest ży działały na ścianie lub objętości. Warunki brzegowe przypisane do linii lub wierzchołków nie będą rozpoznawane przez solver Elmer.



## Wyniki

Dostępne wyniki zależą od [ustawień solvera](#Ustawienia_solvera.md). Jeśli żadna z właściwości **Calculate *** nie została ustawiona na {{true/pl}} to obliczona zostanie tylko gęstość siły elektrycznej i potencjał elektryczny. W przeciwnym wypadku dostępne będą też odpowiednie dodatkowe wyniki.

Możliwe wyniki to:

-   Gęstość energii elektrycznej w $\rm J/m^3$
-   Pole elektryczne w $\rm V/m$
-   Strumień pola elektrycznego w $\rm A\cdot s/m^2$
-   Gęstość energii elektrycznej w $\rm N/m^2$
-   Potencjał elektryczny w $\rm V$
-   Obciążenia potencjalne w $\rm C$





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElectrostatic/pl
