---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   Name: Sketcher Vincolo punto su oggetto
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo punto su oggetto
   Workbenches: Sketcher_Workbench/it
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/it, Sketcher_ConstrainCoincident/it
---

# Sketcher ConstrainPointOnObject/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Sketcher Vincolo punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) fissa i punti sui bordi o sugli assi. Le linee vengono trattate come infinite e anche le curve aperte vengono virtualmente estese.


{{Version/it|1.0}}

: questo strumento è sostituito dallo strumento [Sketcher Vincolo coincidente (unificato)](Sketcher_ConstrainCoincidentUnified/it.md) se l\'opzione **Unifica Coincidente e Punto su oggetto** è selezionata nelle [preferenze](Sketcher_Preferences/it#General.md).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> [Vincolo punto su oggetto](Sketcher_ConstrainPointOnObject/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Vincolo punto su oggetto** dal menu.
    -   Usare la scorciatoia da tastiera: **O**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Selezionare un singolo punto e un singolo bordo (in qualsiasi ordine).
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare un singolo punto e un singolo bordo (in qualsiasi ordine).
    -   Selezionare più punti e un singolo bordo (idem).
    -   Selezionare un singolo punto e più bordi (idem).
2.  Richiamare lo strumento come spiegato sopra.
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Script

Il vincolo può essere creato da [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando il seguente comando:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`è un oggetto schizzo.

-    `LineMoving`è il numero che indica la linea che contiene il punto che deve essere spostato sul `LineFixed` (la linea che rimane fissa).

-    `PointOfLineMoving`è il numero del vertice della linea `LineMoving` che deve essere spostato sulla `LineFixed`.

-    `LinedFixed`è il numero della linea su cui apporre il punto `PointOfLineMoving`.

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega come identificare i numeri che designano linee e punti.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/it
