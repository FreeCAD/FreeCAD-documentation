

## Introduction

Dans FreeCAD et dans cette documentation, un [addon](addon/fr.md) est un composant qui ne fait pas partie de l\'installation de base mais peut être ajouté au système par certaines méthodes.

## Différents types {#différents_types}

Il existe environ trois types d\'extensions:

-   [Macro](Macros/fr.md): petit bout de code en [Python](Python/fr.md) qui fournit un nouvel outil ou une nouvelle fonctionnalité dans un seul fichier se terminant par `.FCMacro`.
-   Module: un seul fichier source Python, ou une collection de fichiers Python, qui étend le logiciel d\'une certaine manière. Les modules ne définissent pas nécessairement un «atelier» graphique mais peuvent fournir une fonctionnalité de support, par exemple, une bibliothèque qui effectue la conversion des formats ou du code qui modifie l\'[interface](interface/fr.md) graphique.
-   [Atelier](External_workbenches/fr.md): collections de fichiers Python qui fournissent des [Gui Commands](Gui_Command/fr.md) (outils) centrés autour d\'un sujet particulier, par exemple, des outils pour concevoir des armoires ou des outils pour travailler avec l\'architecture, ou des outils pour concevoir des bateaux, etc. Ces ateliers définissent généralement de nouvelles barres d\'outils où des [commandes](Gui_Command/fr.md) sont placées sous forme de boutons.

Les macros sont installées dans le répertoire `Macro/` de l\'utilisateur tandis que les modules et les ateliers se trouvent dans le répertoire `Mod/`. {{Code|lang=bash|code=
$HOME/.FreeCAD/Macro/
$HOME/.FreeCAD/Mod/
}}

Généralement l\'utilisation de macros sont un moyen de simplifier ou d\'automatiser une tâche de dessin ou d\'édition d\'un objet particulier. Si plusieurs de ces macros sont collectées dans un répertoire et la structure est fournie pour collecter ces outils, puis le répertoire entier peut être distribué comme un atelier.

En d\'autres termes, les macros, modules et les ateliers sont essentiellement la même chose, des éléments de code Python qui étendent les fonctionnalités de base. Les macros sont généralement courtes et concentrées sur une seule tâche, les modules fournissent généralement de nouvelles fonctions ou interfaces, et les ateliers sont des collections d\'outils (boutons, menus) et d\'interfaces graphiques pour effectuer des tâches connexes.

Si un atelier est suffisamment développé et bien documenté, il peut être inclus en tant qu\'[atelier](workbenches/fr.md) de base dans FreeCAD.

## Installation

À partir de FreeCAD 0.17, la méthode recommandée pour installer des addons est d\'utiliser <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

Cependant, une installation manuelle est toujours possible.

-   [Comment installer une macro](How_to_install_macros/fr.md)
-   [Comment installer un atelier](Installing_more_workbenches/fr.md)




[Category:Addons{{\#translation:}}](Category:Addons.md)
