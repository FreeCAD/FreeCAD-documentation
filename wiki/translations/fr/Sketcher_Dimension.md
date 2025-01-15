---
 GuiCommand:
   Name: Sketcher Dimension
   Name/fr: Sketcher Contrainte de dimension
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de dimension
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **D**
   Version: 1.0
---

# Sketcher Dimension/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Dimension.svg  style="width:24px;"> [Sketcher Contrainte de dimension](Sketcher_Dimension/fr.md) est l\'outil de contrainte contextuelle de l\'atelier Sketcher. En fonction de la sélection en cours, il propose des contraintes de dimension appropriées, mais aussi des contraintes géométriques.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Vous pouvez sélectionner un ou plusieurs éléments (arêtes ou points). Les arêtes des [B-splines](Sketcher_Workbench/fr#Sketcher_CompCreateBSpline.md) ne sont actuellement pas prises en charge.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes des dimensions** est réglée sur {{Value|Les deux}} ou {{Value|Un seul outil}} (par défaut) : appuyez sur le bouton **<img src="images/Sketcher_Dimension.svg" width=16px> [Dimension](Sketcher_Dimension/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_Dimension.svg" width=16px> Dimension** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_Dimension.svg" width=16px> Dimension** du menu contextuel.
    -   S\'il y a une sélection : cliquez avec le bouton droit de la souris dans la vue 3D et sélectionnez l\'option **<img src="images/Sketcher_Dimension.svg" width=16px> Dimension** du menu contextuel.
    -   Utilisez le raccourci clavier : **D**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Si vous n\'avez pas encore sélectionné d\'élément : sélectionnez-en un.
5.  En fonction du ou des éléments sélectionnés, une contrainte est proposée.
6.  Vous pouvez sélectionner un élément supplémentaire.
7.  Vous pouvez également désélectionner un élément en le cliquant à nouveau.
8.  La contrainte proposée est mise à jour après chaque changement de sélection.
9.  Vous pouvez appuyer sur la touche **M** une ou plusieurs fois pour faire défiler les autres contraintes disponibles, le cas échéant.
10. Si une contrainte géométrique est proposée, les éléments sélectionnés peuvent changer, ce qui donne un aperçu du résultat.
11. Faites l\'une des choses suivantes :
    -   Cliquez dans une zone vide de la [vue 3D](3D_view/fr.md) pour confirmer :
        1.  Si une contrainte dimensionnelle est créée, le point cliqué détermine son emplacement. Pour une dimension linéaire, le point cliqué détermine également son type : <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:16px;"> [Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr.md), <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:16px;"> [Contrainte de distance en Y](Sketcher_ConstrainDistanceY/fr.md) ou <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:16px;"> [Contrainte de distance](Sketcher_ConstrainDistance/fr.md).
        2.  Si une [contrainte pilotante de dimension](Sketcher_ToggleDrivingConstraint/fr.md) est créée, en fonction des [préférences](Sketcher_Preferences/fr#Affichage.md), une fenêtre de dialogue s\'ouvre pour [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
        3.  Une contrainte est ajoutée.
        4.  Cet outil fonctionne toujours en mode continu : vous pouvez continuer à créer des contraintes.
    -   Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Dimension/fr
