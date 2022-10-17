---
- GuiCommand   */de
   Name   *Draft Trimex   Name/de   *Draft Trimex
   MenuLocation   *Entwurf → Stutzen/Strecken
   Workbenches   *[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut   ***T** **R**
   SeeAlso   *[Part Extrudieren](Part_Extrude/de.md)
---

# Draft Trimex/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Trimex Werkzeug stutzt oder streckt [Entwurf Linien](Draft_Line/de.md) und [Entwurf Draht](Draft_Wire/de.md) so, dass sie an einem Schnittpunkt mit einer anderen Linie oder Kante enden.


</div>

<img alt="" src=images/Draft_trimex_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">



*Drahtsegment gestreckt, dann Drahtsegment gestutzt; Fläche zu einem festen Körper extrudiert*


</div>

## Trim or extend 

### Usage


<div class="mw-translate-fuzzy">

1.  Wähle eine Linie, die Du stutzen oder strecken möchtest, oder wähle eine Fläche, die Du extrudieren möchtest.
2.  Drücke die **<img src="images/Draft_Trimex.svg" width=16px> [Draft Trimex](Draft_Trimex/de.md)** Taste, oder drücke **T** dann **R** Tasten.
3.  Klicke auf einen Punkt in der 3D Ansicht oder gib eine Entfernung ein und drücke **Enter**.


</div>

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold down **Alt** to invert the default result of the command.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )


<div class="mw-translate-fuzzy">

-   Drücke **X**, **Y** oder **Z**, um den Punkt auf der angegebenen Achse zu beschränken.
-   Halte **Shift** gedrückt, um den Vorgang auf das aktuelle Segment zu begrenzen, und vermeide, ein anderes auszuwählen.
    -   Im Falle des Extrusionsmodus halte **Shift** gedrückt, um eine Fläche in eine andere Richtung zu extruieren.
-   Halte **Alt** während des Stutzens gedrückt, um die Richtung des Vorgangs umzukehren, d.h. das andere Ende des Drahtes wird beschnitten.


</div>

## Extrude

### Usage 

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  It can be helpful to first change the [Draft working plane](Draft_SelectPlane.md) so that it is not coplanar with the face you want to extrude.
2.  Optionally select a single face or an object with a single face.
3.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_Trimex.svg" width=16px> [Draft Trimex](Draft_Trimex.md)** button.
    -   Select the **Modification → <img src="images/Draft_Trimex.svg" width=16px> Trimex** option from the menu.
    -   Use the keyboard shortcut   * **T** then **R**.
4.  If you have not yet selected an object or a face   * select an object with a single face in the [3D view](3D_view.md).
5.  The **Trimex** task panel opens. See [Options](#Options_2.md) for more information.
6.  To define the extrusion direction and distance do one of the following   *
    -   Pick a point in the [3D view](3D_view.md) that does no lie on the same plane as the face.
    -   Make sure the pointer is on the correct side of the face in the [3D view](3D_view.md) and enter a **Distance**.

### Options 

The modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold **Shift** to extrude in a direction that is not parallel to the normal of the face.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch   ***

[Draft API](Draft_API/de.md) und [FreeCAD Scripting Grundlagen](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Für das Trimex Werkzeug ist keine Programmierschnittstelle verfügbar. Siehe das [Teilextrusion](Part_Extrude/de.md) Werkzeug für die Extrusion von Flächen und anderen Formen.


</div>


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`is the object to be extruded.

-    `vector`is the extrusion direction and distance.

-   If `solid` is `True` a solid is created instead of a shell.

-    `extrusion`is returned with the created object.

Example   *


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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/de
