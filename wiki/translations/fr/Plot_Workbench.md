

<img alt="Icône de l\'atelier Plot" src=images/Workbench_Plot.svg  style="width:128px;">

## Introduction


{{TOCright}}

FreeCAD is able to perform plots using the [matplotlib](https://matplotlib.org/) [Python](Python.md) library. A module is provided to this end, as an external add-on in version 0.19 and as a core component from version 0.20 on. Older versions of FreeCAD are not covered in this documentation.

The produced plots offer the standard [matplotlib](https://matplotlib.org/) tools to edit and save. On top of that, a <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) is provided as an external add-on offering more complete tools to edit the plot and save it. The add-on can be installed with the [Add-on manager](Std_AddonMgr.md).

## Module

The module can be invoked in a Python console or in a [macro](Macro.md). The first thing you must do is importing the module. In FreeCAD 0.19 you must first install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), and then you can import Plot typing


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

## Outils


</div>

If you decide to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) using the [Add-on manager](Std_AddonMgr.md), you will have the following tools available to manage the plots created with the module:

-   <img alt="" src=images/Plot_Save.svg  style="width:32px;"> [Suavegarde](Plot_Save/fr.md): Enregistrer sous plusieurs formats. Vous pouvez sélectionner la taille de sortie et la résolution.
-   <img alt="" src=images/Plot_Axes.svg  style="width:32px;"> [Axes](Plot_Axes/fr.md): Ajouter, effacer ou editer les **axes Plot**.
-   <img alt="" src=images/Plot_Series.svg  style="width:32px;"> [Séries](Plot_Series/fr.md): Editer les séries titres et style.
-   <img alt="" src=images/Plot_Grid.svg  style="width:32px;"> [Grille](Plot_Grid/fr.md): Afficher/Cacher la grille.
-   <img alt="" src=images/Plot_Legend.svg  style="width:32px;"> [Légende](Plot_Legend/fr.md): Afficher/Cacher les légendes.
-   <img alt="" src=images/Plot_Labels.svg  style="width:32px;"> [Etiquettes](Plot_Labels/fr.md): Éditer les étiquettes.
-   <img alt="" src=images/Plot_Positions.svg  style="width:32px;"> [Positions](Plot_Positions/fr.md): Ensemble des éléments de positions.

## Script

Puisque l\'atelier Plot est une couche sur `matplotlib`, vous êtes libre d\'utiliser toutes les commandes de la librairie matplotlib. Voir [exemples de scripts](Scripting_and_macros/fr.md) pour des exemples.

## Tutoriels

[Tutoriel de base](Plot_Basic_tutorial/fr.md)

[Tutoriel multi Axes](Plot_MultiAxes_tutorial/fr.md)


{{Plot_Tools_navi

}} 

[Category:External\_Workbenches{{\#translation:}}](Category:External_Workbenches.md) [Category:Addons{{\#translation:}}](Category:Addons.md)
