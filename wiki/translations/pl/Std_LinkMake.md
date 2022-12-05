---
- GuiCommand:
   Name:Std LinkMake
   MenuLocation:None
   Workbenches:All
   Version:0.19
   SeeAlso:[Std Part](Std_Part.md), [Std Group](Std_Group.md), [PartDesign Body](PartDesign_Body.md)
---

# Std LinkMake/pl

## Description


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)**

creates an [App Link](App_Link.md) (`App::Link` class), a type of object that references or links to another object, in the same document, or in another document. It is especially designed to efficiently duplicate a single object multiple times, which helps with the creation of complex [assemblies](assembly.md) from smaller subassemblies, and from multiple reusable components like screws, nuts, and similar fasteners.

The [App Link](App_Link.md) object was newly introduced in v0.19; in the past, simple duplication of objects could be achieved with **[<img src=images/Draft_Clone.svg style="width:16px"> [Draft Clone](Draft_Clone.md)**, but this is a less efficient solution due to its implementation which essentially creates a copy of the internal [Shape](Part_TopoShape.md) of the source object. On the other hand, a Link references directly the original Shape, so it is more memory efficient.

By itself the [Link](App_Link.md) object can behave like an array, duplicating its base object many times; this can be done by setting its **Element Count** property to {{Value|1}} or larger. This \"[Link Array](#Link_Array.md)\" object can also be created with the different array tools of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md), for example, **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft OrthoArray](Draft_OrthoArray.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft PolarArray](Draft_PolarArray.md)**, and **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft CircularArray](Draft_CircularArray.md)**.

When used with the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), Links are intended to be used with **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Bodies](PartDesign_Body.md)**, so it is recommended to set **Display Mode Body** to {{Value|Tip}} to select the features of the entire Body, and not the individual features. To create arrays of the internal [PartDesign Features](PartDesign_Feature.md), use **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign LinearPattern](PartDesign_LinearPattern.md)**, **[<img src=images/PartDesign_PolarPattern.svg style="width:16px"> [PartDesign PolarPattern](PartDesign_PolarPattern.md)**, and **[<img src=images/PartDesign_MultiTransform.svg style="width:16px"> [PartDesign MultiTransform](PartDesign_MultiTransform.md)**.

The **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)** tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar** that is available in all [workbenches](Workbenches.md). The Link object, used in conjunction with **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** to group various objects, forms the basis of the <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench.md) and <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4 Workbenches](Assembly4_Workbench.md).

## Usage

With selection:

1.  Select an object in the [tree view](tree_view.md) or [3D view](3D_view.md) for which you wish to create a Link.
2.  Press the **[<img src=images/Std_LinkMake.svg style="width:16px"> [Make link](Std_LinkMake.md)** button. The produced object has the same icon as the original object, but has an arrow overlay indicating it is a Link.

Without selection:

1.  If no object is selected, press the **[<img src=images/Std_LinkMake.svg style="width:16px"> [Make link](Std_LinkMake.md)** button to create an empty <img alt="" src=images/Link.svg  style="width:24px;"> Link.
2.  Go to the [property editor](property_editor.md), then click on the **Linked Object** property to open the [Link selection dialog](Selection_methods.md) to choose an object, then press **OK**.
3.  Instead of choosing an entire object in the [tree view](tree_view.md), you can also pick subelements (vertices, edges, or faces) of a single object in the [3D view](3D_view.md). In this case, the Link will duplicate only these subelements, and the arrow overlay will be different. This can also be done with **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std LinkMakeRelative](Std_LinkMakeRelative.md)**.

![](images/Std_Link_tree_example.png ) ![](images/Std_Link_example.png )



*(1) An object, (2) an empty Link, (3) a full Link to the first object (with overriding material), and (4) a Link to only some subelements of the object. The empty Link is not tied to the real object so it is not displayed in the [3D view](3D_view.md).*

## Usage: external documents 

1.  Start with a document that has at least one object which will be the source of the Link.
2.  Open a new document or an existing document. For easier handling, use **[<img src=images/Std_TreeMultiDocument.svg style="width:16px"> [Std TreeMultiDocument](Std_TreeMultiDocument.md)** to show both documents in the [tree view](tree_view.md). Before you proceed, [save](Std_Save.md) both documents. The Link won\'t be able to find its source and target unless both documents are saved on disk.
3.  In the first document, select the object that you wish to link; then switch tabs in the [main view area](main_view_area.md) to switch to the second document.
4.  Press **[<img src=images/Std_LinkMake.svg style="width:16px"> [Make link](Std_LinkMake.md)**. The produced object has the same icon as the original object, but has an additional arrow overlay indicating it is a Link coming from an external document.


**Notes:**

-   When saving the document with the Link, it will also ask to [save](Std_Save.md) the source document which contains the original object.

-   To include the original object in the document with the Link, use **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std LinkImport](Std_LinkImport.md)** or **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std LinkImportAll](Std_LinkImportAll.md)**.

-    **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)**can be used on an existing Link object, in order to create a Link to a Link which ultimately resolves to the original object in the source document. This can be used with **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std LinkMakeRelative](Std_LinkMakeRelative.md)** to pick only certain subelements as well.

![](images/Std_Link_tree_documents_example.png ) ![](images/Std_Link_documents_example.png )



*(1, 2) Two objects from a source document linked into a target document, (3) a Link to the second Link (with overriding material), and (4) a Link to the subelements of the second Link.*

### Dragging and dropping 

Instead of switching document tabs, you can create Links by performing a drag and drop operation in the [tree view](Tree_view.md): select the source object from the first document, drag it, then drop it into the second document\'s name while holding the **Alt** key in the keyboard.

Dragging and dropping results in different actions depending on the modifier key that is held.

-   Without modifier key it simply moves the object from one document to the other; an inclined arrow is shown in the cursor.
-   Holding the **Ctrl** key copies the object; a plus sign is shown in the cursor.
-   Holding the **Alt** key creates a Link; a pair of chain links is shown in the cursor.

For the **Ctrl** and **Alt** modifiers, dragging and dropping can also be done with a single document. That is, dragging an object and dropping it into the same document\'s name can be used to create multiple copies or multiple Links to it.

## Groups


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)**

can be used on **[<img src=images/Std_Part.svg style="width:16px"> [Std Parts](Std_Part.md)** in order to quickly duplicate groups of objects positioned in space, that is, [assemblies](assembly.md).

![](images/Std_Link_tree_Std_Part_example.png )



*Link created from a [Std Part](Std_Part.md); the objects are not duplicated but they are listed under the original container and under the Link container.*

A regular **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)** does not possess a **Placement** property, so it cannot control the position of the objects inside of it. However, when **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)** is used with **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)**, the resulting Link behaves essentially like a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)**, and can also be moved in space.

![](images/Std_Link_tree_Std_Group_example.png ) ![](images/Std_Link_Std_Group_example.png )



*Link created from a [Std Group](Std_Group.md); the objects are not duplicated but they are listed under the original container and under the Link container. The Link (with overriding material) can be moved in space, just like a [Std Part](Std_Part.md).*

A Link to a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** will keep the visibility of the objects synchronized with the original Part; so if you hide one object in a Link, it will be hidden in all Links and in the original object. On the other hand a Link to a **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)** will allow independent control of the visibilities.

![](images/Std_Link_tree_Std_Part_visibility.png ) ![](images/Std_Link_tree_Std_Group_visibility.png )



*Left: [Std Part](Std_Part.md) with two objects, and two Links to the Part; the visibility of the objects is synchronized. Right: [Std Group](Std_Group.md) with two objects, and two Links to the Group; the visibility of the objects is independently controlled in each group.*

## Overriding appearance 

When a Link is created, by default the **Override Material** is `False`, so the Link will have the same appearance as the original **Linked Object**.

When **Override Material** is set to `True`, the **Shape Material** property will now control the appearance of the Link.

Regardless of the state of **Override Material**, it is possible to individually set the appearance of the subelements (vertices, edges, faces) of a Link.

1.  Select the Link in the [tree view](tree_view.md). Open the context menu (right-click), and pick **Override colors**.
2.  Now pick the individual subelements that you want in the [3D view](3D_view.md), press **Edit**, and change the properties including transparency.
3.  To remove the custom attributes, select the elements in the list, and press **Remove**.
4.  When you are satisfied with the result, press **OK** to close the dialog.


**Note:**

as of v0.19, the coloring of the subelements is subject to the [topological naming problem](topological_naming_problem.md) so it should be done as the last modelling step, when the model is not subject to change any more.

<img alt="" src=images/Std_Link_override_color_example.png  style="width:500px;">



*(1) An original object, (2) a Link with overriding material, and (3) a second Link with individual modified subelements.*

## Link Array 


**See also:**

[Draft OrthoArray](Draft_OrthoArray.md).

When a Link is created, by default its **Element Count** is {{Value|0}}, so only a single Link object will be visible in the [tree view](tree_view.md).

Given that **Show Element** is `True` by default, when **Element Count** is set to {{Value|1}} or more, automatically more Links will be created below the first one; each new Link can be placed in the desired position by changing its own **Placement** property.

In similar way, each element of the array can have its own appearance changed, either by the **Override Material** and **Shape Material** properties, or by using the **Override colors** menu on the entire array and then selecting individual faces; this is described in [Overriding appearance](#Overriding_appearance.md).

<img alt="" src=images/Std_Link_tree_array_example.png ) ![](images/Std_Link_array_example.png  style="width:500px;">



*(1) Original object, and (2, 3, 4) a Link array with three elements, each in a different position. The first Link has overridden material and transparent faces, the other two have custom face colors.*

Once you are satisfied with the placement and properties of the Link elements in the array, you may change **Show Element** to `False` in order hide the individual Links in the [tree view](tree_view.md); this has the benefit of making the system more responsive, particularly if you have many objects in the document.

When creating this type of Link array, you must place each of the elements manually; however, if you would like to use specific patterns to place the copies, you may use the array tools of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md), like **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft OrthoArray](Draft_OrthoArray.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft PolarArray](Draft_PolarArray.md)**, and **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft CircularArray](Draft_CircularArray.md)**; these commands can create normal copies or Link copies depending on the options at creation time.

## Visibility

When **Show Element** is `True` and individual elements are listed in the [tree view](Tree_view.md) in a [Link Array](#Link_Array.md), each Link can be shown or hidden by pressing the **Space** bar in the keyboard.

Another way to hide the individual elements is using the **Override colors** menu.

1.  Select the array, open the **Override colors** menu (right click).
2.  In the [3D view](3D_view.md), pick any subelement from any Link in the array.
3.  Press **Hide**. An icon of an eye <img alt="" src=images/Invisible.svg  style="width:24px;"> should appear, indicating that this element has been hidden from the [3D view](3D_view.md). The object will temporarily show itself when the cursor hovers over the <img alt="" src=images/Invisible.svg  style="width:24px;"> icon.
4.  You can click **OK** to confirm the operation and close the dialog. The Link will remain hidden even if it is shown as visible in the [tree view](tree_view.md).

![](images/Std_Link_array_visibility_example.png )



*Element color dialog that is available when opening the context menu of a Link object in the tree view.*

If you wish to restore the visibility of this array element, enter the dialog once more, pick the eye icon, then click on **Remove** to remove the hidden status, and click **OK** to confirm and close the dialog. The element will be visible in the [3D view](3D_view.md) again.

When the Link is for a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** or a **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Part.md)**, the **Override colors** menu works in similar way as with arrays; it allows controlling the face color, entire object color, and visibility of the objects in the group.

![](images/Std_Link_Std_Part_visibility_example.png ) ![](images/Std_Link_Std_Part_visibility_example_3D.png )



*A [Std Part](Std_Part.md) containing three objects, and a Link to that Part; in the Link, (1) the first object is made invisible, (2) the second object has some subelements with different colors, (3) the entire third object has a different color and level of transparency.*

## Properties

An [App Link](App_Link.md) (`App::Link` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it has the latter\'s basic properties like **Label** and **Label2**.

The following are the specific properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty| Link}}

-    **Linked Object|XLink**: it indicates the source object of the [App Link](App_Link.md); this can be an entire object, or a subelement of it (vertex, edge, or face).

-    **Link Transform|Bool**: it defaults to `False`, in which case the Link will override the **Linked Object**\'s own placement. If it is set to `True`, the Link will be placed in the same position as the **Linked Object**, and its placement will be relative to the **Linked Object**\'s placement. This can also be achieved with **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std LinkMakeRelative](Std_LinkMakeRelative.md)**.

-    **Placement|Placement**: the placement of the Link in absolute coordinates.

-    **Link Placement|Placement|Hidden**: it is an offset applied on top of the **Placement** of the **Linked Object**. This property is normally hidden but appears if **Link Transform** is set to `True`; in this case, **Placement** now becomes hidden.

-    **Show Element|Bool**: it defaults to `True`, in which case the [tree view](tree_view.md) will show the individual Link copies, as long as **Element Count** is {{Value|1}} or larger.

-    **Element Count|IntegerConstraint**: it defaults to {{Value|0}}. If it is {{Value|1}} or larger, the [App Link](App_Link.md) will behave like an array, and will duplicate the same **Linked Object** many times. If **Show Elements** is `True`, each element in the array will be displayed in the [tree view](tree_view.md), and each can have its own **Placement** modified. Each Link copy will have a name based on the Link\'s [Name](Object_name.md), augmented by `_iN`, where `N` is a number starting from `0`. For example, with a single `Link`, the copies will be named `Link_i0`, `Link_i1`, `Link_i2`, etc.

-    **Link Execute|String**: name of the execute function that will run for this particular Link object. It defaults to {{Value|'appLinkExecute'}}. Set it to {{Value|'None'}} to disable it.

-    **Colored Elements|LinkSubHidden|Hidden**: list of Link elements that have had their color overriden.

-    **Scale|Float**: it defaults to {{Value|1.0}}. It is a factor for uniform scaling in each direction `X`, `Y`, and `Z`. For example, a cube of {{Value|2 mm}} x {{Value|2 mm}} x {{Value|2 mm}}, that is scaled by {{Value|2.0}}, will result in a shape with dimensions {{Value|4 mm}} x {{Value|4 mm}} x {{Value|4 mm}}.

-    **Scale Vector|Vector|Hidden**: the scale factor for each component `(X, Y, Z)` for all Link elements when **Element Count** is {{Value|1}} or larger. If **Scale** is other than {{Value|1.0}}, this same value will be used in the three components.

-    **Scale List|VectorList**: the scale factor for each Link element.

-    **Visibility List|BoolList|Hidden**: {{emphasis|(read-only)}} the visibility state of each Link element, either `True` or `False`.

-    **Placement List|PlacementList|Hidden**: {{emphasis|(read-only)}} the placement for each Link element.

-    **Element List|LinkList|Hidden**: the list of Link elements.

-    **_LinkTouched|Bool|Hidden**:

-    **_ChildCache|LinkList|Hidden**:


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Std_LinkMake#Scripting.md).

The [App Link](App_Link.md) object will additionally show the properties of the original **Linked Object**, so the [property editor](property_editor.md) may have groups of properties like {{TitleProperty|Attachment}}, {{TitleProperty|Box}}, {{TitleProperty|Draft}}, etc.

### View


{{TitleProperty| Link}}

-    **Draw Style|Enumeration**: it defaults to {{Value|None}}; it can be {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; defines the style of the edges in the [3D view](3D_view.md).

-    **Line Width|FloatConstraint**: a float that determines the width in pixels of the edges in the [3D view](3D_view.md). It defaults to {{value|2.0}}.

-    **Override Material|Bool**: it defaults to `False`; if set to `True` it will override the **Linked Object**\'s material, and it will display the colors defined in **Shape Material**.

-    **Point Size|FloatConstraint**: similar to **Line Width**, defines the size of the vertices.

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Shape Material|Material**: this property includes sub-properties that describe the appearance of the object.

    -   
        **Diffuse Color**
        
        , it defaults to  light blue .

    -   
        **Ambient Color**
        
        , it defaults to  dark gray .

    -   
        **Specular Color**
        
        , it defaults to  black .

    -   
        **Emissive Color**
        
        , it defaults to  black .

    -   
        **Shininess**
        
        , it defaults to {{Value|0.2}}

    -   
        **Transparency**
        
        , it defaults to {{Value|0.0}}.


{{TitleProperty|Base}}

-    **Child View Provider|PersistentObject|Hidden**:

-    **Material List|MaterialList|Hidden**: **(read-only)** if individual materials have been added, they will be listed here.

-    **Override Color List|ColorList|Hidden**: **(read-only)** if the individual faces or edges of the link have been overridden they will be listed here.

-    **Override Material List|BoolList|Hidden**: **(read-only)** if the individual materials of the link have been overridden they will be listed here.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{Value|'Link'}} or {{Value|'ChildView'}}.

-    **Show In Tree|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Visibility|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Selection Style|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

It will additionally show the view properties of the original **Linked Object**.

## Inheritance

An [App Link](App_Link.md) is formally an instance of the class `App::Link`, whose parent is the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class). It is a very low level object, which can be used with most other document objects.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `App::Link* object is a core component of the system, it does not depend on any workbench, but it can be used with most objects created in all workbenches.`

## Tworzenie skryptów 


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information.

An App Link is created with the `addObject()` method of the document. It can define its **Linked Object** by overriding its `LinkedObject` attribute, or by using its `setLink` method. 
```python
import FreeCAD as App

doc = App.newDocument()
bod1 = App.ActiveDocument.addObject("Part::Box", "Box")
bod2 = App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
bod1.Placement.Base = App.Vector(10, 0, 0)
bod2.Placement.Base = App.Vector(0, 10, 0)

obj1 = App.ActiveDocument.addObject("App::Link", "Link")
obj2 = App.ActiveDocument.addObject("App::Link", "Link")

obj1.LinkedObject = bod1
obj2.setLink(bod2)
obj1.Placement.Base = App.Vector(-10, -10, 0)
obj2.Placement.Base = App.Vector(10, -10, 0)
obj1.ViewObject.OverrideMaterial = True
App.ActiveDocument.recompute()
```

The basic `App::Link` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `App::LinkPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::LinkPython", "Link")
obj.Label = "Custom label"
```

## Further reading 

The [App Link](App_Link.md) object was introduced after 2 years of development and prototyping. This component was thought and developed almost single-handedly by user **realthunder**. The motivations and design implementations behind this project are described in his GitHub page, [Link](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link). In order to accomplish this feature, several core changes to FreeCAD were made; these were also extensively documented in [Core-Changes](https://github.com/realthunder/FreeCAD_assembly3/wiki/Core-Changes).

The App Link project started after the redesign of the [PartDesign Workbench](PartDesign_Workbench.md) was complete in v0.17. The history of App Link can be traced to some essential forum threads:

-   [Why an object can only be inside one App::Part?](https://forum.freecadweb.org/viewtopic.php?f=19&t=21505) (March 2017)
-   [Introducing App::Link/XLink](https://forum.freecadweb.org/viewtopic.php?f=10&t=21586) (March 2017)
-   [Links](https://forum.freecadweb.org/viewtopic.php?f=20&t=22216) (May 2017)
-   [Realthunder Link implementation: Architecture discussion](https://forum.freecadweb.org/viewtopic.php?f=20&t=23015) (June 2017)
-   [PR #876: Link, stage one, context aware selection](https://forum.freecadweb.org/viewtopic.php?f=17&t=23419) (July 2017)
-   [Preview: Link, stage two, API groundwork](https://forum.freecadweb.org/viewtopic.php?f=17&t=23626) (July 2017)
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712) (December 2017)
-   [Merging of my Link branch](https://forum.freecadweb.org/viewtopic.php?f=10&t=29542) (June 2018)

Finally, the pull request and merge happened:

-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=27&t=38621), old thread (July 2019), [pull request #2350](https://github.com/FreeCAD/FreeCAD/pull/2350) (the BIG merge), [LinkMerge branch](https://github.com/realthunder/FreeCAD/tree/LinkMerge).
-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=8&t=37757), main thread (July 2019)
-   [A simple path description of Link, 019, Link stage, Asm3, merge?](https://forum.freecadweb.org/viewtopic.php?p=329054#p329054) (August 2019)
-   [PR#2559: expose link and navigation actions](https://forum.freecadweb.org/viewtopic.php?f=17&t=39672), an introduction to the Link feature in 0.19 (September 2019).

Other miscellaneous \"links\" about Link include:

-   [Dynamic linked object](Dynamic_linked_object.md) - A pattern with Link and assemblies that aims to reduce duplication of assembly related logic such as orientation, positioning, or number of instances.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkMake/pl
