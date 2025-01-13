---
 GuiCommand:
   Name: Draft Rotate
   MenuLocation: Modification , Rotate<br>Modify , Rotate
   Workbenches: Draft_Workbench, BIM_Workbench
   Shortcut: **R** **O**
   Version: 0.7
   SeeAlso: Draft_SubelementHighlight
---

# Draft Rotate/en

## Description

The <img alt="" src=images/Draft_Rotate.svg  style="width:24px;"> **Draft Rotate** command rotates or copies selected objects around a center point by a given angle. The axis of rotation is perpendicular to the current [working plane](Draft_SelectPlane.md) and the rotation angle is relative to that plane. In subelement mode the command rotates selected points and edges, or copies selected edges, of [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md).

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [BIM Workbench](BIM_Workbench.md).

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Rotating an object around a center point*

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  Optionally select one or more objects, or one or more subelements of [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Rotate.svg" width=16px> [Rotate](Draft_Rotate.md)** button.
    -   [Draft](Draft_Workbench.md): Select the **Modification → <img src="images/Draft_Rotate.svg" width=16px> Rotate** option from the menu.
    -   [BIM](BIM_Workbench.md): Select the **Modify → <img src="images/Draft_Rotate.svg" width=16px> Rotate** option from the menu.
    -   Use the keyboard shortcut: **R** then **O**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).
4.  The **Rotate** task panel opens. See [Options](#Options.md) for more information.
5.  If subelements have been selected: check the **Modify subelements** checkbox to switch on subelement mode.
6.  Pick the first point, the center of rotation, in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
7.  Pick the second point in the [3D view](3D_view.md), or enter a **Base angle**.
8.  Pick the third point in the [3D view](3D_view.md), or enter a **Rotation**.

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 1.0).

-   To manually enter the coordinates for the center of rotation enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system.
-   Press **N** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing. This mode really only makes sense if copy mode is switched on. Depending on the **Select base objects after copying** preference, either the original objects are selected for the next command call or the copies that were created last. See [Preferences](#Preferences.md).
-   Press **C** or click the **Copy** checkbox to toggle copy mode. If copy mode is on, the command will create rotated copies instead of rotating the original objects.
-   Press **B** or click the **Modify subelements** checkbox to toggle subelement mode. If subelement mode is on, the command will use the selected subelements instead of the whole objects. The subelements must belong to [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md).
-   If copy mode and subelement mode are both on, and edges of [Draft Wires](Draft_Wire.md) are selected, new wires will be created from those edges.
-   Holding down **Alt** after entering the **Base angle** will also toggle copy mode. While **Alt** is held down multiple points can be picked for the **Rotation**. Release **Alt** to finish the command and see the created copies.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be rotated with the Draft Rotate command. To rotate it either its **Support** object has to be rotated, or its **Attachment Offset** has to be changed.
-   The base angle concept can be somewhat confusing. Especially since it works only when selecting points, not when specifying the angle using the input field. An explanation of how it works, with an example, can be found in [this forum thread](https://forum.freecad.org/viewtopic.php?p=736674#p736674).

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General → Select base objects after copying**.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To rotate objects use the `rotate` method of the Draft module.


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```

-    `objectslist`contains the objects to be rotated. It is either a single object or a list of objects.

-    `angle`is the angle of rotation in degrees.

-    `center`is the center point of rotation.

-    `axis`is the direction of the axis of rotation.

-   If `copy` is `True` copies are created instead of rotating the original objects.

-    `rotated_list`is returned with the original rotated objects, or with the new copies. It is either a single object or a list of objects, depending on `objectlist`.

Example:


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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/en
