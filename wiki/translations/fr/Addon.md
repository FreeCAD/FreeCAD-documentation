# Addon/fr
{{TOCright}}

## Introduction

Dans FreeCAD et dans cette documentation, une [extension](addon/fr.md) est un composant qui ne fait pas partie de l\'installation de base mais peut être ajouté au système par certaines méthodes.

## Différents types 

Il existe environ trois types d\'extensions:

-   [Macros](Macros/fr.md): petit bout de code en [Python](Python/fr.md) qui fournit un nouvel outil ou une nouvelle fonctionnalité dans un seul fichier se terminant par `.FCMacro`.
-   [Ateliers](External_workbenches/fr.md): collections de fichiers Python qui fournissent des [Gui Commands](Gui_Command/fr.md) (outils) centrés autour d\'un sujet particulier, par exemple, des outils pour concevoir des armoires ou des outils pour travailler avec l\'architecture, ou des outils pour concevoir des bateaux, etc. Ces ateliers définissent généralement de nouvelles barres d\'outils où des [commandes](Gui_Command/fr.md) sont placées sous forme de boutons.
-   [Kits de préférence](Preference_Packs/fr.md) : kits de préférences d\'utilisateurs. {{Version/fr|0.20}}

## Installation

La méthode recommandée pour installer des extensions est d\'utiliser le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Mais pour les macros et les ateliers, une installation manuelle est également possible :

-   [Comment installer une macro](How_to_install_macros/fr.md)
-   [Comment installer un atelier](Installing_more_workbenches/fr.md)

## Informations pour les développeurs 

Si vous avez développé une macro ou un atelier, et que vous souhaitez qu\'il soit inclus dans le gestionnaire des extensions, lisez comment faire sur les pages : ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) et [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Si vous ajoutez votre macro à la page [Liste des macros](Macros_recipes/fr.md), il n\'y a rien d\'autre à faire, elle sera automatiquement récupérée par le gestionnaire des extensions.

Voir aussi :

-   [Distribution d\'un atelier Python](Workbench_creation/fr#Distribution.md)
-   [Distribution d\'un atelier C++](Workbench_creation/fr#Distribution_2.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/fr
