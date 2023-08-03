---
 GuiCommand:
   Name: Assembly3 ConstraintPointsCoincident
   Name/fr: Assembly3 Contrainte de points coïncidents
   Icon: Assembly_ConstraintPointCoincident.svg
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 ConstraintPointsCoincident/fr

## Description

La commande <img alt="" src=images/Assembly_ConstraintPointCoincident.svg  style="width:24px;"> [Contrainte de points coïncidents](Assembly3_ConstraintPointsCoincident/fr.md) établit un lien entre deux objets d\'un assemblage et fixe la distance entre eux et leur orientation. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), l\'objet suivant est déplacé vers une position où les origines des deux ICS sont au même endroit.

Par rapport au premier objet, l\'objet suivant peut encore tourner autour de l\'origine (autour des trois axes). Cela laisse 3 degrés de liberté (DOF = degrees of freedom) pour chaque lien sans contrainte.

Cette contrainte accepte tout type d\'élément !

## Utilisation

1.  Placez deux objets dans un assemblage
2.  Sélectionnez un élément ponctuel de chaque objet
3.  Activez la commande <img alt="" src=images/Assembly_ConstraintPointCoincident.svg  style="width:16px;"> **Contrainte de points coïncidents** en utilisant la commande suivante :
    -   Le bouton **<img src="images/Assembly_ConstraintPointCoincident.svg" width=16px> [Create "PointsCoincident" constraint](Assembly3_ConstraintPointsCoincident/fr.md)**.

## Équivalent cinématique 

Utilisée dans un contexte cinématique, cette contrainte ressemble à une **articulation à rotule**.

Dans la vie réelle, nous ne pouvons pas manipuler les points, c\'est pourquoi des faces sphériques sont utilisées pour représenter les points liés.

<img alt="" src=images/Assembly3_ConstraintPointsCoincident-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintPointsCoincident-02.png  style="width:200px;">



*Objets contraints avant et après l'exécution du solveur*



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPointsCoincident/fr
