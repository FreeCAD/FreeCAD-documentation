---
- GuiCommand:
   Name:Draft Ellipse
   MenuLocation:Drafting → Ellipse
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**E** **L**
   Version:0.7
---

## 描述


<div class="mw-translate-fuzzy">

椭圆工具会根据用户输入的两个点，在当前的[工作平面内创建一个椭圆](Draft_SelectPlane.md)。该椭圆将恰好适配于这两个矩形角点所定义的矩形盒中。另外，此工具将根据[Draft Tray中的](Draft_Tray.md)[Draft Linestyle设置来绘制椭圆](Draft_Linestyle.md)。


</div>


<div class="mw-translate-fuzzy">

此工具也可用于创建椭圆弧，此时还要指定弧的起始角度与结束角度。而要创建圆与圆弧则可采用[底图圆形工具与](Draft_Circle.md)[底图弧形工具](Draft_Arc.md)。另外，您还可以通过[底图B样条与](Draft_BSpline.md)[底图贝塞尔曲线工具来创建近似的椭圆弧与圆弧](Draft_BezCurve.md)。


</div>

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*通过矩形角点所定义的椭圆*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## 如何使用

1.  按下**<img src="images/Draft_Ellipse.png" width=16px> [[Draft Ellipse]]**按钮，或先按**E**键再按**L**键。
2.  在3D视图中点击第一个点，或输入一个 [坐标并按下](Draft_Coordinates.md)**<img src="images/Draft_AddPoint.svg" width=16px> [add point](Draft_AddPoint.md)**按钮。
3.  在3D视图中点击第二个点，或输入一个[坐标并按下](Draft_Coordinates.md)**<img src="images/Draft_AddPoint.svg" width=16px> [add point](Draft_AddPoint.md)**按钮。


</div>

## 选项

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, the coordinates of the second point are relative to the first point, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created ellipse will have **Make Face** set to `True` and will have a filled face.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating ellipses.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   A Draft Ellipse can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Ellipse](Part_Ellipse.md) instead of a Draft Ellipse.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Ellipse object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the ellipse. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **First Angle|Angle**: specifies the angle of the first point of the ellipse, normally {{value|0&#176;}}.

-    **Last Angle|Angle**: specifies the angle of the last point of the ellipse, normally {{value|0&#176;}}.

-    **Major Radius|Length**: specifies the major radius of the ellipse.

-    **Make Face|Bool**: specifies if the ellipse makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if the shape is a full ellipse.

-    **Minor Radius|Length**: specifies the minor radius of the ellipse.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the ellipse. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Ellipse use the `make_ellipse` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeEllipse` method.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```

-   Creates an `ellipse` object with given major (`majradius`) and minor (`minradius`) radius in millimeters.
    -   The bigger value will be used for the major radius (X axis) if no other placement is given.
-   If `placement` is `None` the ellipse is created at the origin.
-   If `face` is `True`, the ellipse will make a face, that is, it will appear filled.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```





 
