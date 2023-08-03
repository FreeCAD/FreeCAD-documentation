---
 GuiCommand:
   Name: FEM ConstraintInitialFlowVelocity
   Name/de: FEM StartbedingungStrömungsgeschwindigkeit
   MenuLocation: Model , Fluid-Randbedingungen , Constraint initial flow velocity
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_ConstraintFlowVelocity/de, FEM_ConstraintInitialPressure/de
---

# FEM ConstraintInitialFlowVelocity/de



## Beschreibung

Erstellt eine Randbedingung für den Startwert einer Strömungsgeschwindigkeit für die Strömungsanalyse eines Fluids.



## Anwendung

1.  Entweder die Schaltfläche **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''FEM ConstraintInitialFlowVelocity'''** drücken oder den Menüeintrag **Model → Fluid-Randbedingungen → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity** auswählen.
2.  Einen Startwert der Strömungsgeschwindigkeit für die Analyse eingeben. Der Wert wird als Kombination der 3 kartesischen Hauptvektorkomponenten (X,Y,Z) angegeben.
3.  Für eine 3D-Analyse wird ein Festkörper (Body) des Modells ausgewählt, für eine 2D-Analyse eine Fläche. Es ist aber auch möglich eine Fläche (z.B. den Einlass einer Leitung) in 3D oder eine Kante in 2D auszuwählen.



## Formeln

Eine Beschreibung, wie man Formeln einsetzt, befindet sich im Abschnitt *Formeln* auf der Seite [RandbedingungStrömungsgeschwindigkeit](FEM_ConstraintFlowVelocity/de#Formeln.md).



## Hinweise

In einfachen Analysen ist es nicht erforderlich, einen Startwert für die Strömungsgeschwindigkeit anzugeben, wird aber als bewährte Vorgehensweise empfohlen.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/de
