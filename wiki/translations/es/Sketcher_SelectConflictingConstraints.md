---
 GuiCommand:
   Name: Sketcher SelectConflictingConstraints
   Name/es: Corquizador SeleccionarRestriccionesConflictivas
   MenuLocation: Croquis , Corquizador Herramientas , Seleccionar Restricciones Conflictivas
   Workbenches: Sketcher Workbench/es
   Shortcut: Shift+Ctrl+E
   Version: 0.15
---

# Sketcher SelectConflictingConstraints/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Selecciona las restricciones conflictivas de un croquis.


</div>

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Over-constrained: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the conflicting constraints.



## Utilización


<div class="mw-translate-fuzzy">

1.  Entre en el modo de edición del croquis.
2.  Elige **Croquis → Croquizador Herramientas → [<img src=images/Sketcher_SelectConflictingConstraints.svg style="width:16px"> Seleccione Restricciones conflictivas** en el menú superior.
3.  Se seleccionarán las restricciones conflictivas del croquis.


</div>

## Notes

-   Conflicting constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectConflictingConstraints/es
