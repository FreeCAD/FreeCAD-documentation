---
- GuiCommand:/ro
   Name:Std Part
   Name/ro:Std Part
   Workbenches:All
   MenuLocation:None
   Version:0.17
   SeeAlso:[Std Group](Std_Group/ro.md), [PartDesign Body](PartDesign_Body/ro.md)
---

# Std Part/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**Part**(piesa) este un container de uz general care ține împreună un grup de obiecte astfel încât ele pot fi mișcate ca o unitate. Piesa poate conține majoritatea obiectelor FreeCAD, cum ar fi corpurile PartDesign, obiecte ale atelierului Part, obiecte Mesh etc.


</div>


<div class="mw-translate-fuzzy">

Piesa oferă un sistem local de coordonate la care se pot atașa schițe și alte obiecte.


</div>

Although it is primarily intended for solid bodies, the Std Part can be used to manage any object that has a [Placement](Placement.md) property, so it can also contain [Mesh Features](Mesh_Feature.md), [sketches](Sketch.md), and other objects derived from the [App GeoFeature](App_GeoFeature.md) class.


<div class="mw-translate-fuzzy">

O Piesă se află în bara de instrumente Structure care este afișată în toate atelierele de lucru.


</div>

The **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar** that is available in all [workbenches](Workbenches.md). To group objects arbitrarily without considering their position, use **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)**; this object does not affect the placements of the elements that it contains, it is essentially just a folder that is used to keep the [tree view](tree_view.md) organized.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Left: elements inside a Std Part in the [tree view](tree_view.md). Right: objects positioned in space, referred to the Origin of the Std Part.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

-   Press the **<img src="images/Std_Part.png" width=24px> '''Create part'''** button in the toolbar. The Part automatically becomes active.
-   Double-click the Part in the Model tree to activate or deactivate it.
-   To add objects to a Part, drag & drop them over the Part in the Model tree.
-   To remove objects from a Part, drag & drop them out of the Part and on the document label at the top of the Model tree.


</div>

### Notes

-   As of v0.19, a given object can only belong to a single Part.
-   Double-click the Part in the [tree view](tree_view.md) or open the context menu (right-click) and select **Toggle active part** to activate or deactivate the Part. If another Part is active, it will be deactivated. See [active status](Std_Part#Active_status.md) for more information.


<div class="mw-translate-fuzzy">

## Limite


</div>


<div class="mw-translate-fuzzy">

-   Chiar și atunci când o Piesă este activă, obiectele nou create nu sunt lasate în interiorul Piesei/Part, dar vor fi plasate în partea de jos a arborescenței. Pur și simplu glisați și fixați-le peste Piesă.
-   O piesă nu are formă. Nu este posibil să aplicați cele mai multe operații 3D asupra unei Piesei, ca operații Booleene.
-   În acest moment, [ Draft Snaps](Draft_Snap.md) nu funcționează pe unul sau mai multe containere Piesă selectate sau pe obiectele din interiorul unui container.
-   \'\' Notă a Redactorului: în acest moment nu este clar statutul activ al piesei nu este clar. \'\'


</div>

## Proprietăți

A [Std Part](Std_Part.md) is internally called [App Part](App_Part.md) (`App::Part` class), and is derived from an [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class), therefore it shares most of the latter\'s properties.

In addition to the properties described in [App GeoFeature](App_GeoFeature.md), the App Part class has some properties that help it manage information in the context of an assembly, for example, **Type**, **Id**, **License**, **LicenseURL**, **Color**, and **Group**.

These are the properties available in the [property editor](property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Id**: ID (Part number) of the item. This field is optional.

-    **License**: the license under which the part is released.

-    **License URL**: the Web address where the terms license can be found.

-    **Placement**: specifies the orientation and position of the Part in the 3D space. See [Placement](Placement.md).

-    **Label**: the Label is the name given to the operation. This name can be changed at your convenience.

-    **Group**: lists the referenced objects.


</div>

#### Hidden properties Data 

-    **Material|Map**: map with material properties. By default, it is empty {}.

-    **Meta|Map**: map with additional meta information. By default, it is empty {}.

-    **Uid|UUID**: the [universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (128-bit number) of the object. This is assigned at creation time.

-    **Label2|String**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool**: whether to display the object or not.

-    **Origin|Link**: the [App Origin](App_Origin.md) object that is the positional reference for all elements listed in **Group**.

-    **_ Group Touched|Bool**: whether the group is touched or not.

### View

The App Part only has the five properties of the basic [App FeaturePython](App_FeaturePython.md), and it does not have hidden properties.


{{TitleProperty|Base}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [tree view](tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


<div class="mw-translate-fuzzy">

### Example de utilizări 

-   As an assembly container that groups objects to be manufactured separately then glued or screwed together, like a wooden table.
-   When importing a STEP assembly in FreeCAD, the main assembly and its sub-assemblies are Part containers.
-   A part that is composed of multiple non-fused components, like a ball bearing.


</div>

The Std Part is intended to be the basic building block to create assemblies. Unlike a [PartDesign Body](PartDesign_Body.md), an assembly is meant to be a collection of separate, distinguishable elements which are connected in some way in the physical world, for example, through pressure, screws, or glue.

Examples that could be Parts:

-   A wooden table that consists of individual wooden pieces (legs, top), which are put together by glue or metal screws.
-   A ball bearing that is composed of multiple steel balls, an inner ring, a retainer, a seal, and an outer ring.
-   An assembly of a screw with a washer, and a matching nut.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Left: three individual contiguous solids, each of them modelled by a [PartDesign Body](PartDesign_Body.md). Right: the individual Bodies put together inside a Std Part to create an assembly.*

In general terms, when importing a STEP file into the program, the main assembly and its sub-assemblies will be imported as Part containers, each of them containing a simple [Part Feature](Part_Feature.md).

## Detailed explanation 


<div class="mw-translate-fuzzy">

### Status Active 

A FreeCAD document can contain multiple Parts. Only one Part can be active at a time. An active Part will be displayed in the tree with a light blue background color.


</div>

An open document can contain multiple Parts. An active Part will be displayed in the [tree view](Tree_view.md) with the background color specified by the **Active container** value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). An active part will also be shown in bold text.

To activate or de-activate a Part:

-   Double click on it on the [tree view](Tree_view.md), or
-   Open the context menu (right click) and select **Toggle active part**.


**Notes:**

-   The {{emphasis|active status}} of Parts was developed in v0.17 in parallel with the {{emphasis|active status}} of [PartDesign Bodies](PartDesign_Body.md); however, as of v0.19 this status does not serve a real purpose for Parts.
-   Even when a Part is active, newly created objects are not placed inside of it automatically. In this case, simply drag these new objects, and drop them onto the desired Part.
-   Only a single Part can be active at a time.

![](images/Std_Part_active.png )



*Document with two Std Parts, of which the second one is active.*


<div class="mw-translate-fuzzy">

### Origini

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). Sketches can be attached to these planes. All elements inside the Part are referenced to the Part\'s Origin; which means that the Part can be moved and rotated in reference to the global coordinate system without affecting the placement of elements inside it.


</div>

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Left: Part Origin in the [tree view](tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


**Note:**

the Origin is an [App Origin](App_Origin.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Part are referenced to the Part\'s Origin which means that the Part can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.


<div class="mw-translate-fuzzy">

### Managementul Vizibilității 

The Part\'s visibility supersedes the visibility of any object it contains. If the Part is hidden, the objects it contains will be hidden as well, even if their visibility is set to true. Multiple objects inside a Part can be visible at a time.


</div>

The Part\'s visibility supersedes the visibility of any object it contains. If the Part is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`. If the Part is visible, then each object\'s **Visibility** determines whether the object is shown or not.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*The visibility of the Std Part determines whether the objects grouped under it are shown in the [3D view](3D_view.md) or not. Left: the Part is hidden, so none of the objects will be shown in the [3D view](3D_view.md). Right: the Part is visible, so each object controls its own visibility.*

### Inheritance

A [Std Part](Std_Part.md) is formally an instance of the class `App::Part`, whose parent is the basic [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class), and is augmented with an Origin extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `App::Part* class is a simple container that has a position in 3D space, and has an Origin to control the placement of the objects grouped under it.`

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Part ([App Part](App_Part.md)) is created with the `addObject()` method of the document. Once a Part exists, other objects can be added to it with the `addObject()` or `addObjects()` methods of this Part.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::Part", "Part")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

You cannot create a scripted `App::Part`. However, you can add `App::Part` behaviour to a scripted `Part::FeaturePython` object by using the following code:


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
        obj.addExtension('App::OriginGroupExtensionPython')
        obj.Origin = FreeCAD.ActiveDocument.addObject('App::Origin', 'Origin')

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
        vobj.addExtension('Gui::ViewProviderOriginGroupExtensionPython')
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject('Part::FeaturePython', 'Group', group.MyGroup(), group.ViewProviderMyGroup(), True)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/ro
