---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/es: Croquizador RestringirBloque
   MenuLocation: Croquis , Restricciones de croquis , Restringir Bloque
   Workbenches: Sketcher Workbench/es
   SeeAlso: Sketcher_ConstrainLock/es
   Version: 0.17
---

# Sketcher ConstrainBlock/es


</div>



## Descripción

The <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> [Sketcher ConstrainBlock](Sketcher_ConstrainBlock.md) tool blocks edges in place with a single constraint. It is mainly intended for [B-splines](Sketcher_CreateBSpline.md), which can be difficult to fully constrain otherwise.

The block constraint only affects the freely movable parts of an edge. Blocked edges can have other constraints, and applying additional constraints to a blocked edge can modify it.




<div class="mw-translate-fuzzy">

## Utilización


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> [Constrain block](Sketcher_ConstrainBlock.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Constrain block** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Constrain block** option from the context menu.

    -   Use the keyboard shortcut: **K** then **B**.
3.  The cursor changes to a cross with the tool icon.
4.  Select a single edge.
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Select one or more edges.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> Constrain block** option from the context menu.
3.  Depending on the selection one or more constraints are added.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/es
