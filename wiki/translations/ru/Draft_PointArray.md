---
 GuiCommand:
   Name: Draft PointArray
   MenuLocation: Modification , Array tools ,  Point array<br>Modify ,  Point array
   Workbenches: Draft_Workbench, BIM_Workbench
   Version: 0.18
   SeeAlso: Draft_OrthoArray, Draft_PolarArray, Draft_CircularArray, Draft_PathArray, Draft_PathLinkArray, Draft_PointLinkArray
---

# Draft PointArray/ru



## Описание

The <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> **Draft PointArray** command creates a regular array from a selected base object by placing copies at the points from a point object. Use the [Draft PointLinkArray](Draft_PointLinkArray.md) command to create a more efficient [Link](App_Link.md) array instead. Except for the type of array that is created, Link array or regular array, the [Draft PointLinkArray](Draft_PointLinkArray.md) command is identical to this command.

The base object can be a 2D object created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also a 3D object such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [BIM Workbench](BIM_Workbench.md).

The point object can be any object with a shape and vertices (including a [Std Part](Std_Part.md) containing one or more of such objects), as well as a [mesh](Mesh_Workbench.md) and a [point cloud](Points_Workbench.md). Duplicate points in the point object are filtered out.

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Draft PointArray*



## Применение

1.  Select the object you wish to array.
2.  Add the point object to the selection.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_PointArray.svg" width=16px> [Point array](Draft_PointArray.md)** button.
    -   [Draft](Draft_Workbench.md): Select the **Modification → Array tools → <img src="images/Draft_PointArray.svg" width=16px> Point array** option from the menu.
    -   [BIM](BIM_Workbench.md): Select the **Modify → <img src="images/Draft_PointArray.svg" width=16px> Point array** option from the menu.
4.  The array is created.
5.  Optionally change the [properties](#Properties.md) of the array in the [Property editor](property_editor.md).



## Свойства

See also: [Property editor](property_editor.md).

A Draft PointArray object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated:



### Данные


{{TitleProperty|Link}}

The properties in this group are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Objects}}

-    **Base|Link**: specifies the object to duplicate in the array.

-    **Count|Integer**: (read-only) specifies the number of elements in the array. This number is determined by the number of points in the **Point Object**.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Extra Placement|Placement**: : specifies an additional [placement](Placement.md), translation and rotation, for each element in the array.

-    **Fuse|Bool**: specifies if overlapping elements in the array are fused or not. Not used for Link arrays. <small>(v1.0)</small> 

-    **Point Object|Link**: specifies the object whose points are used to position the elements in the array.



### Вид


{{TitleProperty|Link}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Основные}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Display Options}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

The properties in this group are not inherited by Link arrays.



## Программирование

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a point array use the `make_point_array` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePointArray` method.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `point_object`is the object containing the points. It can also be the `Label` (string) of an object in the current document. It should have a `Geometry`, `Links`, or `Components` property containing points.

-    `extra`is an `App.Placement`, an `App.Vector` or an `App.Rotation` that displaces each element.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

Пример:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/ru
