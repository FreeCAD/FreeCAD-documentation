---
- GuiCommand:/it
   Name:Sketcher_ConstrainCoincident
   Name/it:Coincidenza
   Workbenches:[Schizzo](Sketcher_Workbench/it.md)
   Shortcut:**C**
   MenuLocation:Sketch → Vincoli → Coincidenza
   SeeAlso:[Blocca](Sketcher_ConstrainBlock/it.md), [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md)
---


</div>

## Descrizione

Crea un vincolo di Coincidenza di punti sull\'elemento selezionato

Questo strumento di vincolo richiede e accetta come argomento due punti e serve per rendere i due punti *coincidenti*. (Nel senso di trasformarli in un unico punto.)

Nella pratica è utile quando un profilo è interrotto - per esempio dove due punti di finelinea sono uno accanto all\'altro, ma le linee devono essere unite. In questo caso, un vincolo di coincidenza sui rispettivi punti finali chiude la breccia.

## Utilizzo


<div class="mw-translate-fuzzy">

Come detto in precedenza, questo strumento richiede due argomenti e entrambi devono essere dei punti.

1.  In primo luogo è necessario evidenziare due punti distinti. (Nota: lo strumento non funziona quando si tenta di selezionare il punto iniziale e quello finale della stessa linea).
2.  Per evidenziare un elemento del disegno, spostare il mouse sopra l\'oggetto e fare clic con il pulsante sinistro del mouse.
3.  Un elemento selezionato assume il colore verde. Il colore è modificabile da {{MenuCommand|Modifica → Preferenze → Visualizzazione → Colori → Selezione}}.
4.  Elementi successivi possono essere selezionati ripetendo la procedura precedente. NOTA: Non è necessario tenere premuto nessun tasto speciale, tipo **Ctrl**, per aggiungere elementi del disegno alla selezione multipla.
5.  Dopo aver evidenziato due punti, si può invocare il comando in uno di questi modi:
    -   Cliccare sull\'icona **<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> Coincidenza** della barra degli strumenti.
    -   Usare la scorciatoia da tastiera **C**.
    -   Usare la voce {{MenuCommand|Sketch → Vincoli → Coincidenza}} dal menu principale.


**Risultato:**

il comando fa sì che i due punti diventino \"coincidenti\" e vengano sostituiti da un singolo punto.


</div>

NOTA: Per rendere due punti coincidenti, FreeCAD deve necessariamente spostare uno o entrambi i punti originali.

## Alternatives to Coincident constraint {#alternatives_to_coincident_constraint}

The two constrained items of a [Coincident](Sketcher_ConstrainCoincident.md) constraint must be start point or end point vertices, or center points of arcs, circles or ellipses. Some combinations which are not possible with a coincident constraint can be emulated using other constraints:

-   The <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraint can be used to place a start point, end point or center point on the midpoint of a straight line.
-   A midpoint-to-midpoint placement of two straight lines can be achieved by creating a new <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Point](Sketcher_CreatePoint.md) and using two <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraints so that it lies on the midpoint of both lines.
-   A vertex can be constrained to lie along an edge using a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;">[PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint. Note that with this constraint, the point can lie anywhere on the full extension of a segment or curve (i.e. also before the start point or beyond the end point).
-   A collinear placement of two straight lines can be obtained by applying a <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Tangent](Sketcher_ConstrainTangent.md) constraint to them, or by combining a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint and a <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Parallel](Sketcher_ConstrainParallel.md) constraint.
-   Two edges can be made identical by using two <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident](Sketcher_ConstrainCoincident.md) constraints, one for each pair of extremities.
-   Two circles can be made identical by using a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident](Sketcher_ConstrainCoincident.md) constraint to merge the centers, and applying an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Equal](Sketcher_ConstrainEqual.md) constraint to their edges. For arcs, this will ensure both arcs are part of the same circle, while allowing them to have different start and end points.


<div class="mw-translate-fuzzy">

### Script generico {#script_generico}

Il vincolo può essere creato dalle macro e dalla console python utilizzando il seguente comando:


</div>

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```


<div class="mw-translate-fuzzy">

dove:

-    `Sketch`è un oggetto schizzo.

-    `LineFixed`è il numero della linea, che non deve muoversi applicando il vincolo.

-    `PointOfLineFixed`è il numero del vertice della linea `LineFixed` che deve soddisfare il vincolo.

-    `LineMoving`è il numero della linea che si sposterà applicando il vincolo.

-    `PointOfLineMoving`è il numero della linea `LineMoving` che deve soddisfare il vincolo.


</div>

As the names `LineFixed` and `LineMoving` indicate, if both constrained vertices are free to move in any direction, the first one (first to be selected in the Gui) will remain fixed and the other one will move. In the presence of existing constraints, however, both edges may move.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `LineFixed`, `PointOfLineFixed`, `LineMoving` and `PointOfLineMoving`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}  
