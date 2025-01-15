---
 GuiCommand:
   Name: Sketcher SelectElementsWithDoFs
   Name/es: Croquizador SeleccionarElementosConGdL 
   MenuLocation: Croquis , Croquizador Herramientas , Seleccionar GdL del solucionador
   Workbenches: Sketcher_Workbench/es
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta está pensada para ayudar a restringir completamente un croquis resaltando en verde los elementos del croquis con grados de libertad (GdL) (inglés: DoF Degrees of Freedom) restantes.


</div>

If such elements exist in a sketch the [Solver messages section of the Sketcher Dialog](Sketcher_Dialog#Solver_messages.md) displays this message:

-   Under constrained: n DoF(s)

Where *n* is the remaining number of degrees of freedom. Clicking the underlined text will select the under-constrained elements.

Please note that a sketch can also have redundant constraints if one of the other [solver messages](Sketcher_Dialog#Solver_messages.md) is displayed.



## Utilización

1.  There are several ways to invoke the tool:
    -   Click the underlined text in the Sketcher Dialog as described above.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_SelectElementsWithDoFs.svg" width=16px> Select unconstrained DoF** option from the menu.
    -   Use the keyboard shortcut: **Z** then **F**.
2.  The under-constrained sketch elements are selected.
3.  Optionally click in an empty area in the [3D view](3D_view.md) to clear the selection.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/es
