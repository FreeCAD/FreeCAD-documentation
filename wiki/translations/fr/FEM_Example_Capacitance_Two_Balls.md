# FEM Example Capacitance Two Balls/fr




{{TutorialInfo/fr
|Topic= Analyse par les éléments finis
|Level=Débutant
|Time=
|Author=[https://wiki.freecadweb.org/User:Sudhanshu_Dubey Sudhanshu Dubey]
|FCVersion=0.19 et au-dessus
|Files=
}}

## Introduction

Cet exemple est destiné à montrer comment simuler le 6ème exemple de [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf), **Electrostatic equation -- Capacitance of two balls**, en utilisant les nouveaux [FEM Exemples](FEM_Examples/fr.md). Ce tutoriel illustre comment configurer l\'exemple, étudier ses différentes parties, le résoudre en utilisant le [FEM Solveur Elmer](FEM_SolverElmer/fr.md) et visualiser les résultats en utilisant [FEM Filtre rattaché à une région](FEM_PostCreateClipFilter/fr.md).

<img alt="" src=images/Two_balls_result_2.png  style="width:1200px;">

## Conditions

-   Une version compatible de FreeCAD mentionnée dans l\'aperçu du tutoriel.

    :   Utilisez **Aide → À propos de FreeCAD** pour voir la version installée de FreeCAD.
-   Aucun logiciel externe n\'est nécessaire pour charger l\'exemple, visualiser le maillage et la géométrie ainsi que pour visualiser les résultats.
-   Pour résoudre l\'Analyse des éléments finis (FEA), le logiciel de résolution Elmer doit être installé sur votre ordinateur. Voir [FEM Solveur Elmer](FEM_SolverElmer/fr.md) pour savoir comment installer Elmer.

## Configurer l\'exemple 

### Charger l\'atelier FEM 

-   Démarrez FreeCAD, l\'atelier Start doit être chargé.
-   Basculez vers l\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [Atelier FEM](FEM_Workbench/fr.md).

### Charger l\'exemple 

-   Allez dans **Utilities → <img src=images/FEM_Examples.svg style="width:24px"> Ouvrez les exemples FEM**.
-   Lorsque l\'interface graphique s\'ouvre, recherchez et ouvrez \"Electrostatics Capacitance Two Balls\". Vous pouvez facilement trouver l\'exemple dans **All** ou dans **Solvers → Elmer**. Pour ouvrir l\'exemple, double-cliquez dessus ou sélectionnez-le et cliquez sur **Setup**.

<img alt="" src=images/Two_balls_selection.png  style="width:300px;">

## Comprendre le cas de simulation 

Ce cas présente la solution de la capacité de sphères parfaitement conductrices en espace libre. Une différence de tension entre les sphères entraîne l\'introduction d\'une charge électrique dans le système. Les sphères ont également une capacité propre qui provient de la différence de tension avec le champ lointain. Par conséquent, une matrice de capacité symétrique de taille 2 × 2 doit être résolue. Les capacités peuvent être calculées à partir de deux configurations de tension différentes.

## Comprendre le modèle 

-   Le modèle contient trois sphères.

1.  Les deux plus petites sont des sphères parfaitement conductrices.
2.  La plus grande simule l\'air ambiant.

-   Les deux sphères plus petites sont fusionnées ensemble puis cette fusion est coupée de la plus grande sphère.

![ 1200px](images/Two_balls_model_full.png )

## Conteneur d\'analyse et ses objets 

-   Il y a au moins 7 objets nécessaires pour effectuer cette analyse électrostatique.
-   Un <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> conteneur d\'analyse

1.  Un <img alt="" src=images/FEM_SolverElmer.svg  style="width:24px;"> solveur Elmer
2.  Une <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> équation électrostatique
3.  Un <img alt="" src=images/FEM_MaterialFluid.svg  style="width:24px;"> matériau fluide (pour représenter l\'air ambiant)
4.  Une <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> contrainte électrostatique (3 d\'entres elles)
5.  La <img alt="" src=images/Fem-thermomechanical-analysis.svg  style="width:24px;"> permittivité constante au vide
6.  Un <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> maillage FEM Gmsh
7.  Une <img alt="" src=images/FEM_MeshRegion.svg  style="width:24px;"> région maillée (pour les plus petites sphères)

<img alt="" src=images/Two_balls_analysis.png  style="width:300px;">

## Exécution de l\'Analyse des éléments finis (FEA) 

-   Dans la [Vue en arborescence](Tree_view/fr.md) double-cliquez sur l\'objet solveur <img alt="" src=images/FEM_SolverElmer.svg  style="width:24px;">.
-   Cliquez sur le fichier **Write** dans la même fenêtre de tâche. Regardez la fenêtre du journal jusqu\'à ce qu\'elle imprime \"write completed.\"
-   Cliquez sur **Run**. Puisqu\'il s\'agit d\'une petite analyse, son exécution devrait prendre quelques secondes, attendez de voir \"ELMER SOLVER FINISHED AT\" en sortie.
-   Cliquez sur **Close** dans la fenêtre de la tâche une fois l\'exécution terminée.
-   Deux nouveaux objets de résultat doivent être créés, <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult et <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput.
-   Si vous obtenez un message d\'erreur sur le solveur binaire ou similaire lors du déclenchement de l\'analyse, vérifiez l\'installation du [FEM Solveur Elmer](FEM_SolverElmer/fr.md)

## Visualisation des résultats 

-   Assurez-vous que l\'analyse est activée.
-   Assurez-vous que l\'analyse contient toujours l\'objet de résultat, sinon relancez simplement le solveur.
-   Assurez-vous que le maillage est invisible. Sinon, sélectionnez l\'objet maillé et appuyez sur **Espace** pour basculer la visibilité.
-   Double-cliquez sur le <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult pour charger dans le [Panneau des tâches](Task_Panel/fr.md).
-   Changez le \"Mode\" en \"Surface\" et le \"Field\" en \"potential\". Appuyez sur **Ok**.
-   Vous remarquerez que la couleur de la sphère est passée au bleu et que le dégradé de droite affiche des valeurs de 0 à +1. Ça devrait ressembler a quelque chose comme ca:

<img alt="" src=images/Two_balls_potential.png  style="width:1200px;">

## Post-traitement du résultat 

-   Bien que nous ayons réussi à visualiser le résultat potentiel, nous ne voyons actuellement que le potentiel zéro dans l\'air entourant les deux boules. Pour voir le potentiel des sphères, nous devons appliquer un filtre de clip.
-   Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult puis dans la barre d\'outils, cliquez sur <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:24px;"> Post Create Clip Filter.
-   Cela ouvrira le [Panneau des tâches](Task_Panel/fr.md) avec les configurations de filtre de clip. Sélectionnez \"Plane\" dans le menu \"Create\" et cochez la case \"Cut Cells\". Après cela, cliquez sur **Apply**.

<img alt="" src=images/Two_balls_postcreate.png  style="width:300px;">

-   Choisissez ensuite les mêmes configurations (Surface et potentiel) que vous avez lors de la visualisation des résultats. Cliquez sur **Ok**. Basculez la visibilité de <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult en utilisant **Espace** et vous devriez voir quelque chose comme ceci:

<img alt="" src=images/Two_balls_result.png  style="width:1200px;">

-   Maintenant, nous pouvons clairement voir la distribution des potentiels dans et autour des sphères.

## Recherche de la capacité 

-   Notre objectif actuel est de trouver la capacité contenue dans <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput.
-   Double-cliquez sur <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput pour l\'ouvrir. Faites défiler jusqu\'à ce que vous trouviez:




    StatElecSolve: Capacitance matrix computation performed (i,j,C_ij)
    StatElecSolve:   1  1    5.08013E+00
    StatElecSolve:   1  2    1.70071E+00
    StatElecSolve:   2  2    5.07960E+00

-   Ici, le résultat souhaité est C~12~ = 1.70071. Cette valeur est proche du `1.691` donné dans les [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf). Nous pouvons obtenir une valeur encore plus proche en faisant une [FEM Région de maillage](FEM_MeshRegion/fr.md) plus fine mais cette activité est laissée à l\'utilisateur. Il est également conseillé à l\'utilisateur de jouer avec le [FEM Filtre rattaché à une région](FEM_PostCreateClipFilter/fr.md) pour obtenir un résultat visuel similaire à la première image de ce tutoriel.


{{Tutorials navi

}} {{FEM Tools navi}}  
