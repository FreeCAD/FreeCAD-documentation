---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   Name/it: Sketcher Vincolo coincidente
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo coincidente
   Workbenches: Sketcher_Workbench/it
   Shortcut: **C**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/it, Sketcher_ConstrainPointOnObject/it
---

# Sketcher ConstrainCoincident/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Sketcher Vincolo coincidente](Sketcher_ConstrainCoincident/it.md) crea un vincolo coincidente tra punti o ({{Version/it|0.21}}) un vincolo concentrico tra cerchi, archi e/o ellissi (facendo coincidere i loro centri).


{{Version/it|1.0}}

: questo strumento è sostituito dallo strumento [Sketcher Vincolo coincidente (unificato)](Sketcher_ConstrainCoincidentUnified/it.md) se l\'opzione **Unifica Coincidente e Punto su oggetto** è selezionata nelle [preferenze](Sketcher_Preferences/it#General.md).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainCoincident.svg" width=16px> [Vincolo coincidente](Sketcher_ConstrainCoincident/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainCoincident.svg" width=16px> Vincolo coincidente** dal menu.
    -   Usare la scorciatoia da tastiera: **C**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due punti.
    -   Selezionare due bordi di cerchi, archi, ellissi o archi di ellissi.
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare due o più punti.
    -   Selezionare due o più bordi di cerchi, archi, ellissi o archi di ellissi.
2.  Richiamare lo strumento come spiegato sopra.
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Note

-    {{Version/it|1.0}}: I punti con vincolo coincidente sono contrassegnati con i **Simboli di vincolo** [colore](Sketcher_Preferences/it#Display.md).



## Script

Il vincolo può essere creato da [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando il seguente comando:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

dove:

-    `Sketch`è un oggetto schizzo.

-    `LineFixed`è il numero della linea, che non deve muoversi applicando il vincolo.

-    `PointOfLineFixed`indica quale vertice di `LineFixed` deve soddisfare il vincolo

-    `LineMoving`è il numero della linea che si sposterà applicando il vincolo

-    `PointOfLineMoving`indica quale vertice di `LineMoving` deve soddisfare il vincolo

Come indicano i nomi `LineFixed` e `LineMoving`, se entrambi i vertici vincolati sono liberi di muoversi in qualsiasi direzione, il primo (il primo ad essere selezionato nella Gui) rimarrà fisso e l\'altro si muoverà. In presenza di vincoli esistenti, però, entrambi i bordi potrebbero spostarsi.

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `LineFixed`, `PointOfLineFixed`, `LineMoving` e `PointOfLineMoving`, e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/it
