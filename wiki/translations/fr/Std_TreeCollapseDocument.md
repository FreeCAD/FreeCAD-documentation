---
 GuiCommand:
   Name: Std TreeCollapseDocument
   Name/fr: Std Arborescence Réduire/développer
   MenuLocation: Affichage , Vue en arborescence , Réduire/développer
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_TreeSingleDocument/fr, Std_TreeMultiDocument/fr
---

# Std TreeCollapseDocument/fr

## Description

La commande **Std Réduire/développer** bascule du mode document de la [vue en arborescence](Tree_view/fr.md) au mode réduction de document. Dans ce mode, l\'activation de la [vue 3D](3D_view/fr.md) d\'un document développera automatiquement ce document dans l\'arborescence et réduira tous les autres documents. Les autres modes sont [Arborescence Document unique](Std_TreeSingleDocument/fr.md) et [Arborescence Tous les documents](Std_TreeMultiDocument/fr.md).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_TreeSyncView.svg" width=16px>** et sélectionnez l\'option **Réduire/développer** dans le menu déroulant. Remarque : l\'image du bouton changera en fonction de l\'option sélectionnée.
    -   Sélectionnez l\'option **Affichage → Vue en arborescence → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Réduire/développer** du menu.



## Préférences

Le mode Document de l\'arborescence est enregistré dans : **Outils → Éditer les paramètres... → BaseApp → Preferences → TreeView → DocumentMode**. Il s\'agit d\'une valeur entière. Les valeurs possibles sont `0` (SingleDocument- un seul document), `1` (MultiDocument - plusieurs documents) ou `2` (CollapseDocument - Réduire les documents). La valeur par défaut est `2`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeCollapseDocument/fr
