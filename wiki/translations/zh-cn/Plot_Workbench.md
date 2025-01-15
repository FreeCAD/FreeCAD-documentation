# <img alt="Plot workbench icon" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Workbench/zh-cn




## Introduction

FreeCAD is able to perform plots using the [matplotlib](https://matplotlib.org/) [Python](Python.md) library. A module is provided to this end, as an external add-on in version 0.19 and as a core component from version 0.20 on. Older versions of FreeCAD are not covered in this documentation.

The produced plots offer the standard [matplotlib](https://matplotlib.org/) tools to edit and save. On top of that, a <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) is provided as an external add-on offering more complete tools to edit the plot and save it. The add-on can be installed with the [Add-on manager](Std_AddonMgr.md).

## Module

The module can be invoked in a Python console or in a [macro](Macros.md). The first thing you must do is importing the module. In FreeCAD 0.19 you must first install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), and then you can import Plot by typing:


```python
from freecad.plot import Plot
```

Since FreeCAD 0.20 the plot module is already packaged with the program, so you don\'t need to install any add-on, but just type:


```python
from FreeCAD.Plot import Plot
```

After that, you can plot a straight line from (0,0) to (1,2) just simply typing:


```python
Plot.plot([0, 1], [0, 2])
```

You can find more complex examples in the [Plot Basic tutorial](Plot_Basic_tutorial.md) and the [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial.md).

## Workbench Tools 

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:

-   <img alt="" src=images/Plot_Save.svg  style="width:32px;"> [Save plot](Plot_Save.md): Saves the plot in several formats. You can select the output size and resolution too.
-   <img alt="" src=images/Plot_Axes.svg  style="width:32px;"> [Axes](Plot_Axes.md): Add, remove or edit plot axes.
-   <img alt="" src=images/Plot_Series.svg  style="width:32px;"> [Series](Plot_Series.md): Edit series title and styling.
-   <img alt="" src=images/Plot_Grid.svg  style="width:32px;"> [Grid](Plot_Grid.md): Show/hide grid.
-   <img alt="" src=images/Plot_Legend.svg  style="width:32px;"> [Legend](Plot_Legend.md): Show/hide legend.
-   <img alt="" src=images/Plot_Labels.svg  style="width:32px;"> [Labels](Plot_Labels.md): Edit labels.
-   <img alt="" src=images/Plot_Positions.svg  style="width:32px;"> [Positions](Plot_Positions.md): Set elements positions.

## Scripting

Since the Plot Workbench is a layer on top of `matplotlib`, you are free to use any function from this library on plot instances. See [Scripting and macros](Scripting_and_macros.md) for examples.

## Tutorial

-   [Plot Basic tutorial](Plot_Basic_tutorial.md)
-   [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial.md)


{{Plot_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Category_Plot.md) > Plot Workbench/zh-cn
