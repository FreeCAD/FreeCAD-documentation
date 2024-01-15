---
 GuiCommand:
   Name: FEM SolverElmer
   Name/fr: FEM Solveur Elmer
   MenuLocation: Résolution , Solveur Elmer
   Workbenches: FEM_Workbench/fr
   Shortcut: **S** **E**
   SeeAlso: FEM_SolverElmer_SolverSettings/fr, FEM_SolverCalculixCxxtools/fr, FEM_SolverZ88, FEM_tutorial/fr
---

# FEM SolverElmer/fr

## Description

[Elmer](https://www.elmerfem.org) est un logiciel de simulation multiphysique open source principalement développé par le CSC - IT Center for Science (CSC). Le développement d\'Elmer a commencé en 1995 en collaboration avec des universités finlandaises, des instituts de recherche et l\'industrie. Après sa publication open source en 2005, l\'utilisation et le développement d\'Elmer sont devenus internationaux.

Elmer comprend des modèles physiques de dynamique des fluides, de mécanique des structures, d\'électromagnétisme, de transfert de chaleur et d\'acoustique, par exemple. Ceux-ci sont décrits par des équations différentielles partielles qu\'[Elmer](https://www.csc.fi/web/elmer) résout par la méthode des éléments finis (FEM).

La création de l\'objet SolverElmer dans le conteneur Analysis de FreeCAD donne accès aux équations Elmer pour une analyse simple ou multiphysique.

Dans la mesure où FreeCAD dispose déjà d\'une intégration poussée de <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:24px;"> [Calculix](FEM_SolverCalculixCxxtools/fr.md) et <img alt="" src=images/FEM_SolverZ88.svg  style="width:24px;"> [Z88](FEM_SolverZ88/fr.md) comme solveurs pour l\'analyse mécanique et thermomécanique, Elmer sera privilégié pour la dynamique des fluides numérique (CFD), la chaleur, l\'électrostatique et l\'électrodynamique. Il peut également être utilisé pour l\'analyse par éléments finis mécanique à travers l\'équation d\'élasticité ou toute combinaison des équations susmentionnées. Cette combinaison fait d\'Elmer le choix privilégié pour les analyses multi-physiques.

## Installation

Elmer nécessite que deux composants soient interfacés avec FreeCAD :

-   ElmerGrid est l\'interface gérant les maillages
-   ElmerSolver gère le calcul.

Il existe des programmes autonomes pour ces deux applications mais leur installation et leur utilisation dépassent le cadre de l\'intégration de FreeCAD.

1.  Téléchargez et installez la version la mieux adaptée à votre système d\'exploitation ([Windows](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/windows/) ou [Linux](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/linux/Readme1st.txt)). Il est recommandé d\'installer la version `mpi` pour bénéficier d\'un support multi-cœur du CPU. ({{Version/fr|0.21}}).
2.  Dans FreeCAD, allez dans **Edition → Préférences → FEM → Elmer**.
3.  Dans les [préférences de FEM](FEM_Preferences/fr#Elmer.md), définissez le chemin d\'accès correct pour `ElmerGrid` et `ElmerSolver`, ou {{VersionPlus/fr|0.21}} : définissez le chemin d\'accès pour `ElmerSolver_mpi` au lieu de `ElmerSolver` pour qu\'Elmer utilise tous les cœurs de processeur disponibles.

    :   ![Onglet Elmer dans les préférences de FEM](images/Preferences-ElmerPath.png )

    :   
        
*Menu de dialogue des préférences Elmer montrant les champs pour localiser les binaires Elmer importants sur le système d'exploitation Windows*
        
        .

Vous êtes prêt à utiliser Elmer dans FreeCAD.


{{VersionMinus/fr|0.19}}

: Maintenant démarrez FreeCAD et changez le schéma d\'unités en *MKS* dans les [préférences](Preferences_Editor/fr#Unit.C3.A9s.md). Voir [Remarques](#Remarques.md).



## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md)
2.  Créez un [conteneur d\'analyse](FEM_Analysis/fr.md) en appuyant sur l\'icône <img alt="" src=images/FEM_Analysis.svg  style="width:22px;">.
3.  Créez un solveur FEM pour Elmer, en appuyant sur l\'icône <img alt="" src=images/FEM_SolverElmer.svg  style="width:22px;">.
    -   Remarque : une analyse réussie nécessite au moins un modèle (2D ou 3D), un matériau ([FEM Fluide](FEM_MaterialFluid/fr.md) ou [FEM Solide](FEM_MaterialSolid/fr.md)), un [maillage Gmsh](FEM_MeshGmshFromShape/fr.md), des équations et des conditions aux limites

    :   ![](images/Elmer_typical_file_tree.png )

    :   
        
*Exemple de [vue en arborescence](Tree_view/fr.md) une fois qu'un solveur pour Elmer est activé*
        
4.  Modifiez les paramètres du solveur dans l\'onglet **Data** de l\'[éditeur de propriétés](Property_editor/fr.md) de l\'objet SolverElmer dans le modèle [vue en arborescence](Tree_view/fr.md)
5.  Double-cliquez sur l\'objet **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** pour préparer une analyse

    :   <img alt="" src=images/ElmerSolver_TaskPanel.png  style="width:300px;">

    :   
        
*Menu de dialogue pour exécuter une analyse Elmer*
        
6.  Sélectionnez le chemin vers lequel l\'analyse écrira en cliquant sur **...**
7.  Cliquez sur **Ecrire** pour écrire les fichiers de cas dans le répertoire sélectionné précédemment
8.  Cliquez sur **Lancer** pour démarrer l\'analyse



### Équations

-   Pour effectuer l\'analyse d\'un comportement physique particulier, une équation doit être utilisée (écoulement, chaleur, électrostatique\...).
-   Disambiguation : le terme *Équation* est utilisé dans FreeCAD pour décrire les différents mécanismes physiques, le terme *Solveur* est utilisé dans tous les documents Elmer. Ainsi, lorsqu\'on utilise dans FreeCAD l\'\"Équation d\'écoulement\", en réalité Elmer utilise le \"Solveur d\'écoulement\" pour trouver une solution à l\'équation de Navier-Stokes.
-   Une ou plusieurs équations peuvent être utilisées en même temps avec Elmer en ajoutant simplement l\'objet équation sous l\'objet SolverElmer, réalisant ainsi des analyses multi-physiques :

1.  Cliquez sur l\'objet **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** dans le modèle de la [vue en arborescence](Tree_view/fr.md)
2.  Sélectionnez une ou plusieurs des équations disponibles :
    -   <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Équation de déformation](FEM_EquationDeformation/fr.md)
    -   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Équation d\'élasticité](FEM_EquationElasticity/fr.md)
    -   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Équation force électrique](FEM_EquationElectricforce/fr.md)
    -   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Équation électrostatique](FEM_EquationElectrostatic/fr.md)
    -   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Équation d\'écoulement](FEM_EquationFlow/fr.md)
    -   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Équation de flux](FEM_EquationFlux/fr.md)
    -   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Équation de chaleur](FEM_EquationHeat/fr.md)
    -   <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [Équation magnétodynamique](FEM_EquationMagnetodynamic/fr.md)
    -   <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [Équation magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md)



### Paramètres du solveur 

-   En fonction des équations utilisées, vous devez modifier les paramètres par défaut du solveur. Ils sont expliqués à la page [Paramètres du solveur d\'Elmer](FEM_SolverElmer_SolverSettings/fr.md).
-   Le solveur effectue par défaut une simulation en régime permanent. Pour effectuer une simulation transitoire (comment le modèle se comporte au cours du le temps), voir la section *Pas de temps (analyses transitoires)* dans les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr#Pas_de_temps_(analyses_transitoires).md).



### Visualisation

Les résultats du solveur Elmer sont affichés dans des objets [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). (Les [objets résultats](FEM_ResultShow/fr.md) ne sont pas possibles).


{{Version/fr|0.21}}

Pour les analyses transitoires, vous obtenez un pipeline de résultats pour chaque pas de temps. Pour les éditer tous en même temps, sélectionnez-les dans la [vue en arborescence](Tree_view/fr.md) et définissez les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md). Pour réaliser des animations de la progression temporelle, la meilleure méthode consiste actuellement à :

-   Cacher la vue du premier résultat.
-   Sélectionner un objet de votre choix dans la vue en arborescence, mais pas un objet de pipeline.
-   Passer la souris sur les pipelines.

Le résultat est une animation comme celle-ci :

![](images/ElmerSolver_TransientAnalysis.gif )



## Remarques

-   **Important** : afin d\'obtenir des résultats raisonnables et de pouvoir échanger les fichiers d\'entrée Elmer (nommés *case.sif*) avec d\'autres utilisateurs, toutes les valeurs dans les fichiers d\'entrée doivent être en unités SI. Dans la version 0.19 de FreeCAD et les versions antérieures, ce n\'est le cas que si vous utilisez le schéma d\'unités MKS dans les [préférences](Preferences_Editor/fr#Unit.C3.A9s.md).
-   Les paramètres du solveur et des équations sont définis indépendamment via l\'onglet **Data** de l\'[éditeur de propriétés](Property_editor/fr.md) de leurs objets respectifs dans la [vue en arborescence](Tree_view/fr.md).
-   Chaque équation aura une priorité. Par exemple, si vous essayez de voir l\'effet d\'un flux convectif d\'air chaud, l\'équation pour le débit doit être résolue avec une priorité plus élevée que la chaleur, sinon le solveur résoudra d\'abord la chaleur par conduction puis le débit.
-   Cas 2D vs 3D : Elmer peut être utilisé pour résoudre des cas 2D et 3D. Cependant, lors de la définition d\'un cas 2D, les faces doivent être mappées dans le plan XY de FreeCAD, sinon le solveur essaiera de calculer un cas 3D sur une face, et les vecteurs normaux seront sous-définis. De plus amples informations peuvent être trouvées dans les forums FreeCAD : <https://forum.freecadweb.org/viewtopic.php?f=18&t=48175>.



## Documentation

Le lien suivant donne accès à la [documentation complète pour Elmer](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/). Cela inclut les manuels ainsi que les tutoriels. Notez que la documentation et les fichiers ajoutés avec \"gui\" concernent généralement l\'utilisation de l\'interface graphique Elmer et non l\'implémentation FreeCAD d\'Elmer.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverElmer/fr
