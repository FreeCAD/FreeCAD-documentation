---
- GuiCommand:/fr
   Name:Sketcher CreatePoint
   Name/fr:Sketcher Point
   MenuLocation:Sketch → Géométries d'esquisse → Créer un point
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
---

# Sketcher CreatePoint/fr

## Description

L\'outil Point crée un point dans l\'esquisse en cours, qui peut être utilisé pour construire des éléments de géométrie. Le point est un élément de construction et n\'apparaîtra jamais dans la vue 3D.

[480px\|Point in the sketcher](IMAGE:Sketcher_Point_fr_01.png.md) 

## Utilisation

-   Cliquez sur le bouton **<img src="images/Sketcher_CreatePoint.svg" width=24px> Créer un point**, pour activer la fonction.
-   Cliquez dans l\'esquisse pour créer un ou plusieurs Point(s).
-   Pressez sur la touche **Echap** ou sur le bouton droit de la souris pour quitter la fonction.

## Options

Un mode d\'accrocher à la grille peut être défini dans la page des [Préférences](Sketcher_Preferences/fr.md) du sketcher.

Le point s\'aligne alors sur la grille, s\'il a une distance de grille inférieure à 25% par rapport à une ligne de grille.

Le mode d\'accrochage ne fixe pas les points sur la grille. Les points peuvent être déplacés avec la souris ou des contraintes vers d\'autres emplacements.

## Limitations

Le point créé n\'est pas disponible en dehors de l\'esquisse. Dans le cas où un point de référence est nécessaire dans la vue 3D, utilisez [PartDesign Point](PartDesign_Point/fr.md) ou [Part Point](Part_Point/fr.md) à la place.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/fr
