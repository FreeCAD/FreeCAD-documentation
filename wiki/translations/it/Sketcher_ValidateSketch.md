---
 GuiCommand:
   Name: Sketcher_ValidateSketch
   Name/it: Convalida lo schizzo
   MenuLocation: Schizzo , Convalida lo schizzo...
   Workbenches: Sketcher_Workbench/it, PartDesign_Workbench/it
   SeeAlso: Sketcher_ConstrainCoincident/it, Topological_naming_problem/it
---

# Sketcher ValidateSketch/it



## Descrizione

L\'utilità **Convalida lo schizzo** può essere usata per analizzare e riparare uno schizzo che non è più modificabile o ha vincoli non validi, o per aggiungere [vincoli di coincidenza](Sketcher_ConstrainCoincident/it.md) a uno schizzo creato da una geometria importata come file DXF. Può anche essere utile individuare una coincidenza mancante in uno schizzo nativo che genera un errore \"can\'t validate broken face\" quando si tenta di applicare una funzione di PartDesign.

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*Il pannello delle attività di convalida dello Sketcher*



## Utilizzo

1.  Questo strumento non può essere utilizzato su uno schizzo in modalità modifica. Se necessario, uscire dalla modalità di modifica effettuando una delle seguenti operazioni:
    -   Premere il pulsante **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Esci](Sketcher_LeaveSketch/it.md)**.
    -   Premere il pulsante **Chiudi** nella parte superiore del [Scheda Azioni](Task_panel/it.md).
    -   Utilizzare la scorciatoia da tastiera: **Esc** (se abilitato in [Sketcher Preferenze](Sketcher_Preferences/it#Generale.md)).
2.  Selezionare lo schizzo da convalidare dalla [Vista ad albero](Tree_view/it.md) o facendo clic su uno dei suoi bordi nella [Vista 3D](3D_view/it.md).
3.  Per aprire l\'utilità di convalida dello schizzo, effettuare una delle seguenti operazioni:
    -   Selezionare l\'opzione **Schizzo → Convalida schizzo...** dal menu.
    -   Premere il pulsante **[<img src=images/Sketcher_ValidateSketch.svg style="width:16px"> [Convalida schizzo...](Sketcher_ValidateSketch/it.md)** (non disponibile in [PartDesign](PartDesign_Workbench/it.md)).
4.  Vedere le [Opzioni](#Opzioni.md) di seguito per le operazioni disponibili.
5.  Al termine, premere il pulsante **Chiudi**.



## Opzioni



### Coincidenze mancanti 

Trova coincidenze mancanti per i vertici sovrapposti e li aggiunge. Premere il pulsante **Trova**; appare una finestra di dialogo per segnalare quante coincidenze mancanti sono state trovate; sono mostrate nella vista 3D come croci gialle. Premere **OK** per chiudere la finestra di dialogo, quindi premere il pulsante **Ripara** per aggiungere le coincidenze mancanti.

Se necessario, definire un valore di tolleranza maggiore nel campo a discesa.

Premere **Evidenzia vertici problematici** per evidenziare i vertici che sono al di fuori di questa tolleranza.

Questa tolleranza viene utilizzata anche dal processo **Trova**/**Ripara**.

Lasciare selezionata la casella di controllo \"Ignora la geometria di costruzione\" per ignorare la geometria di costruzione nell\'analisi.



### Vincoli non validi 

Verifica la presenza di vincoli non validi.

Ad esempio, se è presente un vincolo Cerchio-Linea-Tangente, ma fa riferimento a due linee, viene considerato non valido.

(Ciò a volte accade a causa del [Problema di denominazione topologica](Topological_naming_problem/it.md), ovvero la geometria esterna cambia tipo).

Esegue anche altri controlli, ad esempio per i collegamenti vuoti.



### Geometria degenerata 

La geometria degenerata può derivare dalle azioni del risolutore in uno schizzo.

Ad esempio, se una linea viene costretta ad accorciarsi fino a diventare quasi un punto.

Altri esempi: una linea di lunghezza zero o un cerchio/arco con raggio zero.



### Geometria esterna invertita 

La geometria esterna invertita può verificarsi perché la gestione della geometria invertita è stata modificata all\'incirca con la revisione 0.15.

Questo processo potrebbe essere utile se gli schizzi con geometria esterna non vengono risolti a causa di queste modifiche.



### Vincolo orientamento bloccato 

Sono implementati i vincoli tangenti e perpendicolari (via-punto).

Internamente funzionano vincolando l\'angolo tra i vettori tangenti. Con il vincolo di tangenza, ad esempio, l\'angolo può essere 0 o 180 gradi (vettori co-diretti o opposti). L\'angolo effettivo viene ricordato nei dati del vincolo (\"l\'orientamento del vincolo è bloccato\") e impedisce il ribaltamento. Ma l\'angolo può essere cancellato (\"vincolo di sblocco orientamento\") o aggiornato; questi strumenti fanno esattamente questo.

Il meccanismo di blocco in genere funziona bene e questo strumento non dovrebbe essere necessario. **Dovrebbe essere utilizzato solo dopo aver effettuato il backup del documento aperto.**





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/it
