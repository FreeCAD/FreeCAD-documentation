# Mesh Feature/de
## Einleitung

<img alt="" src=images/Mesh_Tree.svg  style="width:32px;">

Ein [Mesh Feature](Mesh_Feature/de.md)-Objekt (Mesh Formelement) oder formal ein `Mesh::Feature` ist ein einfaches Element mit einem ihm zugeordneten [Mesh MeshObject](Mesh_MeshObject/de.md) (Mesh-Objekt), das in der [3D-Ansicht](3D_view/de.md) angezeigt werden kann.

Ein Mesh Formelement ähnelt konzeptionell einem [Part Formelement](Part_Feature/de.md); Ersteres ist das Basisobjekt für Elemente mit \"Polygonnetz\"-Information, während Letzteres das Basisobjekt für Elemente mit \"geometrischer Form\"-Information ist.

Bitte beachten, dass der Arbeitsbereich [FEM](FEM_Workbench/de.md) ebenfalls Polygonnetze verwendet, aber in diesem Fall wird ein anderes Objekt verwendet, das [FEM FemMeshObject](FEM_Mesh/de.md) genannt wird (`Fem::FemMeshObject`-Klasse). Dieses Objekt ist nicht von dem Mesh Formelement abgeleitet und hat andere Eigenschaften.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD.*

## Anwendung

Fast alle Mesh-Objekte, die mit den im Arbeitsbereich [Mesh](Mesh_Workbench/de.md) verfügbaren Befehlen erzeugt werden, sind [Mesh Formelemente](Mesh_Feature/de.md). Die parametrischen Mesh-Objekte, die mit dem Befehl [Mesh RegelgeometrieErstellen](Mesh_BuildRegularSolid/de.md) erzeugt werden, bilden die einzige Ausnahme. Ein [Mesh Formelement](Mesh_Feature/de.md) kann auch über die [Python-Konsole](Python_console/de.md) erstellt werden, wie im Abschnitt [Skripten](Mesh_Feature/de#Skripten.md) beschrieben.

Das `Mesh::Feature` wird im Arbeitsbereich [Mesh](Mesh_Workbench/de.md) definiert, kann aber als Basisklasse für [skriptgenerierte Objekte](Scripted_objects/de.md) in allen [Arbeitsbereichen](Workbenches/de.md), die 2D- and 3D-Netze erstellen, verwendet werden.

Ein `Mesh::Feature` besitzt einfache Eigenschaften, wie eine [Positionierungund](Placement/de.md) visuelle Eigenschaften, die die Darstellung seiner Kanten und Flächen bestimmen.

## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Arten von Eigenschaften, die skriptgenerierte Objekte besitzen können.

The [Mesh Feature](Mesh_Feature.md) (`Mesh::Feature` class) is derived from the basic [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class) and inherits all its properties. It also has several additional properties. Notably a **Mesh** property, which stores its [Mesh MeshObject](Mesh_MeshObject.md). This is the geometry that is shown in the [3D view](3D_view.md).

These are the properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Daten


{{TitleProperty|Basis}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](#Scripting.md).

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

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

### Ansicht


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom [viewprovider](Viewprovider.md) class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](#Scripting.md).


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: if it is `True`, the object will show the bounding box in the [3D view](3D_view.md).

-    **Display Mode|Enumeration**: {{value|Shaded}} (no edges), {{value|Wireframe}} (no faces), {{value|Flat Lines}} (regular visualization), {{value|Points}} (only vertices).

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [Tree view](Tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar.


{{TitleProperty|Object Style}}

-    **Coloring|Bool|Hidden**: it defaults to `False`.

-    **Crease Angle|FloatConstraint**:

-    **Lighting|Enumeration**: {{value|One side}} (default), {{value|Two side}}; the illumination comes from two sides or one side in the [3D view](3D_view.md).

-    **Line Color|Color**: a tuple of three floating point RGB values completely black .

-    **Line Transparency|Percent**: an integer from {{value|0}} to {{value|100}} (a percentage) that determines the level of transparency of the edges in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible edges; the edges are invisible but they can still be picked as long as **Selectable** is `True`.

-    **Line Width|FloatConstraint**: a float that determines the width in pixels of the edges in the [3D view](3D_view.md). It defaults to {{value|1.0}}.

-    **Open Edges|Bool**: it defaults to `False`.

-    **Point Size|FloatConstraint**: similar to **Line Width**, defines the size of the vertices.

-    **Shape Color|Color**: similar to light gray.

-    **Shape Material|Material|Hidden**: an [App Material](App_Material.md) associated with this object. By default it is empty.

-    **Transparency|Percent**: an integer from {{value|0}} to {{value|100}} (a percentage) that determines the level of transparency of the faces in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible faces; the faces are invisible but they can still be picked as long as **Selectable** is `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

## Skripten


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Mesh Feature is created with the `addObject()` method of the document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Feature", "Name")
obj.Label = "Custom label"
```

For [Python](Python.md) subclassing you should create the `Mesh::FeaturePython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::FeaturePython", "Name")
obj.Label = "Custom label"
```



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Mesh_Workbench.md) > Mesh Feature/de
