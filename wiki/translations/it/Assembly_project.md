# Assembly project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Questo è il piano del progetto per il modulo **Assemblaggio** come parte del [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).

## Finalità e principi 

Questo è un progetto di sviluppo del software con lo scopo di implementare le funzionalità per creare assemblaggi e prodotti. Si tratta di implementare alcune **funzionalità di base** nei moduli CAD di FreeCAD, **Parte e Assemblaggio** (Part e Assembly).

Le fasi dello sviluppo sono pianificate qui e sono monitorate nel sistema di gestione (Issue tracking system) per tenere un registro storico delle modifiche ben strutturato: [Issue tracker](https://www.freecadweb.org/tracker/)

Si consiglia di controllare gli sviluppi attuali in [Ambienti complementari](External_workbenches/it.md), sezione [Assemblaggio e animazione](External_workbenches/it#Assembaggio_e_animazione.md).

## Risultati

Lo scopo del progetto è quello di consentire a FreeCAD di produrre un disegno come questo:

<img alt="" src=images/Gripper.jpg  style="width:400px;">

Questo si produce utilizzando l\'ambiente di **Assemblaggio** per unire tutti i diversi tipi di Parti in modo vincolato, rimanendo il più vicino possibile alle specifiche ISO 10303 per consentire una facile sostituzione dei modelli.

Un altro obiettivo è quello di poter utilizzare [ODE](http://en.wikipedia.org/wiki/Open_Dynamics_Engine) per la cinematica.

## Riflessioni

### Modello multiplo 

<img alt="" src=images/MultiModel.png  style="width:600px;">

Una caratteristica chiave per il disegno del mondo reale è la possibilità di suddividere un progetto in parti più maneggiabili. È impossibile lavorare su tutti gli aspetti di un disegno contemporaneamente o da soli. Questo vale per la geometria e anche per i lavori di ingegneria come FEM o CAM. Perciò serve che FreeCAD abbia la capacità di scomporre i modelli. Questo apre alcune possibilità:

-   Il **Caricamento ritardato** - Solo se risorse come la grafica e la memoria principale servono per il pezzo in lavorazione.
-   L\'[**Ingegneria simultanea**](http://http://it.wikipedia.org/wiki/Concurrent_engineering) - Permette a molte persone di lavorare sullo stesso progetto
-   Un accurato [**Controllo di versione**](http://http://it.wikipedia.org/wiki/Controllo_versione) - Migliorare il controllo di vari aspetti del disegno
-   e molto altro\....

Un disegno di modello multiplo potrebbe apparire così:

### Gestore dei progetti 

Modello Multiplo significa avere un sacco di file appartenenti a un progetto, di solito, in una directory comune. Un file di progetto e un browser di progetto possono aiutare a organizzare i file. Inoltre è possibile salvare le informazioni aggiuntive sul progetto e avere un sito web del progetto.

1\. Due modalità, la modalità \"Simple\" e la modalità \"Project\". Simple significa solo un documento e che tutti gli assemblaggi e le parti vanno in un unico documento. Se viene aperto o creato un Project, FreeCAD è in modalità di progetto.

2\. Projects. La posizione del file FCPrj sull\'unità definisce una directory di root (radice). Tutti i file sotto di questa directory sono definiti con i percorsi relativi alla directory radice. Una vista aggiuntiva sul lato sinistro conterrà il ProjectExplorer che mostrerà l\'albero della directory con i file che sono gestiti. Questa directory radice è usata anche come root per un ambiente SVN, il che permette poi una facile condivisione e il controllo della versione. I riferimenti esterni (verso una directory fuori dalla radice, un sever condiviso o una risorsa web) saranno gestiti e mostrati separatamente nel ProjectExplorer (una pseudo directory per ogni file del server o server web). In questo modo è possibile ottenere una rapida panoramica sui riferimenti esterni e ridefinire i relativi percorsi.

### Diritti d\'autore 

Ora vediamo i diritti d\'autore (copyright) dei modelli 3D che sono un argomento interessante. I modelli 3D ricadono sotto il copyright. Il copyright spetta al **creatore** del modello. È possibile proteggere solo la forma, che è rappresentata dal modello, con un brevetto o un brevetto di progettazione (US) (EE.UU). I brevetti però coprono solo la creazione di una parte fisica per guadagnare soldi. Come, per esempio, il [brevetto del disegno del mouse di Microsoft](http://patft1.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=D464,651.PN.&OS=PN/D464,651&RS=PN/D464,651).

Quindi dobbiamo sempre ricordare il creatore (detentore del copyright) e tutti i tipi di licenza per ogni modello/prodotto/file di un disegno.

Per la licenza vorrei utilizzare le licenze di tipo CC. <http://creativecommons.org/>

Codici di abbreviazione per le licenze CC:

-   BY = Attribution only
-   BY-ND = Attribution-NoDerivatives
-   BY-NC-ND = Attribution-NonCommercial- NoDerivatives
-   BY-NC = Attribution-NonCommercial
-   BY-NC-SA = Attribution-NonCommercial- ShareAlike
-   BY-SA = Attribution-ShareAlike
-   PD = Dedicated to or marked as being in the public domain via one of our public domain tools, or other public domain work; adaptations of works in the public domain may be built upon and licensed by the creator under any license terms desired

Inoltre un collegamento URL al documento completo delle licenza (nel caso di licenze personalizzate)

### ISO 10303 

La ISO 10303 (STEP Standard for the Exchange of Product model data - \"Norme per lo Scambio dei dati dei Prodotti\") è molto importante in questo campo. È la unica definizione di struttura di prodotto che io conosca ben standardizzata e ampiamente discussa e riconosciuta. <img alt="" src=images/Product_structure_modeling_Process-Data_diagram.gif  style="width:500px;">


<div class="mw-translate-fuzzy">

Ecco alcuni link con utili informazioni:

-   [ISO 10303 in Wikipedia](http://http://it.wikipedia.org/wiki/ISO_10303)
-   [WikiStep.org](http://www.wikistep.org/index.php/Main_Page) con un sacco di informazioni di base ma soprattutto rivolte a STEP-NC
-   La [Struttura del prodotto](http://www.wikistep.org/index.php/Product_Basics) in STEP
-   Alcuni [esempi](http://www.wikistep.org/index.php/STEP_Tutorial) su STEP
-   [ISO 10303-11](http://en.wikipedia.org/wiki/ISO_10303-11) sul linguaggio di modellazione (EXPRESS)
-   [Un articolo di Wikipedia](http://en.wikipedia.org/wiki/Product_Structure_Modeling) sulla modellazione del prodotto
-   [Panoramica della Parte 41 - Fondamenti di Descrizione del prodotto e supporto](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part41)
-   [Panoramica della parte 44 (2a edizione) - Configurazione della struttura del prodotto](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part44)
-   [Esempi di piccoli file di AP 214](http://www.steptools.com/support/stdev_docs/express/ap214/index.html)


</div>

### Vincoli degli Assemblaggi 

Un ruolo importante nella costruzione di modelli e prodotti di grandi dimensioni viene svolto dai vincoli di assemblaggio, che impostano determinate regole su come assemblare le parti di un prodotto. Principalmente si tratta di Fix, FACEtoFACE, Angle, Offset e di alcuni modelli di istanze. Questi vincoli hanno bisogno di un solutore specializzato per essere conservarti quando le parti cambiano. Questo solutore è fondamentalmente diverso dal solutore di Schizzo (Sketch). Penso che per questo dobbiamo orientarci su un accesso basato sulla grafica \...

### Cinematica

Un passo ulteriore sarebbe quello di utilizzare [ODE](http://ode.org/), o librerie simili, per mettere insieme i vincoli delle parti e di assemblaggio per fare una simulazione di cinematica delle macchine. Ciò consentirebbe di controllare le collisioni e di esplorare le condizioni di un sistema meccanico.

### Controllo delle revisioni 

Un punto importante è il controllo di versione e di sviluppo distribuito. Con il disegno multi modello è possibile suddividere i progetti in piccole parti e si può distribuire il lavoro a una squadra. A uno sviluppatore di software \"distribuito\" e \"Versione\" suonano familiari, quindi perché non utilizzare un [DVCS](http://http://it.wikipedia.org/wiki/Controllo_di_versione_distribuito). Una buona comparazione di sistemi di controllo di versione distribuito si trova [qui](http://en.wikipedia.org/wiki/Comparison_of_revision_control_software#Technical_information).

Dal momento che abbiamo a che fare con dati grandi e dati che non possono essere facilmente differenziati, siamo limitati nella scelta a quelli che utilizzano il modello di cattura persistente (snapshot persistence model - un sistema che può memorizzare una copia dell\'albero prima e dopo il cambiamento). Qualsiasi sistema che archivi solo le diff (differenze tra le versioni) avrà gravi problemi con i nostri dati (testato personalmente con file Mercurial e Catia). Escludendo i sistemi commerciali e non-free, sostanzialmente restano solo [Git](http://en.wikipedia.org/wiki/Git_%28software%29) e [SVN](http://subversion.apache.org/).

Utilizzare Git per il lavoro presenta due grandi limiti:

-   Git è molto complicato: la ramificazione, la fusione e l\'etichettatura lungo un percorso di sviluppo non lineare. Già la sola fusione con i repository remoti (push, pull) creerà un sacco di complicazioni in materia. Nasconderlo all\'utente sarà un compito difficile.

-   Git consente gestori di Merge e Diff (fusione e differenze) per determinati tipi di file. Noi abbiamo bisogno di un gestore per .fcstd. Questo gestore deve esaminare due documenti di FreeCAD, mostrare e unire le differenze negli oggetti, le caratteristiche e i parametri. Neanche questo è facile.

Però usando Git potrebbero aprirsi un sacco di possibilità, neppure i sistemi PLM di classe alta si sognerebbero mai di \...

## Organizzazione

Ecco alcune attività di sviluppo necessarie per un progetto dignitoso di Assemblaggio/Prodotto:

### Infrastruttura

L\'assemblaggio richiederà alcune modifiche al sistema di base e al livello delle infrastrutture di FreeCAD.

#### Modelli multipli 

I Modelli Multipli (Multi-Model) sono stati pensati fin dall\'inizio della progettazione di FreeCAD. Per questo c\'è una interfaccia multi documento e possiamo caricare un numero illimitato di documenti. Ma dobbiamo migliorare in particolare il visualizzatore 3D per gestire e mostrare più di un documento nella sua vista (Part-Trees).

#### Parte-Alberi 

Dato che in Assemblaggio la composizione delle parti e dei sottoassiemi è il flusso di lavoro principale, devono essere implementati gli strumenti per impilare (raggruppare) le Parti in un albero. A differenza di un DocumentObjectGroup il gruppo di Assemblaggio deve gestire la visibilità e il posizionamento dei figli. Meglio farlo impilando ViewProvider uno sull\'altro. Per questo serve una sorta di interfaccia ClaimChildren() per i ViewProvider.

#### Interfacce unificate di Trascina/Rilascia/Copia/Incolla 

Una interfaccia che fornisca a ViewProvider e agli ambienti il completo controllo sulle operazioni di Drag / Drop / Copia / Incolla nella struttura ad albero o nella vista 3D.

#### Risorse esterne 

Gestione dei collegamenti drogati (doped links) (da browser interno o esterno). Significa caricare risorse su (potenziali) connessioni lente (HTTP).

*(ndt - in gergo, Doping Link: La pratica e gli effetti di incorporare un gran numero di collegamenti ipertestuali su un sito web in cambio di link di ritorno, spesso utilizzati per gonfiare la popolarità del sito.)*

### Materiali

Descrivere il materiale e le sue proprietà è una parte vitale di un sistema CAD/CAE. Il materiale ha un sacco di proprietà e nomi fortemente dipendenti dal settore di utilizzo. Ad esempio, FEM e Meccanica usano modi e standard differenti per descrivere il materiale.

Per la descrizione del materiale è stato scritto un articolo specifico: [Materiali](Material/it.md)

### Modello di oggetti 

E\' necessaria una classe albero per gestire i concetti. Riferimenti, interfacce, collegamenti a documenti, viste, composti, i vincoli, configurazioni, e molto altro \...

## Controlli su STEP 

Implementare un primo importatore STEP che oltre alla geometria e al colore permetta di controllare se il modello è valido anche sotto altri aspetti.

### Soluzionatore di vincoli di assemblaggio 

Definire una interfaccia per un risolutore dei vincoli di Assemblaggio molto simile all\'interfaccia del risolutore di Schizzo (Sketcher).

### Interfaccia di simulazione fisica 

Interfaccia per consentire a un (esterno) (multi) software di simulazione fisica di prendere il controllo del posizionamento delle Parti di un Assemblaggio. Ciò consentirebbe di utilizzare \"bullet\" o \"ODE\" per fare le prove cinematiche e [DMU](http://it.wikipedia.org/wiki/Digital_mock-up).

## Prossime azioni 

-   Modello di oggetti
-   \...

_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Assembly project/it
