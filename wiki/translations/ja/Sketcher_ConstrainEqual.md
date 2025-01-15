---
 GuiCommand:
   Name: Constraint EqualLength
   Name/ja: Constraint EqualLength
   Workbenches: Sketcher Workbench/ja, PartDesign Workbench/ja
   MenuLocation: Sketch , Sketcher constraints , Constrain equal
   SeeAlso: Constraint Radius/ja
---

# Sketcher ConstrainEqual/ja


</div>



## 説明


<div class="mw-translate-fuzzy">

ConstrainEqualはライン、ポリライン、長方形に含まれる複数の線分が等しい長さになるように拘束を行います。円弧や円に対して適用した場合はその半径が等しくなるように拘束を行います。異なるタイプの幾何プリミティブ間（例えば線分と円弧）に適用することはできません。


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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/ja
