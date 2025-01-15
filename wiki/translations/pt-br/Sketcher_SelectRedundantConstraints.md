---
 GuiCommand:
   Name: Sketcher SelectRedundantConstraints
   MenuLocation: Sketch , Sketcher visual , Select redundant constraints
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **P** **R**
   Version: 0.15
---

# Sketcher SelectRedundantConstraints/pt-br

## Description

The <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:24px;"> [Sketcher SelectRedundantConstraints](Sketcher_SelectRedundantConstraints.md) tool selects the redundant constraints in the sketch.

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Redundant constraints: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the redundant constraints.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.

## Usage

1.  There are several ways to invoke the tool:
    -   Click the underlined text in the Sketcher Dialog as described above.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_SelectRedundantConstraints.svg" width=16px> Select redundant constraints** option from the menu.
    -   Use the keyboard shortcut: **Z** then **P**, then **R**.
2.  The redundant constraints are selected.
3.  Optionally click in an empty area in the [3D view](3D_view.md) to clear the selection.

## Notes

-   Redundant constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/pt-br
