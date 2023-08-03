---
 GuiCommand:
   Name: Draft Scale
   MenuLocation: Modification , Scale
   Workbenches: Draft_Workbench, Arch_Workbench
   Shortcut: **S** **C**
   SeeAlso: Draft_SubelementHighlight, Draft_Clone
---

# Draft Scale/en

## Description

The <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> **Draft Scale** command scales or copies selected objects around a base point. In subelement mode the command scales selected points and edges of [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md).

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Scale_example.png  style="width:400px;"> 
*Scaling an object around a base point*

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  Optionally select one or more objects, or one or more subelements of [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Scale.svg" width=16px> [Draft Scale](Draft_Scale.md)** button.
    -   Select the **Modification → <img src="images/Draft_Scale.svg" width=16px> Scale** option from the menu.
    -   Use the keyboard shortcut: **S** then **C**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).
4.  The **Scale** task panel opens. See [Options](#Options.md) for more information.
5.  If subelements have been selected: check the **Modify subelements** checkbox to switch on subelement mode.
6.  Pick the base point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
7.  Enter the X, Y and Z scale factors.
8.  Press **Enter** or the **OK** button to finish the command.

## Options

### First task panel 

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   To manually enter the coordinates for the base point enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press the **Close** button to abort the command.

### Second task panel 

-   Enter the X, Y and Z factors to define the scaling. The values must be larger than zero.
-   Check the **Uniform scaling** checkbox to lock the X, Y and Z factors to the same value.
-   If the **Working plane orientation** checkbox is checked the scale factors are relative to the [working plane](Draft_SelectPlane.md) coordinate system, else they are relative to the global coordinate system.
-   If the **Copy** checkbox is checked a scaled copy of the original object is created. This only works for Draft objects that have a **Points** property, such as [Draft Wires](Draft_Wire.md).
-   If the **Modify subelements** checkbox is checked the command will use the selected subelements instead of the whole objects. The subelements must belong to [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md).
-   If the **Create a clone** checkbox is checked scaled [clones](Draft_Clone.md) of the original objects are created. This works for all object types. For objects that are not Draft objects, or for Draft objects that do not have a **Points** property, this option **must** be selected.
-   Press the **Pick from/to points** button and pick two additional points in the [3D view](3D_view.md) to calculate the scale factors. This will automatically check the **Uniform scaling** checkbox. The X, Y and Z scale factors will therefore be equal and will be set to the distance between the base point and the \'from\' point, divided by the distance between the base point and the \'to\' point.
-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   The command can also scale [Image Planes](Image_CreateImagePlane.md), but not in clone mode.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of scale factors (<small>(v0.20)</small> ) and coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To scale objects use the `scale` method of the Draft module.


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```

-    `objectslist`contains the objects to be scaled. It is either a single object or a list of objects.

-    `scale`is the vector that specifies by the X, Y and Z scale factors.

-    `center`is the center point of the scaling operation.

-   If `copy` is `True` copies are created instead of scaling the original objects.

-    `scaled_list`is returned with the original scaled objects, or with the new copies. It is either a single object or a list of objects, depending on `objectslist`.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/en
