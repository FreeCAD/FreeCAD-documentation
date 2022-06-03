---
- GuiCommand   *
   Name   *Draft PointArray
   MenuLocation   *Modification → Array tools →  Point array
   Workbenches   *[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Version   *0.18
   SeeAlso   *[Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md), [Draft CircularArray](Draft_CircularArray.md), [Draft PathArray](Draft_PathArray.md), [Draft PathLinkArray](Draft_PathLinkArray.md), [Draft PointLinkArray](Draft_PointLinkArray.md)
---

# Draft PointArray/pt-br

## Descrição

The <img alt="" src=images/Draft_PointArray.svg  style="width   *24px;"> **Draft PointArray** command creates a regular array from a selected object by placing copies at the points from a [point compound](#Point_compound.md). Use the [Draft PointLinkArray](Draft_PointLinkArray.md) command to create a more efficient [Link](App_Link.md) array instead. Except for the type of array that is created, Link array or regular array, the [Draft PointLinkArray](Draft_PointLinkArray.md) command is identical to this command.

Both commands can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_PointArray_Example.png  style="width   *400px;"> 
*Draft PointArray*

## Utilização

1.  Select the object you wish to array.
2.  Add the [point compound](#Point_compound.md) object to the selection.
3.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_PointArray.svg" width=16px> [Draft PointArray](Draft_PointArray.md)** button.
    -   Select the **Modification → Array tools → <img src="images/Draft_PointArray.svg" width=16px> Point array** option from the menu.
4.  The array is created.
5.  Optionally change the [properties](#Properties.md) of the array in the [Property editor](property_editor.md).

## Point compound 

A point compound is an object that contains one or more points. These are the supported point compounds and how they can be created   *

-   [Part Compound](Part_Compound.md)   * Create one or more [Draft Points](Draft_Point.md) or [Part Points](Part_Point.md), select them and invoke the [Part Compound](Part_Compound.md) command.
-   Draft Block   * Create one or more [Draft Points](Draft_Point.md) or [Part Points](Part_Point.md), select them and invoke the [Draft Upgrade](Draft_Upgrade.md) command.
-   [Sketcher Sketch](Sketcher_NewSketch.md)   * Create a [Sketch](Sketcher_NewSketch.md) and add one or more [Sketcher Points](Sketcher_CreatePoint.md) to the sketch.

## Propriedades

See also   * [Property editor](property_editor.md).

A Draft PointArray object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated   *

### Data


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

-    **Base|Link**   * specifies the object to duplicate in the array.

-    **Count|Integer**   * (read-only) specifies the number of elements in the array. This number is determined by the number of points in the **Point Object**.

-    **Expand Array|Bool**   * specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Extra Placement|Placement**   *    * specifies an additional [placement](Placement.md), translation and rotation, for each element in the array. <small>(v0.19)</small> 

-    **Point Object|Link**   * specifies the compound object whose points are used to position the elements in the array. The object must have a **Links**, **Components** or **Geometry** property, and contain at least one element with **X**, **Y**, and **Z** properties.

### Vista


{{TitleProperty|Link}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**   * this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**   * this is an inherited property.


{{TitleProperty|Display Options}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**   * this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**   * for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be   * {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**   * not used.

-    **Pattern Size|Float**   * not used.


{{TitleProperty|Object style}}

The properties in this group are not inherited by Link arrays.

## Scripting

See also   * [Autogenerated API documentation](https   *//freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a point array use the `make_point_array` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePointArray` method.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `point_object`is the object containing the points. It can also be the `Label` (string) of an object in the current document. It should have a `Geometry`, `Links`, or `Components` property containing points.

-    `extra`is an `App.Placement`, an `App.Vector` or an `App.Rotation` that displaces each element.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

Example   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part   *   *Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/pt-br
