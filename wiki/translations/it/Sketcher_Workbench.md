# <img alt="L\'icona dell\'ambiente Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/it






## Introduzione

Con <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> l\'[Ambiente Sketcher](Sketcher_Workbench/it.md) è possibile creare schizzi 2D destinati all\'uso in altri ambienti di lavoro. Gli schizzi 2D sono il punto di partenza per molti modelli CAD. In genere definiscono i profili e i percorsi per le operazioni di creazione di forme 3D. Un modello può dipendere da diversi schizzi per la sua forma finale.

Insieme alle operazioni booleane definite in <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Ambiente Part](Part_Workbench/it.md), l\'ambiente Sketcher, o \"The Sketcher\" in breve, costituisce la base della [geometria solida costruttiva](Constructive_solid_geometry/it.md) (CSG) metodo di costruzione dei solidi. Insieme alle operazioni in <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Ambiente PartDesign](PartDesign_Workbench/it.md), costituisce anche la base della metodologia di [modifica delle funzioni](Feature_editing/it.md) per la creazione di solidi. Ma anche molti altri ambienti di lavoro utilizzano gli schizzi.

L\'ambiente Sketcher mette a disposizione i [vincoli](#Vincoli.md), che consentono alle forme 2D di seguire precise definizioni geometriche in termini di lunghezza, angoli e relazioni (orizzontalità, verticalità, perpendicolarità, ecc.). Un risolutore di vincoli calcola l\'estensione vincolata della geometria 2D e consente l\'esplorazione interattiva dei gradi di libertà dello schizzo.

Sketcher non è destinato alla produzione di progetti 2D. Una volta utilizzati gli schizzi per generare una lavorazione solida, questi vengono automaticamente nascosti e i vincoli sono visibili solo in modalità Modifica schizzo. Se si ha solo bisogno di produrre viste 2D per la stampa e non si vuole creare modelli 3D, dare un\'occhiata all\'[Ambiente Draft](Draft_Workbench/it.md).

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Uno schizzo base, completamente vincolato‎.*



## Vincoli

I vincoli vengono utilizzati per limitare i gradi di libertà di un oggetto. Ad esempio, una linea senza vincoli ha 4 gradi di libertà (abbreviati in \"DoF\"): può essere spostata orizzontalmente o verticalmente, può essere allungata e può essere ruotata.

Applicando a una linea un vincolo orizzontale o verticale, oppure un vincolo angolare (rispetto ad un\'altra linea o ad uno degli assi) si limita la sua capacità di ruotare, lasciandola quindi con solo 2 gradi di libertà. Bloccando uno dei suoi punti rispetto all\'origine si rimuove un ulteriore grado di libertà. Applicando un vincolo dimensionale si rimuove l\'ultimo grado di libertà. A questo punto, la linea è quindi considerata **completamente vincolata**.

Gli oggetti possono essere vincolati gli uni rispetto agli altri. Due linee possono essere unite attraverso uno dei loro punti con il vincolo del punto coincidente. È possibile impostare un angolo tra di loro oppure possono essere impostati perpendicolari. Una linea può essere tangente ad un arco o ad un cerchio e così via. Uno schizzo complesso con più oggetti può avere diverse soluzioni e renderlo **completamente vincolato** può significare che solo una di queste possibili soluzioni è stata raggiunta in base ai vincoli applicati.

Ci sono due tipi di vincoli: geometrici e dimensionali. Essi sono descritti nella successiva sezione dedicata agli [Strumenti](#Strumenti.md).



### Modificare i vincoli 

Quando viene creato un [vincolo dimensionale di guida](Sketcher_ToggleDrivingConstraint/it.md) e se la [preferenza](Sketcher_Preferences/it#Display.md) **Richiedi il valore dopo la creazione di un vincolo dimensionale** è selezionata (impostazione predefinita), si apre una finestra di dialogo per modificarne il valore.

![](images/Sketcher_Edit_Constraint.png )

È possibile inserire un valore numerico o una [espressione](Expressions/it.md), ed è possibile nominare il vincolo per facilitarne l\'utilizzo in altre espressioni. È anche possibile selezionare la casella di controllo **Riferimento** per commutare il vincolo in [modalità riferimento](Sketcher_ToggleDrivingConstraint/it.md).

Per modificare il valore di un vincolo dimensionale esistente, effettuare una delle seguenti operazioni:

-   Fare doppio clic sul valore del vincolo nella [vista 3D](3D_view/it.md).
-   Fare doppio clic sul vincolo nella [Finestra di dialogo di Sketcher](Sketcher_Dialog/it.md).
-   Fare clic con il pulsante destro del mouse sul vincolo nella finestra di dialogo di Sketcher e selezionare l\'opzione **Cambia valore** dal menu contestuale.



### Riposizionare i vincoli 

I vincoli dimensionali possono essere riposizionati nella vista 3D trascinandoli. Tenere premuto il pulsante sinistro del mouse sul valore del vincolo e spostare il mouse. I simboli dei vincoli geometrici vengono posizionati automaticamente e non possono essere spostati.



## Schizzi di profili 

Per creare uno schizzo che può essere utilizzato come profilo per generare solidi è necessario seguire alcune regole:

-   Lo schizzo deve contenere solo contorni chiusi. Non sono consentiti spazi tra i punti finali, per quanto piccoli.
-   I contorni possono essere annidati per creare vuoti, ma non devono autointersecarsi o intersecare altri contorni.
-   I contorni non possono condividere i bordi con altri contorni. I bordi duplicati devono essere evitati.
-   Non sono consentite connessioni a T, ovvero più di due bordi che condividono un punto comune, o un punto che tocca un bordo.

Queste regole non si applicano alle geometrie di costruzione (colore predefinito blu), che non viene mostrata al di fuori della modalità di modifica o se lo schizzo viene utilizzato per uno scopo diverso. A seconda dell\'ambiente di lavoro e dello strumento che utilizzerà lo schizzo del profilo, potrebbero essere applicate ulteriori restrizioni.



## Aiuti per il disegno 

L\'ambiente Sketcher dispone di numerosi aiuti al disegno e altre funzionalità che possono essere utili durante la creazione della geometria e l\'applicazione dei vincoli.



### Modalità continua 

Sono disponibili due tipi di modalità continua: **Crea la geometria usando la \"Modalità continua\"** e **Creazione dei vincoli con \"Modalità continua\"**. Se questi sono selezionati nelle [preferenze](Sketcher_Preferences/it#Visualizzazione.md) (impostazione predefinita), gli strumenti correlati verranno riavviati al termine. Per uscire da una modalità continua premere **Esc** o il pulsante destro del mouse. Questo deve essere ripetuto se uno strumento di geometria in modalità continua ha già ricevuto un input. È inoltre possibile uscire da uno strumento continuo avviando un altro strumento di creazione di geometria o vincoli. Tenere presente che premendo **Esc** quando nessuno strumento è attivo si uscirà dalla modalità di modifica dello schizzo. Deselezionare **Esc permette di uscire dalla modalità di modifica dello schizzo** nelle [preferenze](Sketcher_Preferences/it#Generale.md) se si preme spesso inavvertitamente **Esc** troppe volte.



### Vincoli automatici 

Per gli schizzi in cui è selezionata l\'opzione **Vincoli automatici** (impostazione predefinita) diversi vincoli vengono applicati automaticamente. L\'icona di un vincolo automatico proposto viene visualizzata accanto al cursore quando è posizionato correttamente. Facendo clic con il pulsante sinistro del mouse verrà quindi applicato quel vincolo. Questa è un\'impostazione per schizzo che può essere modificata nella [finestra di dialogo di Sketcher](Sketcher_Dialog/it#Vincoli.md) o modificando la [proprietà](Property_editor/it.md) **Autoconstraints** dello schizzo.

I seguenti vincoli vengono applicati automaticamente:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincidente](Sketcher_ConstrainCoincident/it.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Orizzontale](Sketcher_ConstrainHorizontal/it.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Verticale](Sketcher_ConstrainVertical/it.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangente](Sketcher_ConstrainTangent/it.md)

-    {{Version/it|1.0}}: <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Simmetria](Sketcher_ConstrainSymmetric/it.md) (punto medio della linea)



### Aggancio


{{Version/it|0.21}}

È possibile [agganciare](Sketcher_Snap/it.md) alle linee della griglia e alle intersezioni della griglia, ai bordi della geometria e ai punti medi di linee e archi e a determinati angoli. Tenere presente che l\'aggancio (snap) non produce vincoli di per sé. Ad esempio, solo se l\'opzione [Vincoli automatici](#Vincoli_automatici.md) è attivata, l\'aggancio a un bordo produrrà un [Vincolo punto sull\'oggetto](Sketcher_ConstrainPointOnObject/it.md). Ma anche solo scegliere un punto sul bordo avrebbe lo stesso risultato.



### Parametri On-View 


{{Version/it|1.0}}

A seconda dell\'opzione selezionata nelle [preferenze](Sketcher_Preferences/it#Generale.md) possono essere abilitati solo i parametri On-View dimensionali o sia i parametri On-View dimensionali che quelli posizionali. I parametri di posizionali consentono l\'immissione di coordinate esatte, ad esempio il centro di un cerchio o il punto iniziale di una linea. I parametri dimensionali consentono l\'inserimento di dimensioni esatte, ad esempio il raggio di un cerchio o la lunghezza e l\'angolo di una linea. I parametri On-View non sono disponibili per tutti gli strumenti.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determinazione del punto centrale di un cerchio con i parametri posizionali abilitati*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determinazione del raggio di un cerchio con i parametri dimensionali abilitati*

Se i valori vengono immessi e confermati premendo **Enter** o **Tab**, i relativi vincoli vengono aggiunti automaticamente. Se vengono visualizzati due parametri contemporaneamente, ad esempio le coordinate X e Y di un punto, è possibile inserire un valore e selezionare un punto per definire l\'altro. A seconda dell\'oggetto potrebbero essere necessari vincoli aggiuntivi per vincolarlo completamente. I vincoli risultanti dai parametri On-View hanno la precedenza su quelli che possono risultare da [Vincoli automatici](Sketcher_Dialog/it#Vincoli.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arco creato inserendo tutti i parametri On-View con i risultanti vincoli creati automaticamente*



### Visualizzazione delle coordinate 

Se **Mostra le coordinate accanto al cursore durante la modifica** [preferenza](Sketcher_Preferences/it#Visualizzazione.md) è selezionato (impostazione predefinita), i parametri dello strumento di geometria corrente (coordinate, raggio o lunghezza e angolo) vengono visualizzati accanto al cursore. Questo è disattivato mentre vengono visualizzati i parametri On-View.



## Metodi di selezione 

Mentre uno schizzo è in modalità di modifica è possibile utilizzare i seguenti metodi di selezione:



### Selezione elemento nella Vista 3D 

Come altrove in FreeCAD, un elemento può essere selezionato nella [Vista 3D](3D_view/it.md) con un singolo clic sinistro del mouse. Ma non è necessario tenere premuto il tasto **Ctrl** quando si selezionano più elementi. Tuttavia, tenere premuto quel tasto è possibile e ha il vantaggio di poter fare clic in modo errato senza perdere la selezione. Bordi, punti e vincoli possono essere selezionati in questo modo.



### Selezione con riquardo nella Vista 3D 

La selezione con riquadro nella vista 3D funziona senza utilizzare [Std BoxSelection](Std_BoxSelection/it.md) o [Std BoxElementSelection](Std_BoxElementSelection/it.md):

1.  Assicursi che nessuno strumento sia attivo.
2.  Effettuare una delle seguenti operazioni:
    -   Fare clic in un\'area vuota e trascinare un rettangolo da sinistra a destra per selezionare gli elementi che si trovano completamente all\'interno del rettangolo.
    -   Fare clic in un\'area vuota e trascinare un rettangolo da destra a sinistra per selezionare anche gli elementi che toccano o attraversano il rettangolo.

È possibile selezionare tramite riquadro bordi e punti, i vincoli non possono essere selezionati tramite in questo modo.



### Selezione della geometria collegata nella Vista 3D 


{{Version/it|1.0}}

Facendo doppio clic su un bordo nella vista 3D verranno selezionati tutti i bordi direttamente e indirettamente collegati a quel bordo tramite i punti finali. Non è necessario che i bordi siano collegati con [Vincoli coincidenti](Sketcher_ConstrainCoincident/it.md), i punti finali devono solo avere le stesse coordinate.



### Selezione tramite la finestra Dialogo di Sketcher 

I bordi e i punti possono anche essere selezionati dalla sezione Elementi della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md) e i vincoli dalla sezione Vincoli di quella stessa finestra.



## Copia, taglia e incolla 


{{Version/it|1.0}}

Le scorciatoie da tastiera standard, **Ctrl**+**C**, **Ctrl**+**X** e **Ctrl**+**V **, possono essere utilizzate per copiare, tagliare e incollare la geometria dello Sketcher selezionata, inclusi i relativi vincoli. Ma questi strumenti sono disponibili anche dal menu **Sketch → Strumenti Sketcher**. Possono essere utilizzati all\'interno dello stesso schizzo ma anche tra schizzi diversi o istanze separate di FreeCAD. Poiché i dati vengono copiati negli appunti sotto forma di codice Python, possono essere utilizzati anche in altri modi (ad esempio condivisi sul forum).



## Strumenti

Gli strumenti dell\'Ambiente Sketcher si trovano nel menu Sketch e/o in diverse barre degli strumenti. {{Version/it|0.21}}: quasi tutte le barre degli strumenti di Sketcher vengono visualizzate soltanto se uno schizzo è in modalità di modifica. L\'unica eccezione è che la [barra degli strumenti di Sketcher](#Sketcher_toolbar.md) viene visualizzata soltanto se nessuno schizzo è in modalità di modifica.

Alcuni strumenti sono disponibili anche dal menu contestuale [Vista 3D](3D_view/it.md) mentre uno schizzo è in modalità di modifica o dai menu contestuali della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).


{{Version/it|0.21}}

: se uno schizzo è in modalità di modifica, la barra degli strumenti Struttura è nascosta perché nessuno dei suoi strumenti può essere utilizzato.



### Generale



#### Barra degli strumenti di Sketcher 

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Crea schizzo](Sketcher_NewSketch/it.md): crea un nuovo schizzo e apre la finestra [Dialogo Sketcher](Sketcher_Dialog.md) per modificarlo.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Modifica schizzo](Sketcher_EditSketch/it.md): apre la finestra di Dialogo Sketcher per modificare uno schizzo esistente.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Associa schizzo](Sketcher_MapSketch/it.md): associa uno schizzo alla geometria selezionata.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Riposiziona schizzo](Sketcher_ReorientSketch/it.md): posiziona uno schizzo su uno dei piani principali con un offset opzionale. Può essere utilizzato anche per staccare uno schizzo.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Convalida lo schizzo](Sketcher_ValidateSketch/it.md): Può analizza e riparare uno schizzo che non è più modificabile o ha vincoli non validi o aggiungere vincoli coincidenti mancanti.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Unisci schizzi](Sketcher_MergeSketches/it.md): Unisce due o più schizzi.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎‎‎  style="width:32px;"> [Rifletti schizzo](Sketcher_MirrorSketch/it.md): Specchia gli schizzi lungo i loro assi X, Y o l\'origine.



#### Barra degli strumenti in Modalità modifica di Sketcher 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg‎‎  style="width:32px;"> [Esci](Sketcher_LeaveSketch/it.md): Termina la modalità di modifica dello schizzo e chiude la finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Vista normale allo schizzo](Sketcher_ViewSketch/it.md): allinea la [Vista 3D](3D_view/it.md) con lo schizzo.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Vista in sezione](Sketcher_ViewSection/it.md): attiva o disattiva un piano di sezione temporaneo che nasconde eventuali oggetti e parti di oggetti davanti al piano dello schizzo.



#### Barra degli strumenti di modifica di Sketcher 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Attiva/Disattiva la griglia](Sketcher_Grid/it.md): attiva o disattiva la griglia nello schizzo attualmente in fase di modifica. Le impostazioni possono essere modificate nel relativo menu. {{Version/it|0.21}}

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Attiva/Disattiva aggancio](Sketcher_Snap/it.md): Attiva/disattiva l\'aggancio (snap) in tutti gli schizzi. Le impostazioni possono essere modificate nel relativo menu. {{Version/it|0.21}}

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configura l\'ordine di rendering](Sketcher_RenderingOrder/it.md): L\'ordine di rendering di tutti gli schizzi può essere modificato nel relativo menu. {{Version/it|0.21}}



#### Altro

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Interrompi l\'operazione](Sketcher_StopOperation/it.md): Arresta qualsiasi geometria attualmente in esecuzione o strumento di creazione di vincoli.



### Geometrie Sketcher 

Gli strumenti per creare gli oggetti.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Punto](Sketcher_CreatePoint/it.md): Crea un punto.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilinea](Sketcher_CreatePolyline/it.md): Crea una serie di segmenti di linea e arco collegati dai loro punti finali. Lo strumento ha diverse modalità.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Linea](Sketcher_CreateLine/it.md): Crea una linea. {{Version/it|1.0}}: lo strumento ha tre modalità.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea arco:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arco dal centro](Sketcher_CreateArc/it.md): Crea un arco in base al suo centro e ai suoi punti finali. {{Version/it|1.0}}: O dai suoi punti finali e da un punto lungo l\'arco.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arco per tre punti](Sketcher_Create3PointArc/it.md): Disegna un arco da due punti finali e un punto della circonferenza.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arco di ellisse](Sketcher_CreateArcOfEllipse/it.md): Crea un arco di ellisse.

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arco di iperbole](Sketcher_CreateArcOfHyperbola/it.md): Crea un arco di iperbole.

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arco di parabola](Sketcher_CreateArcOfParabola/it.md): Crea un arco di parabola.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea cerchio/ellisse:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Cerchio dal centro](Sketcher_CreateCircle/it.md): Crea un cerchio in base al suo centro e un punto lungo la circonferenza. {{Version/it|1.0}}: O da tre punti lungo la circonferenza.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Cerchio per 3 punti](Sketcher_Create3PointCircle/it.md): Crea un cerchio per tre punti lungo la circonferenza. {{Version/it|1.0}}: Questo è lo stesso strumento di [Cerchio dal centro](Sketcher_CreateCircle/it.md) ma con una modalità iniziale diversa.

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellisse dal centro](Sketcher_CreateEllipseByCenter/it.md): Crea un\'ellisse in base al centro, un punto finale di uno dei suoi assi e un punto lungo l\'ellisse. {{Version/it|1.0}}: O da entrambi i punti finali di uno dei suoi assi e da un punto lungo l\'ellisse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellisse per 3 punti](Sketcher_CreateEllipseBy3Points.md): Crea un\'ellisse in base ai punti finali di uno dei suoi assi e un punto lungo l\'ellisse. {{Version/it|1.0}}: Questo è lo stesso strumento di [Ellisse dal centro](Sketcher_CreateEllipseByCenter/it.md) ma con una modalità iniziale diversa.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea rettangolo:

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rettangolo](Sketcher_CreateRectangle/it.md): Crea un rettangolo. {{Version/it|1.0}}: lo strumento ha quattro modalità. Gli angoli arrotondati e la creazione di una copia sfalsata sono funzioni opzionali.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rettangolo centrato](Sketcher_CreateRectangle_Center/it.md): Crea un rettangolo centrato. {{Version/it|1.0}}: Questo è lo stesso strumento di [Rettangolo](Sketcher_CreateRectangle/it.md) ma con una modalità iniziale diversa.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rettangolo arrotondato](Sketcher_CreateOblong/it.md): Crea un rettangolo arrotondato. Idem.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea poligono regolare:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangolo](Sketcher_CreateTriangle/it.md): crea un triangolo equilatero. {{Version/it|1.0}}: Questo è lo stesso strumento di [Poligono regolare](Sketcher_CreateRegularPolygon/it.md) ma con il numero di lati preimpostato su un valore specifico.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Quadrato](Sketcher_CreateSquare/it.md): Crea un quadrato. Idem.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagono](Sketcher_CreatePentagon/it.md): Crea un pentagono. Idem.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Esagono](Sketcher_CreateHexagon/it.md): Crea un esagono. Idem.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Ettagono](Sketcher_CreateHeptagon/it.md): Crea un ettagono. Idem.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Ottagono](Sketcher_CreateOctagon/it.md): Crea un ottagono. Idem.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Poligono regolare](Sketcher_CreateRegularPolygon/it.md): crea un poligono regolare. È possibile specificare il numero dei lati.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Asola:

  - <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Asola](Sketcher_CreateSlot/it.md): Crea un\'asola.

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Asola ad arco](Sketcher_CreateArcSlot/it.md): Crea un\'asola ad arco. {{Version/it|1.0}}

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline dai punti di controllo](Sketcher_CreateBSpline/it.md): Crea una curva B-spline dai punti di controllo. {{Version/it|1.0}}: O per punti nodo.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [B-spline periodica dai punti di controllo](Sketcher_CreatePeriodicBSpline/it.md): Crea una curva B-spline periodica (chiusa) dai punti di controllo. {{Version/it|1.0}}: Questo è lo stesso strumento di [B-spline dai punti di controllo](Sketcher_CreateBSpline/it.md) ma con una modalità iniziale diversa.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline per i nodi](Sketcher_CreateBSplineByInterpolation/it.md): Crea una curva B-spline per i punti nodo. Idem

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [B-spline periodica per i nodi](Sketcher_CreatePeriodicBSplineByInterpolation/it.md): crea una curva B-spline periodica (chiusa) per i punti nodo. Idem.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Geometria di costruzione](Sketcher_ToggleConstruction/it.md): Attiva/disattiva gli strumenti di creazione della geometria nella/dalla modalità di costruzione oppure attiva/disattiva la geometria selezionata nella/dalla geometria di costruzione.



### Vincoli dello Schizzo 

Questi sono strumenti per creare [vincoli](#Constraints/it.md). Alcuni vincoli richiedono l\'uso di [Vincoli di supporto](Sketcher_helper_constraint/it.md).

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Vincoli dimensionali:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimensione](Sketcher_Dimension/it.md): E\' lo strumento di vincolo sensibile al contesto dell\'ambiente Sketcher. In base alla selezione attuale, offre vincoli dimensionali adeguati, ma anche vincoli geometrici. {{Version/it|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md): Fissa la distanza orizzontale tra due punti o i punti finali di una linea. Se viene preselezionato un punto singolo, la distanza è relativa all\'origine dello schizzo.

  - <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md): Fissa la distanza verticale tra due punti o i punti finali di una linea. Se viene preselezionato un punto singolo, la distanza è relativa all\'origine dello schizzo.

  - <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distanza](Sketcher_ConstrainDistance/it.md): Fissa la lunghezza di una linea, la distanza tra due punti, la distanza perpendicolare tra un punto e una linea; oppure, {{Version/it|0.21}}, la distanza tra i bordi di due cerchi o archi, o tra il bordo di un cerchio o arco e una linea; o, {{Version/it|1.0}}, la lunghezza di un arco.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Raggio/diametro automatico](Sketcher_ConstrainRadiam/it.md): Fissa il raggio degli archi e dei cerchi di peso B-spline e il diametro dei cerchi. 

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Raggio](Sketcher_ConstrainRadius/it.md): Fissa il raggio di cerchi, archi e cerchi di peso B-spline.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diametro](Sketcher_ConstrainDiameter/it.md): Fissa il diametro di cerchi e archi.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angolo](Sketcher_ConstrainAngle/it.md): Fissa l\'angolo tra due bordi, l\'angolo di una linea con l\'asse orizzontale dello schizzo o l\'angolo di apertura di un arco circolare.

  - <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Fissa](Sketcher_ConstrainLock/it.md): Applica i vincoli [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) e [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) ai punti. Se viene selezionato un singolo punto, i vincoli fanno riferimento all\'origine dello schizzo. Se vengono selezionati due o più punti, i vincoli fanno riferimento all\'ultimo punto della selezione.

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincidente (unificato)](Sketcher_ConstrainCoincidentUnified/it.md): Crea un vincolo coincidente tra punti, fissa punti su bordi o assi o crea un vincolo concentrico. Combina gli strumenti [Coincidente](Sketcher_ConstrainCoincident/it.md) e [Punto sull\'oggetto](Sketcher_ConstrainPointOnObject/it.md). {{Version/it|1.0}}

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/it.md): Crea un vincolo coincidente tra punti o un vincolo concentrico.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md): Fissa i punti sui bordi o sugli assi.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Vincoli orizzontali/verticali:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Orizzontale/verticale](Sketcher_ConstrainHorVer/it.md): Vincola le linee o le coppie di punti ad essere orizzontali o verticali, a seconda di quale sia il più vicino all\'allineamento corrente. Combina gli strumenti [Orizzontale](Sketcher_ConstrainHorizontal/it.md) e [Verticale](Sketcher_ConstrainVertical/it.md). {{Version/it|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Orizzontale](Sketcher_ConstrainHorizontal/it.md): Vincola le linee o le coppie di punti ad essere orizzontali.

  - <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Verticale](Sketcher_ConstrainVertical/it.md): Vincola le linee o le coppie di punti ad essere verticali.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallelo](Sketcher_ConstrainParallel/it.md): Vincola le linee ad essere parallele.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicolare](Sketcher_ConstrainPerpendicular/it.md): Vincola due linee ad essere perpendicolari, o due bordi, o un bordo e un asse, ad essere perpendicolari alla loro intersezione. Il vincolo può anche connettere due bordi, costringendoli ad essere perpendicolari in corrispondenza del giunto.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente o collineare](Sketcher_ConstrainTangent/it.md): Vincola due bordi, o un bordo e un asse, ad essere tangenti. Il vincolo può anche connettere due bordi, costringendoli ad essere tangenti in corrispondenza del giunto. Se vengono selezionate due linee, vengono rese collineari.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Uguale](Sketcher_ConstrainEqual/it.md): Vincola i bordi ad avere la stessa lunghezza (linee) o curvatura (altri bordi eccetto le B-spline).

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Simmetrico](Sketcher_ConstrainSymmetric/it.md): Vincola due punti in modo che siano simmetrici intorno ad una linea o asse o intorno ad un terzo punto.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Blocca](Sketcher_ConstrainBlock/it.md): Blocca i bordi sul posto con un singolo vincolo. È destinato principalmente alle B-spline.

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Rifrazione (legge di Snell)](Sketcher_ConstrainSnellsLaw/it.md): Vincola due linee a seguire la legge di rifrazione della luce mentre penetra attraverso un\'interfaccia.

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Attiva/disattiva i vincoli:

  - <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Attiva/disattiva vincolo di guida/riferimento](Sketcher_ToggleDrivingConstraint/it.md): Attiva/disattiva gli strumenti di creazione dei vincoli dimensionali tra la modalità guida e quella di riferimento oppure attiva/disattiva i vincoli dimensionali selezionati tra tali modalità.

  - <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Attiva/disattiva vincolo](Sketcher_ToggleActiveConstraint/it.md): Attiva/disattiva i vincoli selezionati.



### Strumenti dello Sketcher 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea raccordo/smusso:

  - <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Raccordo](Sketcher_CreateFillet/it.md): Crea un raccordo tra due bordi non paralleli. {{Version/it|1.0}}: Lo strumento può anche creare uno smusso.

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Smusso](Sketcher_CreateChamfer/it.md): Crea uno smusso tra due bordi non paralleli. È lo stesso strumento di [Raccordo](Sketcher_CreateFillet/it.md) ma con una modalità iniziale diversa. {{Version/it|1.0}}

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Modifica bordo:

  - <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Rifila](Sketcher_Trimming/it.md): rifila/taglia un bordo alle intersezioni più vicine con altri bordi.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Dividi](Sketcher_Split/it.md): Divide un bordo trasferendo la maggior parte dei vincoli.

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Estendi](Sketcher_Extend/it.md): Estende o accorcia una linea o un arco in una posizione arbitraria o su un bordo o punto di destinazione.

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometria esterna](Sketcher_External/it.md): proietta bordi e/o vertici appartenenti ad oggetti esterni allo schizzo sul piano dello schizzo. {{VersionMinus/it|1.0}}

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Geometria esterna:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Crea geometria di proiezione esterna](Sketcher_Projection/it.md): Crea bordi di proiezione della geometria esterna. {{Version/it|1.1}}

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Crea geometria di intersezione esterna](Sketcher_Intersection/it.md): Crea bordi di intersezione della geometria esterna con il piano dello schizzo. {{Version/it|1.1}}

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Copia carbone](Sketcher_CarbonCopy/it.md): Copia tutta la geometria e i vincoli da un altro schizzo nello schizzo attivo.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg‎  style="width:32px;"> [Seleziona l\'origine](Sketcher_SelectOrigin/it.md): Seleziona l\'origine dello schizzo.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg‎  style="width:32px;"> [Seleziona l\'asse orizzontale](Sketcher_SelectHorizontalAxis/it.md): Seleziona l\'asse orizzontale dello schizzo.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg‎  style="width:32px;"> [Seleziona l\'asse verticale](Sketcher_SelectVerticalAxis/it.md): Seleziona l\'asse verticale dello schizzo.

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Trasformazione polare](Sketcher_Rotate/it.md): TBD. {{Version/it|0.22}}


</div>

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometria](Sketcher_Offset/it.md): aggiunge un contorno equidistante attorno ai bordi selezionati. {{Version/it|0.22}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg‎  style="width:32px;"> [Simmetria](Sketcher_Symmetry/it.md): Copia un elemento dello schizzo in modo simmetrico rispetto ad una linea a scelta.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Rimuove l\'allineamento degli assi](Sketcher_RemoveAxesAlignment/it.md): Rimuovere l\'allineamento degli assi mentre cerca di preservare la relazione di vincolo della selezione. {{Version/it|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Cancella tutta la geometria](Sketcher_DeleteAllGeometry/it.md): Elimina tutta la geometria dallo schizzo.


</div>

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Elimina tutti i vincoli](Sketcher_DeleteAllConstraints/it.md): Elimina tutti i vincoli dallo schizzo.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).



### Strumenti Sketcher B-spline 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Converti la geometria in B-spline](Sketcher_BSplineApproximate/it.md): Converte una geometria, i bordi e le curve compatibili in una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Aumenta il grado della B-spline](Sketcher_BSplineIncreaseDegree/it.md): Aumenta il grado (ordine) di una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Diminuisci il grado della B-spline](Sketcher_BSplineDecreaseDegree/it.md): Diminuisce il grado (ordine) di una B-spline.


</div>

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Aumenta la molteplicità di nodo](Sketcher_BSplineIncreaseKnotMultiplicity/it.md): Aumenta la molteplicità di un nodo B-spline.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Diminuisci la molteplicità](Sketcher_BSplineDecreaseKnotMultiplicity/it.md): Diminuisce la molteplicità di un nodo B-spline.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Inserisci il nodo](Sketcher_BSplineInsertKnot/it.md): Inserisce un nodo in una B-spline esistente. {{Version/it|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Unisci curve](Sketcher_JoinCurves/it.md): Unisce due curve nei punti finali selezionati. {{Version/it|0.21}}


</div>



### Visualizzazione dello Schizzo 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Seleziona i DOF svincolati](Sketcher_SelectElementsWithDoFs/it.md): Evidenzia in verde la geometria con gradi di libertà (DOFs), cioè non completamente vincolata.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg‎  style="width:32px;"> [Seleziona i vincoli associati](Sketcher_SelectConstraints/it.md): Seleziona i vincoli di un elemento dello schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg‎  style="width:32px;"> [Seleziona la geometria associata](Sketcher_SelectElementsAssociatedWithConstraints/it.md): Evidenzia gli elementi dello schizzo associati ai vincoli selezionati.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg‎  style="width:32px;"> [Seleziona i vincoli ridondanti](Sketcher_SelectRedundantConstraints/it.md): Seleziona i vincoli ridondanti di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg‎  style="width:32px;"> [Seleziona i vincoli in conflitto](Sketcher_SelectConflictingConstraints/it.md): Seleziona i vincoli in conflitto di uno schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Mostra/nascondi l\'aiuto circolare per gli archi](Sketcher_ArcOverlay/it.md): TBD. {{Version/it|0.22}}


</div>

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Mostra/nascondi i gradi della B-spline](Sketcher_BSplineDegree/it.md): Mostra o nasconde la visualizzazione del grado di una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Mostra/nascondi i poligoni di controllo della B-spline](Sketcher_BSplinePolygon/it.md): Mostra o nasconde la visualizzazione del poligono che definisce una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Mostra/nascondi il pettine di curvatura](Sketcher_BSplineComb/it.md): Mostra o nasconde la visualizzazione del pettine di curvatura di una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Mostra/nascondi le molteplicità di nodo B-spline](Sketcher_BSplineKnotMultiplicity/it.md): Mostra o nasconde la visualizzazione della molteplicità dei nodi di una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [ Mostra/nascondi il valore dei punti di controllo delle B-spline ](Sketcher_BSplinePoleWeight/it.md): Mostra o nasconde la visualizzazione dei pesi per i punti di controllo di una B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg‎  style="width:32px;"> [Mostra/nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md): Ricrea la geometria interna mancante o eliminata non necessaria di un\'ellisse selezionata, o arco di ellisse o iperbole o parabola o B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg‎  style="width:32px;"> [Cambia spazio virtuale](Sketcher_SwitchVirtualSpace/it.md): Permette di nascondere i vincoli e renderli nuovamente visibili.


</div>



### Strumenti obsoleti 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg‎  style="width:32px;"> [Clona](Sketcher_Clone/it.md): Clona un elemento dello schizzo.


</div>

-   <img alt="" src=images/Sketcher_CloseShape.svg‎  style="width:32px;"> [Chiudi forma](Sketcher_CloseShape/it.md): Crea una forma chiusa applicando vincoli coincidenti ai punti finali. Non disponibile dalla {{VersionPlus/it|0.21}}.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Raccorda schizzo preservando i vincoli](Sketcher_CreatePointFillet/it.md): Crea un raccordo tra due linee non parallele preservandone l\'intersezione (virtuale).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg‎  style="width:32px;"> [Collega segmenti](Sketcher_ConnectLines/it.md): Collega gli elementi dello sketcher applicando vincoli coincidenti ai punti finali. Non disponibile dalla {{VersionPlus/it|0.21}}.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg‎  style="width:32px;"> [Copia](Sketcher_Copy/it.md): Copia un elemento dello schizzo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Sposta](Sketcher_Move/it.md): Sposta la geometria selezionata prendendo come riferimento l\'ultimo punto selezionato.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg‎  style="width:32px;"> [Matrice rettangolare](Sketcher_RectangularArray/it.md): Crea una matrice con gli elementi dello schizzo selezionati.


</div>



## Preferenze


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferences\...](Sketcher_Preferences/it.md): Preferenze disponibili per l\'ambiente Sketcher.


</div>




<div class="mw-translate-fuzzy">

## Migliori Pratiche 


</div>


<div class="mw-translate-fuzzy">

Ogni utente CAD, nel corso del tempo, sviluppa un proprio modo di lavorare, ma ci sono alcuni criteri generali che è utile seguire.


</div>


<div class="mw-translate-fuzzy">

-   Una serie di schizzi semplici è più facile da gestire rispetto a un unico schizzo molto complesso. Ad esempio, si può creare un primo schizzo per produrre (con una estrusione o una rivoluzione) la forma 3D di base, poi un secondo schizzo per eseguire i fori o le aperture (tasche). Alcuni dettagli possono essere omessi e realizzati in seguito come operazioni 3D. È possibile decidere di evitare gli smussi nel disegno, se ce ne sono troppi, e aggiungerli dopo come caratteristica 3D.
-   Creare sempre un profilo chiuso altrimenti il disegno non produrrà un solido, bensì una serie di facce aperte. Quando si desidera escludere alcuni oggetti nella creazione del solido, trasformarli in elementi di costruzione con lo strumento **Modalità costruzione**.
-   Utilizzare la funzione **Vincoli automatici** per ridurre il numero di vincoli da inserire manualmente.
-   Come regola generale, si applicano prima i vincoli geometrici, poi i vincoli dimensionali, e infine si blocca il disegno. Da ricordare: le regole sono fatte per essere infrante. Quando ci sono difficoltà nel manipolare il disegno, può essere utile vincolare alcuni oggetti prima di completare il profilo.
-   Se possibile, centrare il disegno nell\'origine (0,0) con il vincolo **Blocca**. Se il disegno non è simmetrico, posizionare uno dei suoi punti nell\'origine, o scegliere una cifra tonda semplice per le distanze di blocco.
-   Se c\'è la possibilità di scegliere tra il vincolo [lunghezza](Sketcher_ConstrainDistance/it.md) <img alt="" src=images/Constraint_Length.png  style="width:16px;"> e il vincolo [distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> o [distanza verticale](Sketcher_ConstrainDistanceY/it.md) <img alt="" src=images/Constraint_Vertical.png  style="width:16px;">, preferire questi ultimi. I vincoli di distanza orizzontale e verticale sono computazionalmente più economici.
-   In generale, i vincoli migliori da utilizzare sono: Orizzontale e Verticale, Lunghezza Orizzontale e Verticale, Tangente nel punto. Se possibile, limitare l\'uso di questi vincoli: Lunghezza generica, Tangenza Edge-to-edge, Punto su linea; Simmetria.
-   In caso di dubbi sulla validità di uno schizzo una volta completato (le funzioni diventano verdi), chiudere la finestra di dialogo di Sketcher, passare a <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/it.md) ed eseguire <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Controlla la geometria](Part_CheckGeometry/it.md).


</div>



## Tutorial

-   [Sketcher Lecture](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. Questo è un documento PDF lungo più di 80 pagine che funge da manuale dettagliato per lo Sketcher. Spiega le basi dell\'utilizzo di Sketcher e approfondisce la creazione di forme geometriche e ciascuno dei vincoli.
-   [Tutorial base di Sketcher](Basic_Sketcher_Tutorial/it.md) per principianti
-   [Sketcher Micro Tutorial - Pratica con i vincoli](Sketcher_Micro_Tutorial_-_Constraint_Practices/it.md)
-   [Requisiti di uno schizzo](Sketcher_requirement_for_a_sketch/it.md) Requisito minimo per uno schizzo e definizione completa di uno schizzo



## Script

La pagina [scripting](Sketcher_scripting/it.md) contiene esempi su come creare vincoli da script Python.



## Esempi

Per alcune idee su cosa si può ottenere con gli strumenti di Sketcher, dai un\'occhiata a: [Esempi di Sketcher](Sketcher_Examples/it.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/it
