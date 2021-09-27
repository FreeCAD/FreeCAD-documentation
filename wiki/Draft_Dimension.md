---
- GuiCommand:
   Name:Draft Dimension
   MenuLocation:Annotation → Dimension
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**D** **I**
   Version:0.8
   SeeAlso:[Draft FlipDimension](Draft_FlipDimension.md)
---

# Draft Dimension

## Description

The <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> **Draft Dimension** command [creates](#Create.md) a [linear dimension](#Usage_linear_dimension.md), a [radial dimension](#Usage_radial_dimension.md) or an [angular dimension](#Usage_angular_dimension.md). The command can also be used to [convert](#Convert.md) [Std MeasureDistance](Std_MeasureDistance.md) objects.

Linear dimensions based on edges and radial dimensions are parametric. This means that they will update if the measured edge is modified. Measured edges can belong to Draft objects but also to solid bodies. Angular dimensions are not parametric.

Draft Dimensions can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) or [TechDraw ArchView](TechDraw_ArchView.md) commands. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own dimension commands. But these create dimensions that are only displayed on the drawing page and not in the [3D view](3D_view.md).

 <img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">  
*Linear dimension defined by three points*

## Create

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

### Usage linear dimension 

1.  Optionally select a straight edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a straight edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a straight edge in the [3D view](3D_view.md) and release the **Alt** key.
    -   Define the measured distance by picking points:
        -   Pick a first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
        -   Pick a second point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  To position the dimension line do one of the following:
    -   For an aligned dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a horizontal dimension:
        -   Move the pointer above or below the edge or points.
        -   Hold down the **Shift** key, move the pointer and pick a point in the [3D view](3D_view.md).
    -   For a vertical dimension:
        -   Move the pointer to the left or right of the edge or points.
        -   Hold down the **Shift** key, move the pointer and pick a point in the [3D view](3D_view.md).

### Usage radial dimension 

1.  Optionally select a circular edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a circular edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a circular edge in the [3D view](3D_view.md) and release the **Alt** key.
5.  To position the dimension line do one of the following:
    -   For a diameter dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a radial dimension:
        -   Hold down the **Shift** key and pick a point in the [3D view](3D_view.md).

### Usage angular dimension 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
2.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
3.  Hold down the **Alt** key, select two straight edges in the [3D view](3D_view.md) and release the **Alt** key.
4.  To position the dimension arc pick a point in the [3D view](3D_view.md).
5.  Depending on the edges and the picked point the displayed angle will be the acute (sharp) or obtuse (blunt) angle between the edges, or the angle of one of the edges with the horizontal. In some cases you may have to first add auxiliary geometry ([Draft Lines](Draft_Line.md) for example) to get a particular angle.

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, coordinates are relative to the last point, if available, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **T** or click the **Continue** checkbox to toggle continue mode. This mode only works for linear dimensions. If continue mode is on, the command will restart after finishing, allowing you to continue creating dimensions. All subsequent dimensions will start from the final point of the previous dimension, and will use the same baseline as the first dimension. Note that edge selection is not possible for subsequent dimensions.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the {{button|Close}} button to finish the command.

## Convert

### Usage

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.

## Notes

-   Linear and radial Draft Dimensions can be edited with the [Draft Edit](Draft_Edit.md) command.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Dimension object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data linear and radial dimension 


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension line passes.

-    **Linked Geometry|LinkSubList**: specifies the object and its subelement(s) the dimension is linked to.

-    **Normal|Vector**: specifies the normal of the plane of the text.

-    **Support|Link|hidden**: specifies the measured object.


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifies the direction of the measurement.

-    **Distance|Length**: (read-only) specifies the value of the measurement.

-    **End|VectorDistance**: specifies the end point of the measurement.

-    **Start|VectorDistance**: specifies the start point of the measurement.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifies if a radial dimension is displayed as a diameter dimension. If it changed the symbol used in **Override** must be updated manually (from {{Value|Ø}} to {{Value|R}} or vice versa). Not used for linear dimensions.

### Data angular dimension 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (read-only) specifies the value of the measurement.

-    **Center|VectorDistance**: specifies the center of the measurement.

-    **First Angle|Angle**: specifies the start angle of the measurement.

-    **Last Angle|Angle**: specifies the end angle of the measurement.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension arc passes.

-    **Linked Geometry|LinkSubList|hidden**: not used.

-    **Normal|Vector|hidden**: specifies the normal of the plane of the dimension.

-    **Support|Link|hidden**: not used.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|2D text}} the text will be displayed in a plane defined by the **Normal** of the measurement. If it is {{value|3D text}} the text will always face the camera. Note that these values are switched compared to [Draft Texts](Draft_Text.md). This is an inherited property.


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbols displayed at the ends of the dimension line or arc.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the ends of the dimension line or arc, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: specifies the additional length added to the dimension line. Not used for angular dimensions.

-    **Ext Lines|Distance**: specifies the maximum length of the extension lines that go from the measured points to the dimension line. Not used for angular dimensions.

-    **Ext Overshoot|Distance**: specifies the additional length of the extension lines beyond the dimension line. Not used for angular dimensions.

-    **Flip Arrows|Bool**: specifies whether to flip the orientation of the symbols at the ends of the dimension line or arc. Only works if the symbols are arrows.

-    **Line Color|Color**: specifies the color of the dimension including the text.

-    **Line Width|Float**: specifies the width of the lines or arc belonging to the dimension.

-    **Show Line|Bool**: specifies whether to display the dimension line. Does not affect the display of extension lines and overshoots. Not used for angular dimensions.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement. Not used for angular dimensions.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.

## Scripting

See also: _.

To create a Draft Dimension use the `make_dimension` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeDimension` method.

 
```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

There are various ways to invoke this method, depending on the arguments passed to it:

 
```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```

-   Creates a linear `dimension` by measuring the distance between points `p1` and `p2`.
-   Creates a linear `dimension` linked to `object`, measuring the distance between its vertices indexed `i1` and `i2`.
-   Creates a circular `dimension` linked to `object`, with `i1` being the index of the curved edge to measure, and `mode` being either `"radius"` or `"diameter"` to specify the type of dimension.
    -   
        `p3`
        
        in the first call, and `p4` in the other two, specify an optional point through which the dimension line should go.

    -   All points are defined by their `FreeCAD.Vector`.

To create an angular dimension use the following method:

 
```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```

-   Creates an angular `dimension` from the given `center` point, the `angles` list with two elements, and the point `p3` through which the arc should go.
    -   If `angle1 > angle2`, the displayed angle is the difference `angle1 - angle2`; otherwise, the explementary angle is displayed, `360 - (angle2 - angle1)`.
    -   The angles should be given in degrees.

The view properties of `dimension` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Example:

 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension
