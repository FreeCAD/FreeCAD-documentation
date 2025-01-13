# Part Feature/it
## Introduzione

<img alt="" src=images/Part_3D_object.svg  style="width:32px;">

Un oggetto [Part Feature](Part_Feature/it.md), (Funzione Part) o formalmente un `Part::Feature`, è un elemento semplice a cui è associato una [forma topologica](Part_TopoShape/it.md) che può essere visualizzato nella [Vista 3D](3D_view/it.md).

La Part Feature è la classe genitore della maggior parte degli oggetti 2D (Draft, Sketcher) e 3D (Part, PartDesign), ad eccezione delle mesh, che normalmente si basano su [Mesh Feature](Mesh_Feature/it.md), o su [FEM FemMeshObject](FEM_Mesh/it.md) per gli oggetti FEM.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD*



## Utilizzo

[Part Feature](Part_Feature/it.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica, ma solo dalla [console Python](Python_console/it.md) come descritto nel paragrafo [Script](#Script.md).

L\'oggetto {{Incode|Part::Feature}} è definito in [Part](Part_Workbench/it.md) ma può essere usato come classe base per [script di oggetti](Scripted_objects/it.md) in tutti gli [ambienti](Workbenches/it.md) che producono forme geometriche 2D e 3D. Sostanzialmente tutti gli oggetti prodotti in [Part](Part_Workbench/it.md) sono istanze di una `Part::Feature`.


`Part::Feature`

è anche la classe genitrice dei [Corpi di PartDesign](PartDesign_Body/it.md), delle [PartDesign Features](PartDesign_Feature/it.md), e dei [Part Part2DObject](Part_Part2DObject/it.md), che è specializzato per le forme 2D (planari).

Gli ambienti possono aggiungere altre proprietà a questo elemento di base per produrre un oggetto con un comportamento complesso.



## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere oggetti con script.

La [Part Feature](Part_Feature/it.md) (classe `Part::Feature`) è derivata dalla base [App GeoFeature](App_GeoFeature/it.md) (classe`App::GeoFeature`) ed eredita tutte le sue proprietà. Ha anche diverse proprietà aggiuntive. In particolare una proprietà **Shape**, che memorizza la [Part TopoShape](Part_TopoShape/it.md) dell\'oggetto. Questa è la geometria mostrata nella [Vista 3D](3D_view.md). Altre proprietà di questo oggetto sono quelle legate all\'aspetto del suo [TopoShape](Part_TopoShape/it.md).

Queste sono le proprietà disponibili nell\'[editor delle proprietà](Property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell \'[editor delle proprietà](Property_editor/it.md).



### Dati


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: una classe personalizzata associata a questo oggetto. Questa esiste solo per la versione [Python](Python/it.md). Vedere [Script](#Script.md)

-    **Shape|PartShape|Hidden**: una classe [Part TopoShape](Part_TopoShape/it.md) associata a questo oggetto.

-    **Placement**: la posizione dell\'oggetto nella [Vista 3D](3D_view/it.md). Il posizionamento è definito da un punto `Base` (vettore) e una ` Rotation` (asse e angolo). Vedere [Posizionamento](Placement/it.md).

    -   
        **Angle**
        
        : l\'angolo di rotazione attorno al **Axis**. Di default, è {{value|0°}} (zero gradi).

    -   
        **Axis**
        
        : il vettore unitario che definisce l\'asse di rotazione per il posizionamento. Ogni componente ha un valore in virgola mobile compreso tra {{value|0}} e {{value|1}}. Se un valore è superiore a {{value|1}}, il vettore viene normalizzato in modo che l\'entità del vettore sia {{value|1}}. Di default, è l\'asse Z positivo, {{value|(0, 0, 1)}}

    -   
        **Position**
        
        : un vettore con le coordinate 3D del punto base. Di default, è l\'origine {{value|(0, 0, 0)}}

-    **Label|String**: il nome modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria.

-    **Label2|String|Hidden**: una descrizione più lunga e modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria che può includere ritorni a capo. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: un elenco di espressioni. Per impostazione predefinita, è vuoto {{value|[]}}.

-    **Visibility|Bool|Hidden**: se visualizzare o meno l\'oggetto.



### Vista

La maggior parte degli oggetti in FreeCAD ha quello che viene chiamato un \"[viewprovider](viewprovider/it.md)\", che è una classe che definisce l\'aspetto visivo dell\'oggetto nella [vista 3D](3D_view/it.md) e nella [vista ad albero](Tree_view/it.md). Il viewprovider predefinito degli oggetti Part Feature definisce le seguenti proprietà. Anche gli oggetti con script derivati da Part Feature hanno accesso a queste proprietà.


{{TitleProperty|Base}}

-    **Proxy|PythonObject|hidden**: una classe [viewprovider](Viewprovider/it.md) personalizzata associata a questo oggetto. Questo esiste solo per la versione [Python](Python/it.md). Vedere [Script](#Script.md).


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: se è `True`, l\'oggetto mostrerà il riquadro di delimitazione nella [Vista 3D](3D_view/it.md).

-    **Display Mode|Enumeration**: {{value|Flat Lines}} (visualizzazione normale), {{value|Shaded}} (senza bordi), {{value|Wireframe}} (senza facce), {{value|Points}} (solo vertici).

-    **Show In Tree|Bool**: il valore predefinito è `True`, nel qual caso l\'oggetto apparirà nella [Vista ad albero](Tree_view/it.md); in caso contrario, l\'oggetto verrà nascosto nella vista ad albero. Una volta che un oggetto nell\'albero è invisibile, lo si può vedere di nuovo aprendo il menu contestuale sopra il nome del documento (tasto destro) e selezionando {{CheckBox|TRUE|Mostra elementi nascosti}}. Quindi è possibile scegliere l\'elemento nascosto e **Show In Tree** può essere riportato a `True`.

-    **Visibility|Bool**: se è `True`, l\'oggetto appare nella [Vista 3D](3D_view/it.md); altrimenti è invisibile. Per impostazione predefinita, questa proprietà può essere attivata e disattivata premendo la barra **Space**.


{{TitleProperty|Object style}}

-    **Angular Deflection|Angle**: accompagna **Deviation**. È un altro modo per specificare la precisione con cui generare la mesh per il rendering sullo schermo o durante l\'esportazione. Il valore predefinito è {{value|28,5 degrees}} o {{value|0,5 radians}}. Questo è il valore massimo, minore è il valore più uniforme sarà l\'aspetto nella [Vista 3D](3D_view/it.md) e più fine sarà la mesh che verrà esportata.

-    **Deviation|FloatConstraint**: accompagna **Angular Deflection**. È un altro modo per specificare la precisione con cui generare la mesh per il rendering sullo schermo o durante l\'esportazione. Il valore predefinito è {{value|0,5%}}. Questo è il valore massimo, minore è il valore più uniforme sarà l\'aspetto nella [Vista 3D](3D_view/it.md) e più fine sarà la mesh che verrà esportata.

-    **Diffuse Color|ColorList|hidden**: è una lista di tuple RGB che definiscono i colori, simile a **Shape Color**. Il valore predefinito è un elenco di un {{value|[(0.8, 0.8, 0.8)]}}.

-    **Draw Style|Enumeration**: {{value|Solid}} (predefinito), {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; definisce lo stile dei bordi nella [Vista 3D](3D_view/it.md).

-    **Lighting|Enumeration**: {{value|Two side}} (predefinito), {{value|One side}}; l\'illuminazione proviene da due lati o da un lato nella [Vista 3D](3D_view/it.md).

-    **Line Color|Color**: una tupla di tre valori RGB in virgola mobile  almost black .

-    **Line Color Array|ColorList|hidden**: è una lista di tuple RGB che definiscono i colori, simile a **Line Color**. Il valore predefinito è un elenco di un {{value|[(0.09, 0.09, 0.09)]}}.

-    **Line Material|Material|hidden**: un [App Material](App_Material/it.md) associato ai bordi di questo oggetto. Per impostazione predefinita è vuoto.

-    **Line width|FloatConstraint**: un float che determina la larghezza in pixel dei bordi nella [Vista 3D](3D_view/it.md). Il valore predefinito è {{value|2.0}}.

-    **Point Color|Color**: simile a **Line Color**, definisce il colore dei vertici.

-    **Point Color Array|ColorList|hidden**: è una lista di tuple RGB che definiscono i colori, simile a **Point Color**. Il valore predefinito è un elenco di un {{value|[(0.09, 0.09, 0.09)]}}.

-    **Point Material|Material|hidden**: un [App Material](App_Material/it.md) associato ai vertici di questo oggetto. Per impostazione predefinita è vuoto.

-    **Point Size|FloatConstraint**: simile a **Line width**, definisce la dimensione dei vertici.

-    **Shape Color|Color**: simile a light gray.

-    **Shape Material|Material|hidden**: un [App Material](App_Material/it.md) associato a questo oggetto. Per impostazione predefinita è vuoto.

-    **Transparency|Percent**: un numero intero da {{value|0}} a {{value|100}} (una percentuale) che determina il livello di trasparenza delle facce nella [Vista 3D ](3D_view/it.md). Un valore di {{value|100}} indica facce completamente invisibili; le facce sono invisibili ma possono comunque essere selezionate purché **Selectable** sia `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: controlla il modo in cui avviene la selezione nella [Vista 3D](3D_view/it.md) se l\'oggetto ha una [Shape (forma)](Part_TopoShape/it.md) e ci sono molti oggetti oggetti parzialmente coperti da altri. Il valore predefinito è {{value|Disabled}}, il che significa che non verrà eseguita alcuna evidenziazione speciale; {{value|Enabled}} significa che l\'oggetto apparirà sopra qualsiasi altro oggetto quando selezionato; {{value|Object}} significa che l\'oggetto apparirà in primo piano solo se l\'intero oggetto è selezionato nella [Vista ad albero](Tree_view/it.md); {{value|Element}} significa che l\'oggetto apparirà in primo piano solo se un sottoelemento (vertice, bordo, faccia) è selezionato nella [Vista 3D](3D_view/it.md).

-    **Selectable|Bool**: se è `True`, l\'oggetto può essere selezionato con il puntatore nella [Vista 3D](3D_view/it.md). Altrimenti, l\'oggetto non potrà essere selezionato finché questa opzione non sarà impostata su `True`.

-    **Selection Style|Enumeration**: controlla il modo in cui l\'oggetto viene evidenziato. Se è {{value|Shape}}, l\'intera forma (vertici, bordi e facce) verrà evidenziata nella [Vista 3D](3D_view/it.md); se è {{value|BoundBox}} apparirà un riquadro di delimitazione che circonda l\'oggetto e sarà evidenziato.



### Deflessione e deviazione angolare 

<img alt="" src=images/View_property_Deviation.svg  style="width:500px;"> 
*Deflessione angolare e parametri di deviazione; d < deflessione lineare, α < deflessione angolare.*

La deviazione è un valore in percentuale correlato alle dimensioni in millimetri del parallelepipedo contenitore dell\'oggetto. La deviazione in millimetri può essere calcolata come segue:


```python
deviation_in_mm = (w + h + d)/3 * deviation/100
```

dove {{value|w}}, {{value|h}}, {{value|d}} sono le dimensioni del contenitore.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](Scripted_objects/it.md).

Un oggetto Part Feature viene creato con il metodo `addObject()` del documento.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Feature", "Name")
obj.Label = "Custom label"
```

Per la sottoclasse [Python](Python/it.md), si dovrebbe creare un oggetto `Part::FeaturePython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Name")
obj.Label = "Custom label"
```



### Nome

Vedere anche: [Nome oggetto](Object_name/it.md) per ulteriori informazioni sulle proprietà di `Name`.

Il metodo `addObject` ha due argomenti stringa di base.

-   Il primo argomento indica il tipo di oggetto, in questo caso, `"Part::FeaturePython"`.
-   Il secondo argomento è una stringa che definisce l\'attributo `Name`. Se non viene fornito, il valore predefinito è lo stesso nome della classe, ovvero `"Part__FeaturePython"`. `Name` può includere solo semplici caratteri alfanumerici e il carattere di sottolineatura, `[_0-9a-zA-Z]`. Se vengono forniti altri simboli, questi verranno convertiti in trattini bassi; ad esempio, `"A+B:C*"` viene convertito in `"A_B_C_"`.



### Etichetta

Se lo si desidera, l\'attributo `Label` può essere modificato in un testo più significativo.

-    `Label`può accettare qualsiasi stringa UTF8, inclusi accenti e spazi. Poiché la [Vista ad albero](Tree_view/it.md) mostra l\'`Label`, è una buona pratica cambiare l\'`Label` in una stringa più descrittiva.

-   Per impostazione predefinita, l\'`Label` è univoco, proprio come l\'`Name`. Tuttavia, questo comportamento può essere modificato nell\'[editor delle preferenze](Preferences_Editor/it.md), **Modifica → Preferenze → Generale → Documento → Consenti etichette oggetto duplicate in un documento**. Ciò significa che in generale l\'`Label` può essere ripetuto nello stesso documento; durante il test per un elemento specifico, l\'utente dovrebbe fare affidamento su `Name` anziché su `Label`.


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Feature/it
