---
- GuiCommand   */fr
   Name   *Std TreeCollapseDocument
   Name/fr   *Std Arborescence Réduire développer
   MenuLocation   *Affichage → Configuration de l'arborescence → Réduire/développer
   Workbenches   *Tous
   Version   *0.19
   SeeAlso   *[Std Arborescence Document unique](Std_TreeSingleDocument/fr.md), [Std Arborescence Document multiple](Std_TreeMultiDocument/fr.md)
---

# Std TreeCollapseDocument/fr

## Description

La commande **Std Réduire développer** bascule la [vue en arborescence](tree_view/fr.md) du mode document (DocumentMode) au mode réduction document (CollapseDocument). Dans ce mode, l\'activation de la [vue 3D](3D_view/fr.md) d\'un document développera automatiquement ce document dans l\'arborescence et réduira tous les autres documents. Les autres modes sont [Un seul document arborescence](Std_TreeSingleDocument/fr.md) et [Plusieurs documents arborescence](Std_TreeMultiDocument/fr.md).

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option **Réduire/développer** dans le menu déroulant. Remarque   * l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option **Affichage → Configuration de l'arborescence → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Réduire/développer** dans le menu.

## Préférences

Le mode de l\'arborescence est enregistré   * **Outils → Editer paramètres... → BaseApp → Preferences → TreeView → DocumentMode**. Il s\'agit d\'une valeur entière. Les valeurs possibles sont `0` (SingleDocument- un seul document), `1` (MultiDocument - plusieurs documents) ou `2` (CollapseDocument - Réduire les documents). La valeur par défaut est `2`.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TreeCollapseDocument/fr
