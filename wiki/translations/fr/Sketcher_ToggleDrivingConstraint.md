---
- GuiCommand   */fr
   Name   *Sketcher ToggleDrivingConstraint
   Name/fr   *Sketcher Basculer les contraintes pilotes
   MenuLocation   *Sketch → Contraintes d'esquisse → Basculer la contrainte entre pilotante/référence
   Workbenches   *[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut   ***K** **X**
   Version   *0.16
   SeeAlso   *[Sketcher Basculer en géométrie de construction](Sketcher_ToggleConstruction/fr.md)
---

# Sketcher ToggleDrivingConstraint/fr

## Description

L\'icône **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width   *16px"> [Basculer entre contrainte pilotante/référence](Sketcher_ToggleDrivingConstraint/fr.md)** met les contraintes dimensionnelles (Verrou, Distance horizontale/verticale, Longueur, Rayon et Angle) en mode référence et inversement. Les icônes de la barre d\'outils deviennent bleues et, plutôt que des contraintes dimensionnelles, des cotes de référence sont créées. Les cotes de référence ne contraignent pas l\'esquisse. Il peut être utile de créer des cotes de référence dans une esquisse pour vérifier les mesures. lorsqu\'elles reçoivent un nom, elles peuvent également être utilisées pour définir des contraintes dans une autre esquisse via [expressions](Expressions/fr.md).

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) 
*La barre d'outils Contrainte de Sketcher avec les contraintes dimensionnelles en mode cote de référence (bleu).*

![](images/Sketcher_ToggleConstraint_example.png ) 
*Une contrainte de distance horizontale (50 mm), une contrainte verticale (30 mm) et une contrainte d'angle (75°) ont été définies pour définir le profil; une cote de référence a été ajoutée sur le segment de ligne incliné pour connaître sa longueur (31,0583 mm). *

## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width   *16px"> [Basculer la contrainte entre pilotante/référence](Sketcher_ToggleDrivingConstraint/fr.md)**. Les icônes de contraintes dimensionnelles de la barre d'outils Contraintes Sketcher passent du rouge au bleu.
2.  La méthode habituelle de création de contraintes dimensionnelles fonctionne de la même manière, mais une dimension de référence bleue est ajoutée à la place.
3.  Pour remettre la barre d\'outils Contraintes d\'esquisse en mode contrainte (rouge), appuyez à nouveau sur le bouton Basculer la contrainte.
4.  Pour transformer une contrainte dimensionnelle en cote de référence, ou inversement, sélectionnez-la et appuyez sur le bouton Basculer la contrainte.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/fr
