# Manual:A gentle introduction/it
{{Manual:TOC}}

[Python](https://en.wikipedia.org/wiki/Python_%28programming_lingual%29) è un linguaggio di programmazione open source ampiamente utilizzato, riconosciuto per la sua semplicità, versatilità e leggibilità. È spesso incorporato nelle applicazioni come linguaggio di scripting e FreeCAD non fa eccezione. Questa integrazione consente agli utenti di automatizzare le attività, personalizzare i flussi di lavoro ed estendere le funzionalità del software ben oltre la sua interfaccia grafica.

Python offre numerosi vantaggi che lo rendono particolarmente adatto agli utenti di FreeCAD. È adatto ai principianti, con una sintassi chiara e intuitiva che ne facilita l\'apprendimento, anche per chi non ha esperienza di programmazione. Questa accessibilità è particolarmente preziosa nella comunità di FreeCAD, dove molti utenti provengono da background diversi, come ingegneria, architettura e design, senza una vasta esperienza di codifica.

Inoltre, l\'adozione diffusa di Python in altre applicazioni, come [Blender](https://www.blender.org) per la modellazione 3D, [Inkscape](https://www.inkscape.org) per la grafica vettoriale e [.osgeo.org/ GRASS GIS](https://grass)_per_l\'analisi_geospaziale,_lo_rende_una_competenza_essenziale_per_chiunque_desideri_espandere_le_proprie_capacità_di_scripting. Padroneggiare Python in FreeCAD non solo migliora la propria capacità di creare strumenti e macro personalizzati, ma fornisce anche competenze trasferibili che possono essere applicate su varie piattaforme software.

In FreeCAD, gli script Python consentono di:

-   Automatizzare le attività ripetitive per risparmiare tempo e ridurre gli errori.
-   Creare oggetti parametrici personalizzati che si adattano dinamicamente ai cambiamenti.
-   Sviluppare macro e strumenti personalizzati su misura per flussi di lavoro specifici.
-   Interagire con l\'API (Application Programming Interface) di FreeCAD per accedere e manipolare la geometria, le scene e gli elementi dell\'interfaccia utente in modo programmatico.

Sfruttando Python, gli utenti di FreeCAD possono sbloccare tutto il potenziale del software, trasformandolo in uno strumento potente e flessibile su misura per le loro esigenze specifiche.

FreeCAD include una console Python avanzata, accessibile tramite **Visualizza → Pannelli → Python** Console. Questo strumento consente agli utenti di eseguire operazioni oltre l\'interfaccia grafica, come l\'accesso a funzionalità avanzate, la risoluzione dei problemi relativi alla geometria e l\'automazione delle attività. Essa registra anche i comandi Python per le azioni della GUI se l\'opzione *Mostra comandi script nella console Python* è abilitata in **Modifica → Preferenze → Python → Macro**). Mantenendo aperta la console, è possibile osservare lo sviluppo del codice Python mentre si lavora, offrendo un modo intuitivo per apprendere la lingua mentre vengono esplorate le funzionalità di FreeCAD. Infine, FreeCAD dispone anche di un [sistema macro](Macros/it.md), che consente di registrare azioni da riprodurre in seguito. Questo sistema utilizza anche la console Python, semplicemente registrando tutto ciò che viene fatto al suo interno.

![](images/FreeCAD_Python_Console.png )

In questo capitolo, scopriremo molto in generale il linguaggio Python. Se siete interessati a saperne di più, il wiki della documentazione di FreeCAD ha una vasta sezione relativa alla [programmazione in Python](Power_users_hub/it.md).



### Scrivere del codice Python 

In FreeCAD, è possibile scrivere codice Python in due modi principali: tramite la console Python (**Visualizza → Pannelli → Console Python**) o utilizzando l\'editor Macro (**Macro → Macro → Crea**). La console Python consente di inserire comandi uno alla volta, che vengono eseguiti immediatamente premendo Invio, rendendola perfetta per test rapidi o esplorazioni interattive. L\'editor Macro, invece, viene utilizzato per scrivere e salvare script più complessi costituiti da più righe di codice. Queste macro possono essere eseguite in un secondo momento dalla finestra Macro, fornendo un modo potente per automatizzare attività ripetitive ed estendere le funzionalità di FreeCAD. In questo capitolo si potranno utilizzare entrambi i metodi, ma è altamente consigliato l\'uso della console Python, poiché essa informerà immediatamente di eventuali errori commessi durante la digitazione.

Se questa è la prima volta che si sta usando Python, prendere in considerazione la lettura di questa breve [introduzione a Python](Introduction_to_Python/it.md) prima di andare avanti, renderà più chiari i concetti di base di Python.



### Manipolare gli oggetti di FreeCAD 

Cominciamo creando un nuovo documento vuoto:


```python
doc = FreeCAD.newDocument()
```

Nella console Python di FreeCAD, non appena si digita FreeCAD. (la parola \"FreeCAD\" seguita da un punto), appare una finestra di completamento automatico. Questa funzionalità non solo accelera il flusso di lavoro suggerendo i comandi disponibili, ma aiuta anche a scoprire nuove funzioni e caratteristiche all\'interno di FreeCAD. Ogni voce nell\'elenco include una descrizione comando che ne spiega lo scopo, semplificando la comprensione e l\'esplorazione delle funzionalità disponibili. Questa funzionalità di completamento automatico è particolarmente utile per i principianti che imparano lo scripting Python e per gli utenti avanzati che navigano in modo efficiente nell\'ampia API di FreeCAD. Prendersi un momento per esplorare le opzioni nella finestra di completamento automatico: si potrebbero scoprire comandi che semplificano il proprio flusso di lavoro o aprono nuove possibilità.

![](images/FreeCAD_python_newDocument.png )

Digitando **FreeCAD.newDocument()** si crea un nuovo documento vuoto in FreeCAD, proprio come fare clic sul pulsante **Nuovo documento** nella barra degli strumenti. Quando si esegue **doc = FreeCAD.newDocument()**, il nuovo oggetto documento viene assegnato alla variabile **doc**, consentendo di manipolarlo a livello di programmazione. Utilizzando doc, è possibile aggiungere oggetti, modificare proprietà o salvare il documento.

In Python, il punto (.) viene utilizzato per indicare che un elemento è contenuto all\'interno di un altro. Ad esempio, **newDocument** è una funzione all\'interno del **modulo di FreeCAD**, ed è per questo che scriviamo FreeCAD.newDocument. La finestra di completamento automatico che appare mostra tutto ciò che è disponibile nel modulo FreeCAD. Se si digitasse un punto dopo newDocument (senza aggiungere le parentesi), verrà visualizzato tutto ciò che appartiene alla funzione newDocument. Questo illustra come Python organizza e accede agli oggetti e ai loro componenti. È importante notare che le parentesi sono obbligatorie quando si chiama una funzione Python, poiché segnalano l\'esecuzione della funzione.

Ora torniamo al nostro documento. Vediamo cosa possiamo fare con esso. Digitare quanto segue ed esplorare le opzioni disponibili:


```python
doc.
```

In FreeCAD, le convenzioni di denominazione per i comandi Python possono aiutare a comprenderne lo scopo:

-   I nomi che iniziano con una lettera maiuscola sono in genere attributi che memorizzano valori o dati, come le proprietà di un oggetto.
-   I nomi che iniziano con una lettera minuscola sono solitamente funzioni (chiamate anche metodi), che eseguono azioni o operazioni, come la creazione o la modifica di oggetti.
-   I nomi che iniziano con un carattere di sottolineatura (\_) sono generalmente destinati ad uso interno all\'interno del modulo e solitamente possono essere ignorati.

Questa distinzione aiuta a navigare nell\'API di FreeCAD e a selezionare il comando appropriato per le proprie esigenze. Ad esempio, si potrebbe utilizzare un metodo per aggiungere un nuovo oggetto a un documento. Il metodo esegue l\'azione di creazione e aggiunta dell\'oggetto, mentre gli attributi memorizzano le proprietà dell\'oggetto. Comprendere questa struttura semplifica l\'esplorazione delle funzionalità disponibili, soprattutto quando si utilizza la funzione di completamento automatico o si leggono i suggerimenti. Aggiungiamo una casella.


```python
box = doc.addObject("Part::Box", "myBox")
```

Il comando **box = doc.addObject(\"Part::Box\", \"myBox\")** aggiunge un nuovo oggetto cubo (box) 3D al documento. Ecco una semplice spiegazione:

-   **doc.addObject**: Dice a FreeCAD di aggiungere un nuovo oggetto al documento.
-   **Part::Box**: Specifica il tipo di oggetto da creare, in questo caso, un cubo (box) 3D.
-   **myBox**: Assegna un nome al nuovo oggetto, rendendone più semplice l\'identificazione e il riferimento in seguito.

Il risultato di questo comando è che nel documento attivo appare un riquadro e la variabile box memorizza un riferimento ad esso in modo da poterlo modificare o interagire in seguito. Il nostro box viene aggiunto nella vista ad albero, ma non succede ancora nulla nella vista 3D, perché quando si lavora da Python, il documento non viene mai ricalcolato automaticamente. Dobbiamo farlo manualmente, ogni volta che è richiesto:


```python
doc.recompute()
```

Ora nella vista 3D è apparso il box. Molti dei pulsanti della barra degli strumenti che aggiungono oggetti in FreeCAD in effetti fanno due cose: aggiungono l\'oggetto, e ricalcolano. Provate ad aggiungere una sfera con l\'apposito pulsante dell\'ambiente Parte, e vedrete le due righe di codice Python eseguite una dopo l\'altra.

![](images/FreeCAD_python_Sphere.png )

È possibile ottenere un elenco di tutti i possibili tipi di oggetti come Part::Box:


```python
doc.supportedTypes()
```

Ora esploriamo i contenuti del box:


```python
box.
```

Si possono vedere subito un paio di cose molto interessanti quali:


```python
box.Height
```

Questo comando stampa l\'altezza corrente del nostro box. Ora proviamo a cambiarla:


```python
box.Height = 5
```

Se si seleziona il box con il mouse, si vede che nel pannello delle proprietà, sotto la scheda **Dati**, la proprietà **Height** appare con il nuovo valore. Tutte le proprietà di un oggetto FreeCAD che appaiono nelle schede **Dati** e **Vista** sono anche accessibili direttamente con Python, tramite i loro nomi, come abbiamo fatto con la proprietà Height. Le proprietà Dati sono accessibili direttamente dall\'oggetto stesso, ad esempio:


```python
box.Length
```

In FreeCAD, le proprietà visive sono gestite da un **ViewObject**. Ogni oggetto di FreeCAD ha un ViewObject associato, che memorizza informazioni su come l\'oggetto viene visualizzato nell\'interfaccia grafica, come colore, trasparenza o visibilità. Tuttavia, ViewObject è accessibile solo quando FreeCAD è in esecuzione con la sua interfaccia grafica. Se FreeCAD viene avviato in modalità non grafica, ad esempio da un terminale con l\'opzione della riga di comando -c o quando viene utilizzato come libreria Python in uno script esterno, ViewObject non è disponibile. Questo perché in queste modalità non esiste una rappresentazione visiva dell\'oggetto, poiché l\'interfaccia grafica non viene caricata.

Provare esempio per accedere al colore della linea del box:


```python
box.ViewObject.LineColor
```



### Vettori e Posizionamenti 

I vettori sono un concetto fondamentale in qualsiasi applicazione 3D. Un vettore è essenzialmente un elenco di tre numeri (x, y e z) che descrivono un punto, una posizione o una direzione nello spazio 3D. I vettori sono fondamentali per definire la geometria, le trasformazioni e le interazioni nell\'ambiente 3D. Fungono da elementi costitutivi per operazioni quali traslazioni, rotazioni e ridimensionamento.

In FreeCAD, i vettori sono ampiamente utilizzati per creare e manipolare oggetti. Consentono un\'ampia gamma di operazioni matematiche, come addizione, sottrazione, prodotti incrociati, prodotti scalari e proiezioni. Queste operazioni consentono di calcolare distanze, angoli e direzioni o definire relazioni tra oggetti nello spazio.

Comprendere i vettori e il loro funzionamento è essenziale per uno scripting e una personalizzazione efficaci in FreeCAD. Ad esempio, i vettori vengono utilizzati per posizionare gli oggetti, definirne l\'orientamento o persino calcolare i percorsi per operazioni complesse come sweep o loft.

In FreeCAD, i vettori sono rappresentati utilizzando la classe **Vector**, che fornisce vari metodi e proprietà per eseguire operazioni e accedere ai loro componenti. Padroneggiare queste capacità migliorerà significativamente la propria capacità di interagire con l\'ambiente 3D di FreeCAD in modo programmatico. In FreeCAD i vettori funzionano in questo modo:


```python
myvec = FreeCAD.Vector(2, 0, 0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Ecco una breve suddivisione dei comandi precedenti:

-   **myvec = FreeCAD.Vector(2,0,0)**: Crea un vettore myvec con X = 2, Y = 0, Z = 0.
-   **print(myvec)**: Stampa il vettore myvec con i suoi componenti (X, Y, Z).
-   **print(myvec.x)**: Stampa il componente X di myvec.
-   **print(myvec.y)**: Stampa il componente Y di myvec.
-   **othervec = FreeCAD.Vector(0,3,0)**: Crea un secondo vettore othervec con X = 0, Y = 3, Z = 0.
-   **sumvec = myvec.add(othervec)**: Aggiunge myvec e othervec per creare un nuovo vettore sumvec contenente la somma dei loro componenti.

Un\'altra caratteristica comune degli oggetti FreeCAD è il loro **Posizionamento**. Come abbiamo visto nei capitoli precedenti, ogni oggetto ha una proprietà Placement, che contiene la posizione (Base) e l\'orientamento (Rotazione) dell\'oggetto. Con Python è facile manipolare queste proprietà, ad esempio per spostare l\'oggetto:


```python
print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5, 5, 0)
box.Placement = otherpla
```

Ecco una breve suddivisione dei comandi precedenti:

-   **print(box.Placement)**: Stampa il posizionamento del box, che include la sua posizione, rotazione e orientamento nello spazio 3D.
-   **print(box.Placement.Base)**: Stampa la posizione (Base) del box, che è un vettore che rappresenta la sua posizione nello spazio 3D.
-   **box.Placement.Base = sumvec**: Imposta la posizione base (posizione) del box sul vettore sumvec, spostando di fatto il box in questa nuova posizione.
-   **otherpla = FreeCAD.Placement()**: Crea un nuovo oggetto di posizionamento denominato otherpla.
-   **otherpla.Base = FreeCAD.Vector(5,5,0)**: Imposta la posizione base di otherpla su un vettore alle coordinate (5, 5, 0).
-   **box.Placement = otherpla**: Applica otherpla al box, aggiornando il suo posizionamento alla nuova posizione e orientamento definiti da otherpla.

**Approfondimenti**

-   [Python](https://www.python.org)
-   [Macro](Macros/it.md)
-   [Introduzione a Python](Introduction_to_Python/it.md)
-   [Guida agli script di Python ](Python_scripting_tutorial/it.md)
-   [Hub degli utenti esperti](Power_users_hub/it.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:A gentle introduction/it
