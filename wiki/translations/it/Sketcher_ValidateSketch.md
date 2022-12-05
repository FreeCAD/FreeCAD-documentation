---
- GuiCommand:/it
   Name:Sketcher_ValidateSketch
   Name/it:Convalida lo schizzo
   Empty:1
   Workbenches:[Sketcher](Sketcher_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Sketch/Part Design → Convalida lo schizzo...
---

# Sketcher ValidateSketch/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

L\'utilità **Convalida lo schizzo** può essere usata per riparare uno schizzo che non è più modificabile, cha ha vincoli non validi, o per aggiungere [vincoli di coincidenza](Sketcher_ConstrainCoincident/it.md) a uno schizzo creato da una geometria importata come file DXF. Può anche essere utile individuare una coincidenza mancante in uno schizzo nativo che genera un errore \"can\'t validate broken face\" quando si tenta di applicare una funzione di PartDesign.


</div>

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*The Sketcher validation task panel*


<div class="mw-translate-fuzzy">

## Utilizzo


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare lo schizzo da convalidare, dall\'albero del modello o facendo clic su uno dei suoi bordi nella vista 3D. **Nota:** lo schizzo non deve essere in modalità di modifica. Se si è in modalità di modifica dello schizzo, è necessario [usire dallo schizzo](Sketcher_LeaveSketch/it.md).
2.  Aprire l\'utility di convalida dal menu Schizzo o Part Design.
3.  Selezionare le sottostanto opzioni per l\'operazione.
4.  Premere il pulsante **Chiudi** quando fatto.


</div>

## Opzioni

### Coincidenze mancanti 

Trova coincidenze mancanti per i vertici sovrapposti e li aggiunge. Premere il pulsante **Trova**; appare una finestra di dialogo per segnalare quante coincidenze mancanti sono state trovate; sono mostrate nella vista 3D come croci gialle. Premere **OK** per chiudere la finestra di dialogo, quindi premere il pulsante **Ripara** per aggiungere le coincidenze mancanti.

Se necessario, definire un valore di tolleranza maggiore nel campo a discesa.

Press **Highlight troublesome vertexes** to highlight vertexes that are outside this tolerance.

This tolerance is also used by the **Find**/**Fix** process.

Lasciare selezionata la casella di controllo \"Ignora la geometria di costruzione\" per ignorare la geometria di costruzione nell\'analisi.

### Invalid constraints 


<div class="mw-translate-fuzzy">

### Vincoli non validi 


</div>

For example, if there is a Circle-Line-Tangent constraint, but it references two lines, it is considered invalid.

(This sometimes happens due to the [Topological naming problem](Topological_naming_problem.md), i.e. the external geometry changes type).

It also does other checks, such as for empty links.

### Degenerated geometry 

Degenerated geometry can result from solver actions in a sketch.

For instance, if a line is forced to shorten to become almost a point.

Other examples: a zero length line or zero radius circle/arc.

### Reversed external geometry 


<div class="mw-translate-fuzzy">

### Geometria esterna reversa 


</div>

This process might be helpful if sketches with external-geometry fail to solve because of these changes.

### Constraint orientation locking 


<div class="mw-translate-fuzzy">

### Vincolo orientamento bloccato 


</div>

Internally they work by constraining the angle between tangent vectors. With tangent constraint for example, the angle can be 0 or 180 degrees (co-directed or opposed vectors). The actual angle is remembered in the constraint data (\"constraint orientation is locked\"), it guards against flipping. But the angle can be erased (\"constraint orientation unlock\") or updated; these tools do exactly that.

The locking mechanism typically works well and this tool should not be needed. **It should only used after making a backup of the open document.**





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/it
