---
 GuiCommand:
   Name/ru: Указать длину
   Name: TechDraw_LengthDimension
   MenuLocation: TechDraw , Размеры , Указать длину
   Workbenches: TechDraw_Workbench/ru
   SeeAlso: TechDraw_HorizontalDimension/ru, TechDraw_VerticalDimension/ru
---

# TechDraw LengthDimension/ru



## Описание

The **TechDraw LengthDimension** tool adds a linear dimension to a View. The dimension may be the distance between two points, the length of a straight edge, the perpendicular distance between two edges, or the perpendicular distance between a point and an edge.

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width:220px;">


<div class="mw-translate-fuzzy">



*Расстояние указанное между двумя произвольными точками фигуры.*


</div>



## Применение

1.  Select the points and/or edges which define your measurement. The geometry may be selected in the [3D view](3D_view.md) (first two options) or in the drawing (all options):
    -   Select two points.
    -   Select a single straight edge.
    -   Select two edges. If both edges are straight they must be parallel. This will produce a perpendicular dimension if an endpoint of one of the edges has a perpendicular projection on the other edge (the resultant point must lie on the actual edge). If multiple solutions are possible, the endpoint that is closest to its projected point is used. If there is no valid perpendicular projection, the dimension will be the distance between the nearest endpoints of the edges.
    -   Select a point and an edge. This will produce a perpendicular dimension if the point has a perpendicular projection on the actual edge. Else the dimension will be the distance between the point and the nearest endpoint of the edge.
2.  If you have selected geometry in the 3D view: add the correct TechDraw View to the selection by selecting it in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_LengthDimension.svg" width=16px> [Insert Length Dimension](TechDraw_LengthDimension.md)** button.
    -   Select the **TechDraw → Dimensions → <img src="images/TechDraw_LengthDimension.svg" width=16px> Insert Length Dimension** option from the menu.
4.  A dimension is added to the View.
5.  The dimension may be dragged to the desired position.
6.  If needed, add tolerances as described on [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

### Display 3D measurement 

The dimension will initially display the projected measurement (i.e. as shown in the drawing). If required, and if the dimension is based on 3D references, it can be changed to the actual 3D measurement by changing its **Measure Type** property to {{Value|True}}. To base a dimension on 3D references select geometry from the [3D view](3D_view.md) at creation time, or use the <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;"> [TechDraw DimensionRepair](TechDraw_DimensionRepair.md) tool to update existing dimensions.

### Change properties 

To change the properties of a dimension object either double-click it in the drawing or in the [Tree view](Tree_view.md). This will open the [Dimension dialog](#Dimension_dialog.md).



## Диалоговое окно указания размера 


<div class="mw-translate-fuzzy">

![](images/TechDraw_DimensionDialog_ru.png )


</div>

Диалоговое окно указания размера содержит в себе следующие параметры:



### Точность

-   **Номинальный размер**: Если пункт установлен, это указывает, что размер является теоретически точным. Как таковой, он не должен иметь никаких допусков и его значение будет отображаться в прямоугольной рамке: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-   **Предельные отклонения симметричны**: Если пункт установлен, это означает, что верхнее и нижнее предельные отклонения равны. Выглядет такое значение будет как: <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">, в противном же случае: <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-   **Верхнее предельное отклонение**: Величина соответствующая разности между наибольшим предельным и номинальным размером.

-   **Нижнее предельное отклонение**: Величина соответствующая разности между наименьшим предельным и номинальным размером.



### Форматирование

-   **Format Specifier**: How the dimension value will be formatted. By default the specifier is {{Value|%.xf}} where {{Value|x}} is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string). There is also an additional {{Value|%w}} format that prints the specified number of digits after the decimal separator and removes trailing zeros. For example, {{Value|%.2w}} means that at most 2 decimals will be printed and any trailing zeros will be cut off.

-   **Arbitrary Text**: If checked, the dimension is replaced by the content of the **Format Specifier** field.

-   **OverTolerance Format Specifier**: How the overtolerance value will be formatted. By default the specifier is {{Value|%.xf}} where {{Value|x}} is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **UnderTolerance Format Specifier**: How the undertolerance value will be formatted. By default the specifier is {{Value|%.xf}} where {{Value|x}} is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Arbitrary Tolerance Text**: If checked, the tolerances are replaced by the content of the **OverTolerance Format Specifier** **UnderTolerance Format Specifier** fields.



### Стиль отображения 

-   **Изменить направление стрелок размера**: Меняет направление стрелок размерной линии на противоположное. По умолчанию стрелки находятся внутри размерной линии/дуги и направлены наружу.

-   **Цвет**: Цвет линий и текста.

-   **Размер шрифта**: Размер высоты символов текста.

-   **Drawing Style**: The standard (and its style) according to which the dimension is drawn. See the property [**Standard And Style**](#View.md) for details.

### Lines

-   **Override Angles**: If checked, the usual angles for the dimension line and extension lines will be overridden by the specified values.

-   **Dimension line angle**: Override value for angle of dimension line with view X axis (in degrees).

-   **Use default**: Set dimension line angle to the usual angle.

-   **Use selection**: Set dimension line angle to match the angle of the selected edge (or 2 vertices) in the view.

-   **Extension line angle**: Override value for angle of extension lines with view X axis (in degrees).

-   **Use default**: Set extension line angle to the usual angle.

-   **Use selection**: Set extension line angle to match the angle of the selected edge (or 2 vertices) in the view.



## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". This means that if you modify the 3D geometry, the faces and edges of the model may be renamed internally. If a dimension is attached to an edge that is then modified, the dimension may break. In general, it is not possible to keep the projected 2D dimensions synchronized with the actual 3D objects.

Therefore, it is recommended that dimensions be added when the 3D model is no longer being modified.

### Workaround

If you want to keep a TechDraw view with dimensions that won\'t break, you need to dimension an object that won\'t change:

-   Create a non-parametric copy of the object that you want to project with [Part SimpleCopy](Part_SimpleCopy.md).
-   Select this copy, then use [TechDraw View](TechDraw_View.md), and add the desired dimensions.
-   If the original 3D model is modified, the modifications won\'t affect the simple copy, nor the dimensions in the TechDraw view.

See [Landmark Dimensions](TechDraw_LandmarkDimension.md) for another approach to circumventing the topological naming issue.



## Примечания

-   **Edge selection**. Edges can be difficult to select. You can adjust the selection area for edges by changing the [Edge Fuzz preference](TechDraw_Preferences#Advanced.md).
-   **Decimal places**. Dimensions use the global decimal places setting by default. This can be changed in the [preferences](TechDraw_Preferences#Dimensions.md) or by changing the FormatSpec property.
-   **Multiple objects**. Views may contain multiple 3D objects as Source. Dimensions may be applied to geometry from any object(s) in the View (ex from Object1.Vertex0 to Object2.Vertex3).



## Свойства

### Data


{{Properties_Title|Base}}

-    **References 2D|LinkSubList**: The 2D drawing View object(s) on which the measurement is based. Used if **Measure Type** is {{Value|Projected}}.

-    **References 3D|LinkSubList**: The 3D object(s) on which the measurement is based. Used if **Measure Type** is {{Value|True}}.

-    **Type|Enumeration**: Length, radius, diameter, etc. Not normally manipulated by the end user.

-    **Measure Type|Enumeration**: How the measurement is performed.

:   

    :   True - based on 3D geometry.
    :   Projected - based on 2D drawing View geometry.

-    **Theoretical Exact|Bool**: Specifies a theoretically exact (or basic) dimension.

:   

    :   
        `False`
        
        \- a common dimension by default, possibly with tolerances.

    :   
        `True`
        
        \- a theoretical value. As such, it shall not bear any tolerances. The dimension will be displayed by a frame around the value: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-    **Equal Tolerance|Bool**: If over- and undertolerance are equal. Then the negated value of the overtolerance is used as undertolerance.

:   

    :   
        `True`
        
        \- the negated value of the **Over Tolerance** is used as **Under Tolerance**. The display will be <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">

    :   
        `False`
        
        \- the **Under Tolerance** is taken into account. The display will be <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">

-    **Over Tolerance|QuantityConstraint**: The amount by which the dimension may be larger.

-    **Under Tolerance|QuantityConstraint**: The amount by which the dimension may be smaller.

-    **Inverted|Bool**: Marks whether the dimension represents a common or an inverted value.

:   

    :   
        `False`
        
        \- the ordinary value is used. For length it is a positive number, for angle the oblique value (0° - 180°).

    :   
        `True`
        
        \- the inverted value is used. For length a negative number, for angle the reflex value (180° - 360°).

-    **X|Distance**: Horizontal position of the dimension text relative to the View.

-    **Y|Distance**: Vertical position of the dimension text relative to the View.

-    **Lock Position|Bool|Hidden**: Locks the position of the dimension text when `True`.

-    **Rotation|Angle|Hidden**: Read only.

-    **Scale Type|Enumeration|Hidden**: Read only.

-    **Scale|FloatConstant|Hidden**: Read only.

-    **Caption|String|Hidden**: Not used.


{{Properties_Title|Format}}

-    **Format Spec|String**: How the dimension value will be formatted. See [Formatting](#Formatting.md).

-    **Format Spec Over Tolerance|String**: Like **Format Spec**, but for overtolerances.

-    **Format Spec Under Tolerance|String**: Like **Format Spec**, but for undertolerances.

-    **Arbitrary|Bool**: Whether the dimension is replaced by the content of the **Format Spec** field.

:   

    :   
        `False`
        
        \- the content of the **Format Spec** is used to format the actual dimensional value.

    :   
        `True`
        
        \- the content of the **Format Spec** will be displayed as text instead of the dimension value.

-    **Arbitrary Tolerances|Bool**: Like **Arbitrary**, but for the tolerance.


{{Properties_Title|Override}}

-    **Angle Override|Bool**: Whether the direction of dimension and extension lines is overridden.

:   

    :   
        `False`
        
        \- the directions are computed as usual.

    :   
        `True`
        
        \- the directions are overridden by LineAngle and ExtensionAngle property values.

-    **Line Angle|Angle**: Angle of dimension line with view X axis (in degrees).

-    **Extension Angle|Angle**: Angle of extension line(s) with view X axis (in degrees).


{{Properties_Title|References}}

-    **Saved Geometry|TopoShapeList|Hidden**: Reference geometry. <small>(v0.21)</small> 

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Not used.

-    **Stack Order|Integer**: Over or underlap relative to other drawing objects. <small>(v0.21)</small> 


{{Properties_Title|Dimension Format}}

-    **Arrowsize|Length**: The size of the dimension arrows. <small>(v0.21)</small> 

-    **Color|Color**: Color for lines and text.

-    **Flip Arrowheads|Bool**: By default the value *inside* the dimension line/arc means the arrows pointing *outwards*. If placed *outside* the dimension line/arc, the arrows point *inwards* the dimension line/arc.

:   

    :   
        `False`
        
        \- Let the direction of arrows to be selected automatically according to the rule above.

    :   
        `True`
        
        \- Override the automatically chosen direction and force the opposite one.

-    **Font|Font**: The name of the font to use for the dimension text.

-    **Fontsize|Length**: Dimension text size.

-    **Gap Factor ASME|Float**: Adjusts the gap between the dimension points and the start of the extension lines. The gap is this value times the line width. <small>(v0.21)</small> 

-    **Gap Factor ISO|Float**: Adjusts the gap between the dimension points and the start of the extension lines. The gap is this value times the line width. <small>(v0.21)</small> 

-    **Line Spacing Factor|Float**: Adjusts the gap between the dimension text and the dimension line. The gap is this value times the line width. <small>(v0.21)</small> 

-    **Line Width|Length**: Dimension line weight.

-    **Rendering Extent|Enumeration**: Rather universal property specifying how much space the dimension drawing may take up:

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

-    **Standard And Style|Enumeration**: Specifies the standard (and its style) according to which the dimension is drawn:

:   

    :   <img alt="Differences between the supported standards" src=images/TechDraw_Dimension_standardization.png  style="width:500px;">
    :   ISO Oriented - drawn according to the standard ISO 129-1, text is rotated to be parallel with the dimension line tangent.
    :   ISO Referencing - drawn in compliance with ISO 129-1, text is always horizontal, above the shortest possible reference line.
    :   ASME Inlined - drawn according to the standard ASME Y14.5M, text is horizontal, inserted in a break within the dimension line or arc.
    :   ASME Referencing - drawn in compliance with ASME Y14.5M, text is horizontal, short reference line is attached to one side\'s vertical center.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Length Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Distance"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LengthDimension/ru
