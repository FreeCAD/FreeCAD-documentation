---
 GuiCommand:
   Name/ro: Sketcher Select solver DoFs
   Icon: Sketcher SelectElementsWithDoFs.svg
   MenuLocation: Sketch , Instrumente pentru schiţe , Select solver DoFs
   Workbenches: Sketcher Workbench/ro
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/ro


</div>



## Descriere

The <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:24px;"> [Sketcher SelectElementsWithDoFs](Sketcher_SelectElementsWithDoFs.md) tool selects the not fully constrained elements in the sketch.

If such elements exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Under constrained: n DoF(s)

Where *n* is the remaining number of degrees of freedom. Clicking the underlined text will select the under-constrained elements.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.

## Usage

1.  There are several ways to invoke the tool:
    -   Click the underlined text in the Sketcher Dialog as described above.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_SelectElementsWithDoFs.svg" width=16px> Select unconstrained DoF** option from the menu.
    -   Use the keyboard shortcut: **Z** then **F**.
2.  The under-constrained sketch elements are selected.
3.  Optionally click in an empty area in the [3D view](3D_view.md) to clear the selection.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/ro
