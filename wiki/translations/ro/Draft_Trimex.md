---
- GuiCommand:/ro   Name:Draft Trimex   Name/ro:Draft Trimex   Workbenches:[Arch](Draft_Module/ro___Draft]],_[[Arch_Module/ro.md)|MenuLocation:Draft  → Trim/Extend   Shortcut:T R   SeeAlso:[Part Extrude](Part_Extrude/ro.md)---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument taie/scurtează și/sau extinde linii și polilinii, și extrudează fațete.


</div>

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Top: a Draft Wire extended and then trimmed. Bottom: a face extruded into a solid body.*

## Trim or extend 

### Usage


<div class="mw-translate-fuzzy">

1.  Selectați filamentul/polilinia pe care doriți să-l tăiați sau extindeți sau selectați o fațetă pe care doriți să o extrudați
2.  Apăsați butonul **<img src="images/Draft_Trimex.png" width=16px> [[Draft Trimex]]
** sau apăsați tatele {{KEY | T}} apoi **R**
3.  Faceți clic pe un punct din vizualizarea 3D


</div>

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   The solution with the largest length determines the default direction of the command. Hold down **Alt** to invert this direction.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )


<div class="mw-translate-fuzzy">

-   tăierea sau extinderea este decisă automat din poziția mouse-ului
-   dacă mutați cursorul mouse-ului peste un alt obiect, operația de ajustare / extindere se va apropia de acel obiect sau segment
-   apăsând {{KEY | SHIFT}} va [ constrain](Draft_Constrain.md) pe segmentul în curs de curățare sau extindere
-   apăsând {{KEY | ALT}} va inversa direcția de tăiere
-   Când obiectul selectat este o față sau o față este selectată dintr-un obiect existent, instrumentul trimex trece în modul extruder. În modul extrudat, apăsarea tastei {{KEY | SHIFT}} eliberează extrudarea de pe fața normală și permite fixarea în altă parte.


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

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Nu este disponibil. A se vedea instrumentul [Part Extrude](Part_Extrude.md).


</div>


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





 
