---
- GuiCommand:/ru
   Name/ru:Вставить активный вид (3D Вид)
   Name:TechDraw_ActiveView
   MenuLocation:TechDraw → Вставить активный вид (3D Вид)
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Вставить SVG знак](TechDraw_Symbol/ru.md)
---

# TechDraw ActiveView/ru

## Описание

The ActiveView tool inserts a copy of a 3D window into a drawing page.

![](images/TechDraw_ActiveView_example.png ) 
*A simple view from the 3D model that doesn't perform any complex calculation.*

## Применение

1.  Navigate to the correct [3D view](3D_view.md).
2.  If there are multiple drawing pages in the document: optionally select the desired page in the [Tree view](Tree_view.md). This is not optional for {{VersionMinus|0.19}}.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ActiveView.svg" width=16px> [Insert Active View (3D View)](TechDraw_ActiveView.md)** button.
    -   Select the **TechDraw → <img src="images/TechDraw_ActiveView.svg" width=16px> Insert Active View (3D View)** option from the menu.
4.  If there are multiple drawing pages in the document and you have not yet selected a page, the **Page Chooser** dialog box opens: <small>(v0.20)</small> 
    1.  Select the desired page.
    2.  Press the **OK** button.
5.  The **ActiveView to TD View** task panel opens. See [Options](#Options.md) for more information.
6.  Press the **OK** button.

## Options

The following can be specified:

-    **Width**: The width of the generated view.

-    **Height**: The height of the generated view.

-    **Border**: The amount of empty space to be left around the view (but within Width x Height).

-    **Background**: If checked a background with the specified color is added.

-    **Line Width**: The thickness of the lines in the view.

-    **Render Mode**: The available modes are:

    -   
        {{Value|As is}}
        
        : Render primitives as they are.

    -   
        {{Value|Wireframe}}
        
        : Render polygons as wireframe.

    -   
        {{Value|Points}}
        
        : Render only the vertices of the polygons and lines.

    -   
        {{Value|Wireframe overlay}}
        
        : Render a wireframe overlay in addition to the {{Value|As is}} mode.

    -   
        {{Value|Hidden Line}}
        
        : As {{Value|Wireframe}}, but culls lines which would otherwise not be shown due to geometric culling.

    -   
        {{Value|Bounding box}}
        
        : Only show the bounding box of each object.

## Примечания

-   ActiveViews are static once generated, they are never updated with changes to the 3D model.
-   An ActiveView behind the scenes is a [Symbol](TechDraw_Symbol.md). Its **Scale Type** is therefore always initialized as {{Value|Custom}}.
-   This tool is still somewhat **Experimental**.

## Свойства

See [TechDraw Symbol](TechDraw_Symbol.md).

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The ActiveView tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/ru
