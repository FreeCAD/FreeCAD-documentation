





{{TOCright}}

## Introduction

The preferences of the [TechDraw Workbench](TechDraw_Workbench.md) are found in the [Preferences Editor](Preferences_Editor.md), **Edit → Preferences → TechDraw**.

All preferences settings with *italic* labels are default values for new drawing objects. They have no effect on existing objects.

## General

<img alt="General preferences" src=images/TechDraw_PreferencesGeneral.png  style="width:350px;">

### Drawing Update 


<small>(v0.19)</small> 

-   **Update With 3D**: Whether or not pages are updated every time the 3D model is changed. This is a global policy setting.
-   **Allow Page Override**: Whether or not a page\'s **[Keep Update](TechDraw_PageDefault#Properties.md)** property can override the global **Update With 3D** parameter. This is a global policy setting.
-   **Keep Page Up To Date**: Keeps drawing pages in sync with changes of the 3D model *in real time*. This can slow down the response time.
-   **Auto-distribute Secondary Views**: Automatically distributes secondary views for [projection groups](TechDraw_ProjectionGroup.md).

### Labels

-   **Label Font**: The name of the font for labels. The font is also used for new [dimensions](TechDraw_Preferences#Dimensions.md), changing it has no effect on existing dimensions.
-   **Label Size**: Default size for labels.

### Conventions

-   **Projection Group Angle**: If [projection groups](TechDraw_ProjectionGroup.md) will use either first- or third-angle projection. See [multiview projection](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews) for an explanation.
-   **Hidden Line Style**: The style to be used for hidden lines.

### Files

-   **Default Template**: Default [template](TechDraw_Templates.md) file for new pages.
-   **Template Directory**: Starting directory for toolbar button **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insert Page using Template](TechDraw_PageTemplate.md)**.
-   **Hatch Pattern File**: Default [SVG](SVG.md) or [bitmap](bitmap.md) file for [hatches](TechDraw_Hatch.md).
-   **Line Group File**: Alternate file for personal [line group](TechDraw_LineGroup.md) definitions.
-   **Welding Directory**: Default directory for toolbar button **<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Add Welding Information to Leader](TechDraw_WeldSymbol.md)**. <small>(v0.19)</small> 
-   **PAT File**: Default PAT pattern definition file for [geometric hatches](TechDraw_GeometricHatch.md).
-   **Pattern Name**: Name of the default PAT pattern.

## Scale

<img alt="Scale preferences" src=images/TechDraw_PreferencesScale.png  style="width:350px;">

### Scale 

-   **Page Scale**: Default scale for new pages.
-   **View Scale Type**: Default scale for new views.
-   **View Custom Scale**: Default scale for views if **View Scale Type** is *Custom*.

### Size Adjustments 

-   **Vertex Scale**: Scale of [vertex](Glossary#V.md) dots. Multiplier of line width.
-   **Center Mark Scale**: Size of center marks. Multiplier of vertex size.
-   **Template Edit Mark**: Size of [template](TechDraw_Templates.md) field click handles in mm (green dots).
-   **Welding Symbol Scale**: Multiplier for size of [welding symbols](TechDraw_WeldSymbol.md). <small>(v0.19)</small> 

## Dimensions

<img alt="Dimensions preferences" src=images/TechDraw_PreferencesDimensions.png  style="width:350px;">

### Dimensions 

-   **Standard and Style**: The standard to be used for dimensional values. The difference between the standards are shown in the image: <img alt="Differences between the supported standards. ([Image source" src=images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png  style="width:500px;">

:   

    :   ISO Oriented - drawn according to the standard ISO 129-1, text is rotated to be parallel with the dimension line tangent.
    :   ISO Referencing - drawn in compliance with ISO 129-1, text is always horizontal, above the shortest possible reference line.
    :   ASME Inlined - drawn according to the standard ASME Y14.5M, text is horizontal, inserted in a break within the dimension line or arc.
    :   ASME Referencing - drawn in compliance with ASME Y14.5M, text is horizontal, short reference line is attached to one side\'s vertical center.

-   **Use Global Decimals**: Use number of decimals from the [general preferences](Preferences_Editor#Units.md).
-   **Show Units**: Appends the unit (mm, in, etc.) to dimension values.
-   **Alternate Decimals**: Number of decimals if **Use Global Decimals** is not used.
-   **Default Format**: Custom format for dimension text. Uses the [printf format specifier](https://en.wikipedia.org/wiki/Printf_format_string).
-   **Font Size**: Font size for dimension text.
-   **Tolerance Text Scale**: Tolerance font size adjustment. Multiplier of dimension **[Font Size](TechDraw_Preferences#Dimensions_2.md)**.
-   **Diameter Symbol**: Character used to indicate diameter dimensions.
-   **Arrow Style**: Arrowhead style for dimensions.
-   **Arrow Size**: Arrowhead size of dimensions.

## Annotation

<img alt="Annotation preferences" src=images/TechDraw_PreferencesAnnotation.png  style="width:350px;">

-   **Section Line Standard**: Standard to be used to draw section lines in [section views](TechDraw_SectionView.md).
-   **Section Line Style**: Style for section lines.
-   **Section Cut Surface**: Style for section cut surface. The options are: <small>(v0.19)</small> 
    -   *Hide*: There is no visible surface.
    -   *Solid Color*: The surface gets the color set for **Section Face**
    -   *SVG Hatch*: The surface is [hatched](TechDraw_Hatch.md).
    -   *PAT Hatch*: The surface is [geometrically hatched](TechDraw_GeometricHatch.md).
-   **Line Width Group**: A [LineGroup](TechDraw_LineGroup.md) to set the default line widths.
-   **Detail View Outline Shape**: Outline shape for [detail views](TechDraw_DetailView.md).
-   **Detail Highlight Style**: Line style of the outline shape for [detail views](TechDraw_DetailView.md). <small>(v0.19)</small> 
-   **Center Line Style**: Default style for [centerlines](TechDraw_FaceCenterLine.md).
-   **Balloon Shape**: Shape of [balloon annotations](TechDraw_Balloon.md).
-   **Balloon Leader End**: Default style for balloon leader line ends.
-   **Balloon Leader Kink Length**: Length of balloon leader line kink.
-   **Balloon Orthogonal Triangle**: If **Balloon Leader End** is *Filled Triangle*, the triangle can only get a vertical or horizontal direction when the balloon is moved.
-   **Leader Line Auto Horizontal**: Forces last [leader line](TechDraw_LeaderLine.md) segment to be horizontal.
-   **Show Center Marks**: Show arc center marks in views.
-   **Print Center Marks**: Show arc centers in printed output.

## Colors

<img alt="Colors preferences" src=images/TechDraw_Preferences_Colors.PNG  style="width:350px;">

Setup of the default colors for new pages:

-   **Normal**: Normal line color.
-   **Preselected**: Preselection color. The color that is used to highlight objects when hovering with the mouse over them.
-   **Selected**: Color for selected objects.
-   **Background**: Background color around pages.
-   **Dimension**: Color of dimension lines and text.
-   **Centerline**: Color for [centerlines](TechDraw_FaceCenterLine.md).
-   **Detail Highlight**: Line color for the outline shape of [detail views](TechDraw_DetailView.md). <small>(v0.19)</small> 
-   **Transparent Faces**: If checked, object faces will be transparent. Otherwise the set color will be used for faces. <small>(v0.19)</small> 
-   **Hidden Line**: Hidden line color. This color will be used for all kinds of [hidden lines](#HLR_Parameters.md).
-   **Section Face**: Color of the [section view](TechDraw_SectionView.md) cut surface. Only used if the setting **Section Cut Surface** is set to *Solid Color*.
-   **Section Line**: Color of the [section view](TechDraw_SectionView.md) cut line.
-   **Hatch**: [Hatch](TechDraw_Hatch.md) image color.
-   **Geometric Hatch**: [Geometric hatch](TechDraw_GeometricHatch.md) pattern color.
-   **Vertex**: Color of the selectable [vertices](Glossary#V.md) in views.
-   **Leaderline**: Color for new [leaderlines](TechDraw_LeaderLine.md).

## HLR

<img alt="HLR preferences" src=images/TechDraw_PreferencesHLR.png  style="width:350px;">

HLR stands for *hidden line removal*.

-   **Use Polygon Approximation**: Uses an approximation to find hidden lines. This is fast, but the result is a collection of short straight lines.
-   **Show Hard Lines**: Shows hard and outline edges (visible lines always shown)
-   **Show Smooth Lines**: Shows smooth lines. A smooth line is a line indicating a change between tangent surfaces, as in the transition from a flat surface to a [fillet](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Show Seam Lines**: Show seam lines. A seam line is a boundary between faces.
-   **Show UV ISO Lines**: Shows ISO lines. ISO stands for *isoparametric*. [Here is a description](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) what isoparametric lines (in fact curves) are.
-   **ISO Count**: The number of ISO lines per face edge.

## Advanced

<img alt="Advanced preferences" src=images/TechDraw_PreferencesAdvanced.png  style="width:350px;">

-   **Detect Faces**: If checked, TechDraw will attempt to build faces using the line segments returned by the hidden line removal algorithm. Faces must be detected in order to use [hatching](TechDraw_Hatching.md), but there can be a performance penalty in complex models.
-   **Show Section Edges**: Highlights the border of the section cut in [section views](TechDraw_SectionView.md).
-   **Debug Section**: Dumps intermediate results during a Section view processing
-   **Debug Detail**: Dumps intermediate results during a Detail view processing
-   **Allow Crazy Edges**: Includes edges with unexpected geometry in results, e.g. zero lengths
-   **Fuse Before Section**: Performs a fuse operation on the input shape(s) before Section view processing
-   **Show Loose 2D Geom**: Includes 2D Objects in projections, e.g. loose sketches
-   **Edge Fuzz**: Size of selection area around edges. The fuzz unit is approximately 0.1 mm, depending on your current zoom.
-   **Mark Fuzz**: Selection area around center marks. The fuzz unit is approximately 0.1 mm, depending on your current zoom.
-   **Line End Cap Shape**: Setting of the line end cap shape. Explanation of the options: <https://doc.qt.io/qt-5/qt.html#PenCapStyle-enum>
-   **Max SVG Hatch Tiles**: The limit of SVG tiles with a size of 64x64 pixels used to hatch a single face. For large scalings one might get an error about to many SVG tiles, then one needs to increase the tile limit.
-   **Max PAT Hatch Segments**: The maximum hatch line segments used when hatching a face with a PAT pattern.

## Hidden Settings 

\'\'\'Note: \'\'\' Since FreeCAD 0.19, all settings are available in the Preferences dialogs. The following only applies for FreeCAD versions older than 0.19:

Some preference settings are only accessible through the [Parameter editor](Std_DlgParameter.md), **Tools → Edit parameters**.

### Preferences/Mod/TechDraw/Decorations

-   **CenterMarkScale**: default scale factor for CenterMarks
-   **ShowCenterMarks**: default `True`/`False`
-   **PrintCenterMarks**: `True`/`False` show CenterMarks when printing <small>(v0.19)</small> 

### Preferences/Mod/TechDraw/General

-   **DefaultScale**: initial setting of Page Scale <small>(v0.19)</small> 
-   **EdgeFuzz**: pick radius for Edges
-   **MarkFuzz**: pick radius for CenterMarks
-   **SectionFuseFirst**: fuse Source objects before performing Section cut
-   **EdgeEndCap**: shape of Edge ends 0x00 FlatCap, 0x10 SquareCap, 0x20 RoundCap (Qt::PenCapStyle) <small>(v0.19)</small> 

### Preferences/Mod/TechDraw/Format

-   **SectionFormat**: section line style 0-ASME 1-ISO

### Preferences/Mod/TechDraw/Standards

-   **RadiusAligned**: Radius dimension format 0-ISO(aligned) 1-ASME(uniform)





{{TechDraw Tools navi

}} 

[Category:Preferences{{\#translation:}}](Category:Preferences.md)
