---
- GuiCommand:/it
   Name:Draft Trimex
   Name/it:Tronca/Estendi
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Tronca/Estendi
   Shortcut:**T** **R**
   SeeAlso:Parte → [Estrudi](Part_Extrude/it.md)
---

# Draft Trimex/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Tronca/Estendi taglia o estende le [Linee](Draft_Line/it.md) e le [Polilinee](Draft_Wire/it.md) in modo che finiscano in un\'intersezione con un\'altra linea o bordo.


</div>

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Segmento del contorno esteso, poi segmento tagliato; faccia estrusa in un corpo solido*


</div>

## Trim or extend 

### Usage


<div class="mw-translate-fuzzy">

1.  Selezionare una linea che si desidera accorciare o estendere, oppure selezionare una faccia che si desidera estrudere
2.  Premere il pulsante **<img src="images/Draft_Trimex.png" width=16px> Tronca/Estendi
**, o premere i tasti **T** e **R**
3.  Cliccare un punto nella vista 3D, oppure immettere una distanza e premere **Invio**.


</div>

### Options

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   The solution with the largest length determines the default direction of the command. Hold down **Alt** to invert this direction.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )


<div class="mw-translate-fuzzy">

-   Premere il tasto **X**, **Y** o **Z** per vincolare il punto sull\'asse dato.
-   Tenere premuto **Maiusc** per limitare l\'operazione al segmento corrente ed evitare di prenderne un altro.
    -   Nel caso della modalità estrusione, Tenere premuto **Maiusc** per estrudere una faccia in una direzione che non è la normale.
-   Tenere premuto **Alt** durante il taglio per invertire la direzione dell\'operazione, cioè per tagliare l\'altra estremità del contorno.


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

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Non ci sono opzioni per questo strumento. Per l\'estrusione di facce e altre forme consultare lo strumento [Estrudi](Part_Extrude/it.md) del modulo Parte.


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


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/it
