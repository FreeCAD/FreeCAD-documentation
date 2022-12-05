# FreeCAD Scripting Basics/it
{{TOCright}}

## Script Python in FreeCAD 

FreeCAD è stato costruito fin dall\'inizio per essere totalmente controllato tramite gli script Python.

Quasi tutte le parti di FreeCAD, come ad esempio l\'interfaccia oppure i contenuti della finestra, compresa la rappresentazione di quanto contenuto nelle viste 3D, sono accessibili tramite l\'interprete Python incorporato o tramite script personali.

Per questo, FreeCAD risulta probabilmente una delle applicazioni ingegneristiche più profondamente personalizzabili oggi disponibili.

Se non conoscete ancora Python, vi consigliamo di cercare qualche tutorial su internet e di dare un rapido sguardo alla sua struttura.

Python è un linguaggio molto facile da imparare, soprattutto perché può essere eseguito all\'interno di un interprete, dove sia i comandi semplici come i programmi completi, possono essere eseguiti \"al volo\", cioè senza bisogno di compilare nulla.

FreeCAD incorpora un interprete Python. Se non vedete la finestra denominata \"Console Python\" della figura successiva, potete attivarla con **Visualizza → Pannelli → Console Python** e mostrare l\'interprete.

### L\'interprete

Tramite l\'interprete, è possibile accedere a tutti i moduli Python installati nel sistema, come pure ai moduli incorporati in FreeCAD e a tutti i moduli aggiuntivi di FreeCAD installati successivamente.

La schermata seguente mostra l\'interprete Python di FreeCAD:

![The FreeCAD Python interpreter](images/screenshot_pythoninterpreter.jpg )

Tramite l\'interprete è possibile eseguire del codice Python ed esplorare le classi e le funzioni disponibili.

FreeCAD fornisce un browser delle classi molto utile per esplorare il nuovo mondo di FreeCAD.

Quando si digita il nome di una classe nota seguita da un punto (.) (il che significa che si intende completare aggiungendo qualcos\'altro alla classe), si apre la finestra del browser delle classi, dove si può navigare tra le sottoclassi e i metodi disponibili.

Quando si seleziona una voce, viene visualizzato il testo di aiuto associato (se esiste):

![The FreeCAD class browser](images/screenshot_classbrowser.jpg )

Per verificare questo, iniziate a digitare `App.` oppure `Gui.` e osservate cosa succede.

Generalmente, in Python, per esplorare il contenuto dei moduli e delle classi si utilizza il comando `print(dir())`.

Ad esempio, digitando `print(dir())` si ottiene l\'elenco di tutti i moduli attualmente caricati in FreeCAD e con `print(dir(App))` si mostra tutto ciò che è contenuto all\'interno del modulo App, ecc..

Inoltre l\'interprete ricorda i codici che vengono digitati. Questa altra utile caratteristica dell\'interprete permette di esplorare all\'indietro i comandi digitati e di recuperare, attraverso la cronologia, una riga di codice scritta in precedenza.

Per navigare nella cronologia dei comandi, basta usare i tasti **Freccia sù** oppure **Freccia giù**.

Cliccando col tasto destro nella finestra dell\'interprete, si rendono disponibili diverse altre opzioni, quali, ad esempio, copiare lo storico (l\'intera cronologia, cosa utile quando si desidera sperimentare qualcosa prima di utilizzarla in uno script) oppure inserire un nome di un file con il suo percorso completo. {{Top}}

### Help di Python 

Nel menu **Help** di FreeCAD, troverai una voce denominata **Automatic python modules documentation**, che aprirà una finestra del browser contenente una documentazione completa e generata in tempo reale di tutti i moduli Python disponibili per l\'interprete di FreeCAD, inclusi i moduli integrati di Python e FreeCAD, i moduli installati dal sistema e i moduli aggiuntivi di FreeCAD. La documentazione lì disponibile dipende da quanto sforzo ogni sviluppatore di moduli ha fatto per documentare il suo codice, ma i moduli Python hanno la reputazione di essere abbastanza ben documentati. La finestra di FreeCAD deve rimanere aperta affinché questo sistema di documentazione funzioni. {{Top}}

## Moduli incorporati 

Poiché FreeCAD è progettato in modo da poter essere eseguito anche senza un\'interfaccia utente grafica (GUI), quasi tutte le sue funzionalità sono separate in due gruppi: funzionalità principale, denominata `App`, e funzionalità GUI, denominata {{incode |Gui}}. È possibile accedere a questi due moduli anche da script esterni all\'interprete, rispettivamente con i nomi `FreeCAD` e `FreeCADGui`.

-   Nel modulo `App`, si trova tutto ciò che riguarda l\'applicazione stessa, cioè i metodi per l\'apertura o la chiusura di file e documenti, oppure l\'impostazione del documento attivo o la visualizzazione dei contenuti.

-   Nel modulo `Gui`, si trovano gli strumenti per accedere e gestire gli elementi dell\'interfaccia grafica (GUI), cioè gli ambienti di lavoro e le loro barre degli strumenti e, più interessante, la rappresentazione grafica di tutti i contenuti di FreeCAD.

Elencare il contenuto di questi moduli non è molto utile perché crescono abbastanza velocemente con lo sviluppo di FreeCAD. Ma i due strumenti di navigazione forniti (il browser di classe e la guida di Python) dovrebbero fornire una documentazione completa e aggiornata in qualsiasi momento. {{Top}}

### Gli oggetti App e GUI 

Come già accennato, in FreeCAD tutto è separato in core e representation. Ciò include gli oggetti 3D. Si può accedere alle proprietà di definizione degli oggetti (chiamate funzionalità in FreeCAD) tramite il modulo `App` e modificare il modo in cui sono rappresentate sullo schermo tramite il modulo `Gui`. Ad esempio, un cubo ha proprietà che lo definiscono (come larghezza, lunghezza, altezza) che sono archiviate in un oggetto `App` e proprietà di rappresentazione (come il colore delle facce, la modalità di disegno) che sono archiviate in un corrispondente oggetto `Gui`.

Questo modo di fare le cose consente una vasta gamma di operazioni, come gli algoritmi che funzionano solo sulla parte di definizione delle caratteristiche, senza la necessità di prendersi cura di nessuna parte visiva, e consente anche di reindirizzare il contenuto del documento ad applicazioni non-grafiche, quali, ad esempio, elenchi, fogli di calcolo, o analisi degli elementi.

Per ogni oggetto `App` nel tuo documento, esiste un oggetto `Gui` corrispondente. Infatti il ​​documento stesso ha sia un oggetto `App` che un oggetto `Gui`. Questo, ovviamente, si applica solo quando esegui FreeCAD con la sua interfaccia completa. Nella versione da riga di comando non esiste una GUI, quindi sono disponibili solo oggetti `App`. Nota che la parte `Gui` degli oggetti viene rigenerata ogni volta che un oggetto `App` viene contrassegnato come \'da ricalcolare\' (ad esempio quando uno dei suoi parametri cambia), quindi qualsiasi modifica fatta direttamente all\'oggetto `Gui` potrebbe andare persa.

Per accedere alla parte `App` di qualcosa, si digita:


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```

dove `"ObjectName"` è il nome del vostro oggetto. Inoltre è possibile digitare:


```python
myObject = App.ActiveDocument.ObjectName
```

Per accedere alla parte `Gui` dello stesso oggetto, si digita:


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```

dove `"ObjectName"` è il nome del vostro oggetto. Inoltre è possibile digitare:


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```

Se sei in modalità riga di comando e non hai la GUI, l\'ultima riga restituirà `None`. {{Top}}

### Gli oggetti del documento 

In FreeCAD tutto il tuo lavoro risiede all\'interno dei documenti. Un documento contiene la tua geometria e può essere salvato in un file. È possibile aprire più documenti contemporaneamente. Il documento, come la geometria contenuta all\'interno, ha oggetti `App` e `Gui`. L\'oggetto `App` contiene le tue effettive definizioni della geometria, mentre l\'oggetto `Gui` contiene le diverse viste del tuo documento. Puoi aprire più finestre, ognuna delle quali visualizza il tuo lavoro con un fattore di zoom diverso o da una direzione diversa. Queste viste fanno tutte parte dell\'oggetto `Gui` del tuo documento.

Per accedere alla parte `App` del documento attualmente aperto (attivo), digitare:


```python
myDocument = App.ActiveDocument
```

Per creare un nuovo documento, digitare:


```python
myDocument = App.newDocument("Document Name")
```

Per accedere alla parte `Gui` del documento attualmente aperto (attivo), digitare:


```python
myGuiDocument = Gui.ActiveDocument
```

Per accedere alla vista corrente, digitare:


```python
myView = Gui.ActiveDocument.ActiveView
```


{{Top}}

## Utilizzo di moduli aggiuntivi 

I moduli `FreeCAD` e `FreeCADGui` sono responsabili solo della creazione e della gestione degli oggetti nel documento FreeCAD. In realtà non fanno altro che creare o modificare la geometria. Questo perché la geometria può essere di diversi tipi e quindi richiede moduli aggiuntivi, ciascuno responsabile della gestione di un determinato tipo di geometria. Ad esempio, l\'[Ambiente Part](Part_Workbench/it.md), utilizzando il kernel OpenCascade, è in grado di creare e manipolare la geometria di tipo [BRep](https://it.wikipedia.org/wiki/B-Rep). Mentre l\'[Ambiente Mesh](Mesh_Workbench/it.md) è in grado di costruire e modificare oggetti mesh. In questo modo FreeCAD è in grado di gestire un\'ampia varietà di tipi di oggetti, che possono coesistere tutti nello stesso documento, e nuovi tipi possono essere facilmente aggiunti in futuro. {{Top}}

#### Creare degli oggetti 

Ogni modulo ha il proprio modo di gestire la geometria, ma una cosa che di solito tutti possono fare è creare oggetti nel documento. Ma il documento di FreeCAD è anche a conoscenza dei tipi di oggetti disponibili forniti dai moduli:


```python
FreeCAD.ActiveDocument.supportedTypes()
```

elencherà tutti i possibili oggetti che puoi creare. Ad esempio, creiamo una mesh (gestita dal modulo `Mesh`) e una parte (gestita dal modulo `Part`):


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```

Il primo argomento è il tipo di oggetto, il secondo il nome dell\'oggetto. I nostri due oggetti sembrano quasi uguali: non contengono ancora alcuna geometria e la maggior parte delle loro proprietà sono le stesse quando li ispezioni con `dir(myMesh)` e `dir(myPart)`. Ad eccezione di una cosa, `myMesh` ha una proprietà `Mesh` e `myPart` ha una proprietà `Shape`. È qui che vengono archiviati i dati Mesh e Part. Ad esempio, creiamo un cubo `Part` e memorizziamolo nel nostro oggetto `myPart`:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Si può provare a memorizzare il cubo all\'interno della proprietà `Mesh` dell\'oggetto `myMesh`, ma verrà restituito un errore. Questo perché ogni proprietà è fatta per memorizzare solo un certo tipo. In una proprietà `Mesh`, puoi salvare solo elementi creati con il modulo `Mesh`. Nota che la maggior parte dei moduli ha anche una scorciatoia per aggiungere la propria geometria al documento:


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```


{{Top}}

### Modificare gli oggetti 

La modifica di un oggetto avviene allo stesso modo:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Ora cambiamo la sua forma in una più grande:


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```


{{Top}}

### Interrogare gli oggetti 

È sempre possibile sapere di che tipo è un oggetto con:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```

o controllare se un oggetto è derivato da uno di quelli base (struttura di Parte, struttura di Mesh, etc) con:


```python
print(myObj.isDerivedFrom("Part::Feature"))
```

Ora puoi davvero iniziare a giocare con FreeCAD! Per un elenco completo dei moduli disponibili e dei relativi strumenti, visita la sezione . {{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > FreeCAD Scripting Basics/it
