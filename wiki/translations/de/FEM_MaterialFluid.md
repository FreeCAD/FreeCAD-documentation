---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM MaterialFluid
   Name/de: FEM MaterialFluide
   MenuLocation: Modell , Materialien , Material für Fluide
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM MaterialFluid/de



## Beschreibung

Erstellt ein Material für Fluide.

![](images/FEMMaterialFluidProperties.png ) 
*Der Aufgabenbereich FEM-Material*



## Anwendung

1.  Zum Erstellen eines neuen MaterialFluid-Objekts, hat man folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/FEM_MaterialFluid.svg" width=16px> [Material für Fluide‏‎](FEM_MaterialFluid/de.md)** drücken.
    -   Den Menüeintrag **Modell → Materialien → <img src="images/FEM_MaterialFluid.svg" width=16px> Material für Fluide‏‎** auswählen.
2.  Ein MaterialFluid-Objekt bearbeiten:
    -   Mit Doppelklick in der [Baumansicht](Tree_view/de.md) auswählen.
3.  Das Aufgaben-Fenster FEM-Material wird geöffnet.
4.  Eine Fluid-Material in der Ausklappliste auswählen. Übliche Arten für Computational Fluid Dynamics (CFD) sind **Air** (Luft) oder **Water** (Wasser).
5.  Wahlweise die Checkbox **Diesen Aufgabenbereich benutzen** aktivieren, um Materialeigenschaften, wie Dichte, kinematische Viskosität, Wärmeleitfähigkeit, usw. anzupassen.
6.  Soll das Fluid auf das ganze Objekt angewendet wird, dürfen keine geometrischen Elemente ausgewählt werden (die Referenfliste bleibt leer). Das Fluid wird auf das ganze Objekt angewendet. Andernfalls wird das Fluid bestimmten Bereichen des Modells von Hand zugeordnet, indem für jeden eingefügten Werkstoff einige ausgewählt werden; dabei sollte kein Bereich ohne ein zugeordnetes Fluid bleiben.
7.  Die Schaltfläche **OK** drücken, um das Aufgaben-Fenster zu schließen.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/de
