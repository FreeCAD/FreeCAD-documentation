# Draft Rectangle/sv
---
- GuiCommand:   Name: Draft Rectangle   Name/sv: Draft Rectangle   Workbenches: Draft_Workbench/sv   Draft, Arch_Workbench/sv---


</div>

## Description


<div class="mw-translate-fuzzy">

#### Beskrivning

Detta verktyg ritar en rektangel genom att välja två motsatta punkter.


</div>

The corners of a Draft Rectangle can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide a Draft Rectangle by changing its **Columns** and/or **Rows** property.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

#### Bruk

-   Markera punkter i ett tomt område i 3d vyn, eller på ett existerande objekt.
-   Nedtryckning av **CTRL** kommer att [snäppa](Draft_Snap/sv.md) din punkt till tillgängliga snäpp-punkter.
-   Skriv in siffror för att manuellt mata in en koordinat.
-   Nedtryckning av **SKIFT** medan du väljer den motsatta punkten tillåter dig att begränsa den ortogonalt i relation till det ögonblick som du tryckte på **SKIFT**.
-   Om du trycker på **ESC** så avbryts funktionen.
-   Rektanglar har en \"Texturbild\" egenskap som kan användas för att visa en bild som mappas på rektangeln. Du måste se till att ge rektangeln samma dimensioner som bilden. Om man tar bort innehållet i egenskapen så försvinner bilden från rektangeln. Detta är användbart om du behöver kalkera av en pappersritning som du har skannat in.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, the coordinates of the second point are relative to the first point, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created rectangle will have **Make Face** set to `True` and will have a filled face.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating rectangles.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   A Draft Rectangle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Plane](Part_Plane.md) instead of a Draft Rectangle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Rectangle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the rectangle. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the rectangle.

-    **Columns|Integer**: specifies the number of equal-sized columns in which the rectangle is divided.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the rectangle.

-    **Height|Distance**: specifies the height of the rectangle.

-    **Length|Distance**: specifies the length of the rectangle.

-    **Make Face|Bool**: specifies if the rectangle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Rows|Integer**: specifies the number of equal-sized rows in which the rectangle is divided.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the rectangle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

-    **Texture Image|File**: specifies the path of the image file to be mapped onto the face of the rectangle. Blanking this property will remove the image. The rectangle should have the same proportions as the image to avoid distortions.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Rectangle use the `make_rectangle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeRectangle` method.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```

-   Creates a `rectangle` object with `length` in the X direction and `height` in the Y direction, with units in millimeters.
-   If `placement` is `None` the rectangle is created at the origin and the length will be parallel to the X axis.
-   If `face` is `True`, the rectangle will make a face, that is, it will appear filled.

Example: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/sv
