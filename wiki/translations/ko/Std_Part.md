---
- GuiCommand:
   Name:Std Part
   MenuLocation:None
   Workbenches:All
   Version:0.17
   SeeAlso:[Std Group](Std_Group.md), [PartDesign Body](PartDesign_Body.md)
---

# Std Part/ko

## Description


**[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)**

(internally called [App Part](App_Part.md)) is a general purpose container that keeps together a group of objects so that they can be moved together as a unit in the [3D view](3D_view.md).

The Std Part element was developed to be the basic building block to create mechanical [assemblies](assembly.md). In particular, it is meant to arrange objects that have a [Part TopoShape](Part_TopoShape.md), like [Part Primitives](Part_Primitives.md), [PartDesign Bodies](PartDesign_Body.md), and other [Part Features](Part_Feature.md). The Std Part provides an [Origin object](#Origin.md) with local X, Y, and Z axes, and standard planes, that can be used as reference to position the contained objects. In addition, Std Parts may be nested inside other Std Parts to create a big assembly from smaller sub-assemblies.

Although it is primarily intended for solid bodies, the Std Part can be used to manage any object that has a [Placement](Placement.md) property, so it can also contain [Mesh Features](Mesh_Feature.md), [sketches](Sketch.md), and other objects derived from the [App GeoFeature](App_GeoFeature.md) class.

Do not confuse the **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)** with the **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)**. The first one is a specific object used in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), intended to model a [single contiguous solid](PartDesign_Body#Single_contiguous_solid.md) by means of [PartDesign Features](PartDesign_Feature.md). On the other hand, the [Std Part](Std_Part.md) is not used for modelling, just to arrange different objects in space, with the intention to create [assemblies](assembly.md).

The **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar** that is available in all [workbenches](Workbenches.md). To group objects arbitrarily without considering their position, use **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)**; this object does not affect the placements of the elements that it contains, it is essentially just a folder that is used to keep the [Tree view](Tree_view.md) organized.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Left: elements inside a Std Part in the [Tree view](Tree_view.md). Right: objects positioned in space, referred to the Origin of the Std Part.*

## Usage

1.  Press the **[<img src=images/Std_Part.svg style="width:16px"> [Create part](Std_Part.md)** button.
2.  An empty Part is created and automatically becomes *[active](Std_Part#Active_status.md)*.
3.  To add objects to the Part, select them in [Tree view](Tree_view.md), and drag and drop them onto the Part.
4.  To remove objects from the Part, drag them out of the Part, and onto the document label at the top of the [Tree view](Tree_view.md).
5.  Objects can also be added and removed by editing the **Group** property of the Part.

## Notes

-   An object can only belong to a single Part.
-   3D operations like [Part Boolean](Part_Boolean.md) cannot be applied to Parts. For example, you cannot select two Parts, and perform a [Part Fuse](Part_Fuse.md) or [Part Cut](Part_Cut.md).

## Properties

The [Std Part](Std_Part.md), internally called [App Part](App_Part.md) (`App::Part` class), is derived from the [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class) and inherits all its properties. It also has several additional properties. Notably properties that help it manage information in the context of an assembly, for example, **Type**, **Id**, **License**, **LicenseURL** and **Group**.

These are the properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Type|String**: a description for this object. By default, it is an empty string {{value|""}}.

-    **Material|Link**: the material for this object.

-    **Meta|Map|Hidden**: map with additional meta information. By default, it is empty {}.

-    **Id|String**: an identification or part number for this object. By default, it is an empty string {{value|""}}.

-    **Uid|UUID|Hidden**: the [universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (128-bit number) of the object. This is assigned at creation time.

-    **License|String**: a field to specify the license for this object. By default, it is an empty string {{value|""}}.

-    **LicenseURL|String**: a field to specify the web address to the license or contract for this object. By default, it is an empty string {{value|""}}.

-    **Color|Color**: a tuple of four floating point RGBA values white color.

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

-    **Origin|Link|Hidden**: the [App Origin](App_OriginGroupExtension.md) object that is the positional reference for all elements listed in **Group**.

-    **Group|LinkList**: a list of referenced objects. By default, it is empty {{value|[]}}.

-    **_ Group Touched|Bool|Hidden**: whether the group is touched or not.

### View


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [Tree view](Tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

## Detailed explanation 

### Active status 

An open document can contain multiple Parts. But only one Part can be active. The active Part is displayed in the [tree view](Tree_view.md) with the background color specified by the **Active container** value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). It will also be shown with bold text.

To activate or de-activate a Part:

-   Double click on it on the [Tree view](Tree_view.md), or
-   Open the context menu (right click) and select **Toggle active part**.

![](images/Std_Part_active.png )



*Document with two Std Parts, of which the second one is active.*

### Origin

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Left: Part Origin in the [Tree view](Tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


**Note:**

the Origin is an [App Origin](App_OriginGroupExtension.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Part are referenced to the Part\'s Origin which means that the Part can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.

### Visibility Management 

The Part\'s visibility supersedes the visibility of any object it contains. If the Part is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`. If the Part is visible, then each object\'s **Visibility** determines whether the object is shown or not.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*The visibility of the Std Part determines whether the objects grouped under it are shown in the [3D view](3D_view.md) or not. Left: the Part is hidden, so none of the objects will be shown in the [3D view](3D_view.md). Right: the Part is visible, so each object controls its own visibility.*

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Part ([App Part](App_Part.md)) is created with the `addObject()` method of the document. Once a Part exists, other objects can be added to it with the `addObject()` or `addObjects()` methods.


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

You cannot create a scripted `App::Part`. However, you can add `App::Part` behavior to a scripted `Part::FeaturePython` object by using the following code:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             group.MyGroup(),
                             group.ViewProviderMyGroup(),
                             True)
```





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/ko
