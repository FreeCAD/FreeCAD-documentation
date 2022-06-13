---
- GuiCommand   */fr
   Name   *Std MeasureDistance
   Name/fr   *Std Mesurer une distance
   MenuLocation   *Outils → Mesurer une distance‏‎
   Workbenches   *Tous
   SeeAlso   *[Part Menu des mesures](Part_Measure_Menu/fr.md), [Draft Cote](Draft_Dimension/fr.md), [Arch Prendre des cotes](Arch_Survey/fr.md)
---

# Std MeasureDistance/fr

## Description

La commande **Std Mesurer une distance** crée un objet distance qui mesure et affiche la distance entre deux points.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton **<img src="images/Std_MeasureDistance.svg" width=16px> [Mesurer une distance](Std_MeasureDistance/fr.md)**.
    -   Utilisez **Outils  →  <img src="images/Std_MeasureDistance.svg" width=16px> Mesurer une distance** dans le menu.
2.  Sélectionnez le premier point dans la [Vue 3D](3D_view/fr.md).
3.  Sélectionnez le deuxième point n\'importe où sur un objet dans la vue 3D.
4.  L\'ordre de sélection des points peut avoir un impact sur la position de la ligne de cote.
5.  Vous pouvez également inverser la position de la ligne de cote en modifiant la propriété {{PropertyView/fr|Mirror}} de l\'objet cote.

## Remarques

-   Vous ne pouvez pas utiliser les outils d\'accrochage de l\'[atelier Draft](Draft_Workbench/fr.md) avec cette commande.
-   Pour ajouter des cotes aux dessins, utilisez les outils de cotes de l\'[atelier TechDraw](TechDraw_Workbench/fr.md).
-   Pour des outils de mesure plus complets, installez le <img alt="" src=images/Manipulator_workbench_icon.svg  style="width   *24px;"> [Atelier Manipulator](Manipulator_Workbench/fr.md) (un [Atelier externe](External_workbenches/fr.md)).

## Propriétés

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Label}}   * par défaut Label contient la distance mesurée mais cette distance n\'est pas mise à jour lorsque P1 ou P2 sont modifiés ultérieurement.


{{TitleProperty|Measurement}}

-    {{PropertyData/fr|P1}}   * le premier point de dimension.

-    {{PropertyData/fr|P2}}   * le deuxième point de dimension.

-    {{PropertyData/fr|Distance}}   * (en lecture seulement) la distance mesurée entre P1 et P2.

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Dist Factor}}   * ce facteur, multiplié par la distance mesurée, détermine le décalage de la ligne de cote.

-    {{PropertyView/fr|Font Size}}   * la hauteur des lettres (hauteur de ligne en pixels).

-    {{PropertyView/fr|Mirror}}   * si la valeur est `True`, la position de la ligne de cote par rapport à P1 et P2 est inversée.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std MeasureDistance/fr
