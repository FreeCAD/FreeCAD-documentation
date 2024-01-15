---
 GuiCommand:
   Name: Std TreeMultiDocument
   Name/fr: Std Arborescence Tous les documents
   MenuLocation: Affichage , Actions dans la vue en arborescence , Tous les documents
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_TreeSingleDocument/fr, Std_TreeCollapseDocument/fr
---

# Std TreeMultiDocument/fr

## Description

La commande **Std Tous les documents** bascule le mode Document de la [vue en arborescence](Tree_view/fr.md) au mode Tous les documents. Dans ce mode, tous les documents sont visibles dans l\'arborescence et plusieurs documents peuvent être développés. Les autres modes sont [Document unique](Std_TreeSingleDocument/fr.md) et [Réduire/développer](Std_TreeCollapseDocument/fr.md).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option **Tous les documents** dans le menu déroulant. Remarque : l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option **Affichage → du mode Document → <img src="images/Std_TreeMultiDocument.svg" width=16px> Tous les documents** du menu.



## Préférences

Le mode Tous les documents de l\'arborescence est enregistré: **Outils → Éditer les paramètres... → BaseApp → Preferences → TreeView → DocumentMode**. Il s\'agit d\'une valeur entière. Les valeurs possibles sont `0` (SingleDocument- un seul document), `1` (MultiDocument - Tous les documents) ou `2` (CollapseDocument - Réduire les documents). La valeur par défaut est `2`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeMultiDocument/fr
