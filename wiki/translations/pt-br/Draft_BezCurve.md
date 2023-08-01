---
- GuiCommand:
   Name: Draft BezCurve
   MenuLocation: Drafting - Bézier tools - Bézier curve
   Workbenches: [Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut: **B** **Z**
   Version: 0.14
   SeeAlso: [Draft CubicBezCurve](Draft_CubicBezCurve.md), [Draft BSpline](Draft_BSpline.md)
---

# Draft BezCurve/pt-br



## Descrição

The <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Draft BezCurve** command creates a [Bézier curve](http://en.wikipedia.org/wiki/Bezier_curve) from several points.

The command creates a single Bézier curve with a **Degree** that is `number_of_points - 1`. It can be transformed into a piecewise Bézier curve by reducing this property.

The Draft BezCurve and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands use **control points** to define the position and curvature of the spline. The [Draft BSpline](Draft_BSpline.md) command, on the other hand, specifies the **exact points** through which the curve will pass.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Bézier curve defined by multiple points*



## Utilização

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_BezCurve.svg" width=16px> [Draft BezCurve](Draft_BezCurve.md)** button.
    -   Select the **Drafting → Bézier tools → <img src="images/Draft_BezCurve.svg" width=16px> Bézier curve** option from the menu.
    -   Use the keyboard shortcut: **B** then **Z**. <small>(v0.20)</small> 
2.  The **Bézier curve** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick additional points in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  Press **Esc** or the **Close** button to finish the command.



## Opções

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, coordinates are relative to the last point, if available, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created curve will have **Make Face** set to `True` and will have a filled face, provided it is closed and does not self-intersect. Note that a self-intersecting curve with a face will not display properly, for such a curve **Make Face** must be set to `False`.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after using **<img src="images/Draft_FinishLine.svg" width=16px> Finish** or **<img src="images/Draft_CloseLine.svg" width=16px> Close**, or after creating a closed curve by snapping to the first point of the curve, allowing you to continue creating curves.
-   Press **/** or the **<img src="images/Draft_UndoLine.svg" width=16px> Undo** button to undo the last point.
-   Press **A** or the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button to finish the command and leave the curve open.
-   Press **O** or the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button to finish the command and close the curve. A closed curve can also be created by snapping to the first point of the curve.
-   Press **W** or the **<img src="images/Draft_Wipe.svg" width=16px> Wipe** button to delete the segments already placed, but keep working from the last point.
-   Press **U** or the **<img src="images/Draft_SelectPlane.svg" width=16px> [Set WP](Draft_SelectPlane.md)** button to adjust the current working plane in the orientation defined by the last and the previous point.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to finish the command.



## Notas

-   A Draft BezCurve can be edited with the [Draft Edit](Draft_Edit.md) command.
-   OpenCascade, and therefore FreeCAD, does not support Bézier curves of degrees larger than 25. This should not be a problem in practice, as most users typically use Bézier curves of degrees 3 to 5.



## Preferências

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.



## Propriedades

See also: [Property editor](Property_editor.md).

A Draft BezCurve object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the curve. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**: specifies if the curve is closed or not. If the curve is initially open this value is `False`, setting it to `True` will draw a segment to close the curve. If the curve is initially closed this value is `True`, setting it to `False` will remove the last segment and make the curve open.

-    **Continuity|IntegerList**: (read-only) specifies the continuity of the curve.

-    **Degree|Integer**: specifies the degree of the curve.

-    **Length|Length**: (read-only) specifies the total length of the curve.

-    **Make Face|Bool**: specifies if the curve makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the curve does not self-intersect.

-    **Points|VectorList**: specifies the control points of the curve in its local coordinate system.



### Vista


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the curve.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the curve, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the curve, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed curve. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Line use the `make_bezcurve` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeBezCurve` method.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Creates a `bezcurve` object with the given list of points, `pointslist`.
    -   Each point in the list is defined by its `FreeCAD.Vector`, with units in millimeters.
    -   Alternatively, the input can be a `Part.Wire`, from which points are extracted.
-   If `closed` is `True`, or if the first and last points are identical, the curve is closed.
-   If `placement` is `None` the curve is created at the origin.
-   If `face` is `True`, and the curve is closed, the curve will make a face, that is, it will appear filled.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/pt-br
