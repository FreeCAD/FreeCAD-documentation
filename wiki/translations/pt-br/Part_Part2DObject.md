# Part Part2DObject/pt-br
{{TOCright}}

## Introdução

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

A [Part Part2DObject](Part_Part2DObject.md), or formally a `Part::Part2DObject`, is a simple element with a [topological shape](Part_TopoShape.md) that can be displayed in the [3D view](3D_view.md).

The `Part::Part2DObject` is derived from the [Part Feature](Part_Feature.md), but is specialized for 2D geometry, given that its shape will lie on a plane. This plane is defined by its **Placement** property (position, normal, and rotation). However, the plane can also be defined by supporting geometrical elements, such as the plane created by three arbitrary vertices, or a face of a solid body.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in FreeCAD*

## Usage

The [Part Part2DObject](Part_Part2DObject.md) is an internal object, so it cannot be created from the graphical interface, only from the [Python console](Python_console.md) as described in the [Scripting](#Scripting.md) section.

The `Part::Part2DObject` is defined in the [Part Workbench](Part_Workbench.md) but can be used as the base class for [scripted objects](Scripted_objects.md) in all [workbenches](Workbenches.md) that produce 2D geometrical shapes. For example, it is the base object for sketches ([Sketcher SketchObject](Sketcher_SketchObject.md)), and for most objects created with the [Draft Workbench](Draft_Workbench.md).

Workbenches can add more properties to this basic element to produce an object with complex behavior.

## Properties

See [Property](Property.md) for all property types that scripted objects can have.

The [Part Part2DObject](Part_Part2DObject.md) (`Part::Part2DObject` class) is derived from the [Part Feature](Part_Feature.md) (`Part::Feature` class) and inherits all its properties.

The Part Part2DObject also has the following additional properties in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Attachment}}

-    <div id="Property_Attacher_Type">
    </div>
    **Attacher Type|String|Hidden**: class name of the attach engine object driving the attachment. It defaults to `Attacher::AttachEnginePlane`.

-    <div id="Property_Support">
    </div>
    **Support|LinkSubList**: it is the plane or face supporting the 2D geometry. It defaults to an empty list `[]`.

-    <div id="Property_Map_Mode">
    </div>
    **Map Mode|Enumeration**: {{value|Deactivated}} by default. This property determines a plane which the object will use as reference for 2D geometry. Clicking on the ellipsis **...** (three dots), to the right of the entry field starts the [Part EditAttachment](Part_EditAttachment.md) command that allows selecting the supporting plane by picking different elements in the [3D view](3D_view.md). The different modes are: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

-    <div id="Property_Map_Reversed">
    </div>
    **Map Reversed|Bool**: it defaults to `False`; if it is `True` the Z direction will be reversed. For example, a [sketch](sketch.md) will be flipped upside down. Hidden if **Map Mode** is {{value|Deactivated}}.

-    <div id="Property_Map_Path">
    </div>
    **Map Path Parameter|Float|Hidden**: sets point of curve to map a [sketch](sketch.md) to. It goes from {{value|0}} to {{value|1}}, which corresponds to the {{value|start}} and {{value|end}}. It defaults to {{value|0}}.

-    <div id="Property_Attachment_Offset">
    </div>
    **Attachment Offset|Placement**: the position of the object in the [3D view](3D_view.md), with respect to the attachment object\'s placement. The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md). Hidden if **Map Mode** is {{value|Deactivated}}.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Part2DObject is created with the `addObject()` method of the document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

For [Python](Python.md) subclassing you should create a `Part::Part2DObjectPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/pt-br
