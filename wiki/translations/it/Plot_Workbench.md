# <img alt="L\'icona dell\'ambiente Plot" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Workbench/it


{{TOCright}}

## Introduzione

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

### Strumenti

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:

-   <img alt="" src=images/Plot_Save.svg  style="width:32px;"> [Salva grafico](Plot_Save/it.md): consente di salvare il grafico in diversi formati. È possibile selezionare il formato di output e anche la risoluzione.
-   <img alt="" src=images/Plot_Axes.svg  style="width:32px;"> [Assi](Plot_Axes/it.md): aggiunge, rimuove o modifica gli assi del grafico.
-   <img alt="" src=images/Plot_Series.svg  style="width:32px;"> [Serie](Plot_Series/it.md): modifica il titolo e lo stile della serie.
-   <img alt="" src=images/Plot_Grid.svg  style="width:32px;"> [Griglia](Plot_Grid/it.md): mostra o nasconde la griglia.
-   <img alt="" src=images/Plot_Legend.svg  style="width:32px;"> [Legenda](Plot_Legend/it.md): mostra o nasconde la legenda.
-   <img alt="" src=images/Plot_Labels.svg  style="width:32px;"> [Etichette](Plot_Labels/it.md): edita le etichette.
-   <img alt="" src=images/Plot_Positions.svg  style="width:32px;"> [Posizioni](Plot_Positions/it.md): posiziona i vari elementi, come le etichette o la legenda.

## Scripting

### Script

Poiché il modulo Grafico è costruito su `matplotlib`, si è liberi di utilizzare tutti i comandi matplotlib per le istanze del grafico. Consultare la sezione [Scripting and macros](Scripting_and_macros.md) per vedere degli esempi.

## Tutorial

### Tutorial 

-   [Guida di base per il modulo Grafico](Plot_Basic_tutorial/it.md) di FreeCAD
-   [Guida ai grafici MultiAsse](Plot_MultiAxes_tutorial/it.md)


{{Plot_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > Plot Workbench/it
