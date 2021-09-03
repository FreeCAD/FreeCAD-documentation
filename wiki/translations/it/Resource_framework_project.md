


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Questo è il piano del progetto per la struttura delle risorse di FreeCAD come parte del [Piano di sviluppo](Development_roadmap/it.md).

## Finalità e principi {#finalità_e_principi}

E\' un progetto di sviluppo del software finalizzato a implementare il [Product Data Management (PDM)](http://it.wikipedia.org/wiki/Product_Data_Management) (Gestore dei Dati di Prodotto). Si tratta di implementare le parti e i componenti necessari.

Le fasi dello sviluppo sono pianificate qui e sono monitorate nel sistema di gestione delle versioni per tenere un registro storico delle modifiche ben strutturato: <http://www.freecadweb.org/tracker/change_log.php>

## Risultati

-   Controllo di revisione per progetti con grandi disegni.
-   Condividere il lavoro con altri tramite internet/intranet: **Collaborazione**
-   Cataloghi online e offline di [parti standard](http://en.wikipedia.org/wiki/Interchangeable_parts).

## Riflessioni

### Cosa fanno gli altri {#cosa_fanno_gli_altri}

Ecco alcuni link su analoghi prodotti commerciali:

-   [PDMLink](http://www.ptc.com/product/windchill/pdmlink) di PTC - \'\' \"\...quando tutte le parti coinvolte nel prodotto accedono ad un unico repository dati centrale affidabile i produttori hanno la possibilità di gestire in modo efficiente tutti i tipi di dati digitali relativi allo sviluppo del prodotto, tra cui quelli meccanici, elettrici e software. Windchill PDMLink è la soluzione ideale. Basato su Web per un facile accesso a livello aziendale, questo collaudato sistema di gestione dei dati di prodotto (PDM) supporta team dislocati in aree geografiche diverse consentendo di gestire processi critici come la gestione delle modifiche e della configurazione e la progettazione dettagliata.\" \'\'
-   Aras Corp. [Aras PLM Software](http://www.aras.com/) - Essi sembrano offrire soluzioni Open Source, può valer la pena di indagare ulteriormente \...
-   [Catia V6](http://www.3ds.com/de/products/plm-v6/v6r2009x/#vid1)

### Casi d\'uso {#casi_duso}

*Fornito da Charles:*

Naturalmente ci saranno diversi tipi di persone che utilizzeranno questo software, per diversi motivi, e che potrebbero forse avere bisogno di diverse soluzioni PDM, ma sarebbe bene studiare soluzioni che possano essere universali. Io vedo i seguenti metodi diversi di sviluppo (possono anche essercene altri):

-   Utenti singoli - probabilmente c\'è una percentuale significativa di persone che lavorano in questo modo e che possono essere abbastanza autosufficiente, ma il controllo di revisione e le ramificazione sono comunque utili. Molte di queste persone possono lavorare in parti del mondo dove l\'accesso a Internet è precario o costoso, per cui magari lavorano non in linea per lunghi periodi. Sarebbe bello rendere questi progetti individuali replicabili molto facilmente da altre persone, quando si tratta di un lavori validi, in modo che il progetto possa essere sviluppato in più direzioni contemporaneamente - molte evoluzioni darwiniane in molteplici direzioni contempopraneamente

-   Piccoli gruppi di persone che lavorano insieme (forse da parte della stessa istituzione di educazione), ma dove ogni individuo ha la libertà di esplorare tutti gli aspetti del progetto piuttosto che avere assegnata rigidamente una parte specifica del progetto. In genere, trovo che permette più opzioni se può essere esplorato facilmente e offre una maggiore flessibilità.

-   Progetti più ampi di disegno open-source - più membri e dispersi geograficamente. La direzione verso cui vanno i progetti software open-source - dove sembra esserci una tendenza generale verso i sistemi distribuiti (infatti Python si è [spostato](http://mail.python.org/pipermail/python-dev/2009-March/087931.html) recentemente su un DVCS). Vedo la progettazione e l\'ingegneria andare nella stessa direzione per le stesse ragioni. Quindi credo che ci sia un motivo in più per noi per riflettere su come un sistema distribuito potrebbe lavorare in CAD ​​- e se risolveremo questo avremo un grande vantaggio rispetto alle applicazioni di CAD commerciali! Sono convinto che esiste una soluzione, e se non la scopriamo noi, lo farà qualche altro sviluppatore di sistemi CAD!

-   Progetto con una gerarchia più rigida - ci possono essere alcuni progetti in cui i gruppi di lavoro preferiscono questa soluzione, ma penso che questo sistema possa essere popolare solo all\'interno delle imprese.

#### Il sito Web di Blendswap {#il_sito_web_di_blendswap}

[Blendswap](http://www.blendswap.com/) - secondo le sue stesse parole - è \'\' \"\... il luogo dove trovare e condividere i file di Blender con il mondo intero. Tu crei straordinari file di Blender, li condividi nel più grande archivio di modelli 3D open source realizzati con la straordinaria suite Open Source Blender 3D.\" \'\'

[Blender](http://www.blender.org/) è una \'suite di creazione di contenuto 3D\' in codice aperto molto popolare.

Pur non essendo un programma CAD, ci sono molte analogie che devono essere colte e insegnamenti da apprendere dal modo in cui Blender e la sua comunità stà facendo le cose.

Blendswap è un esempio eccellente di un repositorio (archivio) **online**. Le sue caratteristiche fondamentali che credo possiamo imparare sono:

-   Fornisce immagini in miniatura dettagliate sul sito web. Questo permette alle persone di navigare liberamente e trovare velocemente i contenuti.

-   I modelli (file di Blender) arrivano con la licenza chiaramente dettagliata (questi dettagli si possono anche visualizzare velocemente, sono visibili nella miniatura, per mezzo di un logo Creative Commons).

### Possibili sistemi di controllo di revisione {#possibili_sistemi_di_controllo_di_revisione}

E\' solo un piccolo passo per pensare al controllo di revisione nello stesso modo in cui viene utilizzato nello sviluppo del software moderno. Ci sono fondamentalmente due diversi approcci a tale questione:

-   Strutturato, server centralizzato ([Subversion](http://subversion.tigris.org/) o [CVS](http://www.nongnu.org/cvs/))
-   Strutturato, distribuito ([Mercurial](http://www.selenic.com/mercurial/wiki/), [Bazaar](http://bazaar-vcs.org/) e [Git](http://git-scm.com/))

Anche se i \'Casi d\'uso\' richiedono un sistema di controllo di revisione distribuito, questo sistema ha un grande inconveniente. Quando si clona un repositorio tutte le versioni precedenti vengono replicate nel proprio computer. Nel caso di dati CAD, questo può significare una quantità di Mb molto grande. Al contrario di quanto fanno i sistemi dei server centralizzati che scaricano solo la revisione principale e quindi trasferiscono delle quantità di dati relativamente piccole.

### Licenza

In un progetto distribuito in internet è necessario che ogni documento riporti una licenza chiara. Questo è ancora più importante quando riguarda i cataloghi. Le Parti del Catalogo sono utilizzate in progetti (liberi e non liberi) e quindi c\'è bisogno di una licenza chiara per rendere chiaro il loro utilizzo. Dato che esistono diversi sistemi di licenza, consideriamo qui una serie di possibili licenze per i file di CAD:

#### Creative Commons {#creative_commons}

Le licenze CC sono molto popolari per il materiale creativo, è possibile trovarne la descrizione qui: <http://creativecommons.org>

#### ISO 16016 {#iso_16016}

fraganaut01 ci indica un altro sistema di licenze per CAD:

-   Copyright by Provider (no more restrictions)
-   Riferito all\'avviso di protezione ISO16016 (nessuna restrizione speciale)
-   Confidenziale, solo per uso interno. Usare solo con obbligo di riservatezza. Fare riferimento all\'avviso di protezione ISO16016
-   Confidenziale, solo per uso interno. Fare riferimento all\'avviso di protezione ISO16016
-   Qualsiasi diffusione solo con l\'approvazione esplicita dell\'autore

### Disegno

Tutti i dati di revisione controllati, i cataloghi, le esercitazioni e così via, devono avere un qualche tipo di rappresentazione in FreeCAD. Tutto questo può essere riassunto sotto il nome **Risorsa**. Ci deve essere una classe di disegno che contenga questo tipo di informazioni sulle risorse e distingua i diversi casi.

### Architettura

Questa classe di servizio è per definizione, non solo locale alla macchina dell\'utente. E\' basata su [Nuvola](http://it.wikipedia.org/wiki/Cloud_computing) e implementata con diversi servizi su server diversi. Si devono distinguere quattro tipi di server:

-   Server economici - [LAMP](http://it.wikipedia.org/wiki/LAMP_(software_bundle))
-   Server completi (ad esempio server Ubuntu/Debian)
-   Server di download - ad esempio sf.net
-   [BitTorrent](http://it.wikipedia.org/wiki/BitTorrent_(protocol)) gestore di tracce

Questo ci porta al seguente scenario:

<img alt="" src=images/ResourceFramework.png  style="width:1000px;">

## Organizzazione

### Indagine

Innanzitutto devono essere testate le diverse alternative di sistemi di controllo di revisione. Per avere elementi concreti su come si comportano con dati di CAD.

### Disegno {#disegno_1}

Una classe di disegno per la struttura delle risorse.

## Azioni successive {#azioni_successive}

-   Costruire i repository di prova sul server e su due macchine locali
-   Provare i diversi casi d\'uso



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
