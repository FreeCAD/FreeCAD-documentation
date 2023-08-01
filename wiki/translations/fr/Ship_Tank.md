---
- GuiCommand:
   Name:Ship TankNew
   Name/fr:Ship Réservoir
   MenuLocation:Weights → Create a new tank
   Workbenches:[Ship](Ship_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---

# Ship Tank/fr

## Description

Créer une nouvelle instance de réservoir dans une instance de bateau.

Les instances de réservoir sont jusqu\'à présent similaires aux **instances de poids** (voir [Ship Poids](Ship_Weight/fr.md)), c\'est-à-dire qu\'elles agissent comme des poids qui seront pris en compte pour le calcul du centre de gravité et du déplacement. Cependant, ils ont de petites différences dans les entrées requises pour configurer une instance de réservoir, ainsi que dans la façon dont sa contribution au poids du bateau est calculée. Dans cette optique, les réservoirs ne peuvent être créés que sur des géométries solides/volumétriques, et la densité n\'est pas demandée avant qu\'ils ne soient ajoutés à une *condition de charge* (voir [Ship Charge](Ship_LoadCondition/fr.md)). Ensuite, leur contribution au poids et au centre de gravité du bateau dépendra du niveau de remplissage (à définir dans la **condition de charge**) et de l\'angle de roulis et d\'assiette du bateau, tant que le fluide à l\'intérieur se remodèle, affectant effectivement la position du centre de gravité (l\'effet dit de surface libre).

## Utilisation

Afin de créer un poids, sélectionnez la géométrie solide du réservoir (l\'intérieur du réservoir sera éventuellement rempli de fluides) et lancez **Weights → <img src="images/Ship_Tank.svg" width=16px> Create a new tank**.

Le panneau des tâches s\'affiche, dans lequel vous devez sélectionner l\'instance de navire (voir [Ship Créer une coque](Ship_CreateShip/fr.md)) dans laquelle le réservoir doit être ajouté.

Lorsque vous appuyez sur le bouton **Accept**, une nouvelle instance de réservoir est créée dans l**\'instance de bateau** choisie.

## Tutoriels

-   [Tutoriel Construction navale S60](FreeCAD-Ship_s60_tutorial/fr.md)
-   [Tutoriel Construction navale S60 (II)](FreeCAD-Ship_s60_tutorial_(II)/fr.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship Tank/fr
