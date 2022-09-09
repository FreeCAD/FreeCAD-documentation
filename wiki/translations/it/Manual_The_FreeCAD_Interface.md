# Manual:The FreeCAD Interface/it
<div class="mw-translate-fuzzy">





</div>


{{Manual   *TOC/it}}

FreeCAD utilizza il [framework Qt](https   *//en.wikipedia.org/wiki/Qt_(software)) per disegnare e gestire la sua interfaccia. Questa struttura viene utilizzata in una vasta gamma di applicazioni, perciò l\'interfaccia di FreeCAD è molto classica e non presenta particolari difficoltà di comprensione. La maggior parte dei pulsanti sono standard e si trovano dove ci si aspetta che siano **File → Apri, Modifica → Incolla, ecc**. Ecco l\'aspetto di FreeCAD quando lo si apre per la prima volta, subito dopo l\'installazione, e mostra il centro di partenza   *

![](images/FreeCAD-v0-18-FirstStart.png )

Lo start center è una comoda \"schermata di benvenuto\", che mostra le informazioni utili ai nuovi utenti, come gli ultimi file su cui si è lavorato, cosa c\'è di nuovo nel mondo FreeCAD, o sintetiche informazioni sugli ambienti di lavoro più comuni. Comunica inoltre se è disponibile una nuova versione stabile di FreeCAD.

Dopo un po\' di tempo, quando si ha maggiore familiarità con FreeCAD, si possono fare alcuni cambiamenti nelle preferenze, e molto probabilmente si vuole andare direttamente in uno degli altri ambienti di lavoro, con un nuovo documento aperto, o semplicemente, chiudere la pagina iniziale e creare un nuovo documento   *

![](images/FreeCAD-v0-18-NewProject.png )

### Gli ambienti di lavoro 

Notare che tra le due schermate precedenti alcune delle icone sono cambiate. Questo è il momento in cui entra in gioco il concetto più importante utilizzato nell\'interfaccia di FreeCAD   * gli ambienti di lavoro.

Gli ambienti di lavoro sono costituiti da un gruppo di strumenti (i pulsanti della barra degli strumenti, i menu e altri controlli dell\'interfaccia) che sono raggruppati secondo la loro specializzazione. Pensate ad un laboratorio dove ci sono diverse persone che lavorano insieme   * una che lavora con il metallo, un\'altra con il legno. Ognuno di loro ha, nel laboratorio, un tavolo separato con gli strumenti specifici per il proprio lavoro. Tuttavia, tutti possono lavorare sugli stessi oggetti. Lo stesso accade in FreeCAD.

Il più importante controllo dell\'interfaccia di FreeCAD è il selettore Workbench, che si usa per passare da un ambiente all\'altro   *

![](images/FreeCAD-v0-18-WorkbenchMenu.png )

Gli ambienti di lavoro spesso confondono i nuovi utenti, dato che non è sempre facile sapere in quale ambiente cercare uno specifico strumento. Ma in breve tempo, quasi senza rendersene conto, si trova un modo conveniente per organizzare la moltitudine di strumenti che FreeCAD offre, e che sono anche completamente personalizzabili (vedi sotto). Lo stesso strumento può apparire in più di un ambiente. L\'icona del pulsante per uno specifico strumento è sempre la stessa, indipendentemente dall\'ambiente in cui appare.

Più avanti in questo manuale, troverete anche una tabella che mostra i contenuti di tutti gli ambienti di lavoro.

### L\'interfaccia

Diamo uno sguardo alle diverse parti dell\'interfaccia   *

![](images/FreeCAD-v0-18-Cube.png )

-   **La vista 3D** è il componente principale dell\'interfaccia,

è dove gli oggetti con cui si lavora sono disegnati e manipolati. È possibile avere più viste dello stesso documento (o degli stessi oggetti) o più documenti aperti contemporaneamente. Ognuna di queste viste può essere sganciata individualmente dalla finestra principale. È possibile selezionare oggetti o parti di oggetti facendo clic su di essi, quindi è possibile eseguire panoramiche, zoomare e ruotare la vista con i pulsanti del mouse. Questo è spiegato ulteriormente nel prossimo capitolo.

Oltre al pannello di visualizzazione 3D, sono disponibili i seguenti pannelli di informazioni. Possono essere resi visibili o nascosti selezionandoli da **Visualizza → Pannelli**. Il nome del pannello appare nell\'angolo in alto a sinistra del pannello quando viene visualizzato   *

-   **La vista combinata** ha due schede   *
    -   La scheda Modello propone i contenuti e la struttura del documento nella parte superiore e le proprietà (o parametri) dell\'oggetto selezionato (i) nella parte inferiore. Queste proprietà sono divise in due categorie   *
        -   Dati (proprietà che riguardano la geometria stessa)
        -   Vista (proprietà che determinano il modo in cui la geometria appare sullo schermo).
    -   La scheda Azioni è il posto dove FreeCAD chiede di specificare i valori per lo strumento che si sta utilizzando, per esempio, di inserire un valore per la \'lunghezza\' quando si utilizza lo strumento Linea. Essa si chiude automaticamente quando si preme il tasto OK (o Annulla). Inoltre, facendo doppio clic sull\'oggetto correlato nella vista combinata, la maggior parte degli strumenti permette di ritornare sul pannello delle Azioni, per modificare le impostazioni.
        La scheda Azioni a volte ha effetti collaterali sconcertanti e frustranti. Se la scheda Azioni non è vuota, alcune operazioni di FreeCAD non funzionano come previsto. Ad esempio, se nel modello è presente un singolo oggetto come un cubo, facendo doppio clic su di esso si apre la scheda Azioni per consentire all\'utente di modificare i parametri che caratterizzano il cubo. Se si apre la [Vista selezione](#Vista_selezione.md), viene visualizzato il nome interno del cubo. L\'intero cubo diventa verde nel pannello 3D, a indicare che l\'intero cubo è selezionato. Cliccando sullo sfondo si deseleziona l\'intero cubo e si cancella la Vista selezione. Finora, questo è un comportamento normale. Tuttavia, se ora si fai clic su una faccia del cubo, invece della faccia selezionata, non viene selezionato nulla perché la scheda Azioni non è stata completata. Anche se non sono state apportate modifiche ai parametri, FreeCAD aspetta che si faccia clic sul pulsante **OK** (o altro) nella scheda Azioni.

-   **La vista Report** è normalmente nascosta, ma è una buona idea aprirla in quanto elenca tutte le informazioni, avvertimenti o errori che sono di aiuto per decifrare (o eseguire il debug) quello che può aver causato un errore.
-   **La console Python** per impostazione predefinita è anche essa nascosta. Questo è il posto dove è possibile interagire con il contenuto del documento utilizzando il [linguaggio Python](https   *//en.wikipedia.org/wiki/Python_%28programming_language%29). Dato che ogni azione fatta sull\'interfaccia di FreeCAD in realtà esegue un pezzo di codice Python, con questo pannello aperto è possibile vedere il codice svolgersi in tempo reale, e consente strada facendo di imparare un po\' di Python in un modo meraviglioso e facile, quasi senza accorgersene.
-   **La vista Struttura** visualizza solo la struttura ad albero mostrata nella scheda Modello nella vista combinata. È normalmente nascosta.
-   **La vista Proprietà** visualizza solo le informazioni sulle proprietà dell\'oggetto visualizzate nella parte inferiore della vista combinata. È normalmente nascosta.
-   **La vista Selezione** mostra i nomi di tutti gli oggetti che sono attualmente selezionati. Questi sono gli oggetti a cui viene applicata un\'operazione dell\'ambiente. Può essere usata per affinare la selezione deselezionando alcuni di questi oggetti prima che venga applicata un\'operazione. La vista selezione può anche essere utilizzata per cercare oggetti per nome e quindi selezionarli. Per impostazione predefinita, la vista selezione è nascosta. Sebbene sia spesso possibile determinare gli oggetti attualmente selezionati osservando l\'albero degli oggetti nella scheda Modello della vista combinata, per operazioni complesse che richiedono selezioni multiple e in cui la selezione è difficile, è utile rendere visibile questa vista in modo da poter vedere tutte le etichette e contare gli oggetti selezionati.

![](images/FreeCAD-v0-18-ExtrudeTask.png )

### Personalizzare l\'interfaccia 

L\'interfaccia di FreeCAD è altamente personalizzabile. Tutti i pannelli e le barre degli strumenti possono essere spostati in luoghi diversi o impilati uno sull\'altro. Quando è necessario possono anche essere chiusi e riaperti dal menu Visualizza o facendo clic destro su un\'area vuota dell\'interfaccia. Inoltre sono disponibili molte altre opzioni, come la creazione di barre degli strumenti personalizzate contenenti gli strumenti di uno qualsiasi degli ambienti, o l\'assegnazione e la modifica dei tasti di scelta rapida.

Le opzioni di personalizzazione avanzate sono disponibili dal menu **Strumenti → Personalizza**   *

![](images/FreeCAD-v0-18-CustomizeInterface.png )

**Approfondimenti**

-   [Primi passi con FreeCAD](Getting_started/it.md)
-   [Personalizzare l\'interfaccia](Interface_Customization/it.md)
-   [Ambienti di lavoro](Workbenches/it.md)
-   [More about Python](https   *//www.python.org)


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:The FreeCAD Interface/it
