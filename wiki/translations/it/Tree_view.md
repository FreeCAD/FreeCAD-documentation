# Tree view/it
## Introduzione

La [vista ad albero](Tree_view/it.md) appare nella scheda **Modello** della [vista combinata](Combo_view/it.md), uno dei pannelli più importanti dell\'[interfaccia](Interface/it.md); mostra tutti gli oggetti definiti dall\'utente che fanno parte di un documento di FreeCAD. La vista ad albero è una rappresentazione della [struttura del documento](document_structure/it.md) e indica quali informazioni vengono salvate sul disco.

Questi oggetti non devono necessariamente essere forme geometriche visibili nella [vista 3D](3D_view/it.md), ma possono anche oggetti dati di supporto creati con qualsiasi [ambiente](Workbenches/it.md).

![](images/FreeCAD_Tree_view.png )



*La vista ad albero che mostra vari elementi nel documento.*



## Lavorare con la vista ad albero 

Per impostazione predefinita, ogni volta che viene creato un nuovo oggetto, questo viene aggiunto alla fine dell\'elenco nella vista ad albero. La vista ad albero consente di gestire gli oggetti per mantenerli organizzati; consente di creare dei [gruppi](Std_Group/it.md), spostare gli oggetti all\'interno dei gruppi, spostare dei gruppi all\'interno di altri gruppi, etichettare oggetti, copiare oggetti, eliminare oggetti e altre operazioni del menu contestuale (clic destro) che dipendono dall\'oggetto attualmente selezionato e dall\'ambiente di lavoro attualmente attivo.

Molte operazioni creano oggetti che dipendono da un oggetto precedentemente esistente. In questo caso, la vista ad albero mostra questa relazione assorbendo l\'oggetto più vecchio all\'interno del nuovo oggetto. L\'espansione e la compressione degli oggetti nella vista ad albero mostra la cronologia parametrica di quell\'oggetto. Gli oggetti più profondi all\'interno degli altri sono quelli più vecchi, mentre gli oggetti all\'esterno sono i più recenti e sono derivati dagli oggetti più vecchi. Modificando gli oggetti interni, le operazioni parametriche si propagano fino in cima, generando un nuovo risultato.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history.png  style="width:" height="300px;">



*L'oggetto di livello più alto viene creato eseguendo operazioni parametriche su oggetti che sono stati creati da operazioni precedenti.<br>L'espansione completa dell'albero rivela gli elementi originali utilizzati per creare i solidi intermedi.*



### Colonne della vista ad albero 

Per impostazione predefinita, la visualizzazione ad albero mostra solo una singola colonna con le etichette e le icone degli oggetti. Facoltativamente è possibile visualizzare anche una seconda colonna con le descrizioni ed inoltre possono venire aggiunte anche le intestazioni delle colonne.

Per abilitare la colonna della descrizione fare clic con il tasto destro del mouse sulla Vista combinata e nel menu contestuale selezionare:
**Impostazioni albero → Mostra colonna descrizione** {{Version/it|0.21}}



### Modificare l\'etichetta dell\'oggetto 

Seleziona un oggetto nella prima colonna e premi **F2** (su Windows e Linux), o **Invio** (su macOS), per modificare la sua proprietà **Label**. Questa proprietà può anche essere modificata tramite l\'azione del menu contestuale descritta di seguito o nell\'[Editor proprietà](Property_editor/it.md).



### Modificare la descrizione dell\'oggetto 

Un oggetto può facoltativamente avere una descrizione. Questa informazione è archiviata nella relativa proprietà **Label2**. Se viene visualizzata la colonna della descrizione, puoi modificare questa proprietà selezionando un oggetto in quella colonna e premendo **F2** (su Windows e Linux) o **Invio** (su macOS). La proprietà può anche essere modificata nell\'[Editor delle proprietà](Property_editor/it.md).



## Azioni

Poiché la vista ad albero elenca oggetti che possono essere visibili nella [vista 3D](3D_view/it.md), molte delle azioni sono uguali a quelle che possono essere eseguite nella [vista 3D](3D_view/it.md). Le azioni possono essere avviate da un **Menu contestuale** a cui è possibile accedere facendo clic con il pulsante destro del mouse sullo sfondo o su un oggetto.



### Avvio dell\'applicazione 

All\'avvio dell\'applicazione, per impostazione predefinita è attivo l\'ambiente [Start](Start_Workbench/it.md) e non viene stato creato alcun documento, il menu contestuale della [vista ad albero](Tree_view.md) ha una sola voce:

-    **Azioni rapide**. Posizionandosi sopra il cursore si apre un sottomenù contenente quattro comandi:

    -   [Copia la selezione](Std_Expressions/it.md)
    -   [Copia il documento attivo](Std_Expressions/it.md)
    -   [Copia tutti i documenti](Std_Expressions/it.md)
    -   [Incolla](Std_Paste/it.md)

Questi comandi consentono di lavorare con vari documenti, ma sono disabilitati se non è presente alcun documento.



### Nuovo documento 

Una volta creato un nuovo documento, facendo clic con il pulsante destro del mouse sullo sfondo si apre il menu contestuale che ora contiene due voci:

-    **Azioni rapide**come indicato sopra, ma con queste due voci attivate:

    -   [Copia il documento attivo](Std_Expressions/it.md)
    -   [Copia tutti i documenti](Std_Expressions/it.md)

-    **Azioni link**\- un sottomenu con due voci:

    -   
        **Crea un gruppo di link**
        
        \- un altro sottomenu contenente tre comandi:

        -   [Gruppo semplice](Std_LinkMakeGroup/it.md)
        -   [Gruppo con links](Std_LinkMakeGroup/it.md)
        -   [Gruppo con link di trasformazione](Std_LinkMakeGroup/it.md)

    -   [Crea un link](Std_LinkMake/it.md)



### Selezione del documento 

Se si seleziona il documento e si fa clic con il pulsante destro del mouse, oltre ad **Azioni rapide** e **Azioni link**, il menu contestuale conterrà i seguenti comandi:

-    **Mostra gli elementi nascosti nella vista ad albero**: se attivo, la vista ad albero mostra gli oggetti nascosti.

-    **Cerca**: mostra un campo di input per cercare oggetti all\'interno del documento selezionato.

-    **Chiudi il documento**: chiude il documento selezionato.

-    **Aggiungi oggetti dipendenti alla selezione**: tutti gli oggetti dipendenti verranno aggiunti alla selezione. In questo modo si possono vedere le dipendenze e ad es. eliminare tutti gli oggetti dipendenti contemporaneamente. Disponibile solo per oggetti con collegamenti e per documenti.

-    **Salta il ricalcolo**: se attivo, gli oggetti del documento non verranno [ricalcolati](Std_Refresh/it.md) automaticamente.

-    **Consenti i ricalcoli parziali**: se attivo, il documento consentirà il [ricalcolo](Std_Refresh/it.md) solo di alcuni oggetti. Disponibile solo se è attivato **Salta il ricalcolo**.

-    **Segna da ricalcolare**: contrassegna tutti gli oggetti del documento come selezionati e pronti per [ricalcolo](Std_Refresh/it.md).

-    **[Crea gruppo](Std_Group.md)**: crea un [gruppo](Std_Group/it.md) nel documento selezionato.



### Selezione degli oggetti 

Una volta aggiunti gli oggetti al documento, facendo clic con il pulsante destro del mouse su di essi verranno visualizzati comandi aggiuntivi. Questi dipendono dal numero di oggetti selezionati, dal loro tipo e anche dall\'ambiente attivo. Nella maggior parte dei casi e con la maggior parte degli ambienti di lavoro (eccetto l\'[Ambiente Start](Start_Workbench/it.md)) sono disponibili i seguenti comandi:

-    **[Aspetto](Std_SetAppearance/it.md)**: avvia una finestra di dialogo per modificare le proprietà visive dell\'intero oggetto.

-    **[Colore casuale](Std_RandomColor/it.md)**: assegna un colore casuale all\'oggetto.

-    **[Taglia](Std_Cut/it.md)**: disattivo.

-    **[Copia](Std_Copy/it.md)**: copia un oggetto in memoria.

-    **[Incolla](Std_Paste/it.md)**: incolla l\'oggetto copiato nel documento; la copia viene aggiunta alla fine della visualizzazione ad albero.

-    **[Elimina](Std_Delete/it.md)**: rimuove l\'oggetto dal documento.

-    **[Mostra/Nascondi](#Simbolo_dell'occhio.md)**: attiva/disattiva la visibilità degli oggetti nella vista ad albero .

-    **Segna da ricalcolare**: contrassegna l\'oggetto selezionato come pronto per il [ricalcolo](Std_Refresh/it.md).

-    **Ricalcola l'oggetto**: ricalcola l\'oggetto selezionato.

-    **Rinomina**: modifica l\'etichetta dell\'oggetto selezionato, ma non il nome, che è di sola lettura. Questa opzione è disponibile solo se è stato selezionato un singolo oggetto.

Come esempio di estensione del menu contestuale, se si fa clic con il tasto destro del mouse su un [Cubo di Part](Part_Box/it.md) mentre l\'[Ambiente Part](Part_Workbench/it.md) è attivo, sono disponibili i seguenti comandi aggiuntivi:

-    **[Edita](Std_Edit/it.md)**: attiva la modalità di modifica dell\'oggetto.

-    **[Transforma](Std_TransformManip/it.md)**: avvia il widget di trasformazione per spostare o ruotare l\'oggetto.

-    **[Editor allegato](Part_EditAttachment/it.md)**: avvia una finestra di dialogo per collegare l\'oggetto a uno o più altri oggetti.

-    **[Imposta i colori](Part_FaceColors/it.md)**: imposta il colore delle facce selezionate dell\'oggetto.

-    **[Mostra/Nascondi](Std_ToggleVisibility/it.md)**: rende l\'oggetto visibile o invisibile nella [vista 3D](3D_view/it.md).

-    **[Mostra la selezione](Std_ShowSelection/it.md)**: rende visibile l\'oggetto selezionato.

-    **[Nascondi la selezione](Std_HideSelection/it.md)**: rende invisibile l\'oggetto selezionato.

-    **[Commuta la selezionabilità](Std_ToggleSelectability/it.md)**: attiva/disattiva la selezionabilità dell\'oggetto nella [vista 3D](3D_view/it.md).

-    **[Seleziona tutte le istanze](Std_TreeSelectAllInstances/it.md)**: seleziona tutte le istanze di questo oggetto nella vista ad albero.

-    **[Invia alla Console Python](Std_SendToPythonConsole/it.md)**: crea una variabile nella [Console Python](Python_console/it.md) che fa riferimento all\'oggetto.



### Comandi da tastiera 

Le seguenti azioni da tastiera sono disponibili quando è stata attivata la visualizzazione ad albero:

-    **Ctrl**\+**F**: apre una casella di ricerca nella parte inferiore dell\'albero, che consente di cercare e raggiungere gli oggetti utilizzando i loro nomi o etichette.

-   Azioni di espansione e compressione utilizzando le combinazioni **Alt**+**Freccia**: {{Version/it|0.20}}
    -   
        **Alt**
        
        \+**Sinistra**: comprime gli elementi selezionati.

    -   
        **Alt**
        
        \+**Destra**: espande gli elementi selezionati.

    -   
        **Alt**
        
        \+**Su**: espande gli elementi selezionati con tutti i relativi figli di livello 1 compressi (i figli più profondi rimangono invariati).

    -   
        **Alt**
        
        \+**Giù**: espande gli elementi selezionati con tutti i loro figli di livello 1 espansi (i figli più profondi rimangono invariati).



## Icone sovrapposte 

Una o più icone sovrapposte più piccole possono essere visualizzate sopra l\'icona predefinita di un oggetto nella visualizzazione ad albero. Le icone sovrapposte disponibili e il loro significato sono elencati di seguito.



### ![](images/FreeCAD_Tree_view_recompute.png ) Segno di spunta bianco su sfondo blu 

Indica che l\'oggetto deve essere [ricalcolato](Std_Refresh/it.md), a causa delle modifiche apportate al modello o perché l\'utente ha contrassegnato l\'oggetto nel menu contestuale della vista ad albero da ricalcolare. Nella maggior parte dei casi i ricalcoli vengono avviati automaticamente, ma a volte vengono ritardati per motivi di prestazioni.



### ![](images/FreeCAD_Tree_view_tip.png ) Freccia bianca su sfondo verde 

Indica il cosiddetto [Tip](PartDesign_Body/it#Tip.md) di un corpo. Di solito è l\'ultima caratteristica in un [Body di PartDesign](PartDesign_Body/it.md) e rappresenta l\'intero corpo nel mondo esterno al corpo, ad es. quando il corpo viene esportato o utilizzato nelle operazioni [booleane](Part_Boolean/it.md). La punta può essere modificata dall\'utente.



### ![](images/FreeCAD_Tree_view_unattached.png ) Catena di collegamento viola su sfondo bianco 

Viene tipicamente mostrato per [schizzi](Sketch/it.md), primitive geometriche, come cubo, cilindro, ecc. e geometria [Datum](Datum/it.md). Indica che l\'oggetto non è collegato a nulla. Non ha offset di allegato e ottiene la sua posizione e il suo allineamento esclusivamente dalla sua proprietà [Posizionamento](Placement/it.md).

C\'è un [Tutorial di base sugli allegati](Basic_Attachment_Tutorial/it.md) che spiega come gestire tali oggetti.



### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) X Gialla 

Viene utilizzato solo per [schizzi](Sketch/it.md) e indica che lo schizzo non è completamente vincolato. All\'interno di [Sketcher](Sketcher_Workbench/it.md) il numero di gradi di libertà rimanenti viene mostrato nei messaggi del risolutore.



### ![](images/FreeCAD_Tree_view_error.png ) Punto esclamativo bianco su sfondo rosso 

Indica che l\'oggetto presenta un errore che deve essere corretto. Dopo aver ricalcolato l\'intero documento, quando si passa il mouse sull\'oggetto nella visualizzazione ad albero viene visualizzato un tooltip che descrive l\'errore. Nota: tutti gli altri oggetti che dipendono da un oggetto in tale stato di errore non verranno ricalcolati correttamente, quindi potrebbero ancora mostrare uno stato precedente.



### ![](images/FreeCAD_Tree_view_hidden.png ) Simbolo dell\'occhio 

Indica che l\'oggetto sarà nascosto nella vista ad albero se l\'opzione del menu contestuale **Mostra gli elementi nascosti nella vista ad albero** è deselezionata.


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Tree view/it
