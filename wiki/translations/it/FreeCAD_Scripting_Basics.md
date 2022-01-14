# FreeCAD Scripting Basics/it
{{TOCright}}

## Script Python in FreeCAD 

FreeCAD è stato costruito fin dall\'inizio per essere totalmente controllato tramite gli script Python.

Quasi tutte le parti di FreeCAD, come ad esempio l\'interfaccia oppure i contenuti della scena, compresa la rappresentazione di quanto contenuto nelle viste 3D, sono accessibili tramite l\'interprete Python incorporato o tramite script personali.

Per questo, FreeCAD risulta probabilmente una delle applicazioni ingegneristiche più profondamente personalizzabili oggi disponibili.

Se non conoscete ancora Python, vi consigliamo di cercare qualche tutorial su internet e di dare un rapido sguardo alla sua struttura.

Python è un linguaggio molto facile da imparare, soprattutto perché può essere eseguito all\'interno di un interprete, dove sia i comandi semplici come i programmi completi, possono essere eseguiti \"al volo\", cioè senza bisogno di compilare nulla.

FreeCAD incorpora un interprete Python. Se non vedete la finestra denominata \"Console Python\" della figura successiva, potete attivarla con **Visualizza → Pannelli → Console Python** e mostrare l\'interprete.

### L\'interprete

Tramite l\'interprete, è possibile accedere a tutti i moduli Python installati nel sistema, come pure ai moduli incorporati in FreeCAD e a tutti i moduli aggiuntivi di FreeCAD installati successivamente.

La schermata seguente mostra l\'interprete Python di FreeCAD:

![The FreeCAD Python interpreter](images/screenshot_pythoninterpreter.jpg )

Tramite l\'interprete è possibile eseguire del codice Python e sfogliare le classi e le funzioni disponibili.

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


<div class="mw-translate-fuzzy">

### Aiuti di Python 

Nel menu *Aiuto* di FreeCAD, trovate una voce denominata *Documentazione automatica per i moduli Python*, essa apre una finestra del browser contenente una documentazione completa, generata in tempo reale, di tutti i moduli Python a disposizione dell\'interprete di FreeCAD, compreso Python e i moduli interni di FreeCAD, i moduli installati dal sistema e i moduli aggiuntivi di FreeCAD.

La documentazione disponibile dipende dalla fatica che lo sviluppatore del modulo ha fatto per documentare il proprio codice. I moduli Python hanno la reputazione di essere in genere abbastanza ben documentati. La finestra di FreeCAD deve rimanere aperta perché questo sistema di documentazione funzioni.

La voce \"Python Help\" fornisce un collegamento rapido alla sezione wiki \"User Hub\".


</div>

In the FreeCAD **Help** menu, you\'ll find an entry labeled **Automatic python modules documentation**, which will open a browser window containing a complete, realtime-generated documentation of all Python modules available to the FreeCAD interpreter, including Python and FreeCAD built-in modules, system-installed modules, and FreeCAD additional modules. The documentation available there depends on how much effort each module developer put into documenting his code, but Python modules have a reputation for being fairly well documented. Your FreeCAD window must stay open for this documentation system to work. The entry **Python scripting documentation** will give you a quick link to the [Power users hub](Power_users_hub.md) wiki section. {{Top}}


<div class="mw-translate-fuzzy">

## Moduli incorporati (Built-in) 

Dato che FreeCAD è stato progettato per essere eseguito senza una interfaccia grafica (GUI), quasi tutte le sue funzionalità sono divise in due parti: la funzionalità di base, denominata *App*, e la funzionalità grafica, denominata *Gui*. Per questo motivo i due principali moduli incorporati nel nostro FreeCAD sono chiamati App e Gui. Questi due moduli sono accessibili, rispettivamente con il nome \"FreeCAD\" e \"FreeCADGui\", anche tramite script eseguiti al di fuori dell\'interprete.


</div>

Since FreeCAD is designed so that it can also be run without a Graphical User Interface (GUI), almost all its functionality is separated into two groups: Core functionality, named `App`, and GUI functionality, named `Gui`. These two modules can also be accessed from scripts outside of the interpreter, by the names `FreeCAD` and `FreeCADGui` respectively.


<div class="mw-translate-fuzzy">

-   Nel modulo **App**, si trova tutto ciò che riguarda l\'applicazione stessa, cioè i metodi per l\'apertura o la chiusura di file e documenti, oppure l\'impostazione del documento attivo o la visualizzazione dei contenuti.


</div>


<div class="mw-translate-fuzzy">

-   Nel modulo **Gui**, si trovano gli strumenti per accedere e gestire gli elementi dell\'interfaccia grafica (GUI), cioè gli ambienti di lavoro e le loro barre degli strumenti e, più interessante, la rappresentazione grafica di tutti i contenuti di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Elencare tutto il contenuto di tali moduli è un lavoro un po\' controproducente, in quanto essi crescono molto velocemente seguendo lo sviluppo di FreeCAD.

I due strumenti di esplorazione disponibili (il browser delle classi e l\'aiuto di Python) dovrebbero dare, in qualsiasi momento, una completa e aggiornata documentazione di questi moduli.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Gli oggetti App e gli oggetti GUI 

Come abbiamo detto, in FreeCAD, tutto viene separato tra nucleo e rappresentazione. Ciò vale anche per gli oggetti 3D.

È possibile accedere alla definizione delle proprietà degli oggetti (chiamate funzioni in FreeCAD) tramite il modulo App, e cambiare il modo in cui gli oggetti vengono riprodotti sullo schermo tramite il modulo Gui.

Ad esempio, un parallelepipedo ha delle proprietà che lo definiscono, (cioè larghezza, lunghezza e altezza) che vengono memorizzate in un *oggetto App* e delle proprietà di rappresentazione, (come il colore delle facce, la modalità di disegno) che sono memorizzate in un corrispondente *oggetto Gui*.


</div>

As already mentioned, in FreeCAD everything is separated into core and representation. This includes the 3D objects. You can access defining properties of objects (called features in FreeCAD) via the `App` module, and change the way they are represented on screen via the `Gui` module. For example, a cube has properties that define it (like width, length, height) that are stored in an `App` object, and representation properties (like faces color, drawing mode) that are stored in a corresponding `Gui` object.

Questo modo di fare le cose consente una vasta gamma di operazioni, come gli algoritmi che funzionano solo sulla parte di definizione delle caratteristiche, senza la necessità di prendersi cura di nessuna parte visiva, e consente anche di reindirizzare il contenuto del documento a applicazioni non-grafiche, quali, ad esempio, elenchi, fogli di calcolo, o analisi degli elementi.


<div class="mw-translate-fuzzy">

Nel documento, per ogni oggetto App, esiste un corrispondente oggetto Gui. Infatti lo stesso documento possiede sia oggetti App che oggetti Gui.

Questo, naturalmente, è valido solo quando si esegue FreeCAD completo di interfaccia grafica. Nella versione riga di comando, senza interfaccia grafica, sono quindi disponibili solo gli oggetti App.

Ricordare che la parte Gui degli oggetti viene rigenerata ogni volta che un oggetto App viene indicato \"da ricalcolare\" (ad esempio quando cambia uno dei suoi parametri), in quanto le modifiche fatte direttamente all\'oggetto Gui potrebbero perdersi.


</div>


<div class="mw-translate-fuzzy">

Per accedere alla parte App di qualcosa, si digita:


</div>


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

dove \"ObjectName\" è il nome del vostro oggetto.

Inoltre è possibile digitare:


</div>


```python
myObject = App.ActiveDocument.ObjectName
```


<div class="mw-translate-fuzzy">

Per accedere alla parte Gui dello stesso oggetto, si digita:


</div>


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

dove \"ObjectName\" è il nome del vostro oggetto.

Inoltre è possibile digitare:


</div>


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```


<div class="mw-translate-fuzzy">

Se non abbiamo GUI (ad esempio, siamo in modalità riga di comando), l\'ultima riga non restituirà nulla.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Gli oggetti del documento 

In FreeCAD tutto il vostro lavoro si trova all\'interno dei documenti.

Un documento contiene la geometria e può essere salvato in un file. Si possono avere simultaneamente più documenti aperti.

Il documento, come la geometria contenuta all\'interno, ha oggetti App e oggetti Gui. L\'oggetto App contiene le definizioni della geometria reale, mentre l\'oggetto Gui contiene i diversi punti di vista del documento.

È possibile aprire più finestre, ognuna delle quali visualizza il lavoro con un fattore di zoom o un punto di vista diverso. Questi punti di vista fanno tutti parte dell\'oggetto Gui del documento.


</div>

In FreeCAD all your work resides inside documents. A document contains your geometry and can be saved to a file. Several documents can be opened at the same time. The document, like the geometry contained inside, has `App` and `Gui` objects. The `App` object contains your actual geometry definitions, while the `Gui` object contains the different views of your document. You can open several windows, each one viewing your work with a different zoom factor or from a different direction. These views are all part of your document\'s `Gui` object.


<div class="mw-translate-fuzzy">

Per accedere alla parte App del documento attualmente aperto (attivo), si digita:


</div>


```python
myDocument = App.ActiveDocument
```

Per creare un nuovo documento, si digita:


```python
myDocument = App.newDocument("Document Name")
```


<div class="mw-translate-fuzzy">

Per accedere alla parte Gui del documento attualmente aperto (attivo), si digita:


</div>


```python
myGuiDocument = Gui.ActiveDocument
```

Per accedere alla vista corrente, si digita:


```python
myView = Gui.ActiveDocument.ActiveView
```


{{Top}}


<div class="mw-translate-fuzzy">

## Utilizzo di moduli aggiuntivi 

I moduli FreeCAD e FreeCADGui sono responsabili esclusivamente della creazione e della gestione degli oggetti nel documento di FreeCAD.

Essi in realtà non fanno nulla che riguardi la creazione o la modifica della geometria.

Ciò è dovuto al fatto che la geometria può essere di diversi tipi, e quindi la sua gestione è affidata ai moduli aggiuntivi, ognuno di essi ha il compito di gestire uno specifico tipo di geometria.

Il modulo [Parte](Part_Workbench/it.md) utilizza il kernel OpenCascade, e quindi è in grado di creare e manipolare geometrie di tipo [B-rep](http://en.wikipedia.org/wiki/Boundary_representation), che è appunto il tipo di geometria costruito da OpenCascade.

Il modulo [Mesh](Mesh_Workbench/it.md) è in grado di costruire e modificare gli oggetti mesh.

In questo modo, FreeCAD è in grado di gestire un\'ampia gamma di tipi di oggetti che possono coesistere nello stesso documento, e nuovi tipi potrebbero essere aggiunti facilmente in futuro.


</div>

The `FreeCAD` and `FreeCADGui` modules are only responsible for creating and managing objects in the FreeCAD document. They don\'t actually do anything more such as creating or modifying geometry. This is because that geometry can be of several types, and therefore requires additional modules, each responsible for managing a certain geometry type. For example, the [Part Workbench](Part_Workbench.md), using the OpenCascade kernel, is able to create and manipulate [BRep](http://en.wikipedia.org/wiki/Boundary_representation) type geometry. Whereas the [Mesh Workbench](Mesh_Workbench.md) is able to build and modify mesh objects. In this manner FreeCAD is able to handle a wide variety of object types, that can all coexist in the same document, and new types can easily be added in the future. {{Top}}


<div class="mw-translate-fuzzy">

#### Creare degli oggetti 

Ogni modulo tratta la propria geometria in un modo specifico, però in genere tutti i moduli possono creare degli oggetti nel documento.

Il documento FreeCAD è anche a conoscenza dei tipi di oggetti fornibili dai moduli e il seguente comando:


</div>

Each module has its own way of dealing with geometry, but one thing they usually all can do is create objects in the document. But the FreeCAD document is also aware of the available object types provided by the modules:


```python
FreeCAD.ActiveDocument.supportedTypes()
```


<div class="mw-translate-fuzzy">

mostra tutti gli oggetti che si possono creare.

Come esempio, proviamo a creare un oggetto mesh (trattato dal modulo Mesh) e un oggetto parte (trattato dal modulo Part):


</div>


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```


<div class="mw-translate-fuzzy">

Il primo parametro è il tipo di oggetto, il secondo il nome dell\'oggetto. I nostri due oggetti appaiono quasi come la stessa cosa.

Al momento, essi non contengono ancora la geometria, e se li ispezioniamo con dir(myMesh) e con dir(myPart) la maggior parte delle loro proprietà sono le stesse. L\'unica differenza è che myMesh ha una proprietà \"Mesh\" e \"Part\" ha una proprietà \"Shape\". È qui che i dati Mesh e Parte vengono memorizzati.

Come esempio, creiamo un cubo di tipo Parte e poi lo archiviamo nel nostro oggetto myPart:


</div>


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```


<div class="mw-translate-fuzzy">

Se provate a memorizzare il cubo all\'interno della proprietà Mesh dell\'oggetto myMesh, vi verrà restituito un messaggio di \"errore di tipo\". Questo perché le proprietà sono fatte in modo da memorizzare solo uno specifico tipo. Nelle proprietà Mesh di myMesh, è possibile salvare solo elementi creati con il modulo Mesh.

Notare che la maggior parte dei moduli hanno anche un collegamento per aggiungere la loro geometria al documento:


</div>


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```


{{Top}}


<div class="mw-translate-fuzzy">

### Modificare gli oggetti 

La modifica di un oggetto si esegue nello stesso modo:


</div>

Modifying an object is done in the same way:


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


<div class="mw-translate-fuzzy">

### Interrogare gli oggetti 

È sempre possibile sapere di che tipo è un oggetto con:


</div>

You can always look at the type of an object like this:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```


<div class="mw-translate-fuzzy">

o sapere se un oggetto è derivato da uno di quelli base (struttura di Parte, struttura di Mesh, etc) con:


</div>


```python
print(myObj.isDerivedFrom("Part::Feature"))
```


<div class="mw-translate-fuzzy">

Ora si può davvero iniziare a divertirsi con FreeCAD! Per vedere ciò che si può fare con il [Modulo Parte](Part_Workbench/it.md), leggere la pagina [Script per ambiente Parte](Topological_data_scripting/it.md), o la pagina [Script per ambiente Mesh](Mesh_Scripting/it.md) per lavorare con il [Modulo Mesh](Mesh_Workbench/it.md).

Notare che, oltre ai moduli Parte e Mesh che sono i più completi e sono molto utilizzati, anche altri moduli come il [Modulo Draft](Draft_Workbench/it.md) hanno [script](Draft_API/it.md) API che possono servirvi.

Per un elenco completo di tutti i moduli e gli strumenti disponibili, consultare la sezione [:<img src="images/Property.png" style="width:16px"> API/it](:<img src="images/Property.png" style="width:16px"> API/it.md).


</div>


{{Top}}





{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD Scripting Basics/it
