# Part Feature/it



## Introduzione


{{TOCright}}

<img alt="" src=images/Part_3D_object.svg  style="width:32px;">

Un oggetto [Part Feature](Part_Feature/it.md), (Funzione Part) o formalmente un `Part::Feature`, è un elemento semplice a cui è associato una [forma topologica](Part_TopoShape/it.md) che può essere visualizzato nella [Vista 3D](3D_view/it.md).


<div class="mw-translate-fuzzy">

Una Part Feauture è la classe genitore della maggior parte degli oggetti 2D (Draft, Sketcher) e 3D (Part, PartDesign), ad eccezione delle mesh, che normalmente si basano su [Mesh Feature](Mesh_Feature/it.md), o [Fem FemMeshObject](Fem_FemMeshObject/it.md) per gli oggetti FEM.


</div>

Ogni oggetto creato con [Part](Part_Workbench/it.md) è essenzialmente una [Part Feature](Part_Feature/it.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD. La classe `Part::Feature* è l'origine della maggior parte degli oggetti 2D (Draft, Sketcher) e 3D (Part, PartDesign) per avere una [Part TopoShape](Part_TopoShape/it.md).`

## Utilizzo

[Part Feature](Part_Feature/it.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica, ma solo dalla [console Python](Python_console/it.md) come descritto nel paragrafo [Script](Part_Feature/it#Script.md).

L\'oggetto {{Incode|Part::Feature}} è definito in [Part](Part_Workbench/it.md) ma può essere usato come classe base per [script di oggetti](scripted_objects/it.md) in tutti gli [ambienti](Workbenches/it.md) che producono forme geometriche 2D e 3D. Sostanzialmente tutti gli oggetti prodotti in [Part](Part_Workbench/it.md) sono istanze di una `Part::Feature`. Gli oggetti solidi importati da file STEP o BREP sono importati utilizzando [Part](Part_Workbench/it.md), quindi sono anche importati come elementi `Part::Feature` sebbene senza cronologia parametrica.


`Part::Feature`

è anche la classe genitrice dei [Corpi di PartDesign](PartDesign_Body/it.md), delle [PartDesign Features](PartDesign_Feature/it.md), e dei [Part Part2DObject](Part_Part2DObject/it.md), che è specializzato per le forme 2D (planari).

Un oggetto `Part::Feature` ha proprietà semplici come il [posizionamento](Placement/it.md) e le proprietà vista per definire l\'aspetto dei suoi vertici, bordi e facce. Gli ambienti possono aggiungere altre proprietà a questo elemento di base per produrre un oggetto con un comportamento complesso.

## Proprietà

Una [Part Feature](Part_Feature/it.md) (classe `Part::Feature`) è derivata dalla base [App GeoFeature](App_GeoFeature/it.md) (classe`App::GeoFeature`), pertanto condivide la maggior parte delle proprietà di quest\'ultima.


<div class="mw-translate-fuzzy">

Oltre alle proprietà descritte in [App GeoFeature](App_GeoFeature/it.md), Part Feature ha la proprietà {{PropertyData/it|Shape}}, che memorizza la [Part TopoShape](Part_TopoShape/it.md) di questi oggetti, che è la geometria mostrata nella [vista 3D](3D_view/it.md).


</div>

Altre proprietà di questo oggetto sono quelle relative all\'aspetto della sua [TopoShape](Part_TopoShape/it.md), che comprende **Angular Deflection**, **Deviation**, **Draw Style**, **Lighting**, **Line Color**, **Line Width**, **Point Color**, **Point Size**, e anche le proprietà nascoste **Diffuse Color**, **Line Color Array**, **Line Material**, **Point Color Array**, e **Point Material**.

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere oggetti con script.

Queste sono le proprietà disponibili nell\'[editor delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell \'[editor delle proprietà](property_editor/it.md).

### Dati


{{TitleProperty|Base}}

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

#### Proprietà dati nascoste 


<div class="mw-translate-fuzzy">

-    **Expression Engine|ExpressionEngine|hidden**: un elenco di espressioni. Di default, è vuota {{value|[]}}.

-    **Label2|String|hidden**: una descrizione più lunga e modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria che può includere nuove righe. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Proxy|PythonObject|hidden**: una classe personalizzata associata a questo oggetto. Questa esiste solo per la versione [Python](Python/it.md). Vedere [Script](Part_Feature/it#Script.md).

-    **Shape|PartShape|hidden**: una classe [Part TopoShape](Part_TopoShape/it.md) associata a questo oggetto.

-    **Visibility|Bool|hidden**: se visualizzare o no l\'oggetto.


</div>

### Vista


<div class="mw-translate-fuzzy">

La maggior parte degli oggetti in FreeCAD ha quello che viene chiamato un \"fornitore di viste\", che è una classe che definisce l\'aspetto visivo dell\'oggetto nella [vista 3D](3D_view/it.md) e nella [vista ad albero](tree_view/it.md). Il fornitore di viste predefinito degli oggetti Part Feature definisce le seguenti proprietà. Anche gli oggetti con script derivati da Part Feature hanno accesso a queste proprietà.


</div>


{{TitleProperty|Base}}

-    **Proxy|PythonObject|hidden**: a custom [viewprovider](viewprovider.md) class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Part_Feature#Scripting.md).


<div class="mw-translate-fuzzy">


{{TitleProperty|Base}}


</div>

-    **Bounding Box|Bool**: if it is `True`, the object will show the bounding box in the [3D view](3D_view.md).

-    **Display Mode|Enumeration**: {{value|Flat Lines}} (regular visualization), {{value|Shaded}} (no edges), {{value|Wireframe}} (no faces), {{value|Points}} (only vertices).

-    **Show In Tree|Bool**: it defaults to `True`, in which case the object will appear in the [tree view](tree_view.md); otherwise, the object will be hidden in the tree view. Once an object in the tree is invisible, you can see it again by opening the context menu over the name of the document (right-click), and selecting {{CheckBox|TRUE|Show hidden items}}. Then the hidden item can be chosen and **Show In Tree** can be switched back to `True`.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


{{TitleProperty|Object style}}


<div class="mw-translate-fuzzy">

-    **Angular Deflection**: accompagna **Deviation**. È un altro modo per specificare la precisione con cui generare la mesh per il rendering sullo schermo o durante l\'esportazione. Il valore predefinito è 28,5 gradi o 0,5 radianti. Minore è il valore, più uniforme sarà l\'aspetto nella [vista 3D](3D_view/it.md) e più fine sarà la mesh che verrà esportata.

-    **Bounding Box**: se è `True`, l\'oggetto mostra il parallelepipedo che lo contiene nella [vista 3D](3D_view/it.md).

-    **Deviation**: accompagna **Angular Deflection**. È un altro modo per specificare la precisione con cui generare la mesh per il rendering sullo schermo o durante l\'esportazione. Il valore predefinito è 28,5 gradi o 0,5 radianti. Minore è il valore, più uniforme sarà l\'aspetto nella [vista 3D](3D_view/it.md) e più fine sarà la mesh che verrà esportata.

-    **Display Mode**: Flat lines (visualizzazione normale con facce piene), Ombreggiato (bordi leggeri), Wireframe (solo reticolo e facce vuote), Punti (solo vertici).

-    **Draw Style**: Solid, Dashed, Dotted, Dashdot; definisce lo stile dei bordi nella [vista 3D](3D_view/it.md).

-    **Lighting**: Two side, One side; l\'illuminazione proviene da due lati o un lato nella [vista 3D](3D_view/it.md).

-    **Line Color**: una tupla di tre valori `(r,g,b)` per definire il colore dei bordi nella [vista 3D](3D_view/it.md).

-    **Line Width**: un flottante che determina la larghezza in pixel dei bordi nella [vista 3D](3D_view/it.md).

-    **On Top When Selected**: Disabled, Enabled, Object, Element.

-    **Point Color**: una tupla di tre valori `(r,g,b)` per definire il colore dei vertici nella [vista 3D](3D_view/it.md).

-    **Point Size**: un flottante che determina la dimensione in pixel dei vertici nella [vista 3D](3D_view/it.md).

-    **Selectable**: se è `True`, l\'oggetto può essere selezionato con il puntatore nella [vista 3D](3D_view/it.md). Altrimenti, l\'oggetto non può essere selezionato fino a quando questa opzione non è impostata su `True`.

-    **Selection Style**: Shape, BoundBox.

-    **Shape Color**: una tupla di tre valori `(r,g,b)` per definire il colore delle facce nella [vista 3D](3D_view/it.md).

-    **Show In Tree**: se è `True`, l\'oggetto appare nella [vista ad albero](tree_view/it.md). Altrimenti, è impostato come invisibile.

-    **Transparency**: un valore da 0 a 100 che determina il livello di trasparenza delle facce nella [vista 3D](3D_view/it.md). Un valore di 100 indica facce completamente invisibili; le facce che sono invisibili possono comunque essere selezionate se **Selectable** è `True`.

-    **Visibility**: se è `True`, l\'oggetto appare nella [vista 3D](3D_view/it.md); altrimenti non è visibile. Per impostazione predefinita, questa proprietà può essere attivata e disattivata premendo la barra **Spazio** sulla tastiera.


</div>

La deviazione è un valore in percentuale correlato alle dimensioni in millimetri del parallelepipedo contenitore dell\'oggetto. La deviazione in millimetri può essere calcolata come segue: 
```python
deviation_in_mm = (w + h + d)/3 * deviation/100
``` dove {{value|w}}, {{value|h}}, {{value|d}} sono le dimensioni del contenitore.

-    **Draw Style|Enumeration**: {{value|Solid}} (default), {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; defines the style of the edges in the [3D view](3D_view.md).

-    **Lighting|Enumeration**: {{value|Two side}} (default), {{value|One side}}; the illumination comes from two sides or one side in the [3D view](3D_view.md).

-    **Line Color|Color**: a tuple of three floating point RGB values  almost black .

-    **Line Color Array|ColorList|hidden**: it is a list of RGB tuples defining colors, similar to **Line Color**. It defaults to a list of one {{value|[(0.09, 0.09, 0.09)]}}.

-    **Line Material|Material|hidden**: an [App Material](App_Material.md) associated with the edges in this object. By default it is empty.

-    **Line Width|FloatConstraint**: a float that determines the width in pixels of the edges in the [3D view](3D_view.md). It defaults to {{value|2.0}}.

-    **Point Color|Color**: similar to **Line Color**, defines the color of the vertices.

-    **Point Color Array|ColorList|hidden**: it is a list of RGB tuples defining colors, similar to **Point Color**. It defaults to a list of one {{value|[(0.09, 0.09, 0.09)]}}.

-    **Point Material|Material|hidden**: an [App Material](App_Material.md) associated with the vertices in this object. By default it is empty.

-    **Point Size|FloatConstraint**: similar to **Line Width**, defines the size of the vertices.

-    **Shape Color|Color**: similar to light gray.

-    **Shape Material|Material|hidden**: an [App Material](App_Material.md) associated with this object. By default it is empty.

-    **Transparency|Percent**: an integer from {{value|0}} to {{value|100}} (a percentage) that determines the level of transparency of the faces in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible faces; the faces are invisible but they can still be picked as long as **Selectable** is `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: it controls the way in which the selection occurs in the [3D view](3D_view.md) if the object has a [Shape](Part_TopoShape.md), and there are many objects partially covered by others. It defaults to {{value|Disabled}}, meaning that no special highlighting will occur; {{value|Enabled}} means that the object will appear on top of any other object when selected; {{value|Object}} means that the object will appear on top only if the entire object is selected in the [tree view](tree_view.md); {{value|Element}} means that the object will appear on top only if a subelement (vertex, edge, face) is selected in the [3D view](3D_view.md).

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Selection Style|Enumeration**: it controls the way the object is highlighted. If it is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} a bounding box will appear surrounding the object and will be highlighted.

### Deviation value 

<img alt="" src=images/View_property_Deviation.svg  style="width:500px;"> *Deflection parameters of `BRepMesh_IncrementalMesh* algorithm; d < linear deflection, α < angular deflection.`

See the forum thread, [Deviation and Angular deflection](https://forum.freecadweb.org/viewtopic.php?f=3&t=45512).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Un oggetto Part Feature viene creato con il metodo `addObject()` del documento. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Feature", "Name")
obj.Label = "Custom label"
```

This basic `Part::Feature` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `Part::FeaturePython` object. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Name")
obj.Label = "Custom label"
```

### Name


**See also:**

[Object name](Object_name.md), for more information on the properties of the Name.

The `addObject` function has two basic string arguments.


<div class="mw-translate-fuzzy">

-   Il primo argomento indica il tipo di oggetto, in questo caso, `"Part::Feature"`.
-   Il secondo argomento è una stringa che definisce l\'attributo `Name`. Se non viene fornito, per impostazione predefinita è `"Part__Feature"`.
    -   Il {{Incode|Name}} viene stabilito al momento della creazione; non può essere modificato in seguito.
    -   Il `Name` può includere solo caratteri alfanumerici semplici e il trattino basso, `[_0-9a-zA-Z]`. Se vengono forniti altri simboli, questi verranno convertiti in caratteri di sottolineatura; per esempio, `"A+B:C*"` viene convertito in `"A_B_C_"`.
    -   Il `Name` deve essere unico in tutto il documento. Se vengono creati più oggetti con lo stesso nome, viene aggiunto un numero sequenziale per distinguerli, ad esempio, `"Name001"`, `"Name002"`, etc.
-   Se lo si desidera, l\'attributo `Label` può essere modificato in un testo più significativo.
    -   Di default, `Label` è uguale a `Name`.
    -   A differenza di `Name`, `Label` può accettare qualsiasi stringa UTF8, inclusi accenti e spazi. Poiché la [vista ad albero](tree_view/it.md) visualizza `Label`, è buona norma cambiare `Label` in una stringa più descrittiva.
    -   Di default, `Label` deve essere univoco. Questo comportamento può essere modificato nell\'[editor delle preferenze](Preferences_Editor/it.md), {{MenuCommand | Modifica → Preferenze → Generale → Documento → Consenti la duplicazione delle etichette nel documento}}.


</div>

### Label

If desired, the `Label` attribute can be changed to a more meaningful text.

-   The `Label` can accept any UTF8 string, including accents and spaces. Since the [tree view](tree_view.md) displays the `Label`, it is a good practice to change the `Label` to a more descriptive string.
-   By default the `Label` is unique, just like the `Name`. However, this behavior can be changed in the [preferences editor](Preferences_Editor.md), **Edit → Preferences → General → Document → Allow duplicate object labels in one document**. This means that in general the `Label` may be repeated in the same document; when testing for a specific element the user should rely on the `Name` rather than on the `Label`.


 {{Document objects navi}} 
