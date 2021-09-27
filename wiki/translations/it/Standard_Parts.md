# Standard Parts/it
Cosa sono (da fare)

\_\_TOC\_\_

## Le librerie di Parti Standard per FreeCAD 

Attualmente sono disponibili due librerie di parti predisegnate che possono essere inserite automaticamente nel progetto in corso:

-   **BOLTS**
    -   [Sito Web di BOLTS](http://www.bolts-library.org)
    -   [Macro BOLTS](http://www.freecadweb.org/wiki/index.php?title=Macro_BOLTS/it)
-   **FreeCAD Library**
    -   [Sito Web di FreeCAD Library](https://github.com/yorikvanhavre/FreeCAD-library)
    -   [Macro FreeCAD Library](http://www.freecadweb.org/wiki/index.php?title=Macro_PartsLibrary/it)

Viti e bulloni possono anche essere creati agevolmente con:

-   [Macro Screw maker 1 vers 2](http://www.freecadweb.org/wiki/index.php?title=Macro_screw_maker1_2/it). È disponibile anche [Macro Screw maker 1 vers 6](http://forum.freecadweb.org/viewtopic.php?f=22&t=6088#p48519) scaricabile solo dal Forum per motivi di dimensioni del file.

Le varie Macro possono anche essere usate in combinazione tra di loro, importando nello stesso documento parti di diverse librerie. Eventuali *Assemblaggi* possono essere archiviati nella FreeCAD Library.

## BOLTS

Al momento BOLTS offre una raccolta di parti standard principalmente di carattere meccanico, bulloni, dadi, rondelle, etc\..., ma non solo . Sostanzialmente si tratta di una macro che consente di esplorare il catalogo delle parti e di inserirle nel documento di FreeCAD. Vedere anche la pagina: _.

Le istruzioni per l\'installazione e l\'uso di BOLTS si trovano sul suo [sito Web](http://www.bolts-library.org) da cui sono ricavate queste informazioni.

Esempio di parti prelevate da BOLTS e inserite in un documento di FreeCAD:

![](images/BOLTSaddpart_it.png )

### Installazione

1.  Scaricare la versione stabile per FreeCAD dalla pagina [Downloads](http://www.bolts-library.org/en/downloads.html).
2.  Estrarre l\'archivio nella cartella delle macro. In genere in Linux il percorso è */usr/lib/freecad*. Se al termine del processo la cartella delle macro contiene la sottocartella *BOLTS* e il file *start\_bolts.FCMacro*, l\'installazione è conclusa.

### Provare la macro 

1.  Avviare FreeCAD
2.  Aprire il menu *Macro* e selezionare *Macros*
3.  Nella finestra *Eseguire la macro* selezionare *start\_bolts.FCMacro* e poi cliccare su *Esegui*.
4.  Nel selettore delle Parti Standard, che si apre sul lato destro dell\'interfaccia, espandere le collezioni, selezionare una parte e poi cliccare su *Add Part*.

### Possibili errori 

Può capitare che la macro non si avvii e si riceva un messaggio di errore. I più frequenti sono:

-   *No module named yaml*, o simile. Succede quando la libreria *yaml* per python non è installata, occorre installarla.
-   *No module named importlib*, o simile. Succede quando si utilizza una vecchia versione di python che non contiene *importlib*.
-   *uic import failed. Make sure that the pyside tools are installed*. In questo caso manca una parte di *PySide Qt*.

Per la soluzione di questi problemi fare riferimento al [sito Web](http://www.bolts-library.org) di BOLTS dove si trovano esaurienti indicazioni sia per Windows che per Linux.

### Creare un pulsante di avvio veloce per BOLTS 

#### Selezionare la macro e compilare i campi 

Dopo aver installato e testato BOLTS, è possibile aggiungere nell\'interfaccia grafica un pulsante che consenta di avviare velocemente la macro, senza dover aprire il menu *Macro* tutte le volte che si desidera aggiungere una Parte Standard.

1.  Aprire il menu *Strumenti -\> Personalizza*
2.  Selezionare la tabella *Macro*
3.  Nel campo *Macro* selezionare *start\_bolts.FCMacro*
4.  Nei campi successivi inserire i testi che si desidera visualizzare nella barra di stato e negli altri suggerimenti
5.  Cliccare sul campo *Pixmap*
6.  Selezionare *Aggiungi icone*, esplorare la cartella *BOLTS* e selezionare l\'icona *bolts32.png.*
7.  Cliccare su *Add*.

Per apportare delle modifiche fare doppio click sulla macro, editare e poi confermare cliccando *Replace*.

Esempio di compilazione:

![](images/BOLTSmacro1_it.png )

#### Creare una nuova barra e aggiungervi il pulsante 

Per aggiungere il pulsante a una barra degli strumenti

1.  Aprire la tabella *Personalizza -\> Barra degli strumenti*
2.  Nel drop-down di sinistra selezionare *Macro*. Attenzione, ci sono due menu *Macro*, se con quello selezionato non appaiono le voci necessarie, selezionare l\'altro
3.  Nel drop-down di destra selezionare l\'ambiente in cui si vuole inserire il pulsante
4.  Cliccare su *New\...* e nominare BOLTS la nuova barra
5.  Selezionare *start Bolts standard\...* e cliccare sulla freccia verso destra
6.  Se la scheda ha un aspetto simile a quella sottostante, tutto dovrebbe essere andato a buon fine, quindi chiudere il dialogo.

Esempio di personalizzazione:

![](images/BOLTStoolbar_it.png )

#### Provare il comando 

Per provare se il pulsante funziona:

1.  Passare all\'ambiente in cui è stata aggiunta la barra, oppure ad un altro ambiente e poi ritornare in questo se l\'ambiente è già attivo
2.  Cliccare sull\'icona del bullone giallo

### Utilizzare BOLTS in FreeCAD 

#### Inserire una Parte 

Le parti disponibili sono accessibili tramite due percorsi:

-   a - Le raccolte tematiche
-   b - Gli standard di unificazione

Per accedere al catalogo basta:

1.  Avviare BOLTS tramite Macro o tramite icona
2.  Espandere l\'albero per esplorare tutto il contenuto
3.  Selezionare una parte e cliccare su *Add Part*
4.  Nella scheda *Dati* della *Vista combinata* definire la posizione della parte inserita

Esempio di parti inserite e posizionate:

![](images/BOLTSaddpart_it.png )

#### Spostare la finestra del selettore 

Come impostazione predefinita la finestra per selezionare le parti si apre sul lato destro dell\'area di lavoro e riduce lo spazio per la vista. Per non ridurre l\'area della vista si può:

-   chiudere temporaneamente la finestra tramite il suo pulsante con la x, per riaprirla basta cliccare sull\'icona della macro, oppure
-   sganciare la finestra dall\'interfaccia principale cliccando sul suo pulsante con i quadratini sovrapposti e poi spostarla dove si vuole,
-   trascinarla e sovrapporla alla vista combinata, come nell\'esempio sottostante:

![](images/BOLTScomboview_it.png )

## PartsLibrary

In questa libreria si trovano tutte le parti standard definite in FreeCAD, porte, finestre, ecc. Siccome con gli oggetti inseriti tramite questa macro viene anche inserito tutto lo storico della loro creazione essi sono interamente modificabili. Vedere anche la pagina: _

Esempio di PartsLibrary installata:

![](images/PartsLibrary1_it.png )

### Installazione 

1.  Scaricare il repository dalla pagina [FreeCAD-library](https://github.com/yorikvanhavre/FreeCAD-library) cliccando su *Download Zip*
2.  Estrarre l\'archivio
3.  Inserire il file *PartsLibrary.FCMacro* nella cartella delle macro
4.  Inserire le cartelle dei modelli in una cartella principale, a piacere
5.  Editare il file *PartsLibrary.FCMacro* e nella riga 52 inserire il percorso della cartella principale dei modelli; vedere l\'esempio sottostante

Esempio di modifica del percorso:

![](images/LibraryPath_it.png )

### Creare un pulsante di avvio veloce per PartsLibrary 

Seguire le istruzioni descritte sopra per la macro BOLTS

### Utilizzare PartsLibrary 

#### Inserire una Parte 

1.  Avviare PartsLibrary tramite macro o tramite icona
2.  Espandere l\'albero delle parti
3.  Individuare la parte e fare doppio clic su di essa
4.  Nella scheda *Dati* della *Vista combinata* apportare le eventuali modifiche necessarie per posizionare correttamente la parte inserita

#### Spostare la finestra del catalogo 

Seguire le istruzioni descritte sopra per la macro BOLTS

### Aggiungere dei nuovi modelli alla libreria 

Con questa macro è possibile aggiungere al catalogo dei nuovi file *.fcstd* e costruire in questo modo una libreria personale di parti standard anche complesse, secondo le proprie esigenze.

## Screw maker 

Questa macro permette di creare velocemente viti e bulloni conformi alle norme ISO, tramite la loro sigla e la definizione dei parametri.

Oltre alla versione 2 è disponibile anche [Macro Screw maker 1 vers 6](http://forum.freecadweb.org/viewtopic.php?f=22&t=6088#p48519) scaricabile però solo dal Forum per motivi di dimensioni del file.

Le parti create con questa macro possono essere inserite in PartsLibrary. Siccome sono prive dello storico non si può correggerlo, però sono modificabili normalmente.

Esempio di Macro screw maker installata:

![](images/MacroScrewMaker_it.png )

### Installazione 

1.  Creare un nuovo documento di testo di nome *Macro\_screw\_maker1\_2.FCMacro*
2.  Copiare il codice di [Macro screw maker](Macro_screw_maker1_2/it.md) nel documento
3.  Posizionare il file nella cartella delle Macro

oppure

1.  Aprire il menu *Macro*
2.  Cliccare su *Macro \...*
3.  Cliccare su *Crea*
4.  Copiare il codice nella finestra e chiuderla

### Creare un pulsante di avvio veloce per Screw Maker 

Seguire le istruzioni descritte sopra per la macro BOLTS

### Utilizzare Screw Maker 

#### Inserire una Parte 

1.  Avviare Screw Maker tramite macro o tramite icona
2.  Selezionare il tipo di vite
3.  Selezionare i parametri
4.  Cliccare su *create*
5.  Nella scheda *Dati* della *Vista combinata* apportare le eventuali modifiche necessarie per posizionare correttamente la parte inserita

#### Spostare la finestra del costruttore di viti 

La finestra di questa macro è indipendente dalla finestra di FreeCAD e può essere posizionata dove si vuole.


{{languages/it| }}

_ _ _

---
[documentation index](../README.md) > Standard Parts/it
