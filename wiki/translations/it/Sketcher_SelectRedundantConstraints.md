# Sketcher SelectRedundantConstraints/it
---
 GuiCommand:   Name: Sketcher SelectRedundantConstraints   Name/it: Seleziona i vincoli ridondanti   Workbenches: Sketcher Workbench/it   Sketcher|MenuLocation: Sketch , Strumenti , Seleziona i vincoli ridondanti   Shortcut: Shift+Ctrl+R   Version: 0.15---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Seleziona i vincoli ridondanti di uno schizzo.


</div>

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Redundant constraints: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the redundant constraints.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Entrare in modalità di modifica del disegno.
2.  Scegliere ** Sketch** → ** Strumenti** → **<img src="images/Sketcher_SelectRedundantConstraints.png" width=24px> Seleziona i vincoli ridondanti** dal menu in alto.
3.  Vengono selezionati i vincoli che nello schizzo sono ridondanti.


</div>

## Notes

-   Redundant constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/it
