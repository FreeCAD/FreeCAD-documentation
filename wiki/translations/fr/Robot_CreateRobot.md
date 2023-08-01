---
- GuiCommand:/fr
   Name:Robot CreateRobot
   Name/fr:Robot Création de robot
   MenuLocation:Robot → Insérer des robots
   Workbenches:[Robot](Robot_Workbench/fr.md)
---

# Robot CreateRobot/fr

## Description

Insérez un nouveau robot (KUKA IR500) dans la scène.

## Utilisation

1.  Cliquez sur <img alt="" src=images/Robot_CreateRobot.svg  style="width:32px;"> pour insérer un robot KUKA IR500 dans la scène.
2.  L\'insertion de robots différents/supplémentaires peut se faire de deux manières via le bouton
    -   Sélectionner **Robot** → **Insérer des robots** dans le menu supérieur.

    :   **OU**

    -   S\'assurer qu\'un nouveau document est/était créé et activé (activation via un double-clic sur le document dans la [Vue en arborescence](Tree_view/fr.md)).
    -   Passez à l\'onglet \"Tâches\" dans la [Vue en arborescence](Tree_view/fr.md)).
3.  Sélectionnez l\'un des quatre robots prédéfinis.

## Limitations

Relatif aux versions 0.15/0.16

-   Seuls les robots ayant jusqu\'à six axes avec mouvement de rotation sont définissables.
-   Aucun robot avec des mouvements de translation n\'est possible.
-   Le robot doit être défini par du code et un fichier VRML. Pour plus d\'informations, voir [Robot 6 Axes](Robot_6-Axis/fr.md).

## Remarques

Les robots prédéfinis sont:

-   KUKA IR500
-   KUKA IR210
-   KUKA IR125
-   KUKA IR16





{{Robot_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot CreateRobot/fr
