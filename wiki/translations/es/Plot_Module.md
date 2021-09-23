# <img alt="Plot workbench icon" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Module/es


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

## Herramientas


</div>

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Plot_Save.png  style="width:32px;"> [Guardar gráfico](Plot_Save/es.md): Guarda el gráfico en varios formatos, seleccionando el tamaño y resolución.
-   <img alt="" src=images/Plot_Axes.png  style="width:32px;"> [Ejes](Plot_Axes/es.md): Añade, elimina o edita los ejes.
-   <img alt="" src=images/Plot_Series.png  style="width:32px;"> [Series](Plot_Series/es.md): Edita el estilo de las series y establece su título.
-   <img alt="" src=images/Plot_Grid.png  style="width:32px;"> [Malla](Plot_Grid/es.md): Muestra/oculat la malla.
-   <img alt="" src=images/Plot_Legend.png  style="width:32px;"> [Legenda](Plot_Legend/es.md): Muestra/oculta la leyenda.
-   <img alt="" src=images/Plot_Labels.png  style="width:32px;"> [Títulos](Plot_Labels/es.md): Edita los títulos.
-   <img alt="" src=images/Plot_Positions.png  style="width:32px;"> [Posiciones](Plot_Positions/es.md): Posiciona los diferentes elementos, como títulos o legenda.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scripting 

Siendo el módulo de graficado una adaptación de `matplotlib`, usted puede hacer uso libremente de todas las posibilidades del mismo. Acuda a la sección [ejemplos de scripting](Scripting_examples/es.md) para saber más.


</div>

## Tutorial


<div class="mw-translate-fuzzy">

## Tutorial 

-   [Plot Basic tutorial/es](Plot_Basic_tutorial/es.md)
-   [Plot MultiAxes tutorial/es](Plot_MultiAxes_tutorial/es.md)


</div>


{{Plot_Tools_navi

}} 

[Category:External\_Workbenches](Category:External_Workbenches.md) [Category:Addons](Category:Addons.md)

---
[documentation index](../README.md) > [External_Workbenches](Category:External_Workbenches.md) > Plot Module/es
