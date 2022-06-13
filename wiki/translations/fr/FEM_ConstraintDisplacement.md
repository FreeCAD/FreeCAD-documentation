---
- GuiCommand   */fr
   Name   *FEM ConstraintDisplacement
   Name/fr   *FEM Contrainte de déplacement
   MenuLocation   *Modèle → Contraintes mécaniques → Contrainte de déplacement
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   Shortcut   *
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM ConstraintDisplacement/fr

## Description

Crée une contrainte FEM pour un déplacement prescrit d\'un objet sélectionné pour un degré de liberté spécifié.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> [Contrainte de déplacement](FEM_ConstraintDisplacement/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes mécaniques → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Contrainte de déplacement** dans le menu.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la contrainte doit être appliquée, qui peut être un sommet (coin), une arête ou une face.
3.  Choisissez un degré de liberté ou prescrivez un déplacement.

## Remarques

1.  La contrainte utilise la carte \*BOUNDARY dans CalculiX. La fixation d\'un degré de liberté est expliquée ici <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html> et la prescription d\'un déplacement pour un degré de liberté est expliquée ici <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/fr
