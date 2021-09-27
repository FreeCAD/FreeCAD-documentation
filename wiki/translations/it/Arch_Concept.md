# Arch Concept/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}


<div class="mw-translate-fuzzy">

Questa pagina è un tentativo di raccogliere le idee sul disegno parametrico nel campo dell\'architettura per la costruzione del [Modulo Architettura](Arch_Workbench/it.md). Dato che esso è un po\' diverso rispetto a quello dell\'ingegneria meccanica, voglio definire un po\' meglio i concetti prima di pensare a come iniziarne l\'attuazione\... Sentitevi liberi di aggiungere le vostre idee!


</div>

## Software simili 

-   [Revit](http://en.wikipedia.org/wiki/Revit)

-   [Archicad](http://en.wikipedia.org/wiki/Archicad)

-   [Generative Components](http://en.wikipedia.org/wiki/Generative_Components)

## Formati dei file 

-   [STEP](http://en.wikipedia.org/wiki/ISO_10303) - già pienamente funzionante in FreeCAD
-   [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)
    -   <http://forge.osor.eu/plugins/wiki/index.php?id=175&type=g> un SDK di IFC
    -   <http://www.bimserver.org/>
    -   <http://konstruct.nl/parsing-ifc-stepexpress-files-in-python-and-s>

## Concetti generali 

-   FreeCAD è perfetto per questo compito. Disegnare con oggetti parametrici ridimensionerà di molto l\'unico vero problema che vedo in FreeCAD, che è quello di lavorare con migliaia di oggetti. Tutto il necessario è già lì, disponibile, ad esempio, i tipi di oggetti personalizzati, le proprietà personalizzate, ecc.. La difficoltà principale, cioè, progettare un modello generale per trattare l\'interazione tra gli oggetti, ora è potenzialmente superata, dato che FreeCAD ha introdotto un grafico delle dipendenze soprattutto per tale scopo.

-   [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) (Building Information Modeling) **(modello d\'informazioni di un edificio)** è un concetto inventato da alcuni fornitori di software di disegno parametrico per costruzioni, principalmente Autodesk. Significa che non si progetta più un edificio disegnando, ma inserendo informazioni (parametri). Il software produce poi automaticamente un disegno. A mio parere, questo è inverosimile e, più che altro, è solo un concetto di propaganda. Neppure nei software BIM più avanzati (Revit, Archicad e Microstation GC), non si può astrarre l\'atto del disegnare a meno che non si voglia sopprimere ogni creatività. L\'obiettivo non è quello di essere il più automatico, ma di essere flessibile.

-   Il disegno parametrico di ingegneria meccanica si basa generalmente sullo storico delle modifiche e sulla risoluzione di vincoli. Questi due concetti sono molto meno importanti nella progettazione degli edifici, dato che raramente si vuole andare all\'indietro nei passaggi fatti (di solito sono molto semplici), e mantenere dei vincoli quali orizzontalità, angolo o distanza in quanto, anche se sono utili, non sono così importanti come nel designo meccanico.

-   Il disegno parametrico in architettura si basa sugli archetipi: muro, porta/finestra, tetto, solaio, trave, sono quelli di base. Oltre a questi, quelli che si usano maggiormente sono dei loro derivati.

-   Si fa un uso intenso dell\'assemblaggio: ad esempio per formare una vetrata sono raggruppate insieme più finestre.

-   La Relazione è la chiave. Raramente gli elementi sono molto complessi oppure richiedono molto lavoro di modellazione, ma devono spesso essere trasformati con la giustapposizione o l\'inclusione di altri elementi. Ad esempio, un muro non è altro che una semplice estrusione, ma deve collegarsi ad altre pareti, oppure si deve fare un foro quando una finestra viene inserita in esso. Come costruire questo modello di relazione e di come/dove memorizzarlo è il grande problema.

-   Un problema di quasi tutti i software di modellazione parametrica di edifici è che si basano pesantemente su questi oggetti archetipo. La creazione di nuove parti, non-in-libreria, è estremamente impegnativa con alcuni software (Archicad) o molto più facile con altri (Revit), ma è sempre un po\' un problema, e c\'è sempre una grande difficoltà di comunicazione tra le parti \"parametriche\" e le parti \"non-parametriche\". Fondamentalmente si ottiene il pieno potenziale del software solo se si utilizzano delle parti che sono fatte per lo specifico tipo di lavoro. Ad esempio trasformare un solido semplice in una parete è estremamente problematico.

-   Un documento di Autodesk su Revit: <http://images.autodesk.com/adsk/files/bim_parametric_building_modeling_jan07_1_.pdf> questo articolo è principalmente una propaganda per Revit, e diversi concetti, secondo me, sono poco importanti, come i disegni 2D \"generati\" dalla possibilità di modificare il modello in 2D, ma è comunque interessante.

-   La velocità di calcolo degli oggetti, a mio parere, non è un problema molto importante. La modifica di un oggetto non dovrebbe influenzare molti altri oggetti, e di solito è fatta in una fase di aggiustamento, quindi non è così importante avere aggiornamenti con la velocità di un fulmine. Una cosa importante, però, è quello di salvare sempre la forma definitiva degli oggetti, in questo modo, quando si aprono i modelli salvati, non si richiedono calcoli. Prima di salvare, si dovrebbe sempre ricalcolare tutto.

-   Avere uno strumento per le sezioni molto evoluto è assai importante. Planimetrie, prospetti, sezioni, solai: sono tutti strumenti BIM simili, in quanto sono \"piani di taglio\" assonometrici/ortografici, attraverso il modello BIM.

-   C\'è il problema delle annotazioni. Dove tracciare dimensioni? Sul modello? Direttamente sul foglio svg? Non è molto pratico \... Questo punto deve essere ulteriormente analizzato. Le dimensioni apparterranno a un livello che può essere attivato o disattivato in fase di stampa (plot). Inoltre, poiché le stampe sono fatte in una scala specifica, le dimensioni saranno scalate per corrispondere alla scala selezionata o a una scala personalizzata, scelta dall\'utente.

-   Un \"edificio parametrico\" deve essere inteso come un mix di oggetti relazionali compatibili (basati su archetipi) e di altri, non archetipo-based. Trasformare un oggetto da una categoria ad un\'altra dovrebbe essere fattibile, e tutti dovrebbero comportarsi allo stesso modo durante il sezionamento (e la quotatura).

-   Un sistema per creare graficamente dei nuovi componenti ed assiemi, se possibile. Gli assemblaggi dovrebbero funzionare come \"sub-modelli\" che possono essere inseriti/importati/collegati a qualsiasi modello BIM. In questo modo, un sub-modello può essere aggiornato/sostituito e questa modifica si riflette automaticamente nel modello BIM (se il sub-modello è \"collegato\", se è \"importato\", quindi l\'utente può selezionare se \"aggiornare\" il modello per riflettere l\'ultima versione del sub-modello, altrimenti rimane come l\'ultimo importato).

-   Una modalità di modifica, in modo da poter modificare la forma originale che ha generato la parte.


<div class="mw-translate-fuzzy">

## A proposito degli archetipi 

-   Tutti gli archetipi dovrebbe sempre comportarsi come oggetti di programmazione orientata a oggetti (object-oriented): è possibile creare una nuova classe basata su un\'altra classe.

-   Tutti gli archetipi dovrebbero essere in grado di interagire reciprocamente con gli oggetti comuni. Per questo, gli oggetti comuni probabilmente avrebbero bisogno di proprietà personalizzate.

-   Le pareti dovrebbero essere definite da un semplice contorno (che sarebbe estruso orizzontalmente, poi verticalmente), da una forma piana (a cui semplicemente sarebbe conferito uno spessore) o da un solido (a cui non sarebbe fatto nulla). Il risultato sarebbe sempre un solido. I suoi parametri quindi variano, secondo i dati usati al momento della sua creazione.

-   Le pareti dovrebbe connettersi nelle loro intersezioni o nei punti di contatto.

-   Le pareti potrebbero essere realizzato in vari strati (materiali). Gli stessi materiali dovrebbero collegarsi tra loro.

-   Walls don\'t really need a drawing tool. You make them easily by converting something else. But in that case, the draft module could gain a \"double-line\" tool.

-   Porte e finestre sono oggetti molto semplici, il loro parametri riguardano quasi solo la luce interna. Ma devono avere una \"scatola\" che crea un vuoto negli altri oggetti (in cui sono inserite).

-   Anche travi e solette sono semplici, ma a seconda dei loro materiali devono essere in grado di connettersi ad altre solette, travi e pareti. Travi e solette potrebbe anche essere unite in un unico elemento \"strutturale\". Ci sono anche i pilastri. Tutti questi potrebbero essere definiti allo stesso modo delle pareti, con un contorno, una forma o un solido. Potrebbero anche essere basati sulla stessa base delle pareti \...

-   I tetti sono un tipo speciale di oggetto, in realtà di per sè non molto interessante, ma utile in quanto è fastidioso calcolare un tetto manualmente. Fondamentalmente è necessario creare una forma basata su un profilo e su una inclinazione. Dovrebbe essere facile da fare e da estendere (applicare) poi a altri tipi di tetto.

-   Gli assemblaggi devono essere ulteriormente definiti. Essi sono sostanzialmente costituiti da altre parti, che potrebbe essere qualsiasi cosa, forme, finestre, ecc .. e da proprietà personalizzate, come ad esempio la ripetizione di matrici, la deformazione (seguire una forma?), ecc..

-   Il Costruttore del Sito (Site Builder) - uno speciale set di strumenti deve gestire la creazione e l\'aggiornamento del sito. Questo toolbox deve essere compatibile con i principali modellatori di terreno/sito Open Source e con le applicazioni GIS (come GRASS). Site Builder permetterà la creazione di un sito basato su curve topografiche e una facile manipolazione o aggiornamento del sito stesso. Ciò consentirà una facile creazione di: marciapiedi, cordoli, rampe, strade, paesaggismo, giardini e parcheggi con tutti i sistemi di fogna/deflusso richiesti, ecc.. Il database generato permetterà di stimare lo scavo e il riempimento, nonché le altre informazioni necessarie per rendere il sito funzionante. Site Builder sarà utile anche per generare lo scavo richiesto da un progetto.


</div>

## Archetipi (tipi di oggetti) 

### Muri

La parete è un componente verticale dell\'edificio che segue un percorso in un determinato livello (cioè il primo piano, terzo piano, ecc.) o è estruso orizzontalmente da una superficie verticale. Le pareti sono fatte di strati diversi (materiali, ognuno con spessore e specifiche proprietà termiche), e consentono le aperture (il risultato di sottrazioni) o appendici (unioni). Quando due diverse pareti si intersecano, l\'utente può selezionare l\'opzione per collegare le due pareti (con struttura simile). Tutti i parametri di una parete sono disponibili per i futuri calcoli strutturali e termici, nonché per generare i report (distinte dei materiali). Così, tutti i muri, le aree delle superfici, i volumi, le quantità di materiali, ecc. sono direttamente inseriti nella distinta dei materiali e nella stima dei costi.

Come già menzionato, le pareti in BIM sono definite da una linea/polilinea/etc. che rappresenta il \"centro-linea\" del muro. Questa linea può essere allineata con la faccia esterna del muro, la faccia interna della parete, o il centro della parete, o se l\'utente lo specifica, può essere definita in modo personalizzato. Le pareti hanno diversi parametri che le definiscono:

:   \- il livello in cui parete è collocata (cioè al primo piano, in cantina, al quinto piano, ecc.)
:   \- la larghezza
:   \- l\'altezza
:   \- la composizione

Il livello in cui sono poste le pareti, richiede un inserimento precedente di tale \"livello\" da parte dell\'utente. Quando nel modello BIM viene inserito un livello, esso crea automaticamente una sezione orizzontale, che a sua volta genera un \"foglio\", cioè, una volta inserito livello chiamato \"Primo piano\" ad altezza 0,00 che crea automaticamente una sezione di tutti gli elementi visibili in tale altezza (più e meno, in alto e in basso in modo che porte/finestre/aperture siano visibili in tale primo piano). Le piante e i prospetti come concetto sono simili, poichè fondamentalmente entrambi sono anche essi \"piani di sezione\" che si trovano in una determinata posizione/rotazione nello spazio 3D.

I muri consentono l\'inserimento di oggetti da librerie come: porte, finestre, vetrate, e altri oggetti personalizzati che richiedono un\'apertura in tali muri. Può anche essere inserita solo un\'apertura, se essa è richiesta.

### Porta/finestra (inserire elementi) 

Porte e finestre sono in realtà la stessa cosa, un oggetto completo che può avere un sacco di parametri per definire la sua forma, e un volume invisibile che viene usato per tagliare le aperture attraverso le pareti di ricezione. Essi sono tipicamente inseriti in una parete, ma non sempre. Dal momento che non possono differire molto, dovrebbero essere facili da progettare.

### Tetto

Tetto è semplicemente un modo pratico per calcolare le intersezioni della inclinazione del tetto.

### Solaio (Lastra) 

I solai (lastre - Slab) sono elementi orizzontali, creati a partire da una estrusione verticale di un contorno chiuso o da una faccia, dovrebbero collegarsi per materiale agli altri elementi strutturali, e possono avere una serie di appendici (unione) o fori (sottrazione), e di strati (materiali) (ndt: lo strato di cemento è la soletta). Devono essere calcolati le aree orizzontali e il volume.

### Trave e Pilastro (elemento strutturale) 

Un contorno chiuso o una faccia estrusi in qualsiasi direzione, può avere una serie di appendici (unione) o fori (sottrazione).

### Assemblaggio

Un gruppo di finestre che possono costituire un complessivo

## Meccanismi generici 

-   Dipendenza: le finestre devono sapere in quale parete vengono inserite, le pareti devono sapere quale finestra contengono, ecc .. Vedere parti booleane
-   Giunzioni: le pareti devono sapere con quale altro muro connettersi e collegare correttamente i loro materiali. Lo spostamento di un muro deve quindi ricalcolare i muri vicini. Stabilire una tabella di possibili tipi di giunzioni
-   Categorie di bordi: alcuni bordi non devono essere disegnati quando sono tra 2 oggetti dello stesso materiale. Segnare i bordi per scegliere in seguito come renderizzarli.
-   Auto-raggruppamento: gli oggetti di un certo tipo vanno automaticamente inseriti in gruppi specifici
-   \"Disegnatore di finestre\": Un modo semplice per disegnare finestre parametriche, basate su profili

### Analisi energetica 

-   L\'edificio deve essere ottimizzato in modo appropriato per il programma che serve e anche secondo la specifica posizione geografica. Ad esempio lo stesso progetto può essere costruito a Miami, in Florida (Stati Uniti) oppure a Francoforte (Germania) oppure a Sydney (Australia). Però, deve essere ottimizzato con grandi differenze. Ciò che è appropriato per una posizione, potrebbe essere inadeguato per un\'altra posizione. Il disegno che generiamo con FCBIM dovrebbe essere \"testato\" e vedere come si comporta in termini di consumo energetico. In questo momento sono disponibili alcuni strumenti esterni che consentono di ottimizzare le prestazioni energetiche degli edifici. Le principali applicazioni gratuite/open source sono: EnergyPlus, OpenStudio (una interfaccia GUI per EnergyPlus) e ESP-r.

### Simulazione della luce solare 

-   La raccolta luce del giorno è uno degli approcci fondamentali nella progettazione sostenibile. Molti progetti moderni voltano le spalle alla luce naturale e danno come risultato soluzioni indesiderabili per le persone. Negli Stati Uniti una grande percentuale di edifici crea la cosiddetta Sindrome Sick Building, che causa problemi di salute alle persone che vivono e lavorano in essi. L\'utilizzo della luce allevia in parte questo problema. FCBIM dovrebbe includere strumenti che permettono la simulazione della luce diurna, quali Radiance o LuxRender o YAF(a)ray.

### HVAC e Ventilazione Naturale 

-   Strumenti per inserire disegni e calcolare HVAC (riscaldamento, ventilazione e aria condizionata) e che permettono i calcoli per l\'uso della ventilazione naturale. OpenFOAM dovrebbe essere un candidato in questo settore, che forse andrà ad integrare FCBIM.

## Acquisire conoscenze sulla Costruzione 

Lo sforzo per creare un modulo che renda possibile a FreeCAD di fornire un ambiente per la gestione di un **Modello d\'informazioni di un edificio** (Building Information Modeling - BIM) contemporaneo è in corso. Lo sforzo è orientato a elevare le sue capacità fino a confrontarsi con quelle dei più maturi sistemi di modellazione architettonica quali Revit. Riconosciamo le limitazioni nelle implementazioni di BIM disponibili, una di queste è l\'ignoranza di conoscenze della costruzione. Per questo motivo stiamo anche perseguendo un obiettivo parallelo di sviluppo delle capacità che consentano a FreeCAD di acquisire tali conoscenze in genere create per lo più in fase di progettazione iniziale, ma anche nella fase successiva di progettazione dei dettagli. Nelle sezioni seguenti, documenteremo le capacità che non sono molto comuni negli strumenti a disposizione, ma che riteniamo più adeguate ed efficenti per catturare le informazioni e le conoscenze dalla progettazione alla demolizione. Le sezioni seguenti forniscono le specifiche e linee guida per quanto riguarda la parte **Cosa** di questo sforzo. Si deve compilare il **Come** dei progressi del nostro sforzo. Inutile dire, che le cose cambieranno o saranno modificate dato che la nostra comprensione e l\'applicazione vanno di pari passo.

### Descrizione della procedura per identificare gli oggetti 

La sessione di progettazione della costruzione inizia nel momento in cui il progettista stabilisce la direzione Nord e introduce le restrizioni adeguate in base al regolamento edilizio applicabile nel luogo del progetto. Facendo questo le linee di massima per il nuovo edificio sono stabilite.

#### Oggetto 1: Sito della costruzione 

C\'è solo un sito della costruzione in un progetto. Questo oggetto deve essere creato appena la decisione di progettare una casa è presa dal progettista. Dovrebbe esistere come una forma di contenitore (perché essa cerne uno spazio. Vedremo di più in seguito) con i suoi lati, una parte superiore ed una inferiore. I lati possono essere definiti interattivamente in termini di lunghezza e angolazione. Dovrebbe anche essere possibile aggiungere o rimuovere dei lati se necessario. Sebbene il fondo viene creato piatto, esso può anche essere ridefinito con contorni per fornire la pendenza adeguata. Il fondo è l\'unica parte del sito che dovrebbe essere visibile.

#### Oggetto 2: Direzione Nord 

La direzione Nord è un oggetto che stabilisce l\'angolo in direzione del Nord geografico. Si tratta di una parte del sito e rende possibile determinare per il sito i venti dominanti, il movimento del sole, ecc.

#### Oggetto 3: Limitazioni 

Queste sono le distanze dai confini del sito che sono richieste dal codice. Fanno parte del sito ma richiedono alcuni parametri che devono essere forniti al fine di determinare quali limiti e quali distanze. Ad esempio il limite dal confine vicino alla strada può essere differente dal limite da un confine da un sito vicino. Queste informazioni possono essere fornite in modo interattivo, ma con la direzione nord stabilita, è possibile per il progettista inserire queste informazioni durante la raccolta dei requisiti per la progettazione. Il limite, come il sito, è un tipo di oggetto contenitore.

#### Oggetto 4: Livello di costruzione 

A questo punto l\'impronta di massima per la costruzione è stata stabilita. Questa impronta rappresenta il primo livello dell\'edificio. Il livello di costruzione è un oggetto che permette di integrare diversi sistemi di costruzione. Esempi di sistemi di costruzione sono architettonico, strutturale, elettrico, ecc. Il livello di costruzione, come il sito di costruzione, è una forma di contenitore. Ci possono essere uno o più livelli, che sono ordinariamente impilati uno sopra l\'altro a partire dal basso. Il primo livello è stabilito dopo che si sono designati i limiti per tutti i confini del sito. Possono essere creati nuovi livelli, ma viene modificata solo l\'elevazione del fondo dato che i confini del livello sono invisibili.

#### Oggetto 5: Spazio di costruzione 

Lo spazio è definito per soddisfare la funzione principale della costruzione, ad esempio uno spazio per dormire, mangiare, rilassarsi, lavorare, ecc. Gli spazi vengono creati e raggruppati all\'interno dei livelli. Ci sono diversi tipi di spazi che forniscono le funzioni appropriate in differenti tipi di edifici. Ad esempio, in un tipo di edificio residenziale ci sono 4 tipi principali che includono gli spazi per dormire, soggiorno, servizi e di passaggio.

#### Oggetto 6: Oggetto spazio 

Questo rappresenta tutto ciò che può essere situato in uno spazio. Ogni oggetto avrà alcune conoscenze fondamentali delle sue esigenze. Ad esempio per descrivere un\'area di soggiorno, cioè un oggetto con almeno una zona a sedere, saranno necessari i requisiti di spazio per le gambe e di altezza massima.

#### Oggetto 7: Contenitore di costruzione 

La maggior parte degli oggetti descritti finora sono dei tipi di contenitori. I contenitori hanno una superficie interna che è isolata dai limiti (confini). Ci sono i limiti **Inferiore**, **Superiore** e **Laterali**. Due contenitori possono condividere un limite laterale. Quando si verifica questa condivisione, uno speciale oggetto **Lato-Condiviso** (Share-Side) sostituisce i singoli lati di ciascuno dei contenitori interessati. Si stabilisce un legame tra i due contenitori e si permette loro di comunicare. Ad esempio, quando c\'è un lato in comune tra una camera e un locale di servizio, come un bagno e una camera da letto, quel lato aspetta una qualche forma di trattamento per attenuare il rumore e evitare di intasare la zona notte con troppo rumore. Ogni limite in un contenitore ha una **Forma**. Una forma è un oggetto di tipo contenitore che può avere le necessarie descrizioni o **Proprietà** dei tipici materiali di rivestimento della costruzione.

### Diagramma degli oggetti 

Il seguente diagramma illustra la relazione tra tutti gli oggetti descritti finora.

Oggetti per catturare la conoscenza della costruzione:

<img alt="Oggetti per catturare la conoscenza della costruzione" src=images/BldgComponents.png  style="width:800px;">

_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Arch](Arch_Workbench.md) > Arch Concept/it
