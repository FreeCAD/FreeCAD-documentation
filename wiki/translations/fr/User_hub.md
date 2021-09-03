 <img alt="" src=images/User_hub.png  style="width:64px;">

------------------------------------------------------------------------

\_\_NOTOC\_\_

Cette zone est la source d\'aide principale pour les nouveaux utilisateurs de FreeCAD.

Veuillez noter que tout comme FreeCAD, ces pages sont continuellement en développement. Si vous ne trouvez pas les informations dont vous avez besoin, n\'hésitez pas à les demander sur le [forum FreeCAD](http://forum.freecadweb.org).

Si vous voulez apporter votre contribution à FreeCAD, vous pouvez [faire un don](donate.md) ou rendez-vous sur la page [Aider FreeCAD](Help_FreeCAD/fr.md) pour d\'autres moyens de contribuer. Si vous souhaitez modifier ce wiki, [demandez un compte wiki avec des autorisations d\'édition sur le forum](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) et lisez les [Les pages Wiki](WikiPages/fr.md) pour les règles générales à suivre.

Si vous souhaitez découvrir comment le développement de FreeCAD a débuté il y a des années, rendez vous à la page [Histoire](History/fr.md).

## Utiliser FreeCAD 

### Introduction

-   [À propos de FreeCAD](About_FreeCAD/fr.md) : un aperçu général de FreeCAD.
-   Installation : comment installer FreeCAD [sur Windows](Installing_on_Windows/fr.md), [sur Linux](Installing_on_Linux/fr.md) et [sur Mac](Installing_on_Mac/fr.md).
-   [Installation du fichier d\'aide](Installing_Helpfile/fr.md) : comment installer la documentation hors ligne basée sur ce wiki.
-   [Installer des logiciels supplémentaires](Installing_additional_components/fr.md) : comment installer des composants tiers supplémentaires qui peuvent fonctionner avec FreeCAD.
-   [Premiers pas](Getting_started/fr.md) : un rapide tour d\'horizon des outils disponibles.
-   [FAQ](Frequently_asked_questions/fr.md) : foire aux questions.
-   Des [tutoriels](Tutorials/fr.md) couvrant différentes parties de FreeCAD.

Voir aussi :

-   [Migrer vers FreeCAD depuis Fusion360](Migrating_to_FreeCAD_from_Fusion360/fr.md)

### Concepts de base de l\'application 

-   [Interface](Interface/fr.md) : l\'interface FreeCAD est composée de divers éléments graphiques à l\'écran, y compris la [Vue 3D](3D_view/fr.md), la [vue d\'arborescence](tree_view/fr.md), l\'[éditeur de propriétés](property_editor/fr.md), le [panneau de tâches](task_panel/fr.md) et la [console Python](Python_console/fr.md).
-   [Navigation par la souris](Mouse_navigation/fr.md) : les différents types d\'utilisation de la souris ou du trackpad pour naviguer dans la vue 3D.
-   [Méthodes de sélection](Selection_methods/fr.md) : différentes méthodes de sélection d\'objets dans le logiciel.
-   [Objet name](Object_name/fr.md) : tous les objets ont un `Name` en lecture seule qui les identifie de manière unique et un `Label` qui est modifiable par l\'utilisateur.
-   [Éditeur de préférences](Preferences_Editor/fr.md) : le système qui vous permet de contrôler de nombreuses propriétés du système de base et des ateliers individuels.
-   [Formats de fichiers](Import_Export/fr.md) : les différents formats que FreeCAD peut lire et écrire.

### Ateliers

Les [ateliers](Workbenches/fr.md) sont des ensembles d'outils utilisés pour des tâches spécifiques. Voici les ateliers de base fournis avec chaque installation de FreeCAD :

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Macros

Les [macros](Macros/fr.md) sont de petits fragments de code [Python](Python/fr.md) qui exécutent une tâche simple ou complexe qui n\'est pas disponible dans le système FreeCAD de base.

Des utilisateurs avertis ont écrit différentes [macros](macros/fr.md) pour améliorer FreeCAD en rajoutant des fonctionnalités.

Depuis FreeCAD 0.17, de nombreuses macros peuvent être installées à l\'aide du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour une liste des macros, reportez-vous à la page [Liste des macros](Macros_recipes/fr.md). Pour une installation manuelle, voir [Comment installer des macros](How_to_install_macros/fr.md).

### Ateliers Externes 

Lorsque de nombreuses macros ou fonctions sont développées ensemble et organisées dans des barres d'outils et des menus, elles peuvent devenir un nouvel atelier.

Les [Ateliers externes](External_workbenches/fr.md) sont des collections de fonctions qui ne font pas partie du système FreeCAD de base, généralement développées par des utilisateurs expérimentés et visant un besoin particulier.

Depuis FreeCAD 0.17, beaucoup d\'ateliers peuvent être installés à l'aide du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour l\'installation manuelle, voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md).

## Références

[Liste des commandes](List_of_Commands/fr.md) : Une liste complète des commandes disponibles dans FreeCAD.

## Aide en ligne 

Il s\'agit de l\'aide en ligne officielle de FreeCAD. Veuillez noter que l\'ensemble du système d\'aide en ligne est actuellement retravaillé. Il sera utilisé pour générer un fichier .CHM, qui sera inclus avec les paquets d\'installation de FreeCAD. Actuellement, l\'aide en ligne recense quelques uns des articles les plus complets de ce wiki.

-   [Table des matières de l\'aide en ligne](Online_Help_Toc/fr.md)

## Plus

-   Le [Centre des utilisateurs expérimentés](Power_users_hub/fr.md) est l\'endroit où vous pouvez aller si vous voulez approfondir l\'utilisation de FreeCAD.
-   Le [Portail de la Communauté FreeCAD](FreeCAD_Community_Portal/fr.md) liste les projets réalisés par les membres de la communauté d\'utilisateurs de FreeCAD.
-   Vous ne comprenez pas un mot ou une expression utilisée dans FreeCAD ? Essayez la page [Glossaire](Glossary/fr.md).




[Category:Hubs{{\#translation:}}](Category:Hubs.md)
