---
- GuiCommand   *
   Name   *TechDraw Annotation
   MenuLocation   *TechDraw → Annotations → Insert Annotation
   Workbenches   *[TechDraw](TechDraw_Workbench.md)
   SeeAlso   *[Draft Text](Draft_Text.md), [Draft ShapeString](Draft_ShapeString.md)
---

# TechDraw Annotation/pl

## Description

The Annotation tool adds a text block to a drawing page.

<img alt="" src=images/AnnotationSample.png  style="width   *250px;"> 
*Annotation in the drawing page*

## Usage

1.  If you have multiple drawing pages in your document, you will need to select the desired page in the tree.
2.  Press the **<img src="images/TechDraw_Annotation.svg" width=24px> [Insert Annotation](TechDraw_Annotation.md)** button
3.  A text block containing *Default Text* will appear on the page. Use the property editor to change the text. Drag the Annotation to the required position.
4.  You may need to press **<img src="images/Std_Refresh.svg" width=16px> [Refresh](Std_Refresh.md)** and/or **<img src="images/TechDraw_RedrawPage.svg" width=16px> [Redraw Page](TechDraw_RedrawPage.md)** to get your text to change.

![](images/UpdateAnnotation.png ) 
*Modifying the annotation through the property editor*


**Note   ***

some characters interfere with the internal representation of the Annotation text. Specifically, these are the double quote `"`, less than `<`, and greater than `>` symbols; these must be replaced by HTML escape characters, `&amp;quot;`, `&amp;lt;`, and `&amp;gt;` respectively. See [Character encodings in HTML](https   *//en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references) for details.

## Properties

The Annotation inherits all applicable basic View properties except **Scale**. Use the **TextSize** property instead.

-    **Text**   * The text to be displayed.

-    **Font**   * The name of the font to use. Annotation will use the best match of installed fonts.

-    **TextColor**   * The color of the text.

-    **TextSize**   * The size of the text in mm.

-    **MaxWidth**   * The maximum width of the Annotation block. -1 indicates no maximum width.

-    **LineSpace**   * Line spacing adjustment (%).

-    **TextStyle**   * \"Normal\", \"Bold\", \"Italic\", \"Bold-Italic\"

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The New Annotation tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```

## Notes





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Annotation/pl
