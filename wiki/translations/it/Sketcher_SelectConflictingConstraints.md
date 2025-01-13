---
 GuiCommand:
   Name: Sketcher SelectConflictingConstraints
   Name/it: Seleziona i vincoli in conflitto
   MenuLocation: Schizzo , Strumenti , Seleziona i vincoli in conflitto
   Workbenches: Sketcher_Workbench/it
   Shortcut: **Z** **P** **C**
   Version: 0.15
---

# Sketcher SelectConflictingConstraints/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Seleziona i vincoli in conflitto di uno schizzo.


</div>

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Over-constrained: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the conflicting constraints.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Entrare in modalità di modifica del disegno.
2.  Selezionare dal menu in alto **Schizzo → Strumenti → [<img src=images/Sketcher_SelectConflictingConstraints.svg style="width:16px"> Seleziona i vincoli in conflitto**.
3.  Vengono selezionati i vincoli dello schizzo che sono in conflitto.


</div>

## Notes

-   Conflicting constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectConflictingConstraints/it
