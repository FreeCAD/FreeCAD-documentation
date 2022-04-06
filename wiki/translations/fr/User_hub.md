# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/fr





Cette zone est la source d\'aide principale pour les nouveaux utilisateurs de FreeCAD.

FreeCAD est en développement continu, il peut donc y avoir des informations manquantes ou périmées. Si vous ne trouvez pas l\'information dont vous avez besoin, n\'hésitez pas à la demander sur le [forum FreeCAD](https://forum.freecadweb.org).

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

#### Vous venez d\'un autre logiciel? 

-   [Solutions de contournement](Workarounds/fr.md)
-   [Migrer de Fusion360 vers FreeCAD](Migrating_to_FreeCAD_from_Fusion360/fr.md)
-   [Migrer de OnShape vers FreeCAD](Migrating_to_FreeCAD_from_OnShape/fr.md)
-   [Migrer de SolidWorks vers FreeCAD](Migrating_to_FreeCAD_from_SolidWorks/fr.md)
-   [Migrer de Revit vers FreeCAD](Migrating_to_FreeCAD_from_Revit/fr.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [BIM Tableau de compatibilité des applications](BIM_application_compatibility_table/fr.md)

### Concepts de base de l\'application 

-   [Interface](Interface/fr.md) : l\'interface FreeCAD est composée de divers éléments graphiques à l\'écran, y compris la [Vue 3D](3D_view/fr.md), la [vue d\'arborescence](tree_view/fr.md), l\'[éditeur de propriétés](property_editor/fr.md), le [panneau de tâches](task_panel/fr.md) et la [console Python](Python_console/fr.md).
-   [Navigation par la souris](Mouse_navigation/fr.md) : les différents types d\'utilisation de la souris ou du trackpad pour naviguer dans la vue 3D.
-   [Méthodes de sélection](Selection_methods/fr.md) : différentes méthodes de sélection d\'objets dans le logiciel.
-   [Objet name](Object_name/fr.md) : les objets FreeCAD ont un `Name` en lecture seule qui les identifie de manière unique et un `Label` qui est modifiable par l\'utilisateur.
-   [Éditeur de préférences](Preferences_Editor/fr.md) : le système qui vous permet de contrôler de nombreuses propriétés du système de base et des ateliers individuels.
-   [Formats de fichiers](Import_Export/fr.md) : les différents formats que FreeCAD peut lire et écrire.

### Ateliers

Les [ateliers](Workbenches/fr.md) sont des ensembles d'outils utilisés pour des tâches spécifiques. Voici les ateliers de base fournis avec chaque installation de FreeCAD :

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Outils communs](Std_Base/fr.md). Ces commandes et outils sont présents dans tous les ateliers.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> L\'[atelier Arch](Arch_Workbench/fr.md) pour travailler avec des éléments architecturaux.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> L\'[atelier Draft](Draft_Workbench/fr.md) contient des outils 2D et des opérations de CAO 2D et 3D de base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> L\'[atelier FEM](FEM_Workbench/fr.md) fournit un flux de travail d\'analyse par éléments finis (FEA).

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> L\'[atelier Image](Image_Workbench/fr.md) pour travailler avec des images bitmap.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> L\'[atelier Inspection](Inspection_Workbench/fr.md) est fait pour vous donner des outils spécifiques pour l\'examen des formes. Il est toujours en cours de développement.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> L\'[atelier Mesh](Mesh_Workbench/fr.md) pour travailler avec des maillages triangulés.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> L\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md) pour l\'interopérabilité avec OpenSCAD et la réparation de [Géométrie Solide Constructive](Constructive_solid_geometry/fr.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> L\'[atelier Part](Part_Workbench/fr.md) pour travailler avec des pièces de CAO.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> L\'[atelier Part Design](PartDesign_Workbench/fr.md) pour créer des formes de pièces à partir de dessins.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> L\'[atelier Path](Path_Workbench/fr.md) est utilisé pour produire des instructions en G-code. Il est toujours en cours de développement.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> L\'[atelier Points](Points_Workbench/fr.md) pour travailler avec des nuages de points.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> Le [atelier Raytracing](Raytracing_Workbench/fr.md) pour travailler avec le lancer de rayons (rendu).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> L\'[atelier Reverse Engineering](Reverse_Engineering_Workbench/fr.md) est destiné à fournir des outils spécifiques pour convertir des formes/solides/mailles en fonctionnalités paramétriques compatibles avec FreeCAD. Il est toujours en cours de développement.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> L\'[atelier Robot](Robot_Workbench/fr.md) pour étudier les mouvements des robots.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> L\'[atelier Sketcher](Sketcher_Workbench/fr.md) pour travailler avec des esquisses à géométrie contrainte.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> L\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md) pour créer et manipuler des données de feuilles de calcul.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> L\'[Atelier Start](Start_Workbench/fr.md) vous permet de passer rapidement à l\'un des ateliers les plus courants.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> Le [atelier Surface](Surface_Workbench/fr.md) fournit des outils pour créer et modifier des surfaces. Il est similaire à l\'outil [Part Générateur de formes](Part_Builder/fr.md) à partir des bords.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> L\'[atelier TechDraw](TechDraw_Workbench/fr.md) pour produire des dessins techniques à partir de modèles 3D. C\'est le successeur de l\'[atelier Drawing](Drawing_Workbench/fr.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> L\'[atelier Test](Testing/fr.md) est destiné au débogage de FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> L\'[atelier Web](Web_Workbench/fr.md) vous fournit une fenêtre de navigateur au lieu de la [3D view](3D_view/fr.md) dans FreeCAD.

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/fr
