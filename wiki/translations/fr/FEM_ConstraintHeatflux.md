---
- GuiCommand   */fr
   Name   *FEM ConstraintHeatflux
   Name/fr   *FEM Contrainte de flux de chaleur
   MenuLocation   *Modèle → Contraintes thermiques → Contrainte de flux de chaleur
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ConstraintHeatflux/fr

## Description

Cette contrainte spécifie l\'échange de chaleur (transfert de chaleur par film) d\'une surface à la température *T* et avec un coefficient de film *h* et une température ambiante *T~0~*. Le flux de chaleur convective *q* satisfera   * ***q = h(T -T~0~)***

## Utilisation

1.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Contrainte de flux de chaleur](FEM_ConstraintHeatflux/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes thermiques → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Contrainte de flux de chaleur** dans le menu.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez la ou les faces auxquelles la contrainte doit être appliquée.
3.  Entrez la température de surface, le coefficient de transfert de chaleur et la température ambiante.

## Remarques

-   La contrainte utilise la carte \*FILM dans CalculiX.
-   La contrainte heatflux est expliquée à <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/fr
