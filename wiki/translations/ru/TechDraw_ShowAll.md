---
- GuiCommand:
   Name/ru:Показать/скрыть невидимые края
   Name:TechDraw_ShowAll
   MenuLocation:TechDraw → ShowAll
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Изменить внешний вид линий](TechDraw_DecorateLine/ru.md)
---

# TechDraw ShowAll/ru


</div>



## Описание

The **TechDraw ShowAll** tool is intended to temporarily show, and then hide, invisible lines in a View. Lines can be made invisible with the [TechDraw DecorateLine](TechDraw_DecorateLine.md) tool. Note that \"invisible\" is a cosmetic state, not to be confused with hidden lines which are geometric constructs.



## Применение

1.  Select a View with invisible lines on a Page or in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ShowAll.svg" width=16px> [Show/Hide Invisible Edges](TechDraw_ShowAll.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_ShowAll.svg" width=16px> Show/Hide Invisible Edges** option from the menu.
3.  All invisible lines in the View are either shown or hidden.

## Notes

-   To make invisible lines permanently visible use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The effect of the ShowAll tool can be duplicated in [macros](Macros.md) or the [Python](Python.md) console. 
```python
v = App.ActiveDocument.View
vvo = v.ViewObject
vvo.ShowAllEdges = True
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/ru
