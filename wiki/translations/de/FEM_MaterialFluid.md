---
 GuiCommand:
   Name: FEM MaterialFluid
   Name/de: FEM MaterialFluide
   MenuLocation: Modell , Materialien , Material für Fluide
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
---

# FEM MaterialFluid/de



## Beschreibung

Erstellt ein Material für Fluide.

![](images/FEMMaterialFluidProperties.png ) 
*Der Aufgabenbereich FEM-Material*



## Anwendung

1.  Um ein neues MaterialFluid-Objekt zu erstellen hat man folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/FEM_MaterialFluid.svg" width=16px> [Werkstoff für Fluide‏‎](FEM_MaterialFluid/de.md)** drücken.
    -   Den Menüeintrag **Modell → Werkstoffe → <img src="images/FEM_MaterialFluid.svg" width=16px> Werkstoff für Fluide‏‎** auswählen.
2.  Ein MaterialFluid-Objekt bearbeiten:
    -   Mit Doppelklick in der [Baumansicht](Tree_view/de.md) auswählen.
3.  Der Aufgabenbereich FEM-Material wird geöffnet.
4.  Eine Fluidart auswählen. Übliche Arten für Computational Fluid Dynamics (CFD) sind **Air** (Luft) oder **Water** (Wasser).
5.  Davon ausgehend, dass das Fluid auf das ganze Objekt angewendet wird, werden keine geometrischen Elemente ausgewählt (die Referenfliste bleibt leer). Das Fluid wird auf das ganze Objekt angewendet. Andernfalls wird das Fluid bestimmten Bereichen des Modells von Hand zugeordnet, indem für jeden eingefügten Werkstoff einige ausgewählt werden; dabei sollte kein Bereich ohne ein zugeordnetes Fluid bleiben.
6.  Fluid-Eigenshaften wie Dichte, kinematische Viskosität, Wärmeleitfähigkeit usw. können angepasst werden. Einige Haupt-Fluide sind schon in der Liste vorhanden und brauchen keine Anpassung.
7.  Anpassungen können als benutzerdefinierter Werkstoff gespeichert werden.
8.  Die Schaltfläche **OK** drücken, um den Aufgabenbereich zu schließen.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/de
