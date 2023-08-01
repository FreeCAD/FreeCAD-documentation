---
- GuiCommand:
   Name:Draft Rectangle   Name/de:Draft Rectangle
   MenuLocation:Entwurf → Rechteck
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**R** **E**
   SeeAlso:[Part Box](Part_Box/de.md)
---

# Draft Rectangle/de


</div>

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Das Rechteckwerkzeug erstellt ein Rechteck, indem es zwei Punkte auswählt. Es wird das [Entwurf Linienstil](Draft_Linestyle/de.md) verwendet, das auf dem [Draft Tray](Draft_Tray/de.md) eingestellt ist.


</div>

Du kannst optional eine 45-Grad-Fase oder eine runde Verrundung zu jeder Ecke des Rechtecks hinzufügen, und du kannst das Rechteck in eine Reihe von gleich großen Reihen und Spalten unterteilen.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Rechteck definiert durch die beiden Eckpunkte*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Rectangle.svg" width=16px> [Draft Rectangle](Draft_Rectangle.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Rectangle.svg" width=16px> Rectangle** option from the menu.
    -   Use the keyboard shortcut: **R** then **E**.
2.  The **Rectangle** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick the second point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button. This point must not be constrained to the X, Y or Z axis.

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

Beispiel: 
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
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/de
