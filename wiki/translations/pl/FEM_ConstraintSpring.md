---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintSpring
   Name/pl: MES Sprężyna
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Sprężyna
   Workbenches: FEM_Workbench/pl
   Shortcut: 
   Version: 0.20
   SeeAlso: 
}}
{{GuiCommandFemInfo/pl
   Solvers: Elmer
}}
---

# FEM ConstraintSpring/pl



## Opis

Definiuje warunek brzegowy sprężyny, do wykorzystania w analizach mechanicznych z użyciem <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solvera Elmer](FEM_SolverElmer/pl.md).


<small>(v0.21)</small> 

: Sprężyna może być wykorzystana w równaniach <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [deformacji](FEM_EquationDeformation/pl.md) i <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [elastyczności](FEM_EquationElasticity/pl.md).



## Użycie

1.  Użyj przycisku **<img src="images/FEM_ConstraintSpring.svg" width=16px> [Sprężyna](FEM_ConstraintSpring/pl.md)** lub opcji **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintSpring.svg" width=16px> Sprężyna** w menu.
2.  Wciśnij przycisk **Dodaj**.
3.  W [widoku 3D](3D_view/pl.md) wybierz ściany, do których sprężyna powinna zostać przyłożona. Aby usunąć ściany z zaznaczenia, wciśnij przycisk **Usuń** i kliknij na nich.
4.  Zdefiniuj sztywność w kierunku normalnym lub stycznym (w N/m) i wybierz, którą Elmer powinien użyć.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSpring/pl
