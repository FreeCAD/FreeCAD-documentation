---
 GuiCommand:
   Name: FEM ResultsPurge
   Name/fr: FEM Purger les résultats
   MenuLocation: Résultats , Purger les résultats
   Workbenches: FEM_Workbench/fr
   Shortcut: **R** **P**
   SeeAlso: FEM_tutorial/fr
---

# FEM ResultsPurge/fr

## Description

**Purger les résultats** supprime tous les [objets de résultat](FEM_ResultShow/fr.md) et tous les maillages de résultat du conteneur d\'analyse actif de la [vue en arborescence](Tree_view/fr.md).


{{VersionPlus/fr|1.1}}

: supprime tous les objets de sortie de tous les solveurs (objets de résultats CalculiX, pipelines, filtres et rapports textuels).

Si vous voulez seulement supprimer un objet résultat et garder le maillage résultant, créez une copie du maillage résultant, puis sélectionnez l\'objet Result dans la vue en arborescence et supprimez-le en appuyant sur **Suppr**. De cette façon, la copie créée du maillage sera conservée. (L\'utilisation de FEM Purger les résultats supprimerait également la copie).



## Utilisation

Il existe plusieurs façons de lancer la commande :

-   Appuyez sur le bouton **<img src="images/FEM_ResultsPurge.svg" width=16px> [Purger les résultats](FEM_ResultsPurge/fr.md)**.
-   Sélectionnez l\'option **Résultats → <img src="images/FEM_ResultsPurge.svg" width=16px> Purger les résultats** du menu.
-   Utilisez le raccourci clavier : **R** puis **P**.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultsPurge/fr
