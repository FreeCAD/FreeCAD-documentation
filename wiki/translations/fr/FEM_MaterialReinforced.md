---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM MaterialReinforced
   Name/fr: FEM Matériau renforcé
   MenuLocation: Modèle , Matériaux , Matériau renforcé 
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM MaterialReinforced/fr

## Description

Crée un matériau matriciel renforcé. Il combine un matériau de matrice (par exemple le béton) et un matériau de renfort (par exemple l\'acier).



## Utilisation

1.  Pour créer un nouvel objet Matériau renforcé, procédez comme suit :
    -   Cliquez sur le **<img src="images/FEM_MaterialReinforced.svg" width=16px> [Matériau renforcé (type béton)](FEM_MaterialReinforced/fr.md)** ou choisissez l\'option **Modèle → Matériaux → <img src="images/FEM_MaterialReinforced.svg" width=16px> Matériau renforcé (typebéton)** du menu.
2.  Pour modifier un objet Matériau renforcé existant :
    -   Double-cliquez sur l\'objet dans la [vue en arborescence](Tree_view/fr.md).
3.  Sélectionnez le matériau de la matrice.
4.  Vous pouvez appuyé sur le bouton **Éditer** pour modifier ses propriétés. Les propriétés suivantes du matériau doivent être définies : Module de Young, coefficient de Poisson, résistance à la compression et angle de frottement.
5.  Sélectionnez le matériau de renfort.
6.  Vous pouvez appuyé sur le bouton **Éditer** pour modifier ses propriétés. Une limite d\'élasticité doit être définie.



## Remarques

-   Dans les paramètres du solveur CalculiX, il faut régler la non-linéarité du matériau sur linéaire si [FEM Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md) n\'est pas utilisé.
-   Plus d\'informations sur cette fonctionnalité, et un exemple de son utilisation, peuvent être trouvés sur la page [FEM Analyse du béton armé](Analysis_of_reinforced_concrete_with_FEM/fr.md).
-   Pour un tutoriel vidéo (basé sur le [tutoriel FEM](FEM_tutorial/fr.md)) qui utilise cet outil, regardez : [FEM MaterialReinforced tutorial](https://www.youtube.com/watch?v=SZTIqhfCSVc).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialReinforced/fr
