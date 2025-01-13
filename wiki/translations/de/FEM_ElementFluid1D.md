---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ElementFluid1D
   Name/de: FEM ElementFluid1D
   MenuLocation: Model , Element Geometry , Fluid section for 1D flow
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX
}}
---

# FEM ElementFluid1D/de



## Beschreibung

Erstellt einen FEM-Strömungsabschnitt für pneumatische oder hydraulische Anlagen, die mit CalculiX berechnet werden.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementFluid1D.svg" width=16px> [Fluid-Abschnitt für 1D-Strömung](FEM_ElementFluid1D/de.md)** drücken.
    -   Den Menüeintrag **Model → Element-Geometrie → <img src="images/FEM_ElementFluid1D.svg" width=16px> Fluid-Abschnitt für 1D-Strömung** auswählen.
2.  Art des Fluids auswählen: Flüssigkeit, Gas oder Open Channel (offenes Gerinne?)
3.  Art des Abschnitts auswählen: Pipe Manning, Einlassrohr usw.
4.  Parameter der Abschnittsarten eingeben.
5.  Eine Kante auswählen und hinzufügen.



## Einschränkungen

1.  The card only works with a 3 noded network element type. Information can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Hinweise

1.  An example of the set up of a hydraulic network can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  The [\*FLUID SECTION card](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html) is used to model fluid elements for 1D flow.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/de
