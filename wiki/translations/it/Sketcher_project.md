


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Questo è il progetto di sviluppo dell\'ambiente Schizzo di FreeCAD.
Il progetto segue le regole del processo \[<http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology>\| Getting things done\] (metodo per l\'organizzazione delle proprie azioni, per la gestione del tempo e dei progetti per *fare in modo che le cose vengano fatte*).
I progetti sono raccolti nel [Piano di sviluppo](Development_roadmap/it.md) ([Development roadmap](Development_roadmap.md)).

## Finalità e principi {#finalità_e_principi}

Questo è un progetto di sviluppo del software che mira a implementare la funzionalità dei vincoli in Sketcher. Si tratta di implementare alcuni elementi GUI (dell\'interfaccia grafica) e di collegarli al solutore dei vincoli.

Le fasi dello sviluppo sono pianificate qui e sono monitorate nel sistema di gestione <http://www.freecadweb.org/tracker/my_view_page.php> per tenere un registro storico delle modifiche ben strutturato.

## Risultati

## Riflessioni

Al fine di migliorare le prestazioni del soluzionatore del disegnatore di schizzi, si può realizzare un partizionamento basato su un grafico del sistema dei vincoli. L\'insieme dei vincoli e l\'insieme dei parametri incogniti possono essere rappresentati in un [grafo bipartito](http://http://it.wikipedia.org/wiki/Grafo_bipartito) con i vincoli corrispondenti ai nodi di sinistra e le incognite corrispondenti ai nodi di destra.

Un semplice, ma spesso molto utile passo di preprocesso è quello di riconoscere eventuali sottogruppi disgiunti in modo che possano essere trattati separatamente nel risolutore.

Inoltre si può ridurre il numero dei parametri ignoti che vengono presi in considerazione nella soluzione. All\'inizio della soluzione si dovrebbe controllare che i vincoli non siano già soddisfatti. Con una analisi grafica si può trovare un set minimo di parametri sconosciuti che devono essere presi in considerazione per soddisfare tutti i vincoli insoddisfatti.

Facendo un passo in avanti, possono essere rilevate le sotto-parti rigide di un disegno e ridotte a 3 gradi di libertà (x, y, rotazione).

## Organizzazione

## Prossime Azioni {#prossime_azioni}

Per 0.14:

1\. Selezione multipla tramite trascinamento del mouse (selezione di un\'area)

2\. Lista delle Geometrie nella scheda azioni (analoga alla lista dei Vincoli)

3\. Aggiungere un\'opzione nel menu a comparsa per convertire un vincolo di punto coincidente in vincolo di tangenza

4\. Strumento Poligono (comodità)

5\. Aggiornare la documentazione del wiki per il vincolo di Simmetria e lo strumento Polilinea (azioni del tasto M)

Idee da sviluppare:

Interfaccia utente:

1\. Griglia su schermo intero (unità corrente)

2\. Auto-vincoli più efficiente:

2.a Algoritmo che consideri solo la geometria che è presente sullo schermo per aumentare le prestazioni e migliorare la selezione

2.b Prevenire i conflitti di vincoli

3\. Proposte per le linee: vincolo orizzontale, verticale, perpendicolare, tangente?

4\. Revisione delle icone dei vincoli fondendole in un unico Nodo

4.a Unirle in un unico SoNode per migliorare le prestazioni

4.b Remove need for ray pick to increase performance

4.c Condivisione più efficiente della memoria della trama.

4.d Migliorare l\'algoritmo per evitare le sovrapposizioni

4.e Barra degli strumenti per visualizzare i vincoli indipendente

5\. Migliorare le etichette dei dati:

5.a Etichetta di raggio posizionabile con qualsiasi angolo

5.b Eliminare ciò che non è più necessario per memorizzarlo in SoImage

6\. Impostare la griglia su un bordo

7\. Vincoli automatici durante il trascinamento (Punto su Punto, Punto su Linea, Coincidente)?

8\. Evidenziare delle entità o zoom di precisione su un\'area dello schizzo

9\. Associazioni a Progettazione Parti (oggetti trasparenti di supporto)

10\. Implementare la funzione Piano dello schizzo con l\'introduzione del Modulo Assemblaggio

11\. Migliorare la selezione del punto mediante l\'implementazione di nuovi nodi personalizzati.

12\. Costruzione con linee a tratti al posto di linee continue.

Per la versione 0.13:

1\. Supporto per arco/arco e arco/cerchio nel vincolo di tangenza - **FATTO** \[logari81\]

2\. Supporto per archi nel vincolo di perpendicolarità - **FATTO** \[logari81\]

3\. Frecce dello zoom indipendenti (vincolo di simmetria)/linee di quota - **FATTO** \[mrlukeparry\]

4\. Vincoli riferiti a una Geometria esterna - **FATTO** \[logari81\]

5\. Box di selezione - **FATTO** \[mrlukeparry\]

6\. Selezione multipla tramite trascinamento del mouse - **Rinviato alla 0.14**

7\. Migliorare la diagnostica dei vincoli [(Issue \#691)](http://www.freecadweb.org/tracker/view.php?id=691)- **FATTO** \[logari81\]

8\. Lista delle Geometrie nella scheda azioni (analoga alla lista dei vincoli) - **Rinviato alla 0.14**

9\. Supporto per i punti come geometria di costruzione - **FATTO** \[logari81\]

10\. Aggiungere un\'opzione del menu a comparsa per convertire un vincolo di punto coincidente in vincolo di tangenza - **Rinviato alla 0.14**

11\. fare si che il vincolo di simmetria lavori con i punti di simmetria invece delle linee di simmetria (utile, ad esempio, per definire il punto medio) - **FATTO** \[logari81\]

Per la versione 0.12:

1\. parametri dei vincoli (dati) modificabili nella vista 3D **FATTO** \[jriegel\]

2\. sincronizzazione tra elenco di widget di selezione della vista - selezione della vista 3D - **FATTO** \[wmayer\]

3\. evitare la sovrapposizione dei simboli di vincoli **FATTO** - \[mrlukeparry\]

3a. rendere i simboli dei vincoli più piccoli, selezionabili ed evitare la sovrapposizione durante l\'ingrandimento **FATTO** - \[mrlukeparry\]

3b. creare icone di vincoli per la vista di Inventor 3D **FATTO** - \[mrlukeparry\]

3c. rendere le dimensioni dei testi dei dati dependenti dallo zoom \[mrlukeparry\] **FATTO** - \[mrlukeparry\]

3d. rendere il testo dei dati più semplice da selezionare **FATTO** - \[mrlukeparry\]

3e. evitare la sovrapposizione di testo su etichette di dati **FATTO** - \[mrlukeparry\]

4\. testare il nuovo risolutore in modalità autonoma

5\. vincoli esterni (avendo vincoli con riferimenti al di fuori del disegno, ad esempio, alcuni bordi del modello 3D) **0.13** \[jriegel\]

6\. vincoli automatici **FATTO** \[jriegel\]

6a. auto-vincolo per perpendicolarità **FATTO** - \[mrlukeparry\]

7\. visualizzare i vincoli di tangenza **FATTO** - \[mrlukeparry\]

8\. visualizzare i vincoli di distanza da punto a linea e da punto a punto **FATTO** - \[logari81\]

9\. aggiungere gli indici ai simboli vincoli in vista 3D per distinguerli tra i vincoli dello stesso tipo **FATTO** - \[mrlukeparry\]

10\. vincolo di raggio (compresa la visualizzazione) **FATTO** - \[logari81\]

11\. vincolo di angolo (compresa la visualizzazione) **FATTO** - \[logari81\]

12\. implementare uno strumento raccordo in Sketcher **FATTO** \[mrlukeparry\]

12a. fornire un metodo di impostazione del raggio del raccordo [(Issue \#437)](http://www.freecadweb.org/tracker/view.php?id=437)

13\. implementare un strumento Riduci/Estendi in Sketcher **FATTO** - \[logari81\]

13a. implementare uno strumento Estendi **TRALASCIATO** \[logari81\]

13b. supporto per gli archi nello strumento tagliare **FATTO** - \[mrlukeparry\]

14\. vincolo lunghezze uguali (compresa la visualizzazione) **FATTO** - \[logari81\]

15\. diagnostica dei vincoli - conteggio del grado di libertà **FATTO** \[logari81\]

16\. vincolo di simmetria (compresa la visualizzazione) **FATTO** - \[logari81\]

17\. implementare il vincolo di punto su oggetto **FATTO** - \[mrlukeparry\]

18\. rendere gli agganci alla griglia (Snap-Grid) meno \'avidi\' **FATTO** - \[mrlukeparry\]

19\. Pagina Wiki per l\'ambiente di Schizzo (Workbench Sketcher) **FATTO** - \[normandc\]


{{Sketcher Tools navi

}}  

[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
