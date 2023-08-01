# Property editor/de
## Einführung

Der [Eigenschafteneditor](property_editor/de.md) erscheint wenn der Reiter **Modell** der [Combo-Ansicht](combo_view/de.md) auf der [Oberfläche](interface/de.md) aktiv ist; er ermöglicht die Verwaltung der öffentlich zugänglichen Eigenschaften der Objekte im Dokument.

Generell ist der Eigenschafteneditor dazu gedacht, nur ein Objekt zur Zeit zu behandeln. Die im Eigenschafteneditor angezeigten Werte gehören zum ausgewählten Objekt des aktiven Dokuments. Es gibt jedoch einige Eigenschaften, wie Farben, die für viele ausgewählte Objekte gleichzeitig gesetzt werden können. Wenn kein Element ausgewählt wurde, bleibt der Eigenschafteneditor leer.

Nicht alle Eigenschaften können immer geändert werden; je nach dem spezifischen Status der Eigenschaft sind einige von ihnen unsichtbar (nicht aufgeführt) oder schreibgeschützt (nicht bearbeitbar).




![](images/FreeCAD_Property_editor_empty.png )



*Leerer Eigenschafteneditor, wenn kein Objekt ausgewählt ist.*



## Eigenschaftentypen

Eine Eigenschaft ist eine Information wie eine Zahl oder eine Textzeichenfolge, die an ein FreeCAD-Dokument oder ein Objekt im Dokument angehängt ist.

Benutzerdefinierte [skriptgenerierte Objekte](Scripted_objects/de.md) können jeden der im Basissystem definierten Eigenschaftstypen verwenden. Die vollständige Liste findet man unter [Objekteigenschaften](Property/de.md).

Einige der am häufigsten verwendeten Eigenschaftstypen sind:


```python
App::PropertyBool
App::PropertyFloat
App::PropertyAngle
App::PropertyDistance
App::PropertyInteger
App::PropertyString
App::PropertyMatrix
App::PropertyVector
App::PropertyPlacement
```

Verschiedene Objekte können unterschiedliche Typen von Eigenschaften haben. Viele Objekte haben jedoch die gleichen Typen, weil sie von der gleichen internen Klasse abgeleitet sind. Zum Beispiel haben die meisten Objekte, die geometrische Formen beschreiben (Linien, Kreise, Rechtecke, Volumenkörper, importierte Teile usw.), die Eigenschaft \"Platzierung\", die ihre Position in der [3D-Ansicht](3D_view/de.md) definiert.



## Ansicht- und Daten-Eigenschaften 

There are two classes of feature properties accessible through tabs in the property editor:

-    **View**properties, related to the \"visual\" appearance of the object. The **View** properties are tied to the **ViewProvider** (`ViewObject` attribute) of the object, and are only accessible when the graphical user interface (GUI) is loaded. They are not accessible when using FreeCAD in console mode, or as a headless library.

-    **Data**properties, related to the \"physical\" parameters of the object. The **Data** properties define the essential characteristics of the object; they exist at all times, even when FreeCAD is used in console mode, or as a library. This means that if you load a document in console mode, you can edit the radius of a circle or the length of a line, even if you cannot see the result on the screen.

For this reason, **Data** properties are considered to be more \"real\", as they truly define the geometry of a shape. On the other hand, **View** properties are less important because they only affect the superficial appearance of the geometry. For example, a circle of 10 mm radius is different from a circle of 5 mm radius; the color of the circle (view property) doesn\'t affect its shape, but the radius does (data property). In many instances in this documentation, the word \"property\" is understood to refer to a \"Data property\" and not to a \"View property\".



### Grundlegende Eigenschaften 


**Siehe auch: [Objektname](Object_name/de.md)**

The most basic [scripted object](Scripted_objects.md) won\'t show any **Data** property in the property editor, except for its `Label` attribute. The `Label` is a user editable string that identifies the object in the [tree view](Tree_view.md). On the other hand, the `Name` attribute of an object is assigned at the moment of its creation and cannot be changed; this attribute is read-only, and is not displayed in the property editor either.

Ein grundlegendes parametrisches Objekt wird wie folgt erstellt


```python
obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width:" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width:" height="264px;">



*View and Data tabs of the property editor, for a basic "App::FeaturePython" scripted object.*

Most geometrical objects that can be created and displayed in the [3D view](3D_view.md) are derived from a `Part::Feature`. See [Part Feature](Part_Feature.md) for the most basic properties that these objects have.

For 2D geometry, most objects are derived from `Part::Part2DObject` (itself derived from `Part::Feature`) which is the base of [Sketches](Sketch.md), and most [Draft elements](Draft_Workbench.md). See [Part Part2DObject](Part_Part2DObject.md) for the most basic properties that these objects have.



## Maßnahmen

Right clicking in an empty space of the view, or with a property selected, shows only one command:

-    **Show all**: if active, in addition to the standard properties that appear already, it shows all the hidden Data and View properties in their respective tabs.

    -   Data: \"Proxy\", \"Label2\", \"Expression Engine\", and \"Visibility\".
    -   View: \"Proxy\".

When the **Show all** option is active, and one property is selected, more actions are available with a second right click:

-    **Show all**: deactivates the **Show all** command, hiding the additional Data and View properties.

-    **Add Property**: adds a dynamic property to the object; this works with both C++ defined objects, and Python [scripted objects](Scripted_objects.md).

-    **Expression...**: brings up the formula editor, which allows using [expressions](Expressions.md) in the property value.

-    **Hidden**: if active, sets the property as hidden, meaning that it will only be displayed in the property editor if **Show all** is active.

-    **Output**: if active, sets the property as output.

-    **NoRecompute**: if active, sets the property as not recomputed when the document is recomputed; this is useful when a property should be kept unaffected by other updates.

-    **ReadOnly**: if active, sets the property to be read-only; it won\'t be editable in the property editor any more until this switch is turned off. The **Expression...** menu entry is no longer available. **Note:** It may be still possible to change the property via a dialog that updates the property.

-    **Transient**: if active, sets the property as transient. The value of a transient property is not saved to file. When opening a file, it is instantiated with its default value.

-    **Touched**: if active, it becomes touched, and ready for recompute.

-    **EvalOnRestore**: if active, it is evaluated when the document is restored.



## Beispiel für die Eigenschaften eines PartDesign-Objekts 

In this section we show some common properties that are visible for a [PartDesign Body](PartDesign_Body.md), and one [PartDesign Feature](PartDesign_Feature.md). The specific properties of an object can found in the specific documentation page of that object.



### Ansicht

Most of these properties are inherited from the [Part Feature](Part_Feature.md) basic object.

<img alt="" src=images/FreeCAD_Property_editor_View.png  style="width:490px;">


{{TitleProperty|Base}}

-    **Angular Deflection**: it is another way to specify how finely to generate the mesh for rendering on screen or when exporting. The default value is 28.5 degrees, or 0.5 radians. The smaller the value the smoother the appearance will be in the [3D view](3D_view.md), and the finer the mesh that will be exported.

-    **Bounding Box**: indicates if a box showing the overall extent of the object is displayed.

-    **Deviation**: sets the accuracy of the polygonal representation of the model in the [3D view](3D_view.md) (tessellation). Lower values indicate better quality. The value is in percent of object\'s size.

-    **Display Mode**: display mode of the entire Body, {{Value|Flat lines}} (default), {{Value|Shaded}}, {{Value|Wireframe}}, {{Value|Points}}.

-    **Display Mode Body**: display mode of the Tip of the Body, {{Value|Through}} (default), {{Value|Tip}}.

-    **Draw Style**: {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dotted}}, {{Value|Dashdot}}; defines the style of the edges in the [3D view](3D_view.md).

-    **Lighting**: {{Value|One side}}, {{Value|Two side}} (default).

-    **Line Color**: the RGB color of the edges, it defaults to {{value|(25, 25, 25)}}.

-    **Line Width**: the thickness of the edges, it defaults to {{value|2}} pixels.

-    **On Top When Selected**: {{value|Disabled}}, {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Point Color**: the RGB color of the vertices, it defaults to {{value|(25, 25, 25)}}.

-    **Point Size**: the size of the vertices, it defaults to {{value|2}} pixels.

-    **Selectable**: whether the object is selectable or not.

-    **Selection Style**: {{value|Shape}}, {{value|BoundBox}}.

-    **Shape Color**: the RGB color of the shape, it defaults to {{value|(204, 204, 204)}}.

-    **Show In Tree**: if it is `True`, the object appears in the tree view. Otherwise, it is set as invisible.

-    **Transparency**: the degree of transparency from {{value|0}} (default) to {{value|100}}.

-    **Visibility**: whether the object is visible in the [3D view](3D_view.md) or not. Toggle with the **Space** bar in the keyboard.






### Daten

In this case we observe the properties of the [PartDesign Revolution](PartDesign_Revolution.md) feature.

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:490px;">


{{TitleProperty|Base}}

-    **Label**: the user defined name given to the object, this can be changed as desired.


{{TitleProperty|Part Design}}

-    **Refine**: whether to refine the fusion done with other objects.


{{TitleProperty|Revolution}}

-    **Base**: the point in space that specifies where the revolution takes place. It cannot be modified directly, only when editing the feature.

-    **Axis**: the axis around which the revolution will be performed. It cannot be modified directly, only when editing the feature.

-    **Angle**: the angle that specifies how much of the base element is rotated. By default it is {{value|360 deg}}, but it can be any fraction of that.


{{TitleProperty|Sketch Based}}

-    **Midplane**: if the base object is a [Sketch](Sketch.md), when this property is `True`, it will perform the revolution with the sketch serving as a plane of symmetry. This is noticeable if the **Angle** is different from {{value|360 deg}}.

-    **Reversed**: by default it is `True`. Whether to perform the revolution in one direction or the other.






## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Siehe [geskriptete Objekte](scripted_objects/de.md) für die vollständigen Informationen zum Hinzufügen von Eigenschaften zu Objekten, die über [Python](Python/de.md) definiert wurden. Deine Übersetzung

Most properties that are visible in the property editor can be accessed from the [Python console](Python_console.md). These properties are just attributes of the class that defines the selected object. For example, if the property editor shows the **Group** property, this means that the object has the `Group` attribute.


```python
print(obj.Group)
```

These attributes (properties) are added with the `addProperty` method of the base object. At least it is necessary to specify the type of [property](property.md), and its name.


```python
obj.addProperty("App::PropertyFloat", "Custom")
print(obj.Custom)
```

Properties follow the `CapitalCamelCase` or `PascalCase` convention, meaning that each word starts with a capital letter, and there are no underscores. When the property editor displays such names, it leaves a space between each capital letter, making it easier to read.


```python
obj.addProperty("App::PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Property editor showing the Data properties of a [PartDesign Body](PartDesign_Body.md), with two additional properties, "Custom" and "Custom Camel Property".*

In similar way the **View** properties are added, not to the base object, but to its `ViewObject`. Then, it follows that properties like **Angular Deflection**, **Bounding Box**, **Display Mode**, **Display Mode Body**, **Line Color**, and others, can be examined and changed from the [Python console](Python_console.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

Alle öffentlichen Eigenschaften des Objekts und seines Ansichtsanbieters sind in dem entsprechenden Attribut `PropertiesList` enthalten.


```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```





{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Property editor/de
