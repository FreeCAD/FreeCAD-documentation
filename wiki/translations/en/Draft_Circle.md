---
- GuiCommand:
   Name:Draft Circle
   MenuLocation:Drafting → Circle
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**C** **I**
   Version:0.7
   SeeAlso:[Draft Arc](Draft_Arc.md), [Draft Arc 3Points](Draft_Arc_3Points.md)
---

# Draft Circle/en

## Description

The <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> **Draft Circle** command creates a circle in the current [working plane](Draft_SelectPlane.md) from a center and a radius. The radius can be defined by picking a point.

A Draft Circle can be turned into an arc by setting its **First Angle** and **Last Angle** properties to different values.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;"> 
*Circle defined by two points, center and radius*

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Circle.svg" width=16px> [Draft Circle](Draft_Circle.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Circle.svg" width=16px> Circle** option from the menu.
    -   Use the keyboard shortcut: **C** then **I**.
2.  The **Circle** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point, the center of the circle, in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick the second point in the [3D view](3D_view.md), or enter a **Radius**.

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter the coordinates for the center enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   The **Relative** checkbox, displayed in FreeCAD version 0.19 and earlier, has no purpose for this command.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created circle will have **Make Face** set to `True` and will have a filled face.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating circles.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   A Draft Circle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the circle. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **First Angle|Angle**: specifies the start angle of the circle, normally {{value|0&#176;}}.

-    **Last Angle|Angle**: specifies the end angle of the circle, normally {{value|0&#176;}}.

-    **Make Face|Bool**: specifies if the circle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if the **First Angle** and **Last Angle** have the same value. Note that {{value|0&#176;}} and {{value|360&#176;}} are not considered the same.

-    **Radius|Length**: specifies the radius of the circle.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the circle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting

See also: _.

To create a Draft Circle use the `make_circle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeCircle` method.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```

-   Creates a `circle` object with given `radius` in millimeters.
    -   
        `radius`
        
        can also be a `Part.Edge`, whose `Curve` attribute must be a `Part.Circle`.
-   If `placement` is `None` the circle is created at the origin.
-   If `face` is `True`, the circle will make a face, that is, it will appear filled.
-   If `startangle` and `endangle` are given in degrees, and have different values, they are used and the object appears as a [Draft Arc](Draft_Arc.md).

Example: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/en
