 

Questa è una lista estesa, ma non completa, delle funzioni (feature) già implementate in FreeCAD. Se siete interessati a conoscere gli sviluppi futuri è possibile consultare il [Piano di sviluppo](Development_roadmap/it.md). Per un approccio sommario alle caratteristiche sono anche disponibili gli [screenshot](Screenshots/it.md).


{{TOCright}}

## Note di rilascio {#note_di_rilascio}

-   [Note di rilascio della versione 0.11](Release_notes_011/it.md) - Marzo 2011
-   [Note di rilascio della versione 0.12](Release_notes_012/it.md) - Dicembre 2011
-   [Note di rilascio della versione 0.13](Release_notes_0.13/it.md) - Gennaio 2013
-   [Note di rilascio della versione 0.14](Release_notes_0.14/it.md) - Marzo 2014
-   [Note di rilascio della versione 0.15](Release_notes_0.15/it.md) - Marzo 2015
-   [Note di rilascio della versione 0.16](Release_notes_0.16/it.md) - Aprile 2016
-   [Note di rilascio della versione 0.17](Release_notes_0.17/it.md) - Aprile 2018
-   [Note di rilascio della versione 0.18](Release_notes_0.18/it.md) - Marzo 2019
-   [Note di rilascio della versione 0.19](Release_notes_0.19/it.md) - Marzo 2021
-   [Note di rilascio della versione 0.20](Release_notes_0.20/it.md) - TBD

## Funzioni principali {#funzioni_principali}


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) Un **kernel geometrico** (nucleo) basato su [OpenCasCade](http://it.wikipedia.org/wiki/Open_CASCADE_Technology) permette operazioni complesse su profili di varia natura, anche molto articolati. È presente il supporto nativo al [BREP](http://it.wikipedia.org/wiki/B-Rep), alle curve e alle superfici [NURBS](http://it.wikipedia.org/wiki/NURBS), una vasta gamma di entità geometriche, di operazioni booleane e raccordi, e il supporto interno per i file STEP e IGES. 

-   ![](images/Feature3.jpg ) Un **modellatore interamente parametrico**. Tutti gli oggetti di FreeCAD sono nativamente parametrici, il che significa che la loro forma può essere basata sulle [proprietà](Property/it.md) e, quando dipendono da altri oggetti, se subiscono delle modifiche possono essere ricalcolati a richiesta, e registrati dall\'albero delle operazioni annulla o ripeti. Possono essere aggiunti facilmente nuovi tipi di oggetti, anche quelli [completamente programmati in Python](Scripted_objects/it.md)

-   ![](images/Feature4.jpg ) Una **architettura modulare** permette di estendere le funzioni del programma attraverso l\'utilizzo dei plugins. Queste estensioni possono essere complesse, come sono le intere nuove applicazioni programmate in C++ o essere semplici, come gli [script Python](Power_users_hub/it.md) o le [macro](macros/it.md) auto-registrate. Attraverso l\'utilizzo della riga di comando integrata nella GUI, è possibile accedere praticamente a tutte le funzionalità del software per mezzo di semplici comandi **Python**. Si possono [creare e/o modificare oggetti geometrici](Topological_data_scripting/it.md), interagire con [l\'ambiente di lavoro](scenegraph/it.md) o addirittura [personalizzare l\'interfaccia grafica](PySide/it.md) del programma. 

-   ![](images/Feature5.jpg ) È possibile importare ed esportare molti dei **formati standard** di rappresentazione 3D, come ad esempio: [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [STL](http://en.wikipedia.org/wiki/STL_(file_format)), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) oppure [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML), oltre al formato nativo di FreeCAD [Fcstd](Fcstd_file_format/it.md). Il livello di compatibilità tra FreeCAD e un formato di file specifico è variabile, dipende dal modulo che lo implementa.

-   ![](images/Feature7.jpg ) Un ambiente di [sketch](Sketcher_Workbench/it.md) dotato di strumenti per disegnare sagome in 2D vincolate. Questa funzionalità permette di vincolare in diversi modi le geometrie tracciate e poi di utilizzarle come base per la costruzione delle forme 3D.

-   ![](images/Feature9.jpg ) Un modulo di [simulazione robotica](Robot_Workbench/it.md) con il quale studiare i movimenti e le traiettorie del manipolatore. È disponibile una interfaccia grafica di questo modulo che permette di manovrare i vari elementi del modello 3D in modo semplice e intuitivo.

-   ![](images/Feature8.jpg ) Un nuovo modulo comodo per creare [fogli di disegno tradizionali](TechDraw_Workbench/it.md) con opzioni come viste di dettagli, sezioni trasversali, quotatura e altre, che consente di inserire delle viste 2D dei modelli 3D su un foglio. Questo modulo produce quindi fogli SVG o PDF pronti per l\'esportazione. Esiste ancora il vecchio modulo [Drawing](Drawing_Workbench/it.md) con i suoi scarni comandi Gui, ma una potente funzionalità Python.

-   ![](images/Feature-raytracing.jpg ) Un modulo dedicato al [rendering](Raytracing_Workbench/it.md) per mezzo del quale si possono esportare i modelli 3D ed effettuare renderizzazioni con software di terze parti. Al momento è pienamente supportato solo [POV-Ray](http://it.wikipedia.org/wiki/POV-Ray).

-   ![](images/Feature-arch.jpg ) Inoltre, è stato avviato lo sviluppo di un modulo di [architettura](Arch_Workbench/it.md) compatibile con il modello [BIM](http://it.wikipedia.org/wiki/Building_Information_Modeling) e compatibile con l\'[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). Le caratteristiche di questo modulo sono ancora in via di definizione e sono discusse dalla comunità in [questa pagina](http://forum.freecadweb.org/viewtopic.php?f=10&t=821) del forum.

-   ![](images/Feature-CAM.jpg ) Un [modulo Path](Path_Workbench/it.md) dedicato alle lavorazioni meccaniche, come la fresatura (CAM), in grado di produrre, visualizzare e modificare il [Codice G](http://en.wikipedia.org/wiki/G-code). 

-   ![](images/Feature_spreadsheet.png ) Il [foglio di calcolo integrato](Spreadsheet_Workbench/it.md) e un [parser delle espressioni](Expressions/it.md) per guidare i modelli basati su formule o recuperare dati dai modelli.


</div>


<div class="mw-translate-fuzzy">

## Funzioni Generali {#funzioni_generali}


</div>

-   **multipiattaforma**. FreeCAD funziona esattamente allo stesso modo su piattaforme Microsoft Windows®, Linux e macOS®.

-   \'\'\'interfaccia grafica completa \'\'\' basata sulla piattaforma [Qt](http://www.qt.io/) e una interfaccia di visualizzazione 3D basata su [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) che garantisce un rendering rapido e permette di accedere facilmente alle varie proiezioni della scena.

-   **funziona tramite riga di comando**. In modalità riga di comando, FreeCAD viene eseguito senza la sua interfaccia ma con tutti i suoi strumenti di geometria. In questa modalità ha un ingombro di memoria relativamente basso e può essere utilizzato, ad esempio, come server per produrre contenuti per altre applicazioni.


<div class="mw-translate-fuzzy">

-   **può essere importato come un [modulo Python](Embedding_FreeCAD/it.md)**. FreeCAD può essere importato in qualsiasi applicazione in grado di eseguire script Python. Come in modalità riga di comando, la parte di interfaccia di FreeCAD non è disponibile, ma tutti gli strumenti di geometria sono accessibili.


</div>

-   **concepito in Ambienti**. Nell\'interfaccia di FreeCAD gli strumenti sono raggruppati all\'interno di [workbenches](workbenches/it.md) (ambienti di lavoro). Questo permette che vengano visualizzati soltanto gli strumenti necessari all\'azione specifica che si deve compiere, ottenendo un\'area di lavoro pulita, facile da gestire e veloce da caricare.

-   **plugins e moduli per il caricamento ritardato di funzioni e dati**. FreeCAD è diviso in un\'applicazione principale con moduli che vengono caricati solo quando è necessario. Quasi tutti gli strumenti e i tipi di geometria sono memorizzati nei moduli. I moduli si comportano come dei plug-in; oltre al caricamento ritardato, è possibile aggiungere o rimuovere singoli moduli da un\'installazione di FreeCAD esistente.

-   **gestione parametrica degli oggetti**. In un documento di FreeCAD tutti gli oggetti possono essere definiti da parametri. Questi parametri possono essere modificati e ricalcolati in qualsiasi momento. Poiché le relazioni tra gli oggetti vengono mantenute, la modifica di un oggetto si propaga automaticamente a qualsiasi oggetto dipendente.

-   **creazione parametrica di primitive**. Gli oggetti primitivi come box, sfere, cilindri, ecc. possono essere creati specificando i loro vincoli geometrici.

-   **operazioni di modifica grafica**. FreeCAD può eseguire traslazioni, rotazione, ridimensionamento, mirroring, offset (triviali o come descritte in [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) o anche trasformazione della forma, in qualsiasi piano dello spazio 3D.

-   **[constructive solid geometry](http://en.wikipedia.org/wiki/Constructive_solid_geometry) (operazioni booleane)**. FreeCAD può eseguire operazioni di geometria solida costruttiva (unione, differenza, intersezione).


<div class="mw-translate-fuzzy">

-   **creazione grafica di geometrie piane**. Linee, spezzate, rettangoli, b-spline e archi circolari o ellittici possono essere creati graficamente in qualsiasi piano dello spazio 3D


</div>

-   **modellazione lineare o rivolutiva** di **estrusioni**, **sezioni** e **raccordi**.

-   **elementi topologici** quali **vertici**, **spigoli**, **contorni** e **piani** facilmente ottenibili anche tramite [script Python](Scripting/it.md).

-   **test e correzione**. FreeCAD dispone di strumenti per il test delle mesh (test solido, test di non-due-varietà, test di auto-intersezione) e per la riparazione di mesh (riempimento del foro, orientamento uniforme).

-   **annotazioni**. FreeCAD può inserire annotazioni per testo o dimensioni.

-   **strumento annulla/ripristina**. In FreeCAD si può annullare o ripristinare tutto tramite l\'accesso diretto allo storico delle azioni. In questo modo è possibile annullare più modifiche contemporaneamente.

-   **gestione delle modifiche**. Lo storico annulla/ripristina conserva le informazioni sulle modifiche globali e non sulla singola azione, così ogni singolo strumento può gestire esattamente ciò che deve essere annullato o ripristinato.

-   **strumento di sviluppo di [script](Scripting/it.md) integrato**. FreeCAD fornisce un interprete [Python](http://www.python.org/) integrato nel programma e delle API che coprono la quasi totalità del programma, come ad esempio l\'interfaccia, la geometria e la visualizzazione 3D. L\'interprete è in grado di gestire singoli comandi così come interi script complessi. Tutti i moduli possono essere gestiti tramite Python.

-   **console Python integrata**. L\'interprete Python include una console completa della funzione di highlight del codice, dell\'auto-completamento e anche del class-browser. I comandi, in python, possono essere inviati direttamente dall\'interno del programma e essere eseguiti immediatamente. Questa funzione è molto utile per testare al volo il funzionamento di uno script, ma anche per esplorare i contenuti dei moduli di FreeCAD integrati e conoscere a fondo il programma stesso.

-   **azioni dell\'utente registrate nella console**. Tutto ciò che l\'utente fa nell\'interfaccia di FreeCAD esegue del codice Python, che può essere stampato sulla console e registrato in una [macro](macros/it.md).

-   **registrazione e editazione di [macro](Macros/it.md).**. I comandi Python generati quando l\'utente manipola l\'interfaccia possono essere registrati, modificati, e se necessario, salvati per essere poi riprodotti in seguito.

-   **formato dei file composto (basato su ZIP)**. I documenti di FreeCAD vengono salvati con un\'estensione {{FileName|.[FCStd](File_Format_FCStd/it.md)}}. Il documento può contenere molti tipi diversi di informazioni come la geometria, gli script o le icone delle miniature. Il file {{FileName|.FCStd}} è esso stesso un contenitore zip; un file di FreeCAD salvato è già stato compresso.

-   **G.U.I. completamente personalizzabile**. L\'interfaccia di FreeCAD è basata su [Qt](https://www.qt.io) ed è completamente configurabile tramite l\'interprete Python. Oltre alle funzioni standard definite nel software, si ha a disposizione la potenze e la versatilità dell\'intero framework Qt, il quale permette di aggiungere, spostare, agganciare oppure eliminare i widgets dall\'area di lavoro.

-   **creazione di miniature** (per ora disponibile solo su piattaforme GNU/Linux). le icone dei documenti salvati in formato [.fcstd](fcstd_file_format/it.md) forniscono una comoda anteprima del loro contenuto in molte applicazioni di gestione dei file, come Nautilus di Gnome, rendendo facile individuare i propri elaborati.

-   **installatore MSI modulare**. L\'installatore di FreeCAD garantisce una installazione flessibile in ambienti Microsoft Windows®. Sono disponibili anche dei pacchetti specifici per Ubuntu.

## Funzioni in fase di sviluppo {#funzioni_in_fase_di_sviluppo}

-   ![](images/Feature-assembly.jpg ) Un modulo di [Assemblaggio](Assembly_project/it.md) che permetta di lavorare contemporaneamente su diverse forme, documenti, file e relazioni\...

Questo modulo è attualmente in fase di progettazione.

## Ambienti complementari {#ambienti_complementari}

Alcuni utenti esperti hanno creato vari [ambienti complementari](external_workbenches/it.md) personalizzati.







[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
