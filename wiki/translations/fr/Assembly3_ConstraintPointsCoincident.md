---
- GuiCommand:/fr
   Name:Assembly3 ConstraintPointsCoincident
   Name/fr:Assembly3 Contrainte de points coïncidents
   Icon:Assembly_ConstraintPointCoincident.svg
   Workbenches:[Assembly3](Assembly3_Workbench/fr.md)
---

## Description

Cet outil établit un lien entre deux objets d\'un assemblage et fixe la distance entre eux et leur orientation l\'un par rapport à l\'autre. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), l\'objet suivant est déplacé vers une position où les origines des deux ICS sont au même endroit.

Les éléments ponctuels n\'ont aucun étirement dans aucune direction (longueur nulle) et il n\'est donc pas possible de détecter une orientation, c\'est-à-dire que leurs ICS servent uniquement à correspondre aux paramètres des autres éléments. L\'orientation des ICS reste toujours la même que celle du système de coordonnées global et ne peut être utilisée pour réduire les degrés de liberté liés à la rotation.

Par rapport au premier objet, l\'objet suivant peut encore tourner autour de l\'origine (autour des trois axes). Cela laisse 3 degrés de liberté (DOF = degrees of freedom) pour chaque lien sans contrainte.

## Utilisation

1.  Placez deux objets dans un assemblage
2.  Sélectionnez un élément ponctuel de chaque objet
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintPointCoincident.svg" width=16px> [Points coincident](Assembly3_ConstraintPointsCoincident/fr.md)**.






