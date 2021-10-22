# <img alt="Plot workbench icon" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Workbench/pt-br


{{TOCright}}

## Introdução

FreeCAD is able to perform plots using the _ library. A module is provided to this end, as an external add-on in version 0.19 and as a core component from version 0.20 on. Older versions of FreeCAD are not covered in this documentation.

The produced plots offer the standard _ is provided as an external add-on offering more complete tools to edit the plot and save it. The add-on can be installed with the [Add-on manager](Std_AddonMgr.md).

## Module

The module can be invoked in a Python console or in a _ using the [Add-on manager](Std_AddonMgr.md), and then you can import Plot by typing:


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

## Ferramentas

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:

-   <img alt="" src=images/Plot_Save.png  style="width:32px;"> [Salvar gráfico](Plot_Save/pt-br.md): Salva o gráfico em vários formatos. Você pode selecionar o tamanho de saída, assim também como a resolução.
-   <img alt="" src=images/Plot_Axes.png  style="width:32px;"> [Eixos](Plot_Axes/pt-br.md): Adiciona, remove ou edita eixos do gráfico.
-   <img alt="" src=images/Plot_Series.png  style="width:32px;"> [Séries](Plot_Series/pt-br.md): Edita o título e o estilo da série.
-   <img alt="" src=images/Plot_Grid.png  style="width:32px;"> [Grade](Plot_Grid/pt-br.md): Mostra/Oculta a grade.
-   <img alt="" src=images/Plot_Legend.png  style="width:32px;"> [Legenda](Plot_Legend/pt-br.md): Mostra/Oculta a legenda.
-   <img alt="" src=images/Plot_Labels.png  style="width:32px;"> [Rótulos](Plot_Labels/pt-br.md): Edita rótulos.
-   <img alt="" src=images/Plot_Positions.png  style="width:32px;"> [Posições](Plot_Positions/pt-br.md): Coloca as posições dos elementos.

## Scripting

## Scripting 

Como o Plot Workbench é uma camada sobre `matplotlib`, você está livre para usar qualquer função desta biblioteca em instâncias de plotagem. Veja [exemplos de scripting](Scripting_examples/pt-br.md) para exemplos.

## Tutorial

## Tutorial 

-   [Plot Basic tutorial](Plot_Basic_tutorial/pt-br.md)
-   [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial/pt-br.md)


{{Plot_Tools_navi

}} 

_ _

---
[documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > Plot Workbench/pt-br
