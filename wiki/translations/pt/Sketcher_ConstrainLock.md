---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/pt: Sketcher ConstrainLock
   Workbenches: Sketcher Workbench/pt, PartDesign Workbench/pt
   MenuLocation: Sketch , Sketcher constraints , Constrain lock
   SeeAlso: Sketcher_ConstrainBlock
---

# Sketcher ConstrainLock/pt


</div>

## Description

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sketcher ConstrainLock](Sketcher_ConstrainLock.md) tool applies [Horizontal distance](Sketcher_ConstrainDistanceX.md) and [Vertical distance](Sketcher_ConstrainDistanceY.md) constraints to points. If a single point is selected the constraints reference the origin of the sketch. If two or more points are selected the constraints reference the last point in the selection.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainLock.svg" width=16px> [Constrain lock](Sketcher_ConstrainLock.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the context menu.

    -   Use the keyboard shortcut: **K** then **L**.
3.  The cursor changes to a cross with the tool icon.
4.  Select a single point.
5.  Two constraints are added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Select one or more points.
2.  Invoke the tool as explained above.
3.  Depending on the selection two or more constraints are added.

## Notes

-   There is no automatic prompt to edit the constraint values. If required values can be [edited manually](Sketcher_Workbench#Edit_constraints.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/pt
