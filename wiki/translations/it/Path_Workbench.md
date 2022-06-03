# <img alt="L\'icona di Path" src=images/Workbench_Path.svg  style="width   *64px;"> Path Workbench/it


{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

l\'<img alt="" src=images/Workbench_Path.svg  style="width   *24px;"> [Ambiemte Path](Path_Workbench.md) viene utilizzato per produrre delle istruzioni macchina di tipo [CNC](https   *//en.wikipedia.org/wiki/CNC_router) da un modello 3D di FreeCAD. Con questo ambiente si producono oggetti 3D reali su macchine CNC come fresatrici, torni, macchine a taglio laser o simili. In genere, le istruzioni sono in linguaggio [G-Code](https   *//en.wikipedia.org/wiki/G-Code)


</div>

<img alt="" src=images/pathwb.png  style="width   *600px;">


<div class="mw-translate-fuzzy">

L\'ambiente Path di FreeCAD crea le istruzioni macchina con il seguente flusso di lavoro   *

-   Il modello base 3D è un oggetto che in genere viene creato utilizzando uno o più ambienti quali [Disegno](PartDesign_Workbench/it.md), [Parte](Part_Workbench/it.md) o [Draft](Draft_Workbench/it.md).
-   L\'ambiente Path crea una [Lavorazione](Path_Job/it.md). Essa contiene tutte le informazioni necessarie per generare il codice G necessario per eseguire la lavorazione su una fresatrice CNC   * c\'è il pezzo grezzo (Stock), la fresatrice possiede un certo [set di utensili](Path_ToolLibraryEdit/it.md) e segue determinati comandi che controllano la velocità ed i movimenti (solitamente G-Code).
-   Gli utensili vengono selezionati come richiesto dalle operazioni di lavorazione.
-   I percorsi di fresatura sono creati utilizzando, ad es. le operazioni di [Profilo](Path_Profile/it.md) e [Cavità 3D](Path_Pocket_3D/it.md). Questi oggetti Percorso (Path) utilizzano il linguaggio G-Code interno di FreeCAD, indipendente dalla macchina CNC.
-   Si può esportare la lavorazione con un codice G, corrispondente alla propria macchina. Questo passaggio è chiamato \"post-elaborazione\"; sono disponibili diversi post processori.


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## Concetti generali 

L\'ambiente Path genera un codice G che definisce i percorsi richiesti per fresare il progetto rappresentato dal modello 3D in codice interno, [il linguaggio usato da FreeCAD G-Code per le operazioni di lavoro di Path](Path_scripting#The_FreeCAD_Internal_GCode_Format/it.md), viene successivamente tradotto nel codice appropriato per il controller CNC di destinazione selezionando il post processore appropriato.

Il codice G è generato dalle direttive e dalle operazioni contenute in un percorso di lavorazione. Il flusso di lavorazione li elenca nell\'ordine in cui verranno eseguiti. L\'elenco può essere popolato aggiungendo operazioni sui percorsi, ottimizzazioni dei percorsi, comandi parziali dei percorsi e modifiche ai percorsi, dal menu Path o dai pulsanti della GUI.


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


<div class="mw-translate-fuzzy">

Path offre un Gestore degli utensili (Libreria, Tabella utensili), un ispettore del G-Code e strumenti di simulazione. Collega il post processore e consente di importare ed esportare i modelli di lavorazioni.


</div>


<div class="mw-translate-fuzzy">

L\'ambiente Path ha delle dipendenze esterne tra cui   *

1.  Le unità del modello 3D di FreeCAD sono definite nelle impostazioni **Modifica → Preferenze ... → Generale → Unità di misura**. La configurazione del postprocessore definisce le unità G-Code finali.
2.  Il percorso del file macro e le tolleranze geometriche sono definiti nella scheda **Modifica → Preferenze ... → Path → Preferenze lavorazione**.
3.  I colori sono definiti in **Modifica → Preferenze ... → Path → Colori**.
4.  I parametri dei lembi di fermo pezzo (tag) sono definiti nella scheda **Modifica → Preferenze ... → Path → Ottimizzazione**.
5.  Se la qualità del modello Base 3D supporta i requisiti di Path, supera la Verifica della geometria.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

Alcune limitazioni attuali di cui dovreste essere consapevoli sono   *

-   La maggior parte degli strumenti Path non sono veri strumenti 3D ma solo 2.5D. Questo significa che prendono una forma 2D fissa e possono tagliarla fino ad una data profondità. Tuttavia, ci sono due strumenti che producono veri percorsi 3D   * **<img src="images/Path_3DPocket.svg" width=24px> [Cavità 3D](Path_Pocket_3D/it.md)** and **<img src="images/Path_Surface.svg" width=24px> [Sfacciatura 3D](Path_Surface/it.md)** (La quale è ancora una [caratteristica sperimentale](Path_experimental/it.md) a partire da novembre 2020).
-   La maggior parte del banco di lavoro Path è progettato per una semplice fresa/router CNC standard a 3 assi (xyz), ma gli strumenti per il tornio sono in fase di sviluppo nella 0.19\_pre.
-   La maggior parte delle operazioni in Path workbench restituirà percorsi basati solo su un utensile/bit standard, indipendentemente dal tipo di utensile/bit assegnato in un dato controllore di utensili, ad eccezione delle operazioni **<img src="images/Path_Engrave.svg" width=24px> [Incisione](Path_Engrave/it.md)** and **<img src="images/Path_Surface.svg" width=24px> [Safcciatura 3D](Path_Surface/it.md)**.
-   Le operazioni all\'interno del Path workbench non sono a conoscenza dei meccanismi di bloccaggio in uso per fissare il modello alla vostra macchina. Di conseguenza, si prega di rivedere e simulare i percorsi generati prima di inviare il codice alla macchina. Se necessario, modella i tuoi meccanismi di serraggio in FreeCAD per controllare meglio i percorsi generati. Cercate le possibili collisioni con i morsetti o altri ostacoli lungo i percorsi.


</div>

## Unità di misura 

La gestione delle unità di misura in Path può essere fonte di confusione. Ci sono alcuni punti da chiarire   *

1.  Le unità base di FreeCAD per lunghezza e tempo sono rispettivamente \'mm\' e \'s\'. La velocità è quindi \'mm/s\'. Questo è ciò che FreeCAD salva internamente a prescindere da qualsiasi altra cosa
2.  Lo schema predefinito delle unità utilizza le unità predefinite. Se si utilizza lo schema predefinito e si inserisce una velocità di avanzamento senza una stringa di unità, essa viene immessa come \'mm/s\'
3.  La maggior parte delle macchine CNC prevede una velocità di avanzamento sotto forma di \"mm/min\" o \"in/min\". La maggior parte dei post-processori converte automaticamente l\'unità durante la generazione del G-Code.

Schemi delle unità di misura   *

1.  La modifica dello schema delle unità nelle preferenze modifica la stringa dell\'unità predefinita per i campi di input. Se siete utenti di Path e preferite progettare nel sistema metrico, si consiglia vivamente di utilizzare lo schema \"Metric Small Parts & CNC\". Se progettate in unità USA, funzionano Imperial Decimal e Building US
2.  La modifica dello schema delle unità preferite non ha alcun effetto sull\'output, ma aiuta a evitare errori di input

Output   *

1.  La generazione dell\'unità corretta in uscita è responsabilità del post-processore e viene eseguita solo in quel momento
2.  L\'unità di output della macchina non è in nessun modo correlata allo schema dell\'unità selezionata
3.  I post-processori producono un output metrico (G21), imperiale (G20) o configurabile.
4.  Post processori configurabili predefiniti per il sistema metrico (G21)
5.  Se si desidera che il post-processore configurabile emetta il G-Code nel sistema imperiale (G20), impostare l\'argomento corretto nella configazione dell\'output della lavorazione (es. \--Inches per linuxcnc). Questo può essere memorizzato in un modello di lavorazione e impostato come modello predefinito per renderlo automatico per tutte le lavorazioni future

Ispezionare il codice   *

1.  Se si usa lo strumento Ispeziona il G-Code per vedere il codice, lo si vede in \'mm/s\' perché non è ancora stato post-elaborato.

## Heights and depths 


<div class="mw-translate-fuzzy">

## I comandi di Path 

Molti comandi hanno varie altezze e profondità   * <img alt="" src=images/Path-DepthsAndHeights.gif  style="width   *500px;"> 
*Riferimento visivo per le proprietà di profondità (impostazioni)*


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width   *500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Job.svg  style="width   *32px;"> [Lavorazione](Path_Job/it.md)   * Crea una nuova lavorazione CNC


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.svg  style="width   *32px;"> [Post elaborazione](Path_Post/it.md)   * Esporta un progetto in G-code


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.svg  style="width   *32px;"> [Errori nel percorso](Path_Sanity/it.md)   * Controlla la lavorazione selezionata alla ricerca di valori mancanti


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width   *32px;"> [Esporta come modello](Path_ExportTemplate/it.md)   * Esporta la lavorazione corrente come modello


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.svg  style="width   *32px;"> [Ispeziona G-Code](Path_Inspect/it.md)   * Mostra il codice G per il controllo


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.svg  style="width   *32px;"> [Simulatore CAM](Path_Simulator/it.md)   * Mostra l\'operazione di fresatura così come viene eseguita sulla macchina


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SelectLoop.svg  style="width   *32px;"> [Chiudi il ciclo](Path_SelectLoop/it.md)   * Completa un ciclo basato su due bordi selezionati


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width   *32px;"> [Attiva operazione](Path_OpActiveToggle/it.md)   * Utilizzato per attivare o disattivare un\'operazione di lavorazione.


</div>

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width   *32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md)   * Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width   *32px;"> [ToolBit Dock](Path_ToolBitDock.md)   * Toggles the ToolBit Dock. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

### Operazioni di base sul percorso 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Profile.svg  style="width   *32px;"> [Profila](Path_Profile/it.md) (Nuovo in 0.19)   * Crea un\'operazione di profilo dell\'intero modello o da una o più facce o spigoli selezionati. Questa operazione è una combinazione delle operazioni Contornatura, Profila faccia e Profila bordo preesistenti.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.svg  style="width   *32px;"> [Tasca](Path_Pocket_Shape/it.md)   * Crea un\'operazione di scavo da una o più tasche selezionate


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.svg  style="width   *32px;"> [Foratura](Path_Drilling/it.md)   * Esegue un ciclo di perforazione


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Face.svg  style="width   *32px;"> [Sfacciatura](Path_MillFace/it.md)   * Crea un percorso di sfacciatura


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Helix.svg  style="width   *32px;"> [Elica](Path_Helix/it.md)   * Crea un percorso elicoidale


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Adaptive.svg  style="width   *32px;"> [Adattiva](Path_Adaptive/it.md)   * Crea un\'operazione adattiva di compensazione e profilazione.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Slot.svg  style="width   *32px;"> [Scanalatura](Path_Slot/it.md) (Nuovo in 0.19)   * Crea un\'operazione di scanalatura da funzioni selezionate o punti personalizzati


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Engrave.svg  style="width   *32px;"> [Incisione](Path_Engrave/it.md)   * Crea un percorso di incisione


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Vcarve.svg  style="width   *32px;"> [Incisione a V](Path_Vcarve/it.md)   * Crea un percorso per una tasca 3D


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_3DPocket.svg  style="width   *32px;"> [Tasca 3D](Path_Pocket_3D/it.md)   * Crea un percorso per una tasca 3D


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Surface.svg  style="width   *32px;"> [Sfacciatura 3D](Path_Surface/it.md)   * crea un percorso per una sfacciatura 3D (sperimentale, 0.19).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Waterline.svg  style="width   *32px;"> [Piani orizzontali](Path_Waterline/it.md)   * Crea un percorso di lavorazione per piani orizzontali per una superficie 3D (sperimentale, 0.19)


</div>


<div class="mw-translate-fuzzy">

### Ottimizzazione del percorso 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width   *32px;"> [Contorno di limitazione](Path_DressupPathBoundary/it.md)   * aggiunge un contorno di limitazione del percorso ad un percorso selezionato.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width   *32px;"> [Lavorazione degli angoli](Path_DressupDogbone/it.md)   * Aggiunge una modifica di adattamento osso-di-cane (dogbone) per la lavorazione degli angoli ad un percorso selezionato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width   *32px;"> [Percorso di lama](Path_DressupDragKnife/it.md)   * Aggiunge una modifica di percorso di lama (dragknife) a un percorso selezionato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width   *32px;"> [Punto di ingresso o uscita](Path_DressupLeadInOut/it.md)   * Aggiunge un punto di entrata o di uscita a un percorso selezionato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width   *32px;"> [Rampa di ingresso](Path_DressupRampEntry/it.md)   * Aggiunge la modifica di vestizione Rampa di ingresso a un percorso selezionato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.svg  style="width   *32px;"> [Lembo di fermo](Path_DressupTag/it.md)   * Aggiunge un lembo ferma pezzo a un percorso di lavorazione selezionato


</div>


<div class="mw-translate-fuzzy">

### Comandi parziali 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.svg  style="width   *32px;"> [Punto di fissaggio](Path_Fixture/it.md)   * Cambia la posizione del punto di fissaggio


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.svg  style="width   *32px;"> [Commento](Path_Comment/it.md)   * Inserisce un commento nel codice G di un percorso


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.svg  style="width   *32px;"> [Stop](Path_Stop/it.md)   * Inserisce un punto di fermo macchina


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.svg  style="width   *32px;"> [Personalizza](Path_Custom/it.md)   * Inserisce del codice G personalizzato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Shape.svg  style="width   *32px;"> [Percorso da una forma](Path_Shape/it.md)   * Crea un oggetto percorso da un oggetto Parte selezionato


</div>


<div class="mw-translate-fuzzy">

### Modifica del percorso 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.svg  style="width   *32px;"> [Copia](Path_Copy/it.md)   * Crea una copia parametrica di un oggetto percorso selezionato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.svg  style="width   *32px;"> [Copia in serie](Path_Array/it.md)   * Crea una serie duplicando un percorso selezionato


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width   *32px;"> [Copia semplice](Path_SimpleCopy/it.md)   * Crea una copia non parametrica di un oggetto percorso selezionato


</div>

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area.svg  style="width   *32px;"> [Area](Path_Area/it.md)   * Crea un\'area caratteristica dagli oggetti selezionati


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width   *32px;"> [Piano di lavoro](Path_Area_Workplane/it.md)   * Crea un piano di lavoro di un\'area operativa


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width   *32px;"> [Gestione utensili](Path_ToolLibraryEdit/it.md)   * Gestisce gli utensili


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

L\'ambiente Path condivide molti concetti con altri pacchetti software CAM ma ha le sue peculiarità. Se qualcosa sembra sbagliato, questo potrebbe essere un buon punto di partenza.


</div>


<div class="mw-translate-fuzzy">

### Preferenze


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width   *32px;"> [Preferenze\...](Path_Preferences/it.md)   * Preferenze disponibili negli strumenti Path.


</div>

## Script


<div class="mw-translate-fuzzy">

Vedere la pagina [Script di Path](Path_scripting/it.md).


</div>

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md)   * a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path   * Custom paths with Python - Part 1 - 5](https   *//www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL)   * a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https   *//www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC)   * a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https   *//www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.

## Roadmap

-   [Path Development Roadmap](Path_Development_Roadmap.md)   * Read this if you are a developer and want to contribute to Path.





{{Path_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/it
