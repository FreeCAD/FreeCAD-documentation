# Release notes 0.11/it
# Note di rilascio della versione 0.11 

Questo è un riassunto dei cambiamenti più importanti e delle nuove funzionalità disponibili nella versione 0.11 di FreeCAD. L\'elenco completo si trova [qui](http://www.freecadweb.org/tracker/changelog_page.php).

<img alt="" src=images/FreeCAD011.png  style="width:800px;">

Una schermata della versione 0.11

\_\_\_TOC\_\_\_

### Generale

-   Il [progetto di traduzione di FreeCAD](http://crowdin.net/project/freecad) ha ricevuto un grande aiuto da molte persone in tutto il mondo e FreeCAD ora è fornito con almeno 15 lingue: inglese, tedesco, francese, italiano, svedese, spagnolo, portoghese, russo, ucraino, norvegese, afrikaans, finlandese, cinese semplificato, croato e olandese. Per i prossimi rilasci si sta lavorando con molte altre lingue.

![](images/release011-translation.jpg )

-   Sono stati apportati diversi miglioramenti in tutto FreeCAD, ad esempio la struttura gerarchica ora permette di assemblare oggetti complessi, mantenendo tutto lo storico della geometria pulito, facilmente accessibile e modificabile. Nuovi miglioramenti anche alle API di Python permettono di interagire meglio con gli oggetti tramite l\'albero, definendo il loro comportamento, icone, ecc.

![](images/release011-dependency.jpg )

-   Il meccanismo di copia/incolla è stato molto migliorato, ora permette un facile copia/incolla di oggetti tra i documenti.
-   Il [ Part Workbench](Part_Workbench/it.md) (Ambiente Parte) presenta nuovi strumenti quali la simmetria, il raccordo e lo smusso.

### Schizzo e Disegno di Parti 

-   Il solutore dei vincoli del [ Modulo di Schizzo](Sketcher_Workbench/it.md) è stato completamente riscritto e l\'ambiente di Schizzo dispone già di una vasta buona dotazione di strumenti, anche se non ancora completa, quali linee, rettangoli e di vincoli quali punto di coincidenza, parallelismo, lunghezza fissa e vincoli orizzontali o verticali.

-   In aggiunta a Schizzo, ora un nuovo ambiente di lavoro, l\'ambiente Parte, consente di creare rapidamente solidi partendo da schizzi. Ora come regola in FreeCAD, dato che tutto è parametrico, si può tornare indietro in qualsiasi momento per modificare il disegno, e tutta la geometria che dipende da esso si adatterà automaticamente.

![](images/release011-sketcher.jpg )

![](images/Movie.png ) Esempi: [Demo di Schizzo](http://www.youtube.com/watch?v=hvXupH5bA0E) • [Demo del modulo Parte](http://www.youtube.com/watch?v=7ih9Jp3OAwA)

### Simulazione di movimenti di Robot 

-   Il [ Modulo Robot](Robot_Workbench/it.md) è stato esteso con molti strumenti GUI ed ora è abbastanza funzionale e permette di simulare facilmente i movimenti dei robot industriali.

![](images/release011-robot.jpg )

### Disegno 2D - Drafting 

-   Gli agganci (snap) sono stati ottimizzati ed ora funzionano abbastanza velocemente anche su oggetti complessi
-   Lo strumento \"Accorcia/Estendi\" può ora essere chiamato \"Accorcia/Estendi/Estrudi\", in quanto permette di estrudere rapidamente singole facce, che offre una comoda scorciatoia per lo strumento di Estrusione standard di Parte
-   La gestione dei fogli nell processo di produzione delle Proiezione di oggetti Draft (proiezioni in 2D di oggetti 3D) è anche stata migliorata. Ora tutti gli oggetti dell\'ambiente Draft possono essere collocati in una pagina di disegno, e tutti hanno la stessa praticità di gestione degli oggetti standard dell\'ambiente Parte, offrendo la possibilità di cambiare la loro posizione, la rotazione e la scalatura dinamica. Essi offrono anche alcune funzioni extra, come il riempimento con il tratteggio.

![](images/release011-draft-drawing.jpg )

-   Il modulo Draft offre anche nuovi strumenti, quali poligoni regolari e bSplines
-   C\'è anche un nuovo strumento Modifica che permette di modificare la geometria della maggior parte degli oggetti Draft

![](images/release011-draft.jpg )

-   Le quote ora hanno il loro testo modificabile e spostabile, e i segmenti possono avere una freccia finale, cosa che permette di usarli come linee guida
-   Diversi comandi quali sposta, ruota o dimensiona ora possono essere replicati senza uscire dallo strumento
-   Il modulo Draft inoltre incorpora una [API in Python](Draft_API/it.md).
-   L\'importatore DXF ora supporta gli attributi di blocco

![](images/Movie.png ) Esempi: [Draft module demo](http://www.youtube.com/watch?v=Q7cG-LQK8Ps)

### Immagini

-   L\'ambiente Immagine ora dispone di un oggetto ImagePlane che permette di visualizzare un file di immagine all\'interno della scena 3D, questo può essere utilizzato ad esempio per costruire la geometria su modelli acquisiti da scanner

### Documentazione

-   Diverse traduzioni del [manuale di FreeCAD](Online_Help_Toc/it.md) ora sono a buon punto. Controllare nella pagina principale!


{{languages/it | {{en|Release_notes_0.11}} {{de|Release_notes_0.11/de}} {{es|Release_notes_0.11/es}} {{fr|Release_notes_0.11/fr}} {{pl|Release_notes_0.11/pl}} {{ru|Release_notes_0.11/ru}} }}



---
![](images/Button_right.svg) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.11/it
