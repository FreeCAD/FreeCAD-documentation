---
- GuiCommand:/ru
   Name/ru:Экспорт листа в SVG
   Name:TechDraw_ExportPageSVG
   MenuLocation:TechDraw → Экспорт листа в SVG
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Шаблоны](TechDraw_Templates/ru.md), [Draft SVG](Draft_SVG/ru.md)
---

# TechDraw ExportPageSVG/ru

## Описание

The ExportPageSVG tool saves the current drawing page as an [SVG](SVG.md) file.

## Применение

1.  Press the **<img src="images/TechDraw_ExportPageSVG.svg" width=16px> [Export Page as SVG](TechDraw_ExportPageSVG.md)** button.
2.  A File Save dialog will open. Select a location and file name.

## Примечания

-   [TechDraw Hatch](TechDraw_Hatch.md) patterns are not exported to [SVG](SVG.md) due to a limitation in Qt4\'s SVG support.
-   Text positions and sizes are not correct in the exported file. Using the \"system\" default font in the drawing improves the size problem considerably.

## Программирование


**См. так же:**

[TechDrawGui API](TechDrawGui_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The SaveSVG tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)
```

Note that the FreeCADGui module must be active to use this function.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageSVG/ru
