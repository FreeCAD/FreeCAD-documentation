# Pivy/it
## Introduzione

[Pivy](Pivy/it.md) è una libreria di associazione [Python](Python/it.md) per [Coin](https://github.com/coin3d), la libreria di rendering 3D utilizzata in FreeCAD per visualizzare gli oggetti nella [vista 3D](3D_view/it.md). Coin è un\'implementazione open source della specifica \"Open Inventor\" per gestire la grafica. Pertanto, in FreeCAD, i termini \"Pivy\", \"Coin\" o \"Open Inventor\" si riferiscono essenzialmente alla stessa cosa.

Pivy, quando importato in un interprete Python in esecuzione, ci consente di comunicare direttamente con qualsiasi [scena grafica](Scenegraph/it.md) Coin in esecuzione, come la [vista 3D](3D_view/it.md), o anche di crearne di nuove. Pivy non è necessario per compilare FreeCAD, ma è richiesto in fase di esecuzione quando si eseguono ambienti di lavoro basati su Python, che creano forme sullo schermo, come [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md). Per questo motivo, Pivy viene normalmente installato durante l\'installazione di una distribuzione di FreeCAD.

La libreria Coin è divisa in vari moduli, Coin stessa, per manipolare grafi di scene e associarli a diversi sistemi GUI, come Windows e Qt. Se presenti nel sistema, tali moduli sono disponibili anche per Pivy. Il modulo Coin è sempre presente, ed è quello che useremo in tutti gli esempi, e non sarà necessario preoccuparsi di associare la nostra visualizzazione 3D ad alcuna interfaccia, perché questo viene già fatto da FreeCAD stesso. Tutto quello che dobbiamo fare è:


```python
from pivy import coin
```



## Grafo della scena 

Abbiamo già visto nella pagina [Grafo della scena](Scenegraph/it.md) (Scenegraph) come è organizzata una tipica scena di Coin. Tutto ciò che appare in una [vista 3D](3D_view/it.md) di FreeCAD è un Scenegraph di Coin, organizzato allo stesso modo. Abbiamo un nodo radice (principale), e tutti gli oggetti sullo schermo sono suoi figli.

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

Alcuni di questi nodi, ad esempio `SoSeparator` o `SoGroup`, possono avere dei propri figli. L\'elenco completo degli oggetti Coin disponibili si può trovare nella documentazione ufficiale di Coin.

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

Ora, proviamo questo:


```python
col.rgb = (1, 1, 0)
```

Come si può notare tutto è sempre accessibile e modificabile al volo. Non c\'è bisogno di ricalcolare o ridisegnare nulla, Coin si prende cura di tutto. È possibile aggiungere elementi al grafo di scena, modificare le proprietà, nascondere delle cose, mostrare oggetti temporanei, qualsiasi cosa. Naturalmente, questo riguarda solo la visualizzazione nella vista 3D. Questa visualizzazione viene determinata da FreeCAD all\'apertura del file attivo e quando un oggetto ha bisogno di essere ricalcolato. Quindi, se si modifica l\'aspetto di un oggetto di FreeCAD esistente, tali modifiche andranno perse se l\'oggetto viene ricalcolato o quando si riapre il file.

Come già accennato, in uno scenegraph di openInventor l\'ordine è importante. Un nodo influisce su ciò che viene dopo. Ad esempio, se vogliamo avere la possibilità di spostare il nostro cubo, dovremo aggiungere un nodo `SoTranslation` **prima** del cubo:


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

Per muovere il nostro cubo ora possiamo fare:


```python
trans.translation.setValue([2, 0, 0])
```

Infine, la rimozione di qualcosa viene eseguita con:


```python
sg.removeChild(myCustomNode)
```


{{Top}}



## Il Callback 

Un [meccanismo di callback](https://it.wikipedia.org/wiki/Callback) è un sistema che permette a una libreria, che si sta utilizzando, come la nostra libreria Coin, di richiamare, cioè, di chiamare una determinata funzione dell\'oggetto Python attualmente in esecuzione. In questo modo Coin può avvisarci se nella scena si verifica qualche evento specifico. Coin può controllare cose molto diverse, come la posizione del mouse, i clic di un pulsante del mouse, i tasti della tastiera che vengono premuti e tante altre cose.

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

Il callback deve essere iniziato da un oggetto, perché questo oggetto deve essere ancora in esecuzione quando il callback si verifica. Vedere anche la [lista completa](Code_snippets/it#Controllare_gli_eventi_del_mouse_nel_visualizzatore_3D_tramite_Python.md) di possibili eventi e dei loro parametri, o la documentazione ufficiale di Coin. 

## Documentazione

Purtroppo, Pivy non ha ancora una propria documentazione adeguata, ma dato che è una traduzione esatta di Coin, si può tranquillamente utilizzare la documentazione di Coin come riferimento, e utilizzare lo stile Python al posto dello stile C++.

In C++:


```python
SoFile::getClassTypeId()
```

In Pivy:


```python
SoFile.getClassId()
```

-   [Coin3D](https://github.com/coin3d) homepage.
-   [Pivy](https://github.com/coin3d/pivy) homepage.
-   [Coin3D wiki](https://github.com/coin3d/coin/wiki), su GitHub.
-   [Coin3D wiki documentation](https://github.com/coin3d/coin/wiki/Documentation), su GitHub.
-   [Coin3D documentation](https://coin3d.github.io/Coin/html/), ultima documentazione Doxygen generata automaticamente.
-   [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) - raccomandato.



### Meno recente 

Questi collegamenti forniscono documentazione di riferimento per Coin v3.x. Le differenze con v4.x sono minime, quindi potrebbero essere comunque utili.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.


{{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Pivy/it
