# Manual:Traditional 2D drafting/it
{{Manual:TOC/it}}

Si può essere interessati a FreeCAD perché si ha già una certa esperienza di disegno tecnico, ad esempio con un software come [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Si conosce già qualcosa sulla progettazione, oppure si preferisce disegnare le cose prima di costruirle. In ogni caso, FreeCAD dispone di un ambiente di lavoro più tradizionale, con gli strumenti che si trovano nella maggior parte delle applicazioni CAD 2D: l\'ambiente [Draft](Draft_Workbench/it.md).

L\'ambiente Draft, anche se adotta metodi di lavoro ereditati dal tradizionale mondo del CAD 2D, non si limita affatto al regno 2D. Tutti i suoi strumenti lavorano in tutto lo spazio 3D e molti degli strumenti di Draft, ad esempio <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Sposta](Draft_Move/it.md) o <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Ruota](Draft_Rotate/it.md), sono comunemente utilizzati in tutto FreeCAD, perché sono spesso più intuitivi che cambiare i parametri di posizionamento manualmente.

Tra gli strumenti offerti dall\'ambiente Draft, si trovano gli strumenti di disegno tradizionali come <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linea](Draft_Line/it.md), <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Cerchio](Draft_Circle/it.md), o <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Wire](Draft_Wire/it.md) (polilinea), gli strumenti di modifica come <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Sposta](Draft_Move/it.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Ruota](Draft_Rotate/it.md) o <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset/it.md), un sistema [piano di lavoro con griglia](Draft_SelectPlane/it.md) che consente di definire con precisione in quale piano si sta lavorando, e un completo [sistema di aggancio (snap)](Draft_Snap/it.md) che rende molto facile disegnare e posizionare gli elementi in relazione tra di loro con precisione.

Per mostrare il funzionamento e le possibilità dell\'ambiente Draft, cammineremo attraverso un semplice esercizio, il cui risultato sarà questo piccolo disegno. Esso mostra la planimetria di una piccola casa che contiene solo un top cucina (Un piano abbastanza assurdo, ma qui possiamo fare quello che vogliamo)?:

![](images/Exercise_cabin_01.jpg )

-   Passare nell\'ambiente **Draft**
-   Come in tutte le applicazioni di disegno tecnico, è bene preparare il proprio ambiente in modo corretto, questo farà risparmiare un sacco di tempo. Configurare le impostazioni [griglia e piano di lavoro](Draft_SelectPlane/it.md), [Testo](Draft_Text/it.md) e [Dimensioni](Draft_Dimension/it.md) secondo le proprie preferenze nel menu **Modifica → Preferenze → Draft**. In questo esercizio, però, si procederà come se queste impostazioni delle preferenze vengano lasciate ai loro valori predefiniti.

![](images/Freecad_draft_options_01.jpg )

-   C\'è un\'opzione che richiede un po\' di attenzione: **Riempi gli oggetti con le facce quando possibile**. Se essa è attivata, gli oggetti chiusi come i rettangoli o i cerchi sono riempiti automaticamente con una faccia, e questo può rendere difficile l\'aggancio agli oggetti sottostanti. Si può disattivare questa opzione o, in seguito, disattivare la proprietà **Crea facce** di ogni singolo oggetto, per impedire che creino una faccia.

-   L\'ambiente Draft ha anche due barre degli strumenti speciali: una con le **impostazioni di visualizzazione**, in cui è possibile cambiare il piano di lavoro corrente, attivare o disattivare la [modalità costruzione](Draft_ToggleConstructionMode/it.md), impostare il colore della linea, il colore della faccia, lo spessore di linea e le dimensioni del testo da utilizzare per i nuovi oggetti, e un\'altra con le **posizioni di aggancio**. Quindi, è possibile attivare o disattivare la griglia e stabilire di volta in volta le posizioni di [Aggancio](Draft_Snap/it.md):

![](images/Draft_toolbars.jpg )

-   L\'attivazione di tutti i pulsanti di snap è utile, ma rende anche più lento il disegno, poiché è necessario eseguire più calcoli quando si sposta il cursore del mouse. Spesso è meglio mantenere solo quelli che si usano effettivamente.

-   Iniziare attivando la **modalità costruzione** che permette di disegnare alcune linee guida su cui disegnare la geometria finale.
-   Se lo si desidera, impostare il **piano di lavoro** in **XY**. Se si esegue questa operazione, il piano di lavoro non cambia, qualsiasi sia la vista corrente. In caso contrario, il piano di lavoro si adatta automaticamente alla vista corrente, e si deve stare attenti ad essere nella vista dall\'alto ogni volta che si vuole disegnare sul piano XY (terra).
-   Quindi, selezionare lo strumento <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rettangolo](Draft_Rectangle/it.md) e disegnare un rettangolo, a partire dal punto (0,0,0), di 2 metri per 2 metri (lasciando Z a zero). Notare che la maggior parte dei comandi di Draft possono essere eseguiti completamente dalla tastiera, senza toccare il mouse, usando le loro due lettere di scelta rapida. Questo primo rettangolo di 2x2m può essere eseguito da tastiera con: re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**.
-   Duplicare il rettangolo distanziato di 15 centimetri all\'interno, utilizzando lo strumento <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset/it.md), attivando la sua modalità Copia, e assegnando una distanza di 15cm:

![](images/Exercise_cabin_02.jpg )

-   Si possono quindi disegnare un paio di linee verticali per definire dove verranno posizionate le porte e le finestre, utilizzando lo strumento <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linea](Draft_Line/it.md) (notare che la casella della modalità \"relativa\" dovrebbe essere deselezionata per questo passaggio). L\'incrocio di queste linee con i due rettangoli fornisce le intersezioni utili per agganciare i muri. Disegnare la prima linea dal punto (15cm, 1m, 0) al punto (15cm, 3m, 0).
-   Duplicare la linea 5 volte, usando lo strumento <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Sposta](Draft_Move/it.md) con la modalità Copia attivata. Attivare anche la modalità Relativa, che permette di definire gli spostamenti in distanze relative, che è più facile che calcolare la posizione esatta di ogni linea. Eseguire ogni operazione di spostamento in sequenza sulla riga creata immediatamente prima. Assegna a ogni nuova copia un punto iniziale, ad esempio puoi lasciarlo a (0,0,0) e i seguenti punti finali relativi:
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

![](images/Exercise_cabin_03.jpg )

-   Ora c\'è tutto quello che serve, quindi si può disattivare la modalità di costruzione. Notare che tutta la geometria di costruzione è stata collocata in un gruppo \"Costruzione\", che la rende facile da nascondere tutta insieme o addirittura eliminarla completamente in seguito.
-   Disegnare due porzioni di muro utilizzando lo strumento <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Wire](Draft_Wire/it.md). Assicurarsi che lo <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [snap intersezione](Draft_Snap/it.md) sia attivo, dato che ci si deve agganciare alle intersezioni tra le linee ed i rettangoli. Disegnare due polilinee come segue, facendo clic su tutti i vertici del loro contorno. Per chiuderle, fare di nuovo clic sul primo punto, o premere il pulsante **Chiudi**:

![](images/Exercise_cabin_04.jpg )

-   E\' possibile cambiare il loro colore grigio predefinito di un bel modello di tratteggio. Selezionare entrambe le pareti, quindi impostare la loro proprietà **Pattern** in **Simple**, e **Pattern size** a piacere, per esempio **0.005**.

![](images/Exercise_cabin_05.jpg )

-   A questo punto si può nascondere la geometria di costruzione facendo clic destro sul gruppo Construction e scegliendo **Nascondi selezione**.
-   Ora disegnare le finestre e le porte. Assicurarsi che lo <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [snap al punto centrale](Draft_Snap/it.md) sia attivato, e disegnare sei linee come segue:

![](images/Exercise_cabin_06.jpg )

-   Ora cambiare la linea della porta per creare un simbolo di porta aperta. Iniziare a ruotare la linea utilizzando lo strumento <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Ruota](Draft_Rotate/it.md). Fare clic sul punto finale della linea come centro di rotazione, dargli un angolo iniziale di **0**, e un angolo finale di **-90**.
-   Quindi creare l\'arco dell\'apertura con lo strumento <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Arco](Draft_Arc/it.md). Scegliere come centro lo stesso punto usato come centro di rotazione nel passaggio precedente, cliccare l\'altro punto della linea per assegnare il raggio, quindi i punti di inizio e di fine arco come segue:

![](images/Exercise_cabin_07.jpg )

-   Ora si può iniziare a posizionare alcuni mobili. Per cominciare, collocare un piano di lavoro disegnando un rettangolo dall\'angolo interno in alto a sinistra, con una larghezza di 170 centimetri e un\'altezza di -60cm. Nell\'immagine sottostante, la proprietà **Trasparenza** del rettangolo è impostata su 80%, per dare ai mobili un aspetto piacevole.
-   Poi aggiungere un lavandino e un piano cottura. Disegnare questi tipi di simboli a mano può essere molto noioso, e di solito sono facili da trovare su Internet, ad esempio su <http://www.cad-blocks.net> . Da questo sito nella sezione **Download**, per comodità, ci si può procurare un lavandino e un piano cottura separati, e salvarli come file DXF. È possibile scaricare questi due file visitando il link, e facendo clic destro sul pulsante **Raw** , poi su **Salva con nome**.
-   L\'inserimento di un file DXF in un documento FreeCAD aperto può essere fatto scegliendo l\'opzione del menu **File → Importa**, oppure trascinando il file DXF dal file explorer nella finestra di FreeCAD. Il contenuto dei file DXF potrebbero non apparire proprio al centro della visualizzazione corrente, a seconda di dove si trovava nel file DXF. È possibile utilizzare il menu **Visualizza → Viste standard → Visualizza tutto** per adattare la vista e trovare gli oggetti importati. Inserire i due file DXF, e spostarli nella posizione appropriata sul tavolo:

![](images/Exercise_cabin_08.jpg )

-   Ora si possono mettere alcune dimensioni utilizzando lo strumento <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Dimensioni](Draft_Dimension/it.md). Le dimensioni sono disegnate facendo clic su 3 punti: il punto iniziale, il punto finale, e un terzo punto per posizionare la linea di quota. Per rendere le dimensioni orizzontali o verticali, anche se i primi due punti non sono allineati, premere **Shift** mentre si clicca sul secondo punto.
-   È possibile modificare la posizione di un testo di quota con un doppio clic sulla dimensione nella vista ad albero. Un punto di controllo permette di spostare il testo graficamente. Nell\'esercizio, i testi \"0.15\" sono stati allontanati per una migliore chiarezza.
-   È possibile modificare il contenuto del testo di quota modificando la loro proprietà **Override**. Nell\'esempio, il testo delle dimensioni della porta e della finestra sono stati modificati per indicare le loro altezze:

![](images/Exercise_cabin_09.jpg )

-   Aggiungere alcuni testi di descrizione utilizzando lo strumento <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Testo](Draft_Text/it.md). Fare clic in un punto per posizionare il testo, quindi inserire le righe di testo, premendo Invio dopo ogni riga. Per finire, premere Invio due volte.
-   Le linee di indicazione (chiamate anche \"leader\" o linee guida) che collegano i testi all\'oggetto che descrivono sono fatte semplicemente con lo strumento Wire. Disegnare le linee partendo dalla posizione del testo e andando verso l\'oggetto descritto. Fatto ciò, è possibile aggiungere un pallino o una freccia alla fine delle linee impostando la loro proprietà **End Arrow** su **`True`**

![](images/Exercise_cabin_10.jpg )

-   Ora il disegno è completo! Dato che cominciano ad esserci un certo numero di oggetti, sarebbe saggio fare un po\' di pulizia e mettere tutto in una bella struttura per gruppi, in modo da rendere il file più comprensibile da altri:

![](images/Exercise_cabin_11.jpg )

-   Ora è possibile stampare il lavoro ponendolo in un foglio di disegno (una pagina di Drawing), che viene spiegato più avanti in questo manuale, o esportare direttamente il disegno per altre applicazioni CAD esportandolo in un file DXF. È sufficiente selezionare il gruppo \"Floor plan\", selezionare il menu **File → Esporta**, e selezionare il formato di Autodesk DXF. Il file può essere aperto in qualsiasi altra applicazione CAD 2D come [LibreCAD](http://www.librecad.org). Ci possono essere alcune differenze, a seconda delle configurazioni di ciascuna applicazione.

![](images/Exercise_cabin_12.jpg )

-   Però, la cosa più importante di Draft è che la geometria creata con questo ambiente può essere utilizzata come base o facilmente estrusa in oggetti 3D, semplicemente utilizzando lo strumento <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Estrudi](Part_Extrude/it.md) dell\'ambiente [Part](Part_Workbench/it.md), o, per rimanere in Draft, lo strumento <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex/it.md) (Tronca/Estendi/Estrudi), che in realtà esegue un Estrusione di Parte, ma lo fa \"nel modo di Draft\", cioè, consente di indicare e agganciare la lunghezza di estrusione graficamente. L\'estrusione sarà sperimentata con le pareti come illustrato in seguito.
-   Premendo il pulsante <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [piano di lavoro](Draft_SelectPlane/it.md) dopo aver selezionato una faccia di un oggetto, si è anche in grado di posizionare il piano di lavoro ovunque, e quindi di disegnare oggetti Draft in piani diversi, ad esempio sulla parte superiore delle pareti. Questi possono poi essere estrusi per formare altri solidi 3D. Sperimentare l\'impostazione del piano di lavoro su una delle facce superiori delle pareti, quindi disegnare dei rettangoli sopra di essa.

![](images/Exercise_cabin_13.jpg )

-   Tutti i tipi di aperture possono anche essere fatte facilmente disegnando degli oggetti Draft sulle facce dei muri, poi estrudendoli, e quindi utilizzando gli strumenti booleani dell\'ambiente Parte per sottrarli da un altro solido, come abbiamo visto nel capitolo precedente.

Fondamentalmente, l\'ambiente Draft fornisce un modo grafico per creare le operazioni base di Parte. Mentre in Parte di solito gli oggetti si posizionano impostando a mano i loro parametri di posizionamento, in Draft si può farlo sullo schermo. Ci sono casi in cui è meglio uno, e casi in cui è preferibile l\'altro. Non dimenticare che è possibile creare una [barra degli strumenti personalizzata](Interface_Customization/it.md) in uno di questi ambienti, aggiungere gli strumenti dall\'altro, e di ottenere il meglio dei due mondi.

## Downloads

-   Il file creato durante questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   Il file DXF del lavandino: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   Il file DXF del piano cottura: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   Il file DXF finale prodotto durante questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>



## Correlazioni

-   [L\'ambiente Draft](Draft_Workbench/it.md)
-   [Agganciare gli oggetti](Draft_Snap/it.md)
-   [Il piano di lavoro di Draft](Draft_SelectPlane/it.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/it
