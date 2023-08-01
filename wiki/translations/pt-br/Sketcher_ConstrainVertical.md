---
- GuiCommand:/pt-br
   Icon:Constraint Vertical.svg
   Name/pt-br:Vertical constraint
   Workbenches:[Sketcher](Sketcher_Workbench/pt-br.md)
   Shortcut:V
   MenuLocation:Sketch → Sketcher constraints → Constrain vertically
   SeeAlso:[Constraint Horizontal](Sketcher_ConstrainHorizontal/pt-br.md)
---

# Sketcher ConstrainVertical/pt-br


</div>

## Descrição

Creates a vertical constraint to the selected lines or polyline elements. As of <small>(v0.17)</small>  it can also constrain vertices vertically. More than one object can be selected.


<div class="mw-translate-fuzzy">

## Como usar 


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
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/pt-br
