---
- TutorialInfo:/fr
   Topic:Analyse par éléments finis
   Level:Débutant
   Time:10 minutes
   Author:[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
   FCVersion:0.16.6377 ou plus récente
---

# FEM CalculiX Cantilever 3D/fr





## Introduction

Cet exemple est destiné à montrer à quoi ressemble une simple analyse par éléments finis (**FEA**) dans l\'[Atelier FEM](FEM_Workbench/fr.md) de FreeCAD et comment les résultats peuvent être visualisés. Il illustre comment déclencher un FEA et comment changer la valeur et la direction de la charge. De plus, étant donné que le fichier d\'exemple est fourni avec toute installation de FreeCAD, c\'est une vérification utile et facile à exécuter dans le but de vérifier si l\'Atelier FEM est correctement configuré.

<img alt="" src=images/FEM_example01_pic00.jpg  style="width:700px;">

## Exigences

=

-   Une version compatible de FreeCAD désignée dans l\'aperçu du tutoriel.

    :   Utilisez la **Aide → À propos de FreeCAD** pour voir la version de FreeCAD installée
-   Aucun logiciel externe n\'est nécessaire pour charger le fichier d\'exemple, afficher le maillage et la géométrie ainsi que pour visualiser les résultats.
-   Pour relancer le FEA, le logiciel Solver CalculiX doit être installé sur votre ordinateur. Probablement le solveur a déjà été installé avec FreeCAD. Si le solveur CalculiX n\'est pas installé, voir [FEM Installation des composants requis](FEM_Install/fr.md).

## Configurer le fichier d\'exemple 

### Charger l\'atelier Démarrage 

-   Démarrez FreeCAD
-   L\'Atelier Démarrage doit être chargé

### Charger le fichier exemple 

-   Accédez aux exemples de projets et cliquez sur \"Load an FEM analysis example\"
-   Si en raison d\'opérations ultérieures, certaines géométries, contraintes ou résultats sont interrompus ou supprimés, répétez simplement les étapes ci-dessus.

<img alt="" src=images/FEM_example01_pic01.jpg  style="width:700px;">

### Activer le conteneur d\'analyse 

-   Pour travailler avec une analyse, celle-ci doit être activée.
-   Dans la [Vue en arborescence](Tree_view/fr.md) cliquez droit sur <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> 
**MechanicalAnalysis**
-   Choisir **Activate analysis**

<img alt="" src=images/FEM_example01_pic02.jpg  style="width:700px;">

### Conteneur d\'analyse et ses objets 

-   Si l\'analyse est activée, FreeCAD lui-même changera l\'espace de travail actuel en FEM.
-   Il existe au moins les 5 objets nécessaires pour effectuer une analyse mécanique statique.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> conteneur d\'analyse

1.  <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> un solveur
2.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> un matériau
3.  <img alt="" src=images/FEM_ConstraintFixed.png  style="width:24px;"> une contrainte fixée
4.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> une contrainte de force
5.  <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> un maillage FEM

-   Comme les résultats sont également inclus dans l\'exemple, il existe un sixième objet, les résultats <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;">, développé dans le paragraphe suivant.

### Visualisation des résultats 

1.  Assurez-vous que l\'analyse est activée.
2.  Assurez-vous que l\'analyse contient toujours l\'objet résultant, sinon reculez le fichier d\'exemple.
3.  Cliquez sur le bouton <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Afficher le résultat](FEM_ResultShow/fr.md) dans la barre d\'outils FEM.
4.  Dans la fenêtre de tâches, choisissez `z-Displacement`. Il montre `-88.443 mm` dans la direction Z négative.
5.  Cela a du sens puisque la force est également dans la direction Z négative.
6.  Activez la case à cocher Show Displacement.
7.  Le curseur peut être utilisé pour modifier le maillage pour voir la déformation de manière simplifiée.
8.  Choisissez parmi les différents types de résultats pour afficher tous les types de résultats disponibles dans l\'Interface Graphique Utilisateur.

<img alt="" src=images/FEM_example01_pic03.jpg  style="width:400px;">

### Purger les résultats 

1.  Assurez-vous que l\'analyse est activée.
2.  Pour supprimer les résultats : sélectionnez dans la barre d\'outils l\'icône <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;">. [Purger les résultats](FEM_ResultsPurge/fr.md).

### Exécuter la FEA 

-   Dans la [Vue en arborescence](Tree_view/fr.md), double-cliquez sur l\'objet solveur <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
-   Dans le [Panneau des tâches](Task_panel/fr.md) de l\'objet solveur, assurez-vous que l\'analyse statique est sélectionnée.
-   Cliquez sur le fichier d\'écriture .inp dans la même fenêtre de tâches. Regardez la fenêtre de journal jusqu\'à ce qu\'elle imprime \"écriture terminée\".
-   Cliquez sur **Run CalculiX**. Comme il s\'agit d\'une très petite analyse, il faudrait moins d\'une seconde pour s\'exécuter.
-   Dans la fenêtre de texte, il doit imprimer en lettres vertes \"CalculiX done!\" et dans la ligne suivante \"chargement des jeux de résultats \...\"
-   Vous avez terminé votre premier FEA dans FreeCAD s\'il n\'y a pas eu de message d\'erreur.
-   Cliquez sur **Fermer** dans la fenêtre de tâches.
-   Un nouvel objet de résultat devrait être créé. Vous savez déjà comment visualiser les résultats .
-   Si vous obtenez un message d\'erreur sans solveur binaire ou similaire lors du déclenchement de la vérification d\'analyse, voir [FEM Installation des composants requis](FEM_Install/fr.md).

<img alt="" src=images/FEM_example01_pic04.jpg  style="width:400px;">

### Exécuter la FEA rapidement 

-   Dans l\'arborescence, sélectionnez l\'objet solveur <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> de l\'analyse <img alt="" src=images/FEM_Analysis.svg  style="width:24px;">.
-   Dans la barre d\'outils de l\'icône, cliquez sur <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Lancer les calculs\...](FEM_SolverRun/fr.md).
-   Le fichier de saisie Calculix sera écrit, CalculiX sera déclenché et l\'objet résultant devrait être créé.

### Modification de la direction de la charge et de sa valeur 

-   Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez l\'objet FEM mesh <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> et appuyez sur la touche **Espace**.
    -   **Résultat:** la visibilité du maillage FEM sera désactivée. Le modèle géométrique est encore visible.
-   Dans la [Vue en arborescence](Tree_view/fr.md), double-cliquez sur l\'objet de contrainte de force pour ouvrir son [Panneau des tâches](Task_panel/fr.md).
-   Dans la fenêtre de tâches, modifiez la valeur de charge à **500000000N=500MN** (**Remarque:** l\'unité de force dans la fenêtre de tâche doit être en N)
-   Cliquez sur le bouton **Direction**.
-   Sur le modèle géométrique, cliquez sur l\'un des bords longs dans la direction x.
-   Les flèches rouges de la force changent de direction dans la direction x. Ils montrent la direction fixée.
-   Comme la tension doit être appliquée à la boîte, la Direction inverse doit être déclenchée en cliquant dessus.
-   **Résultat:** Les flèches rouges qui illustrent la force changeront leur direction dans la direction x. Ils indiquent la direction fixe.
-   Cliquez sur **OK** dans la fenêtre de tâches.

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Activez la [visibilité](Std_ToggleVisibility/fr.md) du maillage FEM <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> en le sélectionnant dans l\'arborescence et en appuyant sur la touche **Espace**.
-   Vous savez déjà comment déclencher une analyse et comment visualiser les résultats.
-   La déformation dans la direction x devrait être de 19,05 mm.

<img alt="" src=images/FEM_example01_pic06.jpg  style="width:400px;">

## Et ensuite? 

-   Nous avons maintenant terminé le de travail de base pour l\'[Atelier FEM](FEM_Workbench/fr.md).
-   Vous êtes maintenant prêt à faire le deuxième [FEM Tutoriel](FEM_tutorial/fr.md).
-   Nous créerons nous-même le CalculiX cantilever et comparerons les résultats avec la théorie de la poutre.


 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [FEM](Category_FEM.md) > FEM CalculiX Cantilever 3D/fr
