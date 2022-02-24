# App DocumentObject/en
{{TOCright}}

## Introduction

<img alt="" src=images/Px.svg  style="width:32px;">

An [App DocumentObject](App_DocumentObject.md) object, or formally an `App::DocumentObject`, is the base class of all object classes handled in the document.

In general terms, a \"DocumentObject\" is any \"thing\" that can appear in the [Tree view](Tree_view.md), and which is saved and restored when opening a document.

![](images/App_DocumentObject_example.png )



*Tree view showing different objects in the document. Each of them is a "document object", ultimately derived from the base `App::DocumentObject* class.`

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in FreeCAD*

## Usage

The [App DocumentObject](App_DocumentObject.md) is an internal class, so it cannot be created from the graphical interface, nor is it meant to be used by itself. It just defines the basic behavior and properties of objects in the program.

Some of the most important DocumentObjects are the following:

-   The [App FeaturePython](App_FeaturePython.md) class, an empty object that can be used for different purposes, depending on the added properties.
-   The [App GeoFeature](App_GeoFeature.md) class, the base object of all geometrical objects, that is, of objects that have a [Placement](Placement.md) property that defines their position in the [3D view](3D_view.md).
-   The [Part Feature](Part_Feature.md) class, derived from App GeoFeature, and the parent class of objects with 2D and 3D [topological shapes](Part_TopoShape.md).
-   The [Mesh Feature](Mesh_Feature.md) class, derived from App GeoFeature, and the parent class of objects with 2D and 3D [meshes](Mesh_MeshObject.md).

## Properties

See [Property](Property.md) for all property types that scripted objects can have.

These are the basic properties that essentially all objects have. These properties can be accessed from the [Python console](Python_console.md).

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string. By default, it is the same as the `Name`.

-    **Label2|String**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine**: a list of expressions.

-    **Visibility|Bool**: whether to display the object or not.

For derived objects, only **Label** will be listed in the [property editor](property_editor.md) by default. The other properties will be hidden.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A DocumentObject is created with the `addObject()` method of the document. However, in general, there is no need to create this object manually. It is usually better to subclass one of the more complex classes, for example, [App FeaturePython](App_FeaturePython.md), [App GeoFeature](App_GeoFeature.md), [Part Feature](Part_Feature.md), [Part Part2DObject](Part_Part2DObject.md), etc.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObject", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App DocumentObject/en
