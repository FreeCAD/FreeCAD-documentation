---
- GuiCommand:/fr
   Name:Sketcher ToggleDrivingConstraint
   Name/fr:Sketcher Contraintes pilotantes
   MenuLocation:Esquisse → Contraintes d'esquisse → Basculer les contraintes pilotantes/pilotées
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**K** **X**
   Version:0.16
   SeeAlso:[Sketcher Géométrie de construction](Sketcher_ToggleConstruction/fr.md)
---

# Sketcher ToggleDrivingConstraint/fr

## Description

L\'icône **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md)** met les contraintes dimensionnelles (fixe, distance horizontale/verticale, dimension, rayon et angle) en mode piloté et inversement. Les icônes de la barre d\'outils deviennent bleues et, plutôt que des contraintes dimensionnelles, des cotes pilotés sont créées. Les cotes pilotés ne contraignent pas l\'esquisse. Il peut être utile de créer des cotes pilotés dans une esquisse pour vérifier les mesures. Lorsqu\'elles reçoivent un nom, elles peuvent également être utilisées pour définir des contraintes dans une autre esquisse via des [expressions](Expressions/fr.md).

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) 
*La barre d'outils des contraintes de Sketcher avec les contraintes en mode pilotées (bleu).*

![](images/Sketcher_ToggleConstraint_example.png ) 
*Une contrainte de distance horizontale (50 mm), une contrainte verticale (30 mm) et une contrainte d'angle (75°) ont été définies pour définir l'esquisse. Une cote dite pilotée a été ajoutée sur le segment de ligne incliné pour connaître sa longueur (31.0583 mm).*



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Basculer les contraintes pilotantes/pilotées](Sketcher_ToggleDrivingConstraint/fr.md)**. Les icônes des contraintes dimensionnelles de la barre d'outils des contraintes de Sketcher passent du rouge au bleu.
2.  La méthode habituelle de création de contraintes de dimension fonctionne de la même manière mais une cote pilotée bleue est ajoutée à la place.
3.  Pour remettre la barre d\'outils des contraintes de Sketcher en mode pilotant (rouge), appuyez à nouveau sur le bouton Basculer les contraintes pilotantes/pilotées.
4.  Pour transformer une contrainte pilotante en mode piloté, ou inversement, sélectionnez-la et appuyez sur le bouton Basculer les contraintes pilotantes/pilotées.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/fr
