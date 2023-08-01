---
- GuiCommand:
   Name: FEM ConstraintInitialPressure
   Name/de: FEM StartbedingungDruck
   MenuLocation: Model - Fluid-Randbedingungen - Constraint initial pressure
   Workbenches: [FEM](FEM_Workbench/de.md)
   Version: 0.21
   SeeAlso: [FEM StartbedingungStrömungsgeschwindigkeit](FEM_ConstraintInitialFlowVelocity/de.md)
---

# FEM ConstraintInitialPressure/de



## Beschreibung

Erstellt eine Randbedingung für den Startwert eines Druckes für die Strömungsanalyse eines Fluids.



## Anwendung

1.  Either press the toolbar button **<img src="images/FEM_ConstraintInitialPressure.svg" width=16px> '''FEM ConstraintInitialPressure'''** or select the menu **Model →  <img src="images/FEM_ConstraintInitialPressure.svg" width=16px> Fluid Constraints → Constraint initial pressure**.
2.  Enter an initial pressure value.
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face.



## Hinweise

For simple analyses, it is not necessary to specify the initial pressure, however also in these cases it is recommended as best practice.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialPressure/de
