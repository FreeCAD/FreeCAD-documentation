# App DocumentObject/it
## Introduzione

<img alt="" src=images/Px.svg  style="width:32px;">

Un oggetto [App DocumentObject](App_DocumentObject/it.md), o formalmente un `App::DocumentObject`, è la classe di base di tutte le classi di oggetti gestite nel documento.

In termini generali, un \"DocumentObject\" è qualsiasi \"cosa\" che può apparire nella [Vista ad albero](Tree_view/it.md) e che viene salvata e ripristinata all\'apertura di un documento.

![](images/App_DocumentObject_example.png )



*Vista ad albero che mostra diversi oggetti nel documento. Ognuno di essi è un "oggetto documento", derivato in definitiva dalla classe di base `App::DocumentObject*.`

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD*



## Utilizzo

[App DocumentObject](App_DocumentObject/it.md) è una classe interna, quindi non può essere creata dall\'interfaccia grafica, né deve essere utilizzata da sola. Definisce semplicemente il comportamento e le proprietà di base degli oggetti nel programma.

Alcuni dei DocumentObjects più importanti sono i seguenti:

-   La classe [App FeaturePython](App_FeaturePython/it.md), un oggetto vuoto che può essere utilizzato per scopi diversi, a seconda delle proprietà aggiunte.
-   La classe [App GeoFeature](App_GeoFeature/it.md), l\'oggetto base di tutti gli oggetti geometrici, ovvero di oggetti che hanno una proprietà [Posizionamento](Placement/it.md) che definisce la loro posizione nella [Vista 3D](3D_view/it.md).
-   La classe [Part Feature](Part_Feature/it.md), derivata da App GeoFeature e dalla classe padre di oggetti con [forme topologiche](Part_TopoShape/it.md) 2D e 3D.
-   La classe [Mesh Feature](Mesh_Feature/it.md), derivata da App GeoFeature e dalla classe padre di oggetti con [mesh](Mesh_MeshObject/it.md) 2D e 3D.



## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

Queste sono le proprietà di base che essenzialmente hanno tutti gli oggetti. È possibile accedere a queste proprietà dalla [console Python](Python_console/it.md).

-    **Label|String**: il nome di questo oggetto modificabile dall\'utente, è una stringa UTF8 arbitraria. Di default, è uguale al `Name`.

-    **Label2|String**: una descrizione modificabile dall\'utente più lunga di questo oggetto, è una stringa UTF8 arbitraria che può includere nuove righe. Di default, è una stringa vuota {{value|""}}.

-    **Expression Engine|ExpressionEngine**: un elenco di espressioni.

-    **Visibility|Bool**: se visualizzare l\'oggetto o no.

Per gli oggetti derivati, solo la proprietà **Label** verrà elencata di default nell\'[editor delle proprietà](property_editor/it.md). Le altre proprietà saranno nascoste.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](Scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento.

Un DocumentObject viene creato con il metodo `addObject()` del documento. Tuttavia, in generale, non è necessario creare questo oggetto manualmente. Di solito è meglio sottoclassare una delle sottoclassi più complesse, per esempio, [App FeaturePython](App_FeaturePython/it.md), [App GeoFeature](App_GeoFeature/it.md), [Part Feature](Part_Feature/it.md), [Part Part2DObject](Part_Part2DObject/it.md), etc.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObject", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App DocumentObject/it
