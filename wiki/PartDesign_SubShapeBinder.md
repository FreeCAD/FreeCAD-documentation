---
- GuiCommand:
   Name:PartDesign SubShapeBinder
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   MenuLocation:Part Design → Create a sub-object shape binder
   Version:0.19
   SeeAlso:[PartDesign ShapeBinder](PartDesign_ShapeBinder.md), [PartDesign Clone](PartDesign_Clone.md)
---

# PartDesign SubShapeBinder

## Description

A [PartDesign\_SubShapeBinder](PartDesign_SubShapeBinder.md) imports an element from another Body into the active [Body](PartDesign_Body.md). It can take the [Shape](Shape.md) of, or be \"bound\" to one or multiple objects or subelements (edges or faces) from another object.

Then the resulting binder object can be moved or be used to perform advanced operations like [booleans](PartDesign_Boolean.md) or [pads](PartDesign_Pad.md).

It can also bind to objects that are nested inside [Std Parts](Std_Part.md), and it will track the relative placement of these features. This is useful in the context of creating [assemblies](Assembly.md), as often the user needs to reference [features](PartDesign_Feature.md) that are already correctly placed in another subassembly.

 <img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;"> 



*Left: two solids created in two separate [bodies](PartDesign_Body.md). Right: two SubShapeBinders extracted from the first body, imported into the second body, and moved to a different position.*

 <img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;">  
*The two SubShapeBinders are used to create a [boolean cut](PartDesign_Boolean.md), and a [pad](PartDesign_Pad.md), with the second body.*

## Usage

1.  Start with a **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditivePrism.svg style="width:Body](PartDesign_Body.md)** already in place, containing a single [feature](PartDesign_Feature.md), for example, an **[16px">  [AdditivePrism](PartDesign_AdditivePrism.md)**.
2.  Create a second **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditiveBox.svg style="width:Body](PartDesign_Body.md)**, containing a single [feature](PartDesign_Feature.md), for example, an **[16px"> [AdditiveBox](PartDesign_AdditiveBox.md)**. This will be the active body.
3.  Select the entire first body, then press **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [SubShapeBinder](PartDesign_SubShapeBinder.md)**.
4.  Modify the properties of this binder object, for example its placement.
5.  Use it with another operation, such as **<img src=images/PartDesign_Boolean.svg style="width:16px"> [Boolean](PartDesign_Boolean.md)**.

## Properties

The _, the following properties are available in the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Support|XLinkSubList|hidden**: support for the geometry.

-    **Fuse|Bool**: if it is `True` it will fuse the solid linked shapes.

-    **Make Face|Bool**: if it is `True` it will created a face for the linked wires.

-    **Claim Children|PropertyBool**: if it is `True` it will claim the linked objects as children in the [tree view](Tree_view.md).

-    **Relative|Bool**: if it is `True` it will enable relative sub-object linking.

-    **Bind Mode|Enumeration**: binding mode, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: if it is `True` it will enable partial loading of the objects.

-    **Context|XLink|hidden**: container object of this binder object.

-    **_Version|Integer|hidden**: version of this type of object.

-    **Shape|PartShape|hidden**: [Part TopoShape](Part_TopoShape.md) of this object.


{{TitleProperty|Cache}}

-    **Body|Matrix|hidden**: unity matrix of this object.

### View

See [Part Feature](Part_Feature.md).

## Links

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), usage explanation with video.




 {{PartDesign Tools navi}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder
