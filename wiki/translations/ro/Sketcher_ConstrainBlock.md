---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/ro: Constrângere de blocare
   Workbenches: Sketcher Workbench/ro
   MenuLocation: Sketch , Constrângeri desenator , Constrain Block
   SeeAlso: Sketcher_ConstrainLock/ro
---

# Sketcher ConstrainBlock/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

**Constrain Block** permite blocarea unui element geometric pe loc cu ajutorul unei singure constrângeri. Scopul său principal este de a lucra cu [B-Splines](Sketcher_CreateBSpline.md) ceea ce poate fi dificil de restrâns complet în alt mod.


</div>

The block constraint only affects the freely movable parts of an edge. Blocked edges can have other constraints, and applying additional constraints to a blocked edge can modify it.




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

1.  Selectează un element de constrângere;
2.  Apăsă butonul **[<img src=images/Sketcher_ConstrainBlock.png style="width:24px"> '''Constrain Block'''** .

**Note:** pașii 1 și 2 pot fi inversați.


</div>

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





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/ro
