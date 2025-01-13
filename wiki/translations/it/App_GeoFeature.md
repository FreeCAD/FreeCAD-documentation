# App GeoFeature/it
## Introduzione

<img alt="" src=images/Feature.svg  style="width:32px;">

Un oggetto [App GeoFeature](App_GeoFeature/it.md), o formalmente un `App::GeoFeature`, è la classe base della maggior parte degli oggetti che visualizzano elementi geometrici nella [vista 3D](3D_view/it.md) perché include una proprietà {{PropertyData/it|Posizionamento}}.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD*



## Utilizzo

[App GeoFeature](App_GeoFeature/it.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica. In genere non è pensato per essere utilizzato direttamente, ma può essere suddiviso in sottoclassi per ottenere un oggetto vuoto che ha solo la proprietà di base **Placement** per definire la sua posizione nella [vista 3D](3D_view/it.md) .

Alcuni degli oggetti derivati più importanti sono i seguenti:

-   La classe [Part Feature](Part_Feature/it.md), il genitore della maggior parte degli oggetti con [forme topologiche](Part_TopoShape/it.md) 2D e 3D.
-   La classe [Mesh Feature](Mesh_Feature/it.md), il genitore della maggior parte degli oggetti realizzati da [mesh](Mesh_MeshObject/it.md), non solidi.
-   La classe [Fem FemMeshObject](FEM_Mesh/it.md), il genitore delle mesh di elementi finiti create con l\'ambiente [FEM](FEM_Workbench/it.md).
-   La classe [CAM Feature](CAM_Feature/it.md), il genitore dei percorsi creati con l\'ambiente [CAM](CAM_Workbench/it.md) per l\'uso nella lavorazione CNC.
-   La classe [App Part](App_Part/it.md), che definisce [Std Parts](Std_Part/it.md) che può essere utilizzato come contenitore di corpi per eseguire assiemi.

Quando si crea questo oggetto in [Python](Python/it.md), invece di sottoclassare `App::GeoFeature`, è necessario sottoclassare `App::GeometryPython` perché quest\'ultimo include di default un provider di visualizzazione e gli attributi `Proxy` per l\'oggetto stesso e il relativo provider di visualizzazione. Vedere [Script](App_GeoFeature/it#Script.md).



## Proprietà App GeoFeature 

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

L\'oggetto [App GeoFeature](App_GeoFeature/it.md) (classe `App::GeoFeature`) è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject/it.md) (classe `App::DocumentObject`) ed eredita tutte le sue proprietà. Inoltre ha una proprietà **Placement**, che controlla la sua posizione nella [3D view](3D_view.md).



## Proprietà App GeometryPython 

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

La classe [App GeometryPython](App_GeoFeature.md) (`App::GeometryPython`) è derivata dalla classe di base [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature`) ed eredita tutte le sue proprietà. Ha anche diverse proprietà aggiuntive.

Queste sono le proprietà disponibili nell\'[editor delle proprietà](Property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editor delle proprietà](Property_editor/it.md).



### Dati


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: una classe personalizzata associata a questo oggetto.

-    **Placement|Placement**: la posizione dell\'oggetto nella [vista 3D](3D_view/it.md). Il posizionamento è definito da un punto `Base` (vettore) e da una `Rotazione` (asse e angolo). Vedi [Posizionamento](Placement/it.md).

    -   
        **Angle**
        
        : l\'angolo di rotazione attorno a **Axis**. Per impostazione predefinita, è {{value|0°}} (zero gradi).

    -   
        **Axis**
        
        : il vettore unitario che definisce l\'asse di rotazione per il posizionamento. Ogni componente è un valore in virgola mobile compreso tra {{value|0}} e {{value|1}}. Se qualsiasi valore è superiore a {{value|1}}, il vettore viene normalizzato in modo che la grandezza del vettore sia {{value|1}}. Per impostazione predefinita, è l\'asse Z positivo, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : un vettore con le coordinate 3D del punto base. Per impostazione predefinita, è l\'origine {{value|(0, 0, 0)}}.

-    **Label|String**: il nome modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria.

-    **Label2|String|Hidden**: una descrizione di questo oggetto più lunga e modificabile dall\'utente, è una stringa UTF8 arbitraria che può includere ritorni a capo. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: un elenco di espressioni. Per impostazione predefinita, è vuoto {{value|[]}}.

-    **Visibility|Bool|Hidden**: se visualizzare o meno l\'oggetto.



### Vista


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: una classe [viewprovider](Viewprovider/it.md) personalizzata associata a questo oggetto.


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: se è `True`, l\'oggetto mostrerà il riquadro di delimitazione nella [vista 3D](3D_view/it.md).

-    **Display Mode|Enumeration|Enumeration**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).

-    **Show In Tree|Bool**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).

-    **Visibility|Bool**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).


{{TitleProperty|Object Style}}

-    **Shape Color|Color**: una tupla di tre valori RGB in virgola mobile  grigio chiaro .

-    **Shape Material|Material|Hidden**: un [App Material](App_Material/it.md) associato a questo oggetto. Per impostazione predefinita è vuoto.

-    **Transparency|Percent**: un numero intero da {{value|0}} a {{value|100}} che determina il livello di trasparenza delle facce nella [vista 3D](3D_view/it.md). Un valore di {{value|100}} indica facce completamente invisibili; le facce sono invisibili ma possono comunque essere selezionate purché **Selectable** sia `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).

-    **Selectable|Bool**: se è `True`, l\'oggetto può essere selezionato con il puntatore nella [vista 3D](3D_view/it.md). Altrimenti, l\'oggetto non potrà essere selezionato finché questa opzione non sarà impostata su `True`.

-    **Selection Style|Enumeration**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](Scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento.

Una GeoFeature viene creata con il metodo `addObject()` del documento. Se si desidera creare un oggetto con una [forma topologica](Part_TopoShape/it.md) 2D o 3D, potrebbe essere meglio creare una delle sottoclassi specializzate per la gestione delle forme, ad esempio [Part Feature](Part_Feature/it.md) o [Part Part2DObject](Part_Part2DObject/it.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

Per la sottoclasse [Python](Python/it.md) si dovrebbe creare l\'oggetto `App::GeometryPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeometryPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App GeoFeature/it
