---
 GuiCommand:
   Name: FEM EquationElectricforce
   Name/pl: Równanie siły elektrostatycznej
   MenuLocation: Rozwiąż , Równania elektromagnetyczne , Równanie siły elektrostatycznej
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_EquationElectrostatic/pl
---

# FEM EquationElectricforce/pl



## Opis

To równanie opisuje siłę elektrostatyczną działającą na powierzchni.

Informacje o teorii stojącej za tym równaniem można znaleźć w dokumencie [Elmer models manual](http://www.elmerfem.org/blog/documentation/), w sekcji **Electrostatic force** *(siła elektrostatyczna)*.



## Użycie

1.  Po dodaniu solvera Elmer zgodnie z [opisem na stronie solvera](FEM_SolverElmer/pl#Równania.md), zaznacz go w [widoku drzewa](Tree_view/pl.md).
2.  Wciśnij przycisk <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania elektromagnetyczne → Równanie siły elektrostatycznej**.
3.  Teraz wciśnij przycisk <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> lub wybierz opcję **Rozwiąż → Równania elektromagnetyczne → [Równanie elektrostatyczne](FEM_EquationElectrostatic/pl.md)**. Jest to istotne, ponieważ równanie siły elektrostatycznej potrzebuje pola potencjału wyznaczonego przez równanie elektrostatyczne.
4.  Zmień [ustawienia solvera dla równania](#Ustawienia_solvera.md) lub [ogólne ustawienia solvera](FEM_SolverElmer_SolverSettings/pl.md) jeśli to konieczne.

Równanie siły elektrostatycznej oblicza siłę tylko dla powierzchni z <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [warunkiem brzegowym potencjału elektrostatycznego](FEM_ConstraintElectrostaticPotential/pl.md) jeśli w opcjach warunku brzegowego jest używane **Calculate Electric Force**.



## Ustawienia solvera 

Dla ogólnych ustawień solvera zobacz [konfigurację solvera Elmer](FEM_SolverElmer_SolverSettings/pl.md).

Równanie siły elektrostatycznej posiada to specjalne ustawienieː

-    **Exec Solver**: Domyślnie równanie jest rozwiązywane tylko po zakończeniu kroku czasowego. Oznacza to, że jest po raz pierwszy rozwiązywane po osiągnięciu zbieżności rozwiązania innych równań. Gdy ustawione jest *Always*, równanie jest rozwiązywane po każdej iteracji w obrębie kroku czasowego (dla symulacji [stanu ustalonego](FEM_SolverElmer_SolverSettings/pl#Typ.md) cała symulacja jest jednym krokiem czasowym).



## Informacje o cechach analizy 

Równanie siły elektrostatycznej nie ma własnych cech analizy. Korzysta z <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [warunku brzegowego potencjału elektrostatycznego](FEM_ConstraintElectrostaticPotential/pl.md) z <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [równania elektrostatycznego](FEM_EquationElectrostatic/pl.md). Ważne jest aby w warunku brzegowym użyć opcji **Calculate Electric Force**.



## Wyniki

Wynikiem jest gęstość siły elektrycznej w $\rm N/m^2$.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElectricforce/pl
