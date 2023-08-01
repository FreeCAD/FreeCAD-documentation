---
- GuiCommand:
   Name: PartDesign Body
   Name/it: Corpo
   MenuLocation: Part Design - Crea un corpo
   Workbenches: [PartDesign](PartDesign_Workbench/it.md)
   Version: 0.17
   SeeAlso: [Parte standard](Std_Part/it.md), [Editazione delle funzioni](feature_editing/it.md)
---

# PartDesign Body/it

## Descrizione

Un [Corpo](PartDesign_Body/it.md) di PartDesign è l\'elemento base per creare forme solide con [PartDesign](PartDesign_Workbench/it.md). Può contenere [schizzi](Sketch/it.md), [oggetti di riferimento](Datum/it.md) e [funzioni di PartDesign](PartDesign_Feature/it.md) che aiutano a produrre un [singolo solido contiguo](PartDesign_Body/it#Singolo_solido_contiguo.md).

Il Corpo fornisce un oggetto **Origin** che include gli assi X,Y,Z, e i piani standard. Questi elementi possono essere usati come riferimenti per collegare gli [schizzi](Sketch/it.md) e gli [oggetti primitivi](PartDesign_CompPrimitiveAdditive/it.md).


<div class="mw-translate-fuzzy">

Poiché si suppone che il Corpo sia un [singolo solido contiguo](PartDesign_Body/it#Singolo_solido_contiguo.md), esso può essere spostato interamente come un\'unità, senza spostare le singole funzioni. All\'interno di una [Parte standard](Std_Part/it.md) è possibile posizionare più corpi per creare assiemi.


</div>

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*A sinistra: la vista ad albero che mostra le funzioni che producono in sequenza la forma finale dell'oggetto. A destra: l'oggetto finale visibile nella [vista 3D](3D_view/it.md).
*

## Utilizzo

Se non è stato selezionato alcun solido precedente:

1.  Premere il pulsante **<img src="images/PartDesign_Body.svg" width=16px> [Corpo](PartDesign_Body/it.md)**. Viene creato un corpo vuoto che diventa automaticamente **[attivo](PartDesign_Body/it#Stato_attivo.md)**.
2.  Ora si può premere **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nuovo schizzo](PartDesign_NewSketch/it.md)** per creare uno [schizzo](Sketch/it.md) nel corpo. In seguito lo schizzo può essere utilizzato per creare una **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Estrusione](PartDesign_Pad/it.md)**.
3.  In alternativa, si può aggiungere una [funzione di PartDesign](PartDesign_Feature/it.md) primitiva, ad esempio un **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Cubo additivo](PartDesign_AdditiveBox/it.md)**.

Se viene selezionato un oggetto solido:

1.  Premere il pulsante **<img src="images/PartDesign_Body.svg" width=16px> [Corpo](PartDesign_Body/it.md)**. Viene creato un nuovo Corpo contenente una singola **Base Feature**. Questo elemento Base Feature è un semplice riferimento a un altro oggetto precedentemente creato o importato nel documento. Per maggiori informazioni vedere [Funzione di base](PartDesign_Body/it#Funzione_di_base.md). Non è possibile selezionare un Corpo esistente o una [funzione di PartDesign](PartDesign_Feature/it.md) quando si preme **<img src="images/PartDesign_Body.svg" width=16px> [Corpo](PartDesign_Body/it.md)**.

### Note

-   Se, quando si preme il pulsante **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nuovo schizzo](PartDesign_NewSketch/it.md)** della barra degli strumenti di PartDesign non esiste ancora un corpo, ne viene creato automaticamente uno nuovo. Se esiste già un corpo, esso deve essere reso attivo prima di usare **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nuovo schizzo](PartDesign_NewSketch/it.md)**.
-   Fare doppio clic su Corpo nella [vista ad albero](tree_view/it.md) o aprire il menu di scelta rapida (clic con il tasto destro) e selezionare **Attiva corpo** per attivare o disattivare il corpo. Se un altro corpo è attivo, esso viene disattivato. Per maggiori informazioni vedere [Stato attivo](PartDesign_Body/it#Stato_attivo.md).

## Proprietà

Un [Corpo di PartDesign](PartDesign_Body/it.md) (classe `PartDesign::Body`) è derivato da una [Part Feature](Part_Feature/it.md) (classe `Part::Feature`), pertanto condivide tutte le proprietà di quest\'ultimo.

Oltre alle proprietà descritte in [Part Feature](Part_Feature/it.md), il corpo di PartDesign ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md).

### Dati


{{TitleProperty|Base}}

-    **Tip|Link**: è la [funzione di PartDesign](PartDesign_Feature/it.md) definita come \"funzione finale\", che è in genere l\'ultima funzione creata nel corpo. La funzione finale indica la forma finale del corpo, che viene mostrata nella [Vista 3D](3D_view/it.md) quando **Display Mode Body** è impostata su `Tip`. Per maggiori informazioni vedere [Tip](PartDesign_Body/it#Tip.md).

-    **Base Feature|Link**: è una forma esterna usata come prima [funzione di PartDesign](PartDesign_Feature/it.md) nel Corpo. Di solito viene impostata quando si trascina un oggetto solido in un corpo vuoto. Se non viene importato nessun solido in questo modo, questa proprietà rimane vuota. Per maggiori informazioni vedere [Funzione di base](PartDesign_Body/it#Funzione_di_base.md).

-    **Placement**: la posizione dell\'oggetto nella [Vista 3D](3D_view/it.md). Il posizionamento è definito da un punto `Base` (vettore) e una `Rotation` (asse e angolo). Vedere [Posizionamento](Placement/it.md).

-    **Group**: un elenco di [funzioni di PartDesign](PartDesign_Feature/it.md) nel Corpo

#### Proprietà dati nascoste 


<div class="mw-translate-fuzzy">

-    **Origin|Link**: l\'oggetto [App Origin](App_Origin/it.md) che è il riferimento posizionale per tutti gli elementi elencati nel **Gruppo**.

-    **_ Group Touched|Bool**: se il gruppo viene toccato o no.


</div>

Oltre ale proprietà nascoste descritte in [Part Feature](Part_Feature/it.md) il corpo di PartDesign ha le seguenti proprietà nell\'[editor delle proprietà](Property_editor/it.md).

### Vista


{{TitleProperty|Base}}

-    **Display Mode Body|Enumeration**: imposta la modalità di visualizzazione nella vista 3D specifica per il corpo in uno dei due tipi.

    -   
        `Through`
        
        (default) espone tutti gli oggetti all\'interno del Corpo, ovvero [schizzi](Sketch/it.md), [funzioni di PartDesign](PartDesign_Feature/it.md), oggetti di riferimento, ecc. Questa modalità consente di visualizzare le operazioni parziali eseguite all\'interno del Corpo, quindi è la modalità raccomandata durante l\'aggiunta e la modifica di funzioni. Selezionare la funzione desiderata e impostare **Visibility** su `True` o premere la barra **Spazio** sulla tastiera.

    -   
        `Tip`
        
        espone solo la forma finale del corpo, definita dalla proprietà **Tip**. Tutto il resto, tra cui [schizzi](Sketch/it.md), [funzioni di PartDesign](PartDesign_Feature/it.md), oggetti di riferimento, ecc., non viene visualizzato, anche se sono visibili nella [vista ad albero](tree_view/it.md). Questa modalità è consigliata quando non è necessario modificare ulteriormente il corpo, quindi viene visualizzata una forma finale. Questa modalità è consigliata anche quando si desidera selezionare gli elementi secondari (vertici, bordi e facce) della forma finale da utilizzare con gli strumenti di altri ambienti da lavoro.

## Concetto di Corpo 

### Singolo solido contiguo 

Il corpo PartDesign è progettato per modellare un singolo solido contiguo. Per \"contiguo\" si intende un elemento realizzato in un unico pezzo, senza parti mobili o solidi disconnessi. Esempi di solidi contigui sono quelli fabbricati da un singolo pezzo di materia prima mediante un processo di fusione, taglio o fresatura. Ad esempio, un dado, una rondella e un bullone sono costituiti ciascuno da un unico pezzo di acciaio solido senza parti mobili, quindi ciascuno di essi può essere modellato come un corpo PartDesign. Gli oggetti creati saldando due pezzi possono anche essere modellati in un singolo corpo, purché il giunto di saldatura non sia destinato a rompersi.

Quando questi solidi contigui vengono riuniti in un qualche tipo di disposizione, diventano un \"assemblaggio\". In un assemblaggio, gli oggetti non vengono fusi insieme, ma vengono semplicemente \"impilati\" o posizionati uno accanto all\'altro e rimangono singole parti.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*A sinistra: tre solidi contigui individuali, ciascuno modellato in un Corpo di PartDesign. A destra: i singoli Corpi riuniti in un'assemblaggio.*

### Editazione delle funzioni 

Un corpo di PartDesign è progettato per funzionare creando un solido iniziale, da uno [schizzo](Sketch/it.md) o da una [forma primitiva](PartDesign_CompPrimitiveAdditive/it.md), e quindi modificandolo tramite le [\"funzioni\"](PartDesign_Feature/it.md) per aggiungere o rimuovere materiale dalla forma precedente. Per una spiegazione completa, vedere la pagina [editazione delle funzioni](feature_editing/it.md).

Un corpo di PartDesign esegue una [fusione](Part_Fuse/it.md) (unione) automatica degli elementi solidi al suo interno. Ciò significa che (1) i solidi parziali devono toccarsi quando vengono creati e (2) che i solidi disconnessi non sono consentiti.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*A sinistra: due singoli solidi che si intersecano. A destra: un singolo corpo di PartDesign creato con due [funzioni additive](PartDesign_Feature/it.md), che vengono automaticamente fuse insieme, quindi invece di intersecarsi, formano un singolo solido contiguo.*

![](images/PartDesign_Body_non-contiguous.png ) 
*A sinistra: due solidi disconnessi; questo non è un corpo PartDesign valido. A destra: due solidi che si toccano; ciò si traduce in un corpo PartDesign valido. La [funzione](PartDesign_Feature/it.md) più recente deve sempre contattare o intersecare la funzione precedente in modo che sia fusa con essa e diventi un singolo solido contiguo.*


**Nota:**

altri programmi CAD come Catia consentono solidi non contigui nello stesso \"Corpo\". A partire dalla versione 0.19, FreeCAD non lo consente. Ci sono state delle discussioni nel [forum di FreeCAD](https://forum.freecadweb.org/index.php) sulla revoca di questa restrizione, ma non è stata presa alcuna decisione concreta. Se desiderate saperne di più o presentare punti di vista diversi, potete discuterne nel [forum](https://forum.freecadweb.org/index.php).

## Spiegazione dettagliata delle proprietà 

### Stato attivo 

Un documento aperto può contenere più corpi. Per aggiungere una nuova funzione a un corpo specifico, è necessario renderlo **attivo**. Un corpo attivo vinene visualizzato nella [vista ad albero](tree_view/it.md) con il colore di sfondo specificato dal valore **Active container** nell\'[editor delle preferenze](Preferences_Editor/it#Colori.md) (per impostazione predefinita, blu). Un corpo attivo viene anche mostrato in grassetto.

Per attivare o disattivare un corpo:

-   Fare doppio clic su di esso nella [vista ad albero](tree_view/it.md), oppure
-   Aprire il menu contestuale (tasto destro) e selezionare **Attiva/disattiva il corpo**.

L\'attivazione di un corpo commuta automaticamente anche l\'interfaccia nell\'ambiente [PartDesign](PartDesign_Workbench/it.md), se questo non era già l\'ambiente attivo. Può essere attivo solo un singolo corpo per volta.

![](images/PartDesign_Body_active.png )



*Documento con due corpi PartDesign, di cui il secondo è attivo.*

### Origine

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

1.  Create the Body.
2.  If the Body is selected in the [tree view](tree_view.md), press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**; the [task panel](task_panel.md) will open to allow selecting one of the planes.
3.  If the Body is not selected, select the Origin instead and make it visible in the [3D view](3D_view.md) by pressing the **Space** bar in the keyboard. Also expand the Origin object to see the axes and planes.
4.  Select one of the planes, either in the [tree view](tree_view.md) or in the [3D view](3D_view.md), then press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**. The sketch will be created on the chosen plane.

The same process can be used when creating auxiliary datum geometry like [PartDesign Lines](PartDesign_Line.md), [PartDesign Planes](PartDesign_Plane.md), and [PartDesign CoordinateSystems](PartDesign_CoordinateSystem.md).


**Note:**

the Origin is an [App Origin](App_OriginGroupExtension.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Body are referenced to the Body\'s Origin which means that the Body can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*Left: PartDesign Body Origin in the [tree view](tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*

### Funzione di base 

La Funzione di base, Base feature, è la prima [Funzione PartDesign](PartDesign_Feature/it.md) creata nel corpo quando il corpo si basa su un\'altra forma solida. Questo solido può essere creato in qualsiasi ambiente di lavoro o importato da un file esterno, ad esempio un file STEP.

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*PartDesign Bodies, each of them with a single Base Feature, which are taken from previously created solids.*

To create the Base Feature:

1.  select a solid shape external to any Body, and
2.  press **[<img src=images/PartDesign_Body.svg style="width:16px"> [Body](PartDesign_Body.md)**; this will create a new Body with a single Base Feature.


**Note:**

you can\'t select an existing Body, or any of its [features](PartDesign_Feature.md), when pressing **[<img src=images/PartDesign_Body.svg style="width:16px"> [Body](PartDesign_Body.md)**.

If you already have a Body, you can create the Base Feature in this way:

-   in the [tree view](tree_view.md), pick an object, and drag and drop it inside the Body, or
-   in the [property editor](property_editor.md), edit the value of **Base Feature** by pressing the ellipsis **...**, and choosing an object from the list. In this case you can choose an existing Body to be the Base Feature.


**Note:**

dragging and dropping only works for Bodies which don\'t have a Base Feature already.


**Note 2:**

if the Body already has several features, when you drag and drop the external solid, the Base Feature will be created at the beginning of the list of features, that is, it will be added to the beginning of the **Group** property.

The Base Feature is entirely optional; it is only present when including an object from outside the Body. If no external solid is included, you can still build your shape using [sketches](Sketch.md), [pads](PartDesign_Pad.md), [primitive objects](PartDesign_CompPrimitiveAdditive.md), and other [PartDesign Features](PartDesign_Feature.md). In this case the **Base Feature** property remains empty.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*Left: PartDesign Body with a Base Feature that is taken from an external solid object, and many subsequent [PartDesign Features](PartDesign_Feature.md) on top. Right: Body which doesn't have an explicit Base Feature.*


**Note:**

If another PartDesign body is selected as a BaseFeature it must have a shape. If it is empty (no features, no BaseFeature, \...) this will result in error.

### Tip


<div class="mw-translate-fuzzy">

La cima o punta (Tip) è la [PartDesign Feature](PartDesign_Feature/it.md) del corpo che viene esposta all\'esterno (quello che si vede). Viene automaticamente impostata sull\'ultima funzione nella parte inferiore dell\'albero; vale a dire che, se un altro strumento da qualsiasi ambiente di lavoro (ad esempio, [Copia semplice](Part_SimpleCopy/it.md) o [Sottrai](Part_Cut/it.md) di Part) deve utilizzare la forma del corpo, utilizzerà la forma della Punta. Detto in altro modo, la Punta è la rappresentazione finale del Corpo come se la storia parametrica non esistesse.


</div>

![](images/PartDesign_Body_Tip_final.svg )



*Left: PartDesign Body with full parametric history including intermediate features. Right: the Tip is the final shape that can be exported from the Body, while omitting the model's history.*

The Tip is automatically set to the last feature created in the Body. Nevertheless, it can also be set to any of the intermediate features by opening the [tree view](tree_view.md) context menu (right-click) and choosing **[<img src=images/PartDesign_MoveTip.svg style="width:16px"> [Set tip](PartDesign_MoveTip.md)**, or by changing the Body\'s **Tip** value in the [property editor](property_editor.md).

Changing the Tip in effect rolls back its history, making it possible to add features that should have been added earlier. It also exposes a different shape to external tools.


<div class="mw-translate-fuzzy">

Nella [vista ad albero](tree_view/it.md), la funzione finale del corpo è riconoscibile dalla [funzione di PartDesign](PartDesign_Feature/it.md) che ha una icona sovrapposta costituita da una freccia bianca all\'interno di un cerchio verde.


</div>

![](images/PartDesign_Body_Tip_tree.png ) 
*Two PartDesign Bodies, each of them with [PartDesign Features](PartDesign_Feature.md). The Tip is the last feature in them, and is marked with an overlay symbol.*

### Interazione con gli altri ambienti di lavoro 


<div class="mw-translate-fuzzy">

Per impostazione predefinita, le [funzioni](PartDesign_Feature/it.md) all\'interno di un corpo sono selezionabili, e ovviamente ciò è necessario per poter modificare e aggiungere delle funzioni in PartDesign. Tuttavia, non è consigliabile selezionare le singole funzioni per utilizzarle con gli strumenti di altri ambienti di lavoro, come [Part](Part_Workbench/it.md) e [Draft](Draft_Workbench/it.md), poiché i risultati potrebbero essere inaspettati; in tal caso, nella [vista rapporto](Report_view/it.md) potrebbe apparire un messaggio di errore, **Links go out of the allowed scope**.


</div>

Pertanto, per le interazioni con gli altri ambienti, dovrebbe essere selezionato solo il Corpo stesso dall\'albero del modello. Nei casi in cui è necessario selezionare un sottoelemento specifico del Corpo (vertice, bordo, faccia), allora la proprietà vista **Display Mode Body** del Corpo può essere modificata da *Through* (impostazione predefinita) a `Tip`. Questa proprietà è accessibile dal pannello Vista. In modalità *Tip* l\'accesso agli oggetti sottostanti al Corpo (funzioni, riferimenti, schizzi) è disabilitato; nella vista 3D viene nascosto tutto tranne la funzione tip, indipendentemente da quale oggetto è impostato come visibile.

Una volta completate le operazioni in altri ambienti, non dimenticare di ripristinare la proprietà **Display Mode Body** in `Through` per essere di nuovo in grado di modificare il corpo.

![](images/PartDesign_Body_Tip_Display_mode.svg )



*Left: when "Display Mode Body" is set to `Through* it is possible to select and perform operations with the individual [PartDesign Features](PartDesign_Feature.md); in general, this is not recommended. Right: when "Display Mode Body" is set to {{incode|Tip` all selections and operations done on the Body will be done on the Tip, making sure only the final shape of the Body is exposed.}}

### Gestione della visibilità 

La visibilità del corpo prevale sulla visibilità di qualsiasi oggetto in esso contenuto. Se il corpo è nascosto, sono nascosti anche gli oggetti che esso contiene, anche se la loro proprietà **Visibility** è impostata su `True`.

Multiple [Sketches](Sketch.md) may be visible at one time, but only one [PartDesign Feature](PartDesign_Feature.md) (solid result) can be visible at a time. Selecting a hidden feature and pressing the **Space** bar in the keyboard will make it visible, and automatically hide the previously visible feature.

![](images/PartDesign_Body_Visibility.png ) 
*PartDesign Body: multiple [Sketches](Sketch.md) may be visible simultaneously, but only one solid [PartDesign Feature](PartDesign_Feature.md) may be visible at one time, whether it is the Tip or not.*

### Attachment

[PartDesign Features](PartDesign_Feature.md), just like [planar objects](Part_Part2DObject.md), can be attached to different planes, usually the standard planes defined by the Body\'s [Origin](PartDesign_Body#Origin.md), or to custom [PartDesign Planes](PartDesign_Plane.md).

[Sketches](Sketch.md) are normally attached to a plane when they are created. In similar way, [primitive features](PartDesign_CompPrimitiveAdditive.md) can also be attached. Attaching these objects to a plane allows them to be moved within the Body by changing their **Attachment Offset** property. For more information on the attachment modes see [Part EditAttachment](Part_EditAttachment.md).

A [PartDesign Feature](PartDesign_Feature.md) that is not attached will be shown with a red overlay symbol next to their icon in the [tree view](tree_view.md).

![](images/PartDesign_Body_Feature_attachment.png ) 
*PartDesign Body: [PartDesign Features](PartDesign_Feature.md) that are not attached to a plane or coordinate system will be shown with an overlay symbol next to their icon in the [tree view](tree_view.md).*

### Inheritance

A [PartDesign Body](PartDesign_Body.md) is formally an instance of the class `PartDesign::Body`, whose parent is [Part Feature](Part_Feature.md) (`Part::Feature` class) through the intermediate `Part::BodyBase` class, and is augmented with an Origin extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `PartDesign::Body* object is intended to build parametric 3D solids, and thus is derived from the basic {{incode|Part::Feature` object, and has an Origin to control the placement of the features used inside of it.}}

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento.

Un corpo PartDesign viene creato con il metodo `addObject()` del documento. Quando esiste un Corpo, ad esso si possono aggiungere le [funzioni](PartDesign_Feature/it.md) con i metodi `addObject()` o `addObjects()` di questo Corpo.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

In a document that has many Bodies, the [active Body](PartDesign_Body#Active_status.md) can be set using the `setActiveObject` method of the `ActiveView`. The first argument is the fixed string `"pdbody"`, and the second argument is the Body object that should be made active. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/it
