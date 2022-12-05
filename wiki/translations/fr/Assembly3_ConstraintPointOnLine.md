---
- GuiCommand:/fr
   Name:Assembly3 ConstraintPointOnLine
   Name/fr:Assembly3 Contrainte point sur une ligne
   Icon:Assembly_ConstraintPointOnLine.svg
   Workbenches:[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintPointOnLine/fr

## Description

Cet outil établit un lien entre deux objets d\'un assemblage et fixe la distance entre eux et leur orientation l\'un par rapport à l\'autre. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), l\'objet suivant est déplacé vers une position où l\'origine de l\'élément ponctuel se trouve sur l\'axe z de l\'élément linéaire.

Les éléments ponctuels n\'ont aucun étirement dans aucune direction (longueur nulle) et il n\'est donc pas possible de détecter une orientation, c\'est-à-dire que leurs ICS servent uniquement à correspondre aux paramètres des autres éléments. L\'orientation des ICS reste toujours la même que celle du système de coordonnées global et ne peut être utilisée pour réduire les degrés de liberté liés à la rotation. Les éléments droits ont une origine et une direction qui est représentée par l\'axe z de l\'ICS. Une direction des axes x et y n\'est pas détectable et donc la rotation autour de l\'axe z ne peut pas être utilisée pour réduire les DOF. (Cela ne s\'applique pas en combinaison avec des éléments ponctuels de toute façon\...)

Par rapport au premier objet, l\'objet suivant peut toujours se déplacer le long de l\'axe z et tourner autour des trois axes. Cela laisse 4 degrés de liberté (DOF = degrees of freedom) pour chaque lien sans contrainte.

## Utilisation

1.  Placez deux objets dans un assemblage.
2.  Sélectionnez un élément de point d\'un objet et un élément de bord droit de l\'autre objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintPointOnLine.svg" width=16px> [Point sur une ligne](Assembly3_ConstraintPointOnLine/fr.md)**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintPointOnLine/fr
