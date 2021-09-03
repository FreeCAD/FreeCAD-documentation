

## Introduzione

<img alt="" src=images/Feature.svg  style="width:32px;">

Un oggetto [App GeoFeature](App_GeoFeature/it.md), o formalmente un `App::GeoFeature`, è la classe base della maggior parte degli oggetti che visualizzano elementi geometrici nella [vista 3D](3D_view/it.md) perché include la proprietà {{PropertyData/it|Posizionamento}}.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. La classe `App::GeoFeature* è essenzialmente la classe base di tutti gli oggetti nel software che mostrano una geometria nella [vista 3D](3D_view/it.md).`

## Utilizzo

[App GeoFeature](App_GeoFeature/it.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica. In genere non è pensato per essere utilizzato direttamente, ma può essere suddiviso in sottoclassi per ottenere un oggetto vuoto che ha solo la proprietà di base **Placement** per definire la sua posizione nella [vista 3D](3D_view/it.md) .

Alcuni degli oggetti derivati più importanti sono i seguenti:

-   La classe [Part Feature](Part_Feature/it.md), il genitore della maggior parte degli oggetti con [forme topologiche](Part_TopoShape/it.md) 2D e 3D.
-   La classe [Mesh Feature](Mesh_Feature/it.md), il genitore della maggior parte degli oggetti realizzati da [mesh](Mesh_MeshObject/it.md), non solidi.
-   La classe [Fem FemMeshObject](FEM_Mesh/it.md), il genitore delle mesh di elementi finiti create con l\'ambiente [FEM](FEM_Workbench/it.md).
-   La classe [Path Feature](Path_Feature/it.md), il genitore dei percorsi creati con l\'ambiente [Path](Path_Workbench/it.md) per l\'uso nella lavorazione CNC.
-   La classe [App Part](App_Part/it.md), che definisce [Std Parts](Std_Part/it.md) che può essere utilizzato come contenitore di corpi per eseguire assiemi.

Quando si crea questo oggetto in [Python](Python/it.md), invece di sottoclassare `App::GeoFeature`, è necessario sottoclassare `App::GeometryPython` perché quest\'ultimo include di default un provider di visualizzazione e gli attributi `Proxy` per l\'oggetto stesso e il relativo provider di visualizzazione. Vedere [Script](App_GeoFeature/it#Script.md).

## Proprietà

Un oggetto [App GeoFeature](App_GeoFeature/it.md) (classe `App::GeoFeature`) è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject/it.md) (classe `App::DocumentObject`), pertanto condivide tutte le proprietà di quest\'ultimo.

Oltre alle proprietà descritte in [App DocumentObject](App_DocumentObject/it.md), GeoFeature ha la proprietà **Placement**, che controlla la sua posizione nella [vista 3D](3D_view/it.md).

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

Queste sono le proprietà disponibili nell\'[editor delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando {{MenuCommand|Mostra tutto}} nel menu contestuale dell\'[editor delle proprietà](property_editor/it.md).

### Dati


{{TitleProperty|Base}}

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

#### Hidden properties Data {#hidden_properties_data}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](App_GeoFeature#Scripting.md).

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

### Vista


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](App_GeoFeature#Scripting.md).


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

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the program

A GeoFeature is created with the `addObject()` method of the document. If you would like to create an object with a 2D or 3D [topological shape](Part_TopoShape.md), it may be better to create one of the sub-classes specialized for handling shapes, for example, [Part Feature](Part_Feature.md) or [Part Part2DObject](Part_Part2DObject.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

This basic `App::GeoFeature` doesn\'t have a default view provider, so no icon will be displayed on the [tree view](tree_view.md), and no {{MenuCommand|View}} properties will be available.

Therefore, for [Python](Python.md) subclassing, you should create the `App::GeometryPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeometryPython", "Name")
obj.Label = "Custom label"
```

For example, the [Arch BuildingPart](Arch_BuildingPart.md) element of the [Arch Workbench](Arch_Workbench.md) is an `App::GeometryPython` object with a custom icon.


{{Document objects navi

}} 
