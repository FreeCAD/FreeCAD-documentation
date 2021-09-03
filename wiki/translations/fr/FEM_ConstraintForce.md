---
- GuiCommand:/fr
   Name:FEM ConstraintForce
   Name/fr:FEM Contrainte de force
   MenuLocation:Model → Mechanical Constraints → Constraint force
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:
   SeeAlso:[FEM Contrainte de pression](FEM_ConstraintPressure/fr.md)
---

## Description

Cette commande applique une force de valeur donnée \[N\] à la géométrie cible sélectionnée.

## Utilisation

1\) Appliquer une force dans une direction normale sur une face

-   -   Dans l\'atelier FEM, cliquez sur <img alt="Constraint Force" src=images/FEM_ConstraintForce.svg  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** ouvrir la boîte de dialogue des propriétés de contrainte de contrainte

![](images/FEMForceConstraintProperties.PNG )

-   -   Si vous avez affiché Mesh, vous devez le masquer (sélectionnez l'objet maillé et appuyez sur **spacebar**ou faites un clic droit et sélectionnez **Hide item**) et affichez le modèle d\'origine.
    -   Cliquez sur une \"face\" auquel une force doit être appliquée. Il apparaîtra dans la liste des objets géométriques.
    -   Remplissez **Line load** avec une valeur de force dans \[N\] (attention: *Pas* dans \[N/m\])

![](images/ApplyingForceToFace.PNG )

-   -   
        **Direction**
        
        :Dans un cas typique, vous cliquez sur ce champ vide pour appliquer une force en direction normale au visage. Vous pouvez inverser la direction de la force en cliquant sur **Reverse direction**. Dans d\'autres cas, vous devez choisir une face ou un plan qui correspond à la direction de la force (elle peut différer de la face sur laquelle la force est appliquée).

    -   Cliquez **Close** pour terminer la boîte de dialogue et créer l\'object **<img src=images/FEM_ConstraintForce.png style="width:24px"> ConstraintForce**

2\) Appliquer une force pour aligner dans la direction sélectionnée

-   -   Dans l\'espace de travail FEM, cliquez sur <img alt="Constraint Force" src=images/FEM_ConstraintForce.svg  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** ouvrir la boîte de dialogue des propriétés de contrainte de contrainte

    -   Si vous avez affiché Mesh, vous devez le masquer (sélectionnez l'objet maillé et appuyez sur **spacebar** ou faites un clic droit et sélectionnez **Hide item**) et affichez le modèle d\'origine.

    -   Cliquez sur un *segment de ligne* auquel une force doit être appliquée. Il apparaîtra dans la liste des objets géométriques.

    -   Complétez **Area load** avec une valeur de force dans \[N\]

    -   
        **Direction**
        
        : Maintenant, avec le segment de ligne sélectionné, il est probable que la force soit appliquée dans une mauvaise direction. Nous devons spécifier la direction en cliquant sur le bouton **Direction**, puis en cliquant sur une face pointant de manière normale dans la direction de la force (ou dans la direction inversée). Encore une fois, vous pouvez inverser la direction de la force en cliquant sur **Reverse direction**.

![](images/FEMforceonline.PNG )

-   -   Cliquez sur **Close** pour terminer la boîte de dialogue et créer l\'objet **<img src=images/FEM_ConstraintForce.png style="width:24px"> ConstraintForce**





{{FEM Tools navi

}}  
