# <img alt="L\'icona dell\'ambiente Sketcher" src=images/Workbench_Sketcher.svg  style="width   *64px;"> Sketcher Workbench/it


{{TOCright}}

## Introduzione

L\'ambiente <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Sketcher](Sketcher_Workbench/it.md) di FreeCAD serve a creare delle geometrie 2D destinate ad essere utilizzate negli ambienti <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Ambiente DisegnoPezzo](PartDesign_Workbench/it.md), <img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> [Architettura](Arch_Workbench/it.md) o altri ambienti. In genere, un disegno 2D è il punto di partenza per la maggior parte dei modelli CAD. Un semplice schizzo 2D può essere \"estruso\" per creare una forma 3D; successivamente degli schizzi 2D possono essere usati per creare altre funzioni quali tasche, o estrusioni sulla superficie dell\'oggetto 3D precedentemente costruito. Insieme alle operazioni booleane definite nell\'<img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Ambiente Parte](Part_Workbench/it.md), lo Sketcher costituisce la base del metodo [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG) per la costruzione di solidi. Inoltre, insieme alle operazioni dell\'ambiente <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Ambiente DisegnoPezzo](PartDesign_Workbench/it.md), lo Sketcher costituisce anche la base della metodologia per la creazione di solidi nota come [Editazione delle funzioni](feature_editing/it.md).

L\'ambiente Sketcher mette a disposizione i **vincoli**. Consente di vincolare le forme 2D a precise definizioni geometriche in termini di lunghezza, angoli e relazioni (orizzontalità, verticalità, perpendicolarità, ecc.).
Un solutore dei vincoli calcola la quantità di vincoli applicati alla geometria 2D e permette l\'esplorazione interattiva dei gradi di libertà dello schizzo.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width   *450px;"> 
*Uno schizzo base, completamente vincolato‎.*

## Nozioni di base sugli schizzi vincolati 

Per spiegare come funziona il modulo Sketcher, è utile fare un confronto con il **modo tradizionale** di disegnare.

##### Disegno tradizionale 

Il modo tradizionale di disegno CAD è derivato dal vecchio [tavolo da disegno](http   *//en.wikipedia.org/wiki/Drawing_board).
[Le viste ortogonali 2D](http   *//en.wikipedia.org/wiki/Multiview_orthographic_projection) sono disegnate manualmente e finalizzate alla produzione di disegni tecnici (noti anche come dettagli o particolari). Gli oggetti sono disegnati esattamente con le loro forme, misure o dimensioni previste. Per tracciare una linea orizzontale lunga 100 mm a partire dal punto (0,0), si attiva lo strumento linea, si fa clic sullo schermo o si inserisce le coordinate (0,0) per il primo punto, poi si fa un secondo clic o si inserisce il secondo punto di coordinate (100,0). Oppure, si costruisce una linea base senza riguardo alla sua posizione e in seguito la si sposta. Dopo aver disegnato le geometrie si aggiungono le dimensioni.

#### Schizzo vincolato 

Lo strumento Sketcher si allontana da questa logica. Non è più necessario disegnare gli oggetti esattamente come sono desiderati, perché è possibile ridefinirli in seguito tramite i vincoli. È possibile disegnare liberamente gli oggetti e dopo, fintanto che non vengono vincolati, modificarli. Sostanzialmente, essi sono **flottanti**, quindi si possono spostare, allungare, scalare, e così via. Questo permette una grande flessibilità nel processo di progettazione.

#### Cosa sono i vincoli? 

Invece delle dimensioni, i vincoli vengono utilizzati per limitare i gradi di libertà di un oggetto. Ad esempio, una linea senza vincoli ha 4 gradi di libertà (DOF Degrees Of Freedom)   * essa può essere spostata orizzontalmente o verticalmente, può essere allungata, e può essere ruotata.

Applicando a una linea un vincolo orizzontale o verticale, oppure un vincolo angolare (rispetto ad un\'altra linea o ad uno degli assi) si limita la sua capacità di ruotare, lasciandola quindi con solo 2 gradi di libertà. Bloccando uno dei suoi punti rispetto all\'origine si rimuove un ulteriore grado di libertà. Applicando un vincolo dimensionale si rimuove l\'ultimo grado di libertà. A questo punto, la linea è quindi considerata **completamente vincolata**.

Più oggetti possono essere vincolati tra di loro. Due linee possono essere unite attraverso uno dei loro punti con il vincolo punto coincidente. Tra due linee si può impostare un angolo, oppure impostarle perpendicolari. Una linea può essere tangente ad un arco o a un cerchio, e così via. Per vincolare uno schizzo complesso, con più oggetti, sono possibili diverse soluzioni, e renderlo **completamente vincolato** significa che almeno una di queste è stato raggiunta in base ai vincoli applicati.

Ci sono due tipi di vincoli   * geometrici e dimensionali. Essi sono descritti nella successiva sezione dedicata agli [\'Strumenti\'](#Strumenti.md).

#### Per che cosa l\'Ambiente Sketcher non va bene 

Il modulo Sketcher non è pensato per produrre disegni dettagliati in 2D. Dopo che gli schizzi sono stati utilizzati per generare una forma solida vengono automaticamente nascosti. I vincoli (la quotatura dei vincoli e i segni grafici di vincolo) sono visibili solo in modalità **Modifica sketch**.

Se serve solo produrre delle viste 2D per la stampa e non si intende creare dei modelli 3D, si può utilizzare l\'ambiente [Draft](Draft_Workbench/it.md). A differenza degli elementi di Sketcher, gli oggetti di Draft non usano i vincoli, ma sono forme semplici definite al momento della creazione. Sia Draft che Sketcher possono essere utilizzati per il disegno di geometrie 2D e la creazione di solidi 3D, sebbene il loro uso previsto sia diverso. Sketcher viene normalmente utilizzato insieme a [Part](Part_Workbench/it.md) e [PartDesign](PartDesign_Workbench/it.md) per creare solidi. Draft viene normalmente utilizzato per semplici disegni planari su una griglia, come quando si disegna una pianta architettonica, quindi Draft viene utilizzato principalmente con [Arch](Arch_Workbench/it.md). Lo strumento [Da Draft a Schizzo](Draft_Draft2Sketch/it.md) converte un oggetto Draft in un oggetto Sketch e viceversa. Molti strumenti che richiedono un elemento 2D come input funzionano con entrambi i tipi di oggetto poiché viene eseguita automaticamente una conversione interna.

## Flusso di lavoro per gli schizzi 

Uno Sketch è sempre in 2 dimensioni (2D). Per creare un solido, viene creato prima lo schizzo 2D di una singola area chiusa e poi essa viene estrusa o rivoluzionata per aggiungere la terza dimensione, creando un solido 3D dallo schizzo 2D.

Se lo schizzo contiene dei segmenti che si intersecano, punti non collocati esattamente su un segmento, o punti finali di segmenti adiacenti che non sono coincidenti, l\'operazione di Pad o di Rivoluzione non crea un solido. A volte uno schizzo che contiene linee che si intersecano può funzionare per un\'operazione semplice come un Pad, ma le operazioni successive falliscono. È meglio evitare di attraversare le linee. Come eccezione, questa regola non si applica alla geometria di costruzione (linee blu).

All\'interno dell\'area racchiusa si possono avere delle piccole aree non sovrapposte. Queste diverranno dei \"vuoti\" quando si crea il solido 3D.

Quando uno schizzo è completamente vincolato, le funzioni dello schizzo diventano verdi. La geometria di costruzione rimane blu. Di solito a questo punto lo schizzo è \"finito\" e adatto per l\'uso nella creazione di un solido 3D. Tuttavia, una volta chiusa la finestra di dialogo Schizzo, può essere utile andare in <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> [Ambiente Part](Part_Workbench/it.md) ed eseguire <img alt="" src=images/Part_CheckGeometry.svg  style="width   *16px;"> [Controlla la geometria](Part_CheckGeometry/it.md) per assicurarsi che nello schizzo non ci siano funzioni che possono causare problemi successivi.

## Strumenti

Gli strumenti dell\'Ambiente Sketcher si trovano nel menu che appare quando si carica questo ambiente.

### Generale

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> [Nuovo schizzo](Sketcher_NewSketch/it.md)   * Crea un nuovo schizzo su una faccia selezionata o in un piano. Se non si esegue nessuna selezione, di default, viene utilizzato il piano XY.

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width   *32px;"> [Edita schizzo](Sketcher_EditSketch/it.md)   * Modifica lo schizzo selezionato. Apre la finestra [Dialogo di Sketcher](Sketcher_Dialog/it.md)

-   <img alt="" src=images/Sketcher_LeaveSketch.svg‎‎  style="width   *32px;"> [Esci](Sketcher_LeaveSketch/it.md)   * Termina la modalità di modifica dello schizzo.

-   <img alt="" src=images/Sketcher_ViewSketch.svg‎‎‎  style="width   *32px;"> [Vista schizzo](Sketcher_ViewSketch/it.md)   * Imposta la vista del modello in modo perpendicolare al piano dello schizzo.

-   <img alt="" src=images/Sketcher_ViewSection.svg‎‎  style="width   *32px;"> [Vista sezione](Sketcher_ViewSection/it.md)   * Crea un piano di sezione che nasconde temporaneamente qualsiasi materia davanti al piano dello schizzo.

-   <img alt="" src=images/Sketcher_MapSketch.svg‎‎‎  style="width   *32px;"> [Mappa schizzo su faccia](Sketcher_MapSketch/it.md)   * Mappa uno schizzo sulla faccia di un solido selezionata in precedenza.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width   *32px;"> [Riposiziona lo schizzo](Sketcher_ReorientSketch/it.md)   * Permette di modificare la posizione di uno schizzo

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width   *32px;"> [Convalida lo schizzo](Sketcher_ValidateSketch/it.md)   * controlla se nell\'area di tolleranza ci sono dei punti distinti e li fa coincidere.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width   *32px;"> [Unisci schizzi](Sketcher_MergeSketches/it.md)   * Unisce due o più schizzi.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎‎‎  style="width   *32px;"> [Rifletti schizzo](Sketcher_MirrorSketch/it.md)   * Riflette uno schizzo rispetto all\'asse verticale, o all\'asse orizzontale e all\'origine.

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width   *32px;"> [Ferma operazione](Sketcher_StopOperation/it.md)   * Quando è in modalità di modifica, ferma l\'operazione corrente, sia che si tratti di disegnare, impostare vincoli, ecc.

### Geometrie

Gli strumenti per creare gli oggetti.

-   <img alt="" src=images/Sketcher_CreatePoint.svg‎‎  style="width   *32px;"> [Punto](Sketcher_CreatePoint/it.md)   * Disegna un punto.

-   <img alt="" src=images/Sketcher_CreateLine.svg‎‎  style="width   *32px;"> [Linea tra due punti](Sketcher_CreateLine/it.md)   * Disegna un segmento delimitato da due punti. Per quanto riguarda alcuni vincoli le linee sono infinite.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width   *48px;"> [Archi](Sketcher_CompCreateArc/it.md)   * Questo è un menu icona nella barra degli strumenti di Sketcher che contiene i seguenti comandi   *

   ** <img alt="" src=images/Sketcher_CreateArc.svg‎‎  style="width   *32px;"> [Arco](Sketcher_CreateArc/it.md)   * Disegna un arco di circonferenza specificando il centro, il raggio, l\'angolo iniziale e l\'angolo finale.

   ** <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width   *32px;"> [Arco da tre punti](Sketcher_Create3PointArc/it.md)   * Disegna un arco da due punti finali e un punto della circonferenza.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width   *48px;"> [Cerchi](Sketcher_CompCreateCircle/it.md)   * Questo è un menu icona nella barra degli strumenti Sketcher che contiene i seguenti comandi   *

   ** <img alt="" src=images/Sketcher_CreateCircle.svg  style="width   *32px;"> [Circonferenza](Sketcher_CreateCircle/it.md)   * Disegna una circonferenza prendendo in input il centro e il raggio.

   **<img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width   *32px;"> [Circonferenza da tre punti](Sketcher_Create3PointCircle/it.md)    * Disegna un cerchio da tre punti sulla circonferenza.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width   *48px;"> [Sezioni di coni](Sketcher_CompCreateConic/it.md)   * L\'ambiente Schizzo fornisce le seguenti sezioni coniche. A differenza delle B-spline, possono essere usate con tutti i tipi di vincoli come [tangenti](Sketcher_ConstrainTangent/it.md), [punti](Sketcher_ConstrainPointOnObject/it.md), o [perpendicolari](Sketcher_ConstrainPerpendicular/it.md).

   ** <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width   *32px;"> [Ellisse](Sketcher_CreateEllipseByCenter/it.md)   * Disegna un\'ellisse dal centro, raggio maggiore e raggio minore.

   ** <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width   *32px;"> [Ellisse da tre punti](Sketcher_CreateEllipseBy3Points/it.md)   * Disegna una ellisse da due punti del raggio maggiore e un punto del raggio minore.

   ** <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width   *32px;"> [Arco di ellisse](Sketcher_CreateArcOfEllipse/it.md)   * Disegna un arco di ellisse dal punto centrale, un punto del raggio maggiore, il punto iniziale e il punto finale.

   **<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width   *32px;"> [Arco di iperbole](Sketcher_CreateArcOfHyperbola/it.md)   * Disegna un arco di iperbole.

   **<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width   *32px;"> [Arco di parabola](Sketcher_CreateArcOfParabola/it.md)   * Disegna un arco di parabola.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width   *48px;"> [Crea una B-spline](Sketcher_CompCreateBSpline/it.md)   * Questo è un menu icona nella barra degli strumenti Sketcher che contiene i seguenti comandi   *

   ** <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width   *32px;"> [B-spline](Sketcher_CreateBSpline/it.md)    * Disegna una curva B-spline dai suoi punti di controllo.

   ** <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width   *32px;"> [B-spline Periodica](Sketcher_CreatePeriodicBSpline/it.md)    * Disegna una curva B-spline periodica (chiusa) dai suoi punti di controllo.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width   *32px;"> [Polilinea ](Sketcher_CreatePolyline/it.md)   * Disegna una linea composta da segmenti definiti da punti. Premendo il tasto **M** mentre si disegna una polilinea si alternano le diverse modalità della polilinea.

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width   *48px;"> [Crea un rettangolo](Sketcher_CompCreateRectangles/it.md)   * Questo è un menu icona nella barra degli strumenti Sketcher che contiene i seguenti comandi   * <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width   *32px;"> [Rettangolo](Sketcher_CreateRectangle/it.md)   * Disegna un rettangolo specificando gli angoli opposti.

   ** <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width   *32px;"> [Rettangolo dal centro](Sketcher_CreateRectangle_Center/it.md)   * Disegna un rettangolo da un punto centrale e un punto di bordo. <small>(v0.20)</small> 

   ** <img alt="" src=images/Sketcher_CreateOblong.svg  style="width   *32px;"> [Rettangolo arrotondato](Sketcher_CreateOblong/it.md)   * Disegna un rettangolo arrotondato da 2 punti opposti. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width   *48px;"> [Crea un Poligono regolare](Sketcher_CompCreateRegularPolygon/it.md)   * Questo è una icona menu nella barra degli strumenti Sketcher che contiene i seguenti comandi   *

   ** <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width   *32px;"> [Triangolo equilatero](Sketcher_CreateTriangle/it.md)   * Disegna un triangolo equilatero inscritto in una circonferenza di costruzione.

   ** <img alt="" src=images/Sketcher_CreateSquare.svg  style="width   *32px;"> [Quadrato](Sketcher_CreateSquare/it.md)   * Disegna un quadrato inscritto in una circonferenza di costruzione.

   ** <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width   *32px;"> [Pentagono](Sketcher_CreatePentagon/it.md)   * Disegna un pentagono inscritto in una circonferenza di costruzione.

   ** <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width   *32px;"> [Esagono](Sketcher_CreateHexagon/it.md)   * Disegna un esagono inscritto in una circonferenza di costruzione.

   ** <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width   *32px;"> [Ettagono](Sketcher_CreateHeptagon/it.md)   * Disegna un ettagono inscritto in una circonferenza di costruzione.

   ** <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width   *32px;"> [Ottagono](Sketcher_CreateOctagon/it.md)   * Disegna un ottagono inscritto in una circonferenza di costruzione.


<div class="mw-translate-fuzzy">

   ** <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width   *32px;"> [Poligono regolare](Sketcher_CreateRegularPolygon/it.md)    * Disegna un poligono regolare selezionando il numero di lati e selezionando due punti   * il centro e un angolo.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width   *32px;"> [Asola](Sketcher_CreateSlot/it.md)   * Disegna un rettangolo con due lati opposti raccordati con un semicerchio, un\'asola.

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width   *32px;"> [Raccorda](Sketcher_CreateFillet/it.md)   * Raccorda due linee unite in un punto. Selezionare entrambe le linee o fare clic sul punto di angolo, poi attivare lo strumento.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width   *32px;"> [Rifila](Sketcher_Trimming/it.md)   * Accorcia una linea, un cerchio o un arco fino al primo nodo, punto di intersezione.


</div>

-   <img alt="" src=images/Sketcher_Extend.svg  style="width   *32px;"> [Estendi](Sketcher_Extend/it.md)   * Estende una linea o un arco fino ad una linea di un bordo, arco, ellisse, arco di ellisse o un punto nello spazio.

-   <img alt="" src=images/Sketcher_Split.svg  style="width   *32px;"> [Dividi](Sketcher_Split/it.md)   * Divide una linea o un arco in due, converte un cerchio in un arco mantenendo la maggior parte dei vincoli. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width   *32px;"> [Geometria esterna](Sketcher_External/it.md)   * Crea un segmento collegato a una geometria esterna.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width   *32px;"> [CopiaCarbone](Sketcher_CarbonCopy/it.md)   * Copia la geometria di un altro schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width   *32px;"> [Costruzione](Sketcher_ToggleConstruction.md)   * Attiva o disattiva la geometria dello schizzo dalla o nella modalità di costruzione. La geometria di costruzione è mostrata in blu e viene presa in considerazione solo nella modalità di modifica dello schizzo.


</div>

### Vincoli dello Schizzo 

I vincoli sono utilizzati per stabilire le relazioni tra gli elementi del disegno, e per bloccare il disegno lungo l\'asse verticale e l\'asse orizzontale. Alcuni vincoli richiedono dei [Vincoli di supporto](Sketcher_helper_constraint/it.md).

#### Geometric constraints 


<div class="mw-translate-fuzzy">

#### Vincoli geometrici 

Questi vincoli non sono associati a valori numerici.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *32px;"> [Coincidente](Sketcher_ConstrainCoincident/it.md)   * Crea un vincolo di coincidenza (punto-con-punto) tra due punti selezionati.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *32px;"> [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md)   * Crea un vincolo (fissa) un punto-su-un-oggetto sull\'elemento selezionato.


</div>

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width   *32px;"> [Verticale](Sketcher_ConstrainVertical/it.md)   * Crea un vincolo verticale per le linee o le polilinee selezionate. Si può selezionare più oggetti.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width   *32px;"> [Orizzontale](Sketcher_ConstrainHorizontal/it.md)   * Crea un vincolo orizzontale per le linee o le polilinee selezionate. Si può selezionare più oggetti.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width   *32px;"> [Parallela](Sketcher_ConstrainParallel/it.md)   * Crea un vincolo di parallelismo tra due linee selezionate.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width   *32px;"> [Perpendicolare](Sketcher_ConstrainPerpendicular/it.md)   * Crea un vincolo di perpendicolarità tra due linee selezionate.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width   *32px;"> [Tangente](Sketcher_ConstrainTangent/it.md)   * Crea un vincolo di tangenza tra due entità selezionate, o un vincolo collineare tra due segmenti di linea.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width   *32px;"> [Uguaglianza](Sketcher_ConstrainEqual/it.md)   * Crea un vincolo di uguaglianza tra due entità selezionate. Se usato su cerchio o archi, il raggio viene posto uguale.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *32px;"> [Simmetria](Sketcher_ConstrainSymmetric/it.md)   * Crea un vincolo simmetrica tra 2 punti rispetto a una linea.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width   *32px;"> [Fissa](Sketcher_ConstrainBlock/it.md)   * blocca il movimento di un bordo, ovvero impedisce ai suoi vertici di cambiare la loro posizione corrente. Dovrebbe essere particolarmente utile per fissare la posizione delle B-Splines. Vedere la [discussione su Block Constraint nel forum](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Dimensional constraints 


<div class="mw-translate-fuzzy">

#### Vincoli dimensionali 

Vincoli associati a dati. Per questi vincoli si possono usare le [espressioni](Expressions/it.md). I dati possono essere prelevati da un [foglio di calcolo](Spreadsheet_Workbench/it.md).

Le icone blu di questi vincoli si riferiscono alle funzioni introdotte nella versione 0.16 di FreeCAD, attivabili con <img alt="" src=images/Sketcher_ToggleConstraint.png  style="width   *16px;"> **Commuta vincoli**.


</div>

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width   *32px;"> [Bloccato](Sketcher_ConstrainLock/it.md)   * Crea un vincolo che blocca l\'elemento selezionato fissando le sue dimensioni verticali e orizzontali rispetto all\'origine (le dimensioni si possono modificare in seguito).

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width   *32px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md)   * Fissa la distanza orizzontale tra 2 punti o tra gli estremi di una linea. Se viene selezionato un solo elemento, la distanza viene impostata a partire dall\'origine.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width   *32px;"> <img alt="" src=images/Constraint_VerticalDistance_Driven.png  style="width   *18px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md)   * Fissa la distanza verticale tra 2 punti o tra gli estremi di una linea. Se viene selezionato un solo elemento, la distanza viene impostata a partire dall\'origine.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width   *32px;"> <img alt="" src=images/Constraint_Length_Driven.png  style="width   *32px;"> [Lunghezza](Sketcher_ConstrainDistance/it.md)   * Definisce la distanza di una linea selezionata vincolandone la lunghezza o definisce la distanza tra due punti vincolando la distanza tra di loro.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width   *32px;"> [Raggio](Sketcher_ConstrainRadius/it.md)   * Definisce il raggio di un arco o di un cerchio selezionato vincolando il raggio.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width   *32px;"> [Diametro](Sketcher_ConstrainDiameter/it.md)   * Definisce il diametro di un arco o di un cerchio selezionato vincolando il diametro.
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width   *32px;"> [Angolo](Sketcher_ConstrainAngle/it.md)   * definisce l\'angolo interno tra due linee selezionate.


</div>


<div class="mw-translate-fuzzy">

#### Vincoli speciali 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width   *32px;"> [Rifrazione](Sketcher_ConstrainSnellsLaw/it.md)   * Crea un vincolo di rifrazione tra due linee per simulare secondo la Legge di Snell un raggio di luce che attraversa un\'interfaccia.


</div>

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width   *32px;"> [Allineamento interno](Sketcher_ConstrainInternalAlignment/it.md)   * Allinea gli elementi selezionati alla forma selezionata, ad esempio una linea da convertire in asse maggiore di una ellisse.

#### Constraint tools 


<div class="mw-translate-fuzzy">

#### Strumenti per i vincoli 

I seguenti strumenti possono essere utilizzati per cambiare l\'effetto dei vincoli   *


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width   *32px;"> [Commuta vincoli](Sketcher_ToggleDrivingConstraint/it.md)   * Commuta una serie di vincoli, quelli associati a un valore numerico, da decisivi a indicatori e viceversa.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width   *32px;"> [Attiva/disattiva il vincolo](Sketcher_ToggleActiveConstraint/it.md)   * Abilita o disabilita un vincolo già inserito. {{Version/it|0.19}}


</div>

### Strumenti dello Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width   *32px;"> [Seleziona il risolutore DOFs](Sketcher_SelectElementsWithDoFs/it.md)   * Evidenzia in verde la geometria con gradi di libertà (DOFs), cioè non completamente vincolata.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg‎  style="width   *32px;"> [Chiudi Forma](Sketcher_CloseShape/it.md)   * Crea una forma chiusa applicando i vincoli di coincidenza ai punti finali.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg‎  style="width   *32px;"> [Collega Segmenti](Sketcher_ConnectLines/it.md)   * Collega gli elementi dello schizzo applicando i vincoli di coincidenza ai punti finali.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg‎  style="width   *32px;"> [Seleziona Vincoli](Sketcher_SelectConstraints/it.md)   * Seleziona i vincoli di un elemento dello schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg‎  style="width   *32px;"> [Seleziona gli elementi associati a vincoli](Sketcher_SelectElementsAssociatedWithConstraints/it.md)   * Evidenzia gli elementi dello schizzo associati ai vincoli selezionati.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg‎  style="width   *32px;"> [Seleziona i vincoli ridondanti](Sketcher_SelectRedundantConstraints/it.md)   * Seleziona i vincoli ridondanti di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg‎  style="width   *32px;"> [Seleziona i vincoli in conflitto](Sketcher_SelectConflictingConstraints/it.md)   * Seleziona i vincoli in conflitto di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg‎  style="width   *32px;"> [Mostra/Nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md)   * Ricrea la geometria interna mancante o eliminata non necessaria di un\'ellisse selezionata, o arco di ellisse o iperbole o parabola o B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg‎  style="width   *32px;"> [Seleziona Origine](Sketcher_SelectOrigin/it.md)   * Seleziona l\'origine di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg‎  style="width   *32px;"> [Seleziona Asse Y](Sketcher_SelectVerticalAxis/it.md)   * Seleziona l\'asse verticale di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg‎  style="width   *32px;"> [Seleziona Asse X](Sketcher_SelectHorizontalAxis/it.md)   * Seleziona l\'asse orizzontale di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg‎  style="width   *32px;"> [Simmetria](Sketcher_Symmetry/it.md)   * Copia un elemento dello schizzo in modo simmetrico rispetto ad una linea a scelta.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg‎  style="width   *32px;"> [Clona](Sketcher_Clone/it.md)   * Clona un elemento dello schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg‎  style="width   *32px;"> [Copia](Sketcher_Copy/it.md)   * Copia un elemento dello schizzo.


</div>

-   <img alt="" src=images/Sketcher_Move.svg  style="width   *32px;"> [Sposta](Sketcher_Move/it.md)   * Sposta la geometria selezionata prendendo come riferimento l\'ultimo punto selezionato.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg‎  style="width   *32px;"> [Schiera lineare](Sketcher_RectangularArray/it.md)   * Crea una schiera con gli elementi dello schizzo selezionati.


</div>

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width   *32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md)   * Remove axes alignment while trying to preserve the constraint relationship of the selection. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width   *32px;"> [Cancella tutta la geometria](Sketcher_DeleteAllGeometry/it.md)   * Elimina tutta la geometria dallo schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width   *32px;"> [Elimina tutti i vincoli](Sketcher_DeleteAllConstraints/it.md)   * Elimina tutti i vincoli dallo schizzo.


</div>

### Strumenti Sketcher B-spline 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width   *32px;"> [Mostra/nascondi i gradi della B-spline](Sketcher_BSplineDegree/it.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width   *32px;"> [Mostra/nascondi i poligoni di controllo della B-spline](Sketcher_BSplinePolygon/it.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width   *32px;"> [Mostra/nascondi il pettine di curvatura](Sketcher_BSplineComb/it.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width   *32px;"> [Mostra/nascondi le molteplicità di nodo B-spline](Sketcher_BSplineKnotMultiplicity/it.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width   *32px;"> [ Mostra/nascondi il valore dei punti di controllo delle B-spline ](Sketcher_BSplinePoleWeight/it.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width   *32px;"> [Converti la geometria in B-spline](Sketcher_BSplineApproximate/it.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width   *32px;"> [Aumenta il grado della B-spline](Sketcher_BSplineIncreaseDegree/it.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width   *32px;"> [Diminuisci il grado della B-spline](Sketcher_BSplineDecreaseDegree/it.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width   *32px;"> [Aumenta la molteplicità di nodo](Sketcher_BSplineIncreaseKnotMultiplicity/it.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width   *32px;"> [Diminuisci la molteplicità](Sketcher_BSplineDecreaseKnotMultiplicity/it.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width   *32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md), <small>(v0.20)</small> 

### Spazio virtuale dello Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg‎  style="width   *32px;"> [Cambia spazio virtuale](Sketcher_SwitchVirtualSpace/it.md)   * Permette di nascondere i vincoli e renderli nuovamente visibili.


</div>


<div class="mw-translate-fuzzy">

### Preferenze


</div>

-   <img alt="" src=images/Preferences-general.svg  style="width   *32px;"> [Preferences\...](Sketcher_Preferences/it.md)   * Preferenze disponibili per l\'ambiente Sketcher.

## Best Practices 


<div class="mw-translate-fuzzy">

## Migliori pratiche 

Ogni utente CAD, nel corso del tempo, sviluppa un proprio modo di lavorare, ma ci sono alcuni criteri generali che è utile seguire.


</div>


<div class="mw-translate-fuzzy">

-   Una serie di schizzi semplici è più facile da gestire rispetto a un unico schizzo molto complesso. Ad esempio, si può creare un primo schizzo per produrre (con una estrusione o una rivoluzione) la forma 3D di base, poi un secondo schizzo per eseguire i fori o le aperture (tasche). Alcuni dettagli possono essere omessi e realizzati in seguito come operazioni 3D. È possibile decidere di evitare gli smussi nel disegno, se ce ne sono troppi, e aggiungerli dopo come caratteristica 3D.
-   Creare sempre un profilo chiuso altrimenti il disegno non produrrà un solido, bensì una serie di facce aperte. Quando si desidera escludere alcuni oggetti nella creazione del solido, trasformarli in elementi di costruzione con lo strumento **Modalità costruzione**.
-   Utilizzare la funzione **Vincoli automatici** per ridurre il numero di vincoli da inserire manualmente.
-   Come regola generale, si applicano prima i vincoli geometrici, poi i vincoli dimensionali, e infine si blocca il disegno. Da ricordare   * le regole sono fatte per essere infrante. Quando ci sono difficoltà nel manipolare il disegno, può essere utile vincolare alcuni oggetti prima di completare il profilo.
-   Se possibile, centrare il disegno nell\'origine (0,0) con il vincolo **Blocca**. Se il disegno non è simmetrico, posizionare uno dei suoi punti nell\'origine, o scegliere una cifra tonda semplice per le distanze di blocco. Nella versione v0.12, i vincoli esterni (vincoli rispetto a geometrie 3D esistenti come a bordi o altri schizzi) non sono ancora implementati. Questo significa che per collegare i disegni successivi alla geometria del primo schizzo, si devono impostare manualmente le distanze relative al primo disegno. Un vincolo di blocco (25,75) dall\'origine è più facile da ricordare che (23.47,73.02).
-   Se c\'è la possibilità di scegliere tra il vincolo [lunghezza](Sketcher_ConstrainDistance/it.md) <img alt="" src=images/Constraint_Length.png  style="width   *16px;"> e il vincolo [distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) <img alt="" src=images/Constraint_HorizontalDistance.png  style="width   *16px;"> o [distanza verticale](Sketcher_ConstrainDistanceY/it.md) <img alt="" src=images/Constraint_Vertical.png  style="width   *16px;">, preferire questi ultimi. I vincoli di distanza orizzontale e verticale sono computazionalmente più economici.
-   In generale, i vincoli migliori da utilizzare sono   * Orizzontale e Verticale, Lunghezza Orizzontale e Verticale, Tangente nel punto. Se possibile, limitare l\'uso di questi vincoli   * Lunghezza generica, Tangenza Edge-to-edge, Punto su linea; Simmetria.
-   In caso di dubbi sulla validità di uno schizzo una volta completato (le funzioni diventano verdi), chiudere la finestra di dialogo di Sketcher, passare a <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> [Part](Part_Workbench/it.md) ed eseguire <img alt="" src=images/Part_CheckGeometry.svg  style="width   *16px;"> [Controlla la geometria](Part_CheckGeometry/it.md).


</div>

## Tutorial

-   [Sketcher tutorial](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. Questo è un documento PDF lungo 70 pagine che funge da manuale dettagliato per lo sketcher. Spiega le basi dell\'utilizzo di Sketcher e approfondisce la creazione di forme geometriche e ciascuno dei vincoli.
-   [Tutorial base di Sketcher](Basic_Sketcher_Tutorial/it.md) per principianti
-   [Sketcher Micro Tutorial - Pratica con i vincoli](Sketcher_Micro_Tutorial_-_Constraint_Practices/it.md)
-   [Requisiti di uno schizzo](Sketcher_requirement_for_a_sketch/it.md) Requisito minimo per uno schizzo e definizione completa di uno schizzo

## Script

La pagina [scripting](Sketcher_scripting/it.md) contiene esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/it
