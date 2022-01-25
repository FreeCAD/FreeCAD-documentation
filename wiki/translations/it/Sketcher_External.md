---
- GuiCommand:/it
   Name:Sketcher_External
   Name/it:Geometria esterna   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   Shortcut:X
   MenuLocation:Sketch → Geometrie → Geometria Esterna
   SeeAlso:[Linea di costruzione](Sketcher_ToggleConstruction/it.md)
---

# Sketcher External/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Geometria esterna di Sketcher serve quando è necessario applicare un vincolo tra la geometria dello schizzo e qualcosa di esterno allo schizzo. Funziona inserendo un collegamento di tipo vincolo di costruzione geometrico nello schizzo. Il colore predefinito dei bordi esterni collegati, è magenta. Come la geometria di costruzione standard, non collegata (blu), anche la geometria esterna collegata è visibile solo quando il disegno è in modalità di modifica e non viene utilizzata nel risultato successivo, nè usata in un altro strumento. Entrambi i tipi di geometria di costruzione nello schizzo possono essere utilizzati come riferimenti per i vincoli.


</div>

A note of caution, using this tool to link to generated (solid) geometry can lead to unexpected results due to [Topological Naming Problem](Topological_naming_problem.md). Also see [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).

<FILE:Sketcher_ExternalEsempio1.png>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Creare un nuovo schizzo o aprire uno schizzo esistente.
2.  Attivare lo strumento Geometria esterna.
3.  Selezionare il bordo o il punto che si vuole collegare.
4.  Premere Esc o selezionare un altro strumento per interrompere l\'importazione della geometria nello schizzo.


</div>


<div class="mw-translate-fuzzy">

### Regole di selezione 

Le regole per selezione gli oggetti che possono essere importati differiscono drasticamente tra FC v0.16 e FC v0.17.


</div>


<div class="mw-translate-fuzzy">

Cioè, lo schizzo e l\'oggetto devono essere nello stesso corpo, o nella stessa parte, o entrambi al di fuori di qualsiasi parte e corpo.


</div>

Ad esempio, se lo schizzo aperto si trova in Body, è possibile utilizzare un altro schizzo dal Body come geometria esterna, ma non è possibile utilizzare uno schizzo da Body001 o un bordo di un cubo di Part che si trovi nella radice del progetto. Usare la funzione Forma legata per portare una copia dell\'oggetto nel sistema di coordinate dello schizzo aperto. Dopo è possibile usare i bordi o i vertici dell\'oggetto Shapebinder.

-   Non sono permesse dipendenze circolari.

Ciò significa che non è possibile collegarsi ad un Pocket creato con questo schizzo. Non è possibile collegarsi ad alcun oggetto che dipenda dallo schizzo.


<div class="mw-translate-fuzzy">

A differenza della v0.16, per poter utilizzare questo strumento lo schizzo non deve essere su nessuna faccia. I collegamenti diretti tra gli schizzi sono possibili e incoraggiati, poiché sono più affidabili.


</div>

### Come capire se la linea è stata tratta 

Se la linea è tratta con successo diventa di colore magenta. Se non viene tratta, rimane verde.

### Analogia con le Linee di costruzione 

Le linee magenta di geometria esterna possono essere usate come [Linee di costruzione](Sketcher_ToggleConstruction/it.md). Le linee di costruzione sono linee che sono interne al disegno e sono utilizzate per la costruzione della geometria, ma non per le successive operazioni di modellazione di solidi, quali ad es. le estrusioni.

### I due principali utilizzi delle linee geometria esterna 

Nel flusso di lavoro dell\'ambiente PartDesign, lo strumento geometria esterna viene utilizzato per supportare il posizionamento di un aspetto del solido che si sta costruendo, relativo alla fase precedente nella sua costruzione. L\'ambiente PartDesign è destinato a produrre un unico solido, quindi questi schizzi con geometria esterna vengono utilizzati per creare una nuova funzionalità di un singolo solido.

Lo strumento Geometria esterna può, per esempio, essere utilizzato come riferimento per un vincolo utilizzato per posizionare un foro in un oggetto, in una data posizione con riferimento a un bordo o ad un vertice.

### Uso della geometria esterna in un flusso di lavoro di Part 

È possibile utilizzare qualsiasi geometria della parte che si trova nel sistema di coordinate dello schizzo. Si consiglia di collegarsi alla prima caratteristica possibile, in quanto forma un collegamento più stabile.

## Esempio

Quello sottostante è uno schizzo mappato sulla faccia superiore di un solido creato da una estrusione di uno schizzo precedente. Le linee magenta sono la Geometria esterna collegata a due bordi di questo Pad preesistente.

In questo caso sono utilizzati come riferimento per i vincoli di tangenza con la circonferenza di un cerchio. Essi sono utilizzati anche come riferimento per un vincolo orizzontale e un vincolo verticale per individuare il centro del secondo cerchio rispetto all\'estremità e al lato superiore del pad.

<FILE:Sketcher_ExternalEsempio2.png>

Questo è lo stesso schizzo in modalità di modifica, ma il Pad su cui è mappato è nascosto.

<FILE:Sketcher_ExternalEsempio4.png>

Quando lo schizzo viene chiuso le linee Geometria esterna non sono più visibili.

<FILE:Sketcher_ExternalEsempio3.png>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/it
