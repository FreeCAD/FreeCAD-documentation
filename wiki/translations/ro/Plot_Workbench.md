# <img alt="Plot workbench icon" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Workbench/ro


{{TOCright}}

## Introducere

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

## Instrumente

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:

-   <img alt="" src=images/Plot_Save.png  style="width:32px;"> [Save plot](Plot_Save.md): Salvează desenul/graficul în mai multe formate. Puteți selecta și dimensiunea de ieșire și rezoluția.
-   <img alt="" src=images/Plot_Axes.png  style="width:32px;"> [Axes](Plot_Axes.md): Adăugați, eliminați sau editați axele desenelor/graficelor.
-   <img alt="" src=images/Plot_Series.png  style="width:32px;"> [Series](Plot_Series.md): Editează o serie de titluri și stiluri.
-   <img alt="" src=images/Plot_Grid.png  style="width:32px;"> [Grid](Plot_Grid.md): Afișează/ascunde grila.
-   <img alt="" src=images/Plot_Legend.png  style="width:32px;"> [Legend](Plot_Legend.md): Afișează /ascunde legenda.
-   <img alt="" src=images/Plot_Labels.png  style="width:32px;"> [Labels](Plot_Labels.md): Editează etichetele.
-   <img alt="" src=images/Plot_Positions.png  style="width:32px;"> [Positions](Plot_Positions.md): Setează elementele de poziție.

## Scripting

## Script-Programare 

Deoarece Plot este un strat peste `matplotlib`, aveți libertatea de a folosi orice funcție din această bibliotecă peste instanțele de plotare. A se vedea [Scripting and macros](Scripting_and_macros.md) pentru exemple.

## Tutorial

## Tutorial 

-   [Plot Basic tutorial](Plot_Basic_tutorial.md)
-   [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial.md)


{{Plot_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > Plot Workbench/ro
