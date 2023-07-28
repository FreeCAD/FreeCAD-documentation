---
- GuiCommand:/fr
   Name:FEM ConstraintFlowVelocity
   Name/fr:FEM Contrainte de vitesse d'écoulement
   MenuLocation:Modèle → Contraintes du fluide → Contrainte de vitesse d'écoulement
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte vitesse d'écoulement initiale](FEM_ConstraintInitialFlowVelocity/fr.md)
---

# FEM ConstraintFlowVelocity/fr



## Description

Applique une vitesse d\'écoulement comme condition limite à un bord en 2D ou à une face en 3D.



## Utilisation

1.  Appuyez sur le bouton **<img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> '''Contrainte de vitesse d'écoulement'''** ou sélectionnez le menu **Modèle → Contraintes du fluide → <img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> Contrainte de vitesse d'écoulement**.
2.  Sélectionnez les arêtes ou les faces cibles.
3.  Appuyez sur le bouton **Ajouter**.
4.  Décocher *non spécifié* pour activer les champs nécessaires à l\'édition.
5.  Définir les valeurs de vitesse ou ({{Version/fr|0.21}}) spécifier une formule.



## Formules


{{Version/fr|0.21}}

Il est possible de définir une vitesse en spécifiant le profil de vitesse par une formule. Dans ce cas, le solveur définit les vitesses aux différentes positions en fonction du profil.

Pour spécifier par exemple le profil de la vitesse

$\quad
v_{x} (y)=6\left(y-1\right)\left(2-y\right)$

avec $y\in[1;2]$ (en supposant que, par exemple, la paroi d\'un tuyau se trouve à y = 1 m et à y = 2 m)

entrez ceci dans le champ *Formula*: ` Variable Coordinate 2; Real MATC "6*(tx-1)*(2-tx)"`

Ce code a la syntaxe suivante :

-   le préfixe *Variable* spécifie que la vitesse n\'est pas une constante mais une variable
-   la variable pour calculer la vitesse est *Coordinate 2*, c\'est à dire y
-   les valeurs de vitesse sont retournées sous forme de *Real* (valeur à virgule flottante)
-   *MATC* est le préfixe du solveur Elmer que le code suivant est une formule
-   *tx* est toujours le nom de la variable dans les formules *MATC*, peu importe que *tx* dans notre cas soit en fait *y*

Le fait que *y* ne soit compris que dans l\'intervalle $y\in[1;2]$ est dû au fait que *MATC* n\'évalue que l\'intervalle *tx* où le résultat est positif. Ce comportement est un peu spécial mais présente l\'avantage de ne pas avoir à spécifier l\'intervalle manuellement.

Il est également possible d\'utiliser plus d\'une variable. Voir par exemple la définition des rotations dans la [contrainte de déplacement](FEM_ConstraintDisplacement/fr#Rotations.md).



## Remarques

-   Toute composante vectorielle qui devrait être le résultat du solveur doit être définie comme *Non spécifié*.
-   Si la face ou l\'arête cible n\'est pas alignée sur le système de coordonnées cartésiennes principal, il est possible de définir l\'option **Normal à la limite**.

    :   Si l\'option **Normal à la limite** est cochée, le vecteur normal à l\'arête ou à la face sélectionnée est X et il sera orienté à l\'opposé du domaine du maillage.
    :   Par exemple, si un flux d\'air de 20 mm/s doit entrer dans le domaine, alors avec **Normal à la limite** il faut entrer -20 mm/s dans le champ **Vitesse x**.

-   Pour une paroi avec une condition d\'adhérence, définir toutes les composantes de la vitesse à 0.
-   Pour une condition de symétrie, définir l\'écoulement à (0, Non spécifié, Non spécifié) si **Normal à la limite** est coché.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/fr
