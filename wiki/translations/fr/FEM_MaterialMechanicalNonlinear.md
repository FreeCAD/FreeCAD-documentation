---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM MaterialMechanicalNonlinear
   Name/fr: FEM Matériau mécanique non linéaire
   MenuLocation: Modèle , Matériaux ,  Matériau mécanique non linéaire
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM MaterialMechanicalNonlinear/fr

## Description

Crée un matériau mécanique non linéaire. Actuellement, seule la plasticité avec un durcissement simple (isotrope) est disponible. {{Version/fr|1.0}} : l\'écrouissage cinématique est également disponible.



## Utilisation

1.  Pour créer un objet matériau mécanique non linéaire, procédez comme suit :
    -   Ajouter d\'abord un **<img src="images/FEM_MaterialSolid.svg" width=16px> [Matériau pour solide](FEM_MaterialSolid/fr.md)** et sélectionnez-le.
    -   Cliquer sur le bouton **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md)** ou choisissez l\'option **Modèle → Matériaux → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Matériau mécanique non linéaire** dans le menu.
2.  Pour modifier un objet Matériau mécanique non linéaire existant :
    -   Sélectionner le dessus dans la [vue en arborescence](Tree_view/fr.md).
    -   Sélectionner le modèle de matériau (durcissement isotrope (simple) ou {{Version/fr|1.0}} : écrouissage cinématique).
    -   Définir les limites d\'élasticité (contrainte \[MPa\] en fonction de la déformation plastique). Le premier point doit avoir une déformation plastique nulle. Appuyez sur le bouton **...** à côté de **Yield Points** pour saisir les points à l\'aide d\'une liste intuitive. La syntaxe est décrite dans la section [Remarques](##Remarques.md).



## Remarques

-   Dans FreeCAD 0.19 et les versions antérieures, seules 3 points de contrôle peuvent être spécifiés. Depuis la version 0.20, une liste de points de contrôle peut contenir autant de points de contrôle que nécessaire.
-   La syntaxe devrait être :

:   
    
```python
    stress_1, 0
    stress_2, plastic_strain_2
    ...
    
```
    





:   Avec le point comme séparateur décimal puisque c\'est ce qu\'utilise CalculiX.





:   Par exemple pour définir un modèle bilinéaire avec trempe pour l\'acier S275 :





:   
    
```python
    275, 0
    490, 0.2
    
```
    





:   Ou, pour définir une plasticité parfaite sans durcissement pour ce matériau :





:   
    
```python
    275, 0
    
```
    





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialMechanicalNonlinear/fr
