# <img alt="L\'icona di A2plus" src=images/A2p_workbench.svg  style="width:64px;"> A2plus Workbench/it



## Introduzione


{{TOCright}}

A2plus è un [ambiente complementare](External_workbenches/it.md) per [assemblare](Assembly/it.md) varie parti in FreeCAD.

Questa documentazione descrive la versione A2plus **0.4.56 o più recente**.



## Installazione

L\'ambiente A2plus è un componente aggiuntivo di FreeCAD. Può essere facilmente installato tramite il menu **Strumenti → [Addon Manager](Std_AddonMgr/it.md)**. A2plus è in sviluppo attivo e riceve frequentemente nuove funzioni. Pertanto si dovrebbe aggiornarlo regolarmente usando sempre il menu **Strumenti → [Addon Manager](Std_AddonMgr/it.md)**. Il codice A2plus è ospitato e sviluppato in [su GitHub](https://github.com/kbwbe/A2plus) e può anche essere installato manualmente copiandolo nella directory MOD di FreeCAD.



## Per iniziare 

Passare sulla barra degli strumenti di A2plus in FreeCAD. Per creare un assieme, creare un nuovo file. All\'inizio questo file deve essere salvato. Si consiglia (ma non è necessario) di salvarlo nella stessa cartella delle parti che si desidera assemblare.

Ora è possibile aggiungere parti all\'assieme utilizzando il pulsante <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> della barra degli strumenti o <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;">. Il pulsante <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> aggiunge tutti i corpi nel file selezionato come una singola parte. Quando si usa il pulsante <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;"> si può scegliere quale parte di un file deve essere importato come parte. In questo modo si può ad esempio importare solo uno schizzo per assemblare ulteriori parti usando lo schizzo per determinare le posizioni delle parti.

La prima parte aggiunta ottiene una posizione fissa per impostazione predefinita. (in seguito è possibile modificare questo tramite la proprietà della parte **fixed Position**.)

Le parti già presenti nell\'assieme possono essere clonate con il pulsante <img alt="" src=images/A2p_DuplicatePart.svg  style="width:24px;"> della barra degli strumenti.

Per modificare una parte dall\'assieme, selezionarla nell\'albero del modello e utilizzare il pulsante della barra degli strumenti <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Questo apre la parte in una nuova scheda in FreeCAD o passa alla sua scheda se il file è già aperto.

Per aggiornare le parti modificate negli assemblaggi fare clic sul pulsante <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;"> della barra degli strumenti. Il pulsante <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width:24px;"> della barra degli strumenti importa anch\'esso le parti ma ricorsivamente su possibili [sottoassiemi](#Sottoassiemi.md). Se si selezionano una o più parti nella vista ad albero di FreeCAD, A2plus chiederà se aggiornare solo le parti selezionate.

Le parti importate mantengono le loro dipendenze esterne e possono essere modificate. Per parti ben definite, come le viti, è comunque utile che la loro forma non possa essere modificata. Questo può essere ottenuto con il pulsante della barra degli strumenti <img alt="" src=images/_A2p_ConvertPart.svg  style="width:24px;"> che converte la parte selezionata in una copia statica della parte originale.

Per salvare l\'assemblaggio e in seguito chiuderlo, è possibile utilizzare il pulsante <img alt="" src=images/A2p_Save_and_exit.svg  style="width:24px;"> della barra degli strumenti.

Attivando o disattivando il pulsante della barra degli strumenti <img alt="" src=images/A2p_CD_OneButton.svg  style="width:24px;"> si imposta il modo in cui è possibile selezionare diversi bordi, facce ecc.: con un solo click o con **Ctrl**+click.



## Assemblaggio

L\'assemblaggio delle parti viene effettuato aggiungendo dei vincoli tra le parti. Dopo l\'applicazione di un vincolo, A2plus sposta le parti in base al vincolo, se possibile.

Per creare un vincolo tra le parti, tenere premuto il tasto **Ctrl** e selezionare un bordo o una faccia di due parti. Quindi cliccare il bottone del vincolo desiderato nella barra degli strumenti. Apparirà la finestra di dialogo descritta nella sezione [Vincoli](#Vincoli.md). Il vincolo viene aggiunto nell\'albero del modello allegato alle parti interessate.

Per i vincoli complessi tra le parti A2plus potrebbe non riuscire a risolvere i vincoli. Pertanto, dare un\'occhiata anche alla sezione [Risoluzione dei problemi](#Risoluzione_dei_problemi.md) per le strategie su come risolvere tali casi.



### Tenere traccia 

Più parti si aggiungono, più è importante mantenere la traccia. A2plus offre quindi questi strumenti per spostare e visualizzare le parti:

-   Per spostare una parte nell\'assieme, selezionarla nell\'albero del modello e utilizzare il pulsante <img alt="" src=images/A2p_MovePart.svg  style="width:24px;">. Quando la parte è posizionato dove si desidera, fare clic con il tasto sinistro del mouse. Se la parte spostata ha già dei vincoli, la parte viene posizionata di conseguenza premendo il pulsante <img alt="" src=images/A2p_solver.svg  style="width:24px;"> perché questo innesca la risoluzione di tutti i vincoli dell\'assieme.
-   Per mostrare un vincolo selezionarlo nell\'albero del modello e utilizzare il pulsante <img alt="" src=images/A2p_ViewConnection.svg  style="width:24px;">. Ciò rende l\'intero assemblaggio trasparente e evidenzia i due elementi che sono connessi nel vincolo. Per tornare alla visualizzazione normale, fare clic con il tasto sinistro sull\'assieme.
-   Per mostrare solo alcune parti nell\'assieme, selezionare queste parti nell\'albero del modello e utilizzare il pulsante <img alt="" src=images/A2p_Isolate_Element.svg  style="width:24px;">. In alternativa si può nascondere una certa parte selezionandola nell\'albero del modello e premendo **Spazio** per commutare la sua visibilità.
-   Per attivare la vista trasparenza dell\'intero assieme, si può utilizzare il pulsante <img alt="" src=images/A2p_ToggleTransparency.svg  style="width:24px;">.
-   Ogni parte può essere resa trasparente utilizzando la normale modalità di FreeCAD. Tuttavia a volte l\'impostazione della trasparenza per le parti viene persa quando si riapre l\'assieme a causa di un bug in FreeCAD. Per risolvere il problema, si può utilizzare il pulsante <img alt="" src=images/A2p_Restore_Transparency.svg  style="width:24px;"> della barra degli strumenti per ripristinare le impostazioni di trasparenza.



### Vincoli

Quando si crea un vincolo, dopo aver premuto un pulsante della barra degli strumenti dei vincoli, viene visualizzata questa finestra di dialogo:

![](images/A2p_ConstraintPropertiesDialog.png ) 
*Sopra: la finestra di dialogo Proprietà del vincolo di A2plus*

Per alcuni vincoli, consente di modificare la direzione del vincolo. Con il pulsante **<img src="images/A2p_solver.svg" width=24px> Solve** si può verificare in anteprima se questo nuovo vincolo può essere risolto con A2plus. In caso contrario, dare un\'occhiata alla sezione [Risoluzione dei problemi](#Risoluzione_dei_problemi.md).

I vincoli possono essere disabilitati cambiando la loro [visibilità](Std_ToggleVisibility/it.md). Questo si ottiene selezionando il vincolo nella vista ad albero e premendo **Space**. Ciò attiva la proprietà **Suppressed**. Un vincolo soppresso non è preso in considerazione quando l\'assemblaggio viene risolto.

A2plus fornisce i seguenti vincoli:



#### Punto su punto 

Selezionare un [vertice](Glossary#Vertex.md) (punto) su ciascuna parte. Il pulsante della barra degli strumenti <img alt="" src=images/A2p_PointIdentity.svg  style="width:24px;"> aggiunge il vincolo {{Variable|pointIdentity}}. Rende i vertici coincidenti.



#### Punto sul linea 

Selezionare un [vertice](Glossary#Vertex.md) (punto), o [bordo](Glossary#Edge.md) circolare (seleziona il suo punto centrale), o una [faccia](Glossary#Face.md) sferica (seleziona anche il suo punto centrale) su una parte e un [bordo](Glossary#Edge.md) sull\'altra parte. Il pulsante <img alt="" src=images/A2p_PointOnLineConstraint.svg  style="width:24px;"> della barra degli strumenti aggiunge il vincolo {{Variable|pointOnLine}}. Posiziona il vertice sul bordo.



#### Punto su piano 

Selezionare un [vertice](Glossary#Vertex.md) (punto), o [bordo](Glossary#Edge.md) circolare (seleziona il suo punto centrale), o una [faccia](Glossary#Face.md) sferica (seleziona anche il suo punto centrale) su una parte e un piano sull\'altra parte. Il pulsante <img alt="" src=images/A2p_PointOnPlaneConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|pointOnPlane}}. La finestra di dialogo dei vincoli consente di specificare uno scostamento tra il punto e il piano. Questo offset può anche essere capovolto su entrambi i lati del piano. Se l\'offset è zero, il vincolo posiziona il punto sul piano.



#### Sfera su sfera 

Selezionare una [faccia](Glossary#Face.md) sferica o una [vertice](Glossary#Vertex.md) (punto) su entrambe le parti. Il pulsante <img alt="" src=images/A2p_SphericalSurfaceConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|sphereCenterIdent}}. Rende il centro delle sfere, o il centro della sfera e il vertice, o i vertici coincidenti.



#### Bordo circolare sul bordo circolare 

Selezionare un [bordo](Glossary#Edge.md) circolare su entrambe le parti. Il pulsante <img alt="" src=images/A2p_CircularEdgeConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|circularEdge}}. La finestra di dialogo dei vincoli consente di specificare un offset tra i bordi. Questo offset può anche essere invertito. È inoltre possibile impostare la direzione del vincolo e bloccare la rotazione delle parti. Se l\'offset è zero, il vincolo posiziona i bordi concentrici sullo stesso piano.



#### Asse coincidente 

Selezionare una [faccia](Glossary#Face.md) cilindrica o un [bordo](Glossary#Edge.md) lineare su entrambe le parti. Il pulsante <img alt="" src=images/A2p_AxialConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|axisCoincident}}. La finestra di dialogo dei vincoli consente di specificare la direzione dell\'asse. La finestra di dialogo consente inoltre di bloccare la rotazione delle parti. Il vincolo rende coincidenti gli assi o le linee.



#### Asse parallelo 

Selezionare una [faccia](Glossary#Face.md) cilindrica o un [bordo](Glossary#Edge.md) lineare su entrambe le parti. Il pulsante <img alt="" src=images/A2p_AxisParallelConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|axisParallel}}. La finestra di dialogo dei vincoli consente di specificare la direzione dell\'asse. Il vincolo rende paralleli gli assi o le linee.



#### Asse su piano parallelo 

Selezionare una [faccia](Glossary#Face.md) cilindrica o un [bordo](Glossary#Edge.md) lineare su una parte e un piano sull\'altra parte. Il pulsante <img alt="" src=images/A2p_AxisPlaneParallelConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|axisPlaneParallel}}. Il vincolo rende l\'asse o la linea paralleli al piano.



#### Asse su piano normale 

Selezionare una [faccia](Glossary#Face.md) cilindrica o un [bordo](Glossary#Edge.md) lineare su una parte e un piano sull\'altra parte. Il pulsante <img alt="" src=images/A2p_AxisPlaneNormalConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|axisPlaneNormal}}. Il vincolo rende l\'asse o la linea normale rispetto al piano.



#### Asse su angolo piano 

Selezionare una [faccia](Glossary#Face.md) cilindrica o un [bordo](Glossary#Edge.md) lineare su una parte e un piano sull\'altra parte. Il pulsante <img alt="" src=images/A2p_AxisPlaneAngleConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|axisPlaneAngle}}. Il vincolo rende innanzitutto l\'asse parallelo al piano. Poi si può aggiustare l\'angolo dell\'asse nelle impostazioni di vincolo della finestra di dialogo che appare.



#### Piano parallelo 

Selezionare un piano su entrambe le parti. Il pulsante della barra degli strumenti <img alt="" src=images/A2p_PlanesParallelConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|planesParallel}}. La finestra di dialogo dei vincoli consente di specificare la direzione del vincolo. Il vincolo rende paralleli i piani.



#### Piano su piano 

Selezionare un piano su entrambe le parti. Il pulsante della barra degli strumenti <img alt="" src=images/A2p_PlaneCoincidentConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|planeCoincident}}. La finestra di dialogo dei vincoli consente di specificare una direzione del vincolo e un offset tra i piani. Questo offset può anche essere capovolto. Se l\'offset è zero, il vincolo rende i piani coincidenti.



#### Angolo tra i piani 

Selezionare un piano su entrambe le parti. Il pulsante <img alt="" src=images/A2p_AngleConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|angledPlanes}}. La finestra di dialogo dei vincoli consente di specificare un angolo tra i piani. Il vincolo rende i piani paralleli e imposta l\'angolo specificato.



#### Coincidenza al centro di massa 

Selezionare un [bordo](Glossary#Edge.md) chiuso o un piano su entrambe le parti. Il pulsante <img alt="" src=images/A2p_CenterOfMassConstraint.svg  style="width:24px;"> aggiunge il vincolo {{Variable|centerOfMass}}. La finestra di dialogo dei vincoli consente di specificare un offset tra i bordi o i piani. Questo offset può anche essere capovolto. È inoltre possibile impostare la direzione del vincolo e bloccare la rotazione delle parti. Se l\'offset è zero, il vincolo mette i bordi o i piani nello stesso piano.



### Sottoassiemi

Un assieme può contenere altri assiemi. Vengono aggiunti come parti premendo il pulsante <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> della barra degli strumenti e selezionando un file ***.FCStd** contenente un assemblaggio. Tali sottoassiemi possono anche essere modificati come parti utilizzando il pulsante <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Per fasi di assemblaggio più elevate, e in caso di modifiche, accertarsi di aggiornare l\'assieme tramite il pulsante <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">.



## Gestione dei vincoli 

I vincoli che possono essere selezionati vengono visualizzati nella barra degli strumenti e nella finestra di dialogo *Constraint Tools* attivando i pulsanti corrispondenti. La finestra di dialogo *Constraint Tools* si apre tramite il pulsante <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">. È previsto che rimanga aperto per poter aggiungere rapidamente diversi vincoli all\'assieme.

I vincoli esistenti possono essere modificati selezionandoli nell\'albero del modello e quindi facendo doppio clic su di essi o utilizzando il pulsante della <img alt="" src=images/A2p_EditConstraint.svg  style="width:24px;">. Questo apre la finestra di dialogo *Constraint Properties*.

I vincoli possono essere soppressi temporaneamente selezionandoli nell\'albero del modello e cambiando la proprietà **Suppressed** dell\'elemento dell\'albero.

È possibile eliminare i vincoli selezionandoli nell\'albero del modello e premendo **Canc** o selezionando una parte con i vincoli nell\'albero del modello e utilizzando il pulsante <img alt="" src=images/A2p_DeleteConnections.svg  style="width:24px;">.

Tutti i vincoli possono essere risolti in qualsiasi momento con il pulsante <img alt="" src=images/A2p_solver.svg  style="width:24px;">. Se il pulsante della barra degli strumenti <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;"> è attivato, viene eseguita automaticamente una risoluzione dopo ogni modifica di un vincolo.

Il pulsante <img alt="" src=images/A2p_FlipConstraint.svg  style="width:24px;"> ha effetto sull\'ultimo vincolo aggiunto. Capovolge la direzione del vincolo.

Con lo strumento <img alt="" src=images/A2p_CD_ConstraintViewer.svg  style="width:24px;">, è possibile mostrare e ispezionare i vincoli esistenti. Dopo aver fatto click su di esso, viene visualizzata una finestra di dialogo. Quindi selezionare una parte nell\'albero e fare click sul pulsante {{Pulsante|Importa dalla parte}} per ottenere tutti i vincoli di questa parte, oppure selezionare uno o più vincoli nell\'albero e fare click sul pulsante {{Pulsante|Importa dall'albero}}. Di conseguenza si ottengono tutte le informazioni sui vincoli. Cliccando nella colonna *Elimina* è possibile sopprimere un singolo vincolo. Per ulteriori funzionalità, seguire i suggerimenti degli altri pulsanti di dialogo.



## Elenchi delle parti 

Per creare degli elenchi di parti di assiemi, le diverse parti dell\'assieme devono ottenere informazioni sulla parte che possano essere lette da A2plus. Questo viene fatto modificando la parte con il pulsante <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Nella parte aperta premere il pulsante <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;"> per creare un [foglio di calcolo](Spreadsheet_Workbench/it.md) con il nome *#PARTINFO#*.

La struttura del foglio di calcolo è come questa:

![](images/A2p_PartinfoTable.png )

Compilare i campi grigi con le informazioni che si hanno e che si vuole avere nella lista delle parti finali.

Nell\'assemblaggio o nel sottoassieme, utilizzare il pulsante <img alt="" src=images/A2p_PartsList.svg  style="width:24px;">. Viene chiesto se si vuole fare una iterazione ricorsiva su tutti i sottoassiemi. Cliccare su \"Sì\". Questo crea un nuovo foglio di calcolo con il nome *#PARTSLIST#*. Contiene le informazioni dei diversi fogli di calcolo \"#PARTSINFO#\" delle parti in una lista come questa:

![](images/A2p_PartslistTable.png )

La posizione (POS) viene automaticamente impostata in base alla posizione delle parti nell\'albero del modello. La parte di livello superiore ottiene POS 1.

La quantità (QTY) viene calcolata automaticamente dall\'assieme. Se una parte è presente due volte nell\'assieme, ottiene QTY 2.

Se si sono aggiornate delle informazioni sulla parte, è possibile aggiornare di nuovo l\'elenco delle parti premendo nuovamente il pulsante <img alt="" src=images/A2p_PartsList.svg  style="width:24px;">.

Per i sottoassiemi è anche possibile creare un foglio di calcolo delle informazioni utilizzando il pulsante <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;">. Quando si crea o si aggiorna l\'elenco delle parti dell\'assieme principale, queste informazioni vengono utilizzate se si clicca su \"No\" alla domanda se si desidera ripetere l\'iterazione ricorsiva su tutti i sottoassiemi. Quindi le diverse parti non sono nell\'elenco delle parti ma solo nei sottoassiemi.



## Funzioni speciali 



### Struttura dell\'assemblaggio 

Il pulsante <img alt="" src=images/A2p_Treeview.svg  style="width:24px;"> crea un file HTML con la struttura dell\'assieme. Per impostazione predefinita il file viene creato nella cartella del file dell\'assemblaggio. La struttura assomiglia a questa: ![](images/A2p_Dependency-Tree.jpg )

:   ![](images/A2p_Dependency-Tree.jpg )



### Gradi di libertà 

Il pulsante <img alt="" src=images/A2p_DOFs.svg  style="width:24px;"> etichetta tutte le parti dell\'assieme con i loro gradi di libertà. Inoltre genera una lista con tutte le parti e le loro dipendenze. L\'elenco viene visualizzato nel widget di FreeCAD *Vista Report*. Se questo widget non è visibile, può essere mostrato facendo clic con il pulsante destro del mouse su una parte vuota dell\'area della barra degli strumenti di FreeCAD e quindi selezionandolo nel menu di scelta rapida visualizzato o con il menu **Visualizza → Pannelli → [Vista report](Report_view/it.md)**.

Le etichette dei gradi di libertà possono essere rimosse facendo nuovamente clic sul pulsante <img alt="" src=images/A2p_DOFs.svg  style="width:24px;">.



### Etichette delle parti 

Il pulsante <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;"> contrassegna nella vista 3D ogni parte dell\'assieme con il proprio nome. Le etichette delle parti possono essere rimosse facendo nuovamente clic sul pulsante <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;">.



### Forma dell\'intero assemblaggio 

A volte è necessario avere l\'intero assemblaggio combinato in una unica forma. Questa forma può quindi essere utilizzata ad esempio per la stampa 3D nell\'ambiente [Mesh](Mesh_Workbench/it.md) o per i disegni nell\'ambiente [TechDraw](TechDraw_Workbench/it.md). Viene creata utilizzando il pulsante della barra degli strumenti <img alt="" src=images/A2p_SimpleAssemblyShape.svg  style="width:24px;">. Di default la forma non è visibile. Utilizzare lo stesso pulsante della barra degli strumenti per aggiornare la forma in caso di modifiche all\'assieme.



### Convertire i percorsi assoluti in relativi 

Con il menu **A2plus → Misc → [<img src=images/A2p_SetRelativePathes.svg style="width:24px"> Convert absolute paths of imported parts to relative ones** si possono convertire i percorsi assoluti delle parti importate in quelli relativi.



## Preferenze

Le preferenze di A2plus sono accessibili tramite il menu di FreeCAD **Modifica → [Preferenze](Preferences_Editor/it.md)**, nella sezione *A2plus*. È possibile impostare le seguenti opzioni:



### Metodo di risoluzione predefinito 

Use solving of partial systems : Il risolutore inizia con una parte che ha la proprietà **fixed Position** impostata su \"true\" e una parte vincolata ad essa. Tutte le altre parti non sono calcolate. Se è possibile trovare una soluzione, la successiva parte vincolata viene aggiunta e calcolata e così via.
Use \"magnetic\" solver, solving all parts at once : Il risolutore cerca di spostare tutte le parti contemporaneamente in direzione di una parte che ha la proprietà **fixed Position** impostata su \"true\". Notare che nella maggior parte dei casi questo richiede più tempo per il calcolo di una soluzione.
Force fixed position : Questo imposta per tutte le parti dell\'assieme la proprietà **fixed Position** su *true*. Quindi non viene praticamente eseguito nessun calcolo poiché tutte le parti sono sempre fissate nelle posizioni in cui sono state create.



### Comportamento predefinito del risolutore 

Risolve automaticamente se una proprietà di vincolo viene modificata: il risolutore verrà avviato automaticamente. Lo stesso che attivare il pulsante della barra degli strumenti <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;">.



### Comportamento durante l\'aggiornamento delle parti importate 

Recalculate imported parts before updating them : Tutte le parti dell\'assieme, compresi i sottoassiemi, vengono aperte in FreeCAD per essere ricostruite utilizzando i valori dei fogli di calcolo.
Questa funzione è progettata per vincolare in modo completamente parametrico. **Nota:** Questa funzione è molto sperimentale e non è consigliata per progetti importanti.
Problemi noti:

-   L\'assemblaggio può essere distrutto a causa di riferimenti errati ai nomi topologici nelle parti.
-   I fogli di calcolo Master possono rompersi quando vengono modificati mentre un file di una parte di riferimento è già stato chiuso. Questo può causare un arresto anomalo di FreeCAD.

Enable recursive update of imported parts : Apre tutti i sottoassiemi in modo ricorsivo per aggiornarli.





Use experimental topological naming : Durante l\'importazione di parti nell\'assieme, un algoritmo genera dei nomi topologici per ciascun sottoelemento della forma importata. I nomi topologici sono scritti in **mux Info**. Quando è necessario aggiornare una parte importata, questi nomi topologici vengono utilizzati per aggiornare i sottoelementi dei vincoli. Quindi gli assemblaggi diventano più robusti rispetto ai numeri volatili dei sottoelementi di FreeCAD.
**Nota:** Questo aumenta però le dimensioni dei file e il tempo di calcolo durante l\'importazione delle parti. Se è necessario utilizzare la denominazione topologica, bisogna attivarla prima di creare l\'assemblaggio.





Inherit per face transparency from parts and subassemblies : Usa le impostazioni di colore e la trasparenza delle parti importate.
**Nota:** Questa funzione è ancora molto sperimentale e non consigliata per progetti importanti.





Do not import invisible shapes : Questo nasconde le forme di costruzione o di riferimento invisibili. **Nota:** Nessun vincolo deve essere collegato alle origini o agli oggetti di costruzione in sottoinsiemi o in insiemi superiori, altrimenti l\'assemblaggio puoi rompersi.





Use solid union for importing parts and subassemblies : Tutte le parti importate vengono create direttamente come unione.
Questa funzione è utile per le [FEM](FEM_Workbench/it.md) o per la [stampa 3D](Manual:Preparing_models_for_3D_printing/it.md) se è consentito un solo solido. L\'alternativa è creare in seguito una [Forma dell\'intero assemblaggio](A2plus_Workbench/it#Forma_dell.27intero_assemblaggio.md).



### Impostazioni dell\'interfaccia utente 

Show constraints in toolbar : Per risparmiare spazio, se questa opzione non viene utilizzata, i pulsanti della barra degli strumenti per i diversi vincoli non sono visibili. È comunque possibile impostare dei nuovi vincoli utilizzando la finestra di dialogo *Constraint Tools* (il pulsante <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">) della barra degli strumenti.
Use native file manager of your OS : Se questa opzione è usata, viene visualizzato la finestra di dialogo dei file del proprio sistema operativo quando si selezionano i file per gli assemblaggi.



### Archiviazione dei file 

Use relative paths for imported parts : Utilizza i percorsi dei file relativi ai file delle parti.
Use absolute paths for imported parts : Utilizza i percorsi di file assoluti per i file delle parti.
All files are in this project folder : Tutti i file del progetto devono trovarsi nella cartella specificata. Non importa se si trovano in sottocartelle di questa cartella. **Nota:** Nessun file può esistere più volte nella cartella (ad esempio in diverse sottocartelle).
Questa opzione è utile per lavorare su macchine diverse perché in questo caso è sufficiente copiare la cartella del progetto.



## Risoluzione dei problemi 

Prima o poi si incontrano dei problema che A2plus non può risolvere i vincoli che sono stati imposti. Per superare questo, ci sono diverse strategie:



### Utilizzo dello strumento di ricerca dei conflitti 

Questo è il metodo più sicuro quando si hanno diversi vincoli perché questo strumento tenta di risolvere un vincolo dopo l\'altro finché non trova il vincolo in conflitto. Quindi si può continuare utilizzando altre strategie per risolvere il vincolo identificato. Lo strumento viene richiamato utilizzando il pulsante <img alt="" src=images/A2p_SearchConstraintConflicts.svg  style="width:24px;"> della barra degli strumenti.



### Controllo della direzione dei vincoli 

Talvolta i vincoli sembrano essere coerentemente definiti, tuttavia non possono essere risolti. Un esempio: si supponga di avere un set di vincoli {{Variable|[planesParallel](A2plus_Workbench/it#Piano_parallelo.md)}} per due piani. Ora si vuole impostare per gli stessi piani il vincolo {{Variable|[planeCoincident](A2plus_Workbench/it#Piano_su_piano.md)}} e A2plus non può risolverlo. Questo succede perchè le direzioni dei vincoli di {{Variable|[planesParallel](A2plus_Workbench/it#Piano_parallelo.md)}} e di {{Variable|[planeCoincident](A2plus_Workbench/it#Piano_su_piano.md)}} sono diverse. Utilizzare la stessa direzione per entrambi i vincoli per risolvere questo problema.

A2plus permette di controllare automaticamente la giusta direzione per **tutti** i vincoli dell\'assieme utilizzando il pulsante <img alt="" src=images/A2p_ReAdjustConstraints.svg  style="width:24px;"> della barra degli strumenti.



### Eliminazione dei vincoli 

La maggior parte dei casi di vincoli irrisolvibili si verifica direttamente quando si aggiunge un nuovo vincolo. La soluzione è quindi eliminare il vincolo aggiunto per ultimo. A2plus lo propone anche.

A volte la strategia di cancellazione dei vincoli è l\'unica applicabile, ad esempio quando si modifica una parte in FreeCAD in modo che dopo mancano facce o spigoli collegati a vincoli. Si dovrebbe quindi eliminare uno dopo l\'altro i vincoli che sono collegati alla parte modificata. Usare il pulsante della barra degli strumenti <img alt="" src=images/A2p_solver.svg  style="width:24px;"> dopo ogni cancellazione per vedere se si è raggiunto uno stato risolvibile.

Quando si ottiene un assemblaggio che può essere risolto, aggiungere passo dopo passo i vincoli necessari.



### Parti mobili 

In alcuni casi, il risolutore necessita solo di valori di avvio migliori per risolvere i vincoli. Prendiamo ad esempio il caso che si abbia una parte asse e una parte ruota. Si aggiunge un vincolo {{Variable|axisCoincident }} e non si ottiene alcuna informazione che il risolutore abbia avuto esito negativo, ma le parti non vengono spostate di conseguenza e nel widget *Vista Report* di FreeCAD viene visualizzato \"*REACHED POS-ACCURACY :0.0*\". Una soluzione per questo è spostare le parti più vicino alla posizione che si desidera ottenere dal vincolo.

**Nota:** Assicurarsi che almeno una parte del vincolo abbia la proprietà **fixed Position** impostata su *false*.



### Impostazione della proprietà Tip - Entità finale 

Se dopo l\'importazione in un assieme di A2plus mancano alcune funzioni della parte, controllare la proprietà **[Tip - Entità finale](PartDesign_MoveTip/it.md)**.

A2plus importa i corpi delle parti con tutte le loro funzioni fino alla funzione finale, la funzione Tip. Questo è sensato perché impostare la funzione finale su una determinata funzione significa che tutte le funzioni sottostanti la funzione finale non dovrebbero apparire nell\'entità finale. Quindi se in A2plus si perde una parte di funzioni, aprire la parte tramite il pulsante <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">, selezionare un corpo e guardare la sua proprietà **Tip**. Se l\'entità finale non è nella funzione in cui la si desidera, fare clic con il pulsante destro del mouse sulla funzione in cui dovrebbe trovarsi e scegliere **[<img src=images/PartDesign_MoveTip.png style="width:24px"> Set tip**. Infine salvare la parte e ricaricare l\'assieme usando il pulsante <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">.



### Riparare l\'albero dell\'assieme 

Se non si riesce a trovare una ragione chiara per cui alcuni vincoli non possono essere risolti, si può provare a utilizzare il pulsante <img alt="" src=images/A2p_RepairTree.svg  style="width:24px;">. Questo risolve tutti i vincoli e li raggruppa di nuovo sotto le diverse parti.



### Migrare vecchi assemblaggi A2plus 

Assemblaggi creati con versioni di A2plus precedenti marzo 2019 non mostrano le icone corrette per le parti importate e hanno propietà obsolete. Questi assemblaggi devono essere migrati ad A2plus versione 0.4.35 o superiore usando il menù **A2plus → Misc → [<img src=images/A2p_Upgrade.svg style="width:24px"> Migrate proxies of imported parts**. Dopo aver fatto ciò, si può salvare e riaprire il file d\'assemblaggio.



### Evitare i caratteri accentati 

**Questa strategia non è necessaria per Windows.**

Su alcuni sistemi operativi si possono avere problemi se i nomi dei file o i percorsi dei file delle parti o dell\'assieme contengono caratteri accentati. Quindi evitare tali caratteri e tutti i caratteri speciali in generale.



### Posizione di fissaggio 

**Questa strategia non è più necessaria per gli assemblaggi creati con A2plus 0.3.11 o successivi perché ora A2plus presenta un avvertimento per le posizioni fisse mancanti.**

Quando si imposta un vincolo tra due parti e nessuna parte ha la proprietà **fixed Position** impostata su *true* o è connessa da un vincolo a un\'altra parte con **fixed Position** impostato su *true*, il vincolo non può essere risolto. Lo stesso accade se entrambe le parti del vincolo hanno **fixed Position** impostata su *true*.

In questi casi A2plus restituisce l\'informazione che la soluzione non è possibile, ma a volte si vede solo che le parti non vengono spostate di conseguenza e nel widget *Report* di FreeCAD viene visualizzato \"*REACHED POS-ACCURACY :0.0*\". Ciò significa che il risolutore ha completato la risoluzione senza errori, ma che in realtà non è stato in grado di risolvere i vincoli.

Pertanto, verificare che almeno una delle parti nell\'assieme abbia **fixed Position** impostata su \"true\". Quindi assicurarsi di impostare solo i vincoli su una parte che è in qualche modo collegata alla parte fissa. Per visualizzare queste dipendenze, vedere la sezione [Struttura dell\'assemblaggio](A2plus_Workbench/it#Struttura_dell.27assemblaggio.md).



### Parti rotanti 

**Questa strategia non è più necessaria per gli assiemi creati con A2plus 0.4.0 o successivi perché ora A2plus ruota le parti automaticamente un po\' in background per ottenere un angolo iniziale sufficiente per il risolutore.**

Il risolutore spesso fallisce con il vincolo {{Variable|angledPlanes}} se i due piani selezionati hanno un angolo attuale di 0 ° o 180 °. (Le parti non vengono spostate di conseguenza e nel widget *Report* di FreeCAD si vede \"*REACHED POS-ACCURACY :0.0*\".) Una soluzione per questo è di ruotare una parte di alcuni gradi usando la funzione Trasforma di FreeCAD (fare clic con il tasto destro sulla parte nell\'albero del modello e selezionare **Transform** nel menu di scelta rapida).

**Nota:** Assicurarsi che almeno una parte del vincolo abbia la proprietà **fixed Position** impostata su *false*.



## Animazione

A2plus offre animazioni tramite trascinamento e tramite script Python.



### Trascinamento

Le animazioni di trascinamento sono interattive poiché vengono attivate trascinando una parte dell\'assieme. Per ottenere questo tipo di animazioni:

1.  Vincolare completamente la parte il cui movimento o rotazione deve essere animato
2.  Fare click sul pulsante della barra degli strumenti <img alt="" src=images/A2p_MovePartUnderConstraints.svg  style="width:24px;">. Ciò abilita la modalità di trascinamento.
3.  Fare clic sulla parte desiderata nell\'assieme.
4.  Ora si può spostare il mouse e la parte seguirà il movimento del mouse all\'interno dei vincoli definiti.
5.  Per terminare la modalità di trascinamento, fare clic con il pulsante sinistro del mouse nell\'assieme o premere ESC.

Ecco un assieme di esempio per provare l\'animazione di trascinamento: [A2p_example-for-dragging-animation.FCStd](https://forum.freecadweb.org/download/file.php?id=99204)

![](images/A2p_dragging-animation-result.gif )



*Above: The dragging animation using the example assembly*

### Scripting

Nonostante la modalità di trascinamento offra belle animazioni interattive, a volte non sono abbastanza precise per screencast o video. Le animazioni con script hanno il vantaggio di animare i movimenti e le rotazioni in modo definito. Ad esempio, si può ruotare una parte esattamente di 10° avanti e indietro. Gli esempi seguenti utilizzano un assieme in cui una parte deve essere ruotata. Se si prova ad animarlo usando la modalità di trascinamento, si nota quanto è difficile ottenere una rotazione avanti e indietro che può ad es. essere usata in una presentazione. Con lo script di esempio interattivo, tuttavia, questo è un compito facilitato.

Un\'animazione con script funziona solitamente in questo modo:

1.  L\'assieme è completamente vincolato
2.  Lo script modifica un parametro, ad esempio la posizione o l\'angolo di rotazione di una parte
3.  Dopo la modifica del parametro, i vincoli di assieme vengono risolti
4.  I passaggi 2. e 3. vengono ripetuti per ottenere l\'animazione

È anche possibile modificare invece di un parametro di posizionamento un vincolo, ad esempio la distanza tra 2 piani.



#### Semplice Script di esempio 

Il modo più semplice per scrivere un\'animazione è un\'animazione non interattiva che segue un movimento definito. Ecco un esempio: Per prima cosa scarica questo file di assieme: [A2p_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) e anche questo script Python: [/file.php?id=97981 A2p_animation-example-script.py](https://forum.freecadweb.org/download).


<div class="mw-collapsible mw-collapsed toccolours">

Questo è il contenuto dello script e le righe che iniziano con un \'#\' descrivono cosa fanno le diverse righe dello script:


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide
import A2plus.a2p_solversystem as a2p_solver

# we use steps of 1 degree
step = 1
# wait 1 ms between every step
timeout = 0.001
# initial angle is 0 degree
angle = 0
# we take the currently opened document
document = FreeCAD.activeDocument()
# we want later change the rotation angle of the part "star_wheel_001"
starWheel = document.getObject("star_wheel_001")
# define a progress dialog running from 0 to 360
progressDialog = PySide.QtGui.QProgressDialog(u"Animation progress", u"Stop", 0, 360)

# the while block is the main loop to change the angle and solve
# the assembly constraints subsequently
while angle < 360: # run this loop until we have one full turn (360 degrees)
    # increase the rotation angle
    angle += step
    # set the new angle to the progress dialog
    progressDialog.setValue(angle)
    # change the rotation angle of the part "star_wheel_001"
    starWheel.Placement.Rotation.Angle = math.radians(angle)
    # solve the constraints 
    a2p_solver.solveConstraints(document, useTransaction=True)
    # update the view after the solving ('Gui' stands for 'graphical user interface')
    FreeCADGui.updateGui()
    # bring the progress dialog to front
    PySide.QtGui.QWidget.raise_(progressDialog)
    # if 'Stop' was pressed in the dialog, exit the loop
    if progressDialog.wasCanceled():
        angle = 360
    # wait some time before performing the next step
    time.sleep(timeout)
```


</div>


</div>

To use the script to perform the animation, we must

1.  Open the assembly file in FreeCAD.
2.  Open the script file in FreeCAD.
3.  Click on the toolbar button <img alt="" src=images/Menu_Std_DlgMacroExecute_fr_02.png  style="width:24px;"> to execute the script (also called macro).
4.  Change to the tab of the assembly to see the rotation.

Per esercitarti, basta cambiare qualcosa nello script ed eseguirlo in seguito. Ad esempio aumentare *passo* a *5*.

Questo è il risultato dell\'animazione di esempio:

![](images/A2p_animated-example-result.gif )

#### Interactive Script Example 

The first script example demonstrated how to create an animation without any user feedback. For most applications you need to interact with the animation. For example the interesting issue in the example is to see how the driving pins cross the center groove of the wheel. To have a closer look you might present this detail to your colleagues or boss. Therefore you need an interactive solution.

This can be done by using a custom animation dialog with a slider. By moving the slider you can set the rotation angle and therefore rotate back and forth at interesting position.

We use the same assembly file: [A2p_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) and this Python script: [A2p_animation-example-script.py](https://forum.freecadweb.org/download/file.php?id=97982).


<div class="mw-collapsible mw-collapsed toccolours">

This is the content of the script to get the interactive animation dialog:


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide, sys
import FreeCAD.A2plus.a2p_solversystem as a2p_solver
from FreeCAD import Units
from PySide import QtCore, QtGui

# wait 1 ms after every calculation
timeout = 0.001
# we take the currently opened document
document = FreeCAD.activeDocument()
# we want later change the rotation angle of the part "star_wheel_001"
starWheel = document.getObject("star_wheel_001")

class AnimationDlg(QtGui.QWidget): # the animation dialog

    def __init__(self): # to initialize the dialog
        super(AnimationDlg, self).__init__()
        self.initUI()

    def initUI(self): # the definition of the dialog components
        self.setMinimumSize(self.minimumSizeHint()) # set the minimal dialog size to minimum
        self.setWindowTitle('Animation Dialog')
        # use a grid layout for the whole form
        self.mainLayout = QtGui.QGridLayout()
        self.lineNo = 0 # first dialog grid line
        # add description label
        DescriptionLabel = QtGui.QLabel(self)
        DescriptionLabel.setText("Change slider to change rotation angle")
        self.mainLayout.addWidget(DescriptionLabel,self.lineNo,0,1,4)
         # next dialog grid line
        self.lineNo += 1
        # add a label; there is no need for the "self." prefix because we don't want to change the label later
        LabelMin = QtGui.QLabel(self)
        LabelMin.setText("Min")
        LabelMin.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMin,self.lineNo,0)
        # add a spin edit to define the slider minimum
        self.MinEdit = QtGui.QSpinBox(self)
        # get the angle unit as string
        self.MinEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MinEdit.setMaximum(999)
        self.MinEdit.setMinimum(0)
        self.MinEdit.setSingleStep(10)
        self.MinEdit.setValue(0)
        self.MinEdit.setFixedHeight(32)
        self.MinEdit.setToolTip("Minimal angle for the slider")
        QtCore.QObject.connect(self.MinEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMinEdit)
        self.mainLayout.addWidget(self.MinEdit,self.lineNo,1)
        # add the slider
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.setFixedHeight(32)
        self.slider.setToolTip("Move the slider to change the rotation angle")
        QtCore.QObject.connect(self.slider, QtCore.SIGNAL("sliderMoved(int)"), self.handleSliderValue)
        self.mainLayout.addWidget(self.slider,self.lineNo,2)
        # add a label
        LabelMax = QtGui.QLabel(self)
        LabelMax.setText("Max")
        LabelMax.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMax,self.lineNo,3)
        # add a spin edit to define the slider maximum
        self.MaxEdit = QtGui.QSpinBox(self)
        # get the angle unit as string
        self.MaxEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MaxEdit.setMaximum(999)
        self.MaxEdit.setMinimum(1)
        self.MaxEdit.setSingleStep(10)
        self.MaxEdit.setValue(360)
        self.MaxEdit.setFixedHeight(32)
        self.MaxEdit.setToolTip("Maximal angle for the slider")
        QtCore.QObject.connect(self.MaxEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMaxEdit)
        self.mainLayout.addWidget(self.MaxEdit,self.lineNo,4)
         # next dialog grid line
        self.lineNo += 1
        # add a spacer
        self.mainLayout.addItem(QtGui.QSpacerItem(10,10), 0, 0)
        # add a label
        LabelCurrent = QtGui.QLabel(self)
        LabelCurrent.setText("Current angle:")
        LabelCurrent.setFixedHeight(32)
        self.mainLayout.addWidget(LabelCurrent,self.lineNo,1)
        # output the current angle
        self.CurrentAngle = QtGui.QLineEdit(self)
        self.CurrentAngle.setText(str(0))
        self.CurrentAngle.setFixedHeight(32)
        self.CurrentAngle.setToolTip("Current rotation angle")
        self.CurrentAngle.isReadOnly()
        self.mainLayout.addWidget(self.CurrentAngle,self.lineNo,2)
        # add label for the unit
        LabelUnit = QtGui.QLabel(self)
        LabelUnit.setText("deg")
        LabelUnit.setFixedHeight(32)
        self.mainLayout.addWidget(LabelUnit,self.lineNo,3)
        # button to close the dialog
        self.Close = QtGui.QPushButton(self)
        self.Close.setText("Close")
        self.Close.setFixedHeight(32)
        self.Close.setToolTip("Closes the dialog")
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL("clicked()"), self.CloseClicked)
        self.mainLayout.addWidget(self.Close,self.lineNo,4)
        # place the defined grid layout to the dialog
        self.setLayout(self.mainLayout)
        self.update()

    def handleSliderValue(self):
        # set slider value as angle
        starWheel.Placement.Rotation.Angle = math.radians(self.slider.value())
        # output current angle
        self.CurrentAngle.setText(str(self.slider.value()))
        # solve the constraints 
        a2p_solver.solveConstraints(document)
        # update the view after the solving ('Gui' stands for 'graphical user interface')
        FreeCADGui.updateGui()
        # wait some time, important to give time to perform calculations
        time.sleep(timeout)

    def setMinEdit(self):
        # assure that the minimum is samller than the maximum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MaxEdit.setValue(self.MinEdit.value() + 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def setMaxEdit(self):
        # assure that the minimum is samller than the maximum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MinEdit.setValue(self.MaxEdit.value() - 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def CloseClicked(self):
        AnimationDialog.close()

# create and show the defined dialog
AnimationDialog = AnimationDlg()
AnimationDialog.show()

# run this loop when the dialog is visible
while AnimationDialog.isVisible():
    # update the view; important to give the OS feedback the dialog is alive
    FreeCADGui.updateGui()
    # bring the dialog to front, so that the dialog is always visible
    QtGui.QWidget.raise_(AnimationDialog)
    # output slider value here too because during the calculation the slider might have been moved
    AnimationDialog.CurrentAngle.setText(str(AnimationDialog.slider.value()))
```


</div>


</div>

The dialog defined in the script looks like this:

![](images/A2p_AnimationDialog.png )

### Script Commands 

To understand the script syntax better, here is some command info: 
```python starWheel.Placement.Rotation.Angle = math.radians(angle)```

Here we change the placement property `Rotation.Angle` of the part get got previously as `starWheel`. This property gets the angle as [radian](https://en.wikipedia.org/wiki/Radian). The function `radians()` from the library `math` converts the angle from degree to radian.

The property `Rotation.Angle` uses the current placement axis of the part (in our example the X-axis). To rotate the part e.g. around the Z-axis one can set the rotation axis (before calling the rotation command) using the command: 
```python starWheel.Placement.Rotation.Axis = FreeCAD.Vector(0,0,1)``` Instead of rotating, parts can also be moved. To change for example the placement in Y-direction of the wheel, the command would be: 
```python starWheel.Placement.Base.y = PositionShift``` In this case we would not define the variable `angle` but `PositionShift` that we change on every loop run.

There are different ways to set the placement of a part. Some are [ documented here](Placement.md). Unfortunately there is no list (yet) with all possible placement commands. 
```pythona2p_solver.solveConstraints(document, useTransaction=False/True)```

This is an A2plus-specific command. It solves the assembly constraints of the assembly we previously got as `document`. The option `useTransaction` specifies if FreeCAD should store every change in the undo/redo stack. For large animations you might therefore set it to `False`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > A2plus Workbench/it
