---
- GuiCommand:
   Name/ru:Создать новую под-объектную связующую форму
   Name:PartDesign_SubShapeBinder
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   MenuLocation:Part Design → Create a sub-object shape binder
   Version:0.19
   SeeAlso:[Создать связующую форму](PartDesign_ShapeBinder/ru.md), [Создать клон](PartDesign_Clone/ru.md)
---

# PartDesign SubShapeBinder/ru


</div>

## Описание

The **PartDesign SubShapeBinder** tool creates a shape binder referencing geometry from one or more parent objects. A SubShapeBinder is typically used inside a [PartDesign Body](PartDesign_Body.md) to reference geometry outside the Body. Using external geometry directly in a Body is not allowed and will lead to out of scope errors. But a SubShapeBinder can also be used without being nested in a Body.

A SubShapeBinder will track the relative placement of the referenced geometry, which is useful in the context of creating [assemblies](Assembly.md), but on top of that also has its own placement.

The referenced geometry can consist of one or multiple elements. Each element can be an individual object (for example a [PartDesign Body](PartDesign_Body.md)), a subobject (for example a [Part Box](Part_Box.md) inside a [Std Part](Std_Part.md), or a [sketch](PartDesign_NewSketch.md) or [Feature](PartDesign_Feature.md) inside a Body), or a subelement (a face, edge or vertex). Which geometry should be selected depends on the intended purpose of the SubShapeBinder. For a Boolean operation you would need to select a solid. For a [Pad operation](PartDesign_Pad.md) a face, a sketch or a planar wire can be used. And for the [external geometry](Sketcher_External.md) in a sketch, or to attach a sketch, any combination of subelements may be appropriate. Elements can belong to different parent objects, and can even belong to the Body the SubShapeBinder is nested in. Because a SubShapeBinder is [Link-based](Std_LinkMake.md) the referenced geometry can also belong to an external document.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;"> 
*On the left two solids created in two separate [Bodies](PartDesign_Body.md).<br>
On the right two SubShapeBinders referencing geometry from the first Body, nested in the second Body, and moved to a different position.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*The two SubShapeBinders are used to create a [Boolean cut](PartDesign_Boolean.md) and a [Pad](PartDesign_Pad.md) in the second Body.*

## Применение

### Same document 

1.  If there are multiple Bodies in the document: optionally [activate the Body](PartDesign_Body#Active_status.md) the SubShapeBinder should be nested in.
2.  Select the required geometry. Subelements can only be selected in the [3D view](3D_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_SubShapeBinder.svg" width=16px> [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md)** button.
    -   Select the **Part Design → <img src="images/PartDesign_SubShapeBinder.svg" width=16px> Create a sub-object(s) shape binder** option from the menu.
4.  The SubShapeBinder is created.
5.  If there is only one Body in the document the SubShapeBinder is automatically added to it and the Body is activated. If this is the case and the SubShapeBinder should not be nested, it can be dragged out of the Body and dropped onto the <img alt="" src=images/Document.svg  style="width:16px;"> document node in the [Tree view](Tree_view.md).

### External document 

1.  If required open the source document (the external document) and the target document. Both documents must have been saved at least once.
2.  If there are multiple Bodies in the target document: optionally activate the Body the SubShapeBinder should be nested in.
3.  Select the required geometry in the source document. Subelements can only be selected in the [3D view](3D_view.md).
4.  Switch to the target document by clicking its tab in the [Main view area](Main_view_area.md).
5.  Invoke the tool as described above.

### Start with empty SubShapeBinder 

1.  Follow the instructions described under [Same document](#Same_document.md) above but without selecting geometry.
2.  An empty SubShapeBinder is created.
3.  Select the required geometry. Subelements can only be selected in the [3D view](3D_view.md).
4.  In the [Tree view](Tree_view.md) drag and drop the selection onto the SubShapeBinder. If you have selected subelements their parent objects are highlighted in the [Tree view](Tree_view.md), indicating the objects to be dragged.
5.  Optionally add more geometry in the same manner.
6.  To replace already referenced geometry hold down **Ctrl** during the drag and drop operation.

## Notes

-   2D offsetting is supported for some shape types, included planar faces, edges and wires. Because offsetting is a difficult operation for the software it does not always succeed. <small>(v0.20)</small> 
-   A SubShapeBinder that is not nested in a Body can be used as the [Base Feature](PartDesign_Body#Base_Feature.md) for a new Body.
-   The **Support** property contains the links to the referenced geometry. The property is read only by default, but can be changed by following the instructions described under [Start with empty SubShapeBinder](#Start_with_empty_SubShapeBinder.md).
-   A SubShapeBinder created from a sketch can have an opposite \"tool direction\". For example a [Pad](PartDesign_Pad.md) created from the sketch may extend in the +Y direction, while a [Pad](PartDesign_Pad.md), with the same properties, created from the SubShapeBinder extends in the -Y direction. Toggling the **Reversed** property (or checkbox) will solve this.

## Различия между связующей формой и под-объектной связующей формой 

The PartDesign SubShapeBinder tool and the [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) tool are quite similar. Their names are somewhat confusing as both can reference whole objects and subelements.

The main differences are:

-   Editing a PartDesign ShapeBinder is easier. Double-clicking the object in the [Tree view](Tree_view.md) will open a task panel.
-   A PartDesign ShapeBinder can either reference a single whole object, or subelements belong to a single parent object. A PartDesign SubShapeBinder does not have these restrictions.
-   Only PartDesign SubShapeBinders can reference geometry from an external file.
-   A PartDesign SubShapeBinder always tracks the relative placement of the referenced geometry. For a PartDesign ShapeBinder this behavior is optional through its **Trace Support** property.
-   Only PartDesign SubShapeBinders support 2D offsetting.

## Свойства

A PartDesign SubShapeBinder object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Данные


{{TitleProperty|Основные}}

-    **Support|XLinkSubList**: support for the geometry.

-    **Fuse|Bool**: if it is `True` it will fuse the solid linked shapes.

-    **Make Face|Bool**: if it is `True` it will created a face for the linked wires.

-    **Claim Children|PropertyBool**: if it is `True` it will claim the linked objects as children in the [tree view](Tree_view.md).

-    **Relative|Bool**: if it is `True` it will enable relative sub-object linking.

-    **Bind Mode|Enumeration**: binding mode, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: if it is `True` it will enable partial loading of the objects.

-    **Context|XLink|hidden**: container object of this binder object.

-    **Bind Copy On Change|Enumeration**
    

-    **Refine|Bool**: if `True` redundant edges will be removed (for example after a boolean operation). <small>(v0.20)</small> 

-    **_ Version|Integer|hidden**: version of this type of object.

-    **_ Copied Link|XLinkSub|hidden**
    


{{TitleProperty|Cache}}

-    **Body|Matrix|hidden**: unity matrix of this object.


{{TitleProperty|Offsetting}}

-    **Offset**: 2D offset to apply. If Offset = 0, then no offset is applied. If Offset \< 0, then the offset is applied inward. <small>(v0.20)</small> 

-    **Offset Join Type**: Join method of offsetting non-tangent joints. The method can be {{Value|Arcs}}, {{Value|Tangent}} or {{Value|Intersection}}. <small>(v0.20)</small> 

-    **Offset Fill|Bool**: If `True`, a face is made between the new wire and the original wire. See also the **Make Face** property. <small>(v0.20)</small> 

-    **Offset Open Result|Bool**: Affects the way open wires are processed. If `False`, an open wire is made. If `True`, a closed wire is made from a double-sided offset, with rounds around open vertices. <small>(v0.20)</small> 

-    **Offset Intersection|Bool**: Affects the way compounds are processed. If `False`, all children are processed independently. If `True`, and children are edges and wires, the children are offset in a collective manner. <small>(v0.20)</small> 

## Ссылки

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), usage explanation with video.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/ru
