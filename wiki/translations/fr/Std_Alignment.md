---
- GuiCommand:
   Name: Std Alignment
   Name/fr: Std Alignement
   MenuLocation: Édition - Alignement...
   Workbenches: Tous
   SeeAlso: [Std Positionnement](Std_Placement/fr.md)
---

# Std Alignment/fr

## Description

La commande **Std Alignement** aligne un objet par rapport à un objet de référence fixe en utilisant une ou plusieurs paires de points.

![](images/Std_Alignment_example.png ) 
*L'interface de commande après la définition de deux paires de points*

## Utilisation

1.  Sélectionnez l\'objet de référence. Ce sera l\'objet fixe et ne sera pas modifié.
2.  Maintenez la touche **Ctrl** enfoncée pendant que vous sélectionnez l\'objet dont vous souhaitez modifier l\'emplacement.
3.  Sélectionnez l\'option **Édition → Alignement ...** dans le menu.
4.  Une nouvelle fenêtre apparaîtra dans la [Zone de vue principale](Main_view_area/fr.md). Cette fenêtre se compose de deux vues : à gauche l\'objet mobile est affiché et à droite l\'objet fixe.
5.  Définissez la première paire de points en cliquant sur un point dans chaque vue. Cette paire de points est utilisée pour déplacer l\'objet mobile.
6.  Définissez une ou deux paires de points supplémentaires si vous souhaitez également faire pivoter l\'objet mobile.
7.  Cliquez avec le bouton droit sur l\'une des vues et sélectionnez l\'option **Align** dans le menu contextuel pour terminer la commande.

## Options

Les options supplémentaires suivantes sont disponibles dans le menu contextuel :

-   Sélectionnez l\'option **Remove last point** pour supprimer le dernier point de la vue.
-   Sélectionnez l\'option **Cancel** pour abandonner la commande.
-   Cochez l\'option **Syncronize views** si des changements de vue (panoramique, rotation et zoom) doivent être appliqués aux deux vues en même temps.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Alignment/fr
