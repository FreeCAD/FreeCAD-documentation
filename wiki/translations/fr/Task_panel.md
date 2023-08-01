# Task panel/fr
{{TOCright}}

## Introduction

Le [Panneau des tâches](Task_panel/fr.md) apparaît dans l\'onglet **Tâches** de la [vue combinée](Combo_view/fr.md), l\'un des panneaux importants de l\'[interface](interface/fr.md). Il s'agit d'un espace personnalisable pouvant contenir n'importe quel type de widget graphique, comme des sous-fenêtres, des tableaux, des champs de saisie, des cases à cocher, des sélecteurs, des zones de texte, des boutons, des libellés, des images et d'autres éléments, en fonction de l\'[atelier](Workbenches/fr.md) et de l'outil couramment actifs.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="550px;">



*Le panneau des tâches montrant diverses commandes lorsque l'[atelier PartDesign](PartDesign_Workbench/fr.md) est actif et qu'une [esquisse](Sketch/fr.md) est sélectionnée.*

## Travailler avec le panneau des tâches 

Un panneau de tâches s\'ouvre normalement lorsqu\'un outil nécessitant une entrée de l\'utilisateur est activé, soit en appuyant sur un bouton de la barre d'outils ou en double-cliquant sur un objet. Si l\'outil n\'a pas besoin d\'entrée utilisateur, cela produira le résultat ou échouera, mais n\'affichera pas de panneau de tâches.

L\'utilisateur peut entrer n\'importe quoi, par exemple du texte, des coordonnées de points 3D, des éléments d\'une liste, des faces d\'une forme ou des options pour modifier le fonctionnement de l\'outil.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )



*Le panneau des tâches s'ouvre lors de la modification d'une [esquisse](Sketch/fr.md). Différents types d'informations sont présentés, tels que les messages du solveur, les options de la grille, les contraintes et les éléments géométriques.*

De nombreuses commandes requièrent la sélection de formes ou d\'objets présents dans le document ; dans ce cas, le panneau de tâches attendra que l\'utilisateur sélectionne les objets appropriés dans la [vue arborescente](tree_view/fr.md) ou la [vue 3D](3D_view/fr.md). Lorsqu\'un panneau de tâches est ouvert, il est possible de passer à l\'onglet **Modèle** pour afficher la [vue arborescente](Tree_view/fr.md) afin de choisir un objet ; une fois cela fait, il est possible de repasser à l\'onglet **Tâches** pour poursuivre la commande. Le panneau des tâches est généralement fermé en cliquant sur un bouton **OK** ou **Fermer**, ou en appuyant sur la touche **Échap** du clavier pour annuler la commande.

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )



*Le panneau des tâches s'ouvre lors de la modification d'un [Arch Composant](Arch_Component/fr.md). Le panneau attend que l'utilisateur sélectionne des objets pouvant être ajoutés ou soustraits du composant.*

**Remarque :** merci de noter que le passage de l\'onglet **Tâches** à l\'onglet **Modèle** ne met pas fin à la commande active ; la tâche sera toujours exécutée en arrière-plan. Il incombe à l\'utilisateur de mettre fin ou d\'abandonner correctement la commande active avant de lancer une tâche différente ; laisser une tâche en cours peut générer des erreurs lors du lancement d\'autres outils.

## Remarques

-   Les utilisateurs venant d\'autres solutions de CAO qui utilisent la touche **Echap** dans le cadre de leur flux de travail peuvent obtenir des résultats différents dans FreeCAD. Lorsque la touche **Echap** est pressée dans FreeCAD, le panneau des tâches en cours d\'exécution se ferme. Pour désactiver cette fonctionnalité, veuillez consulter [Réglage fin](Fine-tuning#Escape_Key.md) et [Sketcher Préférences](Sketcher_Preferences/fr#G.C3.A9n.C3.A9ral.md).


{{Interface navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Task panel/fr
