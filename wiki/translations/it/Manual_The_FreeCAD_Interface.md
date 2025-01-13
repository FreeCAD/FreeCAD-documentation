# Manual:The FreeCAD Interface/it
{{Manual:TOC}}

FreeCAD è basato sul [Qt framework](https://en.wikipedia.org/wiki/Qt_(software)) ed è caratterizzato da un\'interfaccia semplice e diretta. Gli utenti CAD più esperti saranno in grado di identificare le somiglianze con altri software, mentre i nuovi utenti troveranno facile navigare e scoprire le varie opzioni offerte da FreeCAD. Ecco l\'aspetto predefinito di FreeCAD:

![](images/FreeCAD_022_Start.png )

La Pagina Iniziale funge da schermata di benvenuto, progettata per facilitare un accesso rapido e semplice alle aree principali di FreeCAD che un utente potrebbe voler esplorare. Attraverso essa, gli utenti possono creare facilmente nuove parti, aprire file recenti e avviare il disegno 2D. Inoltre, offre scorciatoie a risorse utili come tutorial e forum di utenti, che sono preziosi sia per i principianti che per gli utenti esperti in cerca di indicazioni o suggerimenti. Gli utenti possono facilmente personalizzare l\'aspetto della pagina iniziale in base alle proprie preferenze.

Man mano che si diventa più esperti con FreeCAD, si potrebbero modificare le impostazioni nelle preferenze. Con questo è possibile configurare FreeCAD per aprirsi direttamente in uno degli ambienti di lavoro con un nuovo documento pronto all\'uso quando lo si avvia. In alternativa, è possibile semplicemente chiudere la scheda Pagina Iniziale e creare manualmente un nuovo documento.

![](images/FreeCAD_022_PartDesign.png )



### Gli Ambienti di lavoro 

FreeCAD utilizza un sistema chiamato \"Ambienti di lavoro\" (Workbenches), simile alle strutture concettuali utilizzate nei software di progettazione avanzata come Revit o CATIA. L\'idea di un ambiente di lavoro è analoga alle stazioni specializzate di un laboratorio scientifico, dove diverse postazioni di lavoro sono attrezzate per tipi distinti di esperimenti. In un laboratorio si potrebbe avere un\'area dedicata alla chimica, un\'altra alla biologia e una terza alla fisica, ciascuna dotata degli strumenti specifici necessari per tali discipline.

Nel contesto di FreeCAD, ogni ambiente è adattato ad un particolare tipo di attività, organizzando tutti gli strumenti necessari per tale attività in un\'unica interfaccia. Quando si passa da un ambiente all\'altro, l\'insieme di strumenti e controlli visibili nell\'interfaccia utente si adatta per riflettere le esigenze dell\'attività selezionata, sebbene il contenuto effettivo del progetto o la \"scena\" su cui si sta lavorando non cambi. Ciò consente transizioni fluide nel flusso di lavoro, ad esempio iniziare un progetto con forme 2D di base nell\'ambiente Draft e quindi elaborare questi disegni con strumenti di modellazione avanzati nell\'ambiente Part.

I termini \"Ambiente\" e \"Modulo\" sono talvolta usati in modo intercambiabile, ma hanno significati distinti all\'interno di FreeCAD. Un Modulo è qualsiasi estensione che aggiunge funzionalità a FreeCAD, mentre un Ambiente è un tipo specifico di Modulo dotato dei propri componenti dell\'interfaccia utente come barre degli strumenti e menu, progettati per facilitare tipi specifici di attività. Pertanto, ogni Ambiente di lavoro è un Modulo, ma non tutti i Moduli si qualificano come Ambienti di lavoro.

Il più importante controllo dell\'interfaccia di FreeCAD è il selettore Ambiente, che si usa per passare da un Ambiente all\'altro:

![](images/FreeCAD_WB.png )

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> [Ambiente Assembly](Assembly_Workbench/it.md) per costruire e risolvere assiemi meccanici. {{Version/it|1.0}}

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> [Ambiente BIM](BIM_Workbench/it.md) per lavorare con elementi architettonici e creare modelli [BIM](https://en.wikipedia.org/wiki/Building_information_modeling). Combina l\'Ambiente Arch e l\'Ambiente BIM precedentemente esterno disponibile in {{VersionMinus/it|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> [Ambiente CAM](CAM_Workbench/it.md) viene utilizzato per produrre istruzioni G-Code. Questo ambiente di lavoro era chiamato \"Path Workbench\" nella {{VersionMinus/it|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Ambiente Draft](Draft_Workbench/it.md) contiene strumenti 2D e operazioni CAD 2D e 3D di base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Ambiente FEM](FEM_Workbench/it.md) fornisce un flusso di lavoro di analisi agli elementi finiti (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [Ambiente Inspection](Inspection_Workbench/it.md) è realizzato per fornire strumenti specifici per l\'esame delle forme. È ancora nelle prime fasi di sviluppo.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> [Ambiente Material](Material_Workbench/it.md) gestisce il sistema dei materiali di FreeCAD. {{Version/it|1.0}}

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Ambiente Mesh](Mesh_Workbench/it.md) per lavorare con maglie triangolari.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [Ambiente OpenSCAD](OpenSCAD_Workbench/it.md) per l\'interoperabilità con OpenSCAD e la riparazione della cronologia del modello della [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Ambiente Part](Part_Workbench/it.md) per lavorare con primitive geometriche ed operazioni booleane.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Ambiente Part Design](PartDesign_Workbench/it.md) per la costruzione di forme Part partendo da schizzi.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Ambiente Points](Points_Workbench/it.md) per lavorare con nuvole di punti.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Ambiente Reverse Engineering](Reverse_Engineering_Workbench/it.md) ha lo scopo di fornire strumenti specifici per convertire forme/solidi/mesh in forme parametriche compatibili con FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [ Ambiente Robot](Robot_Workbench/it.md) per lo studio dei movimenti dei robot. Attualmente non mantenuto.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Ambiente Sketcher](Sketcher_Workbench/it.md) per lavorare con schizzi a geometria vincolata.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Ambiente Spreadsheet](Spreadsheet_Workbench/it.md) per la creazione e la manipolazione di dati in un foglio di calcolo.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Ambiente Surface](Surface_Workbench/it.md) fornisce strumenti per creare e modificare le superfici. È simile al [Part Builder](Part_Builder/it.md) con l\'opzione Faccia dai bordi.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Ambiente TechDraw](TechDraw_Workbench/it.md) per la produzione di disegni tecnici da modelli 3D. È il successore dell\'[Ambiente Drawing](Drawing_Workbench/it.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Ambiente di Test](Testing/it.md) serve per il debug di FreeCAD.

Gli Ambienti di lavoro spesso confondono i nuovi utenti, poiché non è sempre facile sapere in quale ambiente cercare uno strumento specifico. Ma si imparano velocemente e dopo poco tempo il loro uso sembrerà naturale. I nuovi utenti si rendono presto conto che gli Ambienti di lavoro sono un modo conveniente per organizzare la moltitudine di strumenti che FreeCAD ha da offrire. Inoltre, sono anche completamente personalizzabili.



### L\'interfaccia

Diamo uno sguardo alle diverse parti dell\'interfaccia:

![](images/FreeCAD_022_Interface.png )

La finestra principale dell\'applicazione può essere approssimativamente divisa in 11 sezioni:

1.  L\'[Area di visualizzazione principale](main_view_area/it.md), che può contenere diverse finestre a schede.
2.  La [Vista 3D](3D_view/it.md), normalmente incorporata nell\'[Area di visualizzazione principale](main_view_area.md). La vista 3D è l\'elemento centrale dell\'interfaccia, visualizza e consente la manipolazione degli oggetti su cui si sta lavorando. È possibile avere più visualizzazioni dello stesso documento (o oggetti) o avere più documenti aperti contemporaneamente. Inoltre, ciascuna vista può essere staccata separatamente dalla finestra principale.
3.  Il modello e la scheda [Azioni](task_panel/it.md).
    1.  La scheda Modello mostra il contenuto e la struttura del proprio documento.
    2.  La scheda Azioni è dove FreeCAD chiederà valori specifici per l\'ambiente e lo strumento che si sta attualmente utilizzando (ad esempio le dimensioni di un oggetto).
4.  L\'[Editor proprietà](property_editor/it.md) che appare quando la scheda Modello è attiva nell\'interfaccia. Permette di gestire le proprietà degli oggetti esposte pubblicamente nel documento. È composto dalle sezioni Vista e Dati, che mostrano rispettivamente le proprietà di visualizzazione e le proprietà parametriche degli oggetti.
5.  La [Vista di selezione](selection_view/it.md) che indica gli oggetti o i sottoelementi degli oggetti (vertici, bordi, facce) che sono selezionati.
6.  La [Vista report](report_view/it.md) in cui vengono visualizzati messaggi, avvisi ed errori.
7.  La [Python console](python_console/it.md). La console Python, dove vengono stampati tutti i comandi eseguiti e dove è possibile inserire il codice Python.
8.  La [Barra di stato](status_bar/it.md) dove appaiono alcuni messaggi e suggerimenti.
9.  L\'area delle barre degli strumenti, dove sono ancorate le barre degli strumenti.
10. Il [selettore ambiente](Std_Workbench/it.md), dove si seleziona l\'[ambiente](workbenches/it.md) da attivare.
11. Il [menu standard](Standard_Menu/it.md), che contiene le operazioni di base del programma.

La maggior parte dei pannelli di cui sopra può essere nascosta o mostrata utilizzando il menu **Visualizza → Pannelli**



### Personalizzare l\'interfaccia 

L\'interfaccia di FreeCAD è progettata per un\'ampia personalizzazione. Tutte le barre degli strumenti e i pannelli possono essere riposizionati, impilati o addirittura ancorati in varie configurazioni in base alle preferenze dell\'utente. Inoltre, possono essere chiusi e quindi riaperti secondo necessità. Oltre a queste funzionalità, gli utenti hanno numerose altre opzioni tra cui la possibilità di creare barre degli strumenti personalizzate con strumenti selezionati da uno dei qualsiasi degli Ambienti di lavoro disponibili e di assegnare o modificare scorciatoie da tastiera per semplificare il flusso di lavoro. Questa flessibilità garantisce che gli utenti possano personalizzare l\'Ambiente per adattarlo alle proprie esigenze e preferenze specifiche.

Le opzioni di personalizzazione avanzate sono disponibili dal menu **Strumenti → Personalizza**:

![](images/FreeCAD_022_Customization.png )

**Approfondimenti**

-   [Primi passi con FreeCAD](Getting_started/it.md)
-   [Personalizzare l\'interfaccia](Interface_Customization/it.md)
-   [Ambienti di lavoro](Workbenches/it.md)
-   [More about Python](https://www.python.org)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD Interface/it
