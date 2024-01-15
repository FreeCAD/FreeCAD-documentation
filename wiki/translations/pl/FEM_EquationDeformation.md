---
 GuiCommand:
   Name: FEM EquationDeformation
   Name/pl: Równanie deformacji
   MenuLocation: Rozwiąż , Równania mechaniczne , Równanie deformacji
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_EquationElasticity/pl, FEM_tutorial/pl
---

# FEM EquationDeformation/pl



## Opis

To równanie opisuje nieliniowo sprężystą deformację ciał stałych.

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Finite Elasticity** *(nieliniowa sprężystość)*.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania mechaniczne → Równanie deformacji** z menu.
3.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [ustawienia solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie deformacji posiada następujące specjalne ustawienia:

-    **Calculate Pangle**: Czy kąty główne mają być wyznaczone.

-    **Calculate Principal**: Czy wszystkie naprężenia mają być wyznaczone.

-    **Calculate Strains**: Czy odkształcenia mają być wyznaczone. Wyznaczy też naprężenia, nawet jeśli **Calculate Principal** lub **Calculate Stresses** jest ustawione na {{false/pl}}.

-    **Calculate Stresses**: Czy naprężenia mają być wyznaczone. W porównaniu z **Calculate Principal**, naprężenia zredukowane wg kryterium Tresci i naprężenia główne nie zostaną wyznaczone.

-    **Initialize State Variables**: Zobacz instrukcję Elmera aby uzyskać więcej informacji.

-    **Mixed Formulation**: Zobacz instrukcję Elmera aby uzyskać więcej informacji.

-    **Neo Hookean Model**: Używa modelu materiałowego neo-Hookean.

-    **Variable**: Zmienna dla równania deformacji. Zmień tam *3* na *2* jeśli masz geometrię 2D. Dla szczególnego przypadku gdy **Mixed Formulation** i **Neo Hookean Model** są ustawione na {{true/pl}}, wartość zmiennej musi być przestrzenią geometrii + 1, więc dla 3D należy zmienić wartość z *3* na *4*.

Równanie:

-    **Plane Stress**: Wyznacza rozwiązanie zgodnie z teorią płaskiego stanu naprężeń. Stosowane tylko do geometrii 2D.



## Informacje o cechach analizy 

Równanie deformacji uwzględnia następujące cechy analizy jeśli są zdefiniowane:

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md)
-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Warunek brzegowy przemieszczenia](FEM_ConstraintDisplacement/pl.md)
-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Obciążenie siłą](FEM_ConstraintForce/pl.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Warunek początkowy temperatury](FEM_ConstraintInitialTemperature/pl.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md)
-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Obciążenie grawitacją](FEM_ConstraintSelfWeight/pl.md)
-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Sprężyna](FEM_ConstraintSpring/pl.md)



### Uwaga

-   Oprócz analiz 2D, dla wszystkich cech analizy istotne jest żeby były zdefiniowane dla ścian. Cechy w 3D przypisane do linii i wierzchołków nie są rozpoznawane przez solver Elmer.



## Wyniki

Dostępne wyniki zależą od [ustawień solvera](#Ustawienia_solvera.md). Jeśli żadna z właściwości **Calculate *** nie została ustawiona na {{true/pl}} to obliczone zostaną tylko przemieszczenia. W przeciwnym wypadku dostępne będą też odpowiednie dodatkowe wyniki.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationDeformation/pl
