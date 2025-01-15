# <img alt="Icône de l\'atelier Plot" src=images/Workbench_Plot.svg  style="width:64px;"> Plot Workbench/fr




## Introduction

FreeCAD est capable d\'effectuer des tracés en utilisant la bibliothèque [matplotlib](https://matplotlib.org/) de [Python](Python/fr.md). Un module est fourni à cette fin, en tant qu\'extension externe dans la version 0.19 et en tant que composant principal à partir de la version 0.20. Les anciennes versions de FreeCAD ne sont pas couvertes par cette documentation.

Les graphiques produits offrent les outils standard [matplotlib](https://matplotlib.org/) pour l\'édition et la sauvegarde. En plus de cela, un <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [atelier Plot](Plot_Workbench/fr.md) est fourni en tant qu\'extension externe offrant des outils plus complets pour modifier le tracé et le sauvegarder. L\'extension peut être installée avec le [Gestionnaire des extensions](Std_AddonMgr/fr.md).

## Module

Le module peut être lancé dans une console Python ou dans une [macro](Macros/fr.md). La première chose que vous devez faire est d\'importer le module. Dans FreeCAD 0.19 vous devez d\'abord installer l\'<img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [atelier Plot](Plot_Workbench/fr.md) à l\'aide du [Gestionnaire des extensions](Std_AddonMgr/fr.md) et ensuite vous pouvez importer Plot en écrivant :


```python
from freecad.plot import Plot
```

Depuis FreeCAD 0.20, le module de traçage est déjà inclus dans le programme, vous n\'avez donc pas besoin d\'installer de module complémentaire, mais simplement de taper :


```python
from FreeCAD.Plot import Plot
```

Après cela, vous pouvez tracer une ligne droite de (0,0) à (1,2) en tapant tout simplement :


```python
Plot.plot([0, 1], [0, 2])
```

Vous pouvez trouver des exemples plus complexes dans le [Tutoriel de base](Plot_Basic_tutorial/fr.md) et le [Tutoriel graphique à plusieurs axes](Plot_MultiAxes_tutorial/fr.md).

## Outils de l\'atelier 

Si vous décidez d\'installer le module <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [atelier Plot](Plot_Workbench/fr.md) en utilisant le [Gestionnaire des extensions](Std_AddonMgr/fr.md), vous disposerez des outils suivants pour gérer les tracés créés avec le module :

-   <img alt="" src=images/Plot_Save.svg  style="width:32px;"> [Sauvegarde](Plot_Save/fr.md) : Enregistrer sous plusieurs formats. Vous pouvez sélectionner la taille de sortie et la résolution.
-   <img alt="" src=images/Plot_Axes.svg  style="width:32px;"> [Axes](Plot_Axes/fr.md) : Ajouter, effacer ou éditer les axes du graphique.
-   <img alt="" src=images/Plot_Series.svg  style="width:32px;"> [Séries](Plot_Series/fr.md) : Editer les séries titres et style.
-   <img alt="" src=images/Plot_Grid.svg  style="width:32px;"> [Grille](Plot_Grid/fr.md) : Afficher/Cacher la grille.
-   <img alt="" src=images/Plot_Legend.svg  style="width:32px;"> [Légende](Plot_Legend/fr.md) : Afficher/Cacher les légendes.
-   <img alt="" src=images/Plot_Labels.svg  style="width:32px;"> [Etiquettes](Plot_Labels/fr.md) : Éditer les étiquettes.
-   <img alt="" src=images/Plot_Positions.svg  style="width:32px;"> [Positions](Plot_Positions/fr.md) : Ensemble des éléments de positions.

## Script

Puisque l\'atelier Plot est une couche sur `matplotlib`, vous êtes libre d\'utiliser toutes les commandes de la librairie matplotlib. Voir [exemples de scripts](Scripting_and_macros/fr.md) pour des exemples.

## Tutoriels

-   [Plot Tutoriel de base](Plot_Basic_tutorial/fr.md)
-   [Plot Tutoriel graphique à plusieurs axes](Plot_MultiAxes_tutorial/fr.md).


{{Plot_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Category_Plot.md) > Plot Workbench/fr
