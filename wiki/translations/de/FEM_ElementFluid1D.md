---
- GuiCommand:/de
   Name:FEM ElementFluid1D
   Name/de:FEM ElementFluid1D
   MenuLocation:Model → Element Geometry → Fluid section for 1D flow
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Anleitung](FEM_tutorial/de.md)
---

# FEM ElementFluid1D/de



## Beschreibung

Erstellt einen FEM-Strömungsabschnitt für pneumatische oder Hydraulische Anlagen



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementFluid1D.svg" width=16px> [Fluid section for 1D flow](FEM_ElementFluid1D/de.md)** drücken.
    -   Den Menüeintrag **Model → Element-Geometrie → <img src="images/FEM_ElementFluid1D.svg" width=16px> Fluid section for 1D flow** auswählen.
2.  Select Fluid type: Liquid, Gas or Open Channel
3.  Select Section type: Pipe Manning, Pipe Inlet etc.
4.  Enter Section type parameters.
5.  Select and add edge.



## Einschränkungen

1.  The card only works with a 3 noded network element type. Information can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Hinweise

1.  An example of the set up of a hydraulic network can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  The \*FLUID SECTION card is used to model fluid elements for 1D flow. Information on the card can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/de
