---
- GuiCommand:
   Name: Ship Area
   Name/fr: Ship Courbe de surface
   MenuLocation: Ship design - Areas curve
   Workbenches: [Ship](Ship_Workbench/fr.md)
   Shortcut: 
   SeeAlso: 
---

# Ship AreasCurve/fr

## Description

Trace la courbe des aires transversales.

<img alt="" src=images/FreeCAD-Ship-s60Areas.png  style="width:800px;"> 
*Conception d'un projet de courbe des surfaces transversales*

La courbe des surfaces transversales offre des informations très précieuses lors des premières étapes de la conception d\'un navire, car elle donne une idée de la forme et de la répartition du volume du navire.

Une attention particulière doit être accordée aux éventuels épaulements de la courbe, qui indiqueraient une grande résistance du navire (moins d\'efficacité en d\'autres termes).

## Utilisation

Pour calculer la courbe des aires transversales, sélectionnez une **instance de bateau** (voir [Ship Coque](Ship_CreateShip/fr.md)), et lancez **Ship design → <img src="images/Ship_AreasCurve.svg" width=16px> Areas curve**.

Le panneau des tâches et une annotation de surface libre dans la [Vue 3D](3D_view/fr.md) sont affichés. L\'annotation est temporaire et sera supprimée lorsque vous fermerez l\'outil, ne vous inquiétez donc pas à ce sujet.

Par défaut, le tirant d\'eau du navire de conception est sélectionné, ainsi qu\'un angle d\'assiette nul. Vous êtes libre de modifier ces deux champs. Chaque fois que les données de tirant d\'eau et d\'assiette sont modifiées, certaines informations de base concernant la partie immergée du navire sont mises à jour dans la zone de texte.

Vous pouvez également sélectionner le nombre de sections transversales à considérer. Plus le nombre de sections est élevé, meilleure sera la résolution obtenue, au prix d\'un temps de calcul plus long.

Lorsque vous appuyez sur le bouton **Accept**, le calcul commence. Il se peut que FreeCAD soit bloqué pendant un certain temps, soyez patient. Lorsque le calcul est terminé, un tracé de la courbe des aires transversales est créé, ainsi qu\'une feuille de calcul avec ces informations.

## Tutoriels

-   [Tutoriel Construction navale S60](FreeCAD-Ship_s60_tutorial/fr.md)
-   [Tutoriel Construction navale S60 (II)](FreeCAD-Ship_s60_tutorial_(II)/fr.md)



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship AreasCurve/fr
