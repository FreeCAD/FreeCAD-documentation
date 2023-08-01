---
- GuiCommand:
   Name: Draft Trimex
   MenuLocation: Modification - Trimex
   Workbenches: [Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut: **T** **R**
   SeeAlso: [Part Extrude](Part_Extrude.md)
---

# Draft Trimex/en

## Description

The <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> **Draft Trimex** command [trims or extends](#Trim_or_extend.md) a selected object. Intersections with the edge of another object can be used to determine new endpoints. The command can also be used to [extrude](#Extrude.md) a face, in which case it creates a [Part Extrude](Part_Extrude.md) object.

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Top: a Draft Wire extended and then trimmed.<br>
Bottom: a face extruded into a solid body.*

## Trim or extend 

### Usage

1.  Optionally select one object. The object must be a [Draft Line](Draft_Line.md), a [Draft Wire](Draft_Wire.md), a [Draft Arc](Draft_Arc.md) or a [Draft Circle](Draft_Circle.md) (which can only be trimmed). If the selected object is closed it must have its **Make Face** property set to `False`.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Trimex.svg" width=16px> [Draft Trimex](Draft_Trimex.md)** button.
    -   Select the **Modification → <img src="images/Draft_Trimex.svg" width=16px> Trimex** option from the menu.
    -   Use the keyboard shortcut: **T** then **R**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).
4.  The **Trimex** task panel opens. See [Options](#Options.md) for more information.
5.  Move the pointer in the [3D view](3D_view.md) so that the preview matches the desired result. If required use the modifier keys as explained in the [Options](#Options.md).
6.  Do one of the following:
    -   Pick a point in the [3D view](3D_view.md).
    -   Enter a **Distance** or an **Angle**. The distance is a delta distance. This option does not work if modifier keys are used.
    -   Move the pointer over an edge belonging to another object, and click when this edge is highlighted, to trim or extend the selected object using an intersection with the highlighted edge as the new endpoint. When trimming, the projection of the point where the cutting edge is selected onto the object to be trimmed, determines the default result. Note that [Draft Snaps](Draft_Snap.md) can have an undesirable impact here. In some cases it can be useful to turn them off temporarily.

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold down **Alt** to invert the default result of the command.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )

1.  The arc was clicked near the bottom left corner of the wire. This is the default result.

2.  
    **Alt**was held down while the arc was clicked near the bottom left corner of the wire.

3.  
    **Y**was pressed, and while hovering over the left edge **Shift** was held down and then the arc was clicked. Pressing **Y** is only required for edges that are more or less parallel to the Y axis.

## Extrude

### Usage 

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  It can be helpful to first change the [Draft working plane](Draft_SelectPlane.md) so that it is not coplanar with the face you want to extrude.
2.  Optionally select a single face or an object with a single face.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Trimex.svg" width=16px> [Draft Trimex](Draft_Trimex.md)** button.
    -   Select the **Modification → <img src="images/Draft_Trimex.svg" width=16px> Trimex** option from the menu.
    -   Use the keyboard shortcut: **T** then **R**.
4.  If you have not yet selected an object or a face: select an object with a single face in the [3D view](3D_view.md).
5.  The **Trimex** task panel opens. See [Options](#Options_2.md) for more information.
6.  To define the extrusion direction and distance do one of the following:
    -   Pick a point in the [3D view](3D_view.md) that does no lie on the same plane as the face.
    -   Make sure the pointer is on the correct side of the face in the [3D view](3D_view.md) and enter a **Distance**.

### Options 

The modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold **Shift** to extrude in a direction that is not parallel to the normal of the face.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

There is no Python method to trim objects. To extrude objects use the `extrude` method of the Draft module.


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`is the object to be extruded.

-    `vector`is the extrusion direction and distance.

-   If `solid` is `True` a solid is created instead of a shell.

-    `extrusion`is returned with the created object.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(1500, 500)
doc.recompute()

vector = App.Vector(0, 0, 300)
solid = Draft.extrude(rectangle, vector, solid=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/en
