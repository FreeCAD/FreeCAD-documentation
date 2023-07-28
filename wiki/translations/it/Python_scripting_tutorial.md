# Python scripting tutorial/it
{{TOCright}}



## Introduzione

[Python](https://it.wikipedia.org/wiki/Python) è un linguaggio di programmazione relativamente facile da imparare e comprendere. È open-source e multipiattaforma e può essere utilizzato per molti scopi: da semplici script di shell a programmi molto complessi. Ma il suo utilizzo più diffuso è come linguaggio di scripting incorporato in altre applicazioni. È in questa modalità che viene utilizzato all\'interno di FreeCAD. Dalla [console Python](Python_console/it.md), o con script personalizzati, puoi controllare FreeCAD e fargli eseguire operazioni molto complesse.

Ad esempio, tramite uno script Python, è possibile:

-   Creare nuovi oggetti
-   Modificare gli oggetti esistenti
-   Modificare la rappresentazione 3D degli oggetti
-   Modificare l\'interfaccia di FreeCAD

Esistono diversi modi per utilizzare Python in FreeCAD:

-   Dall\'[Interprete Python di FreeCAD](FreeCAD_Scripting_Basics/it.md), da cui si possono inviare comandi in un\'interfaccia in stile \"riga di comando\".
-   Con le [macro](macros/it.md), che sono un modo conveniente per aggiungere rapidamente uno strumento mancante all\'interfaccia di FreeCAD.
-   Da script esterni, che possono essere utilizzati per creare soluzioni abbastanza complesse, anche interi [Ambienti di Lavoro](Workbenches/it.md).

In questo tutorial, lavoreremo su un paio di esempi di base per consentire a tutti di iniziare, ma in questo wiki è disponibile anche molta altra [documentazione sugli script Python](Power_users_hub/it.md). Per chi ancora non conoscesse Python, ma è interessato a capire come funziona, c\'è anche una [Introduzione a Python](Introduction_to_Python/it.md) per una formazione di base.

Prima di procedere con lo scripting Python, andare su **Modifica → Preferenze → Generale → Finestra di output** e selezionare le due caselle:

-    **Reindirizza l'output interno di Python alla finestra di report**.

-    **Reindirizza gli errori interni di Python alla finestra di rapporto**.

Quindi andare su **Visualizza → Panelli** e selezionare:

-    **Report**.



## Scrivere codice Python 

Ci sono due modi per scrivere codice Python in FreeCAD. Nella [console Python](Python_console/it.md) (selezionare **Visualizza → Pannelli → Console Python** dal menu) o nell\'[editor delle Macro](Std_DlgMacroExecute/it.md) (selezionare **Macro → Macro...** dal menu). Nella console si scrivono i comandi Python uno per uno, e li si eseguono premendo **Enter**, mentre le macro possono contenere codice più complesso formato da più righe, eseguito solo quando la macro viene eseguita.

![](images/Screenshot_pythoninterpreter.jpg ) 
*la console Python di FreeCAD*

In questo tutorial puoi usare entrambi i metodi. Puoi copiare e incollare ogni riga nella console Python e quindi premere 

## Esplorare FreeCAD 

Iniziamo creando un nuovo documento vuoto:


```python
doc = FreeCAD.newDocument()
```

Se lo si digita nella console Python di FreeCAD, si nota che non appena si digita `FreeCAD.` si apre una finestra, che consente di completare automaticamente il resto della riga. Ancora meglio, ogni voce nell\'elenco di completamento automatico ha un suggerimento che spiega cosa fa. Ciò semplifica l\'esplorazione delle funzionalità disponibili. Prima di scegliere `newDocument`, dare un\'occhiata alle altre opzioni.

![](images/Screenshot_classbrowser.jpg ) 
*Il meccanismo di completamento automatico della console Python di FreeCAD*

Ora verrà creato il nostro nuovo documento. Questo equivale alla pressione del pulsante **<img src="images/Std_New.svg" width=16px> [Nuovo](Std_New.md)** sulla barra degli strumenti. In effetti, la maggior parte dei pulsanti in FreeCAD non fa altro che eseguire una o più righe di codice Python. Ancora meglio, si può impostare un\'opzione in **Modifica → Preferenze → Generali → Macro** su **Mostra lo scritp dei comandi nella console python**. Questo visualizzerà nella console tutto il codice Python che viene eseguito quando si premono i vari pulsanti. Ciò è molto utile per imparare a riprodurre azioni in Python.

Ora torniamo al nostro documento e vediamo cosa si può fare:


```python
doc.
```

Esploriamo le opzioni disponibili.

Di solito i nomi che iniziano con la lettera maiuscola sono attributi e contengono un valore, mentre i nomi che iniziano con la lettera minuscola sono funzioni (chiamate anche metodi) e \"fanno qualcosa\".

I nomi che iniziano con un carattere di sottolineatura di solito sono lì per il funzionamento interno del modulo e non dobbiamo preoccuparci di loro.

Usiamo ora uno dei metodi per aggiungere un nuovo oggetto al nostro documento:


```python
box = doc.addObject("Part::Box", "myBox")
```

Non succede nulla. Perché? Perché FreeCAD è pensato per realizzare lavori molto complessi. In futuro, lavorerà con centinaia di oggetti complessi, tutti dipendenti l\'uno dall\'altro. Apportare una piccola modifica da qualche parte potrebbe avere un grande impatto; potrebbe essere necessario ricalcolare l\'intero documento, operazione che potrebbe richiedere molto tempo. Per questo motivo, quasi nessun comando aggiorna la scena automaticamente. È necessario farlo manualmente:


```python
doc.recompute()
```

Ora il box è apparso. Molti dei pulsanti che aggiungono oggetti in FreeCAD in realtà fanno due cose: aggiungere l\'oggetto, e ricalcolare. Se l\'opzione **mostra lo script dei comandi nella console Python** di cui sopra è attivata, provate ad aggiungere una sfera con il pulsante della GUI e vedrete le due righe di codice Python che vengono eseguite una dopo l\'altra.

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

Se si seleziona la casella con il mouse, si nota che nel [pannello delle proprietà](Property_editor/it.md), nella scheda 

## Vettori e posizionamenti 

I [vettori](http://it.wikipedia.org/wiki/Vettore_%28matematica%29) sono un concetto fondamentale in qualsiasi applicazione 3D. Si tratta di un elenco di 3 numeri (x, y, z), che descrivono un punto o una posizione nello spazio 3D. Con i vettori si possono eseguire diverse operazioni, ad esempio, sommarli, sottrarli, proiettarli e [molto altro](http://it.wikipedia.org/wiki/Spazio_vettoriale). In FreeCAD, con i vettori si lavora in questo modo:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Un\'altra caratteristica comune degli oggetti FreeCAD è il loro [posizionamento](Placement/it.md). Ogni oggetto ha una proprietà **Placement**, che contiene **Base** (posizione) e **Rotation** (asse) dell\'oggetto. Sono facili da manipolare, ad esempio per spostare il nostro oggetto:


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Prima di continuare, si devono vedere un paio di concetti importanti. 

## App e Gui 

FreeCAD è stato progettato in modo da poter essere utilizzato anche senza la sua interfaccia utente, come applicazione a riga di comando. Quasi tutti gli oggetti in FreeCAD sono quindi costituiti da due parti: un `Object`, il suo componente \"geometrico\", e un `ViewObject`, il suo componente \"visivo\". Quando si lavora in modalità riga di comando, la parte geometrica è presente, ma la parte visiva è disabilitata.

Per illustrare il concetto diamo un\'occhiata al nostro oggetto cubo. Le proprietà geometriche del cubo, come le sue dimensioni, posizione, ecc. sono memorizzate in `Object`. Mentre le sue proprietà visive, come il colore, lo spessore della linea, ecc. sono archiviate in `ViewObject`. Ciò corrisponde alle schede **Dati** e **Vista** nel [pannello Proprietà](Property_editor/it.md). L\'oggetto di visualizzazione di un oggetto è accessibile in questo modo:


```python
vo = box.ViewObject
```

Ora puoi anche modificare le proprietà nella scheda **Visualizza**:


```python
vo.Transparency = 80
vo.hide()
vo.show()
```

Quando si avvia FreeCAD, la console Python carica da subito due moduli di base: 

## Moduli

Il vero potere di FreeCAD risiede nei suoi moduli, con i rispettivi ambienti di lavoro. L\'applicazione di base di FreeCAD è più o meno un contenitore vuoto. Senza i suoi moduli può fare poco più che creare nuovi documenti vuoti. Ogni modulo non solo aggiunge nuovi ambienti di lavoro all\'interfaccia, ma anche nuovi comandi Python e nuovi tipi di oggetti. Di conseguenza, nello stesso documento possono coesistere diversi tipi di oggetti, anche totalmente incompatibili. I moduli più importanti di FreeCAD che esamineremo in questo tutorial sono: [Part](Part_Workbench/it.md), [Mesh](Mesh_Workbench/it.md), [Sketcher](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md).

[Sketcher](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md) utilizzano entrambi il modulo [Part](Part_Workbench/it.md) per creare e gestire la loro geometria. Mentre [Mesh](Mesh_Workbench/it.md) è totalmente indipendente e gestisce i propri oggetti. Maggiori informazioni di seguito.

È possibile sapere quali tipi di oggetti di base sono disponibili per il documento corrente in questo modo:


```python
doc.supportedTypes()
```

I diversi moduli di FreeCAD non vengono caricati automaticamente nella console Python. Questo per evitare un avvio molto lento. I moduli vengono caricati solo quando ne hai bisogno. Quindi, ad esempio, per esplorare cosa c\'è all\'interno del modulo Parte:


```python
import Part
Part.
```

Ma parleremo più avanti del modulo Parte. 

## Modulo Mesh 

I [Mesh](https://it.wikipedia.org/wiki/Mesh_poligonale) sono un tipo molto semplice di oggetto 3D, utilizzato ad esempio da [Sketchup](https://it.wikipedia.org/wiki/SketchUp), [Blender](https://it.wikipedia.org/wiki/Blender_(programma)) e [3D Studio Max](https://it.wikipedia.org/wiki/3ds_Max). Sono composti da 3 elementi: punti (detti anche vertici), linee (detti anche spigoli) e facce. In molte applicazioni, incluso FreeCAD, le facce possono avere solo 3 vertici. Naturalmente nulla vieta di avere una faccia più grande composta da diverse facce triangolari complanari.

I Mesh sono semplici, ma proprio perché sono semplici si può facilmente averne milioni in un unico documento. Tuttavia, in FreeCAD hanno un uso minore e sono per lo più presenti per poter importare oggetti in formati mesh (**.stl**, **.obj**) da altre applicazioni. Il modulo Mesh è stato anche ampiamente utilizzato come modulo di test principale nel primo mese di vita di FreeCAD.

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

Questo è un esempio standard, che utilizza il metodo `createSphere()` per creare automaticamente una sfera, ma si può benissimo creare propri oggetti mesh da uno schizzo, definendo i loro vertici e facce.

Per ulteriori informazioni leggere [ Script per Mesh\...](Mesh_Scripting/it.md) 

## Modulo Part 

Il modulo [Part](Part_Workbench/it.md) è il modulo più potente dell\'intero FreeCAD. Ti permette di creare e manipolare oggetti [BRep](https://it.wikipedia.org/wiki/B-Rep). BREP sta per \"Rappresentazione del confine\". Un oggetto BREP è definito da superfici che racchiudono e definiscono un volume interno. A differenza delle mesh, gli oggetti BREP possono avere un\'ampia varietà di componenti, dalle facce planari alle superfici NURBS molto complesse.

Il modulo Parte si basa sulla potente libreria [OpenCasCade](https://it.wikipedia.org/wiki/Open_CASCADE_Technology), che permette di eseguire facilmente sugli oggetti una vasta gamma di operazioni complesse, come le operazioni booleane, gli arrotondamenti, loft, ecc ..

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

Il modulo Parte (come il modulo Mesh) ha anche un comando veloce che crea automaticamente un oggetto FreeCAD e gli attribuisce una forma, in questo modo è possibile accorciare le 3 ultime righe dell\'esempio precedente con:


```python
Part.show(myshape)
```

Esplorando i contenuti di myshape, noterai molti sottocomponenti interessanti come `Faces`, `Edges`, `Vertexes`, `Solids` e {{incode |Shells}} e un\'ampia gamma di operazioni geometriche come `cut` (sottrazione), `common` (intersezione) o `fuse` (unione). La pagina [Script di dati topologici](Topological_data_scripting/it.md) spiega tutto in dettaglio.

[Approfondimento sugli script in Parte\...](Topological_data_scripting/it.md) 

## Modulo Draft 

FreeCAD offre molti altri moduli, come [Sketcher](Sketcher_Workbench/it.md) e [Draft](Draft_Workbench/it.md), che creano anche oggetti Part. Questi moduli aggiungono ulteriori parametri agli oggetti creati o addirittura implementano un modo completamente nuovo di gestire la geometria della parte in essi contenuta. Il nostro esempio sopra di una scatola è un perfetto esempio di un oggetto parametrico. Tutto ciò che serve per definire la scatola è specificare i parametri altezza, larghezza e lunghezza. Sulla base di questi, l\'oggetto calcolerà automaticamente la sua forma della parte. FreeCAD ti consente di [creare tali oggetti in Python](Scripted_objects/it.md).

Il Modulo [Draft](Draft_Workbench/it.md) aggiunge tipi di oggetti 2D parametrici (che sono tutti oggetti di Parte) quali linee e cerchi, e fornisce anche alcune funzioni generiche, che agiscono non solo sugli oggetti creati con Draft, ma su qualsiasi oggetto Parte. Per esplorare ciò che è disponibile, fare semplicemente:


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```


{{Top}}



## Interfaccia

L\'interfaccia utente di FreeCAD è realizzata con [Qt](https://it.wikipedia.org/wiki/Qt_(toolkit)), un potente sistema di interfaccia grafica, responsabile del disegno e della gestione di tutti i controlli, menu, barre degli strumenti e pulsanti intorno alla [vista 3D](3D_view/it.md). Qt fornisce un modulo, [PySide](PySide.md), che consente a Python di accedere e modificare le interfacce Qt come quelle di FreeCAD. Proviamo a giocherellare con l\'interfaccia Qt e produrre una semplice finestra di dialogo:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```

Si noti che la finestra di dialogo che appare ha l\'icona di FreeCAD nella sua barra degli strumenti, il che significa che Qt sa che l\'ordine è stato emesso dall\'interno dell\'applicazione FreeCAD. È possibile manipolare qualsiasi parte dell\'interfaccia di FreeCAD.

Qt è un sistema di interfaccia molto potente, che permette di fare cose molto complesse, inoltre dispone anche di vari strumenti molto facili da usare, come il Qt Designer con il quale è possibile progettare graficamente le finestre di dialogo e poi aggiungerle all\'interfaccia di FreeCAD con poche righe di codice Python.

[Quì si trovano altre informazioni su PySide\...](PySide/it.md) 

## Macro

Ora che si ha una buona conoscenza delle nozioni di base, dove conserviamo i nostri script Python, e come si fa ad eseguirli facilmente in FreeCAD? Per questo vi è un sistema semplice, chiamato [Macro](Macros/it.md). Una macro è semplicemente uno script Python, che può essere aggiunto a una barra degli strumenti e poi essere lanciato con un semplice clic del mouse. FreeCAD fornisce un semplice editor di testo (Macro → Macro → Crea) in cui è possibile scrivere o incollare degli script. Terminata la scrittura, il menu Strumenti → Personalizza → Macro permette di definire un pulsante per questo script che può anche essere aggiunto alle barre degli strumenti.



## Script esterni 

Un metodo alternativo per creare, salvare ed eseguire i propri script Python consiste nel crearli al di fuori di FreeCAD, utilizzando un editor di propria scelta (ad esempio, Vim). Per eseguire il proprio script Python all\'interno di FreeCAD, assicurarsi di salvarlo con l\'estensione **.py**.

Quindi usare **File → Apri** per aprire il proprio script. Verrà caricato in una nuova scheda nell\'[Area di visualizzazione principale](Main_view_area/it.md). Si può eseguire lo script facendo clic sul pulsante **<img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Esegui macro](Std_DlgMacroExecuteDirect/it.md)**. Eventuali errori o output dello script verranno mostrati nella finestra [Report](Report_view/it.md).

Quando si apportano e si salvano modifiche allo script già caricato, viene visualizzata una finestra di dialogo che chiede se si desidera ricaricare lo script modificato in FreeCAD.

Si può continuare alla pagina [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), oppure si può accedere a quella pagina e ad altre pagine pertinenti nell\'[Hub degli utenti esperti](Power_users_hub/it.md). {{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Python scripting tutorial/it
