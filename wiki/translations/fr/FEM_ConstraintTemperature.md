---
- GuiCommand:/fr
   Name:FEM ConstraintTemperature
   Name/fr:FEM Contrainte température
   MenuLocation:Model → Thermal Constraints → Constraint temperature
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

## Description

Crée une contrainte FEM pour une condition de limite de température.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Create a FEM constraint for a temperature...](FEM_ConstraintTemperature.md)**.
    -   Sélectionnez l\'option **Model → Thermal Constraints → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Constraint temperature
**
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez les objets auxquels la contrainte doit être appliquée, qui peuvent être des sommets (coins), des arêtes ou des faces.
3.  Entrez une température à appliquer aux objets.

## Remarques

1.  La contrainte utilise la carte \*BOUNDARY dans CalculiX. La contrainte temperature est expliquée à <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>





{{FEM Tools navi

}}  
