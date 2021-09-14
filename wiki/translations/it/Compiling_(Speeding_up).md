# Compiling (Speeding up)/it




<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Presentazione

FreeCAD è una grande applicazione che può richiedere da 10 minuti a un\'ora per essere compilata completamente dal sorgente. Ciò dipende principalmente dalla CPU in uso e dal numero di core utilizzati nel processo di compilazione. Ecco alcuni suggerimenti per abbreviare tale processo e ridurre i tempi di costruzione.

### CCache

Installare `ccache` per la costruzione cache

### Disabilitare i moduli 

Quando si utilizza `cmake` per configurare la build, è possibile disabilitare la compilazione di alcuni ambienti che al momento potrebbero non essere necessari. Questo è utile se si vuole solo testare alcuni ambienti di lavoro.

Ad esempio, per evitare di costruire i banchi di lavoro FEM e Mesh:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Utilizzare `cmake-gui`, `cmake-curses-gui` o `cmake-qt-gui` per visualizzare tutte le possibili variabili che possono essere modificate nella configurazione; utilizzando queste interfacce è possibile attivare o disattivare facilmente diversi banchi di lavoro.

### Numero di lavori in parallelo 

Dopo la configurazione fatta con `cmake`, il programma `make` avvia il compilatore C++ effettivo per lavorare sui file del codice sorgente. Si può velocizzare la compilazione lavorando su vari file contemporaneamente. Ciò si ottiene con l\'opzione `-j` di `make`, che indica il numero di \"lavori\" o comandi di compilazione eseguiti contemporaneamente. Questa opzione è un numero intero.

Esegui quattro comandi di compilazione in parallelo:


```python
make -j4
```

Compilare contemporaneamente più file quanti sono i core della CPU nel sistema. Questo è utile se hai molti core e vuoi usarli tutti per compilare il software.


{{code|code=
make -j$(nproc)
}}

Compilare contemporaneamente più file quanti sono i core della CPU nel sistema, meno due. Usa questo in modo che il tuo sistema sia ancora pronto a svolgere qualche altra attività; ad esempio, due core ti permetteranno di usare un browser, mentre il resto dei core continuerà a compilare il software in background.


{{code|code=
make -j$(nproc --ignore=2)
}}

### distcc

Il programma `distcc` può essere utilizzato per eseguire compilazioni distribuite di codice C e C++ su più macchine in una rete.


<div class="mw-translate-fuzzy">





</div>




[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md)
