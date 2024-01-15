# <img alt="L\'icona dell\'ambiente Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/it






## Introduzione

L\'[Ambiente Sketcher](Sketcher_Workbench/it.md) <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> di FreeCAD serve per creare degli schizzi 2D destinati ad essere utilizzati negli ambienti <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/it.md) o altri. In genere, un disegno 2D è il punto di partenza per la maggior parte dei modelli CAD. Un semplice schizzo 2D può essere \"estruso\" per creare una forma 3D; successivamente degli schizzi 2D possono essere usati per creare altre funzioni quali tasche, o estrusioni sulla superficie dell\'oggetto 3D precedentemente costruito. Insieme alle operazioni booleane definite nell\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente Part](Part_Workbench/it.md), lo Sketcher costituisce la base del metodo [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG) per la costruzione di solidi. Inoltre, insieme alle operazioni dell\'ambiente <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md), lo Sketcher costituisce anche la base della metodologia per la creazione di solidi nota come [Editazione delle funzioni](feature_editing/it.md).

L\'ambiente Sketcher mette a disposizione i **vincoli**. Consente di vincolare le forme 2D a precise definizioni geometriche in termini di lunghezza, angoli e relazioni (orizzontalità, verticalità, perpendicolarità, ecc.).
Un solutore dei vincoli calcola la quantità di vincoli applicati alla geometria 2D e permette l\'esplorazione interattiva dei gradi di libertà dello schizzo.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Uno schizzo base, completamente vincolato‎.*



## Nozioni di base sugli schizzi vincolati 

Per spiegare come funziona il modulo Sketcher, è utile fare un confronto con il **modo tradizionale** di disegnare.



##### Disegno tradizionale 

Il modo tradizionale di disegno CAD è derivato dal vecchio [tavolo da disegno](http://en.wikipedia.org/wiki/Drawing_board).
[Le viste ortogonali 2D](http://en.wikipedia.org/wiki/Multiview_orthographic_projection) sono disegnate manualmente e finalizzate alla produzione di disegni tecnici (noti anche come dettagli o particolari). Gli oggetti sono disegnati esattamente con le loro forme, misure o dimensioni previste. Per tracciare una linea orizzontale lunga 100 mm a partire dal punto (0,0), si attiva lo strumento linea, si fa clic sullo schermo o si inserisce le coordinate (0,0) per il primo punto, poi si fa un secondo clic o si inserisce il secondo punto di coordinate (100,0). Oppure, si costruisce una linea base senza riguardo alla sua posizione e in seguito la si sposta. Dopo aver disegnato le geometrie si aggiungono le dimensioni.



#### Schizzo vincolato 

Lo strumento Sketcher si allontana da questa logica. Non è più necessario disegnare gli oggetti esattamente come sono desiderati, perché è possibile ridefinirli in seguito tramite i vincoli. È possibile disegnare liberamente gli oggetti e dopo, fintanto che non vengono vincolati, modificarli. Sostanzialmente, essi sono **flottanti**, quindi si possono spostare, allungare, scalare, e così via. Questo permette una grande flessibilità nel processo di progettazione.



#### Cosa sono i vincoli? 

Invece delle dimensioni, i vincoli vengono utilizzati per limitare i gradi di libertà di un oggetto. Ad esempio, una linea senza vincoli ha 4 gradi di libertà (DOF Degrees Of Freedom): essa può essere spostata orizzontalmente o verticalmente, può essere allungata, e può essere ruotata.

Applicando a una linea un vincolo orizzontale o verticale, oppure un vincolo angolare (rispetto ad un\'altra linea o ad uno degli assi) si limita la sua capacità di ruotare, lasciandola quindi con solo 2 gradi di libertà. Bloccando uno dei suoi punti rispetto all\'origine si rimuove un ulteriore grado di libertà. Applicando un vincolo dimensionale si rimuove l\'ultimo grado di libertà. A questo punto, la linea è quindi considerata **completamente vincolata**.

Più oggetti possono essere vincolati tra di loro. Due linee possono essere unite attraverso uno dei loro punti con il vincolo punto coincidente. Tra due linee si può impostare un angolo, oppure impostarle perpendicolari. Una linea può essere tangente ad un arco o a un cerchio, e così via. Per vincolare uno schizzo complesso, con più oggetti, sono possibili diverse soluzioni, e renderlo **completamente vincolato** significa che almeno una di queste è stato raggiunta in base ai vincoli applicati.

Ci sono due tipi di vincoli: geometrici e dimensionali. Essi sono descritti nella successiva sezione dedicata agli [\'Strumenti\'](#Strumenti.md).



#### Per che cosa l\'Ambiente Sketcher non va bene 

Il modulo Sketcher non è pensato per produrre disegni dettagliati in 2D. Dopo che gli schizzi sono stati utilizzati per generare una forma solida vengono automaticamente nascosti. I vincoli (la quotatura dei vincoli e i segni grafici di vincolo) sono visibili solo in modalità **Modifica sketch**.

Se serve solo produrre delle viste 2D per la stampa e non si intende creare dei modelli 3D, si può utilizzare l\'ambiente [Draft](Draft_Workbench/it.md). A differenza degli elementi di Sketcher, gli oggetti di Draft non usano i vincoli, ma sono forme semplici definite al momento della creazione. Sia Draft che Sketcher possono essere utilizzati per il disegno di geometrie 2D e la creazione di solidi 3D, sebbene il loro uso previsto sia diverso:

-   **L\'Ambiente Sketcher** viene normalmente utilizzato insieme agli ambienti [Part](Part_Workbench/it.md) e [PartDesign](PartDesign_Workbench/it.md) per creare solidi.
-   Il **L\'Ambiente Draft** viene normalmente utilizzato per semplici disegni planari su una griglia, come quando si disegna una pianta architettonica. In queste situazioni Draft viene utilizzato principalmente insieme all\'[Ambiente Arch](Arch_Workbench/it.md).

Lo strumento [Draft a Schizzo ](Draft_Draft2Sketch/it.md) converte un oggetto Draft in un oggetto Sketch e viceversa. Molti strumenti che richiedono un elemento 2D come input funzionano con entrambi i tipi di oggetto poiché la conversione interna viene eseguita automaticamente.



## Flusso di lavoro per gli schizzi 

Uno Sketch è sempre in 2 dimensioni (2D). Per creare un solido, viene creato prima lo schizzo 2D di una singola area chiusa e poi essa viene estrusa o rivoluzionata per aggiungere la terza dimensione, creando un solido 3D dallo schizzo 2D.

Se lo schizzo contiene dei segmenti che si intersecano, punti non collocati esattamente su un segmento, o punti finali di segmenti adiacenti che non sono coincidenti, l\'operazione di Pad o di Rivoluzione non crea un solido. A volte uno schizzo che contiene linee che si intersecano può funzionare per un\'operazione semplice come un Pad, ma le operazioni successive falliscono. È meglio evitare di attraversare le linee. Come eccezione, questa regola non si applica alla geometria di costruzione (linee blu).

All\'interno dell\'area racchiusa si possono avere delle piccole aree non sovrapposte. Queste diverranno dei \"vuoti\" quando si crea il solido 3D.

Quando uno schizzo è completamente vincolato, le funzioni dello schizzo diventano verdi. La geometria di costruzione rimane blu. Di solito a questo punto lo schizzo è \"finito\" e adatto per l\'uso nella creazione di un solido 3D. Tuttavia, una volta chiusa la finestra di dialogo Schizzo, può essere utile andare in <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Ambiente Part](Part_Workbench/it.md) ed eseguire <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Controlla la geometria](Part_CheckGeometry/it.md) per assicurarsi che nello schizzo non ci siano funzioni che possono causare problemi successivi.



## Strumenti

Gli strumenti dell\'Ambiente Sketcher si trovano nel menu Sketch e/o in diverse barre degli strumenti. {{Version/it|0.21}}: quasi tutte le barre degli strumenti di Sketcher vengono visualizzate soltanto se uno schizzo è in modalità di modifica. L\'unica eccezione è che la [barra degli strumenti di Sketcher](#Sketcher_toolbar.md) viene visualizzata soltanto se nessuno schizzo è in modalità di modifica.


{{Version/it|0.21}}

: se uno schizzo è in modalità di modifica, la barra degli strumenti Struttura è nascosta perché nessuno dei suoi strumenti può essere utilizzato.



### Generale



#### Barra degli strumenti di Sketcher 

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Crea schizzo](Sketcher_NewSketch/it.md): Crea un nuovo schizzo su una faccia selezionata o in un piano. Se non si esegue nessuna selezione, di default, viene utilizzato il piano XY.

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Modifica schizzo](Sketcher_EditSketch/it.md): Modifica lo schizzo selezionato. Apre la finestra [Dialogo di Sketcher](Sketcher_Dialog/it.md)

-   <img alt="" src=images/Sketcher_MapSketch.svg‎‎‎  style="width:32px;"> [Mappa schizzo su faccia](Sketcher_MapSketch/it.md): Mappa uno schizzo sulla faccia di un solido selezionata in precedenza.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Riposiziona lo schizzo](Sketcher_ReorientSketch/it.md): Permette di modificare la posizione di uno schizzo

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Convalida lo schizzo](Sketcher_ValidateSketch/it.md): Analizza e ripara uno schizzo che non è più modificabile, ha vincoli non validi o mancano vincoli coincidenti.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Unisci schizzi](Sketcher_MergeSketches/it.md): Unisce due o più schizzi.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎‎‎  style="width:32px;"> [Rifletti schizzo](Sketcher_MirrorSketch/it.md): Riflette uno schizzo rispetto all\'asse verticale, o all\'asse orizzontale e all\'origine.



#### Barra degli strumenti in Modalità modifica di Sketcher 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg‎‎  style="width:32px;"> [Esci](Sketcher_LeaveSketch/it.md): Termina la modalità di modifica dello schizzo.

-   <img alt="" src=images/Sketcher_ViewSketch.svg‎‎‎  style="width:32px;"> [Vista schizzo](Sketcher_ViewSketch/it.md): Imposta la vista del modello in modo perpendicolare al piano dello schizzo.

-   <img alt="" src=images/Sketcher_ViewSection.svg‎‎  style="width:32px;"> [Vista in sezione](Sketcher_ViewSection/it.md): Crea un piano di sezione che nasconde temporaneamente qualsiasi materia davanti al piano dello schizzo.



#### Barra degli strumenti di modifica di Sketcher 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Attiva/Disattiva la griglia](Sketcher_Grid/it.md): attiva o disattiva la griglia nello schizzo attualmente in fase di modifica. Le impostazioni possono essere modificate nel relativo menu. {{Version/it|0.21}}

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Attiva/Disattiva snap](Sketcher_Snap/it.md): Attiva/disattiva lo snap in tutti gli schizzi. Le impostazioni possono essere modificate nel relativo menu. {{Version/it|0.21}}

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configura l\'ordine di rendering](Sketcher_RenderingOrder/it.md): L\'ordine di rendering di tutti gli schizzi può essere modificato nel relativo menu. {{Version/it|0.21}}



#### Altro

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Interrompi l\'operazione](Sketcher_StopOperation/it.md): Quando si è in modalità di modifica, interrompe l\'operazione corrente, sia che si tratti di disegnare, impostare vincoli, ecc.



### Geometrie

Gli strumenti per creare gli oggetti.

-   <img alt="" src=images/Sketcher_CreatePoint.svg‎‎  style="width:32px;"> [Punto](Sketcher_CreatePoint/it.md): Disegna un punto.

-   <img alt="" src=images/Sketcher_CreateLine.svg‎‎  style="width:32px;"> [Linea tra due punti](Sketcher_CreateLine/it.md): Disegna un segmento delimitato da due punti. Per quanto riguarda alcuni vincoli le linee sono infinite.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:

  - <img alt="" src=images/Sketcher_CreateArc.svg‎‎  style="width:32px;"> [Arco](Sketcher_CreateArc/it.md): Disegna un arco di circonferenza specificando il centro, il raggio, l\'angolo iniziale e l\'angolo finale.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arco da tre punti](Sketcher_Create3PointArc/it.md): Disegna un arco da due punti finali e un punto della circonferenza.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Circonferenza](Sketcher_CreateCircle/it.md): Disegna una circonferenza prendendo in input il centro e il raggio.

  -<img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Circonferenza da tre punti](Sketcher_Create3PointCircle/it.md) : Disegna un cerchio da tre punti sulla circonferenza.

-   <img alt="" src=images/Sketcher_Conics.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create conic:

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellisse](Sketcher_CreateEllipseByCenter/it.md): Disegna un\'ellisse dal centro, raggio maggiore e raggio minore.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellisse da tre punti](Sketcher_CreateEllipseBy3Points/it.md): Disegna una ellisse da due punti del raggio maggiore e un punto del raggio minore.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arco di ellisse](Sketcher_CreateArcOfEllipse/it.md): Disegna un arco di ellisse dal punto centrale, un punto del raggio maggiore, il punto iniziale e il punto finale.

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arco di iperbole](Sketcher_CreateArcOfHyperbola/it.md): Disegna un arco di iperbole.

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arco di parabola](Sketcher_CreateArcOfParabola/it.md): Disegna un arco di parabola.

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline dai punti di controllo](Sketcher_CreateBSpline/it.md) : Disegna una curva B-spline dai suoi punti di controllo.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [B-spline periodica dai punti di controllo](Sketcher_CreatePeriodicBSpline/it.md) : Disegna una curva B-spline periodica (chiusa) dai suoi punti di controllo.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline per nodi](Sketcher_CreateBSplineByInterpolation.md): Disegna una curva B-spline per i suoi nodi. {{Version/it|0.21}}

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [B-spline periodica per nodi](Sketcher_CreatePeriodicBSplineByInterpolation/it.md): Disegna una curva B-spline periodica (chiusa) per i suoi nodi. {{Version/it|0.21}}

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilinea ](Sketcher_CreatePolyline/it.md): Disegna una linea composta da segmenti definiti da punti. Premendo il tasto **M** mentre si disegna una polilinea si alternano le diverse modalità della polilinea.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rettangolo](Sketcher_CreateRectangle/it.md): Disegna un rettangolo specificando gli angoli opposti.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rettangolo dal centro](Sketcher_CreateRectangle_Center/it.md): Disegna un rettangolo da un punto centrale e un punto di bordo. <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rettangolo arrotondato](Sketcher_CreateOblong/it.md): Disegna un rettangolo arrotondato da 2 punti opposti. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangolo equilatero](Sketcher_CreateTriangle/it.md): Disegna un triangolo equilatero inscritto in una circonferenza di costruzione.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Quadrato](Sketcher_CreateSquare/it.md): Disegna un quadrato inscritto in una circonferenza di costruzione.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagono](Sketcher_CreatePentagon/it.md): Disegna un pentagono inscritto in una circonferenza di costruzione.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Esagono](Sketcher_CreateHexagon/it.md): Disegna un esagono inscritto in una circonferenza di costruzione.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Ettagono](Sketcher_CreateHeptagon/it.md): Disegna un ettagono inscritto in una circonferenza di costruzione.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Ottagono](Sketcher_CreateOctagon/it.md): Disegna un ottagono inscritto in una circonferenza di costruzione.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Poligono regolare](Sketcher_CreateRegularPolygon/it.md) : Disegna un poligono regolare selezionando il numero di lati e selezionando due punti: il centro e un angolo.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Asola](Sketcher_CreateSlot/it.md): Disegna un rettangolo con due lati opposti raccordati con un semicerchio, un\'asola.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot/it.md): TBD.


</div>

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet:

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Raccorda](Sketcher_CreateFillet/it.md): Crea un raccordo tra due linee non parallele.

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Filetto salva angolo](Sketcher_CreatePointFillet/it.md): Crea un raccordo tra due linee non parallele preservandone l\'intersezione (virtuale).

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:

  - <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Rifila](Sketcher_Trimming/it.md): Accorcia una linea, un cerchio o un arco fino al primo nodo, punto di intersezione.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Dividi](Sketcher_Split/it.md): Divide una linea in due, mantenendo la maggior parte dei vincoli. <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Estendi](Sketcher_Extend/it.md): Estende una linea o un arco fino ad una linea di un bordo, arco, ellisse, arco di ellisse o un punto nello spazio.

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometria esterna](Sketcher_External/it.md): Crea un segmento collegato a una geometria esterna.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Copia Carbone](Sketcher_CarbonCopy/it.md): Copia la geometria di un altro schizzo.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Attiva/disattiva la geometria di costruzione](Sketcher_ToggleConstruction.md): Attiva o disattiva la geometria dello schizzo dalla o nella modalità di costruzione. La geometria di costruzione è mostrata in blu e viene presa in considerazione solo nella modalità di modifica dello schizzo.



### Vincoli dello Schizzo 

I vincoli sono utilizzati per stabilire le relazioni tra gli elementi del disegno, e per bloccare il disegno lungo l\'asse verticale e l\'asse orizzontale. Alcuni vincoli richiedono dei [Vincoli di supporto](Sketcher_helper_constraint/it.md).

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): TBD. <small>(v0.22)</small> 

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/it.md): Crea un vincolo di coincidenza (punto-con-punto) tra due punti selezionati.

Funge da vincolo concentrico se sono selezionati due o più cerchi, archi, ellissi o archi di ellissi.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md): Crea un vincolo (fissa) un punto-su-un-oggetto sull\'elemento selezionato.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Constrain horizontally or vertically:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/Vertical](Sketcher_ConstrainHorVer.md): TBD. <small>(v0.22)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Orizzontale](Sketcher_ConstrainHorizontal/it.md): Crea un vincolo orizzontale per le linee o le polilinee selezionate. Si può selezionare più oggetti.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Verticale](Sketcher_ConstrainVertical/it.md): Crea un vincolo verticale per le linee o le polilinee selezionate. Si può selezionare più oggetti.


</div>

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallela](Sketcher_ConstrainParallel/it.md): Crea un vincolo di parallelismo tra due linee selezionate.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicolare](Sketcher_ConstrainPerpendicular/it.md): Crea un vincolo di perpendicolarità tra due linee selezionate.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/it.md): Crea un vincolo di tangenza tra due entità selezionate, o un vincolo collineare tra due segmenti di linea.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Uguaglianza](Sketcher_ConstrainEqual/it.md): Crea un vincolo di uguaglianza tra due entità selezionate. Se usato su cerchio o archi, il raggio viene posto uguale.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Simmetria](Sketcher_ConstrainSymmetric/it.md): Crea un vincolo simmetrica tra 2 punti rispetto a una linea.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Fissa](Sketcher_ConstrainBlock/it.md): blocca il movimento di un bordo, ovvero impedisce ai suoi vertici di cambiare la loro posizione corrente. Dovrebbe essere particolarmente utile per fissare la posizione delle B-Splines. Vedere la [discussione su Block Constraint nel forum](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): TBD. <small>(v0.22)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Bloccato](Sketcher_ConstrainLock/it.md): Crea un vincolo che blocca l\'elemento selezionato fissando le sue dimensioni verticali e orizzontali rispetto all\'origine (le dimensioni si possono modificare in seguito).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md): Fissa la distanza orizzontale tra 2 punti o tra gli estremi di una linea. Se viene selezionato un solo elemento, la distanza viene impostata a partire dall\'origine.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> <img alt="" src=images/Constraint_VerticalDistance_Driven.png  style="width:18px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md): Fissa la distanza verticale tra 2 punti o tra gli estremi di una linea. Se viene selezionato un solo elemento, la distanza viene impostata a partire dall\'origine.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distanza](Sketcher_ConstrainDistance/it.md): definisce la lunghezza di una linea, la distanza perpendicolare tra un punto e una linea, la distanza tra due punti o, {{Version/it|0.21}}, la distanza tra i bordi di due cerchi.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Raggio o peso](Sketcher_ConstrainRadius/it.md): Definisce il raggio di un arco o di un cerchio o il peso di un polo di una B-spline.


</div>

-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diametro](Sketcher_ConstrainDiameter/it.md): Definisce il diametro di un arco o di un cerchio.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto raggio/diametro](Sketcher_ConstrainRadiam/it.md): Definisce il raggio di un arco, il diametro di un cerchio o il peso di un polo B-spline. {{Version/it|0.20}}


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angolo](Sketcher_ConstrainAngle/it.md): definisce l\'angolo interno tra due linee selezionate.


</div>



#### Vincoli speciali 

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Rifrazione (legge di Snell)](Sketcher_ConstrainSnellsLaw/it.md): Crea un vincolo di rifrazione tra due linee per simulare secondo la Legge di Snell un raggio di luce che attraversa un\'interfaccia.



#### Strumenti per i vincoli 

I seguenti strumenti possono essere utilizzati per cambiare l\'effetto dei vincoli:

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Commuta vincoli](Sketcher_ToggleDrivingConstraint/it.md): Commuta una serie di vincoli, quelli associati a un valore numerico, da decisivi a indicatori e viceversa.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Attiva/disattiva il vincolo](Sketcher_ToggleActiveConstraint/it.md): Abilita o disabilita un vincolo già inserito.



### Strumenti dello Sketcher 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Seleziona i DOF svincolati](Sketcher_SelectElementsWithDoFs/it.md): Evidenzia in verde la geometria con gradi di libertà (DOFs), cioè non completamente vincolata.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg‎  style="width:32px;"> [Seleziona i vincoli associati](Sketcher_SelectConstraints/it.md): Seleziona i vincoli di un elemento dello schizzo.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg‎  style="width:32px;"> [Seleziona la geometria associata](Sketcher_SelectElementsAssociatedWithConstraints/it.md): Evidenzia gli elementi dello schizzo associati ai vincoli selezionati.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg‎  style="width:32px;"> [Seleziona i vincoli ridondanti](Sketcher_SelectRedundantConstraints/it.md): Seleziona i vincoli ridondanti di uno schizzo.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg‎  style="width:32px;"> [Seleziona i vincoli in conflitto](Sketcher_SelectConflictingConstraints/it.md): Seleziona i vincoli in conflitto di uno schizzo.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg‎  style="width:32px;"> [Mostra/nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md): Ricrea la geometria interna mancante o eliminata non necessaria di un\'ellisse selezionata, o arco di ellisse o iperbole o parabola o B-spline.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg‎  style="width:32px;"> [Seleziona origine](Sketcher_SelectOrigin/it.md): Seleziona l\'origine di uno schizzo.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg‎  style="width:32px;"> [Seleziona l\'asse orizzontale](Sketcher_SelectHorizontalAxis/it.md): Seleziona l\'asse orizzontale di uno schizzo.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg‎  style="width:32px;"> [Seleziona l\'asse verticale](Sketcher_SelectVerticalAxis/it.md): Seleziona l\'asse verticale di uno schizzo.

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometria](Sketcher_Offset/it.md): aggiunge un contorno equidistante attorno ai bordi selezionati. {{Version/it|0.22}}

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): TBD. <small>(v0.22)</small> 

-   <img alt="" src=images/Sketcher_Symmetry.svg‎  style="width:32px;"> [Simmetria](Sketcher_Symmetry/it.md): Copia un elemento dello schizzo in modo simmetrico rispetto ad una linea a scelta.

-   <img alt="" src=images/Sketcher_Clone.svg‎  style="width:32px;"> [Clona](Sketcher_Clone/it.md): Clona un elemento dello schizzo.

-   <img alt="" src=images/Sketcher_Copy.svg‎  style="width:32px;"> [Copia](Sketcher_Copy/it.md): Copia un elemento dello schizzo.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Sposta](Sketcher_Move/it.md): Sposta la geometria selezionata prendendo come riferimento l\'ultimo punto selezionato.

-   <img alt="" src=images/Sketcher_RectangularArray.svg‎  style="width:32px;"> [Matrice rettangolare](Sketcher_RectangularArray/it.md): Crea una matrice con gli elementi dello schizzo selezionati.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Rimuove l\'allineamento degli assi](Sketcher_RemoveAxesAlignment/it.md): Rimuovere l\'allineamento degli assi mentre cerca di preservare la relazione di vincolo della selezione. {{Version/it|0.20}}

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Cancella tutta la geometria](Sketcher_DeleteAllGeometry/it.md): Elimina tutta la geometria dallo schizzo.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Elimina tutti i vincoli](Sketcher_DeleteAllConstraints/it.md): Elimina tutti i vincoli dallo schizzo.



### Strumenti Sketcher B-spline 

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Converti la geometria in B-spline](Sketcher_BSplineApproximate/it.md): Converte una geometria, i bordi e le curve compatibili in una B-spline.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Aumenta il grado della B-spline](Sketcher_BSplineIncreaseDegree/it.md): Aumenta il grado (ordine) di una B-spline.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Diminuisci il grado della B-spline](Sketcher_BSplineDecreaseDegree/it.md): Diminuisce il grado (ordine) di una B-spline.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Aumenta la molteplicità di nodo](Sketcher_BSplineIncreaseKnotMultiplicity/it.md): Aumenta la molteplicità di un nodo B-spline.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Diminuisci la molteplicità](Sketcher_BSplineDecreaseKnotMultiplicity/it.md): Diminuisce la molteplicità di un nodo B-spline.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Inserisci il nodo](Sketcher_BSplineInsertKnot/it.md): Inserisce un nodo in una B-spline esistente. {{Version/it|0.20}}

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Unisci curve](Sketcher_JoinCurves/it.md): Unisce due curve nei punti finali selezionati. {{Version/it|0.21}}

### Sketcher visual 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg‎  style="width:32px;"> [Cambia spazio virtuale](Sketcher_SwitchVirtualSpace/it.md): Permette di nascondere i vincoli e renderli nuovamente visibili.

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Mostra/nascondi i gradi della B-spline](Sketcher_BSplineDegree/it.md): Mostra o nasconde la visualizzazione del grado di una B-spline.

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Mostra/nascondi i poligoni di controllo della B-spline](Sketcher_BSplinePolygon/it.md): Mostra o nasconde la visualizzazione del poligono che definisce una B-spline.

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Mostra/nascondi il pettine di curvatura](Sketcher_BSplineComb/it.md): Mostra o nasconde la visualizzazione del pettine di curvatura di una B-spline.

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Mostra/nascondi le molteplicità di nodo B-spline](Sketcher_BSplineKnotMultiplicity/it.md): Mostra o nasconde la visualizzazione della molteplicità dei nodi di una B-spline.

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [ Mostra/nascondi il valore dei punti di controllo delle B-spline ](Sketcher_BSplinePoleWeight/it.md): Mostra o nasconde la visualizzazione dei pesi per i punti di controllo di una B-spline.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): TBD. <small>(v0.22)</small> 



### Strumenti obsoleti 

-   <img alt="" src=images/Sketcher_CloseShape.svg‎  style="width:32px;"> [Chiudi forma](Sketcher_CloseShape/it.md): Crea una forma chiusa applicando vincoli coincidenti ai punti finali. Non disponibile dalla {{VersionPlus/it|0.21}}.

-   <img alt="" src=images/Sketcher_ConnectLines.svg‎  style="width:32px;"> [Collega segmenti](Sketcher_ConnectLines/it.md): Collega gli elementi dello sketcher applicando vincoli coincidenti ai punti finali. Non disponibile dalla {{VersionPlus/it|0.21}}.



## Preferenze

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferences\...](Sketcher_Preferences/it.md): Preferenze disponibili per l\'ambiente Sketcher.



## Migliori Pratiche 

Ogni utente CAD, nel corso del tempo, sviluppa un proprio modo di lavorare, ma ci sono alcuni criteri generali che è utile seguire.

-   Una serie di schizzi semplici è più facile da gestire rispetto a un unico schizzo molto complesso. Ad esempio, si può creare un primo schizzo per produrre (con una estrusione o una rivoluzione) la forma 3D di base, poi un secondo schizzo per eseguire i fori o le aperture (tasche). Alcuni dettagli possono essere omessi e realizzati in seguito come operazioni 3D. È possibile decidere di evitare gli smussi nel disegno, se ce ne sono troppi, e aggiungerli dopo come caratteristica 3D.
-   Creare sempre un profilo chiuso altrimenti il disegno non produrrà un solido, bensì una serie di facce aperte. Quando si desidera escludere alcuni oggetti nella creazione del solido, trasformarli in elementi di costruzione con lo strumento **Modalità costruzione**.
-   Utilizzare la funzione **Vincoli automatici** per ridurre il numero di vincoli da inserire manualmente.
-   Come regola generale, si applicano prima i vincoli geometrici, poi i vincoli dimensionali, e infine si blocca il disegno. Da ricordare: le regole sono fatte per essere infrante. Quando ci sono difficoltà nel manipolare il disegno, può essere utile vincolare alcuni oggetti prima di completare il profilo.
-   Se possibile, centrare il disegno nell\'origine (0,0) con il vincolo **Blocca**. Se il disegno non è simmetrico, posizionare uno dei suoi punti nell\'origine, o scegliere una cifra tonda semplice per le distanze di blocco.
-   Se c\'è la possibilità di scegliere tra il vincolo [lunghezza](Sketcher_ConstrainDistance/it.md) <img alt="" src=images/Constraint_Length.png  style="width:16px;"> e il vincolo [distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> o [distanza verticale](Sketcher_ConstrainDistanceY/it.md) <img alt="" src=images/Constraint_Vertical.png  style="width:16px;">, preferire questi ultimi. I vincoli di distanza orizzontale e verticale sono computazionalmente più economici.
-   In generale, i vincoli migliori da utilizzare sono: Orizzontale e Verticale, Lunghezza Orizzontale e Verticale, Tangente nel punto. Se possibile, limitare l\'uso di questi vincoli: Lunghezza generica, Tangenza Edge-to-edge, Punto su linea; Simmetria.
-   In caso di dubbi sulla validità di uno schizzo una volta completato (le funzioni diventano verdi), chiudere la finestra di dialogo di Sketcher, passare a <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/it.md) ed eseguire <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Controlla la geometria](Part_CheckGeometry/it.md).



## Tutorial

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. Questo è un documento PDF lungo 70 pagine che funge da manuale dettagliato per lo sketcher. Spiega le basi dell\'utilizzo di Sketcher e approfondisce la creazione di forme geometriche e ciascuno dei vincoli.
-   [Tutorial base di Sketcher](Basic_Sketcher_Tutorial/it.md) per principianti
-   [Sketcher Micro Tutorial - Pratica con i vincoli](Sketcher_Micro_Tutorial_-_Constraint_Practices/it.md)
-   [Requisiti di uno schizzo](Sketcher_requirement_for_a_sketch/it.md) Requisito minimo per uno schizzo e definizione completa di uno schizzo



## Script

La pagina [scripting](Sketcher_scripting/it.md) contiene esempi su come creare vincoli da script Python.



## Esempi

Per alcune idee su cosa si può ottenere con gli strumenti di Sketcher, dai un\'occhiata a: [Esempi di Sketcher](Sketcher_Examples/it.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/it
