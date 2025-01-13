# App GeoFeature/de
## Einleitung

<img alt="" src=images/Feature.svg  style="width:32px;">

Ein [App-GeoFeature](App_GeoFeature/de.md)-Objekt, oder formal ein `App::GeoFeature`, ist die Basisklasse der meisten Objekte, die geometrische Elemente in der [3D-Ansicht](3D_view/de.md) anzeigen, da es eine {{PropertyData/de|Placement}} enthält.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*



## Anwendung

Das [App GeoFeature](App_GeoFeature/de.md) ist ein internes Objekt; es kann daher nicht von der grafischen Oberfläche aus erstellt werden. Es ist generell nicht dafür vorgesehen, direkt eingesetzt zu werden, eher zum Ableiten einer Unterklasse für ein nacktes Objekt, das nur eine grundlegende {{PropertyData/de|Placement}} enthält, die seine Position in der [3D-Ansicht](3D_view/de.md) festlegt.

Einige der wichtigsten abgeleiteten Objekte sind folgende:

-   Die Klasse [Part Feature](Part_Feature/de.md) (Part-Formelement), übergeordnete Klasse der meisten Objekte mit 2D- und 3D- [TopoFormen](Part_TopoShape/de.md).
-   Die Klasse [Mesh Feature](Mesh_Feature/de.md) (Mesh-Formelement), übergeordnete Klasse der meisten von [Netzobjekten](Mesh_MeshObject/de.md) abgeleiteten Objekte; keine Festkörper.
-   Die Klasse [Fem FemMeshObject](FEM_Mesh/de.md) (FEM-Netzobjekt), übergeordnete Klasse der FEM-Netze, die mit dem Arbeitsbereich [FEM](FEM_Workbench/de.md) erstellt wurden.
-   Die Klasse [CAM Feature](CAM_Feature/de.md) (CAM-Element), übergeordnete Klasse der Werkzeugbahnen (paths), die mit dem Arbeitsbereich [CAM](CAM_Workbench/de.md) für CNC-Bearbeitungen erstellt wurden.
-   Die Klasse [App Part](App_Part/de.md) (App-Part), die [Std-Parts](Std_Part/de.md) definiert, die als Behälter von Körpern eingesetzt werden, um Baugruppen zusammenzustellen.

Wird dieses Objekt mit [Python](Python/de.md) erstellt, sollte anstatt eine Unterklasse von `App::GeoFeature` abzuleiten, eine Unterklasse von `App::GeometryPython` abgeleitet werden, da letztere einen Standard-Viewprovider enthält sowie `Proxy`-Attribute für das Objekt selbst und seinen Viewprovider. Siehe [Skripten](App_GeoFeature/de#Skripten.md).



## Eigenschaften eines App-GeoFeature-Objekts 

Siehe [Objekteigenschaften](Property/de.md) für alle Arten von Eigenschaften, die skriptgenerierte Objekte besitzen können.

Das Objekt [App GeoFeature](App_GeoFeature/de.md) (Klasse `App::GeoFeature`) ist von dem grundlegenden [App DocumentObject](App_DocumentObject/de.md) (Klasse `App::DocumentObject`) abgeleitet und erbt alle seine Eigenschaften. Zusätzlich besitzt es eine {{PropertyData/de|Placement}}, die seine Position in der [3D-Ansicht](3D_view/de.md) bestimmt.



## Eigenschaften eines App-GeometryPython-Objekts 

Siehe [Objekteigenschaften](Property/de.md) für alle Arten von Eigenschaften, die skriptgenerierte Objekte besitzen können.

Das Objekt [App GeometryPython](App_GeoFeature/de.md) (Klasse `App::GeometryPython`) wird von einem [App GeoFeature](App_GeoFeature/de.md) (Klasse `App::GeoFeature`) abgeleitet und erbt alle seine Eigenschaften. Es besitzt einige zusätzliche Eigenschaften.

Diese sind die im [Eigenschafteneditor](Property_editor/de.md) vorhandenen Eigenschaften. Ausgeblendete Eigenschaften können mit dem Befehl **Alle anzeigen** im Kontextmenü des [Eigenschafteneditors](Property_editor/de.md) angezeigt werden.



### Daten


{{TitleProperty|Basis}}

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



### Ansicht


{{TitleProperty|Basis}}

-    {{PropertyView/de|Proxy|PythonObject|Hidden}}: eine spezielle, mit diesen Objekt vebundene, [Viewprovider](Viewprovider/de.md)-klasse.


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



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.

Ein GeoFeature wird mit der Methode `addObject()` des Dokuments erstellt. Soll ein Objekt mit einer 2D- oder 3D- [Topoform](Part_TopoShape.md) erstellt werden, ist es vielleicht besser, eine Unterklasse zu erstellen, die auf den Umgang mit Formen spezialisiert ist, z.B. [Part Fomelement](Part_Feature/de.md) oder [Part Part2DObject](Part_Part2DObject/de.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

Für die Ableitung von [Python](Python/de.md)-Unterklassen sollte das `App::GeometryPython`-Objekt erstellt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeometryPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App GeoFeature/de
