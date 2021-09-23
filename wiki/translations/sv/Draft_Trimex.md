# Draft Trimex/sv
---
- GuiCommand:/sv   Name:Draft Trimex   Name/sv:Draft Trimex   Workbenches:[Arch](Draft_Workbench/sv___Draft]],_[[Arch_Workbench/sv.md)|MenuLocation:Draft -> Trim/Extend   Shortcut:T R   SeeAlso:[Part Extrude](Part_Extrude/sv.md)---


</div>

## Beskrivning


<div class="mw-translate-fuzzy">

Detta verktyg trimmar/klipper och förlänger linjer och polylines.


</div>

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Top: a Draft Wire extended and then trimmed. Bottom: a face extruded into a solid body.*

## Trim or extend 

### Usage

1.  Optionally select one object. The object must be a [Draft Line](Draft_Line.md), a [Draft Wire](Draft_Wire.md), a [Draft Arc](Draft_Arc.md) or a [Draft Circle](Draft_Line.md) (which can only be trimmed). If the selected object is closed it must have its **Make Face** property set to `False`.
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
    -   Move the pointer over an edge belonging to another object, and click when this edge is highlighted, to trim or extend the selected object using an intersection with the highlighted edge as the new endpoint. Note that [Draft Snaps](Draft_Snap.md) can have an undesirable impact here. In some cases it may be required to turn them off temporarily.

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   The solution with the largest length determines the default direction of the command. Hold down **Alt** to invert this direction.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )


<div class="mw-translate-fuzzy">

-   trimning eller förlängning beslutas automatiskt beroende på muspositionen
-   om du flyttar musmarkören över ett annat objekt, så kommer trim/förläng operationen att snäppa till det objektet eller segmentet
-   Nedtryckning av **SKIFT** kommer att [begränsa](Draft_Constrain/sv.md) dig till det segment som för närvarande trimmas eller förlängs
-   Nedtryckning av **ALT** kommer att invertera trimningens ordning
-   fasning och avrundning stöds inte ännu men är planerat


</div>

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


<div class="mw-translate-fuzzy">

## Skript


</div>

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
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/sv
