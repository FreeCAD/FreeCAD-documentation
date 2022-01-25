---
- GuiCommand:/fr
   Name:Assembly3 ConstraintAngle
   Name/fr:Assembly3 Contrainte d'angle
   Icon:Assembly_ConstraintAngle.svg
   Workbenches:[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintAngle/fr

## Description

Cet outil établit un lien entre deux objets d\'un assemblage et fait correspondre leur orientation. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS = implicit coordinate systems) sont utilisés pour positionner un objet par rapport à un autre.

L\'angle entre deux éléments, c\'est-à-dire l\'angle entre leurs axes z, est fixe.

Le décalage de leurs origines dans les directions x, y et z et les angles entre les axes x et y ne sont pas définis. Par rapport au premier objet, l\'objet suivant peut toujours se déplacer le long des axes x, y et z et tourner autour des deux axes z. Il reste donc 5 degrés de liberté (DOF = degrees of freedom) pour chaque lien non confirmé.

La contrainte accepte les bords droits et les faces planes.

## Utilisation

1.  Placez deux objets ou plus dans un assemblage.
2.  Sélectionnez un élément de bord droit ou un élément de face plane de chaque objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintAngle.svg" width=16px> [Angle](Assembly3_ConstraintAngle/fr.md)**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintAngle/fr
