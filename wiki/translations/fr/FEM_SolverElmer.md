---
- GuiCommand:/fr
   Name:FEM SolverElmer
   Name/fr:FEM Solveur Elmer
   MenuLocation:Solve → Solveur Elmer
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:**S** **E**
   SeeAlso:[FEM Solveur CalculiX](FEM_SolverCalculiX/fr.md), [FEM Solveur Z88](FEM_SolverZ88.md), [FEM Tutoriel](FEM_tutorial/fr.md)
---

## Description

[Elmer](https://www.elmerfem.org) est un logiciel de simulation multiphysique open source principalement développé par le CSC - IT Center for Science (CSC). Le développement d\'Elmer a commencé en 1995 en collaboration avec des universités finlandaises, des instituts de recherche et l\'industrie. Après sa publication open source en 2005, l\'utilisation et le développement d\'Elmer sont devenus internationaux.

Elmer comprend des modèles physiques de dynamique des fluides, de mécanique des structures, d\'électromagnétisme, de transfert de chaleur et d\'acoustique, par exemple. Ceux-ci sont décrits par des équations différentielles partielles qu\'[Elmer](https://www.csc.fi/web/elmer) résout par la méthode des éléments finis (MEF).

La création de l\'objet SolverElmer dans le conteneur Analysis de FreeCAD donne accès aux équations Elmer pour une analyse simple ou multiphysique.

Puisque FreeCAD a déjà une intégration étendue de <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:24px;"> [Calculix](FEM_SolverCalculiX/fr.md) et <img alt="" src=images/FEM_SolverZ88.svg  style="width:24px;"> [Z88](FEM_SolverZ88/fr.md) en tant que solveurs pour l\'analyse mécanique et thermo-mécanique, Elmer sera préféré pour la dynamique des fluides computationnelle (CFD), la chaleur, l\'électrostatique, la magnétostatique et les forces électriques. Il peut également être utilisé pour la FEA mécanique via l\'équation d\'élasticité ou toute combinaison des équations susmentionnées.

## Installation

Elmer nécessite que deux composants soient interfacés avec FreeCAD:

-   ElmerGrid est l\'interface gérant les maillages
-   ElmerSolver gère le calcul.

Il existe des programmes autonomes pour ces deux applications mais leur installation et leur utilisation dépassent le cadre de l\'intégration de FreeCAD.

1.  Accédez aux ressources binaires CSC pour Elmer: [binaires](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/) OU [binaires CSC](https://www.csc.fi/web/elmer/binaries)
2.  Téléchargez et installez la version la mieux adaptée à votre système d\'exploitation ([Windows 64](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/windows/) bits ou [Linux](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/linux/Readme1st.txt))
3.  Dans FreeCAD, allez dans {{MenuCommand|Edition → Préférences → FEM → Elmer}}
4.  Associez le chemin correct pour `ElmerGrid` et `ElmerSolver`

    :   ![Elmer Tab in FEM Preferences](images/Preferences-ElmerPath.png )
    :   
        *Ci-dessus: menu de dialogue des préférences d'Elmer affichant les champs pour localiser les binaires importants d'Elmer sous Windows*
        

Vous êtes prêt à utiliser Elmer dans FreeCAD.

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md)
2.  Créez un conteneur [Analysis](FEM_Analysis/fr.md) en appuyant sur l\'icône <img alt="" src=images/FEM_Analysis.svg  style="width:22px;">.
3.  Créez un solveur FEM pour Elmer, en appuyant sur l\'icône <img alt="" src=images/FEM_SolverElmer.svg  style="width:22px;">.
    -   Remarque: Une analyse réussie nécessite au moins un modèle (2D ou 3D), un matériau ([FEM Fluide](FEM_MaterialFluid/fr.md) ou [FEM Solide](FEM_MaterialSolid/fr.md)), un [Maillage Gmsh](FEM_MeshGmshFromShape/fr.md), des équations et conditions aux limites

    :   ![](images/Elmer_typical_file_tree.png )
    :   
        *Ci-dessus: exemple de [vue en arborescence](Tree_view/fr.md) une fois qu'un solveur pour Elmer est activé*
        
4.  Modifiez les paramètres du solveur dans l\'onglet **Data** de l\'[Éditeur de propriétés](Property_editor/fr.md) de l\'objet SolverElmer dans le modèle [vue en arborescence](tree_view/fr.md)
5.  Double-cliquez sur l\'objet **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** pour préparer une analyse

    :   <img alt="" src=images/ElmerSolver_TaskPanel.png  style="width:300px;">
    :   
        *Ci-dessus: boîte de dialogue pour exécuter une analyse Elmer*
        
6.  Sélectionnez le chemin vers lequel l\'analyse écrira en cliquant sur **...**
7.  Cliquez sur **Write** pour écrire les fichiers de cas dans le répertoire sélectionné précédemment
8.  Cliquez sur **Run** pour démarrer l\'analyse

### A propos des équations {#a_propos_des_équations}

-   Pour effectuer l\'analyse d\'un comportement physique particulier, une équation doit être utilisée (écoulement, chaleur, électrostatique\...).
-   Disambiguation : Le terme *Equation* est utilisé dans FreeCAD pour décrire les différents mécanismes physiques, le terme *Solveur* est utilisé dans tous les documents Elmer. Ainsi, lorsqu\'on utilise dans FreeCAD l\'\"Équation d\'écoulement\", en réalité Elmer utilise le \"Solveur d\'écoulement\" pour trouver une solution à l\'équation de Navier-Stokes.
-   Une ou plusieurs équations peuvent être utilisées en même temps avec Elmer en ajoutant simplement l\'objet équation sous l\'objet SolverElmer, réalisant ainsi des analyses multi-physiques :

1.  Cliquez sur l\'objet **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** dans le modèle de la [vue en arborescence](Tree_view/fr.md)
2.  Sélectionnez une équation:
    -   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Equation élasticité](FEM_EquationElasticity/fr.md)
    -   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Équation force électrique](FEM_EquationElectricforce/fr.md)
    -   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Equation électrostatique](FEM_EquationElectrostatic/fr.md)
    -   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Equation débit](FEM_EquationFlow/fr.md)
    -   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Equation de flux](FEM_EquationFlux/fr.md)
    -   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Equation chaleur](FEM_EquationHeat/fr.md)

## Remarques

-   Les paramètres du solveur et des équations sont définis indépendamment via l\'onglet **Data** de l\'[Éditeur de propriétés](Property_editor/fr.md) de leurs objets respectifs dans la [vue en arborescence](Tree_view/fr.md).
-   Chaque équation aura une priorité. Par exemple, si vous essayez de voir l\'effet d\'un flux convectif d\'air chaud, l\'équation pour le débit doit être résolue avec une priorité plus élevée que la chaleur, sinon le solveur résoudra d\'abord la chaleur par conduction puis le débit.
-   Cas 2D vs 3D : Elmer peut être utilisé pour résoudre des cas 2D et 3D. Cependant, lors de la définition d\'un cas 2D, les faces doivent être mappées dans le plan XY de FreeCAD, sinon le solveur essaiera de calculer un cas 3D sur une face, et les vecteurs normaux seront sous-définis. De plus amples informations peuvent être trouvées dans les forums FreeCAD : <https://forum.freecadweb.org/viewtopic.php?f=18&t=48175>.

## Documentation

Le lien suivant donne accès à la [documentation complète pour Elmer](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/). Cela inclut les manuels ainsi que les tutoriels. Notez que la documentation et les fichiers ajoutés avec \"gui\" concernent généralement l\'utilisation de l\'interface graphique Elmer et non l\'implémentation FreeCAD d\'Elmer.





{{FEM Tools navi

}} 
