---
- GuiCommand   */ru
   Name/ru   *Удалить выравнивание осей
   Name   *Sketcher_RemoveAxesAlignment
   MenuLocation   *Эскиз → Инструменты для эскиза → Удалить выравнивание осей
   Workbenches   *[Sketcher](Sketcher_Workbench/ru.md)
   Version   *0.20
---

# Sketcher RemoveAxesAlignment/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Данный инструмент удаляет выравнивание осей <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width   *16px;"> [горизонтальное](Sketcher_ConstrainHorizontal/ru.md) и <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width   *16px;"> [вертикальное](Sketcher_ConstrainVertical/ru.md) из выбранного элемента, при этом пытается по возможности сохранить ограничения перпендикулярности и эквивалентности ребер.


</div>

## Usage

1.  Select geometry with axes alignments, for example a [rectangle](Sketcher_CreateRectangle.md).
2.  Press the <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width   *24px;"> **Remove axes alignment** toolbar button.

As result the (horizontal, vertical constraints) will be removed. In the example of a rectangle, it stays a rectangle but becomes rotatable.

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width   *300px;"> 
*A selected rectangle with horizontal and vertical constraints.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width   *300px;"> 
*The rectangle after the usage of Remove Axes Alignment.*


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/ru
