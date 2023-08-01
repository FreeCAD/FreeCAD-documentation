# Source documentation/it
## Panoramica

Il codice sorgente di FreeCAD è commentato per consentire la generazione automatica della documentazione di programmazione utilizzando [Doxygen](Doxygen/it.md), un popolare sistema di documentazione del codice sorgente. Doxygen può documentare entrambe le parti C++ e Python di FreeCAD, ottenendo pagine HTML con collegamenti ipertestuali a ciascuna funzione e classe documentata.

La documentazione è online sul [sito web dell\'API di FreeCAD](https://freecad.github.io/SourceDoc/). Si prega di notare che questa documentazione potrebbe non essere sempre aggiornata; se c\'è bisogno di maggiori dettagli, scaricare l\'ultimo codice sorgente di FreeCAD e compilare da sé la documentazione. Se ci sono domande urgenti sul codice, chiedere nella sezione sviluppatori del [Forum di FreeCAD](https://forum.freecadweb.org/index.php).

La compilazione della documentazione dell\'API segue gli stessi passaggi generali della compilazione dell\'eseguibile di FreeCAD, come indicato nella pagina [Compilazione in Linux](Compile_on_Linux/it.md).

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*Flusso di lavoro generale per compilare la documentazione di programmazione di FreeCAD. I pacchetti Doxygen e Graphviz devono essere nel sistema, così come il codice sorgente di FreeCAD stesso. CMake configura il sistema in modo che con una singola istruzione make la documentazione per l'intero progetto venga compilata nei vari file HTML con i diagrammi.*



## Costruire la documentazione del codice sorgente 



### Documentazione completa 

Se c\'è installato Doxygen, è molto facile costruire la documentazione. Installare anche [Graphviz](https://www.graphviz.org/) per poter produrre diagrammi che mostrino le relazioni tra le diverse classi e le librerie nel codice di FreeCAD. Graphviz è utilizzato anche dal [grafico delle dipendenze](Std_DependencyGraph/it.md) di FreeCAD per mostrare le relazioni tra i diversi oggetti. 
```python
sudo apt install doxygen graphviz
```

Quindi seguire gli stessi passi che si farebbero per compilare FreeCAD, come descritto nella pagina [Compilazione in Linux](Compile_on_Linux/it.md), e riassunti qui di seguito per comodità.

-   Prendere il codice sorgente di FreeCAD e metterlo nella sua directory `freecad-source`.
-   Creare un\'altra directory `freecad-build` in cui si compilerà FreeCAD e la sua documentazione.
-   Configurare i sorgenti con `cmake`, assicurandosi di indicare la directory dei sorgenti, e specificare le opzioni richieste per la build.
-   Attivare la creazione della documentazione usando `make`.


```python
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

Mentre ci si trova all\'interno della directory di build, dare le seguenti istruzioni per creare solo la documentazione. 
```python
make -j$(nproc --ignore=2) DevDoc
``` Come accennato in [velocizzare la compilazione](Compiling_(Speeding_up)/it.md), l\'opzione `-j` imposta il numero di core della CPU utilizzati per la compilazione. I file di documentazione risultanti verranno visualizzati nella directory 
```python
freecad-build/doc/SourceDocu/html/
```

Il punto di accesso alla documentazione è il file `index.html`, che si può aprire con un browser web: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```

Il target `DevDoc` genererà una notevole quantità di dati, circa 5 GB di nuovi file, in particolare grazie ai diagrammi creati da Graphviz.



### Documentazione sintetica 

La documentazione completa utilizza circa 3 GB di spazio su disco. Una versione alternativa e più piccola della documentazione che richiede solo circa 600 MB può essere generata con una destinazione diversa. Questa è la versione visualizzata sul [sito web dell\'API di FreeCAD](https://freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

La documentazione sul [sito Web dell\'API di FreeCAD](https://freecad.github.io/SourceDoc/) viene prodotta automaticamente da <https://github.com/FreeCAD/SourceDoc>. Chiunque può ricostruirla e inviare una richiesta di pull:

-   Effettuare il fork del repository su <https://github.com/FreeCAD/SourceDoc>
-   sulla tua macchina: clonare il codice FreeCAD (se non è gia stato fatto), creare una build dir per il documento e clonare il suddetto repository SourceDoc all\'interno. Quel SourceDoc verrà aggiornato quando si ricostruisce il documento e si sarà in grado di eseguire il commit ed inviare i risultati in seguito:


```python
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD
mkdir build
cd build
mkdir -p doc/SourceDocu/html
cd doc/SourceDocu/html
git clone your-fork-url
cd ../../..
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make WebDoc
cd doc/SourceDocu/html
git commit
git push
```

-   Andare al fork online e creare una richiesta di pull.

## Altre versioni 

[FreeCAD 0.19 development](https://iesensor.com/FreeCADDoc/0.19/) documentazione creata da [qingfeng.xia](http://forum.freecadweb.org/viewtopic.php?t=12613).



## Integrare la documentazione di Coin3D 

Sui sistemi Unix, è possibile collegare la documentazione del codice sorgente di Coin3D con quella di FreeCAD. Questo consente una navigazione più agevole e diagrammi di ereditarietà completi per le classi derivate da Coin.

-   Installare il pacchetto `libcoin-doc`, `libcoin80-doc` o con nome simile.
-   Scompattare l\'archivio `coin.tar.gz` che si trova in `/usr/share/doc/libcoin-doc/html`; i file potrebbero essere già decompressi nel sistema.
-   Generare nuovamente la documentazione di origine.

Se non si installa il pacchetto di documentazione per Coin, verranno generati i collegamenti per accedere alla documentazione online su [BitBucket](https://coin3d.bitbucket.io/Coin/). Ciò accadrà se un file di tag Doxygen può essere scaricato al momento della configurazione con `wget`.



## Usare Doxygen 

Vedere la pagina [Doxygen](Doxygen/it.md) per un\'ampia spiegazione su come commentare il codice sorgente C++ e Python in modo che possa essere elaborato da Doxygen per creare automaticamente la documentazione.

Essenzialmente, un blocco di commento, che inizia con `/**` o `///` per C++, o `##` per Python, deve apparire prima di ogni classe o funzione definizione, in modo che venga raccolto da Doxygen. Molti [comandi speciali](Doxygen#Doxygen_markup.md), che iniziano con `\` o `@`, possono essere usati per definire parti del codice e formattare l\'output. La [Sintassi di Markdown](Doxygen#Supporto_Markdown.md) funziona anche all\'interno del blocco dei commenti, il che può essere utile per enfatizzare alcune parti della documentazione. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/it
