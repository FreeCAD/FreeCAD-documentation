---
- GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   Name/it: Punto su oggettto
   Icon: Constraint_PointOnObject.svg
   Workbenches: [Schizzo](Sketcher_Workbench/it.md)
   MenuLocation: PartDesign - Schizzo - Punto su oggetto
   Shortcut: **Maiusc** + **O**
   SeeAlso: [Coincidenza](Sketcher_ConstrainCoincident/it.md)
---

# Sketcher ConstrainPointOnObject/it


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Appone un punto su un altro oggetto, ad esempio, su una linea, un arco o un asse dello schizzo.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare il punto che si desidera apporre su una linea o arco, etc. (il punto selezionato diventa verde).
2.  Selezionare la linea su cui si desidera apporre il punto appena selezionato (la linea selezionata diventa verde).
3.  Invocare il vincolo in uno di questi modi:
    -   Cliccare sull\'icona **[<img src=images/Constraint_PointOnObject.svg style="width:24px">** della barra degli strumenti.
    -   Usare la scorciatoia da tastiera **Maiusc** + **O**.
    -   Usare la voce **Sketch → Vincoli → Punto su oggetto** dal menu principale.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script

Il vincolo può essere creato con una macro e dalla console Python utilizzando il seguente comando:


</div>


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`è un oggetto schizzo.

-    `LineMoving`è il numero che indica la linea che contiene il punto che deve essere spostato sul `LineFixed` (la linea che rimane fissa).

-    `PointOfLineMoving`è il numero del vertice della linea `LineMoving` che deve essere spostato sulla `LineFixed`.

-    `LinedFixed`è il numero della linea su cui apporre il punto `PointOfLineMoving`.


<div class="mw-translate-fuzzy">

Per identificare il numero che indica le linee ed i punti si prega di fare riferimento alla parte di scripting del [vincolo coincidenza](Sketcher_ConstrainCoincident/it#Script.md).


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/it
