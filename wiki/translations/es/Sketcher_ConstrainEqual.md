---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   Name/es: Croquizador RestringirIgual
   Workbenches: Sketcher Workbench/es
   MenuLocation: Croquis , Croquizador Restricciones , Restringir igual
   Shortcut: E
   SeeAlso: Sketcher_ConstrainRadius/es
---

# Sketcher ConstrainEqual/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La restricción Igual fuerza que dos o más segmentos de línea en una línea, polilínea o rectángulo tengan la misma longitud. Si se aplica sobre arcos o circunferencias el radio se restringe para que sea igual. No puede aplicarse sobre geometría que no sea del mismo tipo (por ejemplo segmentos de línea y arcos).


</div>

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


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/es
