# Onboarding FEM Devs/fr
{{TOCright}}

## Description

Cette page oriente les nouveaux développeurs sur la façon de configurer leur environnement de développement afin de pouvoir travailler sur l\'atelier FEM.

## Configuration d\'un environnement de développement 

A définir

### Prérequis

-   Netgen

### Recommandé

-   Paraview

### Compilation via la source 

A définir

### Compilation via Docker 

A définir

## Gestion du code source 

Garder FreeCAD à jour est documenté dans la page [Source code management](Source_code_management/fr.md). Avec des conseils utiles `git`.

## Infrastructure du code FEM 

Le code FEM se trouve dans `src/Mod/Fem`.

-    `App/`application en mode console, définit les structures de base et les classes de base pour les objets documentaires, qui sont utilisées par les modules pour construire les leurs.

-    `Gui/`Application en mode interface utilisateur, définit la [vue 3D](3D_view/fr.md), les outils/fonctions utilisés par le banc de travail pour interagir avec l\'interface utilisateur et la vue 3D, définit les classes de base pour les [view providers](Viewprovider/fr.md).

-    `femcommands/`
    

-    `fem.dox`
    

-    `femexamples/`
    

-    `femguiobjects/`
    

-    `femguiutils/`
    

-    `feminout/`
    

-    `femmesh/`
    

-    `femobjects/`
    

-    `femresult/`
    

-    `femsolver/`
    

-    `femtaskpanels/`
    

-    `femtest/`
    

-    `femtools/`
    

-    `femviewprovider/`
    

-    `InitGui.py`
    

-    `Init.py`
    

-    `ObjectsFem.py`
    

-    `TestFemApp.py`
    

-    `TestFemGui.py`
    

### Conventions de codage 

Veuillez consulter le fichier [coding_conventions.md](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Fem/coding_conventions.md) sur le dépôt de FreeCAD.

## Ajout de nouveaux solveurs FEM 

Un nouveau solveur FEM nécessite les éléments suivants :

-   Exportateur de maillage
-   Importateur de résultats
-   Objet solveur (nécessite des changements dans les paramètres du solveur, les tests unitaires, les modules ObjectsFem aussi)
-   Module de tâche et d\'écriture (c\'est ici que l\'écriture principale de l\'entrée du solveur se produit).
-   Outil GUI pour créer un solveur
-   Onglet de préférences de l\'interface graphique pour définir le chemin binaire du solveur.
-   Un test unitaire pour l\'écriture du solveur. Le mieux est de prendre le cantilever ccx. Ceci est disponible pour tous les types d\'éléments de maillage.
-   Boire une ou deux bières

Voir aussi :

-   [Ajouter un tutoriel sur le solveur FEM](Sandbox:Add_FEM_Solver_Tutorial/fr.md).
-   [Tutoriel FEM Module d\'extension](Extend_FEM_Module/fr.md)
-   Les efforts d\'implémentation du solveur [oofem](https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem).
-   Les efforts de mise en œuvre du solveur \[<https://github.com/FreeCAD/FreeCAD/compare/a03eb6b9625ba>\...dfc01ec949525 myStran\].

## Écrire des tests unitaires 

A définir

## Informatif

-   [Encapsuler une classe Cplusplus dans Python](Wrapping_a_Cplusplus_class_in_Python/fr.md)
-   [Tutoriel: Ajouter des équations FEM](Add_FEM_Equation_Tutorial/fr.md)
-   [Tutoriel Ajout d\'un bouton dans la barre d\'outils FEM](Add_Button_to_FEM_Toolbar_Tutorial/fr.md)

## En relation 

-   Bugs FEM dans le [bugtracker de FreeCAD](https://tracker.freecadweb.org/set_project.php?project_id=4;14).
-   Ouvrir les commentaires FEM [FIXME](https://github.com/FreeCAD/FreeCAD/search?q=FIXME+AND+fem) dans le code source de FreeCAD
-   Ouvrez les commentaires FEM [TODO](https://github.com/FreeCAD/FreeCAD/search?q=TODO+AND+fem) dans le code source de FreeCAD.
-   [Discussion sur le fil de discussion original](https://forum.freecadweb.org/viewtopic.php?f=18&t=60574) pour cette page wiki.
-   [atelier FEM](FEM_Workbench/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Onboarding FEM Devs/fr
