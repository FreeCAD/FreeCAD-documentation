---
 GuiCommand:
   Name: Sketcher SelectRedundantConstraints
   Name/es: Corquizador SeleccionarRestriccionesRedundantes
   Workbenches: Sketcher_Workbench/es
   MenuLocation: Croquis , Corquizador Herramientas , Seleccionar Restricciones Redundantes
   Shortcut: Shift+Ctrl+R
   Version: 0.15
---

# Sketcher SelectRedundantConstraints/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Selecciona las restricciones redundantes de un croquis.


</div>

If such constraints exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Redundant constraints: (#, #, #)

Where *(#, #, #)* are the indices of the constraints. Clicking the underlined text will select the redundant constraints.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.



## Utilización


<div class="mw-translate-fuzzy">

1.  Entre en el modo de edición del croquis.
2.  Elige **Croquis → Croquizador Herramientas → [<img src=images/Sketcher_SelectRedundantConstraints.svg style="width:16px"> Seleccione Restricciones redundantes** en el menú superior.
3.  Se seleccionarán las restricciones redundantes del croquis.


</div>

## Notes

-   Redundant constraints must be removed from the sketch.
-   Instead of the proposed indices it is also possible to delete other constraints.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/es
