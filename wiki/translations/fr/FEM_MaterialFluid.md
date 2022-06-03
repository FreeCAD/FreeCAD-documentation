---
- GuiCommand   */fr
   Name   *FEM MaterialFluid
   Name/fr   *FEM Matériau pour fluide
   MenuLocation   *Modèle → Matériaux → Matériau pour le fluide
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM MaterialFluid/fr

## Description

Ajoute des propriétés de fluide à une pièce.

![](images/FEMMaterialFluidProperties.png ) 
*Le panneau des tâches des matériaux FEM*

## Utilisation

1.  Pour créer un nouvel objet MaterialFluid, effectuez l\'une des opérations suivantes   *
    -   Appuyez sur le bouton **<img src="images/FEM_MaterialFluid.svg" width=16px> [Matériau pour le fluide](FEM_MaterialFluid/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Matériaux → <img src="images/FEM_MaterialFluid.svg" width=16px> Matériau pour le fluide** dans le menu.
2.  Pour modifier un objet MaterialFluid existant   *
    -   Double-cliquez dessus dans la [Vue en arborescence](Tree_view/fr.md).
3.  Le panneau des tâches de matériau FEM s\'ouvre.
4.  Sélectionnez un type de fluide. Pour la dynamique des fluides par calcul (CFD), **Air** ou **Water** sont des options typiques.
5.  Si vous appliquez du fluide à l\'ensemble de l\'objet, ne sélectionnez aucune entité géométrique (laissez la liste de références vide). Le fluide sera appliqué à l\'ensemble du modèle. Sinon, attribuez manuellement un fluide à des domaines de modèle particuliers en sélectionnant certains d\'entre eux pour chaque matériau inséré. Si vous faites cela, ne laissez aucun domaine de votre modèle sans fluide affecté.
6.  Vous pouvez ajuster les propriétés des fluides telles que la densité, la viscosité cinématique, la conductivité thermique, etc., quelques fluides clés sont déjà affectés dans la liste et ils ne nécessitent aucun ajustement.
7.  Si vous apportez des modifications, vous pouvez enregistrer votre matériel personnalisé.
8.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/fr
