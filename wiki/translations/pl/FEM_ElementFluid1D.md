---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ElementFluid1D
   Name/pl: MES: Przekrój dla przepływu 1D
   MenuLocation: Model , Geometria elementu , Przekrój dla przepływu 1D
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ElementFluid1D/pl



## Opis

Tworzy element MES przekroju płynu dla układów pneumatycznych i hydraulicznych rozwiązywanych przy pomocy solvera CalculiX.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ElementFluid1D.svg" width=16px> '''Przekrój dla przepływu 1D'''**.
    -   Wybierz opcję **Model → Geometria elementu → <img src="images/FEM_ElementFluid1D.svg" width=16px> Przekrój dla przepływu 1D** z menu.
2.  Wybierz rodzaj płynu: ciecz, gaz lub otwarty kanał.
3.  Wybierz rodzaj przekroju: rura Manninga, wlot rury itd.
4.  Wprowadź parametry typu przekroju.
5.  Wybierz i dodaj krawędź.



## Ograniczenia

1.  To narzędzie działa tylko z 3-węzłowymi elementami układu płynowego. Więcej informacji można znaleźć na stronie: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Uwagi

1.  Przykład ustawiania układu hydraulicznego można znaleźć tutaj: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  Do modelowania elementów płynowych dla przepływu 1D wykorzystywane jest [słowo kluczowe \*FLUID SECTION w CalculiX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/pl
