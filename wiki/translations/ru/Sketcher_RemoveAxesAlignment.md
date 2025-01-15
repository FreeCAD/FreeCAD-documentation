---
 GuiCommand:
   Name/ru: Удалить выравнивание осей
   Name: Sketcher_RemoveAxesAlignment
   MenuLocation: Эскиз , Инструменты для эскиза , Удалить выравнивание осей
   Workbenches: Sketcher_Workbench/ru
   Version: 0.20
---

# Sketcher RemoveAxesAlignment/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Данный инструмент удаляет выравнивание осей <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [горизонтальное](Sketcher_ConstrainHorizontal/ru.md) и <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [вертикальное](Sketcher_ConstrainVertical/ru.md) из выбранного элемента, при этом пытается по возможности сохранить ограничения перпендикулярности и эквивалентности ребер.


</div>

## Usage

1.  Select two or more edges with Horizontal or Vertical constraints, for example a [rectangle](Sketcher_CreateRectangle.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md)** button.
    -   Select the **Sketch → Sketcher tools → <img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> Remove axes alignment** option from the menu.
    -   Use the keyboard shortcut: **Z** then **R**.

## Example

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*A selected rectangle with horizontal and vertical constraints.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*The rectangle after using the tool.*


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/ru
