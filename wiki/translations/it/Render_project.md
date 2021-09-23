# Render project/it
 **(2020) This page refers to an attempt to update the [Raytracing Workbench](Raytracing_Workbench.md), proposed around 2012. Its original author never completed the implementation so this information is outdated, and should not be considered current.

New development is happening in the [https://github.com/FreeCAD/FreeCAD-render Render Workbench], a complete Python replacement for the [Raytracing Workbench](Raytracing_Workbench.md).

Despite this page mentioning the "Render module", this is not the same project as the new [https://github.com/FreeCAD/FreeCAD-render Render Workbench].
**

## Overview


{{TOCright}}


<div class="mw-translate-fuzzy">

## Il Modulo Render 

Il modulo di rendering fornisce un modo semplice e diretto per realizzare rapidamente le operazioni di rendering di parti create con FreeCAD. La sua filosofia si basa su un sistema di modello in modo da poter visualizzare il proprio lavoro in modo più efficiente. Il modulo Render si propone di nascondere all\'utente il complicato processo di rendering, in modo che egli debba preoccuparsi solo della progettazione delle parti.


</div>

Il flusso di lavoro è il seguente:

-   Creare una funzione di rendering.
-   Selezionare le impostazioni e i modelli desiderati.
-   Assegnare i materiali alle parti visibili nel documento.
-   Posizionare la fotocamera.
-   Visualizzare l\'anteprima del rendering.

Breve descrizione degli strumenti del Modulo Render:

### Operazioni di rendering 

La funzione Render contiene le informazioni che verranno passate al programma di rendering, quali la configurazione della fotocamera, le opzioni di rendering, i materiali e anche quali plug-in usare. Questo significa che è possibile creare molte funzioni di rendering, con diversi materiali oppure con impostazioni della fotocamera indipendenti una dall\'altra. La funzione prende inoltre il controllo del processo di rendering.

### Materiali di Rendering 

Ogni materiale di rendering è basato su una libreria dei materiali che sono memorizzati in file .XML indipendenti. Ai materiali di rendering possono essere assegnate delle proprietà quali il colore, la lucentezza e altri parametri. I materiali vengono aggiunti (allegati) a un oggetto nel documento.





**Per utilizzare il nuovo Ambiente Render, attualmente è necessario essere in grado di compilarlo dal ramo di sviluppo.**

### Utilizzare il modulo Render: 

Prima effettuare il checkout dal repository del ramo [raytracing](https://github.com/mrlukeparry/FreeCAD_sf_master/tree/raytracing). Assicurarsi quindi di poterlo compilare.

Scaricare e installare l\'ultima versione, la 1.2.1, di Lux Render da[download](http://www.luxrender.net/en_GB/download), per il proprio sistema e accertarsi che venga eseguito correttamente.

Aprire FreeCAD e avviare l\'ambiente <img alt="" src=images/Raytracing.png  style="width:16px;"> [ Raytracing](Raytracing_Workbench/it.md), poi impostare il **Percorso dell\'eseguibile** (path) per Lux Render. Può essere impostato in **Modifica → Preferenze → Raytracing**. In **exec path** deve essere impostato il percorso dell\'eseguibile luxconsole.

![](images/luxRenderExecPath.png )

Creare la parte (o le parti) con FreeCAD. Quindi tornare nell\'ambiente <img alt="" src=images/Raytracing.png  style="width:16px;"> [ Raytracing](Raytracing_Workbench/it.md) e creare una **funzione Render**. Editando questa funzione viene visualizzata una nuova \'Azione\' nella finestra della \'Vista Combinata\':

![](images/renderTaskView.png )

Quando si crea una operazione di rendering essa memorizza la posizione corrente e il tipo di fotocamera utilizzata nella vista 3D. È possibile riposizionare la fotocamera e fare clic su **Salva Camera** per memorizzare nella operazione l\'impostazione corrente della telecamera.

È possibile configurare altre impostazioni di rendering:

#### Impostazioni di rendering predefinite 

Le impostazioni di rendering predefinite sono specificate nel plugin di rendering che viene utilizzato. Modificano il processo di rendering per migliorare la qualità del prodotto o la velocità con cui è generato. Lux Render, **MLT Unbiased** produce risultati di qualità in tempi ragionevoli. **Direct Lighting Preview** produce un risultato veloce, ma di bassa qualità.

#### Render Template 

Visualizza i modelli che sono attualmente disponibili per il plug-in di rendering. Selezionando un modello, si genera una scena predefinita, con l\'illuminazione, la geometria e con le parti al suo interno. Attualmente **Lux Classic** funziona correttamente e produce risultati soddisfacenti. Esso tenta di calcolare la scena in base alla posizione della telecamera e alla dimensione complessiva delle parti visibili.

### Avviare un rendering 

Dopo che sono stati impostati i parametri della funzione, è possibile avviare il rendering della scena. Tutte le parti del documento che non sono visibili bella scena non sono incluse nell\'operazione di rendering. Quella successiva è la scena di esempio:

![](images/Example.png )

Il pulsante **Preview Window** renderizza la vista corrente della finestra 3D. Il pulsante **Preview** usa la posizione della telecamera salvata e anche la dimensione dell\'output. Si può eseguire una sola anteprima per ogni operazione di rendering, ma è possibile eseguire diverse operazioni distinte di rendering.

![](images/renderButtons.png )

Quando viene avviato un rendering, appare una nuova finestra di anteprima. Secondo la complessità della scena, l\'operazione può richiedere alcuni secondi per esportare la scena creata e caricarla nel programma di rendering esterno. Appare una schermata di caricamento.

![](images/loading.png )

Se il processo di rendering ha successo, il risultato viene automaticamente visualizzato. Si può liberamente spostare o ridimensionare l\'immagine.

![](images/sceneOutput.png )

### Unbiased Rendering - Rendering accurato 

Il programma di rendering simula sostanzialmente i \'riflessi\' dei raggi di luce che \'rimbalzano\' in una scena. Quando questi raggi di luce colpiscono la fotocamera essi diventano visibili nel risultato. Gradualmente più raggi colpiscono la fotocamera e l\'immagine viene costruita. All\'inizio l\'immagine è rumorosa (poco definita) dove la luce non raggiunge la fotocamera. I motori di rendering **Biased** imitano, tramite algoritmi, il comportamento della luce e producono velocemente una renderizzazione per approssimazione. I motori di rendering **Unbiased**, come [LuxRender](http://www.luxrender.net/en_GB/index), cercano invece di riprodurre esattamente gli effetti della luce reale, con un risultato molto più realistico e accurato.

L\'operazione è progressiva. Quando si è soddisfatti del risultato, premere il tasto **Stop Render**. Ora è possibile salvare l\'output in una posizione desiderata (attualmente memorizzato in un file .png).

![](images/unbiasedRendering.png )

### Velocità di rendering 

I processi di rendering sono in genere eseguiti dalla CPU. Il tempo necessario per un risultato soddisfacente, dipende dalla dimensione del risultato, dalla scena, dal numero e dalla complessità dei materiali utilizzati, dalle luci e dalle prestazioni complessive del sistema. Una veloce anteprima di una parte semplice può richiedere un minuto, mentre un output di alta qualità può richiedere diverse ore.

### Aggiungere i materiali 

Accertarsi di essere in modalità di modifica per la funzione di rendering. Fare clic su **Aggiungi materiali** nella barra degli strumenti. Nella finestra \'Azioni\' viene mostrato un elenco delle biblioteche dei materiali. È possibile scorrere l\'elenco trascinandolo o utilizzando la rotellina del mouse.

![](images/materialSelection.png )

Per aggiungere un materiale ad una parte nel documento, trascinare l\'icona del materiale e rilasciarla sulla parte nella vista 3D.

![](images/materialDragNDrop.png )

Se il materiale ha delle proprietà modificabili, quali il colore, nella scheda \'Azioni\' appare una nuova finestra di dialogo. In caso contrario, la scheda \'Azioni\' visualizza le funzioni di rendering.

![](images/materialProperties.png )

Quando si è soddisfatti delle impostazione delle proprietà, fare clic su **Salva**.

Tutti i materiali che sono all\'interno di una funzione di rendering vengono visualizzati nell\'elenco. Essi possono essere selezionati e cancellati, e se il materiale ha una proprietà si può modificarla con un doppio clic su di essa.

![](images/materialListView.png )

## Link

Vedere anche il [Tutorial di Raytracing](Raytracing_tutorial/it.md)


 

[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md) [Category:Render](Category:Render.md)
