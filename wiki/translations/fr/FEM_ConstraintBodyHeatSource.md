---
- GuiCommand:/fr
   Name:FEM ConstraintBodyHeatSource
   Name/fr:FEM Contrainte source thermique
   MenuLocation: Model → Thermal Constraints → Contrainte de chaleur pour le corps
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

## Description

Définit une température interne en W/kg (et non en J/m³).

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> [Créer une contrainte FEM de type source de chaleur pour un corps](FEM_ConstraintBodyHeatSource/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Model → Thermal Constraints → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Contrainte source de chaleur pour le corps}} dans le menu.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez les objets auxquels la contrainte doit être appliquée, qui peuvent être des sommets (coins), des arêtes ou des faces.
3.  Saisissez une valeur de chaleur spécifique à appliquer aux objets.

## Remarques

-   Pour plus d\'informations, voir [ce fil de forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) et les messages suivants.
-   Des exemples d\'Elmer peuvent également être trouvés dans [Tutoriels Elmer GUI](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).




{{FEM Tools navi

}}  
