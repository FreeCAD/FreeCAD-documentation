# Addon/fr
{{TOCright}}

## Introduction

Dans FreeCAD et dans cette documentation, un [addon](addon/fr.md) est un composant qui ne fait pas partie de l\'installation de base mais peut être ajouté au système par certaines méthodes.

## Différents types 

Il existe environ trois types d\'extensions   *

-   [Macros](Macros/fr.md)   * petit bout de code en [Python](Python/fr.md) qui fournit un nouvel outil ou une nouvelle fonctionnalité dans un seul fichier se terminant par `.FCMacro`.
-   [Ateliers](External_workbenches/fr.md)   * collections de fichiers Python qui fournissent des [Gui Commands](Gui_Command/fr.md) (outils) centrés autour d\'un sujet particulier, par exemple, des outils pour concevoir des armoires ou des outils pour travailler avec l\'architecture, ou des outils pour concevoir des bateaux, etc. Ces ateliers définissent généralement de nouvelles barres d\'outils où des [commandes](Gui_Command/fr.md) sont placées sous forme de boutons.
-   [Kits de préférence](Preference_Packs/fr.md)    * kits de préférences d\'utilisateurs. {{Version/fr|0.20}}

## Installation

La méthode recommandée pour installer des addons est d\'utiliser le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

Mais pour les macros et les ateliers, une installation manuelle est également possible    *

-   [Comment installer une macro](How_to_install_macros/fr.md)
-   [Comment installer un atelier](Installing_more_workbenches/fr.md)

## Informations pour les développeurs 

Si vous avez développé une macro ou un atelier, et que vous souhaitez qu\'il soit inclus dans le gestionnaire d\'addons, lisez comment faire sur les pages    * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) et [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). Si vous ajoutez votre macro à la page [Liste des macros](Macros_recipes/fr.md), il n\'y a rien d\'autre à faire, elle sera automatiquement récupérée par le gestionnaire d\'addons.

### Ateliers en Python 

Pour les ateliers en Python, vous n\'avez pas besoin d\'une approbation spécifique pour que votre atelier soit ajouté au gestionnaire d\'addons. De plus, comme votre addon ne fait pas partie du code source de FreeCAD, vous pouvez choisir la licence qui vous convient. Si vous demandez que votre atelier soit ajouté à la liste par défaut du gestionnaire d\'addons (nous n\'ajouterons aucun nouvel atelier sans une demande de ses auteurs), soit en le demandant sur le forum, soit en ouvrant un problème sur le dépôt [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/), votre code restera sur votre propre dépôt git, nous l\'ajouterons simplement comme un sous-module au dépôt [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/). Bien sûr, avant d\'ajouter votre atelier, nous y jetterons un coup d\'œil et nous nous assurerons qu\'il n\'y a rien de potentiellement problématique. Pour plus de détails sur la structuration de votre addon, y compris des informations sur les métadonnées utilisées par le gestionnaire d\'addons, voir [Création d\'atelier](Workbench_creation/fr.md).

### Ateliers en C++ 

Si vous développez un atelier en C++, il ne peut pas être exécuté directement par les utilisateurs et doit d\'abord être compilé. Vous avez alors deux options, soit vous fournissez vous-même des versions précompilées de votre atelier, pour les différents systèmes d\'exploitation, soit vous demandez à ce que votre code soit intégré au code source de FreeCAD. Pour cela, vous devez utiliser la licence LGPL (ou une licence totalement compatible comme MIT ou BSD), et vous devez présenter vos nouveaux outils à la communauté sur le [forum de FreeCAD](https   *//forum.freecadweb.org) pour examen. Une fois que votre code a été testé et approuvé, vous devez faire un fork du dépôt FreeCAD, si ce n\'est pas encore fait, créer une nouvelle branche, y pousser votre code, et ouvrir une demande d\'extraction pour que votre branche soit fusionnée dans le dépôt principal.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/fr
