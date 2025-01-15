---
 GuiCommand:
   Name: Std SetAppearance
   Name/fr: Std Apparence
   MenuLocation: Affichage , Définir l'apparence...
   Workbenches: Material_Workbench/fr, Part_Workbench/fr, PartDesign_Workbench/fr et d'autres
   Shortcut: **Ctrl**+**D**
   SeeAlso: Std_SetMaterial/fr, Part_ColorPerFace/fr
---

# Std SetAppearance/fr

## Description

La commande **Std Apparence** définit les propriétés d\'affichage des objets sélectionnés.

Cette page a été mise à jour pour la version 1.0.

![](images/Std_SetAppearance_Taskpanel.png ) 
*Le panneau des propriétés d'affichage*



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons de lancer la commande :
    -   Sélectionnez l\'option **Affichage → <img src="images/Std_SetAppearance.svg" width=16px> Définir l'apparence...** du menu.
    -   Sélectionnez l\'option **<img src="images/Std_SetAppearance.svg" width=16px> Définir l'apparence...** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **Ctrl**+**D**.
3.  Le panneau de tâches **Propriétés d\'affichage** s\'ouvre. Voir [Options](#Options.md).
4.  Modifiez une ou plusieurs propriétés.
5.  Les objets sont mis à jour immédiatement.
6.  Vous pouvez sélectionner un ou plusieurs nouveaux objets dont vous souhaitez modifier les propriétés.
7.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches et terminer la commande.

## Options



### Mode d\'affichage 

-   Sélectionnez un **Mode d'affichage** dans la liste déroulante. Les options disponibles sont : {{Value|Filaire ombré}}, {{Value|Ombré}} (pas pour les objets [Draft](Draft_Workbench/fr.md)), {{Value|Filaire}} et {{Value|Points}}. Voir la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour plus d\'informations.



### Matériau

-   Sélectionnez un matériau dans la liste.
    1.  Vous pouvez sélectionner une catégorie dans la liste déroulante située sous la liste des matériaux pour filtrer ces derniers. Les catégories disponibles sont {{Value|Apparences de base}}, {{Value|Apparences des textures}} (ces matériaux ne sont pas encore disponibles) et {{Value|Tous les matériaux}}.
    2.  En option, appuyez sur le bouton **Lancer l'éditeur** pour lancer l\'[éditeur de matériaux](Materials_Edit/fr.md).
-   **Apparence personnalisée :** appuyez sur le bouton **...** pour remplacer l\'apparence du matériau. La fenêtre de dialogue **Propriétés du matériau** s\'ouvre. Voir [Part Couleur par face](Part_ColorPerFace/fr#Utilisation.md).
-   **Couleur des courbes :** non pris en charge pour le moment.
-   **Couleur des lignes :** définit la propriété **Line Color**. Appuyez sur le bouton pour ouvrir la fenêtre de dialogue Sélectionner une couleur.
-   **Couleur des points :** définit la propriété **Point Color**. Cliquez sur le bouton pour ouvrir la fenêtre de dialogue Sélectionner la couleur.



### Affichage

-   **Taille des points :** définit la propriété **Point Size** (en pixels).
-   **Largeur des lignes :** définit la propriété **Line Width** (en pixels).
-   **Transparence :** définit la propriété **Transparency** (en pourcentage), 0% pour opaque, 100% pour entièrement transparent.
-   **Transparence des lignes :** non pris en charge pour le moment.



## Remarques

-   Les propriétés de vue mentionnées peuvent également être modifiées dans l\'[éditeur de propriétés](Property_editor/fr.md).



---
⏵ [documentation index](../README.md) > Std SetAppearance/fr
