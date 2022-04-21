---
- GuiCommand:/fr
   Name:Ship Load‏‎
   Name/fr:Ship Load‏‎
   MenuLocation:Ship design → Load‏‎ an example ship geometry
   Workbenches:[Ship](Ship_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---

# Ship Geometries Examples/fr

## Description

Cet outil charge des géométries d\'exemple.

Ship travaille sur des **entités de bateau**, qui doivent être créées au-dessus de la géométrie fournie. La géométrie doit être un solide, ou un ensemble de solides. Les critères suivants doivent être pris en compte :

-   Toute la géométrie de la coque doit être fournie (y compris les corps symétriques).
-   La géométrie tribord doit être incluse dans le domaine négatif *y*.
-   Le point d\'origine (0,0,0) est l\'intersection de la **section médiane** (point médian entre les perpendiculaires arrière et avant) et de la **ligne de base**.

![](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Critères d'identification des bateaux*

## Utilisation

Afin d\'aider les nouveaux utilisateurs, FreeCAD-Ship comprend un chargeur d\'exemples de géométries, avec le choix suivant:

-   Série 60 de l\'Université d\'Iowa
-   Wigley Canonical Ship
-   Série 60 Catamaran
-   Wigley Catamaran

Vous pouvez charger un de ces exemples en suivant les étapes suivantes :

1.  Appelez le chargeur d\'exemples de géométries de bateaux soit en
    -   appuyant sur l\'icône <img alt="" src=images/Ship_Load.svg  style="width:24px;"> dans la barre d\'outils
    -   sélectionner la commande **Ship design → Load‏‎ an example ship geometry** dans le menu déroulant.
2.  Un dialogue de tâche s\'affiche, vous invitant à choisir l\'une des géométries de bateau d\'exemple.
3.  Sélectionnez l\'exemple que vous souhaitez charger et appuyez sur **Accept**.
4.  Résultat : L\'outil charge un nouveau document avec la géométrie sélectionnée.


**Attention, avant de modifier quoi que ce soit ! Vous travaillez maintenant avec le fichier d'exemple original. Pour préserver l'exemple original non modifié, vous devez d'abord l'enregistrer dans un nouveau fichier avant de modifier quoi que ce soit.**

## Tutoriels

-   [Tutoriel Construction navale S60](FreeCAD-Ship_s60_tutorial/fr.md)
-   [Tutoriel Construction navale S60 (II)](FreeCAD-Ship_s60_tutorial_(II)/fr.md)





{{Ship_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Ship Geometries Examples/fr
