---
 TutorialInfo:r
   Topic: Analyse par éléments finis
   Level: Débutant
   Time: 10 minutes + temps d'exécution
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.17 ou plus
---

# FEM tutorial/fr





## Introduction

Ce tutoriel est une présentation d\'utilisation destiné au lecteur le flux de travail sur base de l\'atelier FEM, ainsi que la plupart des outils disponibles pour effectuer une analyse statique d'éléments finis.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">



## Conditions

-   FreeCAD version 0.17 ou supérieure.
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) et/ou [GMSH](http://geuz.org/gmsh/) sont installés sur le système (inclus dans l\'installation de FreeCAD).
-   [Calculix](http://www.calculix.de/) est installé sur le système (inclus dans l\'installation de FreeCAD).
-   Le lecteur possède les connaissances de base pour utiliser les ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md).



## Procédure



### Modélisation

Dans cet exemple, un cube est utilisé comme objet d\'étude, mais tout modèle créé dans les ateliers Part ou PartDesign peut être utilisé à la place.

1.  Appuyez sur le bouton **![](images/)_[Nouveau_document](Std_New/fr.md)** pour créer un nouveau document.
2.  Activez l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md).
3.  Créez un cube.
4.  Changer ses **Dimensions** selon les valeurs suivantes :
    1.  Longueur : 8. 000 m.
    2.  Largeur : 1. 000 m.
    3.  Hauteur : 1. 000 m.

Maintenant, nous avons un modèle avec lequel travailler.



### Créer l\'analyse 

1.  Lancez l\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md).
2.  Sélectionnez l\'option **Modèle → <img src="images/FEM_Analysis.svg" width=16px> Conteneur d'analyse** dans le menu.



### Contraintes et forces 

1.  Masquez le maillage dans la vue en arborescence.
2.  Affichez le modèle original.
3.  Sélectionnez <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> [Condition de limite fixe](FEM_ConstraintFixed/fr.md).
4.  Cliquez sur **Ajouter**, sélectionnez la face arrière de l\'objet Cube (face sur l\'axe *YZ*) et cliquez sur **OK**.
5.  Sélectionnez <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> [Charge d\'effort](FEM_ConstraintForce/fr.md).
6.  Cliquez sur **Ajouter**, sélectionnez la face avant de l\'objet Cube (la face parallèle à la face arrière) et définissez la valeur **Charge \[N\]** à 9000000.
7.  Réglez la *Direction* sur *-Z* en sélectionnant une des arêtes de la face parallèle à cette direction.
8.  Cliquez sur **OK**.

Nous venons d\'établir les restrictions et les forces pour notre étude statique.



### Matériau

1.  Sélectionnez <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> [Matériau pour solide](FEM_MaterialSolid/fr.md) puis choisir Calculix-Steel comme matériau.
2.  Cliquez sur **OK**.



### Maillage

Il est recommandé de faire un maillage comme dernière étape des préparations de l\'analyse en raison de l\'association à une géométrie dans FreeCAD. Selon l\'installation de FreeCAD, il peut y avoir des maillages Netgen ou GMSH, vous pouvez utiliser l\'un ou l\'autre.

#### Netgen

1.  Sélectionnez le modèle.
2.  <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:24px;"> [Maillage FEM à partir d\'une forme de Netgen](FEM_MeshNetgenFromShape/fr.md) : Génère un maillage d\'éléments finis pour un modèle en utilisant Netgen.
3.  Dans la boîte de dialogue de maillage, cliquez sur **Appliquer** et **OK**.

Vous pouvez également faire glisser et déposer un maillage pour une analyse mécanique d\'un objet qui ne possède pas de maillage dans la [Vue en arborescence](Tree_view/fr.md)

#### GMSH

1.  Sélectionnez le modèle.
2.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [Maillage FEM à partir d\'une forme de Gmsh](FEM_MeshGmshFromShape/fr.md) : Génère un maillage d\'éléments finis pour un modèle en utilisant Gmsh.
3.  Dans la boîte de dialogue de maillage, cliquez sur **Appliquer** et **OK**.

Nous avons maintenant créé un maillage de notre objet et nous sommes prêt à ajouter des contraintes et des forces.



### Exécution du solveur 



#### Procédure régulière 

1.  Sélectionnez l\'objet solveur <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contenu dans le conteneur **Analysis**.
2.  Sélectionnez <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Contrôle de tâches du solveur](FEM_SolverControl/fr.md) dans le menu.
3.  Sélectionnez **Write .inp File**.
4.  Sélectionnez **Run CalculiX**.
5.  Cliquez sur **OK**.



#### Procédure rapide 

1.  Sélectionnez l\'objet solveur <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contenu dans le conteneur **Analysis**.
2.  Cliquez sur <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Lancer les calculs du solveur](FEM_SolverRun/fr.md).



### Analyse des résultats 

1.  Depuis l**\'arborescence de l\'objet**, sélectionner l\'objet **CCX_Results**
2.  Sélectionnez <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Afficher le résultat](FEM_ResultShow/fr.md)
3.  Choisissez parmi les différents types de résultats à visualiser
4.  Le curseur en bas du panneau peut être utilisé pour altérer la visualisation du maillage. Cela permet de visualiser la déformation subie par l\'objet ; gardez en tête qu\'il s\'agit d\'une approximation.
5.  Pour supprimer les résultats, sélectionnez <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purger les résultats](FEM_ResultsPurge/fr.md)


{{Note|Comparaison avec le fichier d'exemple précédent|Si vous sélectionnez le type de résultat '''déplacement Z''',  vous pouvez voir que la valeur obtenue est presque identique au fichier d'exemple fourni avec FreeCAD. Des différences pourraient survenir en raison de la qualité du maillage et le nombre de nœuds qu'il contient.}}

Nous avons complété la procédure de base de l\'[atelier FEM](FEM_Workbench/fr.md).


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM tutorial/fr
