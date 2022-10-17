---
- GuiCommand   */pl
   Name   *Draft PathArray
   Name/pl   *Rysunek Roboczy   * Szyk po ścieżce
   MenuLocation   *Modyfikacja → Narzędzia szyku → Szyk po ścieżce
   Workbenches   *[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Version   *0.14
   SeeAlso   *[Szyk ortogonalny](Draft_OrthoArray/pl.md), [Szyk biegunowy](Draft_PolarArray/pl.md), [Szyk kołowy](Draft_CircularArray/pl.md), [Szyk powiązań po ścieżce](Draft_PathLinkArray/pl.md), [Szyk z punktów](Draft_PointArray/pl.md), [Szyk powiązań w punktach](Draft_PointLinkArray/pl.md)
---

# Draft PathArray/pl

## Opis

Polecenie <img alt="" src=images/Draft_PathArray.svg  style="width   *24px;"> **Szyk po ścieżce**\' tworzy zwykły szyk z wybranego obiektu przez umieszczenie kopii wzdłuż ścieżki. Zamiast tego użyj polecenia [Draft PathLinkArray](Draft_PathLinkArray.md), aby utworzyć bardziej wydajny szyk [powiązań](App_Link.md). Z wyjątkiem typu utworzonych szyków *(szyk powiązań lub zwykły szyk)*, polecenie [Szyk powiązań po ścieżce](Draft_PathLinkArray/pl.md) jest identyczne z tym poleceniem.

Oba polecenia mogą być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_PathArray_Example.png  style="width   *400px;"> 
*Szyk po ścieżce*

## Użycie

1.  Select the object you wish to array.
2.  Add the path object to the selection. It is also possible to select edges instead. The edges must belong to the same object and they must be connected.
3.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_PathArray.svg" width=16px> [Draft PathArray](Draft_PathArray.md)** button.
    -   Select the **Modification → Array tools → <img src="images/Draft_PathArray.svg" width=16px> Path array** option from the menu.
4.  The array is created.
5.  Optionally change the [properties](#Properties.md) of the array in the [Property editor](property_editor.md).

## Alignment

The alignment of the elements in a Draft PathArray depends on the properties of the array and the orientation of the source object. The position of the source object is ignored   * for the purpose of the array the {{Value|x}}, {{Value|y}} and {{Value|z}} are set to {{Value|0}}. If the **Align** property of the array is set to `False` the orientation of the array elements is identical to that of the source object. If it is set to `True` the X axis of the local coordinate system of each element placement is tangent to the path. The Y and Z axes of the local coordinate systems depend on the **Align Mode** property of the array. Other array properties involved in the alignment include **Tangent Vector**, **Force Vertical** and **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width   *600px;"> 
*3 arrays based on the same non-planar path. From left to right   * Align is false, Align is true with Align Mode Original and Align is true with Align Mode Frenet*.

### Align Mode 

Three modes are available   *

#### Original

This mode comes closest to the single **Align Mode** available in version 0.18. It relies on a fixed normal vector. If the path is planar this vector is perpendicular to the plane of the path, else a default vector, the positive Z axis, is used. From this normal vector and the local tangent vector (the local X axis) a [cross product](https   *//en.wikipedia.org/wiki/Cross_product) is calculated. This new vector is used as the local Z axis. The orientation of the local Y axis is determined from the local X and Z axes.

#### Frenet

This mode uses the local normal vector derived from the path at each element placement. If this vector cannot be determined (for example in the case of a straight segment) a default vector, again the positive Z axis, is used instead. With this vector and the local tangent vector the local coordinate system is determined using the same procedure as in the previous paragraph.

#### Tangent

This mode is similar to **Align Mode** {{Value|Original}} but includes the possibility to pre-rotate the source object by specifying a **Tangent Vector**.

### Force Vertical and Vertical Vector 

These properties are only available if **Align Mode** is {{Value|Original}} or {{Value|Tangent}}. If **Force Vertical** is set to `True` the local coordinate system is calculated in a different manner. The **Vertical Vector** is used as a fixed normal vector. From this normal vector and the local tangent vector (the local X axis) again a cross product is calculated. But now this vector is used as the local Y axis. The orientation of the local Z axis is determined from the local X and Y axes.

Using these properties can be required if one of the edged of the path is (almost) parallel to the default normal of the path.

## Properties

See also   * [Property editor](property_editor.md).

A Draft PathArray object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated   *

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
    


{{TitleProperty|Alignment}}

-    **Align|Bool**   * specifies if the elements in the array are aligned along the path or not. If it is `False` all other properties in this group, except **Extra Translation**, do not apply and are hidden.

-    **Align Mode|Enumeration**   * specifies the align mode, which can be {{Value|Original}}, {{Value|Frenet}} or {{Value|Tangent}}.

-    **Extra Translation|VectorDistance**   * specifies an additional displacement for each element along the path.

-    **Force Vertical|Bool**   * specifies whether to override the default normal direction with the value of **Vertical Vector**. Only used if **Align Mode** is {{Value|Original}} or {{Value|Tangent}}.

-    **Tangent Vector|Vector**   * specifies the alignment vector. Only used if **Align Mode** is {{Value|Tangent}}.

-    **Vertical Vector|Vector**   * specifies the override for the default normal direction. Only used if **Vertical Vector** is `True`.


{{TitleProperty|Objects}}

-    **Base|LinkGlobal**   * specifies the object to duplicate in the array.

-    **Count|Integer**   * specifies the number of elements in the array.

-    **Expand Array|Bool**   * specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Path Object|LinkGlobal**   * specifies the object to be used for the path. It must contain {{Value|Edges}} in its [Part TopoShape](Part_TopoShape.md).

-    **Path Subelements|LinkSubListGlobal**   * specifies a list of edges of the **Path Object**. If supplied only these edges are used for the path.

### View


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

To create a path array use the `make_path_array` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePathArray` method.


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `path_object`is the path object. It can also be the `Label` (string) of an object in the current document.

-    `count`is the number of elements in the array.

-    `extra`is a vector that displaces each element.

-    `subelements`is a list of edges of `path_object`, for example `["Edge1", "Edge2"]`. If supplied only these edges are used for the path.

-   If `align` is `True` the elements are aligned along the path depending on the value of `align_mode`, which can be `"Original"`, `"Frenet"` or `"Tangent"`.

-    `tan_vector`is a unit vector that defines the local tangent direction of the elements along the path. It is used when `align_mode` is `"Tangent"`.

-   If `force_vertical` is `True` `vertical_vector` is used for the local Z direction of the elements along the path. It is used when `align_mode` is `"Original"` or `"Tangent"`.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

-    `path_array`is returned with the created array object.

Przykład   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/pl
