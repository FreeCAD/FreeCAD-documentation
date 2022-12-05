# <img alt="L\'icona di Path" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/it


{{TOCright}}

## Introduzione

L\'[Ambiente Path](Path_Workbench/it.md) <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> viene utilizzato per produrre istruzioni macchina per [Macchine CNC](https://en.wikipedia.org/wiki/CNC_router) da un modello 3D di FreeCAD. Questi producono oggetti 3D del mondo reale su macchine CNC come frese, torni, taglio laser e simili. In genere, le istruzioni sono un dialetto [G-code](https://en.wikipedia.org/wiki/G-code). Qui viene presentato un [esempio generale di simulazione della sequenza del percorso utensile del tornio CNC](https://www.ange-softs.com/SIMULCNCHTML/index.html).

<img alt="" src=images/pathwb.png  style="width:600px;">

L\'ambiente Path di FreeCAD crea le istruzioni macchina con il seguente flusso di lavoro:

-   Un modello 3D è l\'oggetto di base, generalmente creato utilizzando uno o più ambienti tra <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench/it.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md) o <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md).
-   Viene creata una [Lavorazione](Path_Job/it.md) nell\'ambiente Path. Contiene tutte le informazioni necessarie per generare il G-code necessario per elaborare la lavorazione su una fresa CNC: c\'è il pezzo grezzo, la fresa ha un certo [set di utensili](Path_ToolLibraryEdit/it.md) e segue determinati comandi che controllano velocità e movimenti (di solito G-code).
-   Gli [Utensili](Path_Tools/it.md) vengono selezionati come richiesto dalle operazioni di lavorazione.
-   I percorsi di fresatura sono creati utilizzando, ad es. le operazioni di [Profilo](Path_Profile/it.md) e [Cavità 3D](Path_Pocket_3D/it.md). Questi oggetti Percorso (Path) utilizzano il linguaggio G-code interno di FreeCAD, indipendente dalla macchina CNC.
-   Si può esportare la lavorazione con un G-code, corrispondente alla propria macchina. Questo passaggio è chiamato \"post-elaborazione\"; sono disponibili diversi post processori.

## Concetti generali 

L\'ambiente Path genera un G-code che definisce i percorsi richiesti per fresare il Progetto rappresentato dal modello 3D nel [linguaggio G-code usato da FreeCAD per le operazioni di lavorazione di Path](Path_scripting#The_FreeCAD_Internal_GCode_Format/it.md), che viene successivamente tradotto nel codice appropriato per il controllo CNC di destinazione selezionando il post processore appropriato.

Il G-code è generato dalle direttive e dalle operazioni contenute in un percorso di lavorazione. Il flusso di lavorazione le elenca nell\'ordine in cui verranno eseguiti. L\'elenco può essere popolato aggiungendo operazioni sui percorsi, ottimizzazioni dei percorsi, comandi parziali dei percorsi e modifiche ai percorsi, dal menu Path o dai pulsanti della GUI.

Path offre un Gestore degli utensili (Libreria, Tabella utensili), un ispettore del G-code e strumenti di simulazione. Collega il post processore e consente di importare ed esportare i modelli di lavorazioni.

L\'ambiente Path ha delle dipendenze esterne tra cui:

1.  Le unità del modello 3D di FreeCAD sono definite nelle impostazioni **Modifica → Preferenze ... → Generale → Unità di misura**. La configurazione del postprocessore definisce le unità G-code finali.
2.  Il percorso del file macro e le tolleranze geometriche sono definiti nella scheda **Modifica → Preferenze ... → Path → Preferenze lavorazione**.
3.  I colori sono definiti in **Modifica → Preferenze ... → Path → Colori**.
4.  I parametri dei lembi di fermo pezzo (tag) sono definiti nella scheda **Modifica → Preferenze ... → Path → Ottimizzazione**.
5.  Se la qualità del modello Base 3D supporta i requisiti di Path, supera la Verifica della geometria.

## Limitazioni

Alcune limitazioni attuali di cui dovreste essere consapevoli sono:

-   La maggior parte degli strumenti Path non sono veri strumenti 3D ma solo 2.5D. Questo significa che prendono una forma 2D fissa e possono tagliarla fino ad una data profondità. Tuttavia, ci sono due strumenti che producono veri percorsi 3D: **<img src="images/Path_3DPocket.svg" width=24px> [Cavità 3D](Path_Pocket_3D/it.md)** and **<img src="images/Path_Surface.svg" width=24px> [Sfacciatura 3D](Path_Surface/it.md)** (La quale è ancora una [caratteristica sperimentale](Path_experimental/it.md) a partire da novembre 2020).
-   La maggior parte del banco di lavoro Path è progettato per una semplice fresa/router CNC standard a 3 assi (xyz), ma gli strumenti per il tornio sono in fase di sviluppo nella 0.19_pre.
-   La maggior parte delle operazioni in Path workbench restituirà percorsi basati solo su un utensile/bit standard, indipendentemente dal tipo di utensile/bit assegnato in un dato controllore di utensili, ad eccezione delle operazioni **<img src="images/Path_Engrave.svg" width=24px> [Incisione](Path_Engrave/it.md)** e **<img src="images/Path_Surface.svg" width=24px> [Sfacciatura 3D](Path_Surface/it.md)**.
-   Le operazioni all\'interno del Path workbench non sono a conoscenza dei meccanismi di bloccaggio in uso per fissare il modello alla vostra macchina. Di conseguenza, si prega di rivedere e simulare i percorsi generati prima di inviare il codice alla macchina. Se necessario, modella i tuoi meccanismi di serraggio in FreeCAD per controllare meglio i percorsi generati. Cercate le possibili collisioni con i morsetti o altri ostacoli lungo i percorsi.

## Unità di misura 

La gestione delle unità di misura in Path può essere fonte di confusione. Ci sono alcuni punti da chiarire:

1.  Le unità base di FreeCAD per lunghezza e tempo sono rispettivamente \'mm\' e \'s\'. La velocità è quindi \'mm/s\'. Questo è ciò che FreeCAD salva internamente a prescindere da qualsiasi altra cosa
2.  Lo schema predefinito delle unità utilizza le unità predefinite. Se si utilizza lo schema predefinito e si inserisce una velocità di avanzamento senza una stringa di unità, essa viene immessa come \'mm/s\'
3.  La maggior parte delle macchine CNC prevede una velocità di avanzamento sotto forma di \"mm/min\" o \"in/min\". La maggior parte dei post-processori converte automaticamente l\'unità durante la generazione del G-Code.

Schemi delle unità di misura:

1.  La modifica dello schema delle unità nelle preferenze modifica la stringa dell\'unità predefinita per i campi di input. Se siete utenti di Path e preferite progettare nel sistema metrico, si consiglia vivamente di utilizzare lo schema \"Metric Small Parts & CNC\". Se progettate in unità USA, funzionano Imperial Decimal e Building US
2.  La modifica dello schema delle unità preferite non ha alcun effetto sull\'output, ma aiuta a evitare errori di input

Output:

1.  La generazione dell\'unità corretta in uscita è responsabilità del post-processore e viene eseguita solo in quel momento
2.  L\'unità di output della macchina non è in nessun modo correlata allo schema dell\'unità selezionata
3.  I post-processori producono un output metrico (G21), imperiale (G20) o configurabile.
4.  Post processori configurabili predefiniti per il sistema metrico (G21)
5.  Se si desidera che il post-processore configurabile emetta il G-Code nel sistema imperiale (G20), impostare l\'argomento corretto nella configazione dell\'output della lavorazione (es. \--Inches per linuxcnc). Questo può essere memorizzato in un modello di lavorazione e impostato come modello predefinito per renderlo automatico per tutte le lavorazioni future

Ispezionare il codice:

1.  Se si usa lo strumento Ispeziona il G-Code per vedere il codice, lo si vede in \'mm/s\' perché non è ancora stato post-elaborato.

## Altezze e profondità 

Molti comandi hanno varie altezze e profondità:

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Riferimento visivo per le proprietà di Profondità (impostazioni)*

## Comandi

Alcuni comandi sono sperimentali e non disponibili per impostazione predefinita. Per abilitarli, vedere [Path sperimentale](Path_experimental/it.md).

### Comandi del progetto 

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Lavorazione](Path_Job/it.md): Crea una nuova lavorazione CNC.

-   <img alt="" src=images/Path_Post.svg  style="width:32px;"> [Post elaborazione](Path_Post/it.md): Esporta un progetto in G-code.

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Controllare il percorso del lavoro per errori comuni](Path_Sanity/it.md): Controlla la lavorazione selezionata alla ricerca di valori mancanti. [**Sperimentale**](Path_experimental/it.md). {{Version/it|0.19}}

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Esporta come modello](Path_ExportTemplate/it.md): Esporta la lavorazione corrente come modello.

### Comandi Utensile 

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Ispeziona G-code](Path_Inspect/it.md): Mostra il G-code per controllo.

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Simulatore CAM](Path_Simulator/it.md): Mostra l\'operazione di fresatura così come viene eseguita sulla macchina

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Chiudi il ciclo](Path_SelectLoop/it.md): Completa un ciclo basato su due bordi selezionati

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Attiva o disattiva l\'operazione](Path_OpActiveToggle/it.md): Attivare o disattivare un\'operazione di lavorazione.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [Editor della libreria delle geometrie utensile](Path_ToolBitLibraryOpen/it.md): Apre un editor per gestire le librerie delle geometrie utensile. {{Version/it|0.19}}

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [Pannello geometrie utensile](Path_ToolBitDock/it.md): Apre un editor per gestire le librerie delle geometrie utensile. {{Version/it|0.19}}

### Operazioni di Base 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profila](Path_Profile/it.md): Crea un\'operazione di profilo dell\'intero modello o da una o più facce o spigoli selezionati. {{Version/it|0.19}}

-   <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Tasca](Path_Pocket_Shape/it.md): Crea un\'operazione di scavo da uno o più scavi selezionati.

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Foratura](Path_Drilling/it.md): Esegue un ciclo di perforazione.

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Sfacciatura](Path_MillFace/it.md): Crea un percorso di sfacciatura.

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Elica](Path_Helix/it.md): Crea un percorso elicoidale.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adattiva](Path_Adaptive/it.md): Crea un\'operazione adattiva di compensazione e profilazione.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Scanalatura](Path_Slot/it.md): Crea un\'operazione di scanalatura da funzioni selezionate o punti personalizzati. [**Sperimentale**](Path_experimental/it.md). {{Version/it|0.19}}

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Incisione](Path_Engrave/it.md): Crea un percorso di incisione.

-   <img alt="" src=images/Path_Deburr.svg  style="width:32px;"> [Sbavatura](Path_Deburr/it.md): Crea un percorso di sbavatura.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Incisione a V](Path_Vcarve/it.md): Crea un percorso di incisione utilizzando una forma dello strumento V. {{Version/it|0.19}}

### Operazioni 3D 

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [Tasca 3D](Path_Pocket_3D/it.md): Crea un percorso per una tasca 3D.

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [Sfacciatura 3D](Path_Surface/it.md): crea un percorso per una sfacciatura 3D. [**Sperimentale**](Path_experimental/it.md). {{Version/it|0.19}}

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Piani orizzontali](Path_Waterline/it.md): Crea un percorso di lavorazione per piani orizzontali per una superficie 3D. [**Sperimentale**](Path_experimental/it.md). {{Version/it|0.19}}

### Ottimizzazione del percorso 

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Contorno di limitazione](Path_DressupPathBoundary/it.md): aggiunge un contorno di limitazione del percorso ad un percorso selezionato.

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Lavorazione degli angoli](Path_DressupDogbone/it.md): Aggiunge una modifica di adattamento osso-di-cane (dogbone) per la lavorazione degli angoli ad un percorso selezionato.

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Percorso di lama](Path_DressupDragKnife/it.md): Aggiunge una modifica di percorso di lama (dragknife) a un percorso selezionato.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [Punto di ingresso o uscita](Path_DressupLeadInOut/it.md): Aggiunge un punto di entrata o di uscita a un percorso selezionato.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Rampa di ingresso](Path_DressupRampEntry/it.md): Aggiunge la modifica di dressup Rampa di ingresso a un percorso selezionato.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Lembo di fermo](Path_DressupTag/it.md): Aggiunge un lembo ferma pezzo a un percorso di lavorazione selezionato.

### Comandi Supplementari 

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Punto di fissaggio](Path_Fixture/it.md): Cambia la posizione del punto di fissaggio.

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Commento](Path_Comment/it.md): Inserisce un commento nel codice G di un percorso.

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Stop](Path_Stop/it.md): Inserisce un punto di fermo macchina.

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Personalizza](Path_Custom/it.md): Inserisce del G-code personalizzato.

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [Percorso da una forma](Path_Shape/it.md): Crea un oggetto percorso da un oggetto Parte selezionato. [**Sperimentale**](Path_experimental/it.md).

### Modifica del percorso 

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copia l\'operazione nella lavorazione](Path_Copy/it.md): Crea una copia parametrica di un oggetto percorso selezionato.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Copia in serie](Path_Array/it.md): Crea una serie duplicando un percorso selezionato.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Copia semplice](Path_SimpleCopy/it.md): Crea una copia non parametrica di un oggetto percorso selezionato.

### Varie

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Area](Path_Area/it.md): Crea un\'area caratteristica dagli oggetti selezionati. [**Sperimentale**](Path_experimental/it.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Piano di lavoro](Path_Area_Workplane/it.md): Crea un piano di lavoro di un\'area operativa. [**Sperimentale**](Path_experimental/it.md).

### Obsoleti

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Gestione utensili](Path_ToolLibraryEdit/it.md): Gestisce gli utensili. Sistema utensile \'Legacy\'. {{VersionMinus/it|0.18}}

## Architettura utensile 

Gestisce utensili, geometrie e la Libreria degli strumenti. Basato sull\'architettura utensile. {{Version/it|0.19}}

-   [Percorso Utensile](Path_Tools/it.md)
-   [Percorso Forma Utensile](Path_ToolShape/it.md)
-   [Percorso Geometria Utensile](Path_ToolBit/it.md)
-   [Percorso Libreria Geometria Utensile](Path_ToolBit_Library/it.md)
-   [Percorso Controllore Utensile](Path_ToolController/it.md)

## Altro

-   [FAQ di Path](Path_FAQ/it.md): L\'ambiente Path condivide molti concetti con altri pacchetti software CAM ma ha le sue peculiarità. Se qualcosa sembra sbagliato, questo è un buon punto di partenza.
-   [Scheda di configurazione percorso](Path_SetupSheet/it.md): È possibile utilizzare una scheda di configurazione per personalizzare il modo in cui vengono calcolati i diversi valori delle proprietà per le operazioni.
-   [Personalizzazione del postprocessore di Path](Path_Postprocessor_Customization/it.md): Se si dispone di una macchina speciale che non può utilizzare uno dei post-processori disponibili, potrebbe essere necessario scrivere il proprio post-processore.
-   [Percorso a quattro assi](Path_fourth_axis/it.md): Fresatura sperimentale a quattro assi.

## Preferenze

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Preferenze\...](Path_Preferences/it.md): Preferenze disponibili per l\'ambiente di lavoro Path.

## Script

Vedere la pagina [Script di Path](Path_scripting/it.md).

## Tutorial

-   [Guida per gli impazienti](Path_Walkthrough_for_the_Impatient/it.md): un breve tutorial per familiarizzare con Path.

## Video

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): una playlist con una serie di 5 video in inglese di sliptonic. Questa serie mostra come lavorare con l\'[Ambiente Path](Path_Workbench/it.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): una playlist con una serie di 7 video lezioni di CAD CAM in inglese .
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) una playlist con una serie di 8 video lezioni di CAD CAM in inglese .

## Tabella di marcia 

-   [Tabella di marcia per lo sviluppo di Path](Path_Development_Roadmap/it.md): Leggi questo se sei uno sviluppatore e vuoi contribuire a Path.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/it
