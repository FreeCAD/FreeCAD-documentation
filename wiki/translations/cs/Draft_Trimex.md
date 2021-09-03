---
- GuiCommand:/cs   Name:Draft Trimex   Name/cs:Kreslení Zakrácení/Prodloužení   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení → Zakrácení/Prodloužení   Shortcut:T R   SeeAlso:[DílVysunutí](Part_Extrude/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj zakracuje a prodlužuje přímky a lomené čáry a vysunuje plochy.


</div>

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Top: a Draft Wire extended and then trimmed. Bottom: a face extruded into a solid body.*

## Trim or extend 

### Usage


<div class="mw-translate-fuzzy">

1.  Vyberte drát, který chcete zakrátit nebo prodloužit nebo vyberte plochu, kterou chcete vysunout
2.  Stiskněte tlačítko **<img src="images/Draft_Trimex.png" width=16px> [Kreslení Zakrácení/Prodloužení](Draft_Trimex/cs.md)
** nebo stiskněte klávesy **T** a potom **R**
3.  Klikněte na bod ve 3D pohledu


</div>

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   The solution with the largest length determines the default direction of the command. Hold down **Alt** to invert this direction.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )


<div class="mw-translate-fuzzy">

-   zakracování nebo prodlužování je řízeno automaticky podle pozice myši
-   když posunete kurzor přes další objekt, operace zakrátit/prodloužit zachytí tento objekt nebo segment
-   stisknutí klávesy **SHIFT** vytvoří [vazbu](Draft_Constrain.md) k segmentu, který je aktuálně zakracován nebo prodlužován
-   stisknutí klávesy **ALT** změní směr zakracování
-   pokud je vybraným objektem plocha nebo je vybrána plocha z existujícího objektu, nástroj Trimex se přepne do vysunovacího módu. Stisknutí klávesy **SHIFT** ve vysunovacím módu uvolní vysunutí z kolmice plochy a umožní zachycení k čemukoliv.


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

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Není dostupné. Podívejte se na nástroj [Díl vysunutí](Part_Extrude/cs.md).


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





 
