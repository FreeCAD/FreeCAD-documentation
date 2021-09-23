# The FreeCAD source code/it
 Il [codice sorgente di FreeCAD](https://github.com/FreeCAD/FreeCAD) è gestito con git, ed è pubblico, aperto e disponibile sotto la [licenza LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License). Esso può essere copiato, scaricato, letto, analizzato, ridistribuito e modificato da chiunque. Se avete intenzione di apportare delle modifiche che desiderate vedere incluse nel codice ufficiale, ricordate che le modifiche devono essere approvate dagli sviluppatori di FreeCAD, quindi è saggio discutere prima le proprie intenzioni e idee nel [forum](http://forum.freecadweb.org), per non rischiare che le modifiche vengano poi respinte a causa di qualche motivo imprevisto.

Se siete interessati a esplorare il codice FreeCAD, qui di seguito ci sono alcuni suggerimenti e informazioni utili per fornire una traccia .

-   Il codice di FreeCAD è programmato principalmente in **C++**, ma si basa pesantemente su **Python**. Una grande parte delle sue funzionalità fornisce un legame di associazione a Python, e offrire sempre un accesso con python per qualsiasi nuova caratteristica implementata in C++ fa parte della filosofia di base dello sviluppo di FreeCAD. Per ottenere questo, in tutto FreeCAD sono abbondantemente utilizzati CPython (gli strumenti di interfacciamento con C forniti da Python stesso) e specialmente [PyCXX](http://cxx.sourceforge.net/). Nel stesso codice di FreeCAD sono forniti anche molti modelli e strumenti personalizzati per rendere molto facile la costruzione dei legami di associazione a python. Alcune parti del codice di alto livello di FreeCAD sono codificate completamente in Python.


<div class="mw-translate-fuzzy">

-   Il codice sorgente di FreeCAD è completamente **multi-piattaforma**, ed è stata messa molta attenzione per consentire che l\'applicazione sia utilizzabile sul maggior numero possibile di piattaforme e configurazioni, e per non mettere gli attuali utenti in situazioni difficili. Pertanto le nuove versioni dei componenti necessari sono rinviate, quanto più possibile, finchè non sono completamente e facilmente disponibili per tutte le piattaforme, e anche la compatibilità (la possibilità di aprire su una nuova versione di FreeCAD un file prodotto con una versione precedente) è considerata un importante priorità.


</div>

-   Quasi tutte le funzionalità di FreeCAD sono divise in due parti distinte, chiamate **App** e **Gui**. Questa separazione si riflette ovunque nella struttura dei file del codice sorgente. La parte App contiene tutte le funzionalità che devono essere eseguite in pura modalità console (senza interfaccia grafica). Dato che FreeCAD può essere compilato ed eseguito senza la sua interfaccia grafica, il codice in App è indipendente da qualsiasi libreria correlata alla GUI. La parte Gui contiene tutto il codice necessario per l\'esecuzione in modalità GUI, ed è costruita attorno alle funzionalità App.


<div class="mw-translate-fuzzy">

-   La maggior parte delle funzionalità di FreeCAD è implementata sotto forma **Moduli**. Senza il sui moduli FreeCAD è una semplice finestra contenitore che può solo aprire e salvare un file. Tutti gli strumenti della geometria e gli ambienti di lavoro sono implementati in moduli. I moduli possono essere scritti in C++, in Python, o con le migliori combinazioni dei due, possono essere moduli ibridi C++ / Python, in cui i solidi, le funzionalità di base sono programmate in C++ mentre gli strumenti per l\'utente finale sono realizzati in Python e sono quindi molto più facile da estendere e adattare dagli utenti FreeCAD. Ogni modulo di solito definisce e crea un **Workbench** nell\'interfaccia FreeCAD, se usato in modalità GUI, di solito con lo stesso nome, ma non è obbligatorio che i moduli contengano un ambiente di lavoro.


</div>


<div class="mw-translate-fuzzy">

-   I moduli di FreeCAD spesso **dipendono da altri moduli**. La maggior parte dei moduli che utilizzano la geometria solida dipendono dal modulo **Part**, che è il modulo fondamentale di FreeCAD, e che implementa la maggior parte dell\'interfaccia con OpenCasCade. Comunque anche altri moduli possono utilizzare direttamente le funzionalità di OpenCasCade, che spesso si basano sulle funzioni di alto livello fornite da Part.


</div>

-   I moduli sono sempre **inizializzati** da Python. Anche se sono scritti interamente in C++, essi contengono sempre un minimo di struttura Python / CPython.


<div class="mw-translate-fuzzy">

-   FreeCAD è un avido utente di **altre librerie open-source**. Oltre a Python e Qt, utilizzati dal core e da quasi tutti i moduli, le due librerie fortemente utilizzate dalla maggior parte dei moduli sono [OpenCasCade Technology](https://en.wikipedia.org/wiki/Open_Cascade_Technology) e [Coin3D](http://www.coin3d.org/). OpenCasCade viene utilizzato per creare e per gestire tutta la geometria solida di FreeCAD, mentre coin3D viene utilizzato per gestire la visualizzazione 3D. OpenCascade è utilizzato principalmente nella parte App, e coin3D esclusivamente nella parte Gui. Con FreeCAD, per fare qualsiasi lavoro legato alla geometria, è fondamentale una conoscenza di base di OpenCasCade. Diversi moduli specifici fanno uso di diverse specifiche librerie, e dato che di solito non ci sono restrizioni su questo punto, salvo che le librerie siano facilmente disponibili per tutte le piattaforme, in una installazione completa di FreeCAD con tutti i suoi moduli, l\'elenco delle dipendenze può essere molto lungo.


</div>


<div class="mw-translate-fuzzy">

-   I **document objects** (gli oggetti del documento) di FreeCAD, che sono tutti gli oggetti contenuti in un documento di FreeCAD, sono quelli che appaiono nella Struttura ad albero nella GUI e in FreeCAD.ActiveDocument.Objects() in Python. Essi possono avere o non avere tutti i dati geometrici, e possono mostrare qualcosa o non mostrare nulla nella Vista 3D. Essi sono sempre divisi nelle parti App e Gui. Durante l\'esecuzione in modalità console la parte Gui non viene caricata. Gli oggetti geometrici standard, come quelle che si trovano in Parte o PartDesign, hanno la loro geometria basata su OpenCasCade definita nella loro controparte App, mentre la controparte Gui (anche di solito chiamato \"View Provider\") è responsabile della creazione di una rappresentazione coin3D di tale geometria, che viene inserita nella scena grafica principale della vista 3D di coin3D.


</div>

-   La struttura di base del codice sorgente è organizzata in questo modo:
    -   **App**: contiene l\'applicazione FreeCAD in modalità console, definisce le strutture di base e le classi di base per gli oggetti del documento, che vengono utilizzate dai moduli per costruire i propri oggetti.
    -   **Base**: contiene le funzionalità di base comunemente utilizzate da tutto FreeCAD: vettori 3D, unità, matrici, posizionamento, ecc
    -   **Gui**: contiene l\'applicazione FreeCAD in modalità GUI, definisce la vista 3D, contiene molti strumenti e funzioni che sono utilizzate dagli ambienti di lavoro per interagire con l\'interfaccia e con la vista 3D, definisce le classi di base per i gestori della vista.
    -   **Doc**: contiene principalmente un file di aiuto all-in-one di Qt generato da questo wiki.
    -   **Mod**: contiene tutti i moduli, anche essi divisi in App e Gui (fatta eccezione per i moduli Python, che non sempre seguono così chiaramente questa regola).


<div class="mw-translate-fuzzy">

### Approfondimenti

-   [Gestione del codice sorgente](Source_code_management/it.md)
-   La sezione per [Utenti avanzati](Power_users_hub/it.md) contiene molta documentazione sui moduli, OpenCasCade e Coin3D, principalmente per la programmazione in Python. Comunque, poiché la funzionalità è simile, queste pagine sono interessanti anche per il programmatore C++.


</div>

[Category:Developer Documentation](Category:Developer_Documentation.md)
