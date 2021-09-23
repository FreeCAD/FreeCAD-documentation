---
- GuiCommand:/ru
   Name/ru:Показать/скрыть невидимые края
   Name:TechDraw_ShowAll
   MenuLocation:TechDraw → ShowAll
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Изменить внешний вид линий](TechDraw_DecorateLine/ru.md)
---

# TechDraw ShowAll/ru

## Описание

The ShowAll tool shows or hide invisible lines in a View. Note that \"invisible\" is a cosmetic state, not to be confused with hidden lines which are geometric constructs.

## Применение

1.  Select a View on a Page or in the tree.
2.  Press the **<img src="images/TechDraw_ShowAll.svg" width=16px> [Show/Hide Invisible Edges](TechDraw_ShowAll.md)** button
3.  The state of the invisible lines in the View will be reversed.

## Свойства

The ShowAll tool has no properties, as it is not a Document Object.

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The effect of the ShowAll tool can be duplicated in [macros](Macros.md) or the [Python](Python.md) console. 
```python
>>> v = App.ActiveDocument.View
>>> vvo = v.ViewObject
>>> vvo.ShowAllEdges = True
>>> App.activeDocument().recompute()
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/ru
