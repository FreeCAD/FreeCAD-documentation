---
- GuiCommand:/fr
   Name:Std TreeMultiDocument
   Name/fr:Std Arborescence Plusieurs documents
   MenuLocation:Affichage → Configuration de l'arborescence → Document multiple
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Arborescence Document unique](Std_TreeSingleDocument/fr.md), [Std Arborescence Réduire développer](Std_TreeCollapseDocument/fr.md)
---

## Description

La commande **Std Document multiple** bascule la [vue en arborescence](tree_view/fr.md) du mode Document (DocumentMode) au mode Document multiple (MultiDocument). Dans ce mode, tous les documents sont visibles dans l\'arborescence et plusieurs documents peuvent être développés. Les autres modes sont [Document unique](Std_TreeSingleDocument/fr.md) et [Réduire développer](Std_TreeCollapseDocument/fr.md).

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option {{MenuCommand|Multi document}} dans le menu déroulant. Remarque: l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option {{MenuCommand|Affichage → Configuration de l'arborescence → <img src="images/Std_TreeMultiDocument.svg" width=16px> Document multiple}} dans le menu.

## Préférences

Le mode de l\'arborescence est enregistré: {{MenuCommand|Outils → Editer paramètres... → BaseApp → Preferences → TreeView → DocumentMode}}. Il s\'agit d\'une valeur entière. Les valeurs possibles sont `0` (SingleDocument- un seul document), `1` (MultiDocument - plusieurs documents) ou `2` (CollapseDocument - Réduire les documents). La valeur par défaut est `2`.





{{Std Base navi

}}  
