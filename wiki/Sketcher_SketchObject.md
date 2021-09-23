# Sketcher SketchObject
 

## Introduction

 <img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;"> 

A [Sketcher SketchObject](Sketcher_SketchObject.md), or formally a `Sketcher::SketchObject`, is the base element to create 2D objects with the [Sketcher Workbench](Sketcher_Workbench.md).

The `Sketcher::SketchObject` is derived from [Part Part2DObject](Part_Part2DObject.md), which means it is a [Part Feature](Part_Feature.md) object specialized for 2D geometry. Like Part2DObject, the SketchObject can be attached to planes and faces. In addition, the SketchObject can handle geometrical constraints of the lines and curves that are drawn within it.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in FreeCAD. The `Sketcher::SketchObject* class is specialized for 2D shapes, and additionally it includes an extension to handle geometrical constraints of its elements.`

## Usage

1.  Switch to the [Sketcher Workbench](Sketcher_Workbench.md).
2.  Press **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NewSketch](Sketcher_NewSketch.md)**.
3.  Select a **Sketch orientation**: XY-plane, XZ-plane, or YZ-plane. Optionally also choose **Reverse direction**, and give an **Offset** value.
4.  Press **OK**.

Although the SketchObject can be used by itself to draw on a plane, it is most commonly used in conjunction with the [PartDesign Workbench](PartDesign_Workbench.md) to create extruded solids.

1.  Switch to the [PartDesign Workbench](PartDesign_Workbench.md).

2.  Press **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.

3.  Press **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**.

4.  
    **Select feature**: XY\_Plane (Base plane), XZ\_Plane (Base plane), or YZ\_Plane (Base plane).

5.  Press **OK**.

## Properties

See [Property](Property.md) for all property types that scripted objects can have.

A [Sketcher SketchObject](Sketcher_SketchObject.md) (`Sketcher::SketchObject` class) is derived from a [Part Part2DObject](Part_Part2DObject.md) (`Part::Part2DObject` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Part2DObject](Part_Part2DObject.md), the basic Sketcher SketchObject has the following properties in the [property editor](property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Attachment}}

-    **Map Mode**, **Map Reversed**, **Attachment Offset**: same as [Part Part2DObject](Part_Part2DObject.md). See [Part EditAttachment](Part_EditAttachment.md) for more information on all attachment mapping modes.


{{TitleProperty|Sketch}}

-    **Constraints|**: named constraints, if they exist; otherwise it is an empty list `[]`.

#### Hidden properties Data 

See [Part Part2DObject](Part_Part2DObject.md) for the rest of the hidden properties.


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Sketcher_SketchObject#Scripting.md).


{{TitleProperty|Sketch}}

-    **Geometry|GeometryList**: a list of Part geometries that exist inside the sketch.

-    **External Geometry|LinkSubList**: a list of Part geometries outside this Sketch that are used for reference.

### View


{{TitleProperty|Auto Constraints}}

-    **Autoconstraints|Bool**: if `True` it will try setting constraints when the geometry is drawn.


{{TitleProperty|Visibility automation}}

-    **Editing Workbench|String**: name of the workbench to activate when editing the sketch; it defaults to {{value|SketcherWorkbench}}.

-    **Hide Dependent|Bool**: if `True` all objects that depend on the sketch are hidden when opening the sketch.

-    **Restore Camera|Bool**: if `True` the camera position is saved before opening the sketch, and is restored after closing it.

-    **Show Links|Bool**: if `True` all objects used in links to external geometry are shown when opening the sketch.

-    **Show Support|Bool**: if `True` all objects this sketch is attached to are shown when opening the sketch.

#### Hidden properties View 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Sketcher_SketchObject#Scripting.md).


{{TitleProperty|Visibility automation}}

-    **Tempo Vis|PythonObject**: a custom class associated with this object, that handles hiding and showing other objects when opening and closing the sketch.

All other view properties, including hidden properties, are those of the base [Part Feature](Part_Feature.md) object.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A SketchObject is created with the  
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObject", "Sketch")
obj.Label = "Custom label"
```

This basic `Sketcher::SketchObject` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `Sketcher::SketchObjectPython` object.

 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher Tools navi

}}  {{Document objects navi}} 
