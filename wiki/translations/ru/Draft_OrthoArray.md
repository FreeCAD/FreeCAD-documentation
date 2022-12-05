---
- GuiCommand:
   Name:Draft OrthoArray
   MenuLocation:Modification → Array tools → Array
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Version:0.19
   SeeAlso:[Draft PolarArray](Draft_PolarArray.md), [Draft CircularArray](Draft_CircularArray.md), [Draft PathArray](Draft_PathArray.md), [Draft PathLinkArray](Draft_PathLinkArray.md), [Draft PointArray](Draft_PointArray.md), [Draft PointLinkArray](Draft_PointLinkArray.md)
---

# Draft OrthoArray/ru

## Описание

The <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> **Draft OrthoArray** command creates an orthogonal (3-axes) array from a selected object. The command can optionally create a [Link](App_Link.md) array, which is more efficient than a regular array.

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Array_example.png  style="width:300px;"> 
*Draft OrthoArray*

## Применение

1.  Optionally select one object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_OrthoArray.svg" width=16px> [Draft OrthoArray](Draft_OrthoArray.md)** button.
    -   Select the **Modification → Array tools → <img src="images/Draft_OrthoArray.svg" width=16px> Array** option from the menu.
3.  The **Orthogonal array** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an object: select one object.
5.  Enter the required parameters in the task panel.
6.  To finish the command do one of the following:
    -   Click in the [3D view](3D_view.md).
    -   Press **Enter**.
    -   Press the **OK** button.

## Options

-   Enter the **Number of elements** for the X, Y and Z directions. This number must be at least {{Value|1}} for every direction.
-   Enter the **X intervals** to specify the displacement for the elements in the X direction. For a rectangular array the Y and Z values must be {{Value|0}}.
-   Enter the **Y intervals** to specify the displacement for the elements in the Y direction. For a rectangular array the X and Z values must be {{Value|0}}.
-   Enter the **Z intervals** to specify the displacement for the elements in the Z direction. For a rectangular array the X and Y values must be {{Value|0}}.
-   Press the **Reset X, Y or Z** button to reset the displacement in the given direction to the default values.
-   If the **Fuse** checkbox is checked overlapping elements in the array are fused. This does not work for Link arrays.
-   If the **Link array** checkbox is checked a Link array instead of a regular array is created. A Link array is more efficient because its elements are [App Link](App_Link.md) objects.
-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   A Draft OrthoArray can be turned into a [Draft PolarArray](Draft_PolarArray.md) or a [Draft CircularArray](Draft_CircularArray.md) by changing its **Array Type** property.
-   A Link array cannot be turned into a regular array or vice versa. The type of array must be decided at creation time.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Properties

See also: [Property editor](property_editor.md).

The Draft OrthoArray command, the [Draft PolarArray command](Draft_PolarArray.md) and the [Draft CircularArray command](Draft_CircularArray.md) create the same object. This object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated:

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
    


{{TitleProperty|Circular array}}

The properties in this group are hidden for orthogonal arrays and polar arrays.

-    **Number Circles|Integer**: specifies the number of circular layers. Must be at least {{Value|2}}.

-    **Radial Distance|Distance**: specifies the distance between circular layers.

-    **Symmetry|Integer**: specifies the number of symmetry lines. This number changes the distribution of the elements in the array.

-    **Tangential Distance|Distance**: specifies the distance between elements in the same circular layer. Must be larger than zero.


{{TitleProperty|Objects}}

-    **Array Type|Enumeration**: specifies the type of array, which can be {{value|ortho}}, {{value|polar}} or {{value|circular}}.

-    **Axis Reference|LinkGlobal**: specifies the object and edge to be used instead of the **Axis** and **Center** properties. Not used for orthogonal arrays.

-    **Base|Link**: specifies the object to duplicate in the array.

-    **Count|Integer**: (read-only) specifies the total number of elements in the array. Only available for Link arrays.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Fuse|Bool**: specifies if overlapping elements in the array are fused or not. Not used for Link arrays.


{{TitleProperty|Orthogonal array}}

The properties in this group are hidden for circular arrays and polar arrays.

-    **Interval X|VectorDistance**: specifies the interval between elements in the X direction.

-    **Interval Y|VectorDistance**: specifies the interval between elements in the Y direction.

-    **Interval Z|VectorDistance**: specifies the interval between elements in the Z direction.

-    **Number X|Integer**: specifies the number of elements in the X direction. Must be at least {{Value|1}}.

-    **Number Y|Integer**: specifies the number of elements in the Y direction. Must be at least {{Value|1}}.

-    **Number Z|Integer**: specifies the number of elements in the Z direction. Must be at least {{Value|1}}.


{{TitleProperty|Polar array}}

The properties in this group are hidden for circular arrays and orthogonal arrays.

-    **Angle|Angle**: specifies the aperture of the circular arc. Use {{value|360&#176;}} for a full circle.

-    **Interval Axis|VectorDistance**: specifies the interval between elements in the **Axis** direction.

-    **Number Polar|Integer**: specifies the number of elements in the polar direction.


{{TitleProperty|Polar/circular array}}

The properties in this group are hidden for orthogonal arrays.

-    **Axis|Vector**: specifies the direction of the axis of the array.

-    **Center|VectorDistance**: specifies the center point of the array. The axis of the array passes through this point. For circular arrays it is an offset from the **Placement** of the **Base** object.

### View


{{TitleProperty|Link}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

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

## Scripting


<div class="mw-translate-fuzzy">


**Смотри так же:**

[Draft API](Draft_API/ru.md) и [Основы написания скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

### Parametric array 

To create a parametric orthogonal array use the `make_array` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeArray` method. The `make_array` method can create Draft OrthoArrays, [Draft PolarArrays](Draft_PolarArray.md) and [Draft CircularArrays](Draft_CircularArray.md). For each array type one or more wrappers are available.

The main method:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

The wrappers for orthogonal arrays are:


```python
array = make_ortho_array(base_object,
                         v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10),
                         n_x=2, n_y=2, n_z=1,
                         use_link=True)
```


```python
array = make_ortho_array2d(base_object,
                           v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0),
                           n_x=2, n_y=2,
                           use_link=True)
```

The wrappers for rectangular arrays are:


```python
array = make_rect_array(base_object,
                        d_x=10, d_y=10, d_z=10,
                        n_x=2, n_y=2, n_z=1,
                        use_link=True)
```


```python
array = make_rect_array2d(base_object,
                          d_x=10, d_y=10,
                          n_x=2, n_y=2,
                          use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `v_x`, `v_y`, and `v_z` are the vectors between the base points of the elements in the respective directions.

-    `d_x`, `d_y`, and `d_z` are the distances between the base points of the elements in the respective directions.

-    `n_x`, `n_y`, and `n_z` are the numbers of elements in the respective directions.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

-    `array`is returned with the created array object.

Пример:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

array = Draft.make_ortho_array2d(rect, v_x, v_y, 3, 4)
doc.recompute()
```

### Non-parametric array 

To create a non-parametric orthogonal array use the `array` method of the Draft module. This method returns `None`.


```python
array(objectslist, xvector, yvector, xnum, ynum)
array(objectslist, xvector, yvector, zvector, xnum, ynum, znum)
```

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

Draft.array(rect, v_x, v_y, 3, 4)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/ru
