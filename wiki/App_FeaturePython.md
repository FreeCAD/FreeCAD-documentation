# App FeaturePython
## Introduction

An <img alt="" src=images/Feature.svg  style="width:32px;"> [App FeaturePython](App_FeaturePython.md) object, or formally an `App::FeaturePython`, is a simple instance of the [App DocumentObject](App_DocumentObject.md) in [Python](Python.md).

This is a simple object that by default doesn\'t have many properties, for example it doesn\'t have a [placement](Placement.md) or a [topological shape](Part_TopoShape.md). Depending on the properties that are assigned to it, it can be used to manage different types of data.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in FreeCAD*

## Usage

The [App FeaturePython](App_FeaturePython.md) is an internal object, so it cannot be created from the graphical interface. It is meant to be sub-classed by classes that will handle different types of data.

For example, the [Draft Text](Draft_Text.md), [Draft Dimension](Draft_Dimension.md), and [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) objects of the [Draft Workbench](Draft_Workbench.md) are `App::FeaturePython` objects with a custom icon and additional properties. They hold data but not an actual [Part TopoShape](Part_TopoShape.md).

If the desired object should have a placement, a shape, an attachment or other complex properties, it is better to create one of the more complex classes, for example, [App GeoFeature](App_GeoFeature.md), [Part Feature](Part_Feature.md), or [Part Part2DObject](Part_Part2DObject.md).

## Properties

See [Property](Property.md) for all property types that scripted objects can have.

The [App FeaturePython](App_FeaturePython.md) (`App::FeaturePython` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class) and inherits all its properties. It also has several additional properties.

These are the properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object.

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string.

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

### View


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom [viewprovider](Viewprovider.md) class associated with this object.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: it is empty by default.

-    **Show In Tree|Bool**: it defaults to `True`, in which case the object will appear in the [Tree view](Tree_view.md); otherwise, the object will be hidden in the tree view. Once an object in the tree is invisible, you can see it again by opening the context menu over the name of the document (right-click), and selecting {{CheckBox|TRUE|Show hidden items}}. Then the hidden item can be chosen and **Show In Tree** can be switched back to `True`.

-    **Visibility|Bool**: it defaults to `True`, in which case the object will be visible in the [3D view](3D_view.md) if it has a [Shape](Part_TopoShape.md), otherwise it will be invisible. By default this property can be toggled on and off by selecting the object, and pressing the **Space** bar.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: it controls the way in which the selection occurs in the [3D view](3D_view.md) if the object has a [Shape](Part_TopoShape.md), and there are many objects partially covered by others. It defaults to {{value|Disabled}}, meaning that no special highlighting will occur; {{value|Enabled}} means that the object will appear on top of any other object when selected; {{value|Object}} means that the object will appear on top only if the entire object is selected in the [Tree view](Tree_view.md); {{value|Element}} means that the object will appear on top only if a subelement (vertex, edge, face) is selected in the [3D view](3D_view.md).

-    **Selection Style|Enumeration**: it controls the way the object is highlighted if it has a [Shape](Part_TopoShape.md). If it is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} a bounding box will appear surrounding the object and will be highlighted.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

An App FeaturePython is created with the `addObject()` method of the document.

 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::FeaturePython", "Name")
obj.Label = "Custom label"
```

 {{Document_objects_navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > App FeaturePython
