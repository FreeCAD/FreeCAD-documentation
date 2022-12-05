# Pivy/it
{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

[Pivy](https://bitbucket.org/Coin3D/pivy/src/default/) è una libreria che collega Python con [Coin3d](https://bitbucket.org/Coin3D/coin/wiki/Home), ed è la libreria di renderizzazione-3D utilizzata in FreeCAD. Quando viene importata in un interprete Python in esecuzione, permette di dialogare direttamente con qualsiasi [grafo di scena](Scenegraph/it.md) (scenegraph) di Coin3d in esecuzione, come ad esempio le viste 3D di FreeCAD, o addirittura di creare nuovi grafi di scena. Pivy è incluso nell\'installazione standard di FreeCAD.


</div>

When imported in a running Python interpreter, Pivy allows us to communicate directly with any running Coin [scenegraph](Scenegraph.md), such as the [3D view](3D_view.md), or even to create new ones. Pivy is not required to compile FreeCAD, but it is required at runtime when running Python-based workbenches that create shapes on screen, like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md). Because of this, Pivy is normally installed when installing a distribution of FreeCAD.


<div class="mw-translate-fuzzy">

La libreria Coin è divisa in vari moduli, Coin stessa, per manipolare grafi di scene e associarli a diversi sistemi GUI, come a Windows oppure, come nel nostro caso, a Qt. Tali moduli sono disponibili anche per Pivy, se sono presenti nel sistema. Il modulo Coin è sempre presente, ed è quello che useremo in tutti gli esempi, e non sarà necessario preoccuparsi di associare la nostra visualizzazione 3D ad alcuna interfaccia, perchè questo viene già fatto da FreeCAD stesso. Tutto quello che dobbiamo fare è:


</div>


```python
from pivy import coin
```


<div class="mw-translate-fuzzy">

## Accesso e modifica del Grafo della scena (Scenegraph) 


</div>


<div class="mw-translate-fuzzy">

Abbiamo già visto nella pagina [Grafo della scena](Scenegraph/it.md) (Scenegraph) come è organizzata una tipica scena di Coin. Tutto ciò che appare in una vista 3D di FreeCAD è un Scenegraph di Coin, organizzato allo stesso modo. Abbiamo un nodo radice (principale), e tutti gli oggetti sullo schermo sono suoi figli.


</div>

FreeCAD dispone di un modo semplice per accedere al nodo radice (root) di una scena grafica in vista 3D:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

Ciò restituisce il nodo principale (root):


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Siamo in grado di ispezionare i figli immediati della nostra scena:


```python
for node in sg.getChildren():
    print(node)
```


<div class="mw-translate-fuzzy">

Alcuni di questi nodi, ad esempio SoSeparators o SoGroups, possono avere dei propri figli. L\'elenco completo degli oggetti Coin disponibili si può trovare nella [documentazione ufficiale di Coin](https://coin3d.bitbucket.io/Coin/annotated.html).


</div>

Ora proviamo ad aggiungere qualcosa al nostro Scenegraph. Aggiungiamo un bel cubo rosso:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```


<div class="mw-translate-fuzzy">

e questo è il nostro (bel) cubo rosso. Ora, proviamo questo:


</div>


```python
col.rgb = (1, 1, 0)
```


<div class="mw-translate-fuzzy">

Visto? Tutto è sempre accessibile e modificabile al volo. Non c\'è bisogno di ricalcolare o ridisegnare nulla, Coin si prende cura di tutto. È possibile aggiungere elementi al grafo di scena, modificare le proprietà, nascondere delle cose, mostrare oggetti temporanei, qualsiasi cosa. Naturalmente, questo riguarda solo la visualizzazione nella vista 3D. Questa visualizzazione viene determinata da FreeCAD all\'apertura del file attivo e quando un oggetto ha bisogno di essere ricalcolato. Quindi, se si modifica l\'aspetto di un oggetto di FreeCAD esistente, tali modifiche andranno perse se l\'oggetto viene ricalcolato o quando si riapre il file.


</div>


<div class="mw-translate-fuzzy">

Per lavorare con i grafi di scena nei nostri script è fondamentale saper accedere a specifiche proprietà dei nodi aggiunti quando questo è necessario. Per esempio, se avessimo voluto spostare il nostro cubo, avremmo aggiunto un nodo SoTranslation al nostro nodo personalizzato, e lo script apparirebbe così:


</div>


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
trans = coin.SoTranslation()
trans.translation.setValue([0, 0, 0])
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(trans)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```


<div class="mw-translate-fuzzy">

Ricordate che, in un Scenegraph di OpenInventor, l\'ordine è importante. Un nodo riguarda ciò che viene dopo, quindi permette di definire qualcosa come: colore rosso, cubo, colore giallo, sfera, e di ottenere un cubo rosso e una sfera gialla. Se aggiungiamo ora la traslazione al nostro nodo personalizzato esistente, essa viene dopo il cubo, e non lo condiziona. Se lo avessimo inserito durante la creazione, come qui sopra, ora si potrebbe fare:


</div>


```python
trans.translation.setValue([2, 0, 0])
```


<div class="mw-translate-fuzzy">

E il nostro cubo si sposterebbe di 2 unità a destra.

Infine, la rimozione di qualcosa si fà con:


</div>


```python
sg.removeChild(myCustomNode)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Utilizzo dei meccanismi di richiamo (callback) 


</div>


<div class="mw-translate-fuzzy">

Un [callback mechanism](http://en.wikipedia.org/wiki/Callback_%28computer_science%29) (meccanismo di richiamo) è un sistema che permette a una libreria che si sta utilizzando, come la nostra libreria Coin, di richiamare, cioè, di chiamare una determinata funzione dell\'oggetto Python attualmente in esecuzione. Ciò è estremamente utile, perché in questo modo Coin può avvisarci se nella scena si verifica qualche evento specifico. Coin può controllare cose molto diverse, come la posizione del mouse, i clic di un pulsante del mouse, i tasti della tastiera che vengono premuti e tante altre cose.


</div>

FreeCAD fornisce un modo semplice per utilizzare tali callback:


```python
from pivy import coin

class ButtonTest:
    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getMouseClick) 

    def getMouseClick(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == coin.SoMouseButtonEvent.DOWN:
            print("Alert!!! A mouse button has been improperly clicked!!!")
            self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)

ButtonTest()
```


<div class="mw-translate-fuzzy">

Il richiamo deve essere iniziato da un oggetto, perché questo oggetto deve essere ancora in esecuzione quando il callback si verifica. Vedere anche la [lista completa](Code_snippets/it#Observación_de_Eventos_del_ratón_en_el_visor_3D_a_través_de_Python.md) degli eventi possibili e dei loro parametri, o la [documentazione ufficiale di Coin](https://coin3d.bitbucket.io/Coin/index.html).


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Documentazione


</div>


<div class="mw-translate-fuzzy">

Purtroppo, Pivy non ha ancora una propria documentazione adeguata, ma dato che è una traduzione esatta di Coin, si può tranquillamente utilizzare la documentazione di Coin come riferimento, e utilizzare lo stile Python al posto dello stile C++.


</div>

In C++:


```python
SoFile::getClassTypeId()
```


<div class="mw-translate-fuzzy">

In Pivy


</div>


```python
SoFile.getClassId()
```


<div class="mw-translate-fuzzy">

-   [Coin Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado
-   [Coin Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket


</div>

### Older

Questi collegamenti forniscono documentazione di riferimento per Coin v3.x. Le differenze con v4.x sono minime, quindi potrebbero essere comunque utili.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.


{{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Pivy/it
