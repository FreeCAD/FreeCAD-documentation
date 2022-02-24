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


<div class="mw-translate-fuzzy">

Lo strumento Parte non è definito da un particolare ambiente di lavoro, ma dal sistema base; di conseguenza lo si trova nella **barra degli strumenti struttura**, che è disponibile in tutti gli [ambienti di lavoro](Workbenches/it.md). Per raggruppare gli oggetti arbitrariamente senza considerare la loro posizione, utilizzare <img alt="" src=images/Std_Group.svg  style="width:16px;"> [Gruppo](Std_Group/it.md); questo oggetto non influenza i posizionamenti degli elementi che contiene, è essenzialmente solo una cartella che viene utilizzata per mantenere organizzata la [vista ad albero](tree_view/it.md).


</div>

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )


<div class="mw-translate-fuzzy">



*A sinistra: elementi all'interno di una Parte nella vista ad albero. A destra: oggetti posizionati nello spazio, riferiti all'Origine della Parte.*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)**. Viene creata una parte vuota che diventa automaticamente *[attiva](Std_Part/it#Stato_attivo.md)*.
2.  Per aggiungere oggetti a una parte, trascinarli e rilasciarli sulla parte nella [vista ad albero](tree_view/it.md).
3.  Per rimuovere oggetti da una parte, trascinarli fuori dalla parte e sull\'etichetta del documento nella parte superiore della [vista ad albero](tree_view/it.md).


</div>


<div class="mw-translate-fuzzy">

### Note


</div>


<div class="mw-translate-fuzzy">

-   A partire dalla v0.19, un dato oggetto può appartenere solo ad una singola Parte.
-   Fare doppio clic sulla Parte nella [vista ad albero](tree_view/it.md) o aprire il menu contestuale (tasto destro del mouse) e selezionare **Attiva/disattiva la parte** per attivare o disattivare la Parte. Se un\'altra Parte è attiva, sarà disattivata. Vedere [Stato attivo](Std_Part/it#Stato_attivo.md) per maggiori informazioni.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Una [Parte](Std_Part/it.md) è internamente chiamata [App Part](App_Part/it.md) (`App::Part` class), e deriva da un [App GeoFeature](App_GeoFeature/it.md) (`App::GeoFeature` class), quindi condivide la maggior parte delle proprietà di quest\'ultimo.


</div>


<div class="mw-translate-fuzzy">

Queste sono le proprietà disponibili nell\'[editore delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editore delle proprietà](property_editor/it.md).


</div>

### Dati


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

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


</div>

### Vista


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [Tree view](Tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

### Spiegazione dettagliata 

### Stato attivo 


<div class="mw-translate-fuzzy">

Un documento aperto può contenere più Parti. Una parte attiva verrà visualizzata nella [vista ad albero](Tree_view/it.md) con il colore di sfondo specificato per il **Contenitore attivo**, per impostazione predefinita il colore in [editor delle preferenze](Preferences_Editor/it#Colori.md) è azzurro. Una parte attiva sarà anche mostrata in grassetto.


</div>


<div class="mw-translate-fuzzy">

Per attivare o disattivare un Parte:

-   Doppio click nella [vista ad albero](Tree_view/it.md), oppure
-   Aprire il menu contestuale (click tasto destro) e selezionare **Attivare la parte**.


</div>

![](images/Std_Part_active.png )



*Documento con due Parti, di cui la seconda è attiva.*

### Origine

L\'Origine è costituita dai tre assi standard (X, Y, Z) e da tre piani standard (XY, XZ e YZ). A questi elementi possono essere collegati, al momento della creazione, [Schizzi](Sketch/it.md) e altri oggetti.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )


<div class="mw-translate-fuzzy">



*A sinistra: Origine di Part nella [vista ad albero](tree_view/it.md).</br> A destra: rappresentazione degli elementi Origine nella [vista 3D](3D_view/it.md).*


</div>


<div class="mw-translate-fuzzy">


**Nota:**

l\'origine è un oggetto [App Origin](App_Origin/it.md)(`App::Origin` class), mentre gli assi e i piani sono rispettivamente oggetti di tipo `App::Linea` e `App::Piano`. Ognuno di questi elementi può essere nascosto e non nascosto singolarmente con la barra **Spazio**; questo è utile per scegliere il riferimento corretto quando si creano altri oggetti.


</div>


**Nota 2:**

tutti gli elementi all\'interno della Parte sono riferiti all\'Origine della Parte, il che significa che la Parte può essere spostata e ruotata in riferimento al sistema globale di coordinate senza influenzare il posizionamento degli elementi all\'interno.

### Gestione della visibilità 

La visibilità della Parte sostituisce la visibilità di qualsiasi oggetto in essa contenuto. Se la Parte è nascosta, anche gli oggetti in essa contenuti saranno nascosti, anche se la loro proprietà individuale **Visibilità** è impostata su `True`. Se la Parte è visibile, allora la **Visibilità** di ogni oggetto determina se l\'oggetto è mostrato o meno.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*La visibilità della parte Std determina se gli oggetti raggruppati sotto di essa sono mostrati o meno nella [vista 3D ](3D_view/it.md).</br>A sinistra: la Parte è nascosta, quindi nessuno degli oggetti sarà mostrato nella [vista 3D](3D_view/it.md).</br>Destra: la Parte è visibile, quindi ogni oggetto controlla la propria visibilità.*

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).


</div>

Vedere [Funzione Part](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento.


<div class="mw-translate-fuzzy">

Una Parte ([App Part](App_Part/it.md)) viene creata con il metodo del documento `addObject()`. Una volta che una Parte esiste, altri oggetti possono essere aggiunti ad essa con i metodi di questa Parte `addObject()` o `addObjects()`.


</div>


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">

Non si può creare uno script `App::Part`. Tuttavia, è possibile aggiungere un ruolo `App::Part` a uno script `Part::FeaturePython` usando il seguente codice:


</div>


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
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

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
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             group.MyGroup(),
                             group.ViewProviderMyGroup(),
                             True)
```





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/it
