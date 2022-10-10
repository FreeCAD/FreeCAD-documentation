---
- GuiCommand   *
   Name   *TechDraw DraftView
   MenuLocation   *TechDraw → Insert Draft Workbench Object
   Workbenches   *[TechDraw](TechDraw_Workbench.md), [Draft](Draft_Workbench.md)
   SeeAlso   *[TechDraw Arch View](TechDraw_ArchView.md)
---

# TechDraw DraftView/en

## Description

The <img alt="" src=images/TechDraw_DraftView.svg  style="width   *24px;"> [DraftView](TechDraw_DraftView.md) tool inserts a view of a selected [Part](Part_Workbench.md)-based or Group object into a drawing page. Unlike the standard <img alt="" src=images/TechDraw_View.svg  style="width   *24px;"> [View](TechDraw_View.md) tool, views created with this tool are handled by the <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft Workbench](Draft_Workbench.md), and specially designed for showing 2D objects. See [Notes](#Notes.md).

![](images/TechDraw_DraftView_example.png ) 
*Draft elements like circles and arrays imported into a TechDraw drawing page*

## Usage

1.  Select a Draft object in the 3D view or in the tree
2.  If you have multiple drawing pages in your document, you will need to select the desired page in the tree.
3.  Press the **<img src="images/TechDraw_DraftView.svg" width=16px> [Insert Draft Workbench Object](TechDraw_DraftView.md)** button
4.  A view of the draft object will appear on the page.

## Options

-   Creating a DraftView of a layer will recursively handle all objects found in that layer. The View is updated automatically when the contents of the layer changes
-   There is no hidden line removal. Each face found in the handled object(s) will simply be projected along the Direction vector, no specific action is taken when faces overlap
-   The Draft View also supports all Draft objects that are not Part-based, such as dimensions and texts
-   Color, line width and line pattern can be specified in the properties. Line patterns can be fine-tuned by directly giving a [stroke-dasharray](https   *//www.w3.org/TR/SVG/painting.html#StrokeProperties) value, such as 3,5
-   Projected faces are filled with the face color

## Properties

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Draft view}}

-    **Source|Link**   * The Draft object to be displayed.

-    **Line Width|Float**   * The width of the lines, independently of the scale.

-    **Font Size|Float**   * The size of all texts appearing in this view (texts and dimensions).

-    **Direction|Vector**   * The projection direction to use.

-    **Color|Color**   * The color of lines.

-    **Line Style|String**   * A line style to use for this view. Can be {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dashdot}}, {{Value|Dot}} or an SVG line pattern like {{Value|0.20,0.20}}.

-    **Line Spacing|Float**   * The spacing to use between lines of texts for multiline texts.

-    **Override Style|Bool**   * If `True`, line color, width and style of this view will override those of the rendered object.

## Notes

The DraftView is rendered within the [Draft Workbench](Draft_Workbench.md), therefore TechDraw has limited control over its appearance. You may need to make changes within Draft to get the representation you want.

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The New Draft tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/en
