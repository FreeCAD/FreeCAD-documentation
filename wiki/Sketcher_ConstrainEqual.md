---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   MenuLocation: Sketch , Sketcher constraints , Constrain equal
   Workbenches: Sketcher_Workbench
   Shortcut: **E**
   SeeAlso: 
---

# Sketcher ConstrainEqual

## Description

The <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Sketcher ConstrainEqual](Sketcher_ConstrainEqual.md) tool constrains edges to have an equal length (lines) or curvature (other edges except [B-splines](Sketcher_CreateBSpline.md)). Selected edges must have the same type. Circles and circular arcs are of the same type (their radii are made equal), and so are ellipses and elliptical arcs (their major and minor radii are made equal).

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> [Constrain equal](Sketcher_ConstrainEqual.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Constrain equal** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Constrain equal** option from the context menu.

    -   Use the keyboard shortcut: **E**.
3.  The cursor changes to a cross with the tool icon.
4.  Select two edges of the same type.
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Select two or more edges of the same type.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> Constrain equal** option from the context menu.
3.  Depending on the selection one or more constraints are added.

## Scripting

 

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual
