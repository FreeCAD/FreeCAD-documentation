---
 GuiCommand:
   Name/ru: Выделить конфликтующие ограничения
   Name: Sketcher_SelectConflictingConstraints
   MenuLocation: Sketch , Инструменты для эскиза , Выделить конфликтующие ограничения
   Workbenches: Sketcher_Workbench/ru
   Shortcut: Shift+Ctrl+E
   Version: 0.15
---

# Sketcher SelectConflictingConstraints/ru


</div>



## Описание

The <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:24px;"> [Sketcher SelectConflictingConstraints](Sketcher_SelectConflictingConstraints.md) tool selects the conflicting constraints in the sketch.

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Over-constrained: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the conflicting constraints.



## Применение

1.  There are several ways to invoke the tool:
    -   Click the underlined text in the Sketcher Dialog as described above.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_SelectConflictingConstraints.svg" width=16px> Select conflicting constraints** option from the menu.
    -   Use the keyboard shortcut: **Z** then **P**, then **C**.
2.  The conflicting constraints are selected.
3.  Optionally click in an empty area in the [3D view](3D_view.md) to clear the selection.

## Notes

-   Conflicting constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectConflictingConstraints/ru
