---
- GuiCommand:
   Name:Ship CreateShip
   Name/fr:Ship Coque
   MenuLocation:Ship design → Create a new ship
   Workbenches:[Ship](Ship_Workbench.md)|
   Shortcut:
   SeeAlso:
---

# Ship CreateShip/fr

## Description

Créer un nouveau bateau ou une nouvelle instance de bateau.

Ship travaille sur des **entités de bateau**, qui doivent être créées au-dessus de la géométrie fournie. La géométrie doit être un solide, ou un ensemble de solides. Les critères suivants doivent être pris en compte :

-   Toute la géométrie de la coque doit être fournie (y compris les corps symétriques).
-   La géométrie tribord doit être incluse dans le domaine négatif *y*.
-   Le point d\'origine (0,0,0) est l\'intersection de la **section médiane** (point médian entre les perpendiculaires arrière et avant) et de la **ligne de base**.

![](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Critères d'identification des bateaux*

## Utilisation

Pour créer une **instance de bateau** (en d\'autres termes, un nouveau bateau), sélectionnez la géométrie solide de la coque et lancez **Ship design → <img src="images/Ship_CreateShip.svg" width=16px> Create a new ship**.

Le panneau des tâches et une annotation de surface libre dans la [Vue 3D](3D_view/fr.md) sont affichés. L\'annotation est temporaire et sera supprimée lorsque vous fermerez l\'outil, ne vous inquiétez donc pas à ce sujet.

Les données les plus pertinentes du bateau doivent être introduites (le bateau utilise un système d\'introduction progressive des données, de sorte que les opérations de base peuvent être effectuées en ne connaissant que les données de base du bateau, des informations supplémentaires étant nécessaires lorsque les opérations deviennent plus complexes).

## Données du bateau 

Les principales dimensions doivent être présentées ici :

-   Length : Longueur entre les perpendiculaires.
-   Beam : Largeur totale du bateau.
-   Draft : Tirant d\'eau nominal.

![](images/FreeCAD-Ship-S60ShipCreationFront.png ) 
*Annotations de longueur*

Couramment, la longueur entre perpendiculaires dépend du tirant d\'eau. Si vous ne connaissez pas la longueur du navire vous pouvez saisir le tirant d\'eau et ajuster la longueur.

![](images/FreeCAD-Ship-S60ShipCreationSide.png ) 
*Annotations des largeurs*

Le même processus est valable pour l\'ajustement de la largeur. Notez que la valeur demandée est la largeur totale, mais que seule l\'annotation sur le côté tribord est montrée.

Lorsque vous appuyez sur le bouton **Accept**, une nouvelle instance de bateau nommée *Ship* est créée dans le dialogue *Tags & Attributs*. La géométrie n\'est plus nécessaire, alors n\'hésitez pas à la cacher ou à la supprimer.

## Tutoriels

-   [Tutoriel Construction navale S60](FreeCAD-Ship_s60_tutorial/fr.md)
-   [Tutoriel Construction navale S60 (II)](FreeCAD-Ship_s60_tutorial_(II)/fr.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship CreateShip/fr
