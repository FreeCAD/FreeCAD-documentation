---
- GuiCommand:/cs
   Icon:Constraint Vertical.svg
   Name/cs:Constraint Vertical
   Workbenches:[Náčrt](Sketcher_Workbench/cs.md)
   Shortcut:V
   MenuLocation:Sketch → Sketcher constraints → Constrain vertically
   SeeAlso:[Vazba vodorovnosti](Sketcher_ConstrainHorizontal/cs.md)
---

# Sketcher ConstrainVertical/cs


</div>

## Popis


<div class="mw-translate-fuzzy">

Na vybrané přímce nebo lomené čáře vytvoří vazbu svislosti. Může být vybrán jeden nebo více objektů.


</div>


<div class="mw-translate-fuzzy">

## Použití


</div>

1.  Select the lines or vertices to be constrained vertically
2.  To invoke the vertical constraint command:
    -   Press the **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertical](Sketcher_ConstrainVertical.md)**.
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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/cs
