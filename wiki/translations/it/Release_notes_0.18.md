# Release notes 0.18/it
FreeCAD 0.18 è stato rilasciato il 12 marzo 2019, può essere scaricato dalla pagina [GitHub](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.3). L\'elenco completo delle modifiche è disponibile in [MantisBT bugtracker FC 0.18 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78).

Le note di rilascio delle precedenti versioni di FreeCAD sono disponibili nella pagina [Funzionalità di FreeCAD](Feature_list/it#Release_notes.md).

## Punti salienti 

Strumenti di [TechDraw](#Ambiente_TechDraw.md) estesi

<img alt="Model by Laurent14" src=images/TechDraw_sheet_screenshot.png  style="width:700px;">




Nuovi strumenti di [Schizzo](#Ambiente_Sketcher.md), e [PartDesign](#Ambiente_PartDesign.md) più stabile e robusto.

<img alt="Model by un1corn" src=images/Part_engine_screenshot.jpg  style="width:700px;">




Strumenti di [Arch e BIM](#Ambiente_Arch.md) migliorati ed estesi.

<img alt="Model by regis" src=images/Arch_work_screenshot.png  style="width:700px;">




## Aspetti generali 

-   Start center ridisegnato
-   L\'albero dei documenti (scheda Modello) offre ora 3 opzioni per la visualizzazione di tutti i documenti, con l\'opzione impostata dal menu **Visualizza → Struttura del documento** :
    -   Documento singolo. Mostra solo il documento attualmente attivo.
    -   Multidocumento. Visualizza tutti i documenti come avveniva in passato fino a FreeCAD 0.17.
    -   Comprimi/Espandi. Espande il documento attivo e comprime tutti gli altri.
-   Quando è attiva un\'azione che richiede l\'input dell\'utente, ora viene visualizzata un\'icona che mostra una matita nella scheda Azioni e scompare quando l\'attività è completata.
-   La vista 3D beneficia ora di un nuovo **[Cubo di navigazione](Navigation_Cube/it.md)** per orientare rapidamente la vista. Ha anche un piccolo menu per impostare la proiezione su ortografica o prospettica, nonché per adattare il contenuto alla vista. Il posizionamento del cubo di navigazione può essere impostato in **Preferenze → Visualizzazione → Vista 3D** e può anche essere nascosto.
-   È stato aggiunto il supporto generico per le unità di ingegneria civile e trasporti degli Stati Uniti. Queste unità includono ft, ft \^ 2, ft \^ 3, mph e angoli come gradi / minuti / secondi. Queste unità consentono l\'espressione dei piedi in forma decimale, al contrario di US Building, che forza le frazioni di pollici.
-   Ora è possibile specificare un\'immagine di sfondo personalizzata per la finestra principale di FreeCAD usando l\'opzione [**Preferenze → Generale → Abilita lo sfondo a mosaico**](Preferences_Editor/it#Generale.md).

<File:Start> center 0.18 screenshot.jpg\|thumb\|left\|Start center ridisegnato <File:FC018> Navigation Cube.png\|thumb\|left\|Il cubo di navigazione <File:FreeCAD> with background image.jpg\|thumb\|left\|FreeCAD con un\'immagine di sfondo personalizzata.




## Ambiente Arch 

<img alt="Arch al lavoro" src=images/Arch_release018_example.jpg  style="width:700px;">

-   Le [Pareti](Arch_Wall/it.md) ora possono essere visualizzate come una pila di blocchi. Ci sono molte opzioni per configurare le loro dimensioni e come devono essere impilati i blocchi.
-   [Parti di edificio](Arch_BuildingPart/it.md) sono i nuovi contenitori Arch per tutti gli usi. Possono raggruppare qualsiasi numero di oggetti, possono essere utilizzati per realizzare pavimenti (piani), edifici ( ora i [Piani](Arch_Floor/it.md) e gli [Edifici](Arch_Building/it.md) producono Parti di edifici), o qualsiasi altro gruppo di oggetti Arch. Possono essere spostati come [Parti](Std_Part/it.md), e sono [clonabili](Draft_Clone/it.md) e [referenziabili](Arch_Reference/it.md)!
-   L\'ambiente [BIM](BIM_Workbench/it.md) (aggiunto tramite il [Gestore degli Addon](Std_AddonMgr/it.md)), è una nuova controparte esterna, sperimentale di [Arch](Arch_Workbench/it.md). In esso, testiamo nuove funzionalità e flussi di lavoro in un ambiente più libero. Assicurati di fare un giro di prova!
-   [Finestre](Arch_Window/it.md) ha dei nuovi preset, quali una finestra scorrevole a 4 pannelli, in più, se [Parts Library](https://github.com/FreeCAD/FreeCAD-library/tree/c5eea12cdda7a3e6349323808815f63b0f97ef2e) è installato, tutte le porte e le finestre della libreria.
-   [Pannelli](Arch_Panel/it.md) ora può creare diversi tipi di pannelli ondulati, come fogli ondulati o persino pannelli sandwich.
-   Gli oggetti [Struttura](Arch_Structure/it.md) hanno una nuova modalità di disegno della trave, che consente di fare clic su due punti per posizionare tra loro un elemento strutturale.
-   Tutti i tipi di IFC sono ora disponibili per tutti gli oggetti Arch. Qualsiasi oggetto può essere esportato in qualsiasi altro tipo su IFC.
-   Il [posizionamento delle finestre](Arch_Window/it.md) è stato completamente ridisegnato. Posizionare correttamente le finestre negli oggetti host, che prima era un vero dolore, ora è molto più semplice.
-   Parametri della finestra dinamici: ora la dimensione dei telai della finestra è una proprietà della finestra, quindi è possibile regolare lo spessore delle finestre di preset senza la necessità di modificare i loro componenti o gli schizzi di base.
-   Ora I set di proprietà IFC sono supportati da tutti gli oggetti Arch.
-   L\'importatore e l\'esportatore IFC sono stati notevolmente migliorati con una serie di nuove funzionalità: supporto per set di proprietà, supporto per la rete, compressione dei file, profili condivisi, supporto per gruppi, set di quantità, ecc\....
-   Ora [Materiale](Arch_SetMaterial/it.md) supporta la gerarchia, se si assegna a un materiale un altro materiale come padre, essi vengono visualizzati correttamente impilati nell\'albero.
-   Tutti gli oggetti ed i materiali di Arch ora supportano i sistemi di classificazione (non ancora supportati dall\'importazione o esportazione IFC).
-   [Riferimento esterno](Arch_Reference/it.md) ora permette di collegare parti da un altro file di FreeCAD in un file di FreeCAD.

-   Ma c\'è molto di più! Controllare in [Arch/BIM development reports](https://github.com/yorikvanhavre/BIM_Workbench/wiki) per vedere tutto ciò che è stato fatto in quest\'anno.

## Ambiente Draft 

<img alt="Strumenti di annotazione di Draft più precisi" src=images/Draft_release018_example.jpg  style="width:700px;">.

-   Lo strumento [Scala](Draft_Scale/it.md) è stato completamente ridisegnato e ora ha maggiori opzioni ed è molto più comodo da usare.
-   Anche lo strumento [Testo](Draft_Text/it.md) è stato completamente ridisegnato, ora ha il suo oggetto parametrico con molte più opzioni. Attenzione, questi nuovi testi non sono supportati da FreeCAD 0.17.
-   [Wire](Draft_Wire/it.md) dispone ora di un\'opzione del tasto destro del mouse che consente di appiattirlo forzatamente sul suo piano mediano.
-   Nuovo strumento [Congiunzione](Draft_Join/it.md), che consente di unire contorni e linee individuali in un unico contorno.
-   Nuovo strumento [Split](Draft_Split/it.md), che divide una linea o un contorno in un punto per creare un altro contorno o linea.
-   Premendo il tasto **** mentre si disegna in modalità draft, l\'obiettivo dell\'oggetto si muove, consentendo di agganciare oggetti che sono oscurati da altri.
-   Lo strumento Aggiungi punto è stato migliorato in modo da aggiungere in modo più affidabile nodi su linee e contorni esattamente dove si fa clic.




## Ambiente FEM 

<img alt="La finestra di dialogo materiale FEM ottimizzata" src=images/FEM-Material-dialog-018.png  style="width:300px;"> Nella versione 0.17 sono state aggiunte tonnellate di nuove funzionalità in FEM. Quindi l\'obiettivo principale per FEM nella Relese 0.18 di FreeCAD non è stato aggiungere ulteriori nuove funzionalità e strumenti, ma rendere quelli esistenti più stabili e correggere il maggior numero possibile di bug. FEM ha ricevuto 470 commit durante il ciclo di sviluppo di FreeCAD 0.18[1](https://forum.freecadweb.org/viewtopic.php?f=10&t=13154&p=297292#p297110).

### Miglioramenti generali al codice base 

-   Tantissime correzioni di errori.
-   Codice rivisto e ripulito. Eliminazione del codice duplicato.
-   Correzione di molti errori di battitura nel codice e nei messaggi visibili.
-   Correzioni sulla compatibilità con Python 3.
-   Sono stati aggiunti altri test unitari.
-   Possibilità di compilare FreeCAD con aggiornamento MESH esterno.

### Strumenti

-   È stato aggiunto uno strumento piano di ritaglio per poter selezionare i solidi che si trovano all\'interno di altri solidi.
-   Il filtro Warp VTK ha suscitato interesse.
-   È stato aggiunto un tipo di analisi per il controllo del modello CalculiX

.

### Materiale

La gestione del materiale è stata migliorata. Ora è possibile utilizzare l\'editor globale del materiale di FreeCAD. Vedere anche [scheda materiale](Release_notes_0.18/it#Material_Handling.md). Per questo, il pannello Azioni del materiale FEM è stato ottimizzato.

## Ambiente Part 

-   Lo strumento [Controlla geometria](Part_CheckGeometry/it.md) ora apre una finestra con una barra di avanzamento e un pulsante **Cancel** per terminare l\'attività se impiega troppo tempo.
-   Il nuovo strumento [Defeaturing](Defeaturing_Workbench/it.md) si basa sullo strumento con lo stesso nome incluso in OCCT 7.3.0. Può rimuovere gli attributi selezionati su un solido come fori, sporgenze, spazi vuoti, smussi, raccordi, ecc. Per maggiori informazioni, vedere l\'articolo [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211) sul sito web di OCCT. Notare che se FreeCAD è basato su una versione precedente di OCCT 7.3.0, questo strumento non è disponibile ed è disattivato.

-   Il nuovo strumento [SliceApart](Part_SliceApart/it.md) si basa su [Slice to Compound](Part_Slice/it.md) e include un\'esplosione automatica dei composti per separare facilmente gli oggetti.

## Ambiente PartDesign 

-   Il nuovo strumento [Sistema di coordinate locale](PartDesign_CoordinateSystem/it.md) ora consente di aggiungere la visualizzazione del sistema di coordinate locale a diversi oggetti di riferimento.

## Ambiente Path 

### Miglioramenti generali 

-   Path ora può visualizzare correttamente il gcode con i termini ABC dell\'asse
-   Miglioramenti all\'editor degli utensili: modifica semplificata per tipi di utensili selettivi

### Miglioramenti delle lavorazioni 

-   Ora le lavorazioni possono avere più oggetti di base
-   L\'organizzazione del contenitore delle lavorazioni è stata migliorata
-   I valori predefiniti per le impostazioni delle operazioni possono essere controllati tramite SetupSheets

### Operazioni

-   Nuova operazione di compensazione adattativa
-   Nuovo operazione di sbavatura
-   Nuova dressup AxisMap che limita il 4° asse facendo corrispondere una direzione lineare a un asse di rotazione
-   Supporto per oggetti 2D e fresatura di bordi individuali tramite Engrave e Deburr
-   RampEntry dressup ora ha un punto di partenza configurabile
-   L\'operazione PocketShape ora può \'usare il contorno\'

### Post Processori 

-   grbl_post -- argomento per sopprimere i comandi di cambio utensile
-   grbl_g81 post processor

## Ambiente Sketcher 

<img alt="Demo di Vista in sezione di Sketcher" src=images/Sketch-clip-plane-demo.png  style="width:700px;">

-   Il nuovo strumento **[Vista in sezione](Sketcher_ViewSection/it.md)** crea un piano di sezione che rimuove dal modello il materiale che si trova davanti al piano dello schizzo. Questo può essere utile quando il piano dello schizzo si trova all\'interno di un modello solido. Premendo di nuovo lo strumento Vista in sezione si ritorna alla visualizzazione completa.
-   Il **Risolutore dello schizzo** ha beneficiato di miglioramenti ed è ora in grado di rilevare meglio i vincoli ridondanti e conflittuali, specialmente quelli indotti da vincoli simmetrici.
-   È stato aggiunto il nuovo strumento **[Vincolo Diametro](Sketcher_ConstrainDiameter/it.md)**
-   **DoF Finder** è una nuova utilità per aiutare a trovare i gradi di libertà. Nel widget Messaggi del Solutore nel pannello Azioni, il messaggio tradizionale *Schizzo sottovincolato con x gradi di libertà* ora sottolinea in blu il testo *x gradi*. Cliccando su di esso si evidenziano in verde, nella vista 3D, gli elementi che non sono completamente vincolati.
-   **Rimuovi automaticamente le ridondanze** è una nuova casella di controllo nella scheda Messaggi del Risolutore. Se abilitato, impedisce la creazione dei vincoli ridondanti quando l\'utente sta creando lo schizzo e applicando i vincoli ed elimina automaticamente i vincoli ridondanti.
-   C\'è un nuovo comando per eliminare tutti i vincoli contemporaneamente. Si trova nel menu **Schizzo → Strumenti → Elimina tutti i vincoli**.
-   Nuova opzione in **Preferenze → Schizzo → Generale → Nascondi le unità di lunghezza di base per i sistemi di unità supportati**. Ciò nasconde l\'unità per i vincoli dimensionali nella modalità di modifica dello schizzo.
-   Ora è possibile impostare la dimensione dei vertici (punti) in **Preferenze → Visualizzazione → Vista 3D → Dimensioni del marcatore**.
-   Nuovo comando **[Sposta](Sketcher_Move/it.md)** per spostare tutta la geometria selezionata dall\'ultimo punto selezionato. Si trova nel menu a discesa **Schizzo → Strumenti → Sposta**.
-   Aggiunta la casella di controllo *Denominazione estesa* al widget Elenco dei vincoli.

Rilevanti Link del forum:

-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192)
-   [Feature #1632: Allow entering of diameter instead of radius for circle radius constraint](https://forum.freecadweb.org/viewtopic.php?f=8&t=29152)
-   [Sketcher Auto Remove Redundants mode](https://forum.freecadweb.org/viewtopic.php?f=9&t=30594)
-   [Constraints extended naming](https://forum.freecadweb.org/viewtopic.php?f=10&t=28890)

## Ambiente Spreadsheet 

## Ambiente Surface 

## Ambiente TechDraw 

TechDraw ha ricevuto numerose aggiunte e miglioramenti per v0.18.

-   Nuovo Esporta pagina in Dxf
-   Nuovo tutorial per TechDraw
-   Migliorata la formattazione delle quote per viste isometriche, angoli, posizione del testo
-   Migliorati i messaggi di errore
-   Migliorata la formattazione della vista in sezione
-   Consente gruppi di linee personalizzate
-   Preferenze aggiuntive
-   Più facile selezionare i bordi e i segni di centro
-   Direzione della vista in base alla vista 3D corrente o alla faccia selezionata
-   Aggiunte le tolleranze + / \* alle dimensioni
-   Nuova dimensione dell\'angolo da 3 punti
-   Menu contestuale RMB (Right Mouse Button - Pulsante destro del mouse)
-   Zoom dalla tastiera (Ctl+/-)
-   Supporto per dimensioni DMS (Decimal Measurement System - Sistema decimale di misura)

## Manipolazione del materiale 

<img alt="Una schea materiale" src=images/Material-Card-018.png  style="width:300px;"> La gestione del materiale è stata migliorata. Ora è possibile creare delle **schede materiali** per ogni materiale. Le schede possono contenere tutte le informazioni, proprietà fisiche, specifiche architettoniche, collegamenti Web, commenti. ecc. Le schede sono file di testo con il suffisso **.FCMat** e possono essere utilizzate per tutti gli ambienti di FreeCAD.

FreeCAD fornisce le schede materiali per metalli standard, materie plastiche e diversi tipi di acciaio.

## Moduli aggiuntivi 

Alcuni dei nuovi moduli della comunità che sono stati attivamente sviluppati durante il ciclo di sviluppo di 0.18.

-   [A2plus](A2plus_Workbench/it.md) è un nuovo ambiente per assemblare parti differenti in FreeCAD. È un\'estensione di Assembly2 che offre una gestione estesa del colore e della trasparenza per le parti e un nuovo vincolo che utilizza il centro di massa delle parti.

-   [Curves](https://github.com/tomate44/CurvesWB), una raccolta di strumenti per creare e modificare curve e superfici NURBS.

-   [Nurbs](https://github.com/microelly2/freecad-nurbs), una raccolta di script per la gestione di superfici e curve a mano libera.

-   [Silk](https://github.com/edwardvmills/Silk), una raccolta di strumenti di modellazione di superfici NURBS focalizzata su curve di basso livello e continuità delle giunzioni.

-   [Flamingo Workbench](Flamingo_Workbench/it.md) una serie di comandi e di oggetti FreeCAD personalizzati che consentono di velocizzare il disegno di strutture e tubazioni.

-   [Ingegneria civile e Trasporti](Civil_Engineering_Workbench/it.md)

-   [GDT](https://github.com/juanvanyo/FreeCAD-GDT), dimensionamento geometrico e tolleranze (GD&T).

-   [InventorLoader](https://github.com/jmplonka/InventorLoader) per importare i file di Autodesk Inventor (in corso).

-   [Kicad StepUp Workbench](https://www.freecadweb.org/wiki/KicadStepUp_Workbench) ha lo scopo di aiutare gli utenti di KiCad e FreeCAD nella collaborazione ECAD e MCAD.

-   [CadQuery FreeCAD Module](https://github.com/jmwright/cadquery-freecad-module/wiki) è un ambiente che consente agli utenti di scrivere script Python, ed è adattato a quelli basati sull\'API CAD di CadQuery. Rende disponibile un nuovo editor di codice e le variabili di script possono essere modificate dinamicamente attraverso l\'uso di una finestra di dialogo dei parametri. L\'ambiente aggiunge anche un menu che include le normali operazioni sui file per gli script CadQuery (apri, nuovo, chiudi, ecc.), e script di esempio per aiutare gli utenti ad apprendere nuovi concetti.

-   [Defeaturing Workbench](Defeaturing_Workbench/it.md) è destinato alla modifica di modelli STEP importati, per rimuovere dal modello le funzioni selezionate.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.18/it
