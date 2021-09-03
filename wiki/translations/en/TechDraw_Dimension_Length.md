---
- GuiCommand:
   Name:TechDraw  Dimension Length
   MenuLocation:TechDraw → Dimension Length
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw Dimension Horizontal](TechDraw_Dimension_Horizontal.md), [TechDraw Dimension Vertical](TechDraw_Dimension_Vertical.md)
---

## Description

The Dimension Length tool adds a linear dimension to a View. The dimension may be between the distance between two vertices, the length of one edge or the distance between 2 edges. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Link Dimension](TechDraw_Dimension_Link.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width:220px;"> 
*Length dimension taken from two arbitrary nodes of the view*

## Usage

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_Dimension_Length.svg" width=20px> [Dimension Length](TechDraw_Dimension_Length.md)** button.
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the dimension dialog:

## Dimension dialog 

The dimension dialog offers the following settings:

![](images/TechDraw_DimensionDialog.png )

### Tolerancing

-   **Theoretically Exact**: If checked, is specifies the dimension as theoretically exact dimension. As such, it shall not bear any tolerances. The dimension will be displayed by a frame around the value: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-   **Equal Tolerance**: If checked, the over- and undertolerance are equal and the negated value of the overtolerance is used as undertolerance. The display will be <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">, otherwise it will be <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-   **Overtolerance**: The amount by which the dimension may be larger.

-   **Undertolerance**: The amount by which the dimension may be smaller.

### Formatting

-   **Format Specifier**: How the dimension value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Arbitrary Text**: If checked, the dimension is replaced by the content of the **Format Specifier** field.

-   **OverTolerance Format Specifier**: How the overtolerance value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **UnderTolerance Format Specifier**: How the undertolerance value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Arbitrary Tolerance Text**: If checked, the tolerances are replaced by the content of the **OverTolerance Format Specifier** **UnderTolerance Format Specifier** fields.

### Display Style 

-   **Flip Arrowheads**: Flips the direction in which the dimension line arrows are pointing. By default they are inside the dimension line/arc and pointing outwards.

-   **Color**: The color for lines and text.

-   **Font Size**: The dimension text size.

-   **Drawing Style**: The standard (and its style) according to which the dimension is drawn. See the property [**Standard And Style**](#View.md) for details.

## Properties

### Data


{{Properties_Title|Base}}

-    **X**: Horizontal position of the dimension text relative to the View.

-    **Y**: Vertical position of the dimension text relative to the View.

-    **Type**: Length,radius,diameter, etc. Not normally manipulated by the end user.

-    **Measure Type**: How the measurement is performed. Not normally manipulated directly by the end user.

:   

    :   *True* - based on 3D geometry or
    :   *Projected* - based on the drawing

-    **Theoretical Exact**: Specifies a theoretically exact (or basic) dimension.

:   

    :   
        `False`
        
        \- a common dimension by default, possibly with tolerances.

    :   
        `True`
        
        \- a theoretical value. As such, it shall not bear any tolerances. The dimension will be displayed by a frame around the value: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-    **Equal Tolerance**: If over- and undertolerance are equal. Then the negated value of the overtolerance is used as undertolerance.

:   

    :   
        `True`
        
        \- the negated value of the **Over Tolerance** is used as **Under Tolerance**. The display will be <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">

    :   
        `False`
        
        \- the **Under Tolerance** is taken into account. The display will be <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">

-    **Over Tolerance**: The amount by which the dimension may be larger.

-    **Under Tolerance**: The amount by which the dimension may be smaller.

-    **Inverted**: Marks whether the dimension represents a common or an inverted value.

:   

    :   
        `False`
        
        \- the ordinary value is used. For length it is a positive number, for angle the oblique value (0° - 180°).

    :   
        `True`
        
        \- the inverted value is used. For length a negative number, for angle the reflex value (180° - 360°).


{{Properties_Title|Format}}

-    **Format Spec**: How the dimension value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-    **Format Spec Over Tolerance**: Like **Format Spec**, but for overtolerances.

-    **Format Spec Under Tolerance**: Like **Format Spec**, but for undertolerances.

-    **Arbitrary**: Whether the dimension is replaced by the content of the **Format Spec** field.

:   

    :   
        `False`
        
        \- the content of the **Format Spec** is used to format the actual dimensional value.

    :   
        `True`
        
        \- the content of the **Format Spec** will be displayed as text instead if the dimension value.

-    **Arbitrary Tolerances**: Like **Arbitrary**, but for the tolerance.

### View


{{Properties_Title|Base}}

-    **Visibility**: Sets whether the dimension is visible. `True` - visible, `False` - hidden.


{{Properties_Title|Dim Format}}

-    **Font**: The name of the font to use for the dimension text.

-    **Font Size**: Dimension text size.

-    **Line Width**: Dimension line weight.

-    **Color**: Color for lines and text.

-    **Standard And Style**: Specifies the standard (and its style) according to which the dimension is drawn:

<img alt="Differences between the supported standards" src=images/TechDraw_Dimension_standardization.png  style="width:500px;">

:   

    :   ISO Oriented - drawn according to the standard ISO 129-1, text is rotated to be parallel with the dimension line tangent.
    :   ISO Referencing - drawn in compliance with ISO 129-1, text is always horizontal, above the shortest possible reference line.
    :   ASME Inlined - drawn according to the standard ASME Y14.5M, text is horizontal, inserted in a break within the dimension line or arc.
    :   ASME Referencing - drawn in compliance with ASME Y14.5M, text is horizontal, short reference line is attached to one side\'s vertical center.

-    **Rendering Extent**: Rather universal property specifying how much space the dimension drawing may take up:

:   

    :   None - no lines or arrows are drawn, only the bare dimension value is displayed.
    :   Minimal - for lengths and angles a single headed line connecting the dimensional value and the end point\'s *virtual extension line* is drawn. The extension line itself is not added.
    :   Diameters are rendered following Confined extent, radii following Reduced extent.
    :   Confined - for lengths and angles a double headed line (or arc) connecting the start and end point\'s *virtual extension lines* is drawn, though the extension lines themselves are not added.
    :   Diameters are drawn with a minimal single headed line from dimensional value to the closest point on circle, radii as with Reduced extent.
    :   Reduced - for lengths and angles a single headed line connecting the dimensional value and the end point\'s *extension line* is drawn along with the extension line itself.
    :   Diameters are drawn with a single headed line from the center to the closest point on circle, radii with a minimal single headed line from dimensional value to the closest arc point.
    :   Normal - the default value. For lengths and angles a double headed line (or arc) connecting the start and end point\'s *extension lines* is drawn, the extension lines themselves as well.
    :   Diameters are drawn as double headed lines striking the center and connecting the closest and farthest points on the circle.
    :   Radii are drawn as a single headed line from center to the closest arc point.
    :   Expanded - Only diameters support this value, rendering them in a horizontal or vertical length-like way. Other dimension types are rendered as with Normal extent.

-    **Flip Arrowheads**: By default the value *inside* the dimension line/arc means the arrows pointing *outwards*. If placed *outside* the dimension line/arc, the arrows point *inwards* the dimension line/arc.

:   

    :   
        `False`
        
        \- Let the direction of arrows to be selected automatically according to the rule above.

    :   
        `True`
        
        \- Override the automatically chosen direction and force the opposite one.

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](topological_naming_problem.md)\". This means that if you modify the 3D geometry the faces and edges of the model may be renamed internally; if a dimension is attached to an edge that is then modified, the dimension may break. In general, it is not possible to keep the projected 2D dimensions synchronized with the actual 3D objects.

Therefore, it is recommended that dimensions be added when the 3D model is no longer being modified.

### Workaround

If you want to keep a TechDraw view with dimensions that won\'t break, you need to dimension an object that won\'t change.

-   Select the object that you want to project, then switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and use **Part → <img src="images/Part_SimpleCopy.svg" width=16px> [Create simple copy](Part_SimpleCopy.md)**. This will create a single object that is not parametric, that is, no longer editable.
-   Select this copy, then use [TechDraw View](TechDraw_View.md), and add the desired dimensions.
-   If the original 3D model is modified, the modifications won\'t affect the simple copy, nor the dimensions in the TechDraw view.

See [Landmark Dimensions](TechDraw_Dimension_Landmark.md) for another approach to circumventing the topological naming issue.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Length tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Distance"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```

## Notes

-   **Edge selection**. Edges can be difficult to select. You can adjust the selection area for edges using the parameter \"/Mod/TechDraw/General/EdgeFuzz\" (see [Std\_DlgParameter](Std_DlgParameter.md)). This is a dimension-less number. The default is 10.0. Values in the 20-30 range will make it noticeably easier to select edges. Large numbers will cause overlaps with other drawing elements.
-   **Decimal places**. Dimensions use the global decimal places setting by default. This can be changed via [preferences](TechDraw_Preferences#Dimensions.md) or by changing the FormatSpec property.
-   **Multiple objects**. Views may contain multiple 3D objects as Source. Dimensions may be applied to geometry from any object(s) in the View (ex from Object1.Vertex0 to Object2.Vertex3).





{{TechDraw Tools navi

}}  
