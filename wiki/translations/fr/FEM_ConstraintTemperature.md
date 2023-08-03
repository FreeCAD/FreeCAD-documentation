---
 GuiCommand:
   Name: FEM ConstraintTemperature
   Name/fr: FEM Contrainte de température
   MenuLocation: Modèle , Contraintes thermiques , Contrainte de température
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM ConstraintTemperature/fr

## Description

Crée une contrainte FEM pour une condition de limite de température.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Contrainte de température](FEM_ConstraintTemperature/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes thermiques → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Contrainte de température
**
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez les objets auxquels la contrainte doit être appliquée, qui peuvent être des sommets (coins), des arêtes ou des faces.
3.  Entrez une température à appliquer aux objets.

### Options

Par défaut, la contrainte définit une température. En utilisant l\'option **Flux de chaleur concentré**, un flux de chaleur à travers la surface de la face (Watt par surface de face) peut être spécifié.

## Remarques

-   La contrainte de température utilise la carte \*BOUNDARY dans CalculiX. La contrainte de température est expliquée à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/fr
