---
- GuiCommand:/ru
   Name:Sketcher ConstrainHorizontal
   Name/ru:Sketcher ConstrainHorizontal
   MenuLocation:Sketch → Ограничения эскиза → Ограничения горизонтальности
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:**H**
   SeeAlso:[Ограничения вертикальности](Sketcher_ConstrainVertical/ru.md)
---

## Описание

Горизонтальное ограничение заставляет выбранную линию или линии в эскизе быть параллельными горизонтальной оси эскиза.

## Использование


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint1.png  style="width:256px;"> Выберите линию на эскизе, нажав на нее.
<img alt="" src=images/HorizontalConstraint2.png  style="width:256px;"> Линия становится тёмно-зелёной.
<img alt="" src=images/HorizontalConstraint3.png  style="width:256px;"> Примените Horizontal Constraint, кликнув иконку Horizontal Constraint <img alt="" src=images/Constraint_Horizontal.svg  style="width:16px;"> на панели инструментов Sketcher Constraints или выбрав пункт меню Constrain horizontally в подменю Sketcher constraints меню Sketcher верстака Sketcher (или меню Part Design верстака Part Design). Выделенная линия ограничится быть параллельной горизонтальной линии эскиза.
<img alt="" src=images/HorizontalConstraint4.png  style="width:256px;"> Можно выделить несколько линий,
<img alt="" src=images/HorizontalConstraint5.png  style="width:256px;"> и затем, применив к ним ограничение, как описано выше, они ограничатся быть параллельными горизонтальной оси эскиза.


</div>

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*The line turns dark green.*

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Apply the Horizontal Constraint by clicking on the **<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Constraint horizontal](Sketcher_ConstrainHorizontal.md)* in the Sketcher Constraints toolbar or by selecting the Constrain horizontally menu item in the Sketcher constraints sub menu of the Sketcher menu item in the Sketcher work bench (or the Part Design menu item of the Part Design work bench). The selected line is constrained to be parallel to the horizontal axis of the sketch.**

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Multiple lines may be selected*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*and then applying the constraint as described above, they are constrained to be parallel to the sketch horizontal axis.*

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}  
