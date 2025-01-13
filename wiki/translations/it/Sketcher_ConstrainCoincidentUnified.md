---
 GuiCommand:
   Name: Sketcher ConstrainCoincidentUnified
   Name/it: Sketcher Vincolo coincidente 
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo coincidente
   Workbenches: Sketcher_Workbench/it
   Shortcut: **C**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainCoincident/it, Sketcher_ConstrainPointOnObject/it
---

# Sketcher ConstrainCoincidentUnified/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:24px;"> [Sketcher Vincolo coincidente (unificato)](Sketcher_ConstrainCoincidentUnified/it.md) crea un vincolo coincidente tra punti, fissa i punti sui bordi o sugli assi (le linee vengono quindi trattate come infinite e anche le curve aperte vengono virtualmente estese), oppure crea un vincolo concentrico tra cerchi, archi e/o ellissi (facendo coincidere i loro centri).

Questo strumento sostituisce gli strumenti [Sketcher Vincolo coincidente](Sketcher_ConstrainCoincident/it.md) e [Sketcher Vincolo punto sull\'oggetto](Sketcher_ConstrainPointOnObject/it.md) se l\'opzione **Unifica Coincidente e Punto su oggetto** è selezionata nelle [preferenze](Sketcher_Preferences/it#General.md).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> [Vincolo coincidente](Sketcher_ConstrainCoincidentUnified/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Vincolo coincidente** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Vincolo → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Vincolo coincidente** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **C**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due punti.
    -   Selezionare due bordi di cerchi, archi, ellissi o archi di ellissi.
    -   Selezionare un singolo punto e un singolo bordo (in qualsiasi ordine).
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare due o più punti.
    -   Selezionare due o più bordi di cerchi, archi, ellissi o archi di ellissi.
    -   Selezionare un singolo punto e un singolo bordo (in qualsiasi ordine).
    -   Selezionare più punti e un singolo bordo (idem).
    -   Selezionare un singolo punto e più bordi (idem).
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Vincolo coincidente** dal menu contestuale.
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Note

-    {{Version/it|1.0}}: I punti con vincoli coincidenti sono contrassegnati con i **Simboli di vincolo** [colore](Sketcher_Preferences/it#Display.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincidentUnified/it
