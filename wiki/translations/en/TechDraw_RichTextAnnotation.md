---
- GuiCommand:
   Name:TechDraw RichTextAnnotation
   MenuLocation:TechDraw → Annotations → Insert Rich Text Annotations
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Templates](TechDraw_Templates.md), [Draft SVG](Draft_SVG.md), [TechDraw Leaderline](TechDraw_LeaderLine.md)
---

## Description

The RichTextBlock tool adds a formatted annotation block to a [Leaderline](TechDraw_LeaderLine.md) or a View.

<img alt="" src=images/TechDraw_RichTextBlock_sample.png  style="width:220px;"> 
*Stand alone RichTextBlock*

## Usage

1.  Press the **<img src="images/TechDraw_RichTextAnnotation.svg" width=16px> [Rich Text Annotation](TechDraw_RichTextAnnotation.md)** button
2.  A Task dialog will open. The dialog allows quick entry of text.
3.  The **Start Rich Text Editor** button will open a full featured editor. Press the Save icon to record your changes.
4.  After the block is created, it can be edited by double clicking the RichTextBlock in the Tree.
5.  To attach the block to a [Leaderline](TechDraw_LeaderLine.md), select the line before starting the RichTextBlock tool.

## Properties

-    **X,Y**: The location of the block. Relative to the end of the line if attached to a [Leaderline](TechDraw_LeaderLine.md), otherwise this is the position on the page.

-    **ShowFrame**: Draws an outline around the block.

-    **MaxWidth**: Limits the horizontal size of the block. A value of -1 is for unlimited width.

-    **AnnoText**: The HTML text of the block.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The RichTextBlock tool can be used in [macros](Macros.md) and from the [Python](Python.md) console. 
```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
blockObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawRichAnno','DrawRichAnno')
FreeCAD.activeDocument().myPage.addView(blockObj)
blockObj.X = 5
blockObj.Y = 5
blockObj.AnnoText = myHTMLText
```

## Notes

-   You can edit your RichTextBlock by double clicking on it in the tree view. Double clicking in the graphics area is not yet supported.





{{TechDraw Tools navi

}}  
