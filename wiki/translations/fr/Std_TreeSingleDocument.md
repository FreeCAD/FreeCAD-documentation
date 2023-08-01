---
- GuiCommand:
   Name:Std TreeSingleDocument
   Name/fr:Std Arborescence Document unique
   MenuLocation:Affichage - Vue en arborescence - Document unique
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Arborescence Document multiple](Std_TreeMultiDocument/fr.md), [Std Arborescence Réduire développer](Std_TreeCollapseDocument/fr.md)
---

# Std TreeSingleDocument/fr

## Description

La commande **Std Document unique** bascule la [vue en arborescence](tree_view/fr.md) du mode Document (DocumentMode) au mode Document unique (SingleDocument). Dans ce mode, un seul document est visible dans l\'arborescence. Les autres modes sont [Arborescence Document multiple](Std_TreeMultiDocument/fr.md) et [Arborescence Réduire développer](Std_TreeCollapseDocument/fr.md).

En mode Document unique, vous pouvez basculer vers un autre document en activant une vue 3D appartenant à ce document. Vous pouvez le faire dans [Zone de vue principale](Main_view_area/fr.md) ou via le menu **Fenêtre** .



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option **Document unique** dans le menu déroulant. Remarque : l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option **Affichage → Vue en arborescence → <img src="images/Std_TreeSingleDocument.svg" width=16px> Document unique** dans le menu.



## Préférences

Le mode Document de l\'arborescence est enregistré : **Outils → Éditer les paramètres... → BaseApp → Preferences → TreeView → DocumentMode**. Il s\'agit d\'une valeur entière. Les valeurs possibles sont `0` (SingleDocument- un seul document), `1` (MultiDocument - plusieurs documents) ou `2` (CollapseDocument - Réduire les documents). La valeur par défaut est `2`.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std TreeSingleDocument/fr
