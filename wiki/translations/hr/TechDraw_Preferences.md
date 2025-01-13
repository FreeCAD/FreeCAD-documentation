# TechDraw Preferences/hr
## Introduction

The preferences for the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md) can be found in the [Preferences Editor](Preferences_Editor.md). In the menu select **Edit → Preferences...** and then **<img src="images/Workbench_TechDraw.svg" width=16px> TechDraw**. This group is only available if the TechDraw Workbench has been loaded in the current FreeCAD session.

There are seven pages: [General](#General.md), [Scale](#Scale.md), [Dimensions](#Dimensions.md), [Annotation](#Annotation.md), [Colors](#Colors.md), [HLR](#HLR.md) and [Advanced](#Advanced.md).

All preferences with *italic* labels are default values for new drawing objects. They have no effect on existing objects.

This page has been updated for version 1.0.




<div class="mw-translate-fuzzy">

### TechCrtanje 1 


</div>

<img alt="General preferences" src=images/Preferences_TechDraw_Page_General.png  style="width:350px;">

### Drawing Update 

-   **Update With 3D (global policy)**: Whether or not pages are updated every time the 3D model is changed.
-   **Allow Page Override (global policy)**: Whether or not a page\'s **[Keep Updated](TechDraw_PageDefault#Properties.md)** property can override the global **Update With 3D** parameter.
-   **Keep Page Up To Date**: Keeps drawing pages in sync with changes of the 3D model *in real time*. This can slow down the response time.
-   **Auto-distribute Secondary Views**: Automatically distributes secondary views for [projection groups](TechDraw_ProjectionGroup.md).

### Labels

-   **Label Font**: The name of the font for labels. The font is also used for new [dimensions](#Dimensions.md), changing it has no effect on existing dimensions.
-   **Label Size**: Default size for labels.

### Conventions

-   **Projection Group Angle**: If [projection groups](TechDraw_ProjectionGroup.md) will use either first-angle (European) projection or third-angle (American) projection. See [multiview projection](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews) for an explanation.
-   **Section Line Convention**: Standard for section lines that controls the position of arrows and symbol (<small>(v1.0)</small> ). The options are:
    -   *ANSI*
    -   *ISO*

### Files

-   **Default Template**: Default [template](TechDraw_Templates.md) file for new pages.
-   **Template Directory**: Starting directory for toolbar button **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insert Page using Template](TechDraw_PageTemplate.md)**.
-   **Hatch Pattern File**: Default [SVG](SVG.md) or [bitmap](bitmap.md) file for [hatches](TechDraw_Hatch.md).
-   **Line Group File**: Alternate file for personal [line group](TechDraw_LineGroup.md) definitions.
-   **Welding Directory**: Default directory for toolbar button **[<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Add Welding Information to Leader](TechDraw_WeldSymbol.md)**.
-   **PAT File**: Default PAT pattern definition file for [geometric hatches](TechDraw_GeometricHatch.md).
-   **Pattern Name**: Name of the default PAT pattern.
-   **Symbol Directory**: Alternate directory to search for SVG symbol files.

### Grid

-   **Show Grid**: Default Show Grid setting for new pages.
-   **Grid Spacing**: Default distance between grid lines for new pages.

### Selection

-   **Enable Multiselection Mode**: If enabled, clicking without **Ctrl** does not clear the existing selection. <small>(v1.0)</small> 

### View Defaults 

-   **Use 3d Camera Direction**: If checked, the 3d camera direction (or normal of a selected face) will be used as the view direction. If not checked, Views will be created as Front Views. <small>(v1.0)</small> 
-   **Always Show Label**: If checked, view labels will be displayed even when frames are suppressed. <small>(v1.0)</small> 

### Snapping

-   **Snap View Alignment**: If checked, Views will be snapped into alignment when dragged. <small>(v1.0)</small> 
-   **View Snapping Factor**: Tolerance for snapping of Views - if a View is within this fraction of View size of perfect alignment, it will snap into alignment. <small>(v1.0)</small> 

## Scale

<img alt="Scale preferences" src=images/Preferences_TechDraw_Page_Scale.png  style="width:350px;">

### Scale 

-   **Page Scale**: Default scale for new pages.
-   **View Scale Type**: Default scale for new views.
-   **View Custom Scale**: Default scale for views if **View Scale Type** is *Custom*.

### Size Adjustments 

-   **Vertex Scale**: Scale of [vertex](Glossary#V.md) dots. Multiplier of line width.
-   **Center Mark Scale**: Size of center marks. Multiplier of vertex size.
-   **Template Edit Mark**: Size of [template](TechDraw_Templates.md) field click handles in mm (green dots).
-   **Welding Symbol Scale**: Multiplier for size of [welding symbols](TechDraw_WeldSymbol.md).




<div class="mw-translate-fuzzy">

### TechCrtanje 2 


</div>

<img alt="Dimensions preferences" src=images/Preferences_TechDraw_Page_Dimensions.png  style="width:350px;">

### Dimensions

-   **Standard and Style**: The standard to be used for dimensional values. The differences between the standards are shown in the image: <img alt="Differences between the supported standards. ([Image source" src=images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png  style="width:500px;">

:   

    :   ISO Oriented - drawn according to the standard ISO 129-1, text is rotated to be parallel with the dimension line tangent.
    :   ISO Referencing - drawn in compliance with ISO 129-1, text is always horizontal, above the shortest possible reference line.
    :   ASME Inlined - drawn according to the standard ASME Y14.5M, text is horizontal, inserted in a break within the dimension line or arc.
    :   ASME Referencing - drawn in compliance with ASME Y14.5M, text is horizontal, short reference line is attached to one side\'s vertical center.

-   **Use Global Decimals**: Use number of decimals from the [general preferences](Preferences_Editor#Units.md).
-   **Show Units**: Appends the unit (mm, in, etc.) to dimension values.
-   **Alternate Decimals**: Number of decimals if **Use Global Decimals** is not selected and **Dimension Format** not specified.
-   **Dimension Format**: Custom format for dimension text. Uses the [printf format specifier](https://en.wikipedia.org/wiki/Printf_format_string).
-   **Font Size**: Font size for dimension text.
-   **Tolerance Text Scale**: Tolerance font size adjustment. Multiplier of dimension **Font Size**.
-   **Diameter Symbol**: Character used to indicate diameter dimensions.
-   **Arrow Style**: Arrowhead style for dimensions.
-   **Arrow Size**: Arrowhead size of dimensions.
-   **Extension Gap Factor - ISO**: Gap between dimension point and start of extension lines for ISO dimensions. <small>(v0.21)</small> 
-   **Extension Gap Factor - ASME**: Gap between dimension point and start of extension lines for ASME dimensions. <small>(v0.21)</small> 
-   **Line Spacing - ISO**: Spacing between the dimension line and dimension text for ISO dimensions. <small>(v0.21)</small> 

### Tools

-   **Dimensioning tools**: Select the type of dimensioning tools for the toolbar. Whichever you choose, all tools are always available in the menu and through shortcuts. The options are: <small>(v1.0)</small> 
    -   *Single tool*: A [single tool](TechDraw_Dimension.md) for all dimensioning in the toolbar: Distance, Distance X / Y, Angle, Radius. Others in dropdown.
    -   *Separated tools*: Individual tools for each dimensioning tool.
    -   *Both*: You will have both the \'Single tool\' and the separated tools.
-   **Dimension tool diameter/radius mode**: While using the [Dimension](TechDraw_Dimension.md) tool you may choose how to handle circles and arcs: <small>(v1.0)</small> 
    -   *Auto*: The tool will apply radius to arcs and diameter to circles.
    -   *Diameter*: The tool will apply diameter to all.
    -   *Radius*: The tool will apply radius to all.

## Annotation

<img alt="Annotation preferences" src=images/Preferences_TechDraw_Page_Annotation.png  style="width:350px;">

### Annotation 

-   **Section Cut Surface**: Style for section cut surface. The options are:
    -   *Hide*: There is no visible surface.
    -   *Solid Color*: The surface gets the color set for **Section Face**
    -   *SVG Hatch*: The surface is [hatched](TechDraw_Hatch.md).
    -   *PAT Hatch*: The surface is [geometrically hatched](TechDraw_GeometricHatch.md).
-   **Show Section Line in Source View**: If checked, the section annotation will be drawn on the Source view. If unchecked, no section line, arrows or symbol will be shown in the Source view. <small>(v1.0)</small> 
-   **Include Cut Line in Section Annotation**: If checked, the cut line will be drawn on the Source view. If unchecked, only the change marks, arrows and symbols will be displayed. <small>(v1.0)</small> 
-   **Complex Section Line Marks**: Show marks at direction changes on [ComplexSection](TechDraw_ComplexSection.md) lines. <small>(v0.21)</small> 
-   **Detail View Outline Shape**: Outline shape for [detail views](TechDraw_DetailView.md). The options are:
    -   *Circle*
    -   *Square*
-   **Detail View Show Matting**: This checkbox controls whether or not to display the outline around a detail view. <small>(v1.0)</small> 
-   **Detail Source Show Highlight**: This checkbox controls whether or not to display a highlight around the detail area in the detail\'s source view. <small>(v1.0)</small> 
-   **Balloon Shape**: Shape of [balloon annotations](TechDraw_Balloon.md).
-   **Balloon Leader End**: Default style for balloon leader line ends, see [balloon properties](TechDraw_Balloon#Properties.md).
-   **Balloon Leader Kink Length**: Length of balloon leader line kink.
-   **Balloon Orthogonal Triangle**: If **Balloon Leader End** is *Filled Triangle*, the triangle can only get a vertical or horizontal direction when the balloon is moved.
-   **Leader Line Auto Horizontal**: Forces last [leader line](TechDraw_LeaderLine.md) segment to be horizontal.
-   **Broken View Break Type**: Default break type used to indicate [BrokenViews](TechDraw_BrokenView.md): <small>(v1.0)</small> 
    -   *No Break Lines*
    -   *ZigZag Lines*
    -   *Simple Lines*
-   **Show Center Marks**: Show arc center marks in views.
-   **Print Center Marks**: Show arc centers in printed output.

### Lines

-   **Line Standard**: Standard to be used to draw section lines in [section views](TechDraw_SectionView.md).
-   **Line Width Group**: A [LineGroup](TechDraw_LineGroup.md) to set the default line widths.
-   **Hidden Line Style**: Style of hidden lines. <small>(v1.0)</small> 
-   **Section Line Style**: Style for section lines.
-   **Detail Highlight Style**: Line style of the outline shape for [detail views](TechDraw_DetailView.md).
-   **Center Line Style**: Default style for [centerlines](TechDraw_FaceCenterLine.md).
-   **Break Line Style**: Default style for lines used to indicate [BrokenViews](TechDraw_BrokenView.md). <small>(v1.0)</small> 
-   **Line End Cap Shape**: The default (round) should almost always be the right choice. Flat or square caps are useful if you are planning to use a drawing as a 1:1 cutting guide.

## Colors

<img alt="Colors preferences" src=images/Preferences_TechDraw_Page_Colors.png  style="width:350px;">

Setup of the default colors for new pages:

-   **Normal**: Normal line color.
-   **Preselected**: Preselection color. The color that is used to highlight objects when hovering with the mouse over them.
-   **Selected**: Color for selected objects.
-   **Background**: Background color around pages.
-   **Dimension**: Color of dimension lines and text.
-   **Centerline**: Color for [centerlines](TechDraw_FaceCenterLine.md).
-   **Detail Highlight**: Line color for the outline shape of [detail views](TechDraw_DetailView.md).
-   **Grid Color**: Color for all page grids.
-   **Template Underline**: Color for the underline that marks editable texts in templates. <small>(v1.0)</small> 
-   **Hidden Line**: Hidden line color. This color will be used for all kinds of [hidden lines](#HLR_Parameters.md).
-   **Section Face**: Color of the [section view](TechDraw_SectionView.md) cut surface. Only used if the setting **Section Cut Surface** is set to *Solid Color*.
-   **Section Line**: Color of the [section view](TechDraw_SectionView.md) cut line.
-   **Hatch**: [Hatch](TechDraw_Hatch.md) image color.
-   **Geometric Hatch**: [Geometric hatch](TechDraw_GeometricHatch.md) pattern color.
-   **Vertex**: Color of the selectable [vertices](Glossary#V.md) in views.
-   **Leaderline**: Color for new [leaderlines](TechDraw_LeaderLine.md).
-   **Transparent Faces**: If checked, object faces will be transparent. Otherwise the set color will be used for faces.
-   **Light on dark**: If checked text and lines will have a light color. To be used if the **Page Color** is dark. Transparent or light colored faces are recommended with this option. <small>(v0.21)</small> 
-   **Monochrome**: If checked, the set color will be used for all text and lines. <small>(v0.21)</small> 
-   **Page Color**: The background color of the page. <small>(v0.21)</small> 

## HLR

<img alt="HLR preferences" src=images/Preferences_TechDraw_Page_HLR.png  style="width:350px;">

HLR stands for *hidden line removal*.

-   **Use Polygon Approximation**: Uses an approximation to find hidden lines. This is fast, but the result is a collection of short straight lines.
-   **Show Hard Lines**: Shows hard and outline edges (visible lines always shown)
-   **Show Smooth Lines**: Shows smooth lines. A smooth line is a line indicating a change between tangent surfaces, as in the transition from a flat surface to a [fillet](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Show Seam Lines**: Show seam lines. A seam line is a boundary between faces.
-   **Show UV ISO Lines**: Shows ISO lines. ISO stands for *isoparametric*. [Here is a description](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) what isoparametric lines (in fact curves) are.
-   **ISO Count**: The number of ISO lines per face edge.

## Advanced

<img alt="Advanced preferences" src=images/Preferences_TechDraw_Page_Advanced.png  style="width:350px;">

-   **Detect Faces**: If checked, TechDraw will attempt to build faces using the line segments returned by the hidden line removal algorithm. Faces must be detected in order to use [hatching](TechDraw_Hatching.md), but there can be a performance penalty in complex models.
-   **Report Progress**: Issue progress messages while building View geometry. <small>(v0.21)</small> 
-   **Use New Face Finder Algorithm**: If checked, the new face finder algorithm will be used instead of the original one. <small>(v0.21)</small> 
-   **Auto Correct Dimension Refs**: If checked, an attempt is made to update dimension references when the model changes. <small>(v0.21)</small> 
-   **Show Section Edges**: Highlights the border of the section cut in [section views](TechDraw_SectionView.md).
-   **Fuse Before Section**: Performs a fuse operation on the input shape(s) before Section view processing.
-   **Switch Workbench on Click**: If checked, double-clicking on a page in the tree will automatically switch to TechDraw and the page will be made visible. <small>(v1.1)</small> 
-   **Allow Crazy Edges**: Includes edges with unexpected geometry in results, e.g. zero lengths.
-   **Validate Shapes**: If checked, input shapes will be checked for errors before use and invalid shapes will be skipped. It can be slower but may prevent crashes. <small>(v1.1)</small> 
-   **Debug Section**: Dumps intermediate results during a Section view processing.
-   **Debug Bad Shape**: If checked, shapes that failed validation will be saved as B-rep files for later analysis. <small>(v1.1)</small> 
-   **Debug Detail**: Dumps intermediate results during a Detail view processing.
-   **Overlap Edges Scrub Passes**: The number of attempts to remove overlapping edges returned by the Hidden Line Removal algorithm. A value of 0 indicates no scrubbing. Values above 2 are generally not productive. Each attempt adds to the time required to produce the drawing. <small>(v0.21)</small> 
-   **Edge Fuzz**: Size of selection area around edges. The fuzz unit is approximately 0.1 mm, depending on your current zoom. The default is 10. Values in the 20-30 range will make it noticeably easier to select edges. Large numbers will cause overlaps with other drawing elements.
-   **Mark Fuzz**: Selection area around center marks. The fuzz unit is approximately 0.1 mm, depending on your current zoom.
-   **Max SVG Hatch Tiles**: The limit of SVG tiles with a size of 64x64 pixels used to hatch a single face. For large scalings one might get an error about to many SVG tiles, then one needs to increase the tile limit.
-   **Max PAT Hatch Segments**: The maximum hatch line segments used when hatching a face with a PAT pattern.
-   **Balloon Drag**: Modifier key for balloon drag can be changed from the default here to avoid conflicts with OS or navigation style key bindings. <small>(v1.0)</small> 





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/hr
