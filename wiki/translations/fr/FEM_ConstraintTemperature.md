---
 GuiCommand:
   Name: FEM ConstraintTemperature
   Name/fr: FEM Condition limite de température
   MenuLocation: Modèle , Conditions limites et charges thermiques , Condition limite de température
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM ConstraintTemperature/fr

## Description

Définit une condition limite de température ou, en option, une charge de flux thermique concentré.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Condition limite de température](FEM_ConstraintTemperature/fr.md)**.
    -   Sélectionner l\'option **Modèle → Conditions limites et charges thermiques → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Condition limite de température
**
2.  Dans la [vue 3D](3D_view/fr.md), sélectionner les objets auxquels la condition limite doit être appliquée, qui peuvent être des sommets (coins), des arêtes ou des faces.
3.  Rentrer une température à appliquer aux objets.



### Options

Par défaut, cette fonction définit une condition limite de température. En utilisant l\'option **Flux de chaleur concentré**, on peut spécifier une valeur de flux de chaleur (en mW) à chaque noeud appartenant à l\'entité géométrique sélectionnée.



## Remarques

-   La condition limite de température utilise la carte \*BOUNDARY dans CalculiX. Elle est expliquée à l\'adresse suivante : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>
-   L\'option de flux de chaleur concentré utilise la carte \*CFLUX dans CalculiX : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node168.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/fr
