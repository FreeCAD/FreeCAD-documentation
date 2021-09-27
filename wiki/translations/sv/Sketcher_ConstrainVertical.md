---
- GuiCommand:/sv
   Icon:Constraint Vertical.svg
   Name/sv:Vertical constraint
   Workbenches:[Sketcher](Sketcher_Workbench/sv.md)
   Shortcut:V
   MenuLocation:Sketch → Sketcher constraints → Constrain vertically
   SeeAlso:[Constraint Horizontal](Sketcher_ConstrainHorizontal/sv.md)
---

# Sketcher ConstrainVertical/sv


</div>

## Beskrivning

Creates a vertical constraint to the selected lines or polyline elements. As of <small>(v0.17)</small>  it can also constrain vertices vertically. More than one object can be selected.


<div class="mw-translate-fuzzy">

## Bruk


</div>

1.  Select the lines or vertices to be constrained vertically
2.  To invoke the vertical constraint command:
    -   Press the **<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertical](Sketcher_ConstrainVertical.md)**.
    -   Use the **V** keyboard shortcut
    -   Use the **Sketch → Sketcher constraints → Constrain vertically** entry in the Sketch dropdown menu
3.  Alternatively, the tool can be started without prior selection, and it will expect a selection; but only lines will be selectable.
4.  Right-click or press **Esc** once, to exit the tool.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}  

_

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/sv
