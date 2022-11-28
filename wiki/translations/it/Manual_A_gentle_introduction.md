# Manual:A gentle introduction/it
<div class="mw-translate-fuzzy">





</div>


{{Manual   *TOC/it}}

[Python](https   *//en.wikipedia.org/wiki/Python_%28programming_language%29) è un linguaggio di programmazione open source, ampiamente popolare, molto spesso incorporato in una applicazione come script, come nel caso di FreeCAD. Esso ha una serie di caratteristiche che lo rendono particolarmente interessante per gli utenti di FreeCAD   * È molto facile da imparare, specialmente per le persone che non hanno mai programmato prima, ed è incorporato in molte altre applicazioni, il che lo rende un prezioso strumento da conoscere, e poi essere in grado di usarlo in molte altre applicazioni, come ad esempio [Blender](http   *//www.blender.org), [Inkscape](http   *//www.inkscape.org) o [GRASS](http   *//grass.osgeo.org/).

FreeCAD fa un ampio uso di Python. Con esso, è possibile accedere e controllare praticamente qualsiasi funzione di FreeCAD. È possibile ad esempio creare dei nuovi oggetti, modificare la loro geometria, analizzare il loro contenuto, o addirittura creare nuovi comandi, strumenti e pannelli per l\'interfaccia. Alcuni ambienti di FreeCAD e la maggior parte degli ambienti addon sono completamente programmati in Python. FreeCAD ha una console Python avanzata, disponibile dal menù **Visualizza-\>Pannelli-\>Console Python**. Spesso è utile per eseguire operazioni per le quali non vi è ancora alcun pulsante nella barra degli strumenti, o per verificare le forme che danno problemi, o per eseguire delle operazioni ripetitive   *

![](images/Exercise_python_01.jpg )


<div class="mw-translate-fuzzy">

Ma la console Python ha anche un altro uso molto importante   * Ogni volta che si preme un pulsante della barra degli strumenti, o si eseguono altre operazioni in FreeCAD, un po\' di codice Python viene stampato nella console ed eseguito. Lasciando la console Python aperta, è possibile letteralmente vedere il codice python svolgersi mentre si lavora, e in poco tempo, quasi inconsapevolmente, si impara un po\' di linguaggio Python.


</div>

FreeCAD ha anche un [sistema di macro](Macros/it.md), che permette di registrare le azioni per poterle riprodurre in un momento successivo. Anche questo sistema utilizza la console Python, registrando semplicemente in essa tutto ciò che viene fatto.

In questo capitolo, scopriremo molto in generale il linguaggio Python. Se siete interessati a saperne di più, il wiki della documentazione di FreeCAD ha una vasta sezione relativa alla [programmazione in Python](Power_users_hub/it.md).

### Scrivere del codice Python 


<div class="mw-translate-fuzzy">

Ci sono due semplici modi per scrivere del codice Python in FreeCAD   * dalla console Python (menu **Visualizza -\> Pannelli -\> Console Python**), o dall\'editor delle Macro (menu **Strumenti -\> Macro -\> Nuova**). Nella console, si scrivono i comandi Python uno per uno, e essi vengono eseguiti quando si preme Invio, mentre la macro può contenere uno script più complesso fatto di diverse righe, e viene eseguita solo quando la macro viene lanciata dalla stessa finestra Macro.


</div>

In questo capitolo, si descrive come utilizzare entrambi i metodi, ma si consiglia vivamente di utilizzare la console Python, perché essa informa immediatamente l\'utente sugli eventuali errori che si possono fare durante la digitazione.

Se questa è la prima volta che si sta usando Python, prendere in considerazione la lettura di questa breve [introduzione a Python programming](Introduction_to_Python/it.md) prima di andare avanti, renderà più chiari i concetti di base di Python.

### Manipolare gli oggetti di FreeCAD 

Cominciamo creando un nuovo documento vuoto   *

doc = FreeCAD.newDocument()

Se si digita questo nella console Python di FreeCAD, si noterà che non appena si digita \"FreeCAD.\" (la parola FreeCAD seguita da un punto), si apre una finestra pop-up che permette di completare automaticamente e velocemente il resto della riga. In più, ogni voce dell\'elenco di completamento automatico ha un tooltip che spiega quello che fa. Questo rende molto facile esplorare le funzionalità disponibili. Prima di scegliere \"newDocument\", dare un\'occhiata alle altre opzioni disponibili.

![](images/Exercise_python_02.jpg )

Non appena si preme **Enter** viene creato il nuovo documento. Questo è simile a premere il pulsante \"nuovo documento\" sulla barra degli strumenti. In Python, il punto viene utilizzato per indicare qualcosa che è contenuto all\'interno di qualcos\'altro (newDocument è una funzione che si trova all\'interno del modulo FreeCAD). La finestra che si apre, pertanto mostra tutto ciò che è contenuto all\'interno di \"FreeCAD\". Se si aggiungesse un punto dopo newDocument, al posto delle parentesi, verrebbe mostrato tutto quello che è contenuto all\'interno della funzione newDocument. Le parentesi sono obbligatorie quando si chiama una funzione Python, come nel caso di prima. In seguito illustreremo meglio questo.

Ora torniamo al nostro documento. Vediamo cosa possiamo fare con esso. Digitare quanto segue ed esplorare le opzioni disponibili   *

doc.

Di solito i nomi che iniziano con una lettera maiuscola sono attributi, che contengono un valore, mentre i nomi che iniziano con la lettera minuscola sono funzioni (chiamate anche metodi), che \"fanno qualcosa\". I nomi che iniziano con un carattere di sottolineatura di solito servono per l\'uso interno del modulo, e non è necessario preoccuparsene. Usiamo uno dei metodi per aggiungere un nuovo oggetto al nostro documento   *

box = doc.addObject("Part   *   *Box","myBox")

Nella vista ad albero viene aggiunto un cubo, ma nella vista 3D non succede ancora nulla, perché quando si lavora da Python, il documento non viene mai ricompilato automaticamente. Dobbiamo farlo manualmente, ogni volta che serve   *

doc.recompute()


<div class="mw-translate-fuzzy">

Ora nella vista 3D è apparso il cubo. Molti dei pulsanti della barra degli strumenti che aggiungono oggetti in FreeCAD in effetti fanno due cose   * aggiungono l\'oggetto, e ricalcolano. Se la casella \"Mostra i comandi di script nella console Python\" descritta in precedenza è attiva, provate ad aggiungere una sfera con l\'apposito pulsante dell\'ambiente Parte, e vedrete le due righe di codice Python eseguite una dopo l\'altra.


</div>

È possibile ottenere un elenco di tutti i possibili tipi di oggetti come Part   *   *Box   *

doc.supportedTypes()

Ora esploriamo i contenuti del box   *

box.

Si vedono subito un paio di cose molto interessanti come ad esempio   *

box.Height 

Questo stampa l\'altezza corrente del box. Ora proviamo a cambiare la situazione   *

box.Height = 5 

Se si seleziona il box con il mouse, si vede che nel pannello delle proprietà, sotto la scheda **Dati**, la proprietà **Height** appare con il nuovo valore. Tutte le proprietà di un oggetto FreeCAD che appaiono nelle schede **Dati** e **Vista** sono anche accessibili direttamente con Python, tramite i loro nomi, come abbiamo fatto con la proprietà Height. Le proprietà Dati sono accessibili direttamente dall\'oggetto stesso, ad esempio   *

box.Length 

Le proprietà Vista sono memorizzate all\'interno di un **ViewObject**. Ogni oggetto FreeCAD possiede un ViewObject, che memorizza le proprietà di visualizzazione dell\'oggetto. Quando si esegue FreeCAD senza la sua interfaccia grafica (per esempio quando lo si lancia da un terminale con la linea di comando -c, o usandolo da un altro script Python), il ViewObject non è disponibile, poiché non vi è alcuna visualizzazione.

Provare esempio per accedere al colore della linea del box   *

box.ViewObject.LineColor 

### Vettori e Posizionamento 

I vettori sono un concetto fondamentale in qualsiasi applicazione 3D. Si tratta di un elenco di 3 numeri (x, y e z), che descrivono un punto o una posizione nello spazio 3D. Con i vettori si possono fare un sacco di cose, come addizioni, sottrazioni, proiezioni e molto altro ancora. In FreeCAD i vettori di lavorano in questo modo   *

myvec = FreeCAD.Vector(2,0,0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0,3,0)
sumvec = myvec.add(othervec)

Un\'altra caratteristica comune degli oggetti FreeCAD è la loro **Posizionamento**. Come abbiamo visto nei capitoli precedenti, ogni oggetto ha una proprietà Placement, che contiene la posizione (Base) e l\'orientamento (Rotazione) dell\'oggetto. Con Python è facile manipolare queste proprietà, ad esempio per spostare l\'oggetto   *

print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5,5,0)
box.Placement = otherpla

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [Python](https   *//www.python.org)
-   [Lavorare con le Macro](Macros/it.md)
-   [Introduzione agli script Python](Introduction_to_Python/it.md)
-   [Usare Python in FreeCAD](Python_scripting_tutorial/it.md)
-   [Hub degli script Python](Power_users_hub/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:A gentle introduction/it
