# Sketcher SelectRedundantConstraints/ro
---
 GuiCommand:   Name: Sketcher SelectRedundantConstraints   Name/ro: Sketcher SelectRedundantConstraints   Workbenches: Sketcher Workbench/ro   Sketcher|MenuLocation: Sketch , Sketcher tools , Select Redundant Constraints   Shortcut: Shift+Ctrl+R   Version: 0.15---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Selectează constrângerile redundante dintr-o schiță.


</div>

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Redundant constraints: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the redundant constraints.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.




<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

1.  Intrați în modul edit al schiței.
2.  Alegeți traseul ** Sketch** → ** Sketcher tools** → **<img src="images/Sketcher_SelectRedundantConstraints.png" width=32px> Select Redundant Constraints** din meniul principal.
3.  Constrângerile redundante ale schiței vor fi selectate.


</div>

## Notes

-   Redundant constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/ro
