---
 GuiCommand:
   Name: FEM EquationFlux
   Name/pl: Równanie strumienia
   MenuLocation: Rozwiąż , Równanie strumienia
   Workbenches: FEM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# FEM EquationFlux/pl

To równanie jest używane do wyznaczenia strumieni pochodzących głównie z równań typu Poissona. Obejmuje to <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [równanie ciepła](FEM_EquationHeat/pl.md) oraz <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [równanie elektrostatyczne](FEM_EquationElectrostatic/pl.md).

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Flux Computation** *(obliczenia strumieni)*.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Wciśnij przycisk <img alt="" src=images/FEM_EquationFlux.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równanie strumienia** z menu.
3.  Teraz dodaj równanie ciepła (przycisk <img alt="" src=images/_FEM_EquationHeat.svg  style="width:24px;"> lub opcja **Rozwiąż→ [równanie ciepła](FEM_EquationHeat/pl.md)**) lub równanie elektrostatyczne (przycisk <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> lub opcja **Rozwiąż → [równanie elektrostatyczne](FEM_EquationElectrostatic/pl.md)**). Jest to istotne, ponieważ równanie strumienia wymaga warunków brzegowych ustawionych dla tych równań.
4.  W przypadku używania równania elektrostatycznego, zmień właściwość **Flux Coefficient** na *None* a właściwość **Flux Variable** na *Potential*.
5.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie strumienia posiada następujące specjalne ustawienia:

-    **Average Within Materials**: Jeśli {{true/pl}}, ciągłość jest wymuszana w obrębie tego samego materiału w nieciągłej dyskretyzacji Galerkina przy pomocy członów funkcji kary nieciągłego sformułowania Galerkina.

-    **Calculate Flux**: Wyznacza wektor strumienia.

-    **Calculate Flux Abs**: Wyznacza wartość bezwzględną wektora strumienia. Wymaga właściwości **Calculate Flux** ustawionej na {{true/pl}}.

-    **Calculate Flux Magnitude**: Wyznacza wartość pola wektorowego. Wymaga właściwości Jest to właściwie to samo co **Calculate Flux Abs**, ale to wymaga mniej pamięci, ponieważ rozwiązuje równanie macierzowe tylko raz. Wadą jest to, że wartości ujemną mogą zostać wprowadzone.

-    **Calculate Grad**: Wyznacza gradient strumienia.

-    **Calculate Grad Abs**: Wyznacza bezwzględny gradient strumienia. Wymaga właściwości **Calculate Grad** ustawionej na {{true/pl}}.

-    **Calculate Grad Magnitude**: Wyznacza wartość pola wektorowego. Wymaga właściwości Jest to właściwie to samo co **Calculate Grad Abs**, ale to wymaga mniej pamięci, ponieważ rozwiązuje równanie macierzowe tylko raz. Wadą jest to, że wartości ujemną mogą zostać wprowadzone.

-    **Discontinuous Galerkin**: Dla nieciągłych pól standardowa aproksymacja Galerkina wprowadza ciągłość, która może być niefizyczna. Rozwiązaniem jest ustawienie tej właściwości na {{true/pl}}. Wtedy wynik może być nieciągły i może nawet być zwizualizowany jako taki.

-    **Enforce Positive Magnitude**: Jeśli {{true/pl}}, ujemne wartości obliczonego pola wielkości są ustawiane na zero.

-    **Flux Coefficient**: Nazwa współczynnika proporcjonalności do obliczenia strumienia.

-    **Flux Variable**: Nazwa zmiennej potencjalnej używanej do obliczenia gradientu.



## Informacje o cechach analizy 

Równanie strumienia nie ma własnych warunków brzegowych. Korzysta z warunków brzegowych <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [równania ciepła](FEM_EquationHeat/pl.md) i <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [równania elektrostatycznego](FEM_EquationElectrostatic/pl.md).



## Wyniki

Dostępne wyniki zależą od [ustawień solvera](#Ustawienia_solvera.md). Jeśli żadna z właściwości **Calculate *** nie została ustawiona na {{true/pl}} to obliczone zostaną tylko przemieszczenia. W przeciwnym wypadku dostępne będą też odpowiednie dodatkowe wyniki.

Wynikowy strumień jest albo strumieniem ciepła w $\rm W/m^2$ (myląco nazwanym \"strumieniem temperatury\") lub strumieniem potencjalnym w $\rm W/m^2$ ($\rm A\cdot V/m^2$).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationFlux/pl
