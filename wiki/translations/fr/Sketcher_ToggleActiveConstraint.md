---
- GuiCommand:/fr
   Name:Sketcher ToggleActiveConstraint
   Name/fr:Sketcher Basculer les contraintes
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   MenuLocation:Sketch → Contraintes d'esquisse → Activer/désactiver la contrainte
   SeeAlso:[Sketcher Basculer en mode construction](Sketcher_ToggleConstruction/fr.md)
   Version:0.19
---

# Sketcher ToggleActiveConstraint/fr

## Description


**[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Activer/désactiver la contrainte](Sketcher_ToggleActiveConstraint/fr.md)**

vous permet d\'activer et de désactiver une contrainte déjà placée. Cela vous permet de conserver la contrainte en arrière-plan mais de tester temporairement une autre disposition de la géométrie existante.

L\'outil **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Active/désactive la barre d'outil...](Sketcher_ToggleDrivingConstraint/fr.md)** est similaire en ce sens qu\'il désactive l\'effet de la contrainte; cependant, avec cet outil, la contrainte ne conserve pas son ancienne valeur. D\'autre part, avec **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Activer/désactiver la contrainte](Sketcher_ToggleActiveConstraint/fr.md)** vous pouvez réactiver immédiatement l\'ancienne contrainte.

## Utilisation

1.  Sélectionnez une contrainte déjà placée, puis appuyez sur **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Activer/désactiver la contrainte](Sketcher_ToggleActiveConstraint/fr.md)**.
2.  Sinon, accédez au [Panneau des tâches](Task_panel/fr.md), à la section **Constraints**, sélectionnez la contrainte, puis ouvrez le menu contextuel (clic droit) et sélectionnez **Deactivate** .
3.  Pour réactiver la contrainte, sélectionnez-la et appuyez à nouveau sur **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Activer/désactiver la contrainte](Sketcher_ToggleActiveConstraint/fr.md)**.

## Exemples

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:" height="350px;"> 
*Une esquisse pleinement contrainte.‎*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:" height="350px;"> <img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:" height="350px;"> 
*A gauche: contrainte désactivée. L'esquisse n'est plus entièrement contrainte. À droite: la géométrie non contrainte peut être déplacée; l'ancienne contrainte est toujours disponible et peut être réactivée pour revenir à l'esquisse entièrement contrainte.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_task_panel.png  style="width:" height="350px;"> 
*Panneau des tâches avec la contrainte désactivée.*

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Le statut actif d\'une contrainte peut être contrôlé par [macros](macros/fr.md) et depuis la [console Python](Python_console/fr.md). 
```python
SketchObject.toggleActive(index)
```

Utilisez la méthode `toggleActive` d\'un [Sketcher SketchObject](Sketcher_SketchObject/fr.md) et `index` de la contrainte pour l\'activer ou la désactiver. L\'index commence de `0` jusqu\'à `N-1`, où `N` est le nombre total de contraintes.

Exemple: 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/fr
