---
- GuiCommand:/fr
   Name:FEM MaterialMechanicalNonlinear
   Name/fr:FEM Matériau mécanique non linéaire
   MenuLocation:Model → Materials →  Matériau mécanique non linéaire
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM MaterialMechanicalNonlinear/fr

## Description

Ajoute un modèle de matériau mécanique non linéaire. Actuellement, seule la plasticité avec durcissement simple est disponible.

## Utilisation

1.  Pour définir un modèle de matériau mécanique non linéaire, procédez comme suit :
    -   Ajoutez d\'abord le **<img src="images/Fem-add-material.svg" width=16px> [Materiau pour solide](FEM_MaterialSolid/fr.md)** et sélectionnez-le.
    -   Cliquez sur le bouton **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [FEM Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md)** ou choisissez l\'option **Model → Materials → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Matériau mécanique non linéaire** dans le menu.
2.  Pour modifier un objet Matériau Fluide existant :
    -   Cliquez dessus dans la [Vue en arborescence](Tree_view/fr.md).
    -   Sélectionnez le modèle de matériau (actuellement, seul le durcissement simple est disponible).
    -   Définissez les limites d\'élasticité (contrainte vs déformation plastique). Le premier point doit avoir une déformation plastique nulle spécifiée. Actuellement, seuls 3 points d\'écoulement peuvent être définis.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialMechanicalNonlinear/fr
