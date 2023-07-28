# Part Feature/de
{{TOCright}}



## Einleitung

<img alt="" src=images/Part_3D_object.svg  style="width:32px;">

Ein [Part Formelement](Part_Feature/de.md)-Objekt, oder formal ein `Part:: Feature`, ist ein einfaches Element mit einer [topologischen Form](Part_TopoShape/de.md), das in der [3D-Ansicht](3D_view/de.md) angezeigt werden kann.

Das Part-Formelement ist die Elternklasse der meisten 2D-(Draft-, Sketcher-) und 3D- (Part-, PartDesign-) Objekte, mit Ausnahme von Polygonnetzen, die normalerweise auf dem[Mesh Formelement](Mesh_Feature/de.md) oder dem [FEM Polygonnetz](FEM_Mesh/de.md)-Objekt für FEM-Objekte basieren.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*



## Anwendung

Das [Part-Formelement](Part_Feature/de.md) ist ein internes Objekt, kann also nicht von der grafischen Oberfläche aus erstellt werden, sondern nur von der [Python-Konsole](Python_console/de.md) aus, wie im Abschnitt [Skripten](#Skripten.md) beschrieben.

Das `Part::Feature` wird im Arbeitsbereich [Part](Part_Workbench/de.md) definiert, kann aber als Basisklasse für [skriptgenerierte Objekte](scripted_objects/de.md) in allen [Arbeitsbereichen](Workbenches/de.md) verwendet werden, die 2D- und 3D-Geometrieformen erstellen. Im Wesentlichen sind alle im Arbeitsbereich [Part](Part_Workbench/de.md) erstellten Objekte Instanzen eines `Part::Feature`s.

Das `Part::Feature` ist auch die Elternklasse des [PartDesign Körpers](PartDesign_Body/de.md), der [PartDesign Formelemente](PartDesign_Feature/de.md) und der [Part Part2DObjekte](Part_Part2DObject/de.md), die auf 2D-(planare) Formen spezialisiert ist.

Arbeitsbereiche können diesem Grundelement weitere Eigenschaften hinzufügen, um ein Objekt mit komplexem Verhalten zu erzeugen.



## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Das [Part-Formelement](Part_Feature/de.md) (Klasse `Part::Feature`) wird von dem Grundelement [App GeoFeature](App_GeoFeature/de.md) (Klasse `App::GeoFeature`) abgeleitet, und erbt alle seine Eigenschaften. Es besitzt auch einige zusätzliche Eigenschaften. Hervorzuheben ist eine {{PropertyData/de|Shape}}, die die [Part TopoForm](Part_TopoShape/de.md) des Objekts speichert. Dies ist die Geometrie, die in der [3D-Ansicht](3D_view/de.md) gezeigt wird. Andere Eigenschaften die dieses Objekt besitzt, sind solche die die Darstellung der [TopoForm](Part_TopoShape/de.md) beeinflussen.

Diese sind die im [Eigenschafteneditor](Property_editor/de.md) enthaltenen Eigenschaften. Ausgeblendete Eigenschaften können mit dem Befehl **Alle anzeigen** im Kontextmenü des [Eigenschafteneditors](Property_editor/de.md) angezeigt werden.



### Daten


{{TitleProperty|Grundlage}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](#Scripting.md).

-    **Shape|PartShape|Hidden**: a [Part TopoShape](Part_TopoShape.md) class associated with this object.

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

Most objects in FreeCAD have what is called a \"[viewprovider](viewprovider.md)\", which is a class that defines the visual appearance of the object in the [3D view](3D_view.md), and in the [Tree view](Tree_view.md). The default viewprovider of Part Feature objects defines the following properties. Scripted objects that are derived from Part Feature will have access to these properties as well.


{{TitleProperty|Base}}

-    **Proxy|PythonObject|hidden**: a custom [viewprovider](Viewprovider.md) class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](#Scripting.md).


{{TitleProperty|Anzeigeoptionen}}

-    **Bounding Box|Bool**: if it is `True`, the object will show the bounding box in the [3D view](3D_view.md).

-    **Display Mode|Enumeration**: {{value|Flat Lines}} (regular visualization), {{value|Shaded}} (no edges), {{value|Wireframe}} (no faces), {{value|Points}} (only vertices).

-    **Show In Tree|Bool**: it defaults to `True`, in which case the object will appear in the [Tree view](Tree_view.md); otherwise, the object will be hidden in the tree view. Once an object in the tree is invisible, you can see it again by opening the context menu over the name of the document (right-click), and selecting {{CheckBox|TRUE|Show hidden items}}. Then the hidden item can be chosen and **Show In Tree** can be switched back to `True`.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar.


{{TitleProperty|Objektstil}}

-    **Angular Deflection|Angle**: it is a companion to **Deviation**. It is another way to specify how finely to generate the mesh for rendering on screen or when exporting. The default value is {{value|28.5 degrees}}, or {{value|0.5 radians}}. This is the maximum value, the smaller the value the smoother the appearance will be in the [3D view](3D_view.md), and the finer the mesh that will be exported.

-    **Deviation|FloatConstraint**: it is a companion to **Angular Deflection**. It is another way to specify how finely to generate the mesh for rendering on screen or when exporting. The default value is {{value|0.5%}}. This is the maximum value, the smaller the value the smoother the appearance will be in the [3D view](3D_view.md), and the finer the mesh that will be exported.

-    **Diffuse Color|ColorList|hidden**: it is a list of RGB tuples defining colors, similar to **Shape Color**. It defaults to a list of one {{value|[(0.8, 0.8, 0.8)]}}.

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


{{TitleProperty|Auswahl}}

-    **On Top When Selected|Enumeration**: it controls the way in which the selection occurs in the [3D view](3D_view.md) if the object has a [Shape](Part_TopoShape.md), and there are many objects partially covered by others. It defaults to {{value|Disabled}}, meaning that no special highlighting will occur; {{value|Enabled}} means that the object will appear on top of any other object when selected; {{value|Object}} means that the object will appear on top only if the entire object is selected in the [Tree view](Tree_view.md); {{value|Element}} means that the object will appear on top only if a subelement (vertex, edge, face) is selected in the [3D view](3D_view.md).

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Selection Style|Enumeration**: it controls the way the object is highlighted. If it is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} a bounding box will appear surrounding the object and will be highlighted.



### Verdrehwinkel und Winkelabweichung 

<img alt="" src=images/View_property_Deviation.svg  style="width:500px;"> 
*Parameter für Verdrehwinkel und Winkelabweichung: d < lineare Abweichung, α < Winkelabweichung.*

Die Abweichung ist ein Wert in Prozent, der mit den Abmaßen in mm der Bounding-Box des Objekts zusammenhängt. Die Abweichung in mm kann wie folgt berechnet werden:


```python
deviation_in_mm = (w + h + d)/3 * deviation/100
```

wobei {{value|w}}, {{value|h}}, {{value|d}} die Begrenzungsrahmen Abmessungen sind.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Ein Part Formelement wird mit der `addObject()` Methode des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Feature", "Name")
obj.Label = "Custom label"
```

Für [Python](Python/de.md)-Subclassing sollte ein `Part::FeaturePython`-Objekt erstellt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Name")
obj.Label = "Custom label"
```



### Namen

See also: [Object name](Object_name.md) for more information on the properties of the `Name`.

The `addObject` method has two basic string arguments.

-   The first argument indicates the type of object, in this case, `"Part::FeaturePython"`.
-   The second argument is a string that defines the `Name` attribute. If it is not provided, it defaults to the same name as the class, that is, `"Part__FeaturePython"`. The `Name` can only include simple alphanumeric characters, and the underscore, `[_0-9a-zA-Z]`. If other symbols are given, these will be converted to underscores; for example, `"A+B:C*"` is converted to `"A_B_C_"`.



### Beschriftung

If desired, the `Label` attribute can be changed to a more meaningful text.

-   The `Label` can accept any UTF8 string, including accents and spaces. Since the [Tree view](Tree_view.md) displays the `Label`, it is a good practice to change the `Label` to a more descriptive string.
-   By default the `Label` is unique, just like the `Name`. However, this behavior can be changed in the [preferences editor](Preferences_Editor.md), **Edit → Preferences → General → Document → Allow duplicate object labels in one document**. This means that in general the `Label` may be repeated in the same document; when testing for a specific element the user should rely on the `Name` rather than on the `Label`.


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Feature/de
