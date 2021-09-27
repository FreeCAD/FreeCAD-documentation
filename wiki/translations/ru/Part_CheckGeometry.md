# Part CheckGeometry/ru
---
- GuiCommand:/ru
   Name:Part CheckGeometry‏‎
   Name/ru:Part CheckGeometry‏‎
   MenuLocation:Деталь → Проверка геометрии
   Workbenches:[Part](Part_Workbench/ru.md)
   SeeAlso:---


</div>

## Описание


<div class="mw-translate-fuzzy">

## Введение

Инструмент проверки геометрии позволяет убедиться, что тело не содержит ошибок.


</div>

## Применение

1.  Select a part (beware to select the whole part and not just a face to check for valid solid)
2.  Invoke the tool by either:
    -   Clicking on the **<img src="images/Part_CheckGeometry.svg" width=16px> [CheckGeometry](Part_CheckGeometry.md)** button available in the Part workbench toolbar.
    -   Using the **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Check geometry** entry from the top menu.
3.  The **Settings** task panel opens, unless **Skip settings page** is enabled. See [Options](#Options.md) for more information. Click **Run check**.

Results will be reported in the _.

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 

If ticked, additionally a Boolean OPerations (BOP) check is performed. <small>(v0.19)</small> 

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/ru
