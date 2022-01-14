# Python scripting tutorial/it
<div class="mw-translate-fuzzy">


{{docnav/it|[Introduzione a Python](Introduction_to_Python/it.md)|[Basi di Script in FreeCAD](FreeCAD_Scripting_Basics/it.md)}}


</div>


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Python](http://it.wikipedia.org/wiki/Python) è un linguaggio di programmazione, molto semplice da usare e molto veloce da imparare.

È open-source, multi-piattaforma, e può essere usato da solo per una vasta gamma di cose, sia per semplici script che per programmi molto complessi.

Uno dei suoi usi più frequenti è sicuramente come linguaggio di script poiché è facile da incorporare in altre applicazioni. Questo è esattamente il modo in cui viene utilizzato all\'interno di FreeCAD.

Dalla console di Python, o tramite script personali, è possibile pilotare FreeCAD e fargli eseguire azioni molto complesse per le quali non esiste ancora lo strumento per l\'interfaccia grafica utente.


</div>


<div class="mw-translate-fuzzy">

Ad esempio, tramite uno script Python, è possibile:

-   creare nuovi oggetti
-   modificare gli oggetti esistenti
-   modificare la rappresentazione 3D degli oggetti
-   modificare l\'interfaccia di FreeCAD


</div>


<div class="mw-translate-fuzzy">

Ci sono anche altri modi per utilizzare Python in FreeCAD:

-   Tramite [l\'Interprete di Python in FreeCAD](FreeCAD_Scripting_Basics/it.md), dove è possibile inviare semplici comandi come si fa in una interfaccia di tipo \"linea di comando\"
-   Tramite le [macro](macros/it.md), che sono un modo pratico per aggiungere rapidamente all\'interfaccia di FreeCAD uno strumento mancante
-   Tramite degli script esterni, che possono essere utilizzati per programmare le cose molto complesse, ad esempio, creare completi [Ambienti di lavoro](Workbenches/it.md).


</div>


<div class="mw-translate-fuzzy">

In questo tutorial, lavoreremo su un paio di esempi semplici per consentire a tutti di iniziare, ma in questo wiki è disponibile anche molta altra [documentazione sugli script Python](Power_users_hub/it.md).

Per chi non conosce ancora Python, ma è interessato a capire come funziona, c\'è anche una [Introduzione a Python](Introduction_to_Python/it.md) per una formazione di base.


</div>


<div class="mw-translate-fuzzy">

**Importante!** Prima di iniziare gli esercizi di script Python, andare nel menu Modifica → Preferenze → Generali → Finestra di Output e attivare queste due caselle:

-   Reindirizzare l\'output interno di Python nella vista report
-   Reindirizzare gli errori interni di Python alla finestra di report

Poi dal menu principale andare in Visualizza → Pannelli e attivare:

-   Report

Questo vi farà risparmiare molti problemi!


</div>


<div class="mw-translate-fuzzy">

## Scrivere un codice Python 

In FreeCAD, ci sono due modi semplici per scrivere un codice Python: Tramite la console di Python (disponibile con Visualizza → Pannelli → Console Python) oppure tramite l\'editor delle Macro (Strumenti → Macro).

Nella console, si scrivono i comandi Python uno per uno (riga per riga), e questi vengono eseguiti quando si preme Invio, mentre le macro possono contenere uno script più complesso fatto di diverse righe, e i comandi vengono eseguiti solo quando viene eseguita la macro.


</div>

There are two ways to write Python code in FreeCAD. In the [Python console](Python_console.md) (select **View → Panels → Python console** from the menu) or in the [Macro editor](Std_DlgMacroExecute.md) (select **Macro → Macros...** from the menu). In the console you write Python commands one by one, executing them by pressing **Enter**, while macros can contain more complex code made up of several lines, executed only when the macro is executed.

![](images/Screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

![La console di Python in FreeCAD](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

In questo tutorial si utilizzeranno entrambi i metodi, sia il copia/incolla di ogni riga, una per una, nella console Python seguito da **Invio** dopo ogni riga, sia il copia/incolla dell\'intero codice in una nuova finestra Macro.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Esplorare FreeCAD 

Iniziamo creando un nuovo documento vuoto:


</div>

Let\'s start by creating a new empty document:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

Quando si digita questo nella console Python di FreeCAD si nota che, non appena si digita \"FreeCAD\", si apre una finestra che consente di auto-completare rapidamente il resto della riga.

In più, ogni voce dell\'elenco di completamento automatico possiede un testo di aiuto che la descrive. Questo rende molto facile esplorare le funzionalità disponibili.

Prima di scegliere \"newDocument\", date un\'occhiata alle altre opzioni disponibili.


</div>

![](images/Screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

![Il sistema di auto-completamento della console Python di FreeCAD](images/Screenshot_classbrowser.jpg )


</div>


<div class="mw-translate-fuzzy">

Ora verrà creato il nostro nuovo documento. Questo equivale alla pressione sul pulsante \"nuovo documento\" della barra degli strumenti.

In effetti, la maggior parte dei pulsanti di FreeCAD non fa altro che eseguire una o due righe di codice Python.

Meglio ancora, in Modifica → Preferenze → Generale → Macro è possibile attivare l\'opzione \"mostra lo script dei comandi nella console Python\". Questo visualizzerà nella console tutto il codice Python che viene eseguito quando si premono i vari pulsanti. E\' molto utile per imparare a riprodurre le azioni in codice Python.


</div>


<div class="mw-translate-fuzzy">

Ora torniamo al nostro documento. Vediamo cosa possiamo fare con esso:


</div>


```python
doc.
```


<div class="mw-translate-fuzzy">

Esploriamo le opzioni disponibili.

Di solito i nomi che iniziano con la lettera maiuscola sono attributi e contengono un valore, mentre i nomi che iniziano con la lettera minuscola sono funzioni (chiamate anche metodi) e \"fanno qualcosa\".

I nomi che iniziano con un carattere di sottolineatura di solito sono lì per il funzionamento interno del modulo e non dobbiamo preoccuparci di loro.

Usiamo ora uno dei metodi per aggiungere un nuovo oggetto al nostro documento:


</div>


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

Non succede nulla. Perché? Perché FreeCAD è pensato per realizzare lavori molto complessi.

In futuro, lavorerà con centinaia di oggetti complessi, tutti dipendenti l\'uno dall\'altro.

Apportare una piccola modifica da qualche parte potrebbe avere un grande impatto, potrebbe essere necessario ricalcolare l\'intero documento, operazione che potrebbe richiedere molto tempo \... Per questo motivo, quasi nessun comando aggiorna la scena automaticamente. È necessario farlo manualmente:


</div>


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

Visto? Ora il box è apparso! Molti dei pulsanti che aggiungono oggetti in FreeCAD in realtà fanno 2 cose: aggiungere l\'oggetto, e ricalcolare.

Se l\'opzione \"mostra lo script dei comandi nella console Python\" di cui sopra è attivata, provate ad aggiungere una sfera con il pulsante della GUI e vedrete le due righe di codice python che vengono eseguite una dopo l\'altra.


</div>

Ora esploriamo le caratteristiche del nostro box:


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


<div class="mw-translate-fuzzy">

Se selezionamo il box con il mouse, nella scheda \"Dati\", del pannello delle proprietà, ora appare il valore della nostra proprietà \"Altezza\".

Tutte le proprietà di un oggetto di FreeCAD che appaiono qui (e anche nella scheda \"Vista\", di cui parleremo più avanti), sono anche accessibili direttamente tramite Python, tramite i loro nomi, come abbiamo fatto con la proprietà \"Altezza\".

Provate a cambiare le altre dimensioni del box.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Vettori e posizionamenti 

I [vettori](http://it.wikipedia.org/wiki/Vettore_%28matematica%29) sono un concetto fondamentale in qualsiasi applicazione 3D. Si tratta di un elenco di 3 numeri (x, y, z) che descrivono un punto o una posizione nello spazio 3D.

Con i vettori si possono eseguire diverse operazioni, ad esempio, sommarli, sottrarli, proiettarli e [molto altro](http://it.wikipedia.org/wiki/Spazio_vettoriale).

In FreeCAD, con i vettori si lavora in questo modo:


</div>

[Vectors](https://en.wikipedia.org/wiki/Euclidean_vector) are a very fundamental concept in any 3D application. A vector is a list of 3 numbers (x, y and z), describing a point or position in 3D space. Many things can be done with vectors, such as additions, subtractions, projections and [much more](https://en.wikipedia.org/wiki/Vector_space). In FreeCAD vectors work like this:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```


<div class="mw-translate-fuzzy">

Un\'altra caratteristica comune degli oggetti FreeCAD è la loro [**collocazione**](Tasks_Placement/it.md) nello spazio, (accessibile dalla scheda **Vista combinata → Proprietà → Dati → Placement**, <img alt="Tache\_Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">, oppure tramite il menu *\' Modifica → Posizionamento\...*\').

Ogni oggetto possiede alcuni attributi di posizionamento, che contengono la posizione (Base) e l\'orientamento (Rotation) dell\'oggetto. Questi attributi si manipolano facilmente, ad esempio, per spostare il nostro oggetto:


</div>


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Prima di continuare, si devono vedere un paio di concetti importanti. {{Top}}


<div class="mw-translate-fuzzy">

## App e Gui 

FreeCAD è stato inizialmente creato per lavorare come applicazione a riga di comando, senza la sua attuale interfaccia utente. Di conseguenza, quasi tutto viene separato in una componente \"geometria\" e una componente \"vista\".

Quando si lavora in modalità riga di comando, la parte geometria è presente, ma tutta la parte di visualizzazione è semplicemente disabilitata. Quindi, in FreeCAD, quasi tutti gli oggetti si compongono di due parti, una parte Object e una parte ViewObject.


</div>

FreeCAD has been designed so that it can also be used without its user interface, as a command-line application. Almost every object in FreeCAD therefore consists of two parts: an `Object`, its \"geometry\" component, and a `ViewObject`, its \"visual\" component. When you work in command-line mode, the geometry part is present, but the visual part is disabled.


<div class="mw-translate-fuzzy">

Per illustrare il concetto, consideriamo il nostro oggetto cubo, le proprietà geometriche del cubo, come ad esempio le sue dimensioni, posizione, ecc .. sono memorizzate in Object, mentre le sue proprietà di visualizzazione, come il suo colore, spessore della linea, ecc .. sono memorizzati in ViewObject. Ciò corrisponde alle schede \"Dati\" e \"Vista\" nella finestra delle proprietà.

Alla parte ViewObject di un oggetto si accede in questo modo:


</div>


```python
vo = box.ViewObject
```


<div class="mw-translate-fuzzy">

Ora è anche possibile modificare le proprietà della scheda \"Vista\":


</div>


```python
vo.Transparency = 80
vo.hide()
vo.show()
```


<div class="mw-translate-fuzzy">

Quando si avvia FreeCAD, la console python carica 2 moduli base: FreeCAD e FreeCADGui (a cui si può accedere anche dai collegamenti App e Gui). Essi contengono tutti i tipi di funzionalità generiche per lavorare con i documenti ed i loro oggetti.

Per illustrare questo concetto: notare che FreeCAD e FreeCADGui contengono entrambi un attributo ActiveDocument, che è il documento attualmente aperto.

FreeCAD.ActiveDocument e FreeCADGui.ActiveDocument non sono la stessa cosa. Essi sono i due componenti di un documento FreeCAD, e contengono attributi e metodi diversi. Ad esempio, FreeCADGui.ActiveDocument contiene ActiveView che è la vista 3D attualmente attiva.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Moduli

Ora vi starete sicuramente chiedendo che cosa si possa ancora fare con \"Part:: Box\".

L\'applicazione di base di FreeCAD è più o meno un contenitore vuoto. Senza i suoi moduli, può fare poco più che creare nuovi documenti vuoti. La vera potenza di FreeCAD è nei suoi affidabili moduli.

Ogni modulo non solo aggiunge all\'interfaccia nuovi ambienti di lavoro, ma aggiunge anche nuovi comandi Python e nuovi tipi di oggetti. Di conseguenza, nello stesso documento possono coesistere diversi tipi di oggetti, compresi anche oggetti totalmente incompatibili .

I moduli principali di FreeCAD, che vederemo in questo tutorial, sono [Parte](Part_Workbench/it.md), [Mesh](Mesh_Workbench/it.md), [Schizzo](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md).


</div>

The true power of FreeCAD lies in its faithful modules, with their respective workbenches. The FreeCAD base application is more or less an empty container. Without its modules it can do little more than create new, empty documents. Each module not only adds new workbenches to the interface, but also new Python commands and new object types. As a result several different, and even totally incompatible, object types can coexist in the same document. The most important modules in FreeCAD that we\'ll look at in this tutorial are: [Part](Part_Workbench.md), [Mesh](Mesh_Workbench.md), [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md).


<div class="mw-translate-fuzzy">

I moduli [Schizzo](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md) utilizzano entrambi il modulo [Parte](Part_Workbench/it.md) per creare e gestire le loro geometrie, che sono geometrie B-Rep, mentre il modulo [Mesh](Mesh_Workbench/it.md) è totalmente indipendente, e gestisce autonomamente i propri oggetti. In seguito saranno fornite ulteriori informazioni.


</div>

È possibile sapere quali tipi di oggetti di base sono disponibili per il documento corrente in questo modo:


```python
doc.supportedTypes()
```


<div class="mw-translate-fuzzy">

I diversi moduli di FreeCAD, anche se hanno aggiunto a FreeCAD i loro tipi di oggetti, non sono caricati automaticamente nella console Python. Questo per evitare di avere un avvio molto lento. I moduli vengono caricati solo quando servono. Quindi, per esempio, per esplorare l\'interno del modulo Parte:


</div>


```python
import Part
Part.
```

Ma parleremo più avanti del modulo Parte. {{Top}}


<div class="mw-translate-fuzzy">

## Mesh


</div>


<div class="mw-translate-fuzzy">

I [Mesh](http://it.wikipedia.org/wiki/Mesh_poligonale) sono un tipo molto semplice di oggetti 3D, utilizzati ad esempio da [Sketchup](http://it.wikipedia.org/wiki/SketchUp), [Blender](http://it.wikipedia.org/wiki/Blender_%28programma%29) o [3D studio Max](http://it.wikipedia.org/wiki/3D_Studio_Max). Essi sono composti da 3 elementi: i punti (chiamati anche vertici), le linee (chiamate anche bordi) e le facce. In molte applicazioni, inclusa FreeCAD, le facce possono avere solo tre vertici. Naturalmente nulla impedisce di avere una faccia piana più grande composta da diverse facce triangolari complanari.


</div>


<div class="mw-translate-fuzzy">

Gli oggetti mesh (grigliati) sono semplici, ma poiché sono semplici si può facilmente averne a milioni in un unico documento. In FreeCAD sono poco usati, e lo sono per lo più per importare oggetti in formato mesh (.Stl, .Obj) da altre applicazioni. Comunque sono stati ampiamente utilizzati come principale modulo di test nel primo mese di vita di FreeCAD.


</div>

Gli oggetti mesh e gli oggetti FreeCAD sono cose diverse. Si può pensare l\'oggetto FreeCAD come un contenitore per un oggetto Mesh (e, come vedremo più avanti, anche per gli oggetti Parte). Quindi, per aggiungere un oggetto mesh in FreeCAD, dobbiamo prima creare un oggetto FreeCAD e un oggetto Mesh, poi aggiungere l\'oggetto Mesh all\'oggetto FreeCAD:


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```


<div class="mw-translate-fuzzy">

Questo è un esempio standard, che utilizza il metodo createSphere() per creare automaticamente una sfera, ma si può benissimo creare propri oggetti mesh da uno schizzo, definendo i loro vertici e facce.


</div>

Per ulteriori informazioni leggere [ Script per Mesh\...](Mesh_Scripting/it.md) {{Top}}


<div class="mw-translate-fuzzy">

## Parte

Il [Modulo Parte](Part_Workbench/it.md) è il modulo più potente di tutto FreeCAD. Permette di creare e manipolare oggetti [BRep](http://it.wikipedia.org/wiki/B-Rep). Gli oggetti di questo tipo, a differenza dei mesh, possono avere un\'ampia varietà di componenti.

In breve, **BRep** significa Boundary Representation. Questo significa che essi sono definiti dalle loro superfici, che racchiudono e definiscono un volume interno. Queste superfici possono essere varie cose, come facce piane o superfici NURBS molto complesse. Essi inoltre incorporano il concetto di volume.


</div>

The [Part](Part_Workbench.md) module is the most powerful module in the whole of FreeCAD. It allows you to create and manipulate [BRep](https://en.wikipedia.org/wiki/Boundary_representation) objects. BREP stands for \"Boundary Representation\". A BREP object is defined by surfaces that enclose and define an inner volume. Unlike meshes, BREP objects can have a wide variety of components from planar faces to very complex NURBS surfaces.


<div class="mw-translate-fuzzy">

Il modulo Parte si basa sulla potente libreria [OpenCasCade](http://it.wikipedia.org/wiki/Open_CASCADE_Technology), che permette di eseguire facilmente sugli oggetti una vasta gamma di operazioni complesse, come le operazioni booleane, gli arrotondamenti, loft, ecc ..


</div>

Il modulo Parte funziona allo stesso modo del modulo Mesh: Si crea un oggetto FreeCAD, un oggetto Parte, quindi si aggiunge l\'oggetto Parte all\'oggetto FreeCAD:


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```


<div class="mw-translate-fuzzy">

Il modulo Parte (come il modulo Mesh) ha anche un comando veloce che crea automaticamente un oggetto FreeCAD e gli attribuisce una forma, in questo modo è possibile accorciare le 3 ultime righe dell\'esempio precedente con:


</div>


```python
Part.show(myshape)
```


<div class="mw-translate-fuzzy">

Esplorando il contenuto di myShape, noterete che sono disponibili vari sotto-componenti interessanti quali Facce, Bordi, Vertici, Solidi e Superfici, e una vasta gamma di operazioni geometriche come taglio (sottrazione), comune (intersezione) o fusione (unione). La pagina [Script di dati topologici](Topological_data_scripting/it.md) spiega tutto questo in modo dettagliato.


</div>


<div class="mw-translate-fuzzy">

[Approfondimento sugli script in Parte\...](Topological_data_scripting/it.md)


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Draft

FreeCAD offre altri moduli, quali [Schizzo](Sketcher_Workbench/it.md) o [Draft](Draft_Workbench/it.md), che creano anche loro degli oggetti Parte, ma vi aggiungono dei parametri, o usano un modo diverso per gestire la geometria della Parte.

Il box del nostro precedente esempio è un esempio di perfetto oggetto parametrico.

Per definire il box, basta specificare solo pochi parametri, quali altezza, larghezza e lunghezza. Sulla base di questi dati, l\'oggetto calcolerà automaticamente la sua forma Parte. FreeCAD consente di [creare questi oggetti con Python](Scripted_objects/it.md).


</div>

FreeCAD features many more modules, such as [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md), that also create Part objects. These modules add additional parameters to the objects created, or even implement a whole new way to handle the Part geometry in them. Our box example above is a perfect example of a parametric object. All you need to define the box is to specify the parameters height, width and length. Based on those, the object will automatically calculate its Part shape. FreeCAD allows you to [create such objects in Python](Scripted_objects.md).


<div class="mw-translate-fuzzy">

Il [Modulo Draft](Draft_Workbench/it.md) aggiunge un paio di tipi di oggetti 2D parametrici (che sono tutti oggetti di Parte) quali linee e cerchi, e fornisce anche alcune funzioni generiche che funzionano non solo sugli oggetti creati con Draft, ma su qualsiasi oggetto Parte. Per esplorare ciò che è disponibile, fare semplicemente:


</div>


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Interfaccia

L\'interfaccia utente di FreeCAD è realizzata con [Qt](http://it.wikipedia.org/wiki/Qt_%28toolkit%29), un potente sistema di interfaccia grafica, responsabile del disegno e della gestione di tutti i comandi, dei menu, delle barre degli strumenti e dei pulsanti per la vista 3D.

Qt offre un modulo, chiamato PySide, che consente a Python di accedere e modificare le interfacce Qt, come quella di FreeCAD.

Proviamo a giocherellare con l\'interfaccia Qt e produrre una semplice finestra di dialogo:


</div>

The FreeCAD user interface is made with [Qt](https://en.wikipedia.org/wiki/Qt_(software)), a powerful graphical interface system, responsible for drawing and handling all the controls, menus, toolbars and buttons around the [3D view](3D_view.md). Qt provides a module, [PySide](PySide.md), which allows Python to access and modify Qt interfaces such as FreeCAD\'s. Let\'s try to fiddle with the Qt interface and produce a simple dialog:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```


<div class="mw-translate-fuzzy">

Notare che la finestra di dialogo che appare contiene l\'icona di FreeCAD nella sua barra degli strumenti, questo significa che Qt sa che l\'ordine è stato emesso all\'interno dell\'applicazione FreeCAD. Quindi si può con facilità e manipolare direttamente qualsiasi parte dell\'interfaccia di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Qt è un sistema di interfaccia molto potente, che permette di fare cose molto complesse, inoltre dispone anche di vari strumenti molto facili da usare, come il Qt Designer con il quale è possibile progettare graficamente le finestre di dialogo e poi aggiungerle all\'interfaccia di FreeCAD con poche righe di codice Python.


</div>

[Quì si trovano altre informazioni su PySide\...](PySide/it.md) {{Top}}


<div class="mw-translate-fuzzy">

## Macro

Ora che avete una buona conoscenza delle nozioni di base, dove conserviamo i nostri script Python, e come facciamo per eseguirli facilmente in FreeCAD? Per questo vi è un sistema semplice, chiamato [Macro](Macros/it.md).

Una macro è semplicemente uno script Python, che può essere aggiunto a una barra degli strumenti e poi essere lanciato con un semplice clic del mouse.

FreeCAD fornisce un semplice editor di testo (Macro → Macro → Crea) in cui è possibile scrivere o incollare degli script. Terminata la scrittura, il menu Strumenti → Personalizza → Macro permette di definire un pulsante per questo script che può anche essere aggiunto alle barre degli strumenti.


</div>

Now that you have a good understanding of the basics, where are we going to keep our Python scripts, and how are we going to launch them inside FreeCAD? There is an easy mechanism for that, called [Macros](Macros.md). A macro is a Python script that can be added to a toolbar and launched via a mouse click. FreeCAD provides you with a simple text editor (**Macro → Macros... → Create**) where you can write or paste scripts. Once the script is done, use **Tools → Customize... → Macros** to define a button for it that can be added to toolbars.


<div class="mw-translate-fuzzy">

Ora siete pronti per approfondire le conoscenze sull\'uso degli script in FreeCAD.

Dirigetevi al [Centro degli utenti esperti](Power_users_hub/it.md)!


</div>


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav/it|[Introduzione a Python](Introduction_to_Python/it.md)|[Basi di Script in FreeCAD](FreeCAD_Scripting_Basics/it.md)}}


</div>


{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Python scripting tutorial/it
