# Part Part2DObject/pl
## Introduction

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

A _ associated that can be displayed in the [3D view](3D_view.md).

The `Part::Part2DObject` is derived from a [Part Feature](Part_Feature.md), but is specialized for 2D geometry, given that its shape will lie on a plane. This plane is defined by its **Placement** property (position, normal, and rotation). However, the plane can also be defined by supporting geometrical elements, such as the plane created by three arbitrary vertices, or a face of a solid body.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `Part::Part2DObject* class is specialized for 2D shapes, so it is the base class for planar objects created with the Draft and Sketcher workbenches. It includes an extension that allows it to be attached to faces and planes.`

## Usage

The [Part Part2DObject](Part_Part2DObject.md) is an internal object, so it cannot be created from the graphical interface, only from the [Python console](Python_console.md) as described in the [Scripting](Part_Part2DObject#Scripting.md) section.

The `Part::Part2DObject` is defined in the [Part Workbench](Part_Workbench.md) but can be used as the base class for [scripted objects](scripted_objects.md) in all [workbenches](Workbenches.md) that produce 2D geometrical shapes. For example, it is the base object for sketches ([Sketcher SketchObject](Sketcher_SketchObject.md)), and for most objects created with the [Draft Workbench](Draft_Workbench.md).

Workbenches can add more properties to this basic element to produce an object with complex behavior.

## Properties

See [Property](Property.md) for all property types that scripted objects can have.

A _ (`Part::Feature` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Part Part2DObject has the following properties in the [property editor](property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Attachment}}

-    **Map Mode|Enumeration**: {{value|Deactivated}} by default. This property determines a plane which the object will use as reference for 2D geometry. Clicking on the ellipsis **...** (three dots), to the right of the entry field opens the [Part EditAttachment](Part_EditAttachment.md) [task panel](task_panel.md) that allows selecting the supporting plane by picking different elements in the [3D view](3D_view.md). The different modes are: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

See [Part EditAttachment](Part_EditAttachment.md) for more information on all mapping modes.

The following two properties are normally hidden. They become visible once **Map Mode** is something other than {{value|Deactivated}}.

-    **Map Reversed|Bool**: it defaults to `False`; if it is `True` the Z direction will be reversed. For example, a [sketch](sketch.md) will be flipped upside down.

-    **Attachment Offset|Placement**: the position of the object in the [3D view](3D_view.md), with respect to the attachment object\'s placement. The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

#### Hidden properties Data 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Part_Part2DObject#Scripting.md).


{{TitleProperty|Attachment}}

-    **Attacher Type|String**: class name of the attach engine object driving the attachment. It defaults to `Attacher::AttachEnginePlane`.

-    **Support|LinkSubList**: it is the plane or face supporting the 2D geometry. It defaults to an empty list `[]`.

-    **Map Path Parameter|Float**: sets point of curve to map a [sketch](sketch.md) to. It goes from {{value|0}} to {{value|1}}, which corresponds to the {{value|start}} and {{value|end}}. It defaults to {{value|0}}.

### View


{{TitleProperty|Grid}}

-    **Grid Size|Length**: the size of the spacing of the local grid lines in the [3D view](3D_view.md); it defaults to {{value|10 mm}}.

-    **Grid Snap|Bool**: it defaults to `False`; if `True` the grid can be used to snap points.

-    **Grid Style|Enumeration**: the style of the grid lines; {{value|Dashed}} (default) or {{value|Light}}.

-    **Show Grid|Bool**: it defaults to `False`; if `True` a grid local to the object will be displayed in the [3D view](3D_view.md). This grid is independent of the [Draft Grid](Draft_ToggleGrid.md).

-    **Tight Grid|Bool**: if `True` (default) the local grid will be localized around the origin of the shape, otherwise it will extend itself more.

#### Hidden properties View 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Part_Part2DObject#Scripting.md).

All other view properties, including hidden properties, are those of the base [Part Feature](Part_Feature.md) object.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Part2DObject is created with the `addObject()` method of the document. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

This basic `Part::Part2DObject` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `Part::Part2DObjectPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```

For example, most tools from the [Draft Workbench](Draft_Workbench.md), like [Draft Line](Draft_Line.md), [Draft Rectangle](Draft_Rectangle.md), [Draft Polygon](Draft_Polygon.md), etc., are `Part::Part2DObjectPython` objects with a custom icon and additional properties.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/pl
