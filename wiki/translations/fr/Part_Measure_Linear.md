---
- GuiCommand:
   Name:Part Measure Linear
   Name/fr:Part Mesure linéaire
   MenuLocation:Mesure → Mesure linéaire
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Std Mesurer une distance](Std_MeasureDistance/fr.md), [Draft Dimension](Draft_Dimension/fr.md)
---

# Part Measure Linear/fr

## Description

Cette commande mesure la distance entre deux éléments topologiques sélectionnés (sommet, arête, face) et affiche les mesures dans la [vue 3D](3D_view/fr.md). La distance la plus courte entre les deux éléments et les mesures delta (distances parallèles aux axes globaux X, Y, Z) sont affichées.

L\'apparence des mesures peut être modifiée dans le menu des [préférences](PartDesign_Preferences/fr#Mesure.md).

<img alt="" src=images/MeasureLinear3D1.png  style="width:400px;"> <img alt="" src=images/MeasureLinearDelta1.PNG  style="width:400px;">

## Utilisation

1.  Sélectionner n\'importe quelle combinaison de deux éléments : sommets, arêtes, faces\...
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Part_Measure_Linear.svg" width=16px> [Mesure linéaire](Part_Measure_Linear/fr.md)**.
    -   Sélectionnez l\'option **Mesure → <img src="images/Part_Measure_Linear.svg" width=16px> Mesure linéaire** dans le menu.
3.  Alternativement, la commande peut être lancée sans sélection préalable. Un dialogue de sélection s\'ouvre alors dans le [Panneau des tâches](Task_Panel/fr.md). Un widget de contrôle fournit également des boutons pour réinitialiser la sélection, basculer l\'affichage des mesures dans la [vue 3D](3D_view/fr.md) et effacer toutes les mesures.
4.  Les mesures sont automatiquement supprimées à la fermeture du document.

## Remarques

-   Vous ne pouvez pas utiliser les outils d\'aimantation de l\'[atelier Draft](Draft_Workbench/fr.md) avec cette commande.
-   Pour ajouter des cotes aux dessins, utilisez les outils de cotes de l\'[atelier TechDraw](TechDraw_Workbench/fr.md).
-   Pour des outils de mesure plus complets, installez l\'<img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [atelier Manipulator](Manipulator_Workbench/fr.md) (un [atelier externe](External_workbenches/fr.md)).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Measure Linear/fr
