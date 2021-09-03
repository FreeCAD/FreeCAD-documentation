---
- GuiCommand:/fr
   Name:Sketcher ConstrainPointOnObject
   Name/fr:Sketcher Contrainte point sur objet
   MenuLocation:Sketch → Contraintes d'esquisse  → Contrainte point sur objet
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**Maj** + **O**
   SeeAlso:[Sketcher Constraint Coincident](Sketcher_ConstrainCoincident/fr.md)
---

## Description

Appose un point sur un autre objet tel qu\'une ligne, un arc ou un axe d\'esquisse.

## Utilisation

1.  Sélectionnez le point que vous souhaitez apposer sur une ligne/un arc/etc. (**Résultat:** une fois sélectionné, le point deviendra vert).
2.  Sélectionnez la ligne que vous souhaitez apposer sur le point que vous venez de sélectionner (**Résultat:** une fois sélectionnée, la ligne devient verte).
3.  Lancez l\'outil **Contraindre le point sur l\'objet** par de plusieurs méthodes:
    -   Appuyez sur le bouton **<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Contrainte point sur objet](Sketcher_ConstrainPointOnObject.md)** dans la barre d\'outils.
    -   Utilisez le raccourci clavier **Maj** + **O**.
    -   Utilisez l\'entrée {{MenuCommand|Sketch → Contraintes d'esquisse → Contrainte point sur objet}}.

**Remarque :** l\'ordre dans lequel vous sélectionnez la ligne et le point n\'a pas d\'importance. Le point ira toujours à la ligne. En d\'autres termes, la ligne reste fixe.

## Script

La contrainte peut être créée à partir de macros et de la console python en utilisant la commande suivante :


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`est un objet d\'esquisse

-    `LineMoving`est le nombre qui désigne la ligne, qui contient le point qui doit être déplacé sur le `LineFixed` (La ligne qui est fixée)

-    `PointOfLineMoving`est le numéro du sommet de la ligne `LineMoving` qui doit être déplacé sur `LineFixed`.

-    `LinedFixed`est le numéro de la ligne à apposer sur le point `PointOfLineMoving`.

La page [Sketcher : Écrire des scripts](Sketcher_scripting/fr.md) explique comment identifier les nombres qui désignent des lignes et des points.





{{Sketcher Tools navi

}}  
