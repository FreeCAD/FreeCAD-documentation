---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch , Sketcher constraints , Constrain equal
   Shortcut: E
   SeeAlso: Sketcher_ConstrainRadius
---

# Sketcher ConstrainEqual/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

**Constrângerea de egalitate** forțează două sau mai multe segmente de linie, o poli-linie sau un dreptunghi să aibă o lungime egală. Dacă se aplică la arce sau cercuri, razele sunt constrânse să fie egale. Nu poate fi aplicată primitivelor geometrice care nu sunt de același tip (de exemplu, segmente de linie și arcuri de cerc).


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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/ro
