---
 GuiCommand:
   Name: FEM ConstraintHeatflux
   Name/fr: FEM Charge de flux de chaleur
   MenuLocation: Modèle , Conditions limites et charges thermiques , Charge de flux de chaleur
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM ConstraintHeatflux/fr

## Description

Cette commande définit une charge de flux de chaleur convective sur une surface à une température *T* avec un coefficient de film *h* et avec la température de l\'environnement (puits) *T~0~*. Le flux de chaleur convective *q* satisfera: ***q = h(T -T~0~)***. En outre, il est possible de définir une charge de flux régulier de chaleur de surface.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Charge de flux de chaleur](FEM_ConstraintHeatflux/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges thermiques → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Charge de flux de chaleur** du menu.
2.  Dans la [vue 3D](3D_view/fr.md), sélectionnez la ou les faces auxquelles la charge de flux de chaleur doit être appliquée.
3.  Entrez le coefficient de transfert de chaleur et la température ambiante souhaités.



### Options

Par défaut, cette fonctionnalité définit un flux de chaleur convectif. En utilisant l\'option **Flux de chaleur de surface**, on peut spécifier une valeur de flux de chaleur en Watts par surface (W/m\^2).



## Remarques

-   La charge de flux de chaleur utilise le jeu de paramètres \*FILM dans CalculiX. Elle est expliquée à l\'adresse suivante : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>
-   L\'option de flux de chaleur de surface utilise la carte \*DFLUX dans CalculiX : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/fr
