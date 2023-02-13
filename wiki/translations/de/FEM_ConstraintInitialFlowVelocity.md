---
- GuiCommand:/de
   Name:FEM ConstraintInitialFlowVelocity
   Name/de:FEM RandbedingungInitialeFließgeschwindigkeit
   MenuLocation:Modell → Strömungs-Randbedingungen → Randbedingung initiale Fließgeschwindigkeit
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM RandbedingungFließgeschwindigkeit](FEM_ConstraintFlowVelocity/de.md)
---

# FEM ConstraintInitialFlowVelocity/de


</div>



## Beschreibung

Erstellt eine Startbedingung einer Fließgeschwindigkeit für die Strömungsanalyse einer Flüssigkeit.



## Anwendung


<div class="mw-translate-fuzzy">

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [Randbedingung initiale Fließgeschwindigkeit](FEM_ConstraintInitialFlowVelocity/de.md)** drücken.
    -   Den Menüeintrag **Modell → Strömungs-Randbedingungen → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Randbedingung initiale Fließgeschwindigkeit** auswählen.
2.  Den Startwert der Fließgeschwindigkeit für die Analyse eingeben.
3.  Der Wert wird als Kombination der 3 kartesischen Hauptvektorkomponenten (X,Y,Z) angegeben.


</div>

## Limitation

-   The constraint cannot be oriented other then using the main Cartesian components. This is a limitation of Elmer.



## Hinweise

In the most simple analyses, it is not necessary to specify the initial flow velocity, however it is recommended as best practice.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/de
