---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintTemperature
   Name/fr: FEM Condition limite de température
   MenuLocation: Modèle , Conditions limites et charges thermiques , Condition limite de température
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintTemperature/fr

## Description

Définit une condition limite de température ou, en option, une charge de flux thermique concentré.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Condition limite de température](FEM_ConstraintTemperature/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges thermiques → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Condition limite de température
**
2.  Appuyez sur le bouton **Ajouter**.
3.  Dans la [vue 3D](3D_view/fr.md), sélectionnez les objets auxquels la condition limite doit être appliquée, qui peuvent être des sommets, des arêtes ou des faces. Vous pouvez également appuyer sur le bouton **Supprimer** et cliquez sur les objets que vous souhaitez supprimer de la sélection.
4.  Choisissez le type de contrainte et spécifiez son paramètre :
    -   *Temperature* (par défaut) : condition limite de température, entrez la *Température* (K),
    -   *CFlux* : charge de flux de chaleur concentré, entrez le *Flux de chaleur concentré* (mW). Cette valeur sera divisée par le nombre de nœuds de l\'entité géométrique sous-jacente pour obtenir un flux total d\'une magnitude donnée sur cette entité.



## Remarques

-   La condition limite de température utilise la carte \*BOUNDARY dans CalculiX. Elle est expliquée à l\'adresse suivante : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>
-   L\'option de flux de chaleur concentré utilise la carte \*CFLUX dans CalculiX : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node168.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/fr
