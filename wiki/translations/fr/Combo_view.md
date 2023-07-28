# Combo view/fr
{{TOCright}}

## Introduction

La [vue combinée](combo_view/fr.md) est l'un des panneaux principaux de l'[interface](interface/fr.md) FreeCAD. Il est situé sur le côté gauche de l\'écran par défaut. Il est composé de **deux parties** :

-   la [partie supérieure](#Partie_sup.C3.A9rieure.md) comporte deux onglets : l\'onglet **Modèle** et l\'onglet **Tâches**
-   la [partie inférieure](#Partie_inf.C3.A9rieure.md) affiche l\'[éditeur de propriétés](property_editor/fr.md). Il comporte deux onglets: pour les propriétés **Vue** et les **Données**. **\'Remarque :** L\'[éditeur de propriétés](property_editor/fr.md) s\'affiche uniquement lorsque l\'onglet **Modèle** est **actif**, c\'est-à-dire lorsque la [vue arborescente](tree_view/fr.md) est visible.


**Remarque:**

à l\'origine, la partie supérieure ([vue arborescente](tree_view/fr.md)) était séparée de la partie inférieure ([éditeur de propriétés](property_editor/fr.md)), mais elles ont ensuite été combinées et la vue \"combo\" a donc été créée.



## Partie supérieure 

L\'onglet **Modèle** affiche la [vue arborescente](tree_view/fr.md), qui représente le contenu du document, y compris les géométries 2D et 3D avec leur historique paramétrique, mais également les objets de prise en charge contenant des données enregistrées dans le document.

L\'onglet **Tâches** affiche le [panneau des tâches](task_panel/fr.md), qui indique différentes actions en fonction de l\'atelier actif et de l\'outil actif.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="600px;">



*La vue combinée comporte deux onglets : l'onglet Modèle qui permet d'afficher la [vue arborescente](tree_view/fr.md) avec l'[éditeur de propriétés](property_editor/fr.md), et l'onglet Tâches qui contrôle l'affichage du [panneau de tâches](task_panel/fr.md).*



## Partie inférieure 

La partie inférieure de la vue combinée affiche l\'[éditeur de propriétés](property_editor/fr.md), qui affiche deux onglets pour les propriétés **Vue** et **Données**. L\'éditeur de propriétés s\'affiche uniquement lorsque l\'onglet **Modèle** est actif, c\'est-à-dire lorsque la [vue arborescente](tree_view/fr.md) est visible.

-   L\'onglet **Vue** affiche les propriétés de visualisation des objets, qui n\'affectent que leur apparence dans la [vue 3D](3D_view/fr.md).

-   L\'onglet **Données** affiche les propriétés paramétriques des objets, qui déterminent la définition des formes géométriques.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Tree_Data_properties.png  style="width:" height="600px;">



*La partie inférieure de la vue combinée est l'éditeur de propriétés, qui affiche les propriétés Vue et Données.*

## Désactiver la vue combinée 

Pour utiliser ces vues par elles-mêmes, utilisez l\'[éditeur de paramètres](Std_DlgParameter/fr.md). Créez les sous-groupes suivants s\'ils n\'existent pas :

-    `BaseApp/Preferences/DockWindows/TreeView`
    

-    `BaseApp/Preferences/DockWindows/PropertyView`
    

ajoutez ensuite le paramètre `Enabled` de type `Booléen` et définissez-le sur `True`.

Activez ensuite la vue à l\'aide du menu, **Affichage → Panneaux → Vue arborescente** ou **→ Affichage des propriétés**.


{{Std Base navi

}} {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Combo view/fr
