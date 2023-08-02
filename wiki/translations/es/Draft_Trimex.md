---
- GuiCommand:
   Name: Draft Trimex
   Name/es: Draft Trimex
   MenuLocation: Croquis -> Recortar/Extender
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   Shortcut: **T** **R**
   SeeAlso: Part Extrude/es
---

# Draft Trimex/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta recorta/corta y extiende líneas y polilíneas, y extruye caras.


</div>

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Top: a Draft Wire extended and then trimmed.<br>
Bottom: a face extruded into a solid body.*

## Trim or extend 

### Usage


<div class="mw-translate-fuzzy">

1.  Selecciona el contorno que quieres recortar o extender, o selecciona una cara que quieras extruir
2.  Presiona el botón **<img src="images/Draft_Trimex.png" width=16px> [Recortar](Draft_Trimex/es.md)
**, o presiona las teclas **T** y **R**
3.  Designa un punto en la vista 3D


</div>

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold down **Alt** to invert the default result of the command.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )


<div class="mw-translate-fuzzy">

-   Recortar o extender se decide de forma automática en función de la posición del cursor
-   Si mueves el cursor sobre otro objeto, la operación de recortar/extender se ajustará a dicho objeto o segmento
-   Presionando **SHIFT** se realizará una [restricción](Draft_Constrain/es.md) al segmento que está siendo actualmente recortado o extendido.
-   Presionando **ALT** se invertirá la dirección del recorte
-   Cuando el objeto seleccionado es una cara, o cuando se selecciona una cara de un objeto existente, la herramienta de recortar/extender cambia al modo extruir. En modo extruir, presionando **SHIFT** se restringe la extrusión a la normal a la cara.


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

## Programación


</div>


<div class="mw-translate-fuzzy">

No disponible. Mira la herramienta [Extrusión](Part_Extrude/es.md).


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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/es
