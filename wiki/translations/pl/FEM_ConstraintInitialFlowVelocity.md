---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintInitialFlowVelocity
   Name/pl: MES: Warunek początkowy prędkości przepływu
   MenuLocation: Model , Warunki brzegowe dla płynu , Warunek początkowy prędkości przepływu
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintFlowVelocity/pl, FEM_ConstraintInitialPressure/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Elmer
}}
---

# FEM ConstraintInitialFlowVelocity/pl



## Opis

Tworzy warunek początkowy prędkości do analizy przepływu płynu.



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [Warunek początkowy prędkości przepływu](FEM_ConstraintInitialFlowVelocity/pl.md)** lub wybierz opcję **Model → Warunki brzegowe dla płynu → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Warunek początkowy prędkości przepływu**.
2.  Wprowadź wartość początkowej prędkości przepływu dla analizy. Wartość jest wprowadzana jako kombinacja 3 wektorów w kartezjańskim układzie (X,Y,Z).
3.  Do analizy 3D wybierz bryłę z modelu, do analizy 2D wybierz powierzchnię. Jest też jednak możliwe wskazanie powierzchni (np. wlotu rury) w 3D lub krawędzi w 2D.



## Równania

Opis wprowadzania równań jest zawarty w sekcji *Równania* na stronie [warunku brzegowego prędkości przepływu](FEM_ConstraintFlowVelocity#Formulas/pl.md).



## Uwagi

W przypadku prostych analiz nie jest konieczne wprowadzania początkowej prędkości przepływu, ale jest to zalecane.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/pl
