---
 GuiCommand:
   Name: FEM ConstraintInitialTemperature
   Name/pl: MES Warunek początkowy temperatury
   MenuLocation: Model , Warunki brzegowe i obciążenia termiczne , Temperatura początkowa
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM ConstraintInitialTemperature/pl



## Opis

Definiuje temperaturę początkową do analizy termo-mechanicznej



## Użycie

1.  Jest kilka sposobów wywołania tej komendyː
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> '''Warunek początkowy temperatury'''**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia termiczne → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Warunek początkowy temperatury** z menu.
2.  Wprowadź wartość temperatury początkowej dla analizy.



## Ograniczenia

To narzędzie definiuje temperaturę początkową dla wszystkich węzłów siatki modelu - nie ma możliwość wskazania indywidualnych obszarów.



## Uwagi

-   To narzędzie korzysta ze słowa kluczowego \*INITIAL CONDITIONS w CalculiX. Jest ono opisane na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>
-   Temperatura początkowa musi być zdefiniowana dla wszystkich analiz termomechanicznych wykonywanych za pomocą CalculiX, nawet tych w stanie ustalonym.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/pl
