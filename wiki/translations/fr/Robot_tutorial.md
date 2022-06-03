# Robot tutorial/fr
---
- TutorialInfo   */fr
   Topic   * Robot Workbench
   Level   * Débutant
   Time   *
   Author   *r-frank
   FCVersion   *0.16.6703 et plus
   Files   *
}}

Ce tutoriel a pour but de vous apprendre à utiliser l\'[atelier de simulation de Robot](Robot_Workbench/fr.md) pour simuler une cellule de configuration de robot.

![Visualiser la simulation](images/Robot_Tutorial_RobotSimulation.gif )

## Avant de commencer 

Ce tutoriel est écrit pour FreeCAD version 0.11 R3977 ou ultérieure. Si vous n\'avez pas FreeCAD sur votre PC, allez à la [page de téléchargement](Download/fr.md) afin de l\'installer.

Ce tutoriel vise l\'utilisation des [robots industriels](http   *//fr.wikipedia.org/wiki/Robotique_industrielle) et pas les robots mobiles ou de service (voir [ici](http   *//en.wikipedia.org/wiki/Robot#Modern_robots)).

## Installation de la scène 

1.  Cliquer sur [Robot Workbench](Robot_Workbench/fr.md)
2.  Créer un nouveau document en choisissant **File** → **New** dans menu
3.  Insert un Kuka IR500 le robot dans la scène en choisissant **Robot** → **insert Robots** → **Kuka IR500** du menu
4.  Changer à vue axonométrique en cliquant sur <img alt="" src=images/View-axometric.png  style="width   *32px;">
5.  Zoomer pour adapter tout en cliquant sur ![32px](images/view-zoom-all.png)
6.  Sauvegarder votre fichier\...

## Définir une trajectoire 

1.  Cliquer sur [Robot Worbench](Robot_Workbench/fr.md) Activer le modèle dans l\' arborescence
2.  Créé une nouvelle trajectoire en cliquant sur <img alt="" src=images/Robot_CreateTrajectory.png  style="width   *32px;">
3.  Sélectionner le robot dans l\'arbre
4.  Donner la position départ pour le robot en cliquant sur <img alt="" src=images/Robot_SetHomePos.png  style="width   *32px;">
5.  Cliquer sur le panneau de configuration <img alt="" src=images/Robot_InsertWaypoint.png  style="width   *32px;">
6.  Changer la position du robot en utilisant le curseur
7.  Quand le robot et la trajectoire sont sélectionnés dans la vue 3D cliquer sur le bouton <img alt="" src=images/Robot_InsertWaypoint.png  style="width   *32px;"> pour insérer un point de départ dans la trajectoire
8.  Chaque point de la trajectoire est visible avec une croix jaune, tous les points de la trajectoire sont connectés avec des lignes oranges
9.  Définir au moins trois points différents et les insérer dans la trajectoire

## Simulation des mouvement du robot 

1.  Sélectionner robot et trajectoires dans l\'arborescence
2.  Sélectionner la simulation en cliquant sur le bouton <img alt="" src=images/Robot_Simulate.png  style="width   *32px;">
3.  Cliquer sur le bouton démarrer la simulation **I>**
4.  Visualiser la simulation


 {{Robot Tools navi}} {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Robot](Robot_Workbench.md) > Robot tutorial/fr
