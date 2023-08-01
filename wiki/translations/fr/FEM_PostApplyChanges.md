---
- GuiCommand:/fr
   Name:FEM PostApplyChanges
   Name/fr:FEM Appliquer les modifications
   MenuLocation:Résultats → Appliquer les modifications au pipeline
   |Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Std Rafraîchir](Std_Refresh/fr.md), [FEM Fonctions de filtrage](FEM_PostCreateFunctions.md)
---

# FEM PostApplyChanges/fr

## Description

Permet d\'indiquer si les modifications apportées aux pipelines et aux filtres sont appliquées immédiatement ou non.

Si la fonction est active, les modifications apportées aux [fonctions de filtrage](FEM_PostCreateFunctions/fr.md) et aux filtres ont un effet immédiat. Cependant, pour les grands maillages de résultats, cela peut ralentir le PC de manière significative.

Si la fonction n\'est pas active, un changement de la taille et de la position des fonctions aura d\'abord un effet après avoir recompilé l\'objet fonction (voir [Std Rafraîchir](Std_Refresh/fr.md)). Pour les modifications des filtres, la modification aura d\'abord un effet lorsque vous appuierez dans le menu du dialogue du filtre sur le bouton **Appliquer** ou en recompilant l\'objet filtre.



## Utilisation

Cliquez sur le bouton de la barre d\'outils **<img src="images/FEM_PostApplyChanges.svg" width=16px> '''Appliquer les modifications au pipeline'''** ou utilisez le menu **Résultats → <img src="images/FEM_PostApplyChanges.svg" width=16px> Appliquer les modifications au pipeline**.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostApplyChanges/fr
