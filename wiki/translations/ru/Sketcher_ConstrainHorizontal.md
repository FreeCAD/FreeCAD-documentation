---
- GuiCommand:
   Name/ru:Ограничение горизонтальности
   Name:Sketcher_ConstrainHorizontal
   MenuLocation:Sketch - Ограничения эскиза - Ограничение горизонтальности
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:**H**
   SeeAlso:[Ограничение вертикальности](Sketcher_ConstrainVertical/ru.md)
---

# Sketcher ConstrainHorizontal/ru

## Описание

Горизонтальное ограничение заставляет выбранную линию или линии в эскизе быть параллельными горизонтальной оси эскиза.

## Применение

<img alt="" src=images/HorizontalConstraint1.png  style="width:500px;"> 
*Выберите отрезок на эскизе, кликнув по нему.*

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*Линия становится тёмно-зелёной.*


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Примените Horizontal Constraint, кликнув иконку Horizontal Constraint [<img src=images/Constraint_Horizontal.svg style="width:16px"> на панели инструментов Sketcher Constraints или выбрав  пункт меню Constrain horizontally в подменю Sketcher constraints меню Sketcher верстака Sketcher (или меню Part Design верстака Part Design). Выделенная линия ограничится быть параллельной горизонтальной линии эскиза.*


</div>

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Можно выбрать несколько линий*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*и затем, применив к ним ограничение, как описано выше, они будут всегда оставаться параллельными горизонтальной оси эскиза.*

## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/ru
