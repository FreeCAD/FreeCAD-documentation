---
- GuiCommand:/fr
   Name:Assembly3 ConstraintAxial
   Name/fr:Assembly3 Contrainte axiale
   Icon:Assembly_ConstraintAxial.svg
   Workbenches:[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintAxial/fr

## Description

Cet outil établit un lien entre deux ou plusieurs objets d\'un assemblage et fait correspondre leur orientation. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), les objets suivants sont déplacés vers des positions où les axes z sont colinéaires.

Le décalage de leurs origines sur leur axe z commun et l\'angle entre leurs axes x (et y également) ne sont pas définis. Par rapport au premier objet, les objets suivants peuvent toujours se déplacer le long de l\'axe z et tourner autour de cet axe. Cela laisse 2 degrés de liberté (DOF = degrees of freedom) pour chaque lien sans contrainte.

La contrainte accepte

:   \- des arêtes droites, qui deviennent colinéaires,
:   \- des faces planes, qui sont alignées en utilisant leur axe normal à la surface,
:   \- des faces cylindriques, qui sont alignées en utilisant la direction axiale.

Différents types d\'éléments géométriques peuvent être mélangés.

## Utilisation

1.  Placez deux objets ou plus dans un assemblage.
2.  Sélectionnez un élément de chaque objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Alignement axial](Assembly3_ConstraintAxial/fr.md)**.

---
[documentation index](../README.md) > Assembly3 ConstraintAxial/fr
