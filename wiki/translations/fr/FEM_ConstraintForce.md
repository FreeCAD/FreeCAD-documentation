---
 GuiCommand:
   Name: FEM ConstraintForce
   Name/fr: FEM Charge d'effort
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Charge d'effort
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintPressure/fr
---

# FEM ConstraintForce/fr

## Description

Cette commande applique une force d\'une valeur donnée \[N\] à la géométrie sélectionnée.



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintForce.svg" width=16px> [Charge d'effort](FEM_ConstraintForce/fr.md)**.
    -   Sélectionner l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintForce.svg" width=16px> Charge d'effort** du menu.
2.  L\'objet Mesh sera automatiquement caché et laissera apparaître le modèle original. Si l\'objet Mesh est toujours visible, effectuer l\'une des opérations suivantes pour le masquer :
    -   Sélectionner l\'objet Mesh dans la [vue en arborescence](Tree_view/fr.md) et appuyez sur la **barre d'espace**.
    -   Cliquer avec le bouton droit de la souris sur l\'objet Mesh dans la [vue en arborescence](Tree_view/fr.md) et sélectionner **Cacher l'élément** dans son menu contextuel.
3.  La boîte de dialogue **Paramètres des fonctions d'analyse** dans le [panneau des tâches](Task_panel/fr.md) est également ouverte.
4.  Appuyer sur le bouton **Ajouter** et sélectionnez une ou plusieurs *faces*, *arêtes* ou *sommets* dans la [vue 3D](3D_view/fr.md) pour appliquer la force. Les éléments sélectionnés apparaîtront dans la liste des objets géométriques.
5.  Vous pouvez également appuyer sur le bouton **Supprimer** et désélectionner un ou plusieurs des éléments sélectionnés dans la [vue 3D](3D_view/fr.md). Les éléments désélectionnés seront supprimés de la liste des objets géométriques.
6.  Vous pouvez modifier la valeur **Charge [N]**.
7.  Vous pouvez sélectionner une face ou une arête et appuyez sur le bouton **Direction** pour modifier la direction de la force. Dans un cas typique, vous laisserez ce champ vide pour appliquer la force dans la direction normale.
8.  Vous pouvez cocher la case **Inverser la direction** pour inverser la direction de la force.
9.  Cliquer sur **OK** pour terminer.

![](images/FEM_ConstraintForce_example.JPG )



## Remarques

-   La force définie est appliquée uniformément aux objets sélectionnés. Par exemple, si vous définissez une charge de force de 200 N appliquée à deux faces ayant la même surface, chaque face sera chargée uniformément de 100 N.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintForce/fr
