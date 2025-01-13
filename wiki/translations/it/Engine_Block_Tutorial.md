---
 TutorialInfo:t
   Topic:  Part
   Level:  Base
   Time:  1 ora
   Author: Andrewbuck40
   FCVersion: 0.14.3700
   Files: 
}}

!{width="600"}

Questa è una guida introduttiva alla modellazione in FreeCAD.

Il tutorial si propone di far conoscere i tipi di dati primitivi per gli oggetti parametrici, le operazioni booleane, il disegno 2D e il processo di conversione di progetti 2D in modelli 3D.

Come lavoro di esempio viene modellato un semplice monoblocco motore con il basamento, come mostrato nella figura sopra.

## Operazioni iniziali 

Per cominciare, aprire FreeCAD, andare su **File , Nuovo** e creare un nuovo documento, quindi andare su **File , Salva** e salvarlo sul computer dove si preferisce, denominare **\"Motore\"** il progetto.

Notare che, dopo aver salvato il progetto, nella vista della *struttura* sul lato sinistro dello schermo, viene mostrato il nome del progetto su cui si sta lavorando. È possibile avere contemporaneamente più progetti aperti, in questo caso, nella vista ad albero tutti i progetti sono mostrati come radice di un albero.

## Sgrossatura della billetta 

Ora si inizia a lavorare sul modello. Per prima cosa aggiungere un cubo  per rappresentare la sagoma del blocco motore. Per fare questo si deve aggiungere un oggetto *Part* al modello, andare quindi in **Visualizza , Ambienti , Part** e selezionare l\'Ambiente Part. Notare che dopo aver selezionato l\'ambiente di lavoro, la barra degli strumenti in alto propone un diverso set di pulsanti. Esplorare un paio di altri \'Ambienti di lavoro\' per familiarizzare con il sistema degli ambienti e poi tornare all\'Ambiente Part.

### Il Blocco Motore 

Nell\'Ambiente Part si possono vedere diversi pulsanti per creare degli oggetti primitivi del tipo cubo, sfera, cono, ecc. Fare clic sul pulsante !{width="16"} *Cubo* per aggiungerne uno alla scena. Ciascuno degli oggetti primitivi elencati ha una serie predefinita di parametri che vengono impostati quando la forma primitiva viene aggiunta alla scena. Si può provare ad aggiungerne una forma per tipo e vedere come si presentano. Le primitive possono essere rimosse dalla scena selezionandole e premendo il tasto di cancellazione. Ci sono due modi per selezionare gli oggetti: è possibile usare il tasto sinistro del mouse su di loro nella Vista 3D, oppure è possibile cliccare sul loro nome nella vista ad albero alla sinistra. In entrambi i metodi, tenere premuto **Ctrl** durante la selezione permette la selezione multipla. È possibile ingrandire la Vista 3D con la rotellina del mouse. Per spostare la vista, premere il tasto centrale e trascinare. Per ruotare la vista premere e tenere premuto il pulsante centrale del mouse e contemporaneamente premere e tenere premuto il pulsante sinistro del mouse, quindi trascinare il mouse e eseguire la rotazione. Si può anche fare un click con il pulsante centrale in un punto all\'interno di un oggetto 3D per produrre la rotazione dello spazio 3D intorno a quel punto. Inoltre, i numeri 1-6 e il numero 0 del tastierino numerico visualizzano la scena secondo le viste standard . Dedicare un paio di minuti per prendere confidenza con la manipolazione della Vista 3D.

:   *Ulteriori letture: Navigare con il mouse*

Dopo aver posizionato il cubo e acquisito dimestichezza con il mouse, si prosegue impostando le dimensioni del modello CAD.

Selezionare il cubo cliccando su di esso nella vista ad albero e poi fare clic sulla scheda *Dati* della *Finestra delle proprietà* che si trova sotto la vista ad albero .

Nella scheda dei dati è possibile modificare le proprietà dell\'oggetto selezionato nella vista ad albero. Sempre nella stessa scheda, secondo il tipo di oggetto selezionato, si devono impostare differenti parametri. Per un cubo  servono 3 vettori, uno per la sua posizione nello spazio 3D, un altro per il suo orientamento e un terzo per definire le sue dimensioni. Per una sfera si deve specificare il suo punto centrale, e il raggio. I coni hanno un raggio, una altezza e la posizione, e così via.

In questo caso si sta costruendo un piccolo blocco motore a due cilindri quindi impostare la dimensione e la posizione del cubo con i seguenti valori :

:   {\    class: wikitable border=1

\|- \| X: 0.0 mm \|\| Lunghezza: 140.0 mm \|- \| Y: -40.0 mm \|\| Larghezza: 80.0 mm \|- \| Z: 0.0 mm \|\| Altezza: 110.0 mm \|- \|}

Dopo aver dimensionato correttamente il blocco motore, dare al progetto un nome più descrittivo. Selezionarlo nella vista ad albero e usare il tasto destro del mouse per rinominarlo oppure premere il tasto **F2**. Chiamare **Billetta** questa parte.

### Il primo cilindro 

Ora si procede praticando il foro del primo cilindro attraverso tutta la lunghezza del blocco motore. Per fare questo, occorre aggiungere al modello un cilindro con la forma che si desidera asportare e poi eseguire una operazione booleana per *sottrarre* il materiale dal blocco. Fare clic sul pulsante aggiungi !{width="16"} *Cilindro* per creare un nuovo cilindro, quindi selezionarlo nella vista ad albero e impostarne le proprietà come segue:

:   {\    class: wikitable border=1

\|- \| X: 40.0 mm \|\| Altezza: 110.0 mm \|- \| Y: 0.0 mm \|\| Raggio: 25.0 mm \|- \| Z: 0.0 mm \|\| \|- \|}

Se le proprietà sono impostate correttamente, si vedono le estremità circolari del cilindro sulle facce superiore ed inferiore del blocco motore.

Selezionare questo oggetto nella vista ad albero e nominarlo **Cilindro 1**.

### Il secondo cilindro 

È possibile creare il secondo cilindro nello stesso modo del primo, però è molto più facile copiare il lavoro già fatto per il primo e cambiare solo la coordinata X della posizione.

Per fare questo, selezionare **Cilindro 1** nella vista ad albero e poi andare in **Modifica , Duplica selezione**.

Appena impartito il comando, si vede immediatamente apparire il nuovo cilindro nella vista ad albero , ma non lo si vede nella vista 3D, in quanto è nella stessa posizione del primo cilindro. Ora selezionare *Cilindro 2* nella vista ad albero e poi modificare la sua coordinata X impostandola in 100 mm.

Notare che mentre si aggiornano i numeri nel campo dati si vede il movimento del cilindro nella vista 3D.

Dopo che il secondo cilindro è ubicato correttamente è possibile vedere il suo aspetto. Per vedere l\'aspetto del cilindro selezionare la **Billetta** nella vista ad albero e poi nasconderla premendo la **barra spaziatrice** . Come esercizio, nascondere tutti tre gli oggetti uno ad uno e poi mostrarli di nuovo.



### Forare il Blocco 

!{width="300"}

Ora che entrambi i cilindri sono posizionati essi vanno utilizzati per forare il blocco in modo appropriato. Per fare questo si applicano le *Operazioni Booleane* sulle 3 primitive. Iniziare creando una unione dei due cilindri in modo da poterli sottrarre contemporaneamente, come gruppo, dal blocco.

Selezionare **Cilindro 1** nella vista ad albero con ***CTRL**+LeftClick* poi nello stesso modo selezionare anche **Cilindro 2**. Ora premere il pulsante !{width="16"} **Unione** per fondere gli oggetti in uno solo.

Notare che nella vista ad albero, ora è presente un nuovo oggetto chiamato *Fusion*. Facendo clic sulla freccia accanto a *Fusion* si vedono i due cilindri, ma essi non sono accessibili.

Rinominare il blocco con **Cilindri** al posto di *Fusion*, così in seguito sarà più facile trovarlo.

A questo punto si deve forare il blocco motore.

Selezionare **Billetta** e quindi selezionare anche **Cilindri** poi premere il pulsante !{width="16"} *Taglia* .

I due oggetti selezionati sono di nuovo uniti come per una operazione di unione e il singolo oggetto risultante viene chiamato *Cut* . Premere il tasto 2 del tastierino numerico per ottenere la vista dall\'alto e poter guardare dall\'altra parte del blocco motore dritto verso il basso attraverso i cilindri, quindi con *Tasto centrale + Tasto sinistro  + Trascinare* ruotare e osservare il blocco motore. Il risultato dovrebbe essere simile alla figura a destra.

Notare che nella schermata la vista ad albero sulla sinistra è espansa per visualizzare le primitive individuali e che è selezionato **Cilindro 2** per esaminare la sua scheda *Dati* nella finestra delle *Proprietà*.

### I vantaggi chiave della modellazione parametrica 

Ora che i cilindri sono stati scavati si può capire facilmente uno dei vantaggi di questo sistema. Supporre che ad un certo punto dello sviluppo, si scopre che si vogliono dei cilindri un po \'più grandi. Dato che le operazioni di unione e di intersezione eseguite sono state registrate e raggruppate nella vista ad albero, è possibile cambiare la dimensione del cilindro e FreeCAD deve solo eseguire nuovamente il processo di unione e intersezione per determinare la dimensione del nuovo motore. Prima di continuare l\'esercitazione, provare a modificare il raggio e la posizione dei due cilindri e poi tornare ai parametri definiti prima.



## Il Carter 



### Billetta e alloggiamento dell\'albero motore 

Ora si tratta di lavorare sul basamento sotto al monoblocco.

Aggiungere un nuovo box o cubo, rinominarlo **Billetta Basamento**, e assegnargli le seguenti proprietà:

:   {\    class: wikitable border=1

\|- \| X: 0.0 mm \|\| Lunghezza: 140.0 mm \|- \| Y: -50.0 mm \|\| Larghezza: 100.0 mm \|- \| Z: -85.0 mm \|\| Altezza: 85.0 mm \|- \|}

Per tenere separata la parte basamento è possibile attribuirgli un colore diverso. Per cambiare il colore fare clic destro sull\'oggetto nella vista ad albero e modificarlo. È possibile assegnare all\'oggetto un colore personalizzato o un colore casuale .

Aggiungere un altro cubo denominato *Taglio di accoppiamento*, e assegnargli le seguenti proprietà:

:   {\    class: wikitable border=1

\|- \| X: 0.0 mm \|\| Lunghezza: 140.0 mm \|- \| Y: -40.0 mm \|\| Larghezza: 80.0 mm \|- \| Z: -85.0 mm \|\| Altezza: 30.0 mm \|- \|}

poi ritagliare il *Taglio di accoppiamento* dalla **Billetta Basamento** :

Rinominare il risultante oggetto *Cut* in **Basamento scavato**.

### Scavare l\'alloggiamento dell\'albero 

Il prossimo taglio è semi-circolare e serve per alloggiare nel basamento l\'albero a gomiti. Si inizia con un cilindro, però l\'orientamento predefinito del cilindro è verticale, mentre quì ne serve uno orizzontale. Questo significa che si deve capire come ruotare il cilindro per allinearlo correttamente con il motore. Guardando gli assi guida nell\'angolo in basso a destra della finestra 3D si vede che l\'albero motore deve essere collocato lungo l\'asse x positivo. Rispetto alla posizione iniziale è quindi necessario ruotare il cilindro di 90 gradi attorno ad un asse parallelo all\'asse y della scena. Questa operazione permette anche di capire quali parametri si devono inserire per il cilindro.

Creare un cilindro chiamato **Scavo per l\'albero** e attribuirgli le seguenti proprietà :

:   {\    class: wikitable border=1

\|- \| Axis X: 0.0 mm \|\| Angolo: 90.0 gradi \|- \| Axis Y: 1.0 mm \|\| \|- \| Axis Z: 0.0 mm \|\| \|- \| Position X: 0.0 mm \|\| Altezza: 140.0 mm \|- \| Position Y: 0.0 mm \|\| Raggio: 20.0 mm \|- \| Position Z: -55.0 mm \|\| \|- \|}

Asportare lo **Scavo per l\'albero** dal **Basamento scavato** e rinominare il risultante oggetto in **Basamento con alloggiamento**.



### Finire il basamento 

Infine si devono asportare 2 cubi, per consentire il passaggio delle bielle dal blocco motore all\'albero motore attraverso il basamento.

Creare due oggetti chiamati **Cubo intagliatore 1** e **Cubo intagliatore 2** con le seguenti proprietà:

:   {\    class: wikitable border=1

\|- \| X: 15.0 mm \|\| Lunghezza: 50.0 mm \|- \| Y: -25.0 mm \|\| Larghezza: 50.0 mm \|- \| Z: -55.0 mm \|\| Altezza: 55.0 mm \|- \|}

:   {\    class: wikitable border=1

\|- \| X: 75.0 mm \|\| Lunghezza: 50.0 mm \|- \| Y: -25.0 mm \|\| Larghezza: 50.0 mm \|- \| Z: -55.0 mm \|\| Altezza: 55.0 mm \|- \|}

!{width="300"}

Unire i due cubi in un oggetto chiamato *Cubi intagliatori*, poi asportare questo oggetto da *Basamento con alloggiamento*, chiamando *Carter* il risultato finale.

Ricordare, che è possibile nascondere il *Blocco Motore* selezionandolo e premendo la barra spaziatrice in modo da poter vedere meglio cosa si sta facendo, inoltre, e che è possibile duplicare *Cubo intagliatore 1* e cambiare solo la coordinata X per ottenere il *Cubo intagliatore 2*.

Il risultato finale dovrebbe essere simile alla figura di destra. Nella schermata la vista ad albero è completamente espansa e si vede la gerarchia delle operazioni booleane utilizzate per costruire il dispositivo. Ricordare che si può ancora intervenire nella vista albero e cambiare diametro al cilindro, modificare le dimensioni o la posizione dell\'albero a gomiti, ecc, senza dover ricostruire l\'intero modello da zero. Dal basamento si può ancora asportare altro materiale, ma per ora è sufficiente quanto fatto.

Il lavoro prosegue utilizzando la modalità di elaborazione 2D per progettare la sagoma della testata e ridurre il peso del blocco motore rimuovendo dalla billetta gran parte del materiale inutile che è ancora presente intorno ai cilindri.

## Disegno 2D della guarnizione di testa 

Per i fori dei bulloni della testa e per la forma del blocco motore sono usate in seguito varie operazioni booleane con cui \"asportare\" le parti del blocco che non servono. Ogni bullone della testa è fatto nello stesso modo, e attraversa tutto il monoblocco fino al carter, l\'unica differenza è la loro posizione alla sommità della testa. Questo significa che si può semplicemente \"disegnare\" la forma della guarnizione della testata sulla faccia superiore del motore, e poi utilizzarla anche come modello per eseguire i fori che si desiderano.

### Entrare in modalità Disegno 2D 

La prima cosa da fare è passare all\'ambiente di lavoro Disegno 2D, per fare questo dalla modalità Parte è possibile selezionare *Disegno 2D* nel menu a tendina in alto che attualmente riporta la voce *Parte*. Quando non si riesce a trovare la casella a discesa  è possibile selezionare un ambiente con **Visualizza , Ambienti**. Anche se il disegno da eseguire è un disegno 2D, si lavora nella finestra 3D dicendo a FreeCAD in quale piano deve proiettare i disegni. Quando si seleziona l\'ambiente Disegno 2D viene mostrata la barra degli strumenti di questo ambiente e nella parte destra immediatamente sopra della vista 3D vengono visualizzate varie icone. Per impostare il piano di lavoro  fare clic sul pulsante dell\'icona più a sinistra in cui è presente una delle seguenti voci {none, top, front, size o d}. Dopo aver cliccato su tale pulsante, sul lato sinistro della barra appaiono i comandi di selezione del piano composti da una casella di testo per inserire un offset, e altri 5 pulsanti: XY, XZ, YZ, Vista, e None. I primi tre sono la vista dall\'alto, la vista anteriore e la vista laterale. La voce Vista utilizza il piano perpendicolare alla direzione di visualizzazione . L\'ultimo  non proietta in un piano e permette di definire tutte le coordinate XYZ di ogni punto che si disegna. In questa esercitazione serve impostare un piano orizzontale scostato di 110  poi fare clic sul pulsante XY per proiettare il disegno sul piano XY, collocato a 110 millimetri sull\'asse Z e che corrisponde alla faccia superiore del blocco motore.

Ora che si è detto a FreeCAD in quale piano deve disegnare si può iniziare a progettare la guarnizione della testata.

Un\'ultima cosa da fare è impostare la visualizzazione 3D. Anche se tutti i disegni prodotti sono proiettati nel piano 2D precedentemente definito, si può osservare il piano in cui si disegna da qualsiasi angolazione . Poiché il piano di lavoro è quello complanare alla parte superiore del blocco motore, è bene impostare la vista 3D secondo tale piano, o almeno approssimativamente in quella direzione.

Premere il tasto 2 del tastierino numerico per attivare la vista dall\'alto . Con il motore in vista dall\'alto verso il basso, è possibile centrarlo nell\'area di lavoro trascinandolo con il pulsante centrale del mouse per spostare la vista.

Infine, la modalità Disegno 2D permette di agganciare  parti del disegno agli angoli del blocco motore, al centro dei cilindri, ecc. Per agevolare questi agganci, è utile nascondere il carter così i nuovi disegni si agganciano solo alla parte su si sta lavorando .

### Disposizione dei bulloni della testata 

Dopo che il corretto piano di proiezione e la visualizzazione sono impostati si aggiungono gli elementi di disegno 2D nello stesso modo usato per aggiungere le primitive.

Fare clic sul pulsante !{width="16"} *Cerchio* e muovere il mouse nella vista 3D.

A questo punto è necessario fornire a FreeCAD la posizione XY per il centro del cerchio, e il valore del raggio. In entrambi i casi è possibile inserire i dati con il mouse , oppure digitare i valori nelle caselle di immissione di testo che appaiono sopra la vista ad albero.

Proseguire aggiungendo un paio di cerchi casuali sulla parte superiore del motore, nonché alcuni non sul ​​motore, cioè appena fuori dall\'oggetto, nello spazio vuoto circostante la figura del motore. Dopo queste operazioni, ruotare la vista intorno alla parte superiore del blocco motore e osservare i cerchi disegnati, notare che essi sono \"appiattiti\" nel piano in cui sono proiettati e che le linee della faccia superiore del blocco motore sono anche esse in questo piano; questo sarà importante quando si andrà ad estrudere il disegno per modellare il motore. Ora che si sa come aggiungere gli elementi 2D è possibile eliminare i cerchi aggiunti per prova e poi iniziare a definire l\'aspetto effettivo della testata.

Attenzione, se il cerchio scompare all\'interno del blocco motore, significa che il piano di proiezione del disegno non è correttamente impostato in modalità XY e con offset 110 mm.

L\'aggiunta di elementi di disegno con il mouse è veloce e facile, ma non è molto precisa.

Per creare il modello del bullone, inizialmente si approfitta del fatto che muovendo il mouse si aggiornano i numeri nelle caselle di testo appena sopra la vista 3D e che questo permette di vedere le coordinate del punto in cui si vuole posizionare l\'elemento.

Ottenute queste coordinate approssimative si passa a digitare i reali valori che servono per un posizionamento di precisione.

Per aggiungere un cerchio, ripristinare la vista dall\'alto del motore, fare clic sul pulsante *Aggiungi cerchio*, e spostare il mouse in prossimità dell\'angolo in alto a sinistra del blocco motore in modo da occupare una posizione valida per la testa del bullone.

Pare che X = 10, Y = 30, sia una buona posizione per il cerchio .

Ora che si sa come determinare facilmente le coordinate degli elementi del disegno si può progettare un modello di bullone o altre forme 2D per ulteriori parti, quali i canali del circuito dei fluidi, scanalature, ecc. Per i primi 3 bulloni di un lato della testata usare le seguenti coordinate:

Notare che durante la digitazione dei valori nelle caselle si può premere Invio per passare alla casella successiva, inoltre è meglio spostare il mouse fuori dalla vista 3D prima di iniziare a digitare le coordinate in quanto il movimento del mouse può sovrascrivere i numeri che sono già stati inseriti nei campi di immissione di testo. Inoltre, su alcuni sistemi, per qualche motivo, ci sono problemi con la digitazione dei cerchi che hanno la loro coordinata Z impostata a 12.5, se succede questo, è possibile impostare il piano di proiezione del disegno su *Nessuno* e quindi immettere manualmente le coordinate Z che per i cerchi deve essere 110. Infine, durante la creazione dei cerchi, accertarsi di attivare la casella *Riempito* altrimenti quando essi si estrudono creano solo tubi e non cilindri solidi.

:   {\    class: wikitable border=1

\|- \| X1: 10 \|\| Y1: 25 \|\| Raggio: 2.5 mm \|- \| X2: 70 \|\| Y2: 25 \|\| Raggio: 2.5 mm \|- \| X3: 130 \|\| Y3: 25 \|\| Raggio: 2.5 mm \|}

Chiamare i cerchi **Bullone 1** **Bullone 2** e **Bullone 3**.

### L\'altro lato del Blocco 

Ora che i primi tre bulloni sono situati su un lato del motore, servono altri tre bulloni speculari sul lato opposto, ci sono tre modi per ottenere questo:

-   Si può continuare ad aggiungere cerchi come fatto per i primi tre e variare solo la coordinata Y in modo da posizionare i bulloni sul lato opposto del motore.

-   Si può selezionare i tre cerchi esistenti, andare in **Modifica , Duplica Selezione** e poi variare le coordinate Y dei tre nuovi cerchi.

-   Si può utilizzare la funzionalità di specchio dell\'Ambiente Part.

Dal momento che in questo esempio il primo e il secondo metodo sono già stati utilizzati, si sceglie la terza via. Ognuno dei tre metodi ha i suoi vantaggi e svantaggi, ma è buona regola utilizzare i primi due metodi con i modelli semplici , mentre con i modelli con molte duplicazione e/o con duplicazioni di forme/oggetti molto complicati si dovrebbe preferire il terzo metodo.

Quindi, anche se in questo caso è un po *esagerato*, gli altri bulloni sono realizzati riflettendo gli esistenti, per una dimostrazione.

Tornare in Ambiente Part tramite **Visualizza , Ambienti** .

Selezionare i tre cerchi dei bulloni nella vista ad albero, e quindi premere il pulsante !{width="16"} *Specchio*.

Quando si preme il pulsante specchio si dovrebbe vedere un nuovo pannello pop-up chiamato *Vista Combinata* nel pannello sotto la vista ad albero. Molti strumenti hanno bisogno di ulteriori input prima di poter eseguire le operazioni e la Vista Combinata consente di immettere questi parametri. È possibile ridimensionare il pannello della Vista combinata trascinando in sù o in giù la linea di divisione che lo separa dalle proprietà.

Selezionare **Bullone 1** nella lista della Vista combinata e impostare XZ per il *piano di riflessione*, quindi premere OK .

A questo punto del lavoro si dovrebbe avere un blocco motore con i cilindri forati e le posizioni dei bulloni segnate.

### Asportare il sovrametallo dalla billetta del blocco motore 

Ora che i fori per i bulloni della testata sono segnati  serve \"rifilare\" la parte esterna della billetta della bancata e dargli una forma migliore. Questo per rendere il motore più leggero, migliorare il raffreddamento e utilizzare meno materiale per la fusione del monoblocco. Come si è già fatto per il modello del bullone, ora si passa a creare un disegno 2D per definire la forma del prodotto finito. E\' possibile disegnare la curva spline direttamente con il mouse, oppure utilizzare l\'approccio ibrido adottato per i cerchi in cui si è usato il mouse per trovare delle coordinate approssimative e poi si sono fissati i valori effettivi voluti.

Però, un metodo più interessante è quello di utilizzare la *Modalità costruzione* del disegno 2D per tracciare alcune forme guida che aiutino a tracciare una bella e simmetrica curva spline agganciata a queste forme guida.

Come oggetti guida servono due poligoni regolari per ciascun cilindro, concentrici con il cilindro.

Per iniziare, passare alla vista dall\'alto del blocco motore, nascondere il carter, tornare all\'ambiente disegno 2D, selezionare il piano offset di riferimento a 110 mm e la modalità piano XY  poi fare clic sul pulsante *Modalità costruzione* nella barra dei comandi.

Il pulsante \'Modalità di costruzione\' si presenta come una spatola o cazzuola e si trova appena sopra l\'angolo superiore a destra della vista 3D. La Modalità costruzione funziona esattamente come la Modalità normale tranne che tutti gli oggetti di disegno 2D creati in modalità costruzione vengono tracciati in un colore diverso e sono automaticamente inseriti in un gruppo distinto della vista ad albero; questo permette di nascondere i disegni guida e lasciare visibili solo gli elementi reali, quali le marcature dei fori dei bulloni, e di nascondere il gruppo di costruzione, inoltre, permette anche di eliminare tutti gli oggetti guida eliminando solo il corrispondente gruppo.

:   *Ulteriori letture: Modalità Costruzione*

Ora che il piano di disegno è impostato correttamente e si è in Modalità costruzione, fare clic sul pulsante !{width="16"} *Poligono* e muovere il mouse lungo il bordo del cilindro sinistro tenendo premuto il tasto CTRL.

Notare che viene agganciato un punto nero, sul bordo o al centro del cilindro, secondo la posizione del mouse sulla circonferenza.

Spostarsi fino ad agganciare il punto nero centro del cilindro e fare clic sul pulsante sinistro del mouse. Questo pone il centro del poligono al centro del cilindro.

Ora, il programma richiede il numero di lati del poligono e il raggio in cui esso è inscritto.

Indagare un po\' con il mouse e verificare che un raggio di 30 è adatto  e immettere 14 per il numero di lati, ma questa volta lasciare l\'opzione *Riempito* deselezionata. Se non è possibile ottenere lo snap per agganciare il centro del cilindro  è sempre possibile inserire le coordinate manualmente .

Aggiungere un secondo poligono, anche lui centrato sul cilindro sinistro, ma questo con 22 lati e 45 mm di raggio.

Infine aggiungere gli stessi due poligoni sopra il cilindro di destra .

!{width="300"}

Al termine si dovrebbe avere due \"forme a 8\" che circondano i cilindri ed i bulloni della testa. Notare che, se il programma non richiede il numero di lati, si deve impostare solo il centro e il raggio e poi si deve modificare il numero di lati nella finestra delle proprietà.

Quando i poligoni di guida sono posizionati si può cominciare disegnare la curva spline che definisce la forma esterna del blocco motore. Dal momento che questa curva sarà parte dell\'oggetto finale è possibile disattivare la *Modalità costruzione* facendo clic sullo stesso pulsante premuto per attivarla.

Cliccare ora sul pulsante !{width="16"} *BSpline* e iniziare a disegnare la Polilinea con *CTRL + clic sinistro* in ogni luogo in cui si desidera aggiungere un punto di controllo per la curva spline.

E\' bene che il primo punto di controllo sia sul punto più a sinistra del poligono guida interno del cilindro sinistro.

Continuare ad aggiungere punti di controllo lungo tutta la curva spline fino a quando si fa clic sul punto precedente a quello in cui si è iniziato a disegnare, quindi fare clic sul pulsante *Chiudi* nel punto dove è stata digitata la posizione e il raggio per i cerchi 2D disegnati per i bulloni della testa.

Facendo clic sul pulsante Chiudi si finisce di disegnare i punti di controllo per la curva spline e si uniscono le estremità formando un contorno chiuso. E\' molto importante chiudere bene i contorni quando si prevede di estruderli in oggetti solidi come si farà in questo caso. Per ottenere invece curve spline aperte è sufficiente fare clic sul pulsante *Termina*, anziché che sul pulsante Chiudi, quando si è finito di disegnare.

A destra si può vedere come dovrebbe essere la curva spline prima di premere il pulsante *Chiudi* . Notare inoltre che la casella di controllo *Riempito* è attiva in modo che la curva spline risultante formi una lastra piena, piuttosto che un anello vuoto, questo serve per estrudere una forma solida delimitata alle estremità.


{{clear
---

# Engine Block Tutorial/it

 } 
<img alt="" src=images/_Engine_Block_Tutorial_-_Spline_Edit_Mode.png  style="width:300px;">

Nella precedente immagine, i punti di controllo non sono visibili quindi è stato aggiunto un secondo screenshot che mostra la spline finita in modalità di modifica (cliccare sul pulsante *Modifica* per attivare o disattivare la modifica dell\'oggetto selezionato, accertarsi di disattivarlo dopo le modifiche o semplicemente saltare questo passaggio se si è soddisfatti della forma del proprio blocco motore). Inoltre, notare che c\'è una discontinuità sul bordo più a sinistra della curva spline, anche se è chiusa bene, questo è un bug nel comportamento del programma che attualmente è corretto, come risultato la curva spline può essere leggermente diversa se si si esegue una versione più recente del software.



### Estrusione del disegno 2D nel modello 3D per completare il progetto 

Ora si è prossimi al disegno finale del motore.

Ritornare nell\'ambiente Parte e fare clic sul pulsante <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> *Estrudi Schizzo*.

Nella casella combinata che si apre, utilizzare *CTRL + Tasto sinistro* per selezionare i 6 bulloni della testa e la curva spline per l\'estrusione.

L\'estrusione di default avviene lungo l\'asse Z con direzione positiva, quì invece serve estrudere il disegno della testa *verso il basso*, nel blocco motore, lungo l\'asse Z in direzione negativa quindi, per la direzione, si deve impostare X = 0, Y = 0 e Z = -1, e digitare 110 per la lunghezza (l\'altezza del blocco motore). Dopo aver inserito tutti i valori, cliccare su OK e osservare che i cerchi dei bulloni vengono estrusi verso il basso formando dei cilindri e che la spline viene estrusa verso il basso producendo una sorta di cilindri dai bordi \"increspati\".

Selezionare e nascondere il **Blocco Forato** per rendere visibile l\'estrusione della spline, quindi nascondere questo oggetto in modo da poter vedere le estrusioni dei 6 cilindri dei bulloni di testa.

Come si può constatare, le forme 3D molto sofisticate si possono realizzare tramite l\'estrusione di un disegno 2D. Si potrebbero anche estrudere gli elementi del disegno con lunghezze diverse quindi, ad esempio, realizzare fori ciechi nel blocco e ricavare passaggi d\'acqua separati che vanno fino in fondo.

A questo punto tutti gli oggetti estrusi hanno come nome solo \"Extrude001 \...\" per cui è bene nominare ciascuno di loro in modo da poterli identificare nella sezione successiva (chiamarli ad esempio *Foro bullone di testa 1* fino a *Foro bullone di testa 6* e chiamare l\'estrusione della spline **Spline estrusa**).

Dopo l\'estrusione dei profili rimangono da eseguire solo poche operazioni booleane per produrre il progetto definitivo del blocco.

Espandere il progetto e visualizzare i componenti principali (il *Blocco forato* e il *Carter*) e tutti gli oggetti estrusi appena creati.

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:300px;">

Dato che gli oggetti 3D per i fori e per la forma esterna sono disponibili, si possono ora utilizzare alcune operazioni booleane per unire il tutto.

Selezionare le 6 estrusioni dei fori per i bulloni nella vista ad albero e unirle tra di loro con una operazione di fusione (a cui dare di conseguenza il nome **Fori per i bulloni della testa**).

Quindi selezionare il **Blocco forato** e i **Fori per i bulloni della testa** in questo ordine ed eseguire la foratura (come si è fatto per i fori dei cilindri), nominare il risultato del *Taglio* con **Blocco con fori dei bulloni**.

Infine, selezionare il **Blocco con fori dei bulloni** e la **Spline estrusa** poi premere il pulsante <img alt="" src=images/Part_Common.svg  style="width:16px;"> *Intersezione*, quindi nominare il risultato **Blocco motore**.

L\'oggetto finale dovrebbe essere simile a quello dell\'immagine di destra.


{{clear}}



---
⏵ [documentation index](../README.md) > Engine Block Tutorial/it
