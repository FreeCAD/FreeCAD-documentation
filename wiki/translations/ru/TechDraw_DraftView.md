---
- GuiCommand:
   Name/ru:Вставить объект верстака Draft
   Name:TechDraw_DraftView
   MenuLocation:TechDraw - Вставить объект верстака Draft
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md), [Draft](Draft_Workbench/ru.md)
   SeeAlso:[Вставить объект верстака Arch](TechDraw_ArchView/ru.md)
---

# TechDraw DraftView/ru


</div>



## Описание

The **TechDraw DraftView** tool inserts a view of a selected [Part](Part_Workbench.md)-based or Group object into a drawing page. Unlike the standard <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [View](TechDraw_View.md) tool, views created with this tool are handled by the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md), and specially designed for showing 2D objects. See [Notes](#Notes.md).

![](images/TechDraw_DraftView_example.png ) 
*Draft elements like circles and arrays imported into a TechDraw drawing page*



## Применение

1.  Optionally rotate the [3D view](3D_view.md). The camera direction in the [3D view](3D_view.md) determines the initial value of the **Direction** property of the View.
2.  Select one or more objects in the [3D view](3D_view.md) or [Tree view](Tree_view.md). A separate view will created for each object.
3.  If there are multiple drawing pages in the document: optionally add the desired page to the selection by selecting it in the [Tree view](Tree_view.md).
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_DraftView.svg" width=16px> [Insert Draft Workbench Object](TechDraw_DraftView.md)** button.
    -   Select the **TechDraw → Views From Other Workbenches → <img src="images/TechDraw_DraftView.svg" width=16px> Insert Draft Workbench Object** option from the menu.
5.  If there are multiple drawing pages in the document and you have not yet selected a page, the **Page Chooser** dialog box opens: <small>(v0.20)</small> 
    1.  Select the desired page.
    2.  Press the **OK** button.



## Опции

-   Creating a DraftView of a layer will recursively handle all objects found in that layer. The View is updated automatically when the contents of the layer changes
-   There is no hidden line removal. Each face found in the handled object(s) will simply be projected along the Direction vector, no specific action is taken when faces overlap
-   The Draft View also supports all Draft objects that are not Part-based, such as dimensions and texts
-   Color, line width and line pattern can be specified in the properties. Line patterns can be fine-tuned by directly giving a [stroke-dasharray](https://www.w3.org/TR/SVG/painting.html#StrokeProperties) value, such as 3,5
-   Projected faces are filled with the face color




<div class="mw-translate-fuzzy">

### Ограничения


</div>

The DraftView is rendered within the [Draft Workbench](Draft_Workbench.md), therefore TechDraw has limited control over its appearance. You may need to make changes within Draft to get the representation you want.



## Свойства

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Draft view}}

-    **Source|Link**: The Draft object to be displayed.

-    **Line Width|Float**: The width of the lines, independently of the scale.

-    **Font Size|Float**: The size of all texts appearing in this view (texts and dimensions).

-    **Direction|Vector**: The projection direction to use.

-    **Color|Color**: The color of lines.

-    **Line Style|String**: A line style to use for this view. Can be {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dashdot}}, {{Value|Dot}} or an SVG line pattern like {{Value|0.20,0.20}}.

-    **Line Spacing|Float**: The spacing to use between lines of texts for multiline texts.

-    **Override Style|Bool**: If `True`, line color, width and style of this view will override those of the rendered object.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The New Draft tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/ru
