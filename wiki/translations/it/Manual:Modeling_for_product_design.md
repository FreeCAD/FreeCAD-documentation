# Manual:Modeling for product design/it
{{Manual:TOC/it}}

[Product design](https://en.wikipedia.org/wiki/Product_design) è in origine un termine commerciale, ma nel mondo 3D, significa spesso modellazione di qualcosa con l\'idea di [stamparlo in 3D](https://en.wikipedia.org/wiki/3D_printing) o, più in generale, prodotto da una macchina, per esempio con una stampante 3D o con una [macchina CNC](https://en.wikipedia.org/wiki/Numerical_control).

Quando si stampano oggetti in 3D, è di fondamentale importanza che gli oggetti siano dei **solidi**. Dato che diventeranno reali, oggetti solidi, questo è ovvio. Naturalmente nulla impedisce che essi siano vuoti internamente. Ma è sempre necessario sapere esattamente quale punto è all\'interno del materiale, e quale punto è al di fuori, perché la stampante 3D o la macchina CNC deve sapere esattamente cosa è riempito di materiale e cosa non lo è. In FreeCAD, l\'ambiente [PartDesign](PartDesign_Workbench/it.md) è lo strumento perfetto per costruire questi pezzi, perché si prende sempre cura che gli oggetti rimangono solidi e costruibili.

Per illustrare come funziona l\'ambiente PartDesign, cerchiamo di modellare questo pezzo ben noto di [Lego](https://en.wikipedia.org/wiki/Lego):

![](images/Exercise_lego_01.jpg )

La cosa bella con i pezzi Lego è che le dimensioni sono facili da reperire su Internet, almeno per i pezzi standard. Questi sono abbastanza facili da modellare e da stampare in 3D, e con un po\' di pazienza (la stampa 3D richiede spesso molte regolazioni di messa a punto) si possono fare pezzi che sono totalmente compatibili e che si incastrano perfettamente nei blocchi Lego originali. Nell\'esempio seguente, faremo un pezzo che è 1,5 volte più grande di quello originale.


<div class="mw-translate-fuzzy">

Ora useremo esclusivamente strumenti di [ Sketcher](Sketcher_Workbench/it.md) e [ PartDesign](PartDesign_Workbench/it.md). Dato che tutti gli strumenti dell\'ambiente Sketcher sono inclusi anche nell\'ambiente PartDesign, possiamo stare in PartDesign e non avremo bisogno di passare avanti e indietro tra i due.


</div>

Gli oggetti di Part Design sono completamente basati su **Schizzi**. Uno Schizzo è un oggetto 2D, fatto di segmenti lineari (linee, archi di cerchio o ellissi) e di vincoli. I vincoli possono essere applicati sia sui segmenti lineari sia sui loro punti finali o centrali, e costringono la geometria ad adottare determinate regole. Ad esempio, è possibile inserire un vincolo verticale su un segmento di linea per costringerlo a rimanere in verticale, o applicare un vincolo di posizione (blocco) su un punto finale per impedirgli di muoversi. Quando uno schizzo ha la giusta quantità di vincoli che impedisce a qualsiasi punto del disegno di spostarsi, si parla di uno schizzo completamente vincolato. Quando ci sono dei vincoli ridondanti, che possono essere rimossi senza consentire alla geometria da spostarsi, si parla di geometria sovra-vincolata. Questo deve essere evitato, e, se succede, FreeCAD lo comunica.


<div class="mw-translate-fuzzy">

Gli Schizzi hanno una modalità di modifica, in cui la loro geometria e i loro vincoli possono essere cambiati. Quando si ha finito con le modifiche, e si esce dalla modalità di modifica, gli schizzi si comportano come qualsiasi altro oggetto FreeCAD, e possono essere utilizzati come elementi di base per tutti gli strumenti di PartDesign, ma anche in altri ambienti di lavoro, come ad esempio [ Parte](Part_Workbench/it.md) o [ Arch](Arch_Workbench/it.md). [Draft](Draft_Workbench/it.md) ha anche uno strumento che converte gli oggetti di Draft in schizzi, e viceversa.


</div>


<div class="mw-translate-fuzzy">

-   Cominciamo modellando una forma cubica che sarà la base del nostro mattoncino Lego. Successivamente intaglieremo l\'interno, e vi aggiungeremo le 8 bugne. Quindi cominciamo questo facendo uno schizzo rettangolare che sarà poi estruso:
-   Passare nell\'ambiente [PartDesign](PartDesign_Workbench/it.md)
-   Cliccare sul pulsante <img alt="" src=images/Sketcher_NewSketch.png  style="width:16px;"> [Nuovo Schizzo](Sketcher_NewSketch/it.md). Appare una finestra di dialogo che chiede dove si vuole posizionare il disegno, scegliere il piano **XY**, che è il piano \"terra\". Viene creato il disegno e viene immediatamente commutato in modalità di modifica, e la vista viene ruotata in modo che il disegno sia ortogonale all\'osservatore.
-   Ora si può disegnare un rettangolo, selezionando lo strumento <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:16px;"> [Rettangolo](Sketcher_CreateRectangle/it.md) e cliccando 2 punti d\'angolo opposti. È possibile inserire i due punti dove si vuole, dato che la loro posizione corretta verrà impostata nel passaggio successivo.
-   Notare che al rettangolo sono stati automaticamente aggiunti alcuni vincoli: i segmenti verticali hanno ricevuto un vincolo verticale, quelle orizzontali un vincolo orizzontale, e ogni angolo un vincolo di punto-con-punto che incolla insieme i segmenti. Si può sperimentare lo spostamento del rettangolo trascinando le sue linee con il mouse, tutta la geometria si manterrà fedele ai vincoli.


</div>

![](images/Exercise_lego_02.jpg )


<div class="mw-translate-fuzzy">

-   Ora, aggiungiamo altri tre vincoli:
    -   Selezionare uno dei segmenti verticali e aggiungere un <img alt="" src=images/Constraint_VerticalDistance.png  style="width:16px;"> [vincolo distanza verticale](Sketcher_ConstrainDistanceY/it.md). Dategli una dimensione di 23.7mm.
    -   Selezionare uno dei segmenti orizzontali e aggiungere un <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> [vincolo distanza orizzontale](Sketcher_ConstrainDistanceX/it.md). Dategli una dimensione di 47.7mm.
    -   Infine, selezionare uno dei punti d\'angolo, quindi il punto di origine (che è il punto di incrocio degli assi rosso e verde), e aggiungere un <img alt="" src=images/Constraint_PointOnPoint.png  style="width:16px;"> [vincolo coincidente](Sketcher_ConstrainCoincident/it.md). Il rettangolo salta al punto di origine, e lo schizzo diventa verde, il che significa che ora è completamente vincolato. Si può provare a spostare le sue linee o punti, ma nulla può più muoversi.


</div>

![](images/Exercise_lego_03.jpg )

Notare che l\'ultimo vincolo punto-su-punto non era assolutamente necessario. Non si è mai costretti a lavorare con schizzi completamente vincolati. Tuttavia, se vogliamo stampare questo blocco in 3D, è necessario mantenere il pezzo vicino al punto di origine (che è il centro dello spazio in cui la testina di stampa può muoversi). Con l\'aggiunta di quel vincolo siamo certi che il pezzo rimarrà sempre \"ancorato\" al punto di origine.


<div class="mw-translate-fuzzy">

-   Lo schizzo di base è pronto, possiamo lasciare la modalità di modifica premendo il pulsante **Chiudi** sulla parte superiore del pannello Azioni, o semplicemente premendo il tasto **Esc**. Se necessario in seguito, siamo in grado di rientrare in modalità di modifica in qualsiasi momento facendo doppio clic sullo schizzo nella vista ad albero.
-   Facciamo estrudere lo schizzo utilizzando lo strumento <img alt="" src=images/PartDesign_Pad.png  style="width:16px;"> [Pad](PartDesign_Pad/it.md), per una lunghezza di 14,4 mm. Le altre opzioni possono essere lasciate ai loro valori di default:


</div>

![](images/Exercise_lego_04.jpg )

Il **Pad** si comporta in modo molto simile allo strumento [Estrusione](Part_Extrude/it.md) che abbiamo usato nel capitolo precedente. Ci sono, però, alcune differenze, e la principale è che un pad non può essere spostato, esso è sempre collegato al suo schizzo. Se si vuole cambiare la posizione del pad, è necessario spostare il disegno di base. Nel contesto attuale, in cui vogliamo essere sicuri che nulla si muova dalla sua posizione, si tratta di una sicurezza aggiuntiva.


<div class="mw-translate-fuzzy">

-   Ora intagliamo l\'interno del blocco, utilizzando lo strumento <img alt="" src=images/PartDesign_Pocket.png  style="width:16px;"> [Tasca](PartDesign_Pocket/it.md), che è la versione PartDesign di [Parte Taglia](Part_Cut/it.md). Per effettuare una tasca, creiamo uno schizzo sulla faccia inferiore del blocco, che sarà utilizzato per rimuovere una parte del blocco.
-   Con la faccia inferiore selezionata, premere il pulsante <img alt="" src=images/Sketcher_NewSketch.png  style="width:16px;"> [Nuovo schizzo](Sketcher_NewSketch/it.md).
-   Disegnare un rettangolo sulla faccia.


</div>

![](images/Exercise_lego_05.jpg )


<div class="mw-translate-fuzzy">

-   Ora vincoliamo il rettangolo in relazione alla faccia inferiore. Per fare questo, bisogna \"importare\" alcuni bordi della faccia con lo strumento <img alt="" src=images/Sketcher_External.png  style="width:16px;"> [Geometria esterna](Sketcher_External/it.md). Utilizzare questo strumento sulle due linee verticali della faccia inferiore:


</div>

![](images/Exercise_lego_06.jpg )


<div class="mw-translate-fuzzy">

Notare che con questo strumento possono essere aggiunti solo i bordi dalla faccia di base. Quando si crea uno schizzo con una faccia selezionata, si crea una relazione tra quella faccia e il disegno, che è importante per le successive operazioni. È sempre possibile rimappare in un secondo tempo uno schizzo su un\'altra faccia con lo strumento<img alt="" src=images/Sketcher_MapSketch.png  style="width:16px;"> [Mappa schizzo](Sketcher_MapSketch/it.md).


</div>


<div class="mw-translate-fuzzy">

-   La geometria esterna non è \"reale\", viene nascosta quando si esce dalla modalità di modifica. Ma è possibile usarla per posizionare i vincoli. Posizionare i seguenti 4 vincoli:
    -   Selezionare il punto in alto a sinistra del rettangolo e il punto in alto della linea importata di sinistra e aggiungere un vincolo <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) di 1.8mm
    -   Selezionare nuovamente il punto in alto a sinistra del rettangolo e il punto in alto della linea importata di sinistra e aggiungere un vincolo <img alt="" src=images/Constraint_VerticalDistance.png  style="width:16px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) di 1.8mm
    -   Selezionare il punto in basso a destra del rettangolo e il punto in basso della linea importata di destra e aggiungere un vincolo <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) di 1.8mm
    -   Selezionare nuovamente il punto in basso a destra del rettangolo e il punto in basso della linea importata di destra e aggiungere un vincolo <img alt="" src=images/Constraint_VerticalDistance.png  style="width:16px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) di 1.8mm


</div>

![](images/Exercise_lego_07.jpg )


<div class="mw-translate-fuzzy">

-   Uscire dalla modalità di modifica. Ora si può eseguire l\'operazione di tasca: con il disegno selezionato, premere il pulsante <img alt="" src=images/PartDesign_Pocket.png  style="width:16px;"> [Pocket](PartDesign_Pocket/it.md). Assegnargli una lunghezza di 12.6 mm, che lascia alla faccia superiore del pad lo spessore di 1.8 mm (ricordare che l\'altezza totale del pad è di 14.4 mm).


</div>

![](images/Exercise_lego_08.jpg )


<div class="mw-translate-fuzzy">

-   Ora si devono attaccare le 8 bugne sulla faccia superiore. Per fare questo, dato che sono una ripetizione di una stessa caratteristica, si può usare il pratico strumento <img alt="" src=images/PartDesign_LinearPattern.png  style="width:16px;"> [Schiera lineare](PartDesign_LinearPattern/it.md) dell\'ambiente Part Design, che permette di modellare una volta e poi ripetere la forma.
-   Iniziare selezionando la faccia superiore del blocco
-   Creare un <img alt="" src=images/Sketcher_NewSketch.png  style="width:16px;"> [Nuovo schizzo](Sketcher_NewSketch/it.md).
-   Creare due <img alt="" src=images/Sketcher_Circle.png  style="width:16px;"> [cerchi](Sketcher_CreateCircle/it.md).
-   Per ogni cerchio, selezionarlo e aggiungere un <img alt="" src=images/Constraint_Radius.png  style="width:16px;"> [/it\|Vincolo raggio](Sketcher_ConstrainRadius.md) di 3.6mm a ciascuno di essi
-   Importare il bordo sinistro della faccia di base con lo strumento <img alt="" src=images/Sketcher_External.png  style="width:16px;"> [Geometria esterna](Sketcher_External/it.md).
-   Inserire due vincoli verticali e due vincoli orizzontali di 6 mm tra il centro di ogni cerchio ed i punti d\'angolo del bordo importato, in modo che il centro di ogni cerchio sia a 6 millimetri dal bordo della faccia:


</div>

![](images/Exercise_lego_09.jpg )


<div class="mw-translate-fuzzy">

-   Si noti, ancora una volta, che quando si blocca la posizione e la dimensione di ogni elemento del disegno, esso diventa completamente vincolato. Questo permette di andare sempre sul sicuro. Ora si potrebbe cambiare il primo schizzo, ma tutto quanto fatto in seguito sarebbe conservato.
-   Uscire dalla modalità di modifica, selezionare questo nuovo schizzo, e creare un <img alt="" src=images/PartDesign_Pad.png  style="width:16px;"> [Pad](PartDesign_Pad/it.md) di 2.7mm:


</div>

![](images/Exercise_lego_10.jpg )


<div class="mw-translate-fuzzy">

-   Si noti che, come in precedenza con la tasca, dato che si è utilizzata la faccia superiore del blocco di base come base per questo ultimo schizzo, qualsiasi operazione di PartDesign che si esegua con questo disegno sarà costruita correttamente sulla forma di base: la due bugne non sono oggetti indipendenti, esse sono state estruse direttamente dal mattoncino. Questo è il grande vantaggio di lavorare con l\'ambiente PartDesign, a patto di costruire sempre ogni passaggio su quello precedente, in realtà si sta costruendo un oggetto solido finale.
-   Ora è possibile duplicare le bugne quattro volte, in modo da ottenerne otto. Selezionare l\'ultimo Pad appena creato.
-   Premere il pulsante <img alt="" src=images/PartDesign_LinearPattern.png  style="width:16px;"> [Schiera lineare](PartDesign_LinearPattern/it.md).
-   Dargli una lunghezza di 36mm (che è l\'estensione totale a cui si vuole adattare le copie), nella direzione \"asse orizzontale dello schizzo\", e creare 4 occorrenze:


</div>

![](images/Exercise_lego_11.jpg )

-   Notare, ancora una volta, che questa non è solo una duplicazione di un oggetto, ma è una \*caratteristica\* di una forma che è stata duplicata, l\'oggetto finale è ancora un solo oggetto solido.
-   Ora si deve lavorare sui tre \"tubi\" che riempiono il vuoto che è stato creato sulla faccia inferiore. Ci sono diverse possibilità: creare uno schizzo con tre cerchi, un pad e poi una tasca per tre volte, o creare uno schizzo di base con un cerchio dentro l\'altro e fare pad per formare il tubo già completo, o anche altre combinazioni. Come sempre, in FreeCAD ci sono molti modi per raggiungere il medesimo risultato. A volte un modo non funziona come si desidera, e si deve cercare altri modi. Qui, useremo l\'approccio più sicuro, facendo le cose un passo alla volta.
-   Selezionare la faccia che è al fondo della cavità scavata in precedenza all\'interno del blocco.
-   Creare un nuovo schizzo, aggiungere un cerchio con un raggio di 4,8825 millimetri, importare il bordo sinistro della faccia, e vincolarlo verticalmente e orizzontalmente a 10,2 millimetri dall\'angolo superiore della faccia:

![](images/Exercise_lego_12.jpg )

If you have trouble to select features hiding part of the model can help. To hide a feature select it from tree view and press Space-key to toggle visibility.

-   Uscire dalla modalità di modifica, e con questo schizzo eseguire un pad con una lunghezza di 12,6 mm
-   Creare una schiera lineare da questo ultimo pad, dargli una lunghezza di 24 mm e 3 occorrenze. Ora nello spazio vuoto ci sono tre tubi pieni:

![](images/Exercise_lego_13.jpg )


<div class="mw-translate-fuzzy">

-   Ora si devono fare i fori finali. Selezionare la faccia circolare del primo dei tre \"spinotti\"
-   Creare un nuovo schizzo, importare il bordo circolare della faccia, creare un cerchio con un vincolo raggio di 3,6 millimetri, e aggiungere un <img alt="" src=images/Constraint_PointOnPoint.png  style="width:16px;"> [Vincolo di coincidenza](Sketcher_ConstrainCoincident/it.md) tra il centro del cerchio importato e il nuovo cerchio. Ora il cerchio è perfettamente centrato, e ancora una volta completamente vincolato:


</div>

![](images/Exercise_lego_14.jpg )

-   Uscire dalla modalità di modifica, e da questo schizzo creare una tasca con una lunghezza di 12,6 mm
-   Creare una schiera lineare da questa tasca, con una lunghezza di 24 mm e 3 occorrenze. Questo è l\'ultimo passo, ora il pezzo di Lego è completo, possiamo dargli un bel colore in segno di vittoria!

![](images/Exercise_lego_15.jpg )

Notare che la storia della modellazione (ciò che appare nella vista ad albero) è diventata piuttosto lunga. Essa è preziosa perché in seguito ogni singolo passo di quello che si è fatto può essere modificato. Adattando questo modello per creare un altro tipo di mattoncino, per esempio uno con 2x2 bugne, o 2x4, è una parte del lavoro, basta cambiare un paio di dimensioni e il numero di occorrenze delle schiere lineari. Si possono anche creare facilmente pezzi più grandi che non esistono nel gioco Lego originale.

Ma può anche essere utile sbarazzarsi dello storico, per esempio, se si ha intenzione di modellare un castello con questo mattoncino, e non si vuole avere nel file tutta questa cronologia ripetuta 500 volte.


<div class="mw-translate-fuzzy">

Ci sono due modi semplici per sbarazzarsi della storia, uno è con lo strumento [Crea una semplice copia](Part_SimpleCopy/it.md) dell\'ambiente [Part](Part_Workbench/it.md), che crea una copia del pezzo che non dipende più dalla storia (è possibile eliminare tutta la storia in seguito), l\'altro modo è esportare il pezzo come un file STEP e poi reimportarlo.


</div>

**Assemblaggio**


<div class="mw-translate-fuzzy">

Ma esiste anche il meglio dei due mondi, che è [Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2), un addon che può essere installato dal repository [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons). Questo Workbench è denominato \"2\" perché è anche in fase di sviluppo un ambiente di Assemblaggio built-in ufficiale, che non è ancora pronto. L\'ambiente Assembly2, invece, funziona già molto bene per costruire assemblaggi, e dispone anche di un paio di vincoli oggetto-su-oggetto, che è possibile utilizzare per vincolare la posizione di un oggetto in relazione ad un altro. Nell\'esempio che segue, tuttavia, è più veloce e più facile posizionare i pezzi usando <img alt="" src=images/Draft_Move.png  style="width:16px;"> [Draft muovi](Draft_Move/it.md) e <img alt="" src=images/Draft_Rotate.png  style="width:16px;"> [Draft ruota](Draft_Rotate/it.md) che utilizzando i vincoli di Assembly2.


</div>

-   Salvare il file nello stato attuale
-   Installare [Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2) e riavviare FreeCAD
-   Creare un nuovo documento vuoto
-   Passare nell\'ambiente Assembly2
-   Premere il pulsante **Import a part from another FreeCAD document**
-   Selezionare il file salvato in precedenza
-   Il pezzo finale viene importato nel documento corrente. L\'ambiente Assembly2 individua automaticamente nel file qual è il pezzo finale che deve essere utilizzato, e il nuovo oggetto rimane collegato al file. Se si modifica il contenuto del primo file, basta premere il tasto **Update parts imported into the assembly** per aggiornare anche qui i pezzi.
-   Utilizzando diverse volte il pulsante **Import a part from another FreeCAD document** , e lo spostamento e la rotazione dei pezzi (con gli strumenti Draft o manipolando la loro proprietà Placement), è possibile creare rapidamente un piccolo assemblaggio:

![](images/Exercise_lego_16.jpg )

**Download**

-   Il modello prodotto nel corso di questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [Ambiente Schizzo](Sketcher_Workbench/it.md)
-   [Ambiente Part Design](PartDesign_Workbench/it.md)
-   [The Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2)


</div>




[Category:Tutorials/it](Category:Tutorials/it.md)

---
[documentation index](../README.md) > Manual:Modeling for product design/it
