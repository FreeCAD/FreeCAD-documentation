---
 GuiCommand:
   Name: Sketcher ConstrainHorizontal
   MenuLocation: Sketch , Sketcher constraints , Constrain horizontal
   Workbenches: Sketcher_Workbench
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainHorVer, Sketcher_ConstrainVertical
---

# Sketcher ConstrainHorizontal/en

## Description

The <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Sketcher ConstrainHorizontal](Sketcher_ConstrainHorizontal.md) tool constrains lines or pairs of points to be horizontal (parallel to the horizontal axis of the sketch).


<small>(v1.0)</small> 

: In most cases it is advisable to use the combined [Sketcher ConstrainHorVer](Sketcher_ConstrainHorVer.md) tool instead.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Auto tool for Horizontal/Vertical** [preference](Sketcher_Preferences#General.md) is selected (default): press the down arrow to the right of the **<img src="images/Sketcher_ConstrainHorVer.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Constrain horizontal** option from the dropdown.

    -   If this preference is not selected (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> [Constrain horizontal](Sketcher_ConstrainHorizontal.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Constrain horizontal** option from the menu.

    -   Use the keyboard shortcut: **H**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points.
    -   Select a single line.
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select two or more points.
    -   Select one or more lines. Points can be included in the selection, but will be ignored.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Constrain horizontal** option from the context menu.
3.  Depending on the selection one or more constraints are added.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/en
