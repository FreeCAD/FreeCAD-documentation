---
- GuiCommand:
   Name: Assembly3 ConstraintEqualAngle
   Name/fr: Assembly3 Contrainte égalité angle
   Icon: Assembly_ConstraintEqualAngle.svg
   Workbenches: [Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintEqualAngle/fr

## Description

Cet outil construit un lien entre deux objets d\'un assemblage et fixe un angle entre eux par rapport à la valeur d\'un autre angle. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS) sont utilisés pour positionner un objet par rapport à un autre.

Il peut traiter des éléments de ligne 3D et des éléments de face planaire ainsi que des éléments de ligne 2D dans un plan de travail.

Les directions des lignes ainsi que les normales des faces sont représentées par l\'axe z de chaque ICS, ce qui permet de fixer l\'angle entre les axes z des deux éléments (sur la base d\'un autre angle entre deux axes z).

## Utilisation

1.  Placez deux objets dans un assemblage
2.  Sélectionnez un élément de ligne ou un élément de face planaire de chaque objet.
3.  Sélectionnez deux autres éléments de ligne ou de face planaire pour extraire la valeur de l\'angle entre eux.
4.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintEqualAngle.svg" width=16px> [Equal angle](Assembly3_ConstraintEqualAngle/fr.md)**.

:   En outre, la fonction \"Flip element\" du panneau des propriétés des éléments peut être nécessaire si les SCI ne sont pas orientés comme prévu.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintEqualAngle/fr
