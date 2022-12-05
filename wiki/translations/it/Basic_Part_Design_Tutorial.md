---
- TutorialInfo:/it   Topic:Modellazione   Level:Base   Author:HarryGeier ([[User:HarryGeier   HarryGeier]])|Time:Circa un'ora   FCVersion:0.17 o superiore   Files:[https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd Basic Part Design for v0.17]
---

# Basic Part Design Tutorial/it




<div class="mw-translate-fuzzy">




</div>


<div class="mw-translate-fuzzy">

Questo tutorial presenta ai nuovi utenti alcuni degli strumenti e delle tecniche utilizzate nell\'ambiente [ Part Design](PartDesign_Workbench/it.md) v0.17. Non è una guida completa ed esaustiva all\'ambiente Part Design, molti strumenti e molte capacità non sono utilizzate. Questo tutorial guida l\'utente attraverso i passi necessari per modellare la parte mostrata nell\'immagine sottostante utilizzando degli schizzi.


</div>

![](images/Tut17_final_refined.png )

Il video dell\'intera costruzione è disponibile in: <https://youtu.be/geIrH1cOCzc>


<div class="mw-translate-fuzzy">

(sotto sono riportate le schermate di ogni sezione)


</div>

## Prima di iniziare 

## The Task 


<div class="mw-translate-fuzzy">

## Lo scopo 

In questa esercitazione, si prevede di utilizzare l\'ambiente Part Design per creare un modello solido 3D della parte mostrata nel [Disegno](Drawing_Workbench/it.md) sottostante. Sono fornite tutte le dimensioni necessarie per portare a termine questo compito. Si inizierà creando il nucleo della forma da uno schizzo di base e poi si costruirà sulla forma aggiungendo ad essa ciò che è conosciuto come funzioni (Features). Le funzioni aggiungono del materiale, o rimuovono del materiale dal pieno mediante l\'uso di disegni supplementari accompagnati dalle operazioni delle funzioni. Questo tutorial non utilizza tutte le funzioni e gli strumenti disponibili nell\'ambiente Part Design, ma ne utilizza a sufficienza per dare agli utenti di questo tutorial le basi su cui costruire le loro conoscenze e competenze.


</div>

## La Parte 

![](images/Tutorial_Drawing_Sheet.png )

## Constructing The Part 

### Startup


<div class="mw-translate-fuzzy">

## Costruzione della Parte 

### Inizio

Prima di iniziare accertarsi di essere nell\'ambiente Part Design. Fatto questo, creare un nuovo documento, se non è ancora stato fatto. Dato che salvare spesso il proprio lavoro è una buona abitudine, per prima cosa salvare il documento dandogli il nome preferito.


</div>


<div class="mw-translate-fuzzy">

Tutti i lavori in Part Design iniziano con un [Corpo](Glossary#Body.md). Quindi costruiremo il solido all\'interno del corpo iniziando con uno [schizzo](Glossary#Sketch.md).

1.  Cliccare su <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Crea un nuovo corpo](PartDesign_Body/it.md) per creare e attivare un nuovo corpo contenitore. 
*Nota: questo passaggio può essere omesso. Quando si crea uno schizzo, se non viene trovato alcun corpo esistente, ne viene automaticamente creato e attivato uno nuovo.*
2.  Cliccare su <img alt="" src=images/PartDesign_NewSketch.svg  style="width:32px;"> [Crea nuovo schizzo](PartDesign_NewSketch/it.md). Questo crea lo schizzo all\'interno del corpo appena creato.
3.  Dobbiamo definire dove deve essere allegato lo schizzo. Lo collegheremo ad un piano dell\'[Origine](Glossary#Origin.md) del Corpo.
4.  Nella scheda Azioni dalla Vista combinata, selezionare **Piano YZ** nell\'elenco e poi premere **OK**:


</div>

1.  Click on <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Create new body](PartDesign_Body.md) to create and activate a new Body Container. 
*Note: this step can be omitted. When creating a sketch, if no existing Body is found, a new one will be automatically created and activated.*
2.  Click on <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create new sketch](PartDesign_NewSketch.md). This will create the sketch within the just created body.
3.  We need to define where the sketch will be attached. We will attach it to a plane from the Body´s [Origin](Glossary#Origin.md).
4.  In the [Tasks tab](Task_panel.md) from the [Combo view](Combo_view.md), select **YZ_Plane** in the list and press **OK**:

<img alt="" src=images/Tut17_sketchplanes.png  style="width:250px;">


<div class="mw-translate-fuzzy">

*Nota: se il pannello laterale non è sufficientemente largo è possibile che il pulsante OK non sia visibile. Per renderlo più ampio trascinare il bordo destro. Posizionare il puntatore del mouse sul bordo; quando il puntatore si trasforma in una freccia bidirezionale, tenere premuto il tasto sinistro del mouse e trascinare.*


</div>


<div class="mw-translate-fuzzy">

Dopo aver fatto clic su OK, FreeCAD passa automaticamente all\'ambiente [Sketcher](Sketcher_Workbench/it.md) e apre lo schizzo in modalità di modifica:


</div>

![](images/Tut17_sketcherempty.png )

### Create the sketch 


<div class="mw-translate-fuzzy">

### Creare lo schizzo 

Per procedere, utilizzare lo strumento <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilinea](Sketcher_CreatePolyline/it.md) e fare una forma simile a quella dell\'immagine successiva. Non è necessario che sia perfetta, in quanto, dopo averla costruita, si applicheranno i vincoli. Dopo aver prodotto la forma di base, si passa ad applicare i vincoli. Se la casella *Autovincoli* era impostata su ON, alcuni di loro saranno già stati applicati automaticamente, in caso contrario, procedere come segue. Prima però assicurarsi di aver chiuso lo strumento polilinea cliccando con il tasto destro o premendo ** Esc** due volte; il cursore del mouse dovrebbe tornare da mirino a freccia standard. Non premere **Esc** una terza volta o si esce dalla modalità di modifica dello schizzo, se ciò accade, fare clic sulla scheda Modello, quindi fare doppio clic sull\'elemento Schizzo nell\'albero o fare clic con il pulsante destro del mouse e selezionare **Modifica schizzo** nel menu contestuale.


</div>

*NOTE: Since this tutorial was written there have been improvements to the sketcher solver, if it detects a redundant constraint it will turn the sketch orange in colour, and before further constraints are added, the redundant constraint should be removed. (The redundant constraint is shown in the Task view, click on the blue reference and press delete.)*


<div class="mw-translate-fuzzy">

1.  Selezionare le due linee orizzontali con il mouse facendo clic su di esse e, una volta selezionate, fare clic su <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> vincolo orizzontale.
2.  Selezionare la linea verticale sulla destra e poi cliccare su <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;">vincolo verticale.
3.  Selezionare i punti di inizio e fine della polilinea e poi fare clic su <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> vincolo coincidente per chiudere la polilinea.
4.  Selezionare la linea orizzontale inferiore e la linea verticale destra e applicare un <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> vincolo uguaglianza.
5.  Selezionare entrambe le linee orizzontali o verticali e applicare il corrispondente vincolo di lunghezza <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:32px;"> orizzontale o <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:32px;"> verticale e dargli un valore 26 mm.
6.  Selezionare la linea orizzontale superiore e applicare il vincolo di lunghezza orizzontale e assegnargli il valore 5 mm
7.  Seleziona il punto in basso a destra, (vertice) della linea orizzontale Origine e poi il punto centrale della griglia e applicare il <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> vincolo di coincidenza per bloccare la forma.


</div>

A questo punto si dovrebbe avere un disegno completamente vincolato, come indicato dal cambio di colore e dal messaggio mostrato nella Vista Combinata. Lo schizzo dovrebbe apparire esattamente come nell\'immagine sottostante.

![](images/Tut17B_profile.png )


<div class="mw-translate-fuzzy">

Ora, nella Vista Combinata, cliccare sul pulsante Close per uscire dalla modalità di modifica schizzo e selezionare <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> *Prisma* (Pad) dalla barra degli strumenti o dal menu di Part Design. Questo apre la finestra di dialogo per Pad nella Vista Combinata. Aprire il menu a discesa di tale finestra e selezionare *due dimensioni*. Come si può vedere nel disegno presentato all\'inizio di questo tutorial la parte è lunga 53 mm. Ora, quello che vogliamo fare è estrudere lo schizzo in entrambe le direzioni simmetricamente dal centro del piano per coprire tale distanza. Il motivo di questo diventerà evidente più avanti. Per ora, dato che vogliamo che in totale sia lungo 53 mm inserire 26,5 per la *lunghezza* e di nuovo 26,5 per la *seconda lunghezza*. In alternativa, si può fornire una sola lunghezza di 53 mm e attivare la casella *Simmetrico al piano*. Fatto questo, abbiamo prodotto la base solida a cui aggiungere le funzioni aggiuntive per costruire la Parte.


</div>

Il video dei passaggi utilizzati in questa parte del tutorial è in: <https://youtu.be/cUyPnCMeTgg>

### Features with pocket and external geometry 


<div class="mw-translate-fuzzy">

### Funzioni con Tasca e Geometria esterna 

Utilizzando il mouse, o con le icone di visualizzazione, ruotare il modello in modo da poter vedere la sua faccia posteriore. Quando la faccia posteriore della Parte è visibile, selezionarla cliccando su di essa, come si vede nell\'immagine successiva.


</div>

![](images/PD_WB_Tutorial003.png )


<div class="mw-translate-fuzzy">

Dopo aver selezionato la faccia, fare clic sull\'icona Nuovo schizzo nella barra degli strumenti o dal menu Part Design per mappare il prossimo schizzo sulla faccia posteriore della Parte. Poi selezionare lo strumento <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> rettangolo e posizionare un rettangolo sulla faccia posteriore della parte in modo simile a come mostrato di seguito. Infine, seguendo i passaggi elencati, vincolare lo schizzo.


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare una delle linee orizzontali e applicare un vincolo distanza orizzontale 5 mm.
2.  Selezionare una delle linee verticali e applicare un vincolo distanza verticale 11 mm.
3.  Selezionare lo strumento <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> *Geometria esterna*,
4.  Selezionare il vertice in alto a destra della faccia e cliccare su di esso per dotare lo schizzo di un punto di una geometria esterna a cui collegarlo.


</div>

![](images/tut17_slot_unconstrained.png )


<div class="mw-translate-fuzzy">

1.  Fare clic con il tasto destro per terminare la modalità geometria esterna
2.  Selezionare il punto appena reso disponibile con lo strumento Geometria esterna, quindi selezionare il vertice in alto a destra del rettangolo e fare clic sul vincolo coincidente. A questo punto il disegno dovrebbe essere completamente vincolato e apparire come nell\'immagine successiva.


</div>

![](images/tut17_slote_constrained.png )


<div class="mw-translate-fuzzy">

Fatto questo, cliccare sul pulsante Chiudi nella parte superiore della scheda Azioni della Vista combinata, quindi selezionare lo strumento <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> *Tasca* (Pocket) dalla barra degli strumenti o nel menu di Part Design. Questo strumento fa l\'opposto dello strumento Pad. Così come lo strumento Pad aggiunge del materiale alla Parte, lo strumento Tasca rimuove il materiale dal pezzo. Entrambe le operazioni sono chiamate funzioni (features). Per questa operazione Tasca selezionare il tipo *Attraversa tutto* dal menu a tendina e quindi fare clic sul pulsante OK.


</div>


<div class="mw-translate-fuzzy">

Per l\'operazione successiva, assicurarsi che \"Pocket\" sia selezionato nella vista ad albero del modello, poi cliccare sulla funzione <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> *Specchio* sulla barra degli strumenti o dal menu Part Design. Nella finestra di dialogo Specchio della Vista Combinata, selezionare *asse orizzontale dello schizzo* dal menu a tendina di *Piano*. Quindi fare clic su OK. In questo modo la funzione Specchio funziona perché, durante la prima operazione fatta con lo schizzo base, la funzione di base del nostro modello è stata estrusa in entrambe le direzioni del piano orizzontale. Se tutto è andato bene e dopo averla ruotata, ora si dovrebbe avere una Parte che si presenta come l\'immagine sottostante.


</div>

![](images/tut17_profilewithslots.png )

Il video dei passaggi utilizzati in questa parte del tutorial è in: <https://youtu.be/wiGXV9G7mrM>

### Features with pad and external geometry 


<div class="mw-translate-fuzzy">

### Funzioni con Pad e geometria esterna 

Dopo aver dato un\'occhiata, ruotare nuovamente la parte e selezionare ancora la faccia posteriore per mappare il prossimo Schizzo.


</div>

![](images/tut17_profilewithslotsrearplane.png )

Selezionare Nuovo schizzo e fare un nuovo rettangolo in modo simile a quanto illustrato nella prossima immagine. Quindi procedere aggiungendo al rettangolo i vincoli dimensionali.

1.  Selezionare una linea orizzontale e applicare un vincolo distanza orizzontale con il valore 16.7.
2.  Selezionare una linea verticale e applicare un vincolo distanza verticale di 7 mm
3.  Utilizzando lo strumento Geometria esterna, selezionare il vertice superiore sinistro della faccia della parte.

![](images/tut17_sidblockunconstrained.png )

Ora selezionare il vertice superiore sinistro del rettangolo e il punto geometria esterna, poi fare clic sul vincolo coincidente per vincolare completamente lo schizzo.

![](images/tut17_sideblockconstraind.png )

Chiudere Sketcher.

Procedere cliccando sulla funzione Pad e nella finestra di dialogo Pad della Vista combinata impostare la lunghezza 26 mm, lasciando il tipo *Quota* e spuntando la casella di controllo *Invertita*. Utilizzando la casella di controllo invertita si fa sì che il Pad vada dentro la Parte invece di uscire da essa. Questa operazione fornisce il seguente risultato.

![](images/tut17_sideblock.png )

Utilizzare nuovamente la funzione Specchio per creare il secondo pad, ma prima assicurarsi che nella vista ad albero sia selezionato il Pad creato in precedenza, quindi fare clic su Specchio nella barra degli strumenti o selezionare l\'operazione dal menu di Part Design. Ripetere l\'operazione fatta prima per Tasca e selezionare *Asse orizzontale dello schizzo* dal menu a tendina di Piano.

![](images/tut17_profilewithsideblocks.png )

Il video dei passaggi utilizzati in questa parte del tutorial è in: <https://youtu.be/Ido1owp8ubc>

### Feature with pocket and external geometry 


<div class="mw-translate-fuzzy">

### Funzioni con Cavità e Geometria esterna 

A questo punto ruotando la Parte dalla parte anteriore, possiamo vedere che la Parte comincia ad essere simile alla Parte mostrata nel disegno quotato all\'inizio di questo tutorial. Quando la parte anteriore è visibile, fare clic con il mouse sulla faccia inclinata per selezionare la faccia da usare per il prossimo schizzo.


</div>

![](images/tut17_innerplane.png )


<div class="mw-translate-fuzzy">

Ora usare lo strumento rettangolo per posizionare un rettangolo nello schizzo e poi applicare i seguenti vincoli.


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare una linea orizzontale e una linea verticale, e dopo che entrambe sono selezionate, fare clic sul vincolo *uguaglianza*.
2.  Selezionare una linea orizzontale o verticale e applicare a entrambe il corrispondente vincolo lunghezza orizzontale o verticale con il valore 17 mm
3.  Utilizzando lo strumento Geometria esterna, selezionare il vertice in alto a destra, come mostrato nell\'immagine seguente.


</div>

![](images/tut17_rechtangleholeunconstrained.png )

Ora, utilizzando le dimensioni del disegno, applicare i seguenti vincoli.

1.  Selezionare il punto geometria esterna e il vertice in alto a destra dell\'attuale schizzo e applicare il vincolo distanza orizzontale di 7 mm
2.  Selezionare il punto geometria esterna e il vertice in alto a destra dell\'attuale schizzo e applicare il vincolo distanza verticale di 11 mm

Il risultato dovrebbe essere il seguente.

![](images/tut17_rectangleholeconstrained.png )

A questo punto *scavando* (Pocket) semplicemente questo schizzo, il foro risultante sarebbe perpendicolare al lato inclinato su cui è mappato, ma questo non è quello che vogliamo ottenere.

![](images/tut17_wrongplaneforpocket.png )

Vogliamo che il foro sia perpendicolare alla faccia posteriore, ma le dimensioni delle sue proiezioni non hanno le dimensioni 17 mm x 17 mm che sono quelle date nel disegno. Si possono fare due conti per calcolare le dimensioni necessarie, oppure si possono utilizzare gli strumenti forniti in FreeCAD per farsi fare questa proiezione.

Il video dei passaggi utilizzati in questa parte del tutorial è in: <https://youtu.be/x4d5nZPWCLQ>


<div class="mw-translate-fuzzy">

Per creare una tasca che abbia il rettangolo inclinato sulla faccia in uscita, si può disegnare un nuovo rettangolo sul retro, e usare la proiezione del rettangolo inclinato come riferimento esterno. Quindi ruotare di nuovo il solido per rendere visibile la faccia posteriore del pezzo e selezionarla per mappare su di essa lo schizzo definitivo.


</div>

![](images/tut17_profilewithsideblocksrearplane.png )


<div class="mw-translate-fuzzy">

Selezionare **Nuovo schizzo** <img alt="" src=images/PartDesign_NewSketch.svg  style="width:32px;"> nella barra degli strumenti o nel menu di Part Design. Ora, in modalità di modifica degli schizzi, il rettangolo dello schizzo inclinato non è visibile. Per renderlo selezionabile, passare dalla vista combinata alla scheda del modello e selezionare l\'ultimo schizzo realizzato sul piano inclinato (Sketch003), poi usare la barra spaziatrice per renderlo visibile. Quindi, selezionare la funzione specchio precedente (mirrored001) e usando ancora la barra spaziatrice, nasconderla. Ora si dovrebbe vedere il rettangolo inclinato all\'interno della vista 3D. È possibile continuare a lavorare con la scheda del modello visibile o tornare alla scheda delle azioni. Utilizzando lo strumento <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> Geometria esterna, nel rettangolo inclinato selezionare il bordo orizzontale superiore e il bordo orizzontale inferiore del rettangolo inclinato. Quindi, aggiungere un nuovo rettangolo allo schizzo utilizzando lo strumento rettangolo <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;">.


</div>

![](images/tut17_rectangleunconstrained.png )

1.  Selezionare il vertice superiore sinistro del nuovo rettangolo e il punto in alto a sinistra della geometria esterna poi fare clic sul vincolo coincidente.
2.  Fare clic sul vertice in basso a destra del nuovo rettangolo e il punto in basso a destra della geometria esterna poi fare clic sul vincolo coincidente.

E con questo dovremmo finire.

![](images/tut17_rectangleconstrained.png )


<div class="mw-translate-fuzzy">

Per concludere questo tutorial, chiudere la finestra di sketch usando *Chiudi* o *Esci dalla modifica* dal menu di scelta rapida dello sketch004. Quindi selezionare la funzione <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> Pocket dalla barra degli strumenti o dal menu Part Design. Dal menu a discesa Tipo selezionare **Attraverso tutto** e fare clic sul pulsante OK.


</div>

![](images/Tut17_final.png )

A questo punto, sono visibili alcune linee che provengono dalle funzioni intersecanti precedenti. In questo caso il *blocco laterale* interseca il *profilo base* facendolo apparire come un blocco triangolare sopra al profilo (cioè, c\'è una linea extra visibile nell\'immagine sopra sul lato destro del modello). Per rimuovere queste linee, si può attivare \"Affina forma\" nelle impostazioni di Part Design o, per mantenere una discreta velocità di elaborazione, ma avere queste linee mentre si costruisce, attivare l\'affinazione individualmente per ciascuna funzione che crea tali linee. L\'impostazione della funzione può essere eseguita nella scheda \"Dati\" della funzione. Impostare la [**proprietà *refine***](Property_editor/it#Dati.md) su TRUE per la funzione pocket Pocket001 per invocare l\'affinamento.

![](images/Tut17_refine.png ) ![](images/Tut17_final_refined.png )

Il video dei passaggi utilizzati in questa parte del tutorial è in: <https://youtu.be/UYI0gvxCYeI>

Questo tutorial e il vostro modello sono terminati.

## Risorse aggiuntive 

-   File di FreeCAD per il confronto (fatto con 0.17) [Download](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd)


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Basic Part Design Tutorial/it
