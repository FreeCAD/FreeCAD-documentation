---
- GuiCommand:/it
   Name:Std Part
   Name/it:Parte
   MenuLocation:Nessuno
   Workbenches:Tutti
   Version:0.17
   SeeAlso:[Gruppo](Std_Group/it.md), [PartDesign Corpo](PartDesign_Body/it.md)
---

# Std Part/it

## Descrizione

Una <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Parte](Std_Part/it.md) (internamente chiamata [App Part](App_Part/it.md)) è un contenitore per scopi generali che contiene un gruppo di oggetti in modo che essi possano essere spostati in blocco come una singola unità nella vista 3D.

L\'elemento Parte è stato sviluppato per essere l\'elemento di base per creare [assemblaggi](assembly/it.md) meccanici. In particolare, ha lo scopo di disporre oggetti che hanno una [forma topologica](Part_TopoShape/it.md), come le [primitive di Part](Part_Primitives/it.md), i [corpi di PartDesign](PartDesign_Body/it.md), e altre [funzioni di Part](Part_Feature/it.md). Parte fornisce un [Origine](Std_Part/it#Origine.md) con assi X, Y e Z locali e piani standard; questa origine viene utilizzata come riferimento per posizionare e collegare quegli altri oggetti. Inoltre, le Parti possono essere nidificate all\'interno di altre Parti per creare un grande assieme da sotto-assiemi più piccoli.

Sebbene sia destinato principalmente a corpi solidi, Parte può essere utilizzato per gestire qualsiasi oggetto che abbia una proprietà [Posizionamento](Placement/it.md), quindi può anche contenere [Funzioni Mesh](Mesh_Feature/it.md), [schizzi](Sketch/it.md) e altri oggetti derivati dalla classe [App GeoFeature](App_GeoFeature/it.md).

Non confondere il <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corpo di PartDesign](PartDesign_Body/it.md) con la <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Parte](Std_Part/it.md). Il primo è un oggetto specifico utilizzato in <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md), destinato a modellare un [singolo solido contiguo](PartDesign_Body/it#Singolo_solido_contiguo.md) mediante le [ funzioni di PartDesign](PartDesign_Feature/it.md). Invece, la [Parte](Std_Part/it.md) non viene utilizzata per la modellazione, ma solo per disporre diversi oggetti nello spazio, per creare degli [assemblaggi](assembly/it.md).

Lo strumento Parte non è definito da un particolare ambiente di lavoro, ma dal sistema base; di conseguenza lo si trova nella **barra degli strumenti struttura**, che è disponibile in tutti gli [ambienti di lavoro](Workbenches/it.md). Per raggruppare gli oggetti arbitrariamente senza considerare la loro posizione, utilizzare <img alt="" src=images/Std_Group.svg  style="width:16px;"> [Gruppo](Std_Group/it.md); questo oggetto non influenza i posizionamenti degli elementi che contiene, è essenzialmente solo una cartella che viene utilizzata per mantenere organizzata la [vista ad albero](tree_view/it.md).

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*A sinistra: elementi all'interno di una Parte nella vista ad albero. A destra: oggetti posizionati nello spazio, riferiti all'Origine della Parte.*

## Utilizzo

1.  Premere il pulsante **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)**. Viene creata una parte vuota che diventa automaticamente *[attiva](Std_Part/it#Stato_attivo.md)*.
2.  Per aggiungere oggetti a una parte, trascinarli e rilasciarli sulla parte nella [vista ad albero](tree_view/it.md).
3.  Per rimuovere oggetti da una parte, trascinarli fuori dalla parte e sull\'etichetta del documento nella parte superiore della [vista ad albero](tree_view/it.md).

### Note

-   A partire dalla v0.19, un dato oggetto può appartenere solo ad una singola Parte.
-   Fare doppio clic sulla Parte nella [vista ad albero](tree_view/it.md) o aprire il menu contestuale (tasto destro del mouse) e selezionare **Attiva/disattiva la parte** per attivare o disattivare la Parte. Se un\'altra Parte è attiva, sarà disattivata. Vedere [Stato attivo](Std_Part/it#Stato_attivo.md) per maggiori informazioni.

### Limitazioni

-   Al momento, i metodi [Snap di Draft](Draft_Snap/it.md) non funzionano sui contenitori di Parti selezionati né sugli oggetti al loro interno.
-   Una Parte non ha una [forma topologica](Part_TopoShape/it.md), quindi operazioni 3D come le [operazioni booleane](Part_Boolean/it.md) non possono essere utilizzate su una parte. Ad esempio, non è possibile selezionare due parti ed eseguire una [Unione](Part_Fuse/it.md) o un [Taglio](Part_Cut/it.md) con esse.
    -   Queste operazioni booleane funzionano solo sugli oggetti contenuti fintanto che sono derivati da [Part Feature](Part_Feature/it.md) e hanno una [forma topologica](Part_TopoShape/it.md).

## Proprietà

Una [Parte](Std_Part/it.md) è internamente chiamata [App Part](App_Part/it.md) (`App::Part` class), e deriva da un [App GeoFeature](App_GeoFeature/it.md) (`App::GeoFeature` class), quindi condivide la maggior parte delle proprietà di quest\'ultimo.

Oltre alle proprietà descritte in [App GeoFeature](App_GeoFeature/it.md), la classe App Part ha alcune proprietà che la aiutano a gestire le informazioni nel contesto di un assieme, ad esempio, **Type**, **Id**, **License**, **LicenseURL**, **Color**, e **Group**.

Queste sono le proprietà disponibili nell\'[editore delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editore delle proprietà](property_editor/it.md).

### Dati


{{TitleProperty|Base}}

-    **Type|String**: una descrizione per questo oggetto. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Id|String**: un numero di identificazione o un numero di parte per questo oggetto. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **License|String**: un campo per specificare la licenza per questo oggetto. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **LicenseURL|String**: un campo per specificare l\'indirizzo web della licenza o del contratto per questo oggetto. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Color|Color**: una serie di quattro valori RGBA a virgola mobile white color.

-    **Placement|Placement**: la posizione dell\'oggetto nella [vista 3D](3D_view/it.md). Il posizionamento è definito da un punto `Base` (vettore), e una `Rotazione` (asse e angolo). Vedi [Posizionamento](Placement/it.md).

    -   
        **Angle**
        
        : l\'angolo di rotazione intorno al **Axis**. Per impostazione predefinita, è {{value|0°}} (zero gradi).

    -   
        **Axis**
        
        : il vettore che definisce l\'asse di rotazione per il posizionamento. Ogni componente è un valore in virgola mobile tra {{value|0}} e {{value|1}}. Se un valore è superiore a {{value|1}}, il vettore è normalizzato in modo che la grandezza del vettore sia {{value|1}}. Per impostazione predefinita, l\'asse Z è positivo, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : un vettore con coordinate 3D nel punto base. Per impostazione predefinita, è l\'origine {{value|(0, 0, 0)}}.

-    **Label|String**: il nome modificabile dall\'utente di questo oggetto, è una stringa arbitraria UTF8.

-    **Group|LinkList**: un elenco di oggetti di riferimento. Per impostazione predefinita, è vuoto {{value|[]}}.

#### Proprietà dati nascoste 

-    **Material|Map**: mappa con le proprietà del materiale. Per impostazione predefinita, è vuota {}.

-    **Meta|Map**: mappa con ulteriori meta-informazioni. Per impostazione predefinita, è vuota {}.

-    **Uid|UUID**: L\' [identificatore univoco universale](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (128-bit number) dell\'oggetto. Questo viene assegnato al momento della creazione.

-    **Label2|String**: una descrizione più lunga e modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria che può includere nuove linee. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Expression Engine|ExpressionEngine**: un elenco di espressioni. Per impostazione predefinita, è vuoto {{value|[]}}.

-    **Visibility|Bool**: se visualizzare o meno l\'oggetto.

-    **Origin|Link**: l\'oggetto [App Origin](App_Origin/it.md) è il riferimento posizionale per tutti gli elementi elencati in **Group**.

-    **_ Group Touched|Bool**: se il gruppo viene coinvolto o meno.

### Vista

La App Part ha solo cinque proprietà di base [App FeaturePython](App_FeaturePython/it.md), e non ha proprietà nascoste.


{{TitleProperty|Base}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. Se l\'opzione è {{value|Shape}}, l\'intera forma (vertici, bordi e facce) verrà evidenziata nella [vista 3D](3D_view/it.md); se è {{value|BoundBox}} verrà evidenziato solo il bounding box.

-    **Show In Tree|Bool**: se è `True`, l\'oggetto appare nella [vista ad albero](tree_view/it.md). Altrimenti, è impostato come invisibile.

-    **Visibility|Bool**: se è `True`, l\'oggetto appare nella [vista 3D](3D_view/it.md); altrimenti è invisibile. Per impostazione predefinita questa proprietà può essere attivata e disattivata premendo la barra **Spazio** sulla tastiera.

## Concetto di assemblaggio 

La Parte è destinata ad essere il blocco di base per la creazione di assemblaggi. A differenza di un [corpo di PartDesign](PartDesign_Body/it.md), un assemblaggio è inteso come un insieme di elementi separati e distinguibili che sono collegati in qualche modo nel mondo fisico, per esempio, attraverso la pressione, le viti o la colla.

Esempi che potrebbero essere Parti:

-   Un tavolo di legno che consiste di singoli pezzi di legno (gambe, piano), che sono messi insieme con colla o viti di metallo.
-   Un cuscinetto a sfere composto da più sfere d\'acciaio, un anello interno, un fermo, una guarnizione e un anello esterno.
-   Un assemblaggio di una vite con una rondella e un dado corrispondente.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*A sinistra: tre singoli solidi contigui, ciascuno modellato da un [Corpo di PartDesign](PartDesign_Body.md).
</br>
A destra: i singoli corpi messi insieme all'interno di una Parte per creare un assemblaggio.*

In termini generali, quando si importa un file STEP nel programma, l\'insieme principale e i suoi sottoinsiemi saranno importati come contenitori di Parti, ognuno dei quali contiene una semplice [Funzione Part](Part_Feature/it.md).

### Spiegazione dettagliata 

### Stato attivo 

Un documento aperto può contenere più Parti. Una parte attiva verrà visualizzata nella [vista ad albero](Tree_view/it.md) con il colore di sfondo specificato per il **Contenitore attivo**, per impostazione predefinita il colore in [editor delle preferenze](Preferences_Editor/it#Colori.md) è azzurro. Una parte attiva sarà anche mostrata in grassetto.

Per attivare o disattivare un Parte:

-   Doppio click nella [vista ad albero](Tree_view/it.md), oppure
-   Aprire il menu contestuale (click tasto destro) e selezionare **Attivare la parte**.


**Note:**

-   Lo {{emphasis|stato attivo}} delle Parti è stato sviluppato nella v0.17 in parallelo con lo {{emphasis|stato attivo}} dei [Corpo di PartDesign](PartDesign_Body/it.md); tuttavia, a partire dalla v0.19 per le Parti tale stato non ha un vero e proprio scopo.
-   Anche quando una Parte è attiva, gli oggetti appena creati non vengono posizionati automaticamente al suo interno. In questo caso, è sufficiente trascinare questi nuovi oggetti e rilasciarli sulla Parte desiderata.
-   Solo una Parte singola alla volta può essere attiva.

![](images/Std_Part_active.png )



*Documento con due Parti, di cui la seconda è attiva.*

### Origine

L\'Origine è costituita dai tre assi standard (X, Y, Z) e da tre piani standard (XY, XZ e YZ). A questi elementi possono essere collegati, al momento della creazione, [Schizzi](Sketch/it.md) e altri oggetti.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*A sinistra: Origine di Part nella [vista ad albero](tree_view/it.md).</br> A destra: rappresentazione degli elementi Origine nella [vista 3D](3D_view/it.md).*


**Nota:**

l\'origine è un oggetto [App Origin](App_Origin/it.md)(`App::Origin` class), mentre gli assi e i piani sono rispettivamente oggetti di tipo `App::Linea` e `App::Piano`. Ognuno di questi elementi può essere nascosto e non nascosto singolarmente con la barra **Spazio**; questo è utile per scegliere il riferimento corretto quando si creano altri oggetti.


**Nota 2:**

tutti gli elementi all\'interno della Parte sono riferiti all\'Origine della Parte, il che significa che la Parte può essere spostata e ruotata in riferimento al sistema globale di coordinate senza influenzare il posizionamento degli elementi all\'interno.

### Gestione della visibilità 

La visibilità della Parte sostituisce la visibilità di qualsiasi oggetto in essa contenuto. Se la Parte è nascosta, anche gli oggetti in essa contenuti saranno nascosti, anche se la loro proprietà individuale **Visibilità** è impostata su `True`. Se la Parte è visibile, allora la **Visibilità** di ogni oggetto determina se l\'oggetto è mostrato o meno.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*La visibilità della parte Std determina se gli oggetti raggruppati sotto di essa sono mostrati o meno nella [vista 3D ](3D_view/it.md).</br>A sinistra: la Parte è nascosta, quindi nessuno degli oggetti sarà mostrato nella [vista 3D](3D_view/it.md).</br>Destra: la Parte è visibile, quindi ogni oggetto controlla la propria visibilità.*

## Eredità

Una [Parte](Std_Part/it.md) è formalmente un\'istanza della classe `App::Part`, il cui genitore è il genitore di base [App GeoFeature](App_GeoFeature/it.md). (`App::GeoFeature` class), ed è incrementato con un\'estensione di Origine.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. La classe `App::Part* è un semplice contenitore che ha una posizione nello spazio 3D e ha un'origine per controllare il posizionamento degli oggetti raggruppati sotto di essa.`

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Funzione Part](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento.

Una Parte ([App Part](App_Part/it.md)) viene creata con il metodo del documento `addObject()`. Una volta che una Parte esiste, altri oggetti possono essere aggiunti ad essa con i metodi di questa Parte `addObject()` o `addObjects()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::Part", "Part")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

Non si può creare uno script `App::Part`. Tuttavia, è possibile aggiungere un ruolo `App::Part` a uno script `Part::FeaturePython` usando il seguente codice:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension('App::OriginGroupExtensionPython')
        obj.Origin = FreeCAD.ActiveDocument.addObject('App::Origin', 'Origin')

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension('Gui::ViewProviderOriginGroupExtensionPython')
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject('Part::FeaturePython', 'Group', group.MyGroup(), group.ViewProviderMyGroup(), True)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/it
