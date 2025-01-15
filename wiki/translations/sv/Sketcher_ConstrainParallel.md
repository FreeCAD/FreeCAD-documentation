---
 GuiCommand:
   Name: Constraint Parallel
   Name/sv: Constraint Parallel
   Workbenches: Sketcher Workbench/sv, PartDesign Workbench/sv
   MenuLocation: Sketch , Sketcher constraints , Constrain parallel
   SeeAlso: Sketcher_ConstrainVertical/sv, Sketcher_ConstrainHorizontal/sv
---

# Sketcher ConstrainParallel/sv


</div>

## Description

The <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Sketcher ConstrainParallel](Sketcher_ConstrainParallel.md) tool constrains lines to be parallel.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> [Constrain parallel](Sketcher_ConstrainParallel.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Constrain parallel** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Constrain parallel** option from the context menu.

    -   Use the keyboard shortcut: **P**.
3.  The cursor changes to a cross with the tool icon.
4.  Select two lines.
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Select two or more lines. <small>(v1.0)</small> : Points can be included in the selection, but will be ignored.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> Constrain parallel** option from the context menu.
3.  Depending on the selection one or more constraints are added.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1` and `Line2` and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/sv
