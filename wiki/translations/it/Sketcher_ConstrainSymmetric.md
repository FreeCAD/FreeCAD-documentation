# Sketcher ConstrainSymmetric/it
---
- GuiCommand:   Name: Sketcher ConstrainSymmetric   Name/it: Simmetria   Workbenches: Sketcher Workbench/it   Schizzo---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il vincolo Simmetria forza due punti selezionati ad essere simmetrici rispetto ad una data linea. Entrambi i punti selezionati sono vincolati a giacere sulla normale alla linea di simmetria attraverso gli stessi due punti e sono vincolati equidistanti dalla linea.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

<img alt="" src=images/SymmetricConstraint1.png  style="width:256px;">


</div>

Selezionare due punti (vertici) e una linea nello schizzo. La linea e i punti selezionati assumono il colore verde scuro.


<div class="mw-translate-fuzzy">

<img alt="" src=images/SymmetricConstraint2.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

Fare clic sull\'icona <img alt="" src=images/Constraint_Symmetric.png  style="width:16px;"> nella barra degli strumenti di vincolo o selezionare il Vincolo Simmetria dal sottomenu dell\'ambiente Schizzo (o quello dell\'ambiente PartDesign).


</div>

Questo applica il vincolo agli elementi selezionati.


<div class="mw-translate-fuzzy">

<img alt="" src=images/SymmetricConstraint3.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">


**Note:**

se si desidera definire un vincolo di simmetria rispetto a un punto, l\'ordine della selezione è importante, a seconda che si selezioni lo strumento all\'inizio o alla fine.

-   Se si fa prima clic sullo strumento: selezionare il primo punto, quindi il punto di riferimento di simmetria e infine il secondo punto.
-   Se si fa clic sullo strumento alla fine: selezionare il primo punto, quindi il secondo punto e infine il punto di riferimento di simmetria.


</div>

Vedere il tracker [issue #4144](https://freecadweb.org/tracker/view.php?id=4144), e la [discussione nel forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=39611).

## Scripting

Two points and a symmetry line:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Two points and a symmetry point:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

A line and a symmetry point (In the GUI one can select a line and a point, but it uses internally the same form as above, with the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` and `PointOfLineS`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/it
