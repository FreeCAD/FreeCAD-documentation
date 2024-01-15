# Sketcher ConstrainHorizontal/it
---
 GuiCommand:   Name: Constraint Horizontal   Name/it: Vincolo orizzontale   Workbenches: Sketcher Workbench/it   Schizzo, PartDesign Workbench/it---


</div>



## Descrizione

Il vincolo Orizzontale impone a una o più linee selezionate nello schizzo di essere parallele all\'asse orizzontale del disegno.



## Utilizzo


<div class="mw-translate-fuzzy">

Selezionare una linea nello schizzo cliccando su di essa.

<img alt="" src=images/HorizontalConstraint1.png  style="width:256px;">

La linea assume il colore verde scuro.

<img alt="" src=images/HorizontalConstraint2.png  style="width:256px;">

Applicare il vincolo Orizzontale facendo clic sull\'icona vincolo orizzontale <img alt="" src=images/Constraint_Horizontal.svg  style="width:16px;"> nella barra degli strumenti vincoli di Schizzo oppure selezionando la voce nel menu orizzontale Vincoli di Schizzo nell\'ambiente Schizzo (o nel menu di Parte per l\'ambiente di lavoro Part Design).

<img alt="" src=images/HorizontalConstraint3.png  style="width:256px;">

La linea selezionata viene forzata parallela all\'asse orizzontale del disegno.

Si possono selezionare più linee,

<img alt="" src=images/HorizontalConstraint4.png  style="width:256px;">

a cui applicare lo stesso vincolo di prima,

<img alt="" src=images/HorizontalConstraint5.png  style="width:256px;">

e forzarle parallele all\'asse orizzontale dello schizzo.





</div>

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*The line turns dark green.*

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Apply the Horizontal Constraint by clicking on the **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Constraint horizontal](Sketcher_ConstrainHorizontal.md)* in the Sketcher Constraints toolbar or by selecting the Constrain horizontally menu item in the Sketcher constraints sub menu of the Sketch menu item in the Sketcher work bench (or the Part Design menu item of the Part Design work bench). The selected line is constrained to be parallel to the horizontal axis of the sketch.**

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Multiple lines may be selected*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*and then applying the constraint as described above, they are constrained to be parallel to the sketch horizontal axis.*

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/it
