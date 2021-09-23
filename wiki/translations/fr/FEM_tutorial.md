# FEM tutorial/fr
{{TutorialInfo/fr
|Topic=Analyse par éléments finis
|Level=Débutant
|Time=10 minutes + temps d'exécution
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16.6700 ou plus
}}

## Introduction

Ce tutoriel est une présentation d\'utilisation destiné au lecteur le flux de travail sur base de l\'atelier FEM, ainsi que la plupart des outils disponibles pour effectuer une analyse statique d'éléments finis.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Conditions

-   FreeCAD version 0.16.6700 ou plus
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) et/ou [GMSH](http://geuz.org/gmsh/) doivent être installés sur votre système
-   Pour GMSH, installez par [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) la [Macro GMSH](Macro_GMSH/fr.md) développée par [psicofil](https://github.com/psicofil/Macros_FreeCAD)
-   [Calculix](http://www.calculix.de/) doit être aussi installé sur votre système
-   L\'utilisateur doit avoir les connaissances de base concernant l\'utilisation des ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md)

## Procédure

### Modélisation

Dans cet exemple, un cube est utilisé pour l\'étude, mais tous les modèles créés avec les ateliers Part ou PartDesign peuvent être utilisés.

1.  Créez un [nouveau document](Std_New/fr.md) (appuyez sur le bouton <img alt="" src=images/Std_New.svg  style="width:24px;">)
2.  Activez l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)
3.  Créez un Cube
4.  Changer ses **Dimensions** selon les valeurs suivantes :
    1.  Height (hauteur) : 1.000 mm
    2.  Length (longueur) : 8.000 mm
    3.  Width (largeur) : 1.000 mm

Maintenant, nous avons un modèle avec lequel nous pouvons travailler.

### Créer l\'analyse 

#### Netgen

1.  Sélectionner le modèle
2.  Cliquer sur <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> [Nouvelle analyse mécanique](FEM_Analysis/fr.md) depuis la barre d\'outils pour créer une analyse de l\'objet sélectionné
3.  Dans la fenêtre de dialogue du maillage, cliquer sur **OK**

Vous pouvez également faire glisser et déposer un maillage pour une analyse mécanique d\'un objet qui ne possède pas de maillage dans la [Vue en arborescence](Tree_view/fr.md)

#### GMSH

L\'utilisation de la macro de psicofil\'s est recommandée et est utilisée pour cet exemple.

1.  Activer la macro
2.  Sélectionner l\'objet à analyser, dans cet exemple notre cube
3.  Cochez la case **Create Mechanical Analysis from mesh**
4.  Cliquez **OK**

Nous avons maintenant créé un maillage de notre objet et nous sommes prêt à ajouter des contraintes et des forces.

### Contraintes et forces 

1.  Masquer le maillage depuis l\'arborescence.
2.  Afficher le modèle original
3.  Sélectionner <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> [Créer une contrainte FEM fixe](FEM_ConstraintFixed/fr.md)
4.  Sélectionner la face arrière du Cube (face sur l\'axe **YZ**) puis cliquer OK
5.  Sélectionner <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> [Créer une contrainte de force FEM](FEM_ConstraintForce/fr.md)
6.  Sélectionner la face avant du Cube (la face parallèle à la face arrière) puis définir la valeur **Area load** à 9000000.00
7.  Définir la **Direction** à **-Z** en sélectionnant une des arêtes de face parallèles à cette direction.
8.  Cliquer OK

Nous venons d\'établir les restrictions et les forces pour notre étude statique.

### Préparations finales 

1.  Sélectionner <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> [Matériau pour le solide](FEM_MaterialSolid/fr.md) puis choisir Calculix comme matériau
2.  Cliquer sur **OK**

### Exécution du solveur 

#### Procédure régulière 

1.  Sélectionner l\'objet solveur <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contenu dans l
**\'Analyse mécanique**
2.  Sélectionner <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Contrôle de tâches du solveur ](FEM_SolverControl/fr.md) depuis le menu
3.  Sélectionner **Write Calculix Input File**
4.  Sélectionner **Run Calculix**
5.  Cliquer sur **Fermer**

#### Procédure rapide 

1.  Sélectionner l\'ojet solveur <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contenu dans l
**\'Analyse mécanique**
2.  Cliquer sur <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Analyse rapide](FEM_SolverRun/fr.md).

### Analyse des résultats 

1.  Depuis l**\'arborescence de l\'objet**, sélectionner l\'objet **Results**
2.  Sélectionner <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Afficher le résultat](FEM_ResultShow/fr.md)
3.  Choisir parmi les différents types de résultats à visualiser
4.  Le curseur en bas du panneau peut être utilisé pour altérer la visualisation du maillage. Cela permet de visualiser la déformation subie par l\'objet ; gardez en tête qu\'il s\'agit d\'une approximation.
5.  Pour supprimer les résultats, sélectionner <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purger les résultats](FEM_ResultsPurge/fr.md)


{{Note|Comparaison avec le fichier d'exemple précédent|Si vous sélectionnez le type de résultat '''déplacement Z''',  vous pouvez voir que la valeur obtenue est presque identique au fichier d'exemple fourni avec FreeCAD. Des différences pourraient survenir en raison de la qualité du maillage et le nombre de nœuds qu'il contient.}}

Nous avons complété la procédure de base de l\'[atelier FEM](FEM_Workbench/fr.md).


{{Tutorials navi

}} {{FEM Tools navi}}

---
[documentation index](../README.md) > FEM tutorial/fr
