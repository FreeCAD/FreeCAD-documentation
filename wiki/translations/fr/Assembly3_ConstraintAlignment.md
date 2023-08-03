---
 GuiCommand:
   Name: Assembly3 ConstraintAlignment
   Name/fr: Assembly3 Contrainte d'alignement
   Icon: Assembly_ConstraintAlignment.svg
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 ConstraintAlignment/fr

## Description

Cet outil relie deux ou plusieurs objets d\'un assemblage et fait correspondre leurs orientations. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), les objets suivants sont déplacés vers des positions où les plans x-y de tous les SCI sont coplanaires et les axes z pointent dans la même direction.

Le décalage de leurs axes z et l\'angle entre leurs axes x (et y également) ne sont pas définis. En ce qui concerne le premier objet, les objets suivants peuvent toujours se déplacer dans les directions x et y et tourner autour de l\'axe z. Cela laisse 3 degrés de liberté pour chaque lien sans contrainte. Cela laisse 3 degrés de liberté (DOF = degrees of freedom) pour chaque lien sans contrainte.

## Utilisation

1.  Placez deux objets ou plus dans un assemblage.
2.  Sélectionnez un élément de face planaire de chaque objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintAlignment.svg" width=16px>[Alignment](Assembly3_ConstraintAlignment/fr.md)**.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintAlignment/fr
