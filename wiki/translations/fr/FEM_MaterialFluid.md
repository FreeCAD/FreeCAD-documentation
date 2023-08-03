---
 GuiCommand:
   Name: FEM MaterialFluid
   Name/fr: FEM Matériau pour fluide
   MenuLocation: Modèle , Matériaux , Matériau pour fluide
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM MaterialFluid/fr

## Description

Ajoute des propriétés de fluide à une pièce.

![](images/FEMMaterialFluidProperties.png ) 
*Le panneau des tâches des matériaux FEM*



## Utilisation

1.  Pour créer un nouvel objet MaterialFluid, effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton **<img src="images/FEM_MaterialFluid.svg" width=16px> [Matériau pour fluide](FEM_MaterialFluid/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Matériaux → <img src="images/FEM_MaterialFluid.svg" width=16px> Matériau pour fluide** dans le menu.
2.  Pour modifier un objet MaterialFluid existant :
    -   Double-cliquez dessus dans la [Vue en arborescence](Tree_view/fr.md).
3.  Le panneau des tâches de matériau FEM s\'ouvre.
4.  Sélectionnez un type de fluide. Pour la dynamique des fluides numériques (CFD), **Air** ou **Water** sont des options typiques.
5.  Dans la mesure où vous appliquez le fluide à l\'ensemble de l\'objet, ne sélectionnez aucune entité géométrique (laissez la liste des références vide). Le fluide sera appliqué à l\'ensemble du modèle. Sinon, attribuez manuellement le fluide à des domaines particuliers du modèle en sélectionnant certains d\'entre eux pour chaque matériau inséré, si vous faites cela, ne laissez aucun domaine de votre modèle sans fluide attribué.
6.  Vous pouvez ajuster les propriétés du fluide telles que la densité, la viscosité cinématique, la conductivité thermique, etc., quelques fluides clés sont déjà assignés dans la liste et ils n\'ont pas besoin d\'être modifiés.
7.  Si vous apportez des modifications, vous pouvez enregistrer votre matériau personnalisé.
8.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/fr
