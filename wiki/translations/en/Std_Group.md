---
- GuiCommand:
   Name:Std Group
   MenuLocation:[Tree view](Tree_view.md) → Right click on the document name → Create group
   Workbenches:All
   Shortcut:
   Version:
   SeeAlso:[Std Part](Std_Part.md), [Draft SelectGroup](Draft_SelectGroup.md), [Draft AddToGroup](Draft_AddToGroup.md)
---

## Description

[Std Group](Std_Group.md) (internally called [App DocumentObjectGroup](App_DocumentObjectGroup.md)) is a general purpose container that allows you to group different types of objects in the [tree view](tree_view.md), regardless of their data type. It is used as a simple folder to categorize and organize the objects in your model, in order to keep a logical structure. Std Groups may be nested inside other Std Groups.

The Std Group tool is not defined by a particular workbench, but by the base system, thus it is found in the {{MenuCommand|structure toolbar}} that is available in all [workbenches](Workbenches.md).

To group 3D objects as a single unit, with the intention of creating assemblies, use [Std Part](Std_Part.md) instead.

![](images/Std_Group_example.png )


*Various elements inside Std Groups in the tree view.*

## Usage

1.  Click on the name of the document in the [tree view](tree_view.md), open the context menu (right click), and choose **Create group**.
2.  Alternatively, press the **<img src="images/Std_Group.svg" width=16px> [Group](Std_Group.md)** button in the structure toolbar. An empty Group is created.
3.  To add objects to a Group, select them in [tree view](tree_view.md), and then drag and drop them over the Group.
4.  To remove objects from a Group, drag them out of the Group, and onto the document label at the top of the [tree view](tree_view.md).

### Notes

-   The Group object does not affect the positions in the [3D view](3D_view.md) of the elements that it contains; it is essentially just a folder that is used to keep the [tree view](tree_view.md) organized.
-   The Group can also be created from the [Python console](Python_console.md), and sub-classed to create special \"groups\", as indicated in the [Scripting](Std_Group#Scripting.md) section.

## Properties

A [Std Group](Std_Group.md) is internally called [App DocumentObjectGroup](App_DocumentObjectGroup.md) (`App::DocumentObjectGroup` class), and is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [App FeaturePython](App_FeaturePython.md), which is the most basic instance of an [App DocumentObject](App_DocumentObject.md), the App DocumentObjectGroup has the **Group** property.

These are the properties available in the [property editor](property_editor.md). Hidden properties can be shown by using the {{MenuCommand|Show all}} command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string.

-    **Group|LinkList**: a list of referenced objects. By default, it is empty {{value|[]}}.

#### Hidden properties Data {#hidden_properties_data}

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Std_Group#Scripting.md).

### View


{{TitleProperty|Base}}

See [App FeaturePython](App_FeaturePython.md) for the basic view properties.

#### Hidden properties View {#hidden_properties_view}

-    **Proxy|PythonObject**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Std_Group#Scripting.md).

## Inheritance

A [Std Group](Std_Group.md) is formally an instance of the class `App::DocumentObjectGroup`, whose parent is the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), and is augmented with a Group extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::DocumentObjectGroup* class is a simple container which uses the Group extension to be able to hold any type of object.`

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Group ([App DocumentObjectGroup](App_DocumentObjectGroup.md)) is created with the `addObject()` method of the document. Once a Group exists, other objects can be added to it with the `addObject()` or `addObjects()` methods of this Group. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

This basic `App::DocumentObjectGroup` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `App::DocumentObjectGroupPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

For example, a [FEM Analysis](FEM_Analysis.md) is an `App::DocumentObjectGroupPython` object with a custom icon and additional properties.

## Links

-   [Use case in Arch Tutorial](Arch_tutorial#Organizing_your_model.md)
-   [Document structure](Document_structure.md)
-   [Organizing your model](http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial#Organizing_your_model)





{{Std Base navi

}}  
