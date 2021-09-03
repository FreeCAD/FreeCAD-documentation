

## Einleitung


{{TOCright}}

Ein <img alt="" src=images/Mesh_Tree.svg  style="width:32px;"> [Polygonnetz Formelement](Mesh_Feature/de.md) Objekt oder formal ein `Mesh::Feature` ist ein einfaches Element mit einem ihm zugeordneten [Polygonnetz Objekt](Mesh_MeshObject/de.md), das in der [3D Ansicht](3D_view/de.md) angezeigt werden kann.

Ein Polygonnetz Formelement ähnelt konzeptionell einem [Part Formelement](Part_Feature/de.md); Ersteres ist das Basisobjekt für Elemente mit \"Polygonnetz\" Information, während Letzteres das Basisobjekt für Elemente mit \"geometrischer Form\" Information ist.

Bitte beachte, dass der **<img src="images/Workbench_FEM.svg" width=16px> [FEM Arbeitsbereich](FEM_Workbench/de.md)** ebenfalls Polygonnetze verwendet, aber in diesem Fall wird ein anderes Objekt verwendet, das [Fem FemPolygonnetzObjekt](Fem_FemMeshObject/de.md) (`Fem::FemMeshObject` Klasse) genannt wird. Dieses Objekt ist nicht von Polygonnetz Formelement abgeleitet und hat daher andere Eigenschaften.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die `Mesh::Feature* Klasse ist der Ursprung der meisten Objekte, die über ein [Dreieckspolygonnetz](Mesh_MeshObject/de.md) verfügen. Diese Objekte werden von der [Polygonnetz Arbeitsbereich](Mesh_Workbench/de.md) oder durch Importieren von STL, OBJ und ähnlichen Polygonnetzformatdateien erstellt.`

## Anwendung

Fast alle Polygonnetz Objekte, die mit den in der grafischen Oberfläche [Polygonnetz Arbeitsbereich](Mesh_Workbench/de.md) verfügbaren Befehlen erzeugt werden, sind [Polygonnetz Funktionen](Mesh_Feature/de.md). Die einzige Ausnahme bilden die parametrischen Polygonnetzobjekte, die mit dem Befehl [Polygonnetz BauRegularSolid](Mesh_BuildRegularSolid/de.md) erzeugt werden. Ein [Polygonnetz Funktion](Mesh_Feature/de.md) kann auch über die [Python Konsole](Python_console/de.md) erzeugt werden, wie im Abschnitt [Skripten](Mesh_Feature/de#Skripten.md) beschrieben.

The `Mesh::Feature` is defined in the [Mesh Workbench](Mesh_Workbench.md) but can be used as the base class for [scripted objects](scripted_objects.md) in all [workbenches](Workbenches.md) that produce 2D and 3D meshes.

A `Mesh::Feature` has simple properties like a [placement](Placement.md), and visual properties to define the appearance of its edges and faces.

## Eigenschaften

A [Mesh Feature](Mesh_Feature.md) (`Mesh::Feature` class) is derived from the basic [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [App GeoFeature](App_GeoFeature.md), the Mesh Feature has the **Mesh** property, which stores the [Mesh MeshObject](Mesh_MeshObject.md) of this element; this is the geometry that is shown in the [3D view](3D_view.md).

Other properties that this object has are those related to the appearance of its [Mesh MeshObject](Mesh_MeshObject.md), including **Crease Angle**, **Lighting**, **Line Color**, **Line Transparency**, **Line Width**, **Open Edges**, **Point Size**, and also the hidden property **Coloring**.

See [Property](Property.md) for all property types that scripted objects can have.

These are the properties available in the [property editor](property_editor.md). Hidden properties can be shown by using the {{MenuCommand|Show all}} command in the context menu of the [property editor](property_editor.md).

### Daten


{{TitleProperty|Base}}

-    **Mesh|MeshKernel**: a [Mesh MeshObject](Mesh_MeshObject.md) class associated with this object. It lists the number of {{Value|Points}}, {{Value|Edges}}, and {{Value|Faces}} of the mesh.

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

#### Ausgeblendete Dateneigenschaften {#ausgeblendete_dateneigenschaften}


{{TitleProperty|Base}}

-    **Expression Engine|ExpressionEngine**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Label2|String**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Mesh_Feature#Scripting.md).

-    **Visibility|Bool**: whether to display the object or not.

### Ansicht

Most objects in FreeCAD have what is called a \"view provider\", which is a class that defines the visual appearance of the object in the [3D view](3D_view.md), and in the [tree view](tree_view.md). The default view provider of Mesh Feature objects defines the following properties. Scripted objects that are derived from Mesh Feature will have access to these properties as well.


{{TitleProperty|Base}}

-    **Bounding Box|Bool**: if it is `True`, the object will show the bounding box in the [3D view](3D_view.md).

-    **Crease Angle|FloatConstraint**:

-    **Display Mode|Enumeration**: {{value|Shaded}} (no edges), {{value|Wireframe}} (no faces), {{value|Flat Lines}} (regular visualization), {{value|Points}} (only vertices).

-    **Lighting|Enumeration**: {{value|One side}} (default), {{value|Two side}}; the illumination comes from two sides or one side in the [3D view](3D_view.md).

-    **Line Color|Color**: a tuple of three floating point RGB values completely black .

-    **Line Transparency|Percent**: an integer from {{value|0}} to {{value|100}} (a percentage) that determines the level of transparency of the edges in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible edges; the edges are invisible but they can still be picked as long as **Selectable** is `True`.

-    **Line Width|FloatConstraint**: a float that determines the width in pixels of the edges in the [3D view](3D_view.md). It defaults to {{value|1.0}}.

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Open Edges|Bool**: it defaults to `False`.

-    **Point Size|FloatConstraint**: similar to **Line Width**, defines the size of the vertices.

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

-    **Shape Color|Color**: similar to light gray.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [tree view](tree_view.md). Otherwise, it is set as invisible.

-    **Transparency|Percent**: an integer from {{value|0}} to {{value|100}} (a percentage) that determines the level of transparency of the faces in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible faces; the faces are invisible but they can still be picked as long as **Selectable** is `True`.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.

#### Ausgeblendete Eigenschaften Ansicht {#ausgeblendete_eigenschaften_ansicht}


{{TitleProperty|Base}}

-    **Coloring|Bool**: it defaults to `False`.

-    **Proxy|PythonObject**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Mesh_Feature#Scripting.md).

-    **Shape Material|Material**: an [App Material](App_Material.md) associated with this object. By default it is empty.

## Skripten


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the program.

A Mesh Feature is created with the `addObject()` method of the document. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Feature", "Name")
obj.Label = "Custom label"
```

This basic `Mesh::Feature` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `Mesh::FeaturePython` object. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::FeaturePython", "Name")
obj.Label = "Custom label"
```


{{Mesh Tools navi

}} {{Document objects navi}} 

[Category:Glossary{{\#translation:}}](Category:Glossary.md)
