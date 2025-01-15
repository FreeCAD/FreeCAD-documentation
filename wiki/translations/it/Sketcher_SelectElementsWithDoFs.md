---
 GuiCommand:
   Name/it: Seleziona il Risolutore dei gradi di libertà
   Icon: Sketcher SelectElementsWithDoFs.svg
   MenuLocation: Sketch , Strumenti , Seleziona gli elementi con gradi di libertà
   Workbenches: Sketcher Workbench/it
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento ha lo scopo di aiutare a vincolare completamente uno schizzo evidenziando in verde gli elementi dello schizzo con residui gradi di libertà (DoF).


</div>

If such elements exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Under constrained: n DoF(s)

Where *n* is the remaining number of degrees of freedom. Clicking the underlined text will select the under-constrained elements.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.



## Utilizzo

1.  There are several ways to invoke the tool:
    -   Click the underlined text in the Sketcher Dialog as described above.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_SelectElementsWithDoFs.svg" width=16px> Select unconstrained DoF** option from the menu.
    -   Use the keyboard shortcut: **Z** then **F**.
2.  The under-constrained sketch elements are selected.
3.  Optionally click in an empty area in the [3D view](3D_view.md) to clear the selection.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/it
