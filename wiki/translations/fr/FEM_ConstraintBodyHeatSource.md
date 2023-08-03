---
 GuiCommand:
   Name: FEM ConstraintBodyHeatSource
   Name/fr: FEM Contrainte source thermique
   MenuLocation: Modèle , Contraintes thermiques , Contrainte source de chaleur pour le corps
   Workbenches: FEM_Workbench/fr
   Version: 0.19
   SeeAlso: FEM_tutorial/fr
---

# FEM ConstraintBodyHeatSource/fr

## Description

Définit une température interne du corps en W/kg.



## Utilisation

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Contrainte source de chaleur pour le corps'''** ou sélectionnez le menu **Modèle → Contraintes thermiques → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Contrainte source de chaleur pour le corps**.
2.  Définissez la valeur :
    -   
        {{VersionPlus/fr|1.0}}
        
        : pour une analyse 3D, sélectionnez un \"solide\" (corps) de votre modèle. Pour une analyse 2D, sélectionnez une face.

    -   
        {{VersionMinus/fr|0.20}}
        
        : puisque la contrainte n\'a pas de dialogue de tâche, utilisez l\'[Éditeur de propriétés](Property_editor/fr.md) et définissez la propriété **Heat Source**.

## Limitation


{{VersionMinus/fr|0.20}}

: la source de chaleur du corps est appliquée à l\'ensemble du modèle, c\'est-à-dire à tous les corps de la configuration. Il n\'est pas possible de sélectionner un corps individuellement.



## Remarques

-   Cette contrainte ne fonctionne qu\'avec le solveur Elmer.
-   Pour plus d\'informations, voir [ce fil de forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) et les messages suivants. [Ce fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) peut également être utile.
-   Des exemples d\'Elmer peuvent également être trouvés dans [Tutoriels Elmer GUI](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).




{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/fr
