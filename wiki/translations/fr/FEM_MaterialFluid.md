---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM MaterialFluid
   Name/fr: FEM Matériau pour fluide
   MenuLocation: Modèle , Matériaux , Matériau pour fluide
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Elmer
}}
---

# FEM MaterialFluid/fr

## Description

Crée un matériau pour le fluide.

![](images/FEMMaterialFluidProperties.png ) 
*Le panneau des tâches des matériaux FEM*



## Utilisation

1.  Pour créer un nouvel objet MaterialFluid, effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton **<img src="images/FEM_MaterialFluid.svg" width=16px> [Matériau pour fluide](FEM_MaterialFluid/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Matériaux → <img src="images/FEM_MaterialFluid.svg" width=16px> Matériau pour fluide** du menu.
2.  Pour modifier un objet MaterialFluid existant :
    -   Double-cliquez dessus dans la [vue en arborescence](Tree_view/fr.md).
3.  Le panneau des tâches de matériau FEM s\'ouvre.
4.  Sélectionnez un type de fluide dans la liste déroulante. Pour la dynamique des fluides numérique (CFD), *Air* ou *Water* sont des options courantes.
5.  Vous pouvez également cliquer sur le bouton **Utiliser ce panneau de tâches** pour modifier les propriétés telles que la densité, la viscosité cinématique, la conductivité thermique, etc.
6.  Si vous appliquez le fluide à l\'ensemble de l\'objet, ne sélectionnez aucune entité géométrique (laissez la liste de référence vide). Le fluide sera appliqué à l\'ensemble du modèle. Sinon, attribuez manuellement le fluide à des domaines particuliers du modèle en sélectionnant certains d\'entre eux pour chaque matériau inséré. Si vous faites cela, ne laissez aucun domaine de votre modèle sans fluide attribué.
7.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/fr
