---
 GuiCommand:
   Name: FEM MaterialMechanicalNonlinear
   Name/fr: FEM Matériau mécanique non linéaire
   MenuLocation: Modèle , Matériaux ,  Matériau mécanique non linéaire
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM MaterialMechanicalNonlinear/fr

## Description

Ajoute un modèle de matériau mécanique non linéaire. Actuellement, seule la plasticité avec durcissement simple est disponible.

## Utilisation

1.  Pour définir un modèle de matériau mécanique non linéaire, procédez comme suit :
    -   Ajoutez d\'abord le **<img src="images/Fem-add-material.svg" width=16px> [Matériau pour solide](FEM_MaterialSolid/fr.md)** et sélectionnez-le.
    -   Cliquez sur le bouton **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md)** ou choisissez l\'option **Modèle → Matériaux → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Matériau mécanique non linéaire** dans le menu.
2.  Pour modifier un objet Matériau mécanique non linéaire existant :
    -   Cliquez dessus dans la [Vue en arborescence](Tree_view/fr.md).
    -   Sélectionnez le modèle de matériau (actuellement, seul le durcissement simple est disponible).
    -   Définissez les limites d\'élasticité (contrainte vs déformation plastique). Le premier point doit être spécifié avec une déformation plastique nulle.

## Remarques

-   Dans FreeCAD 0.19 et les versions antérieures, il est possible de spécifier seulement 3 points de rupture. Depuis la version 0.20, cette limitation n\'existe plus et une liste de limites d\'élasticité peut en contenir autant que nécessaire.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialMechanicalNonlinear/fr
