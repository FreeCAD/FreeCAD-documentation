---
- GuiCommand   */fr
   Name   *Assembly3 ConstraintCoincidence
   Name/fr   *Assembly3 Contrainte de coïncidence
   Icon   *Assembly_ConstraintCoincidence.svg
   Workbenches   *[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintCoincidence/fr

## Description

Cet outil relie deux ou plusieurs objets d\'un assemblage et fait correspondre leurs orientations. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

En supposant que le premier objet est déjà verrouillé en place par la <img alt="" src=images/Assembly_ConstraintLock.svg  style="width   *24px;"> [Contrainte de verrouillage](Assembly3_ConstraintLock/fr.md), les objets suivants sont déplacés vers des positions où les plans x-y de tous les SCI sont coplanaires et les axes z colinéaires.

Une option pour cette liaison est de définir une distance entre les plans x-y et de les rendre parallèles.

L\'angle entre leurs axes x (et y également) n\'est pas défini. Par rapport au premier objet, les objets suivants peuvent encore tourner autour de l\'axe z. Cela laisse 1 degré de liberté (DOF = degree of freedom) pour chaque lien sans contrainte.

Ce lien peut être utilisé comme une charnière en cinématique.

La rotation peut être arrêtée en mettant Lock Angle sur true dans le panneau des propriétés et l\'angle peut être réglé sur une valeur spécifique. Avec une valeur contrôlée, le lien peut être utilisé comme un actionneur dans un système cinématique.

## Utilisation

1.  Placez deux objets ou plus dans un assemblage.
2.  Sélectionnez un élément de face plane de chaque objet.
3.  Activez la commande <img alt="" src=images/Assembly_ConstraintCoincidence.svg  style="width   *16px;"> **Contrainte de coïncidence** en utilisant la commande suivante    *
    -   Le bouton **<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Create "PlaneCoincident" constraint](Assembly3_ConstraintCoincidence/fr.md)**.

## Équivalent cinématique 

Utilisée dans un contexte cinématique, cette contrainte ressemble à une charnière ou à un *joint tournant* lorsqu\'elle est utilisée avec des arcs et des cercles.

Dans la vie réelle, les formes des objets permettent la rotation et empêchent le glissement. Dans ce cas, des arcs et des cercles sont utilisés pour simuler cela.

<img alt="" src=images/Assembly3_ConstraintCoincidence-01.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_ConstraintCoincidence-02.png  style="width   *200px;">



*Objets contraints avant et après l'exécution du solveur*



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintCoincidence/fr
