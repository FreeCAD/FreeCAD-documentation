---
- GuiCommand   */fr
   Name   *Sketcher ConstrainPointOnObject
   Name/fr   *Sketcher Contrainte point sur objet
   MenuLocation   *Esquisse → Contraintes d'esquisse  → Contrainte point sur objet
   Workbenches   *[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut   ***O**
   SeeAlso   *[Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md)
---

# Sketcher ConstrainPointOnObject/fr

## Description

Appose un point sur un autre objet tel qu\'une ligne, un arc ou un axe d\'esquisse.

## Utilisation

1.  Sélectionnez un point et un bord dans n\'importe quel ordre.
2.  Il existe plusieurs façons de lancer cette commande    *
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width   *16px"> [Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md)** dans la barre d\'outils.
    -   Utilisez le raccourci clavier **O**.
    -   Utilisez l\'entrée **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainPointOnObject.svg style="width   *16px"> Contrainte point sur objet**.

## Script

La contrainte peut être créée à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) à l\'aide de la commande suivante   *


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`est un objet esquisse

-    `LineMoving`est le numéro qui désigne la ligne contenant le point qui doit être déplacé sur la ligne `LineFixed` (la ligne qui est fixe).

-    `PointOfLineMoving`est le numéro du sommet de la ligne `LineMoving` qui doit être déplacé sur `LineFixed`.

-    `LinedFixed`est le numéro de la ligne à apposer sur le point `PointOfLineMoving`.

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique comment identifier les nombres qui désignent des lignes et des points.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/fr
