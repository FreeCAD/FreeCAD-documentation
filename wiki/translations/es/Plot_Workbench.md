# <img alt="Icono de entorno de trabajo Plot" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Workbench/es






## Introducción

FreeCAD puede realizar gráficas utilizando la biblioteca [matplotlib](https://matplotlib.org/) de [Python](Python.md). Se proporciona un módulo para este fin, como complemento externo en la versión 0.19 y como componente central a partir de la versión 0.20. Las versiones anteriores de FreeCAD no están cubiertas en esta documentación.

Los gráficos producidos ofrecen las herramientas estándar de [matplotlib](https://matplotlib.org/) para editar y guardar. Además de eso, se proporciona un entorno de trabajo <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot](Plot_Workbench/es.md) como complemento externo que ofrece herramientas más completas para editar el trazado y guardarlo. El complemento se puede instalar con el [Administrador de complementos](Std_AddonMgr.md).



## Módulo

El módulo se puede invocar en una consola de Python o en una [macro](Macros.md). Lo primero que debes hacer es importar el módulo. En FreeCAD 0.19, primero debe instalar el entorno de trabajo <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot](Plot_Workbench/es.md) usando el [Administrador de complementos](Std_AddonMgr/es.md), y luego puede importar Plot escribiendo:


```python
from freecad.plot import Plot
```

Desde FreeCAD 0.20, el módulo de trazado ya está incluido con el programa, por lo que no necesita instalar ningún complemento, simplemente escriba:


```python
from FreeCAD.Plot import Plot
```

Después de eso, puedes trazar una línea recta desde (0,0) hasta (1,2) simplemente escribiendo:


```python
Plot.plot([0, 1], [0, 2])
```

Puedes encontrar ejemplos más complejos en el [tutorial básico de Plot](Plot_Basic_tutorial/es.md) y el [tutorial multi-ejes de Plot](Plot_MultiAxes_tutorial/es.md).



## Herramientas de entorno de trabajo 

Si decide instalar el <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [entorno de trabajo Plot](Plot_Workbench/es.md) usando el [Administrador de complementos](Std_AddonMgr/es.md), tendrá las siguientes herramientas disponibles para administrar las gráficas creadas con el módulo:

-   <img alt="" src=images/Plot_Save.svg  style="width:32px;"> [Guardar gráfico](Plot_Save/es.md): Guarda el gráfico en varios formatos, seleccionando el tamaño y resolución.
-   <img alt="" src=images/Plot_Axes.svg  style="width:32px;"> [Ejes](Plot_Axes/es.md): Agrega, elimina o edita los ejes.
-   <img alt="" src=images/Plot_Series.svg  style="width:32px;"> [Series](Plot_Series/es.md): Edita el estilo de las series y establece su título.
-   <img alt="" src=images/Plot_Grid.svg  style="width:32px;"> [Malla](Plot_Grid/es.md): Muestra/oculta la malla.
-   <img alt="" src=images/Plot_Legend.svg  style="width:32px;"> [Leyenda](Plot_Legend/es.md): Muestra/oculta la leyenda.
-   <img alt="" src=images/Plot_Labels.svg  style="width:32px;"> [Títulos](Plot_Labels/es.md): Edita los títulos.
-   <img alt="" src=images/Plot_Positions.svg  style="width:32px;"> [Posiciones](Plot_Positions/es.md): Posiciona los diferentes elementos, como títulos o leyenda.



## Programación

Siendo el módulo de graficado una capa encima de `matplotlib`, usted puede hacer uso libremente de todas las posibilidades de esta biblioteca. Acuda a la sección [Programación y macros](Scripting_and_macros/es.md) para saber más.

## Tutorial

-   [Tutorial básico de Plot](Plot_Basic_tutorial/es.md)
-   [Tutorial de multi-ejes de Plot](Plot_MultiAxes_tutorial/es.md)


{{Plot_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > Plot Workbench/es
