# Python scripting tutorial/it
{{TOCright}}

## Introduzione

[Python](https   *//it.wikipedia.org/wiki/Python) è un linguaggio di programmazione relativamente facile da imparare e comprendere. È open-source e multipiattaforma e può essere utilizzato per molti scopi   * da semplici script di shell a programmi molto complessi. Ma il suo utilizzo più diffuso è come linguaggio di scripting incorporato in altre applicazioni. È in questa modalità che viene utilizzato all\'interno di FreeCAD. Dalla [console Python](Python_console/it.md), o con script personalizzati, puoi controllare FreeCAD e fargli eseguire operazioni molto complesse.

Ad esempio, tramite uno script Python, è possibile   *

-   Creare nuovi oggetti
-   Modificare gli oggetti esistenti
-   Modificare la rappresentazione 3D degli oggetti
-   Modificare l\'interfaccia di FreeCAD

Esistono diversi modi per utilizzare Python in FreeCAD   *

-   Dall\'[Interprete Python di FreeCAD](FreeCAD_Scripting_Basics/it.md), dove puoi inviare comandi in un\'interfaccia in stile \"riga di comando\".
-   Con le [macro](macros/it.md), che sono un modo conveniente per aggiungere rapidamente uno strumento mancante all\'interfaccia di FreeCAD.
-   Da script esterni, che possono essere utilizzati per creare soluzioni abbastanza complesse, anche interi [Ambienti di Lavoro](Workbenches/it.md).

In questo tutorial, lavoreremo su un paio di esempi di base per consentire a tutti di iniziare, ma in questo wiki è disponibile anche molta altra [documentazione sugli script Python](Power_users_hub/it.md). Per chi non conosce ancora Python, ma è interessato a capire come funziona, c\'è anche una [Introduzione a Python](Introduction_to_Python/it.md) per una formazione di base.

Prima di procedere con lo scripting Python, vai su **Modifica → Preferenze → Generale → Finestra di output** e seleziona due caselle   *

-    **Reindirizza l'output interno di Python alla finestra di report**.

-    **Reindirizza gli errori interni di Python alla finestra di rapporto**.

Quindi vai su **Visualizza → Panelli** e seleziona   *

-    **Report**.

## Scrivere codice Python 

Ci sono due modi per scrivere codice Python in FreeCAD. Nella [console Python](Python_console/it.md) (selezionare **Visualizza → Pannelli → Console Python** dal menu) o nell\'[editor delle Macro](Std_DlgMacroExecute/it.md) (selezionare **Macro → Macro...** dal menu). Nella console si scrivono i comandi Python uno per uno, e li si eseguono premendo **Enter**, mentre le macro possono contenere codice più complesso formato da più righe, eseguito solo quando la macro viene eseguita.

![](images/Screenshot_pythoninterpreter.jpg ) 
*la console Python di FreeCAD*

In questo tutorial puoi usare entrambi i metodi. Puoi copiare e incollare ogni riga nella console Python e quindi premere **Enter**, oppure copiare e incollare l\'intero codice in una nuova finestra Macro. {{Top}}

## Esplorare FreeCAD 

Iniziamo creando un nuovo documento vuoto   *


```python
doc = FreeCAD.newDocument()
```

Se lo si digita nella console Python di FreeCAD, noterai che non appena digiti `FreeCAD.` si apre una finestra, che consente di completare automaticamente il resto della riga. Ancora meglio, ogni voce nell\'elenco di completamento automatico ha un suggerimento che spiega cosa fa. Ciò semplifica l\'esplorazione delle funzionalità disponibili. Prima di scegliere `newDocument`, dai un\'occhiata alle altre opzioni.

![](images/Screenshot_classbrowser.jpg ) 
*Il meccanismo di completamento automatico della console Python di FreeCAD*

Ora verrà creato il nostro nuovo documento. Questo equivale alla pressione del pulsante **<img src="images/Std_New.svg" width=16px> [Std New](Std_New.md)** sulla barra degli strumenti. In effetti, la maggior parte dei pulsanti in FreeCAD non fa altro che eseguire una o più righe di codice Python. Ancora meglio, puoi impostare un\'opzione in **Modifica → Preferenze → Generali → Macro** su **Mostra lo scritp dei comandi nella console python**. Questo visualizzerà nella console tutto il codice Python che viene eseguito quando si premono i vari pulsanti. Ciò è molto utile per imparare a riprodurre azioni in Python.

Ora torniamo al nostro documento e vediamo cosa ci puoi fare   *


```python
doc.
```

Esploriamo le opzioni disponibili.

Di solito i nomi che iniziano con la lettera maiuscola sono attributi e contengono un valore, mentre i nomi che iniziano con la lettera minuscola sono funzioni (chiamate anche metodi) e \"fanno qualcosa\".

I nomi che iniziano con un carattere di sottolineatura di solito sono lì per il funzionamento interno del modulo e non dobbiamo preoccuparci di loro.

Usiamo ora uno dei metodi per aggiungere un nuovo oggetto al nostro documento   *


```python
box = doc.addObject("Part   *   *Box", "myBox")
```

Non succede nulla. Perché? Perché FreeCAD è pensato per realizzare lavori molto complessi. In futuro, lavorerà con centinaia di oggetti complessi, tutti dipendenti l\'uno dall\'altro. Apportare una piccola modifica da qualche parte potrebbe avere un grande impatto; potrebbe essere necessario ricalcolare l\'intero documento, operazione che potrebbe richiedere molto tempo. Per questo motivo, quasi nessun comando aggiorna la scena automaticamente. È necessario farlo manualmente   *


```python
doc.recompute()
```

Ora il box è apparso. Molti dei pulsanti che aggiungono oggetti in FreeCAD in realtà fanno due cose   * aggiungere l\'oggetto, e ricalcolare. Se l\'opzione **mostra lo script dei comandi nella console Python** di cui sopra è attivata, provate ad aggiungere una sfera con il pulsante della GUI e vedrete le due righe di codice Python che vengono eseguite una dopo l\'altra.

Ora esploriamo le caratteristiche del nostro box   *


```python
box.
```

Si possono vedere subito un paio di cose molto interessanti quali   *


```python
box.Height
```

Questo comando stampa l\'altezza corrente del nostro box. Ora proviamo a cambiarla   *


```python
box.Height = 5
```

Se selezioni la tua casella con il mouse, vedrai che nel [pannello delle proprietà](Property_editor/it.md), nella scheda **Data**, appare la nostra proprietà **Height**. Tutte le proprietà di un oggetto FreeCAD che appaiono lì (e anche nella scheda **View**, di cui parleremo più avanti), sono direttamente accessibili anche in Python, con i loro nomi, come abbiamo fatto con **Height ** proprietà. Prova a cambiare le altre dimensioni della scatola. {{Top}}

## Vettori e posizionamenti 

I [vettori](http   *//it.wikipedia.org/wiki/Vettore_%28matematica%29) sono un concetto fondamentale in qualsiasi applicazione 3D. Si tratta di un elenco di 3 numeri (x, y, z) che descrivono un punto o una posizione nello spazio 3D. Con i vettori si possono eseguire diverse operazioni, ad esempio, sommarli, sottrarli, proiettarli e [molto altro](http   *//it.wikipedia.org/wiki/Spazio_vettoriale). In FreeCAD, con i vettori si lavora in questo modo   *


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Un\'altra caratteristica comune degli oggetti FreeCAD è il loro [posizionamento](Placement/it.md). Ogni oggetto ha una proprietà **Placement**, che contiene **Base** (posizione) e **Rotation** (asse) dell\'oggetto. È facile da manipolare, ad esempio per spostare il nostro oggetto   *


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Prima di continuare, si devono vedere un paio di concetti importanti. {{Top}}

## App e Gui 

FreeCAD è stato progettato in modo da poter essere utilizzato anche senza la sua interfaccia utente, come applicazione a riga di comando. Quasi tutti gli oggetti in FreeCAD sono quindi costituiti da due parti   * un `Object`, il suo componente \"geometrico\", e un `ViewObject`, il suo componente \"visivo\". Quando si lavora in modalità riga di comando, la parte geometrica è presente, ma la parte visiva è disabilitata.

Per illustrare il concetto diamo un\'occhiata al nostro oggetto cubo. Le proprietà geometriche del cubo, come le sue dimensioni, posizione, ecc. sono memorizzate in `Object`. Mentre le sue proprietà visive, come il colore, lo spessore della linea, ecc. sono archiviate in `ViewObject`. Ciò corrisponde alle schede **Dati** e **Vista** nel [pannello Proprietà](Property_editor.md). L\'oggetto di visualizzazione di un oggetto è accessibile in questo modo   *


```python
vo = box.ViewObject
```

Ora puoi anche modificare le proprietà nella scheda **Visualizza**   *


```python
vo.Transparency = 80
vo.hide()
vo.show()
```

Quando si avvia FreeCAD, la console Python carica da subito due moduli di base   * `FreeCAD` e `FreeCADGui` (a cui è possibile accedere anche tramite le loro scorciatoie `App` e ` Gui`). Queste contengono tutti i tipi di funzionalità generiche per lavorare con i documenti e i loro oggetti. Per illustrare questo concetto, si noti che sia `FreeCAD` che `FreeCADGui` contengono un attributo `ActiveDocument`, che è il documento attualmente aperto. `FreeCAD.ActiveDocument` e `FreeCADGui.ActiveDocument` non sono tuttavia lo stesso oggetto. Sono i due componenti di un documento FreeCAD e contengono attributi e metodi diversi. Ad esempio, `FreeCADGui.ActiveDocument` contiene `ActiveView`, che è la [vista 3D](3D_view/it.md) attualmente aperta. {{Top}}

## Moduli

Il vero potere di FreeCAD risiede nei suoi moduli, con i rispettivi ambienti di lavoro. L\'applicazione di base di FreeCAD è più o meno un contenitore vuoto. Senza i suoi moduli può fare poco più che creare nuovi documenti vuoti. Ogni modulo non solo aggiunge nuovi ambienti di lavoro all\'interfaccia, ma anche nuovi comandi Python e nuovi tipi di oggetti. Di conseguenza, nello stesso documento possono coesistere diversi tipi di oggetti, anche totalmente incompatibili. I moduli più importanti di FreeCAD che esamineremo in questo tutorial sono   * [Part](Part_Workbench/it.md), [Mesh](Mesh_Workbench/it.md), [Sketcher](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md).

[Sketcher](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md) utilizzano entrambi il modulo [Part](Part_Workbench/it.md) per creare e gestire la loro geometria. Mentre [Mesh](Mesh_Workbench/it.md) è totalmente indipendente e gestisce i propri oggetti. Maggiori informazioni di seguito.

È possibile sapere quali tipi di oggetti di base sono disponibili per il documento corrente in questo modo   *


```python
doc.supportedTypes()
```

I diversi moduli di FreeCAD non vengono caricati automaticamente nella console Python. Questo per evitare un avvio molto lento. I moduli vengono caricati solo quando ne hai bisogno. Quindi, ad esempio, per esplorare cosa c\'è all\'interno del modulo Parte   *


```python
import Part
Part.
```

Ma parleremo più avanti del modulo Parte. {{Top}}

## Modulo Mesh 

I [Mesh](https   *//it.wikipedia.org/wiki/Mesh_poligonale) sono un tipo molto semplice di oggetto 3D, utilizzato ad esempio da [Sketchup](https   *//it.wikipedia.org/wiki/SketchUp), [Blender](https   *//it.wikipedia.org/wiki/Blender_(programma)) e [3D Studio Max](https   *//it.wikipedia.org/wiki/3ds_Max). Sono composti da 3 elementi   * punti (detti anche vertici), linee (detti anche spigoli) e facce. In molte applicazioni, incluso FreeCAD, le facce possono avere solo 3 vertici. Naturalmente nulla vieta di avere una faccia più grande composta da diverse facce triangolari complanari.

I Mesh sono semplici, ma proprio perché sono semplici si può facilmente averne milioni in un unico documento. Tuttavia, in FreeCAD hanno un uso minore e sono per lo più presenti per poter importare oggetti in formati mesh (**.stl**, **.obj**) da altre applicazioni. Il modulo Mesh è stato anche ampiamente utilizzato come modulo di test principale nel primo mese di vita di FreeCAD.

Gli oggetti mesh e gli oggetti FreeCAD sono cose diverse. Si può pensare l\'oggetto FreeCAD come un contenitore per un oggetto Mesh (e, come vedremo più avanti, anche per gli oggetti Parte). Quindi, per aggiungere un oggetto mesh in FreeCAD, dobbiamo prima creare un oggetto FreeCAD e un oggetto Mesh, poi aggiungere l\'oggetto Mesh all\'oggetto FreeCAD   *


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh   *   *Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```

Questo è un esempio standard, che utilizza il metodo `createSphere()` per creare automaticamente una sfera, ma si può benissimo creare propri oggetti mesh da uno schizzo, definendo i loro vertici e facce.

Per ulteriori informazioni leggere [ Script per Mesh\...](Mesh_Scripting/it.md) {{Top}}


<div class="mw-translate-fuzzy">

## Parte

Il [Modulo Parte](Part_Workbench/it.md) è il modulo più potente di tutto FreeCAD. Permette di creare e manipolare oggetti [BRep](http   *//it.wikipedia.org/wiki/B-Rep). Gli oggetti di questo tipo, a differenza dei mesh, possono avere un\'ampia varietà di componenti.

In breve, **BRep** significa Boundary Representation. Questo significa che essi sono definiti dalle loro superfici, che racchiudono e definiscono un volume interno. Queste superfici possono essere varie cose, come facce piane o superfici NURBS molto complesse. Essi inoltre incorporano il concetto di volume.


</div>

The [Part](Part_Workbench.md) module is the most powerful module in the whole of FreeCAD. It allows you to create and manipulate [BRep](https   *//en.wikipedia.org/wiki/Boundary_representation) objects. BREP stands for \"Boundary Representation\". A BREP object is defined by surfaces that enclose and define an inner volume. Unlike meshes, BREP objects can have a wide variety of components from planar faces to very complex NURBS surfaces.


<div class="mw-translate-fuzzy">

Il modulo Parte si basa sulla potente libreria [OpenCasCade](http   *//it.wikipedia.org/wiki/Open_CASCADE_Technology), che permette di eseguire facilmente sugli oggetti una vasta gamma di operazioni complesse, come le operazioni booleane, gli arrotondamenti, loft, ecc ..


</div>

Il modulo Parte funziona allo stesso modo del modulo Mesh   * Si crea un oggetto FreeCAD, un oggetto Parte, quindi si aggiunge l\'oggetto Parte all\'oggetto FreeCAD   *


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part   *   *Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```


<div class="mw-translate-fuzzy">

Il modulo Parte (come il modulo Mesh) ha anche un comando veloce che crea automaticamente un oggetto FreeCAD e gli attribuisce una forma, in questo modo è possibile accorciare le 3 ultime righe dell\'esempio precedente con   *


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

Il [Modulo Draft](Draft_Workbench/it.md) aggiunge un paio di tipi di oggetti 2D parametrici (che sono tutti oggetti di Parte) quali linee e cerchi, e fornisce anche alcune funzioni generiche che funzionano non solo sugli oggetti creati con Draft, ma su qualsiasi oggetto Parte. Per esplorare ciò che è disponibile, fare semplicemente   *


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

L\'interfaccia utente di FreeCAD è realizzata con [Qt](http   *//it.wikipedia.org/wiki/Qt_%28toolkit%29), un potente sistema di interfaccia grafica, responsabile del disegno e della gestione di tutti i comandi, dei menu, delle barre degli strumenti e dei pulsanti per la vista 3D.

Qt offre un modulo, chiamato PySide, che consente a Python di accedere e modificare le interfacce Qt, come quella di FreeCAD.

Proviamo a giocherellare con l\'interfaccia Qt e produrre una semplice finestra di dialogo   *


</div>

The FreeCAD user interface is made with [Qt](https   *//en.wikipedia.org/wiki/Qt_(software)), a powerful graphical interface system, responsible for drawing and handling all the controls, menus, toolbars and buttons around the [3D view](3D_view.md). Qt provides a module, [PySide](PySide.md), which allows Python to access and modify Qt interfaces such as FreeCAD\'s. Let\'s try to fiddle with the Qt interface and produce a simple dialog   *


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




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Python scripting tutorial/it
