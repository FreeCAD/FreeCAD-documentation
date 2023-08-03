---
 GuiCommand:
   Icon: Constraint Vertical.svg
   Name/es: Restricción de verticalidad
   Workbenches: Sketcher Workbench/es
   Shortcut: V
   MenuLocation: Sketch , Restricciones de croquis , Restricción de verticalidad
   SeeAlso: Sketcher_ConstrainHorizontal/es
---

# Sketcher ConstrainVertical/es


</div>

## Descripción

Creates a vertical constraint to the selected lines or polyline elements. As of <small>(v0.17)</small>  it can also constrain vertices vertically. More than one object can be selected.


<div class="mw-translate-fuzzy">

## Utilización


</div>

1.  Select the lines or vertices to be constrained vertically
2.  To invoke the vertical constraint command:
    -   Press the **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertically](Sketcher_ConstrainVertical.md)** button.
    -   Use the **V** keyboard shortcut
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> Constrain vertically** entry in the Sketch dropdown menu
3.  Alternatively, the tool can be started without prior selection, and it will expect a selection.
4.  Right-click or press **Esc** once, to exit the tool.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/es
