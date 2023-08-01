# Robot Workbench/fr
**L'atelier Robot n'est plus maintenu. Si vous avez de l'expérience avec le sujet et que vous souhaitez le maintenir, veuillez indiquer votre intention dans la section développeur du [https://forum.freecadweb.org/index.php forum FreeCAD].

La raison pour laquelle cet atelier se trouve toujours dans le code source principal est que cet atelier est programmé en C++. Si cet atelier pouvait être programmé en Python, alors il pourrait être transformé en [atelier externe](external_workbenches/fr.md) et il pourrait être déplacé vers un référentiel distinct.
**

## Introduction

<img alt="Icône de l\'atelier Robot" src=images/Workbench_Robot.svg  style="width:128px;">

L\'<img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [atelier Robot](Robot_Workbench/fr.md) permet de simuler les [robots industriels à 6 axes](Robot_6-Axis/fr.md), comme par exemple [Kuka](http://kuka.com/).

Vous pouvez accomplir les tâches suivantes :

-   mettre en place un environnement de simulation avec un robot et des pièces de travail
-   créer et remplir des trajectoires
-   décomposer les fonctions d\'une pièce CAO en une trajectoire
-   simuler le mouvement et l\'accessibilité d\'un robot
-   exporter la trajectoire vers un fichier programme de robot

Pour commencer, essayez le [tutoriel Robot](Robot_tutorial/fr.md) et voyez l\'interface de programmation dans le fichier d\'exemple \[<https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/RobotExample.py>. RobotExample.py\] .




<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Outils

Voici les principales commandes dont vous pouvez vous servir pour créer une configuration de robot.

### Robots

Les outils pour créer et gérer les robots à 6 axes

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Créer un robot](Robot_CreateRobot/fr.md): Insère un nouveau robot dans la scène
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Simuler une trajectoire](Robot_Simulate/fr.md): Ouvre le dialogue de simulation afin de régler une simulation
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Exporter une trajectoire](Robot_Export/fr.md): Exporte la trajectoire dans un fichier programme robot
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Définir la positon de départ](Robot_SetHomePos/fr.md): Définit la position de départ d\'un robot
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Restaurer la positon de départ](Robot_RestoreHomePos/fr.md): Retourne le robot à sa positon de départ

### Trajectoires

Les outils pour créer et manipuler les trajectoires. Il y en a deux sortes, paramétriques et non-paramétriques.

#### Trajectoire non-paramétriques 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Créer une trajectoire](Robot_CreateTrajectory/fr.md): Créé une nouvelle trajectoire vide
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Définir l\'orientation par défaut](Robot_SetDefaultOrientation/fr.md): Règle l\'orientation par défaut des points de passage
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Définir les paramètres de vitesse par défaut](Robot_SetDefaultValues/fr.md): Règle les valeurs par défaut pour la création de points de passage
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Insérer dans la trajectoire](Robot_InsertWaypoint/fr.md): Insère un point de passage de la position actuelle du robot dans la trajectoire
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Insérer dans la trajectoire](Robot_InsertWaypointPre/fr.md): Insère un point de passage de la position actuelle du pointeur de la souris dans la trajectoire

#### Trajectoire paramétriques 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width:30px;"> [Générer une trajectoire à partir d\'un ensemble d\'arêtes](Robot_Edge2Trac/fr.md): Insère un nouvel objet dont les arêtes formeront une trajectoire
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width:30px;"> [Habiller une trajectoire](Robot_TrajectoryDressUp/fr.md): Créé un habillage qui supplante certaines propriétés d\'une trajectoire
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width:30px;"> [Grouper et connecter des trajectoires](Robot_TrajectoryCompound/fr.md): Crée un composé (compound) et connecte un ensemble de trajectoires

## Script

Voir [Robot API exemple](Robot_API_example/fr.md) pour une description des fonctions utilisées pour modéliser les déplacements du robot.

## Tutoriels

-   [Robot 6-Axis](Robot_6-Axis/fr.md)
-   [VRML Préparation pour Simulation d\'un Robot](VRML_Preparation_for_Robot_Simulation/fr.md)





{{Robot Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Robot](Category_Robot.md) > Robot Workbench/fr
