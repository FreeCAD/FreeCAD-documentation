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
-   La classe [Path Feature](Path_Feature/it.md), il genitore dei percorsi creati con l\'ambiente [Path](Path_Workbench/it.md) per l\'uso nella lavorazione CNC.
-   La classe [App Part](App_Part/it.md), che definisce [Std Parts](Std_Part/it.md) che può essere utilizzato come contenitore di corpi per eseguire assiemi.

Quando si crea questo oggetto in [Python](Python/it.md), invece di sottoclassare `App::GeoFeature`, è necessario sottoclassare `App::GeometryPython` perché quest\'ultimo include di default un provider di visualizzazione e gli attributi `Proxy` per l\'oggetto stesso e il relativo provider di visualizzazione. Vedere [Script](App_GeoFeature/it#Script.md).

## Proprietà App GeoFeature 

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

L\'oggetto [App GeoFeature](App_GeoFeature/it.md) (classe `App::GeoFeature`) è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject/it.md) (classe `App::DocumentObject`) ed eredita tutte le sue proprietà. Inoltre ha una proprietà **Placement**, che controlla la sua posizione nella [3D view](3D_view.md).

## Proprietà App GeometryPython 

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

La classe [App GeometryPython](App_GeoFeature.md) (`App::GeometryPython`) è derivata dalla classe di base [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature`) ed eredita tutte le sue proprietà. Ha anche diverse proprietà aggiuntive.


<div class="mw-translate-fuzzy">

Queste sono le proprietà disponibili nell\'[editor delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editor delle proprietà](property_editor/it.md).


</div>

### Dati


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object.

-    **Placement|Placement**: the position of the object in the [3D view](3D_view.md). The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

    -   
        **Angle**
        
        : the angle of rotation around the **Axis**. By default, it is {{value|0°}} (zero degrees).

    -   
        **Axis**
        
        : the unit vector that defines the axis of rotation for the placement. Each component is a floating point value between {{value|0}} and {{value|1}}. If any value is above {{value|1}}, the vector is normalized so that the magnitude of the vector is {{value|1}}. By default, it is the positive Z axis, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : a vector with the 3D coordinates of the base point. By default, it is the origin {{value|(0, 0, 0)}}.

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string.

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

### Vista


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom [viewprovider](Viewprovider.md) class associated with this object.


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: if it is `True`, the object will show the bounding box in the [3D view](3D_view.md).

-    **Display Mode|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Show In Tree|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Visibility|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).


{{TitleProperty|Object Style}}

-    **Shape Color|Color**: a tuple of three floating point RGB values  light gray .

-    **Shape Material|Material|Hidden**: an [App Material](App_Material.md) associated with this object. By default it is empty.

-    **Transparency|Percent**: an integer from {{value|0}} to {{value|100}} that determines the level of transparency of the faces in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible faces; the faces are invisible but they can still be picked as long as **Selectable** is `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Selection Style|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

## Script


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A GeoFeature is created with the `addObject()` method of the document. If you would like to create an object with a 2D or 3D [topological shape](Part_TopoShape.md), it may be better to create one of the sub-classes specialized for handling shapes, for example [Part Feature](Part_Feature.md) or [Part Part2DObject](Part_Part2DObject.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

For [Python](Python.md) subclassing you should create the `App::GeometryPython` object.


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
