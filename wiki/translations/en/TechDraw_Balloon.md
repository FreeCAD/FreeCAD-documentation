---
- GuiCommand   *
   Name   *TechDraw Balloon
   MenuLocation   *TechDraw → Annotations → Insert Balloon Annotation
   Workbenches   *[TechDraw](TechDraw_Workbench.md)
   Version   *0.19
   SeeAlso   *[TechDraw Annotation](TechDraw_Annotation.md)
---

# TechDraw Balloon/en

## Description

The Balloon tool can add balloons with leader line in a drawing.

<img alt="" src=images/Techdraw_balloon.png  style="width   *600px;">

## Usage

1.  Select one of the following   *
    -   A View (on the page or in the [Tree view](Tree_view.md)).
    -   A vertex in a View. <small>(v0.20)</small> 
    -   An edge in a View. <small>(v0.20)</small> 
    -   A closed region in a View. <small>(v0.20)</small> 
2.  There are several ways to invoke the tool   *
    -   Press the **<img src="images/TechDraw_Balloon.svg" width=16px> [TechDraw Balloon](TechDraw_Balloon.md)** button.
    -   Select the **TechDraw → Annotations → <img src="images/TechDraw_Balloon.svg" width=16px> Insert Balloon Annotation** option from the menu.
3.  If a View or a region was selected   *
    1.  The cursor changes to a balloon icon.
    2.  Click a point on the page for the origin of the Balloon.

To move the bubble of a Balloon, press and hold the left mouse button on its center and drag the mouse.

To change the properties of a Balloon double-click it on the page or in the [Tree view](Tree_view.md). This will open the Balloon task panel.

**Note   *** The position of a Balloon is relative to its Source View and uses the same scale factor.

## Using separators 

When using a rectangle shape, separators can be added using \"\|\" in the text. For example \"AAA\|TEST\|111\" gives   *

<img alt="" src=images/balloon_separator.png  style="width   *300px;">

## Properties

### Data

-    **Text**   * Text to be displayed.

-    **Source View**   * Source View for the balloon.

-    **Origin X**   * Balloon origin x-position relative to the View.

-    **Origin Y**   * Balloon origin y-position relative to the View.

-    **End Type**   * End symbol for the balloon line. Options   * <img alt="" src=images/Arrownone.svg  style="width   *20px;"> None, <img alt="" src=images/Arrowfilled.svg  style="width   *20px;"> Filled Arrow, <img alt="" src=images/Arrowopen.svg  style="width   *20px;"> Open Arrow, <img alt="" src=images/Arrowtick.svg  style="width   *20px;"> Tick, <img alt="" src=images/Arrowdot.svg  style="width   *20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width   *20px;"> Open Circle, <img alt="" src=images/arrowfork.svg  style="width   *20px;"> Fork, <img alt="" src=images/arrowpyramid.svg  style="width   *20px;"> Filled Triangle

-    **End Type Scale**   * Scale factor for the **End Type**.

-    **Bubble Shape**   * Shape of the balloon bubble. Options   * <img alt="" src=images/Circular.svg  style="width   *20px;"> Circular, None, <img alt="" src=images/Triangle.svg  style="width   *20px;"> Triangle, <img alt="" src=images/Inspection.svg  style="width   *20px;"> Inspection, <img alt="" src=images/Hexagon.svg  style="width   *20px;"> Hexagon, <img alt="" src=images/TechDraw_Square.svg  style="width   *20px;"> Square, <img alt="" src=images/Rectangle.svg  style="width   *20px;"> Rectangle

-    **Shape Scale**   * Scale factor for the **Shape**.

-    **Text Wrap**   * Text wrap length; -1 means the text will never be wrapped and the result is in every case a single line.

-    **Kink Length**   * Distance from the **Shape** to the leader line kink.

-    **X**   * Horizontal position of the balloon bubble relative to the View.

-    **Y**   * Vertical position of the balloon bubble relative to the View.

### View

-    **Color**   * Color of the balloon text.

-    **Font**   * The name of the font to use for the balloon bubble.

-    **Fontsize**   * Dimension text size in mm.

-    **Line Visible**   * Whether the balloon line is visible.

-    **Line Width**   * Balloon line width

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Balloon tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
bal1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewBalloon','Balloon')
rc = page.addView(bal1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Balloon/en
