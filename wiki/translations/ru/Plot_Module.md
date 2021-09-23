# Plot Module/ru


<img alt="Plot workbench icon" src=images/Workbench_Plot.svg  style="width:128px;">


{{TOCright}}

## Introduction

FreeCAD is able to perform plots using the [matplotlib](https://matplotlib.org/) [Python](Python.md) library. A module is provided to this end, as an external add-on in version 0.19 and as a core component from version 0.20 on. Older versions of FreeCAD are not covered in this documentation.

The produced plots offer the standard [matplotlib](https://matplotlib.org/) tools to edit and save. On top of that, a <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) is provided as an external add-on offering more complete tools to edit the plot and save it. The add-on can be installed with the [Add-on manager](Std_AddonMgr.md).

## Module

The module can be invoked in a Python console or in a [macro](Macros.md). The first thing you must do is importing the module. In FreeCAD 0.19 you must first install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), and then you can import Plot by typing:


```python
from freecad.plot import Plot
```

From FreeCAD 0.20 on plot module is already packaged within the program, so you don\'t need to install any add-on, but just type


```python
from FreeCAD.Plot import Plot
```

After that, you can plot a straight line from (0,0) to (1,2) just simply typing


```python
Plot.plot([0, 1], [0, 2])
```

You can find more complex examples in the [Plot Basic tutorial](Plot_Basic_tutorial.md) and the [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial.md).


<div class="mw-translate-fuzzy">

## Инструменты


</div>

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:


<div class="mw-translate-fuzzy">

Доступные инструменты.

-   <img alt="" src=images/Plot_Save.png  style="width:32px;"> [Сохранить диаграмму](Plot_Save/ru.md): Сохраняет диаграмму в нескольких форматах. Вы так же можете выбрать размер и разрешение на выходе.
-   <img alt="" src=images/Plot_Axes.png  style="width:32px;"> [Настройка осей](Plot_Axes/ru.md): Добавить, убрать или редактировать оси диаграммы.
-   <img alt="" src=images/Plot_Series.png  style="width:32px;"> [Настройка числовых рядов](Plot_Series/ru.md): Редактирует последовательности чисел в титлах и их стиль.
-   <img alt="" src=images/Plot_Grid.png  style="width:32px;"> [Показать/скрыть сетку](Plot_Grid/ru.md): Показывает/скрывает сетку.
-   <img alt="" src=images/Plot_Legend.png  style="width:32px;"> [Показать/скрыть легенду](Plot_Legend/ru.md): Показывает/скрывает легенду.
-   <img alt="" src=images/Plot_Labels.png  style="width:32px;"> [Настроить подписи](Plot_Labels/ru.md): Редактирует подписи.
-   <img alt="" src=images/Plot_Positions.png  style="width:32px;"> [Настройка расположения и размеров](Plot_Positions/ru.md): Устанавливает позиции элементов.


</div>

## Scripting

Since the Plot Workbench is a layer on top of `matplotlib`, you are free to use any function from this library on plot instances. See [Scripting and macros](Scripting_and_macros.md) for examples.

## Tutorial


<div class="mw-translate-fuzzy">

## Учебники

-   [Plot Basic tutorial](Plot_Basic_tutorial/ru.md)
-   [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial/ru.md)


</div>


{{Plot_Tools_navi

}} 

[Category:External\_Workbenches](Category:External_Workbenches.md) [Category:Addons](Category:Addons.md)
