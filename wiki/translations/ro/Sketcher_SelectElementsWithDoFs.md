---
- GuiCommand:/ro
   Name/ro:Sketcher Select solver DoFs
   Icon:Sketcher SelectElementsWithDoFs.svg
   MenuLocation:Sketch → Instrumente pentru schiţe → Select solver DoFs
   Workbenches:[Sketcher](Sketcher_Workbench/ro.md)
   Version:0.18
---

# Sketcher SelectElementsWithDoFs/ro


</div>



## Descriere

This tool is meant to aid in fully constraining a sketch by highlighting in green the sketch elements with remaining degrees of freedom (DoF).

## Usage

In the Solver messages box located at the top of the [Tasks tab](Task_panel.md), the following message(s) should be displayed:

-   In case of an **under-constrainend** sketch:

> Under-constrained sketch with X degrees of freedom

where \"X\" is the number of degrees of freedom remaining in the sketch; you will receive more information if you click on the blue link, or if you use the menu.

1.  The elements which have degrees of freedom are now highlighted in green.
2.  Click anywhere in the sketch to clear the highlight color.

-   In case of a **fully-constrainend** sketch:

> Fully constrained sketch 





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/ro
