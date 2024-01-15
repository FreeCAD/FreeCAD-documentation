---
 GuiCommand:
   Name: FEM ElementFluid1D
   MenuLocation: Model , Element Geometry , Fluid section for 1D flow
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
---

# FEM ElementFluid1D/pt-br



## Descrição

Creates a FEM fluid section element for pneumatic and hydraulic networks



## Utilização

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementFluid1D.svg" width=16px> [Fluid section for 1D flow](FEM_ElementFluid1D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementFluid1D.svg" width=16px> Fluid section for 1D flow** option from the menu.
2.  Select Fluid type: Liquid, Gas or Open Channel
3.  Select Section type: Pipe Manning, Pipe Inlet etc.
4.  Enter Section type parameters.
5.  Select and add edge.



## Limitações

1.  The card only works with a 3 noded network element type. Information can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Notas

1.  An example of the set up of a hydraulic network can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  The \*FLUID SECTION card is used to model fluid elements for 1D flow. Information on the card can be found here: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/pt-br
