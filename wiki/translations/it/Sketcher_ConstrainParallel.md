# Sketcher ConstrainParallel/it
---
- GuiCommand:   Name:Sketcher ConstrainParallel   Name/it:Parallela   Icon:Constraint Parallel.svg   Workbenches:[MenuLocation:PartDesign - Schizzo - Parallela   Shortcut:**Shift** + **P**   SeeAlso:[[Sketcher ConstrainVertical/it|Verticale](Sketcher_Workbench/it___Schizzo]].md), [Orizzontale](Sketcher_ConstrainHorizontal/it.md)---


</div>

## Descrizione

Il vincolo Parallela costringe due linee rette o due bordi selezionati a essere paralleli tra loro.

## Utilizzo

Il disegno contiene due linee orientate in modo casuale.


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel1.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

Selezionare entrambe le linee facendo clic in successione su ciascuna di esse.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel2.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

Applicare il vincolo Parallela in uno di questi modi:

-   Cliccare sull\'icona <img alt="" src=images/Constraint_Parallel.png  style="width:16px;"> nella barra degli strumenti dei vincoli di Sketcher
-   Usare la scorciatoia da tastiera **Shift** + **P**.
-   Usare la voce **Sketch → Vincoli → Parallela** dal menu principale.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel3.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

**Risultato.** Le linee selezionate sono forzate ad essere parallele tra di loro. Ora, modificando l\'orientamento di una linea si cambia anche l\'orientamento dell\'altra allo stesso modo.


</div>

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1` and `Line2` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/it
