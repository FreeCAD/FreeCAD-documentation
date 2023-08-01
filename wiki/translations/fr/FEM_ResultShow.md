---
- GuiCommand:
   Name:FEM ResultShow
   Name/fr:FEM Afficher les résultats
   MenuLocation:Résultats → Afficher les résultats
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:**R** **S**
   SeeAlso:[FEM Pipeline de résultats](FEM_PostPipelineFromResult/fr.md), [FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ResultShow/fr

## Description

La commande **Afficher les résultats** ouvre la boîte de dialogue pour un objet résultat FEM. Un objet Result est automatiquement créé lorsqu\'une analyse FEM a été effectuée en utilisant le solveur [Calculix](FEM_SolverCalculixCxxtools/fr.md) ou [Z88](FEM_SolverZ88/fr.md).

Un objet Résultat contient le maillage résultant et permet de visualiser les résultats. Il est conçu et donc limité aux résultats thermomécaniques. Sauf pour le [solveur Elmer](FEM_SolverElmer/fr.md), il peut être utilisé comme alternative à un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Un pipeline de résultats peut être utilisé pour visualiser n\'importe quel type de résultats (électriques, etc.).

Les unités utilisées pour l\'objet Result sont celles du [système d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) alors que pour un pipeline de résultats les unités sont [SI](https://fr.wikipedia.org/wiki/Syst%C3%A8me_international_d%27unit%C3%A9s).

La visualisation des résultats n\'est active que lorsque la boîte de dialogue est ouverte. Cependant, les paramètres de la boîte de dialogue sont stockés dans le fichier du modèle FreeCAD.



## Utilisation

Pour afficher la boîte de dialogue des résultats :

-   sélectionnez l\'objet résultat dans la [vue en arborescence](Tree_view/fr.md),
-   puis appuyez sur le bouton de la barre d\'outils **<img src="images/FEM_ResultShow.svg" width=16px> '''Afficher les résultats'''
**
-   ou utilisez le menu **Résultats → <img src="images/FEM_ResultShow.svg" width=16px> Afficher le résultat** (raccourci **R** puis **S**).
-   vous pouvez également double-cliquer sur l\'objet résultat dans l\'arborescence.

Lorsque la boîte de dialogue est ouverte, le maillage résultant s\'affiche automatiquement.

[left\|framed](File:FEM_Result-Object-Dialog.png.md)

La boîte de dialogue à gauche offre les fonctions suivantes :

-   Sélection d\'un type de résultat, le minimum et le maximum seront affichés dans la boîte de dialogue. Le maillage résultant sera coloré en fonction.

-   Le bouton **'''Histogramme'''** permet d\'obtenir un histogramme indiquant la quantité de nœuds du maillage ayant un certain résultat. Le tracé de l\'histogramme peut être modifié par les boutons de sa barre d\'outils. Il est également possible de sauvegarder l\'histogramme en tant qu\'image en utilisant le bouton de sauvegarde de sa barre d\'outils.

-   L\'option **Afficher** permet d\'activer le curseur et de visualiser la déformation du maillage résultant. La valeur du curseur est un facteur avec lequel le résultat *Magnitude de déplacement* est multiplié.Remarque : le curseur n\'affecte que la magnitude de déplacement, pas ses composantes X, Y et Z.

-   Le bouton Après avoir saisi une équation, appuyez sur le bouton et le résultat sera affiché dans les champs affichant le minimum et le maximum. Le maillage du résultat sera coloré en conséquence.**Remarque** : les résultats des calculs sont toujours en MPa, mm ou T, quel que soit le [système d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) que vous utilisez.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultShow/fr
