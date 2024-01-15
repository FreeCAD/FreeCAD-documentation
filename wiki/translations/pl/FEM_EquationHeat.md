---
 GuiCommand:
   Name: FEM EquationHeat
   Name/pl: Równanie ciepła
   MenuLocation: Rozwiąż , Równanie ciepła
   Workbenches: FEM_Workbench/pl
   Version: 0.17
   SeeAlso: FEM_tutorial/pl
---

# FEM EquationHeat/pl



## Opis

To równanie opisuje przepływ ciepła w ciałach sztywnych i płynach.

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Heat Equation** *(równanie ciepła)*.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równanie ciepła** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie ciepła posiada następujące specjalne ustawienia:

-    **Bubbles**: Istnieje również sformułowanie residual-free-bubbles stabilizowanej metody elementów skończonych. Jest bardziej dokładne i nie uwzględnia żadnych członów ad hoc. Jednak może być bardziej kosztowne obliczeniowo. Jeśli zarówno **Uwaga**: Jeśli podczas *first solver iteration* pojawi się ten błąd: ERROR:: IterSolve: Numerical Error: System diverged over maximum tolerance. to metoda **Bubbles** zawiodła. W takim wypadku należy ustawić **[Stabilize](FEM_SolverElmer_SolverSettings/pl#Baza.md)** na {{true/pl}}.

Równanie:

-    **Convection**: Typ konwekcji do użycia w równaniu ciepła.**Uwaga**: Jeśli nie jest to ustawione na *None* to **[Stabilize](FEM_SolverElmer_SolverSettings/pl#Baza.md)** musi być ustawione na {{true/pl}}, inaczej człon konwekcyjny nie będzie uwzględniany w równaniu ciepła.

-    **Phase Change Model**: Model używany do przemiany fazowej (lód w wodę itd.). Model *Spatial 1* korzysta z metody apparent-heat-capacity, *Spatial 2* i *Temporal* są metodami effective-heat-capacity.Więcej informacji o tych modelach można uzyskać w [tym artykule](https://blog.rwth-aachen.de/gfd/files/2017/07/BT_2013_Schueller_elmer_icemole.pdf) (sekcja 2.5.2.2) (w języku niemieckim). Artykuł pokazuje też, że *Spatial 1* ma problemy numeryczne dla większych gradientów temperatur i że *Spatial 2* było preferowane do przemiany lodu w wodę.



## Informacje o cechach analizy 

Równanie ciepła uwzględnia następujące cechy analizy jeśli są zdefiniowane:

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Objętościowe źródło ciepła](FEM_ConstraintBodyHeatSource/pl.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Warunek początkowy temperatury](FEM_ConstraintInitialTemperature/pl.md)
-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Warunek brzegowy temperatury](FEM_ConstraintTemperature/pl.md)



### Uwaga

-   Oprócz analiz 2D, dla wszystkich cech analizy istotne jest żeby były zdefiniowane dla ścian lub brył. Cechy w 3D przypisane do linii i wierzchołków nie są rozpoznawane przez solver Elmer.



## Wynik

Wynikiem jest temperatura w Kelvinach.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationHeat/pl
