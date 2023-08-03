---
 GuiCommand:
   Name: Draft Rotate
   Name/ro: Draft Rotate
   MenuLocation: Draft , Rotate
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   Shortcut: **R** **O**
---

# Draft Rotate/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument rotește sau copiază obiectele selectate cu un unghi dat în jurul unui punct de pe [work plane](Draft_SelectPlane.md) curent. Dacă nu este selectat niciun obiect, veți fi invitat să selectați unul ..


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Rotating an object around a center point*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Select objects you wish to rotate or copy
2.  Press the **<img src="images/Draft_Rotate.png" width=16px> [[Draft Rotate]]** button, or press **R** then **O** keys
3.  Click a center point on the 3D view, or type a coordinate
4.  Click a second point on the 3D view, or give a reference angle
5.  Click a third point on the 3D view, or give a rotation angle


</div>

## Opţiuni

The single character keyboard shortcuts and the modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Press **X**, **Y** or **Z** after a point to constrain the next point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **ENTER** between each X, Y and Z component.
-   Press **T** or click the checkbox to check/uncheck the **'''Continue'''** button. If continue mode is on, the Rotate tool will restart after you finish or close it, allowing you to rotate or copy the objects another time without pressing the Rotate button again.
-   Pressing **ALT** or **C** or clicking the **'''Copy'''** button will make a copy of the objects, instead of rotating them. If you keep **ALT** pressed after clicking the third point, you will be able to place more copies, until you release the **ALT** key.
-   Press **CTRL** while drawing to force [snapping](Draft_Snap.md) your point to the nearest snap location, independently of the distance.
-   Press **SHIFT** while drawing to [constrain](Draft_Constrain.md) your next point horizontally or vertically in relation to the rotation center.
-   Press **ESC** or the **'''Cancel'''** button to abort the current command.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be rotated with the Draft Rotate command. To rotate it either its **Support** object has to be rotated, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To store and reuse the same copy mode setting across commands: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

The Rotate tool can by used in [macros](macros.md) and from the python console by using the following function:


</div>


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```


<div class="mw-translate-fuzzy">

-   Rotates the given object or the objects contained in the given list with the given angle around the given center if provided, using axis as a rotation axis.
-   If axis is omitted, the rotation will be around the vertical Z axis.
-   If copymode is True, the actual objects are not moved, but copies are created instead.
-   Returns the objects (or their copies is copymode was True).


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/ro
