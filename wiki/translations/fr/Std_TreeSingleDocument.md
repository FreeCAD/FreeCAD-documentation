---
 GuiCommand:
   Name: Std TreeSingleDocument
   Name/fr: Std Arborescence Document unique
   MenuLocation: Affichage , Actions dans la vue en arborescence , Document unique
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_TreeMultiDocument/fr, Std_TreeCollapseDocument/fr
---

# Std TreeSingleDocument/fr

## Description

La commande **Std Document unique** bascule le mode Document de la [vue en arborescence](Tree_view/fr.md) au mode Document unique. Dans ce mode, un seul document est visible dans l\'arborescence. Les autres modes sont [Arborescence Tous les documents](Std_TreeMultiDocument/fr.md) et [Arborescence Réduire/développer](Std_TreeCollapseDocument/fr.md).

En mode Document unique, vous pouvez basculer vers un autre document en activant une vue 3D appartenant à ce document. Vous pouvez le faire dans [Zone de vue principale](Main_view_area/fr.md) ou via le menu **Fenêtre** .



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option **Document unique** dans le menu déroulant. Remarque : l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option **Affichage → Actions dans la vue en arborescence → <img src="images/Std_TreeSingleDocument.svg" width=16px> Document unique** du menu.



## Préférences

Le mode Document de l\'arborescence est enregistré : **Outils → Éditer les paramètres... → BaseApp → Preferences → TreeView → DocumentMode**. Il s\'agit d\'une valeur entière. Les valeurs possibles sont `0` (SingleDocument- un seul document), `1` (MultiDocument - plusieurs documents) ou `2` (CollapseDocument - Réduire les documents). La valeur par défaut est `2`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeSingleDocument/fr
