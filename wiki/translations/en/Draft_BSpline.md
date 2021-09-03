---
- GuiCommand:
   Name:Draft BSpline
   MenuLocation:Drafting → B-spline
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**B** **S**
   Version:0.7
   SeeAlso:[Draft Wire](Draft_Wire.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md), [Draft BezCurve](Draft_BezCurve.md)
---

## Description

The <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> **Draft BSpline** command creates a [B-spline curve](http://en.wikipedia.org/wiki/B-spline) from several points.

The Draft BSpline command specifies the **exact points** through which the curve will pass. The [Draft BezCurve](Draft_BezCurve.md) and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands, on the other hand, use **control points** to define the position and curvature of the spline.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline defined by multiple points*

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_BSpline.svg" width=16px> [Draft BSpline](Draft_BSpline.md)** button.
    -   Select the {{MenuCommand|Drafting → <img src="images/Draft_BSpline.svg" width=16px> B-spline}} option from the menu.
    -   Use the keyboard shortcut: **B** then **S**.
2.  The {{MenuCommand|B-spline}} task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick additional points in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  Press **Esc** or the **Close** button to finish the command.

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the {{MenuCommand|Relative}} checkbox to toggle relative mode. If relative mode is on, coordinates are relative to the last point, if available, else they are relative to the coordinate system origin.
-   Press **G** or click the {{MenuCommand|Global}} checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the {{MenuCommand|Filled}} checkbox to toggle filled mode. If filled mode is on, the created spline will have **Make Face** set to `True` and will have a filled face, provided it is closed and does not self-intersect. Note that a self-intersecting spline with a face will not display properly, for such a spline **Make Face** must be set to `False`.
-   Press **T** or click the {{MenuCommand|Continue}} checkbox to toggle continue mode. If continue mode is on, the command will restart after using **<img src="images/Draft_FinishLine.svg" width=16px> Finish** or **<img src="images/Draft_CloseLine.svg" width=16px> Close**, or after creating a closed spline by snapping to the first point of the spline, allowing you to continue creating splines.
-   Press the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button to undo the last point. The **Ctrl**+**Z** keyboard shortcut currently does not work.
-   Press **A** or the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button to finish the command and leave the spline open.
-   Press **O** or the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button to finish the command and close the spline. A closed spline can also be created by snapping to the first point of the spline.
-   Press **W** or the **<img src="images/Draft_Wipe.svg" width=16px> Wipe** button to delete the curve segments already placed, but keep working from the last point.
-   Press **U** or the **<img src="images/Draft_SelectPlane.svg" width=16px> [Set WP](Draft_SelectPlane.md)** button to adjust the current working plane in the orientation defined by the last and the previous point.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the {{button|Close}} button to finish the command.

## Notes

-   A Draft BSpline can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft BSpline can be converted to a [Draft Wire](Draft_Wire.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: {{MenuCommand|Edit → Preferences... → General → Units → Units settings → Number of decimals}}.
-   To change the initial value of filled mode: {{MenuCommand|Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible}}. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Properties

See also: [Property editor](Property_editor.md).

A Draft BSpline object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the spline. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**: specifies if the spline is closed or not. If the spline is initially open this value is `False`, setting it to `True` will draw a curve segment to close the spline. If the spline is initially closed this value is `True`, setting it to `False` will remove the last curve segment and make the spline open.

-    **Make Face|Bool**: specifies if the spline makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the spline does not self-intersect.

-    **Parameterization|Float**: affects the shape of the spline.

-    **Points|VectorList**: specifies the points of the spline in its local coordinate system.

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the spline.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the spline, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the spline, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed spline. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft BSpline use the `make_bspline` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeBSpline` method.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Creates a `bspline` object from the given list of points, `pointslist`.
    -   Each point in the list is defined by its `FreeCAD.Vector`, with units in millimeters.
    -   Alternatively, the input can be a `Part.Wire`, from which points are extracted.
-   If `closed` is `True`, or if the first and last points are identical, the spline is closed.
-   If `placement` is `None` the spline is created at the origin.
-   If `face` is `True`, and the spline is closed, the spline will make a face, that is, it will appear filled.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```





 
