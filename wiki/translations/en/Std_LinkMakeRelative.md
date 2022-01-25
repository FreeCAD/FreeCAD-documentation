---
- GuiCommand:
   Name:Std LinkMakeRelative
   MenuLocation:None
   Workbenches:All
   Version:0.19
   SeeAlso:[Std Part](Std_Part.md), [Std Group](Std_Group.md), [Std LinkMake](Std_LinkMake.md)
---

# Std LinkMakeRelative/en

## Description


**[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std LinkMakeRelative](Std_LinkMakeRelative.md)**

creates an [App Link](App_Link.md) (`App::Link` class), just like **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)**, but it operates on selected subelements first, and sets the **Link Transform** to `True`.

## Usage

With selection:

1.  Select a subelement in the [3D view](3D_view.md), this means a vertex, edge, or face, or any combination of these. These subelements must belong to a single object.
2.  Press the **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std LinkMakeRelative](Std_LinkMakeRelative.md)** button. The produced object has the same icon as the original object, but has two arrow overlays indicating it is a relative Link.

Without selection:

-   If no object is selected, this command does nothing.
-   If an object is selected in the [tree view](tree_view.md) only, but no subelement is selected in the [3D view](3D_view.md), the command does nothing either.

<img alt="" src=images/Std_Link_tree_sublink_example.png ) ![](images/Std_Link_sublink_example.png  style="width:500px;">



*Original body, and three Links created from the subelements of it, including edges and faces.*

## Properties

This command creates a new [App Link](App_Link.md); its properties are described in **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)**.

In particular, **Link Transform** is set to `True`, so **Placement** becomes hidden, and instead **Link Placement** controls the position of the Link with respect to the position of **Linked Object**.

## Scripting

See [Std LinkMake](Std_LinkMake.md) for the general information.

An App Link is created with the `addObject()` method of the document. To define a relative link, its `setLink` method is used to pick the source object, and one or more of its subelements. Then the `LinkTransform` attribute is set to `True`.


```python
import FreeCAD as App

doc = App.newDocument()
body = App.ActiveDocument.addObject("Part::Box", "Box")

obj = App.ActiveDocument.addObject("App::Link", "Link")
obj.setLink(body, '', ['Edge1', 'Edge6', 'Edge7', 'Edge10', 'Face2', 'Face3'])
obj.LinkTransform = True
obj.LinkPlacement.Base = App.Vector(20, 20, 0)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkMakeRelative/en
