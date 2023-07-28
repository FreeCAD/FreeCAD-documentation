---
- GuiCommand:/fr
   Name:Std SetAppearance
   Name/fr:Std Apparence
   MenuLocation:Affichage → Apparence...
   Workbenches:Tous
   Shortcut:**Ctrl**+**D**
   SeeAlso:[Part Définir les couleurs](Part_FaceColors/fr.md)
---

# Std SetAppearance/fr

## Description

La commande **Std Apparence** affiche les propriétés d\'affichage du [Panneau des tâches](Task_Panel/fr.md) pour les objets sélectionnés.

<img alt="" src=images/DlgDisplayProperties.png  style="width:250px;"> 
*Le panneau des tâches propriétés d'affichage*



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_SetAppearance.svg" width=16px> Apparence...** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_SetAppearance.svg" width=16px> Apparence...** dans le menu contextuel de la [vue en arborescence](tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **Ctrl**+**D**.
3.  Modifiez une ou plusieurs propriétés d\'affichage. Voir [Options](#Options.md). Les objets seront mis à jour immédiatement.
4.  Sélectionnez éventuellement un ou plusieurs nouveaux objets dont vous souhaitez modifier les propriétés d\'affichage.
5.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches et terminer la commande.

## Options



### Mode d\'affichage 

-   Sélectionnez un **Mode d'affichage** dans la liste déroulante. Les options disponibles sont: « Lignes plates », « Ombrées » (pas pour les objets [Draft](Draft_Workbench/fr.md)), « Filaire » et « Points ». Voir la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour plus d\'informations.



### Matériau

-   Sélectionnez un matériau prédéfini dans la liste déroulante (\'Par défaut\', \'Aluminium\', \'Laiton\', \'Bronze\', etc.).
-   Appuyez sur le bouton **...** pour ouvrir la boîte de dialogue Propriétés du matériau et modifier les couleurs ambiantes, diffuses, émissives et spéculaires, ainsi que la brillance.
-   **Diagramme de couleur:** non pris en charge pour le moment.
-   **Couleur de la forme :** définit la propriété **Shape Color**. Appuyez sur le bouton pour ouvrir la boîte de dialogue Sélectionner une couleur.
-   **Couleur de trait :** définit la propriété **Line Color**. Appuyez sur le bouton pour ouvrir la boîte de dialogue Sélectionner une couleur.
-   **Couleur du point :** définit la propriété **Point Color**. Appuyez sur le bouton pour ouvrir la boîte de dialogue Sélectionner une couleur.



### Affichage

-   **Taille de point :** définit la propriété **Point Size** (en pixels).
-   **Epaisseur de ligne :** définit la propriété **Line Width** (en pixels).
-   **Transparence :** définit la propriété **Transparency** (en pourcentage). 0% est opaque, 100% est entièrement transparent.
-   **Transparence de ligne :** non pris en charge pour le moment.



## Remarques

-   Les propriétés de vue mentionnées peuvent également être modifiées dans l\'[Éditeur de propriétés](Property_editor/fr.md) ou la [Vue combinée](Combo_view/fr.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SetAppearance/fr
