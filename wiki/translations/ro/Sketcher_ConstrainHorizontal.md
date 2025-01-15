---
 GuiCommand:
   Name: Constraint Horizontal
   Name/ro: Constraint Horizontal
   Workbenches: Sketcher Workbench/ro
   Shortcut: H
   MenuLocation: Sketch , Sketcher constraints , Constrain horizontally
   SeeAlso: Sketcher ConstrainVertical/ro
---

# Sketcher ConstrainHorizontal/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

**Constrângerea orizontală** forțează o linie din schiță să fie paralelă cu axa orizontală a schiței.


</div>


<small>(v1.0)</small> 

: In most cases it is advisable to use the combined [Sketcher ConstrainHorVer](Sketcher_ConstrainHorVer.md) tool instead.




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint1.png  style="width:256px;"> Selectați linia făcând click pe ea.
<img alt="" src=images/HorizontalConstraint2.png  style="width:256px;"> Linia își schimbă culaorea în verde închis.
<img alt="" src=images/HorizontalConstraint3.png  style="width:256px;"> Apply the Horizontal Constraint by clicking on the Horizontal Constraint icon <img alt="" src=images/Constraint_Horizontal.png  style="width:16px;"> în bara de instrumente Sketcher Constructors sau selectând elementul de meniu Sketcher Constructors din Atelierul Sketcher (sau elementul de design al piesei de proiectare a bancului de lucru Part Design). Linia selectată este constrânsă să fie paralelă cu axa orizontală a schiței.
<img alt="" src=images/HorizontalConstraint4.png  style="width:256px;"> Multiple linii pot fi selectate,
<img alt="" src=images/HorizontalConstraint5.png  style="width:256px;"> și apoi aplicarea constrângerii așa cum este descrisă mai sus, ele sunt constrânse să fie paralele cu axa orizontală.


</div>

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


<div class="mw-translate-fuzzy">


</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/ro
