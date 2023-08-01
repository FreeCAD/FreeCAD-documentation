---
- GuiCommand:
   Name: Assembly3 ConstraintSameOrientation
   Name/fr: Assembly3 Contrainte orientation identique
   Icon: Assembly_ConstraintSameOrientation.svg
   Workbenches: [Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintSameOrientation/fr

## Description

Cet outil établit un lien entre deux ou plusieurs objets d\'un assemblage et fait correspondre leur orientation. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), les objets suivants sont déplacés vers des positions où tous les ICS ont la même orientation, c\'est-à-dire que tous les axes z sont parallèles et tous les axes x sont parallèles (ce qui rend les axes y également parallèles).

Le décalage de leurs origines dans les directions x, y et z n\'est pas défini. En ce qui concerne le premier objet, les objets suivants peuvent toujours se déplacer le long des axes x, y et z. Cela laisse 3 degrés de liberté pour chaque lien sans contrainte. Cela laisse 3 degrés de liberté (DOF = degree of freedom) pour chaque lien sans contrainte.

La contrainte accepte les faces planes.

## Utilisation

1.  Placez deux objets ou plus dans un assemblage
2.  Sélectionnez un élément de face plane de chaque objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintSameOrientation.svg" width=16px> [Same orientation](Assembly3_ConstraintSameOrientation/fr.md)**.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintSameOrientation/fr
