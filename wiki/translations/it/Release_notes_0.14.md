


<div class="mw-translate-fuzzy">

FreeCAD 0.14 è stato rilasciato il 1 Luglio 2014. Questo è un riassunto dei cambiamenti più interessanti. L\'elenco completo delle modifiche è disponibile in [Mantis changelog](http://www.freecadweb.org/tracker/changelog_page.php). Versioni precedenti in: [0.13](Release_notes_013/it.md) - [0.12](Release_notes_012/it.md) - [0.11](Release_notes_011.md)


</div>

<img alt="" src=images/Freecad_jeep.png  style="width:1024px;">


<center>

Jeep modellata da Psicofil


</center>

## Aspetti generali {#aspetti_generali}

### Migrazione del sito {#migrazione_del_sito}

Abbiamo finalmente spostato tutte le applicazioni web di FreeCAD da [SourceForge](http://www.sourceforge.net) al nostro [own domain](http://www.freecadweb.org). La nuova homepage di FreeCAD si trova all\'indirizzo <http://www.freecadweb.org>, il wiki ora è a <http://www.freecadweb.org/wiki>, il bug and features tracker a <http://www.freecadweb.org/tracker>, e il forum a <http://forum.freecadweb.org>. Se avevate un account per una di queste applicazioni quando eravamo su SourceForge, è possibile recuperarlo seguendo queste [istruzioni](http://forum.freecadweb.org/viewtopic.php?f=8&t=4942).

L\'unica parte di FreeCAD che rimane in SourceForge è il repository git principale, allo stesso indirizzo: <http://sourceforge.net/p/free-cad/code/ci/master/tree/> ma tale codice è anche riflesso automaticamente su GitHub, all\'indirizzo <http://github.com/FreeCAD/FreeCAD_sf_master>

Se non conosci ancora l\'incredibile comunità FreeCAD, facci visita sul forum, e sarai stupito dal suo talento, energia e disponibilità.

### Passato a PySide, FreeCAD è ora pienamente LGPL {#passato_a_pyside_freecad_è_ora_pienamente_lgpl}

Date le molte complicazioni causate dal modello a doppia licenza di FreeCAD (LGPL & GPL), alcuni dei componenti di FreeCAD (cioè il kernel OpenCasCade) incompatibili con il codice GPL, abbiamo deciso di convertire tutte le restanti parti di codice GPL di FreeCAD in LGPL. Come risultato di questa operazione, [PyQt](http://en.wikipedia.org/wiki/PyQt) non più usato, ed è sostituito da [PySide](http://en.wikipedia.org/wiki/PySide). Non ci sono grosse conseguenze per gli autori di script python, PyQt può ancora essere utilizzato all\'interno FreeCAD.

Dopo che abbiamo completato il passaggio a LGPL, anche OpenCascade è [passata a LGPL](http://www.opencascade.org/getocc/license/), cosa che avrebbe anche risolto tutti i nostri conflitti licenza. Ma ora abbiamo un modello di licenza molto più chiaro e unitario, che dovrebbe soddisfare tutte le distribuzioni linux più severe.

### Plugins e progetti collaterali: Parts library, BOLTS, importatore Eagle {#plugins_e_progetti_collaterali_parts_library_bolts_importatore_eagle}

L\'ultimo anno ha visto emergere alcuni progetti collaterali interessanti a fianco di FreeCAD. È stato avviato dalla comunità e sta lentamente crescendo una [Parts library](http://github.com/yorikvanhavre/FreeCAD-library) costituita da un insieme di parti riutilizzabili da aggiungere ai propri modelli FreeCAD. Può essere avviata e utilizzata dall\'interno di FreeCAD con l\'uso di una macro.

Un altro progetto simile, ma più ambizioso è [BOLTS](http://bolts-library.org/), che è anche una libreria di parti, ma costruite con script parametrici, in grado di produrre una grande varietà di parti parametriche. BOLTS, anche se applicazione indipendente, può anche essere eseguito da FreeCAD avviando una macro. L\'immagine sottostante mostra BOLTS in esecuzione all\'interno FreeCAD.

<img alt="" src=images/Freecad-bearing.png  style="width:1024px;">

Un altro progetto esterno interessante è [EAGLE importer](http://sourceforge.net/projects/eaglepcb2freecad/), che permette di importare in FreeCAD progetti di schede PCB realizzati da diverse applicazioni.

### Esportazione WebGL {#esportazione_webgl}

Ora, da FreeCAD, è possibile esportare la scena come un file[WebGL](http://en.wikipedia.org/wiki/WebGL)-abilitato html. Questo file include un visualizzatore embedded [three.js](http://threejs.org/)-based che consente di ispezionare la scena dal web senza alcun plugin, purché lo si visualizzi con un browser WebGL-compatibile.

### Sistema di unità di misura {#sistema_di_unità_di_misura}

Infine, è stato implementato un sistema di [unità di misura](units/it.md) a livello di FreeCAD, quindi a disposizione di tutti i moduli. Ora è possibile scegliere uno schema unità dalle preferenze. Gli schemi attualmente disponibili includono millimetri, metri e misure imperiali, ma a breve dovrebbe diventare disponibile molto altro. Una volta che lo schema è impostato, la maggior parte delle proprietà e gli strumenti di FreeCAD utilizzano di preferenza questa unità. Ma il sistema è molto flessibile, e nella maggior parte dei casi, si possono mescolare le unità quanto si vuole, per esempio dando misure in pollici in un set di documenti in millimetri.

### Style Sheets {#style_sheets}

FreeCAD 0.14 diventa ancora più personalizzabile con l\'aggiunta di [Style Sheets](http://forum.freecadweb.org/viewtopic.php?f=8&t=4700&start=30) utilizzato per controllare l\'immagine di sfondo nella finestra principale. L\'utente non è più vincolato allo sfondo di pietra grigia. Quasi ogni tipo di immagine, o disegno personalizzato possono essere utilizzati per riempire lo sfondo della finestra principale di FreeCAD.

<img alt="" src=images/Style_Sheets.png  style="width:1024px;">

### Stile di visualizzazione {#stile_di_visualizzazione}

La barra predefinita degli strumenti Vista è stato ampliato con un paio di nuovi pulsanti per commutare facilmente la visualizzazione di tutta la vista tra la modalità 3D wireframe, ombreggiata o linee.

### Finestra 3D anti-aliasing {#finestra_3d_anti_aliasing}

Nuove opzioni anti-aliasing, che si possono trovare nelle preferenze, sono state aggiunte al sistema vista 3D di FreeCAD. Se avete un buon chip grafico 3D, ora è possibile apprezzare FreeCAD con una elevata qualità anti-aliasing.

## Part

### Loft e Sweep {#loft_e_sweep}

Gli strumenti [Part Loft](Part_Loft/it.md) e [Part Sweep](Part_Sweep/it.md) è sono stati migliorati e ora è possibile utilizzare gli oggetti Draft come profili.

### Offset

Il nuovo strumento [Part Offset](Part_Offset/it.md) crea copie di una forma selezionata ad una determinata distanza dalla forma base.

### Spessore

Ora è disponibile un nuovo strumento [Part Thickness](Part_Thickness/it.md). Questo strumento funziona su una forma solida, e la trasforma in un oggetto cavo, dando a ciascuna delle sue facce un dato spessore.

### Make Compound {#make_compound}


<div class="mw-translate-fuzzy">

Il modulo [Part](Part_Workbench/it.md) ora fornisce uno strumento [Make Compound](Part_MakeCompound/it.md), che consente di creare rapidamente un oggetto composto da un insieme di forme selezionate.


</div>

### Primitive Part {#primitive_part}

Nuove Part primitive sono state aggiunte allo strumento [Crea primitive](Part_CreatePrimitives/it.md): Prismi, poligoni regolari e spirali ora sono facili da creare compilando un paio di parametri. Inoltre, alcuni strumenti del modulo [Draft](Draft_Workbench/it.md) ora possono usufruire di questa funzione e creare anche queste primitive, invece del loro regolare oggetto Draft, se l\'opzione corrispondente è impostata nelle impostazioni delle preferenze Draft.

![](images/Part_Create_Primitives1.jpeg )

### Strumenti Misura {#strumenti_misura}


<div class="mw-translate-fuzzy">

Un nuovo set di strumenti di misura è stato aggiunto a [Part](Part_Workbench/it.md). Con questi, è possibile selezionare due elementi di una forma (vertici, spigoli o facce), e visualizzare la loro distanza in distanza assoluta, e lungo assi X e Y.


</div>

## PartDesign & Sketcher {#partdesign_sketcher}

### Validate sketch {#validate_sketch}


<div class="mw-translate-fuzzy">

Ora l\'ambiente [Sketcher](Sketcher_Workbench/it.md) dispone del nuovo strumento [Validate sketch](Sketcher_Validate/it.md) per aiutarvi a convalidare uno schizzo, trovando vincoli mancanti o ridondanti. Si può anche aggiungere automaticamente alcuni vincoli mancanti, al fine di rendere lo schizzo completamente vincolato.


</div>

### Gear generator {#gear_generator}


<div class="mw-translate-fuzzy">

Uno strumento [involute gear generator](PartDesign_InvoluteGear/it.md) è stato aggiunto all\'ambiente [PartDesign ](PartDesign_Workbench/it.md), per creare rapidamente gli ingranaggi da parametri.


</div>

## Drawing

### Proiezioni automatiche {#proiezioni_automatiche}

L\'ambiente Drawing continua ad essere migliorato con alcune nuove interessanti funzionalità. Proiezioni ortogonali ora permette di visualizzare tutte le viste, nonché un maggiore controllo sulle singole viste. Un\'altra caratteristica fondamentale, Drawing Templates ora può contenere i dati che definiscono la posizione di Bordo e Cartiglio il che limita automaticamente le proiezioni all\'interno del Bordo, e allo stesso tempo evita automaticamente di inserirle nello spazio occupato dal cartiglio.

<img alt="" src=images/DrawingWB.png  style="width:1024px;">

### Simboli

Nell\'ambiente [Drawing](Drawing_Workbench/it.md) è disponibile un nuovo strumento [Simbolo](Drawing_Symbol/it.md) consentendo di inserire rapidamente oggetti SVG sul foglio da disegno. Questi oggetti vengono memorizzati nel file di FreeCAD, quindi non c\'è bisogno di inviare il file in formato SVG originale quando si distribuiscono dei file.

## Raytracing

### Nuovi strumenti di rendering {#nuovi_strumenti_di_rendering}

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Anche l\'ambiente [Raytracing](Raytracing_Workbench/it.md) ha ricevuto qualche attenzione, e la sua barra degli strumenti è stata rielaborata. I \"vecchi\" pulsanti che producevano manualmente i file Povray parziali sono stati rimossi (sono ancora presenti nel menu Raytracing), e ora si può produrre un rendering più o meno allo stesso modo come si usa l\'ambiente [Drawing](Drawing_Module/it.md): Si crea un nuovo progetto, si assegna ad esso un modello, poi lo si riempie con la vista degli oggetti. Quando si ha finito, basta premere il pulsante di rendering, o esportarlo in un file pronto per il rendering esterno a FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Inoltre, il sistema di [modelli Raytracing](Raytracing_Workbench#Templates/it.md) è stato esteso, e i modelli ora sono più facili da manipolare e creare.


</div>

Gli script .pov prodotti da FreeCAD ora contengono il rapporto di auto-aspetto. Gli utenti non devono più mantenere un rapporto di aspetto 4:3 nelle impostazioni Raytracing o modificare manualmente l\'uscita e cambiare i rapporti, per ottenere un corretto rendering. Ora possono essere inseriti qualsiasi larghezza e altezza senza timore che gli oggetti vengano restituiti schiacciati o allungati.

### Supporto Luxrender {#supporto_luxrender}


<div class="mw-translate-fuzzy">

Insieme al supporto esistente per [POV-Ray](http://en.wikipedia.org/wiki/POV-Ray), il modulo [Raytracing](Raytracing_Workbench/it.md) ora supporta anche [LuxRender](http://en.wikipedia.org/wiki/LuxRender). Se POV-Ray è un [classical-style raytracer](http://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29), che spara raggi dalla telecamera per trovare il colore di ogni pixel dell\'immagine, Luxrender invece è un [unbiased renderer](http://en.wikipedia.org/wiki/Unbiased_rendering), che richiede molto più tempo per rendere le scene, ma è in grado di produrre una illuminazione molto più realistica.


</div>

## Foglio di calcolo {#foglio_di_calcolo}

In FreeCAD è stato aggiunto un nuovo [ambiente Spreadsheet](Spreadsheet_Workbench/it.md). Esso consente di creare un oggetto [foglio di calcolo](Spreadsheet_Create/it.md), che contiene dati in un foglio bidimensionale. Dispone inoltre di un editor in modo da poter modificare il contenuto del foglio di calcolo (sono supportati testi, numeri e alcune formule di base), e uno speciale oggetto [cell controller](Spreadsheet_Controller/it.md), che può eseguire la scansione del documento per certi tipi di oggetti, estrarre da essi una certa proprietà, e compilare un determinato intervallo di celle con questi valori.

<img alt="" src=images/Arch_tutorial_53.jpg  style="width:1024px;">

## Draft

### Importare e esportare DWG {#importare_e_esportare_dwg}


<div class="mw-translate-fuzzy">

Ora FreeCAD è in grado di importare ed esportare verso il [formato DWG](http://en.wikipedia.org/wiki/.dwg), grazie ala multipiattaforma free [Teigha Converter](http://www.opendesign.com/guestfiles/TeighaFileConverter). Quando Teigha Converter è installato, e il suo percorso è impostato nelle preferenze di Draft, FreeCAD è in grado di usarlo per importare ed esportare file DWG, convertendoli in dxf, quindi utilizzando l\'importatore ed esportatore dxf di Draft. L\'importazione e l\'esportazione dei file DWG ha quindi le stesse limitazioni del [formato dxf](Draft_DXF/it.md).


</div>

### Lavorare con i gruppi da Draft verso Drawing {#lavorare_con_i_gruppi_da_draft_verso_drawing}


<div class="mw-translate-fuzzy">

Lo strumento [Draft to Drawing](Draft_Drawing/it.md), utilizzato per posizionare oggetti di Draft in un foglio di disegno [Drawing](Drawing_Module/it.md), ora può essere applicato ai gruppi, e permette di creare un numero inferiore di Viste di oggetti nel foglio di disegno. Combinando in modo razionale gli oggetti Draft in gruppi, si dispone di un modo rapido per controllare l\'aspetto di molti oggetti nella pagina.


</div>

### Dimensioni ricodificate {#dimensioni_ricodificate}


<div class="mw-translate-fuzzy">

Lo strumento [Dimensioni](Draft_Dimension/it.md) è stato completamente ricodificato, e gli oggetti Dimensione ora si comportano molto meglio, hanno acquisito alcune nuove proprietà, come frecce più belle e scalabili, un maggiore controllo sulla posizione del testo e sulla direzione della dimensione , e soprattutto un migliore supporto per l\'ambiente [Drawing](Drawing_Module/it.md). Ora è possibile inserire le dimensioni in qualsiasi piano dello spazio 3D, e ottenere risultati corretti quando si metteno su un foglio di disegno con lo strumento [Drawing](Draft_Drawing/it.md).


</div>

<img alt="" src=images/Draft_dimensions_recode.jpg  style="width:1024px;">

### Tratteggio


<div class="mw-translate-fuzzy">

L\'ambiente [Draft](Draft_Module/it.md) dispone anche di un nuovo \"giocattolo\": tratteggio. Sul specifici oggetti Draft (quelli che formano una forma chiusa come polilinee chiuse, rettangoli, poligoni regolari o cerchi), ora è possibile applicare un tratteggio. Attualmente, sono disponibili di default solo un paio di modelli di tratteggio, ma poiché tali modelli sono molto facili da creare (sono semplici file SVG), e possono già essere aggiunti dall\'utente dei modelli personalizzati, la collezione di default potrebbe crescere rapidamente. Gli oggetti Draft con i riempimenti sono anche supportati fedelmente dall\'ambiente [Drawing](Drawing_Module/it.md).


</div>

<img alt="" src=images/Draft_hatches.jpg  style="width:1024px;">

### Ellissi

È stato aggiunto il supporto per le [ellissi](Draft_Ellipse/it.md), l\'ambiente Draft ora permette di disegnare ellissi complete o porzioni di ellissi.

### Smussi

Allo stesso modo dei raccordi, che erano apparsi nella [versione 0.13](Release_notes_013/it.md), ora i rettangoli, contorni e poligoni di Draft hanno una proprietà smusso, che smussa i loro angolo. Lo smusso viene applicato prima del raccordo, e entrambe le proprietà possono essere utilizzate insieme, questo consente di trasformare rapidamente un contorno molto semplice in un oggetto complesso fatto di molte sezioni.

### Upgrade e Downgrade ricodificati {#upgrade_e_downgrade_ricodificati}

Gli strumenti [Upgrade](Draft_Upgrade/it.md) e [Downgrade](Draft_Downgrade/it.md), prima ermetici pezzi di magia, di cui non si era mai troppo sicuri di quello che sarebbe stato il risultato, sono stati ricodificati, e ora appare un messaggio molto più amichevole che informa su quanto è stato fatto e perché. Ora sono disponibili anche per gli scripting Python, non solo il blocco, ma anche le loro singole operazioni interne, in modo da poter ordinare con precisione un determinato tipo di Upgrade da eseguire.

### Facebinder


<div class="mw-translate-fuzzy">

È stato aggiunto un nuovo strumento [Facebinder](Draft_Facebinder/it.md), che fa un\'operazione molto semplice, ma potenzialmente molto utile: Riunisce qualsiasi quantità di facce selezionate da diversi oggetti, e le usa per creare un nuovo oggetto. Il nuovo oggetto mantiene i collegamenti agli oggetti originali, in modo che qualsiasi successiva loro modifica viene riflessa nell\'oggetto facebinder. Questo dovrebbe essere utile soprattutto per gli oggetti [architettura](Arch_Workbench/it.md), dove ora è possibile creare nuovi oggetti dalle facce di diversi altri oggetti.


</div>

### Shape strings {#shape_strings}

Lo strumento [ShapeString](Draft_ShapeString/it.md) crea oggetti planari da un testo e un tipo di carattere TrueType. Questi oggetti, a differenza delle comuni annotazioni come sono i [Testi](Draft_Text/it.md), sono oggetti 3D reali, possono essere estrusi, e quindi possono essere usati per creare incisioni o altri tipi di oggetti 3D con il testo in rilievo.

### Curve di Bezier {#curve_di_bezier}


<div class="mw-translate-fuzzy">

Accanto alle curve [arco di circonferenza](Draft_Arc/it.md) e [B-spline](Draft_BSpline/it.md) già esistenti, nel modulo Draft ne è stata inserita una nuova: la [curva di Bezier](Draft_BezCurve/it.md). Può essere creata cliccando dei punti, allo stesso modo di altri oggetti Draft, ma poi si può [editare](Draft_Edit/it.md) e modificare i suoi punti di ancoraggio, controllare con precisione la forma della curva.


</div>

## Arch

### Struttura Preset e profili {#struttura_preset_e_profili}


<div class="mw-translate-fuzzy">

Lo strumento [Struttura](Arch_Structure/it.md) ha avuto diversi miglioramenti: ora è dotato di caratteristiche predefinite che consentono di creare rapidamente una trave o una colonna sulla base di un profilo standard di tipo INP o HEB, e di un sistema di posizionamento più facile, con una speciale modalità di [aggancio](Draft_Snap/it.md). Ora è anche possibile assegnare agli elementi strutturali un percorso di estrusione, quindi sono diventate possibili delle configurazioni molto avanzate. Alcuni dei pezzi offerti da [BOLTS](Release_notes_0.14#Plugins_and_side_projects:_Parts_library.2C_BOLTS.2C_Eagle_importer.md) possono anche essere creati direttamente come elementi strutturali Arch.


</div>

### Finestre predefinite {#finestre_predefinite}

Anche allo strumento [Finestra](Arch_Window/it.md) è stato aggiunto un sistema di finestre predefinite. Anche se ancora basate su schizzi, cosa che assicura la massima flessibilità (praticamente si può creare facilmente qualsiasi tipo di finestra), ora si possono costruire nuove finestre partendo da una serie predefinita. Basta scegliere un preset, inserire alcuni parametri, e posizionare la finestra in un muro esistente o in un elemento strutturale, se lo si desidera. A livello inferiore, verrà creato lo schizzo appropriato, che è modificabile in qualsiasi momento.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:1024px;">

### Spazio

Ora è disponibile un nuovo oggetto [Spazio](Arch_Space/it.md) che consente di costruire, marcare e calcolare spazi ed aree del pavimento. Questi oggetti spazio comprendono sempre un volume solido, in modo da poter sempre conoscere il loro volume e superficie. Essi possono essere costruiti da una forma solida, o dalla serie delle facce di contorno.

### Muri multistrato {#muri_multistrato}

Ora i [Muri](Arch_Wall/it.md) possono essere multistrato con un trucco molto semplice: più pareti possono essere basate su una stessa linea di base, specificando una distanza di spostamento dalla linea di base. Questo, combinato ad esempio con [Carpenteria](Arch_Frame/it.md), consente di realizzare complesse strutture di pareti, o pareti con strati isolamenti. Inoltre, questi muri sono consapevoli dei loro \"muri fratelli\" (le altre pareti basati sulla stessa linea di base), e qualsiasi finestra posta su una di queste pareti anche creare una apertura nei suoi fratelli.

<img alt="" src=images/Screenshot_arch_multiwall.jpg  style="width:1024px;">

### Scale

È stato aggiunto anche un nuovo strumento [Scala](Arch_Stairs/it.md), che permette di costruire le scale complesse impostando alcuni parametri. Attualmente sono disponibili solo scale dritte, ma la lista crescerà nel tempo. Queste scale hanno molti parametri di configurazione, quali le dimensioni dello scalino, l\'alzata, o il tipo di struttura.

### Armature

Con lo strumento [Armature](Arch_Rebar/it.md) sono stati introdotti i rinforzi. Anche essi si basano anche sugli schizzi, per garantire grande flessibilità. Essi sono creati essenzialmente disegnando la sagoma delle barre sulle facce appropriate degli [elementi strutturali](Arch_Structure/it.md), poi convertendo le sagome in armature reali.

<img alt="" src=images/Screenshot_arch_rebar.jpg  style="width:1024px;">

### Carpenteria

I sistemi carpenteria sono utilizzati ovunque in architettura: cancello, sistemi strutturali, telaio dei muri, ecc. Il nuovo strumento [Carpenteria](Arch_Frame/it.md) (Frame) permette di creare facilmente tutti i tipi di telai, combinando un oggetto profilo, che può essere qualsiasi forma piatta estrudibile, quale un rettangolo o un cerchio, e un oggetto percorso, che definisce le linee della estrusione a cui gli elementi dell\'oggetto profilo sono sottoposti. I percorsi sono tipicamente disegnati con l\'ambiente [Sketcher](Sketcher_Workbench/it.md). Questi oggetti Carpenteria possono poi essere trasformati in pareti o strutture, se necessario.

### Ispeziona

Ora nell\'ambiente Arch è disponibile un altro strumento semplice, ma utile: la modalità [Ispeziona](Arch_Survey/it.md). In questa modalità, quando si clicca su vertici, spigoli, facce o oggetti interi, si ottiene la loro altezza, lunghezza, area o volume. Queste informazioni sono visualizzate sul modello, ma sono anche copiate negli appunti, e raccolte come testo, quindi è facile incollale in altre applicazioni, fornendo un flusso di lavoro piuttosto veloce per definire le fatture.

### Tutorial

Un nuovo [tutorial](Arch_tutorial/it.md) di 35 pagine descrive l\'ambiente Arch in tutti i suoi dettagli, proponendo un esercizio completo.

### Importare e esportare file IFC {#importare_e_esportare_file_ifc}


<div class="mw-translate-fuzzy">

È stato fatto molto lavoro sia su FreeCAD che su [IfcOpenShell](http://www.ifcopenshell.org), che è la parte di software responsabile della gestione dei file IFC nel modulo Arch. Quando si utilizza una [versione di sviluppo](http://github.com/aothms/IfcOpenShell) di IfcOpenShell, oltre a uno spettacolare incremento di velocità durante l\'importazione di un file IFC medio (circa 50Mb), FreeCAD è anche in grado di esportare i modelli in formato IFC. Il supporto all\'esportazione è ancora nelle prime fasi di sviluppo, ma riesce già a esportare i file in modo leggibile senza errori dalla maggior parte delle principali applicazioni che supportano IFC.


</div>

## Lista completa {#lista_completa}

L\'elenco completo delle correzioni e delle nuove funzionalità può essere letto suhttp://freecadweb.org/tracker/changelog\_page.php

[Category:News{{\#translation:}}](Category:News.md) [Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Releases{{\#translation:}}](Category:Releases.md)
