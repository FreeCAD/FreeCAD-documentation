---
- GuiCommand   */fr
   Name   *Assembly3 ConstraintMultiParallel
   Name/fr   *Assembly3 Contrainte parallèle
   Icon   *Assembly_ConstraintMultiParallel.svg
   Workbenches   *[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintMultiParallel/fr

## Description

Cet outil établit un lien entre deux ou plusieurs objets d\'un assemblage et fait correspondre leur orientation. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width   *24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), les objets suivants sont déplacés vers des positions où tous les axes z pointent dans la même direction, c\'est-à-dire que tous les axes z sont parallèles.

Le décalage de leurs origines dans les directions x, y et z et les angles entre les axes x (et y également) ne sont pas définis. Par rapport au premier objet, les objets suivants peuvent toujours se déplacer le long des axes x, y et z et tourner autour de l\'axe z. Il reste donc 4 degrés de liberté. Cela laisse 4 degrés de liberté (DOF = degrees of freedom) pour chaque lien sans contrainte.

La contrainte accepte les bords droits et les faces planes, qui deviennent parallèles.

## Utilisation

1.  Placez deux objets ou plus dans un assemblage.
2.  Sélectionnez un élément de bord droit ou un élément de face plane de chaque objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintMultiParallel.svg" width=16px> [Multi parallel](Assembly3_ConstraintMultiParallel/fr.md)**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintMultiParallel/fr
