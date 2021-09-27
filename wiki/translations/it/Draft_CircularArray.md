---
- GuiCommand:/it
   Name:Draft CircularArray
   Name/it:Serie circolare
   MenuLocation:Modifiche → Strumenti serie → Serie circolare
   Workbenches:[Draft](Draft_Workbench/it.md)
   Version:0.19
   SeeAlso:[Serie ortogonale](Draft_OrthoArray/it.md), [Serie polare](Draft_PolarArray/it.md), [Serie su tracciato](Draft_PathArray/it.md), [Serie di link su tracciato](Draft_PathLinkArray/it.md), [Serie su punti](Draft_PointArray/it.md), [Clona](Draft_Clone/it.md)
---

# Draft CircularArray/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_CircularArray.svg  style="width:16px;"> _ con un angolo polare di 360 gradi e creando diverse serie concentriche.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su qualsiasi oggetto che abbia una [Part TopoShape](Part_TopoShape/it.md), che significa forme 2D create con [Draft](Draft_Workbench/it.md), ma anche solidi 3D creati con altri ambienti, ad esempio [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md). Può anche creare [App Link](App_Link/it.md) anziché semplici copie.


</div>

<img alt="" src=images/Draft_CircularArray_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">


*Una serie circolare di un oggetto.*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md).

1.  Optionally select one object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_CircularArray.svg" width=16px> [Draft CircularArray](Draft_CircularArray.md)** button.
    -   Select the **Modification → Array tools → <img src="images/Draft_CircularArray.svg" width=16px> Circular array** option from the menu.
3.  The **Circular array** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an object: select one object.
5.  Enter the required parameters in the task panel.
6.  To finish the command do one of the following:
    -   Pick a point in the [3D view](3D_view.md) for the **Center of rotation**.
    -   Press **Enter**.
    -   Press the **OK** button.

## Opzioni

-   Enter the **Radial distance** to specify the distance between the circular layers, and between the center and the first circular layer.
-   Enter the **Tangential distance** to specify the distance between the elements on the same circular layer. Must be larger than zero.
-   Enter the **Number of circular layers**. The element at the center counts as one layer. Must be at least {{Value|2}}. The maximum that can be entered in the task panel is {{Value|99}}, but higher values are possible by changing the **Number Circles** property of the array.
-   Enter the **Symmetry** value. This number determines how the elements are distributed. A value of {{Value|3}}, for example, results in a pattern with three equal 120° pie segments. Larger values for the **Symmetry** and the **Tangential distance** result in fewer or even no elements on the inner layers.
-   Pick a point in the [3D view](3D_view.md), note that this will also finish the command, or type coordinates for the **Center of rotation**. The rotation axis of the array will pass through this point. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press the **Reset point** button to reset the **Center of rotation** to the origin.
-   If the **Fuse** checkbox is checked overlapping elements in the array are fused. This does not work for Link arrays.
-   If the **Link array** checkbox is checked a Link array instead of a regular array is created. A Link array is more efficient because its elements are [App Link](App_Link.md) objects.
-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   The default rotation axis for the array is the positive Z axis. This can be changed by editing its **Axis** property.
-   A Draft CircularArray can be turned into a [Draft OrthoArray](Draft_OrthoArray.md) or a [Draft PolarArray](Draft_PolarArray.md) by changing its **Array Type** property.
-   A Link array cannot be turned into a regular array or vice versa. The type of array must be decided at creation time.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and distances: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Proprietà

See [Draft OrthoArray](Draft_OrthoArray#Properties.md).

## Script

See also: _.

To create a circular array use the `make_array` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeArray` method. The `make_array` method can create [Draft OrthoArrays](Draft_OrthoArray.md), [Draft PolarArrays](Draft_PolarArray.md) and Draft CircularArrays. For each array type one or more wrappers are available.

The main method:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

The wrapper for circular arrays is:


```python
array = make_circular_array(base_object,
                            r_distance=100, tan_distance=50,
                            number=3, symmetry=1,
                            axis=App.Vector(0, 0, 1), center=App.Vector(0, 0, 0),
                            use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `r_distance`and `tan_distance` are the radial and tangential distances between the elements.

-    `number`is the number of circular layers in the pattern, the original object counts as the first layer.

-    `symmetry`is an integer used in some calculations that affect the way the elements are distributed around the circumferences. Usual values are from 1 to 6. Higher values are not recommended and will make the elements in the inner layers disappear.

-    `axis`and `center` are vectors that describe the direction of the axis of rotation, and a point through which that axis passes.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

-    `array`is returned with the created array object.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)

array = Draft.make_circular_array(tri, 1800, 1200, 4, 1)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CircularArray/it
