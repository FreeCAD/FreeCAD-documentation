---
- GuiCommand:/fr
   Name:Std TreeSelection
   Name/fr:Std Arborescence Aller à la sélection
   MenuLocation:Affichage → Configuration de l'arborescence → Aller à la sélection
   Workbenches:Tous
   Shortcut:**T** **G**
   Version:0.19
---

## Description

La commande **Std Aller à la sélection** fait défiler la [vue en arborescence](tree_view/fr.md) jusqu\'au premier objet créé dans une sélection [vue 3D](3D_view/fr.md).

Si le mode de la vue en arborescence [Synchroniser la sélection](Std_TreeSyncSelection/fr.md) est désactivé, l\'arborescence défile jusqu\'au premier objet créé dans la sélection dont le parent a déjà été développé dans l\'arborescence. Si aucun des parents des objets n\'est développé, la commande n\'aura aucun effet dans ce mode.

## Utilisation

1.  Sélectionnez un ou plusieurs objets dans une vue 3D.
2.  Il existe plusieurs façons d\'appeler la commande:
3.  \* Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option {{MenuCommand|<img src="images/Std_TreeSelection.svg" width=16px> Aller à la sélection}} dans le menu déroulant. Remarque: l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option {{MenuCommand|Affichage → Configuration de l'arborescence → <img src="images/Std_TreeSelection.svg" width=16px> Aller à la sélection}} dans le menu.
    -   Sélectionnez l\'option {{MenuCommand|<img src="images/Std_TreeSelection.svg" width=16px> Aller à la sélection}} dans le menu contextuel de la vue 3D.
    -   Utilisez le raccourci clavier: **T** puis **G**.





{{Std Base navi

}}  
