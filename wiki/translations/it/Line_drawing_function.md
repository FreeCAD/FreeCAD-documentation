# Line drawing function/it
## Introduzione

Questa pagina mostra come si possono facilmente creare delle funzionalità avanzate con Python.

In questo esercizio, andremo a creare un nuovo strumento che disegna una linea partendo da due punti cliccati nella vista 3D.

Questo strumento può essere collegato a un comando di FreeCAD, e tale comando può essere chiamato da un qualsiasi elemento dell\'interfaccia, ad esempio da una voce di menu o da un pulsante in una barra degli strumenti.



## Lo script principale 

Per prima cosa scriviamo uno script che contenga tutta la nostra funzionalità. Dopo, salviamo questo script in un file e lo importiamo in FreeCAD, in modo che tutte le classi e le funzioni che scriviamo diventino disponibili in FreeCAD. Lanciamo perciò il nostro editor di testo preferito, e digitiamo le seguenti righe:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}



### Spiegazione dettagliata 


```python
import Part, FreeCADGui
from pivy.coin import *
```

In Python, quando si desidera utilizzare le funzioni di un altro modulo è necessario importarlo. Nel nostro caso, abbiamo bisogno delle funzioni del [Ambiente Parte](Part_Workbench/it.md) per creare la linea, e del modulo Gui `FreeCADGui` per accedere alla [Vista 3D](3D_view/it.md). Inoltre, abbiamo anche bisogno del contenuto completo della libreria di Coin, in modo da poter utilizzare direttamente tutti gli oggetti Coin, come, ad esempio, `SoMouseButtonEvent`, ecc ..


```python
class line:
```

Qui definiamo la nostra classe principale.

Perché utilizzare una classe e non una funzione? Il motivo è che abbiamo bisogno che il nostro strumento rimanga \"vivo\" mentre aspettiamo che l\'utente clicchi sullo schermo.

Una funzione termina quando il suo compito è stato svolto, invece un oggetto (una classe definisce un oggetto) rimane attivo finché non viene distrutto.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```

In Python, ogni classe o funzione può avere una stringa di documentazione (docstring). In FreeCAD, questo è particolarmente utile perché quando chiameremo la classe nell\'interprete, la stringa di descrizione verrà visualizzata come tooltip (nota di descrizione o aiuto).


```python
def __init__(self):
```

Le classi di Python possono sempre contenere una funzione `__init__`, che viene eseguita quando la classe viene chiamata per creare un oggetto. Qui metteremo tutto quello che vogliamo che accada quando il nostro strumento line inizia.


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```

In una classe, di solito si aggiunge `self.` prima di un nome di variabile, in modo che sia facilmente accessibile a tutte le funzioni dentro e fuori la classe. In questo script, usiamo `self.view` per accedere e manipolare la vista 3D attiva.


```python
self.stack = []
```

Qui creiamo una lista vuota per archiviare i punti 3D inviati dalla funzione `getpoint()`.


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```


<div class="mw-translate-fuzzy">

Questa è la parte importante.

Dato che in realtà si tratta una scena [Coin3d](http://www.coin3d.org/), FreeCAD utilizza il meccanismo di callback (richiamo) di Coin, il quale permette di chiamare una funzione ogni volta che nella scena accade un determinato evento.

Nel nostro caso, stiamo creando un callback per gli eventi [SoMouseButtonEvent](http://doc.coin3d.org/Coin/group__events.html) e li colleghiamo alla funzione getpoint. Adesso, ogni volta che un pulsante del mouse viene premuto o rilasciato, viene eseguita la funzione getpoint.


</div>


<div class="mw-translate-fuzzy">

Notare che alla addEventCallbackPivy() esiste anche un\'alternativa, chiamata addEventCallback() la quale dispensa dall\'uso di pivy. Ma, dal momento che pivy è un modo molto efficace e naturale per accedere a ogni parte di una scena di Coin, è meglio utilizzarlo il più possibile!


</div>


{{Top}}


```python
def getpoint(self, event_cb):
```


<div class="mw-translate-fuzzy">

Ora definiamo la funzione getpoint, che sarà eseguita quando un pulsante del mouse verrà premuto in una vista 3D. Questa funzione riceverà un argomento, che chiamiamo event_cb.

Da questo evento callback possiamo accedere all\'oggetto event, che contiene diverse parti di informazioni

Per maggiori informazioni sugli eventi controllabili consultate [questa pagina](Code_snippets/it#Observing_mouse_events_in_the_3D_viewer_via_Python.md).


</div>


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```


<div class="mw-translate-fuzzy">

La funzione getpoint viene chiamata ogni volta che un pulsante del mouse viene premuto o rilasciato. Invece, noi vogliamo definire un punto 3D solo quando viene premuto (altrimenti otteniamo due punti 3D molto vicini l\'uno all\'altro). Pertanto quì dobbiamo verificare e stabilire questo.


</div>


```python
pos = event.getPosition()
```


<div class="mw-translate-fuzzy">

Qui otteniamo le coordinate dello schermo nella posizione del cursore del mouse


</div>


```python
point = self.view.getPoint(pos[0], pos[1])
```


<div class="mw-translate-fuzzy">

Questa funzione ci fornisce un vettore di FreeCAD (x, y, z) contenente il punto 3D che giace sul piano focale, esattamente sotto il cursore del mouse. Se siamo in vista camera, immaginiamo un raggio proveniente dalla fotocamera, passante per il cursore del mouse, che colpisce il piano focale. Questo è il nostro punto 3D. Se siamo in vista ortogonale, il raggio è parallelo alla direzione di visualizzazione.


</div>


```python
self.stack.append(point)
```


<div class="mw-translate-fuzzy">

Aggiungiamo il nostro nuovo punto nella pila (stack)


</div>


```python
if len(self.stack) == 2:
```

Abbiamo già abbastanza punti? Se sì, allora disegnamo la linea!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```


<div class="mw-translate-fuzzy">

Qui usiamo la funzione Line() del [Modulo Parte](Part_Workbench/it.md) che crea una linea da due vettori di FreeCAD.

Tutto quanto che si crea e si modifica all\'interno del modulo Parte, rimane nel modulo Parte. Quindi, fino ad ora, abbiamo creato una linea Parte. Essa non è legata ad alcun oggetto del nostro documento attivo, perciò sullo schermo non viene ancora visualizzato nulla.


</div>


```python
shape = l.toShape()
```


<div class="mw-translate-fuzzy">

Il documento di FreeCAD può accettare solo shape (forme) dal modulo Parte. Le shape sono il tipo più generico di forme del modulo Part. Dobbiamo quindi convertire la nostra linea in una shape prima di poterla aggiunge al documento.


</div>


```python
Part.show(shape)
```


<div class="mw-translate-fuzzy">

Il modulo Parte ha una funzione molto utile, show(), che crea un nuovo oggetto nel documento e collega ad esso una shape (forma).

Possiamo anche creare prima un nuovo oggetto nel documento, poi associare manualmente ad esso la shape.


</div>


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


<div class="mw-translate-fuzzy">

Siccome con la nostra linea abbiamo finito, terminiamo il meccanismo di callback, che consuma preziosi cicli di CPU.


</div>


{{Top}}




<div class="mw-translate-fuzzy">

### Test e Utilizzo dello script 

Ora, salviamo il nostro script in qualche posizione in cui l\'interprete Python di FreeCAD possa trovarlo.

Durante l\'importazione dei moduli, l\'interprete punta nei seguenti luoghi: i percorsi di installazione di Python, la directory bin di FreeCAD, e tutte le directory dei moduli FreeCAD. Quindi, la soluzione migliore è quella di creare una nuova directory in una delle FreeCAD [Mod directories](Installing_more_workbenches/it.md), e salvare in essa il nostro script. Per esempio, creiamo una directory \"MyScripts\", e salviamo il nostro script come \"exercise.py\".


</div>

Now let\'s save our script in a folder where the FreeCAD Python interpreter can find it. When importing modules, the interpreter will look in the following places: the Python installation paths, the FreeCAD **bin** folder, and all FreeCAD **Mod** (module) folders. So the best solution is to create a new folder in one of the **Mod** folders. Let\'s create a **MyScripts** folder there and save our script in it as **exercise.py**.


<div class="mw-translate-fuzzy">

Adesso che tutto è pronto, basta avviare FreeCAD, creare un nuovo documento, e, nell\'interprete Python, eseguire:


</div>


```python
import exercise
```


<div class="mw-translate-fuzzy">

Se non viene visualizzato nessun messaggio di errore, significa che il nostro script \"exercise\" è stato caricato.

Ora possiamo controllare il suo contenuto con:


</div>


```python
dir(exercise)
```


<div class="mw-translate-fuzzy">

Il comando dir() è un comando integrato di Python che elenca il contenuto di un modulo. Possiamo vedere che la nostra classe line() è lì, in attesa.

Non rimane che provarla scrivendo:


</div>


```python
'line' in dir(exercise)
```

Now let\'s test it:


```python
exercise.line()
```


<div class="mw-translate-fuzzy">

Poi, clicchiamo due volte nella vista 3D, e bingo, ecco la nostra linea! Per farne una nuova, basta riscrivere ancora exercise.line(), e ancora, e ancora \... Siete contenti, no?


</div>


{{Top}}




<div class="mw-translate-fuzzy">

### Includere lo script nell\'interfaccia di FreeCAD 

Per essere davvero efficace il nostro nuovo strumento linea (line) dovrebbe avere un suo pulsante sull\'interfaccia, in modo da non dover digitare ogni volta tutte queste cose.

Il modo più semplice è quello di trasformare la nostra nuova directory MyScripts in un ambiente di lavoro completo di FreeCAD.

È facile. Basta solo inserire un file chiamato **InitGui.py** nella directory MyScripts. Il file InitGui.py conterrà le istruzioni per creare un nuovo ambiente di lavoro (workbench), poi aggiungere ad esso il nostro nuovo strumento.

Oltre a questo dobbiamo anche modificare un po\' il nostro codice di exercise, in modo che lo strumento line() sia riconosciuto come un comando ufficiale di FreeCAD.

Cominciamo creando un file InitGui.py, e scriviamo in esso il seguente codice:


</div>

For our new line tool to be really useful, and to avoid having to type all that stuff, it should have a button in the interface. One way to do this is to transform our new **MyScripts** folder into a full FreeCAD workbench. This is easy, all that is needed is to put a file called **InitGui.py** inside the **MyScripts** folder. **InitGui.py** will contain the instructions to create a new workbench, and add our new tool to it. Besides that we will also need to change our exercise code a bit, so the `line()` tool is recognized as an official FreeCAD command. Let\'s start by creating an **InitGui.py** file, and writing the following code in it:


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```


<div class="mw-translate-fuzzy">

A questo punto, penso che dovreste già capire da soli lo script precedente.

Creiamo una nuova classe che chiamiamo MyWorkbench, le diamo un titolo (MenuText), e definiamo una funzione Initialize() che verrà eseguita quando l\'ambiente di lavoro verrà caricato in FreeCAD. In tale funzione, si carica il contenuto del nostro file exercise, e si aggiungono i comandi di FreeCAD contenuti in una lista di comandi.

Dopo, costruiamo una barra degli strumenti denominata \"My Scripts\" a cui assegniamo la nostra lista comandi. Al momento, ovviamente, disponiamo di un solo strumento, quindi la nostra lista dei comandi contiene un solo elemento.

Quando il nostro ambiente di lavoro è pronto, lo aggiungiamo all\'interfaccia principale.


</div>


<div class="mw-translate-fuzzy">

Questo non basta ancora perché un comando di FreeCAD deve essere formattato in un certo modo per poter funzionare. Quindi è necessario modificare un po\' il nostro strumento line().

Ora il nostro nuovo script exercise.py deve essere come questo:


</div>


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```


<div class="mw-translate-fuzzy">

Quì abbiamo trasformato la nostra funzione \_\_init\_\_() in una funzione Activated(), perchè, quando i comandi di FreeCAD vengono eseguiti, essi eseguono automaticamente la funzione Activated().

Inoltre, abbiamo aggiunto una funzione GetResources(), che fornisce a FreeCAD le informazioni per trovare l\'icona dello strumento, il nome e la descrizione (tooltip) del nostro strumento.

Qualunque immagine jpg, png o svg può fungere da icona, essa può essere di qualsiasi dimensione, ma è meglio usare una dimensione vicina all\'aspetto finale, come, ad esempio, 16x16, 24x24 o 32x32.

Poi, abbiamo aggiunto la classe line() come un comando ufficiale di FreeCAD con il metodo AddCommand().


</div>


<div class="mw-translate-fuzzy">

Questo è tutto, ora basta riavviare FreeCAD e avremo un bell\'ambiente di lavoro con il nostro nuovo strumento line()!


</div>


{{Top}}



### Cosa si può aggiungere? 


<div class="mw-translate-fuzzy">

Se questo esercizio vi è piaciuto, perché non cercare di migliorare questo piccolo strumento? Si possono fare molte cose, come ad esempio:

-   Aggiungere assistenza per gli utenti: fino ad ora abbiamo fatto uno strumento molto spoglio, l\'utente potrebbe essere un po\' disorientato quando lo utilizza. Perciò si potrebbe aggiungere qualche informazione, che suggerisca come procedere. Ad esempio, si potrebbero mostrare dei messaggi nella console di FreeCAD. In merito, visita il modulo FreeCAD.Console
-   Aggiungere la possibilità di digitare manualmente le coordinate dei punti 3D. Guarda la funzione input() di Python, per esempio
-   Aggiungere la possibilità di definire più di 2 punti
-   Aggiungere controlli per altri eventi. Al momento verifichiamo solo gli eventi del pulsante del mouse, ma se ​​vogliamo anche fare qualcosa quando il mouse viene spostato oppure visualizzare le coordinate attuali?
-   Assegnare un nome all\'oggetto creato

Non esitate a scrivere le vostre domande o idee nel [forum](http://forum.freecadweb.org/)!


</div>

Don\'t hesitate to ask questions or share ideas on the [forum](https://forum.freecadweb.org/)! {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Line drawing function/it
