---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintBodyHeatSource
   Name/fr: FEM Source de chaleur du corps
   MenuLocation: Modèle , Conditions limites et charges thermiques , Source de chaleur du corps
   Workbenches: FEM_Workbench/fr
   Version: 0.19
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintBodyHeatSource/fr

## Description

Définit une température interne du corps en W/kg.


{{VersionPlus/fr|1.0}}

: peut également définir la source de chaleur en W.



## Utilisation

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Source de chaleur du corps'''** ou sélectionnez **Modèle → Conditions limites et charges thermiques → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Source de chaleur du corps** du menu.

2.  
    {{VersionPlus/fr|0.21}}: appuyez sur le bouton **Ajouter**. pour une analyse 3D, sélectionnez un \"solide\" (corps) de votre modèle. Pour une analyse 2D, sélectionnez une face.

3.  Définissez la valeur :
    -   
        {{VersionMinus/fr|0.20}}
        
        : puisque l\'outil n\'a pas de fenêtre de dialogue, utilisez l\'[éditeur de propriétés](Property_editor/fr.md) et définissez la propriété **Heat Source**.

    -   
        {{Version/fr|0.21}}
        
        : entrez la chaleur du corps en W/kg.

    -   
        {{VersionPlus/fr|1.0}}
        
        : sélectionnez le mode :

        -   *Taux de dissipation* : entrez le taux de dissipation en W/kg.
        -   *Puissance totale* : entrez la puissance totale en W.

## Limitations

-    {{VersionMinus/fr|0.20}}: la source de chaleur du corps est appliquée à l\'ensemble du modèle, c\'est-à-dire à tous les corps de la configuration. Il n\'est pas possible de sélectionner un corps individuellement.

-    {{VersionMinus/fr|0.21}}: cette fonction ne fonctionne qu\'avec le solveur Elmer.



## Remarques

-   Cette fonction ne fonctionne qu\'avec le solveur Elmer.

-   Pour plus d\'informations, voir [ce fil de forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) et les messages suivants. [Ce fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) peut également être utile.

-   Des exemples d\'Elmer peuvent également être trouvés dans [Tutoriels Elmer GUI](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).

-    {{VersionPlus/fr|1.0}}: cette fonction utilise le [jeu de paramètres \*DFLUX de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html).

-    {{VersionPlus/fr|1.0}}: puisque CalculiX s\'attend à ce que le flux de chaleur du corps soit saisi en W/mm\^3 alors que pour Elmer c\'est en W/kg, la conversion de la valeur spécifiée (en W ou W/kg) est faite en interne pour chaque solveur, en utilisant le volume du solide sélectionné et la densité du matériau qui lui est assigné, si nécessaire.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/fr
