---
- GuiCommand:/pt
   Icon:Constraint Vertical.svg
   Name/pt:Vertical constraint
   Workbenches:[Sketcher](Sketcher_Workbench/pt.md)
   Shortcut:V
   MenuLocation:Sketch → Sketcher constraints → Constrain vertically
   SeeAlso:[Constraint Horizontal](Sketcher_ConstrainHorizontal/pt.md)
---


</div>

## Descrição

Creates a vertical constraint to the selected lines or polyline elements. As of <small>(v0.17)</small>  it can also constrain vertices vertically. More than one object can be selected.


<div class="mw-translate-fuzzy">

## Como usar {#como_usar}


</div>

1.  Select the lines or vertices to be constrained vertically
2.  To invoke the vertical constraint command:
    -   Press the **<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertical](Sketcher_ConstrainVertical.md)**.
    -   Use the **V** keyboard shortcut
    -   Use the {{MenuCommand|Sketch → Sketcher constraints → Constrain vertically}} entry in the Sketch dropdown menu
3.  Alternatively, the tool can be started without prior selection, and it will expect a selection; but only lines will be selectable.
4.  Right-click or press **Esc** once, to exit the tool.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}  

[Category:Sketcher/pt](Category:Sketcher/pt.md)
