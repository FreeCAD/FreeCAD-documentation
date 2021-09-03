---
- GuiCommand:/fr
   Name:FEM ConstraintHeatflux
   Name/fr:FEM Contrainte flux de chaleur
   MenuLocation:Model → Thermal Constraints → Constraint heatflux
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

## Description

Cette contrainte spécifie l\'échange de chaleur (transfert de chaleur par film) d\'une surface à la température *T* et avec un coefficient de film *h* et une température ambiante \'\'T~0~ \'\'. Le flux de chaleur convective *q* satisfera: ***q = h(T -T~0~)***

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Create a FEM contrainst for a heatflux...](FEM_ConstraintHeatflux/fr.md)**.
    -   Sélectionnez l\'option **Model → Thermal Constraints → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Constraint heatflux** dans le menu.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez la ou les faces auxquelles la contrainte doit être appliquée.
3.  Entrez la température de surface, le coefficient de film et la température ambiante souhaités.

## Remarques

1.  La contrainte utilise la carte \*FILM dans CalculiX. La contrainte heatflux est expliquée à <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>





{{FEM Tools navi

}}  
