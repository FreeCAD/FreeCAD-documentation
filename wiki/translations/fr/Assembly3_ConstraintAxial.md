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
3.  Activez la commande <img alt="" src=images/Assembly_ConstraintAxial.svg  style="width:16px;">. **Contrainte axiale** en utilisant l\'une des commandes suivantes :
    -   Le bouton **<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Create "AxialAlignment" constraint](Assembly3_ConstraintAxial/fr.md)**.

## Équivalent cinématique 

Utilisée dans un contexte cinématique, cette contrainte ressemble à une *articulation cylindrique*.

Dans la vie réelle, nous ne pouvons pas manipuler les axes et nous utilisons donc des faces cylindriques pour représenter les axes liés.

<img alt="" src=images/Assembly3_ConstraintAxial-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintAxial-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintAxial-03.png  style="width:200px;">



*Objets contraints avant et après l'exécution du solveur puis glissés le long de l'axe*



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 ConstraintAxial/fr
