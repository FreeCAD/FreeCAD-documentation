---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   Name/fr: Sketcher Contrainte point sur objet
   MenuLocation: Esquisse , Contraintes d'esquisse  , Contrainte point sur objet
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/fr, Sketcher_ConstrainCoincident/fr
---

# Sketcher ConstrainPointOnObject/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Sketcher Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md) fixe des points sur des arêtes ou des axes. Les lignes sont considérées comme infinies et les courbes ouvertes sont également virtuellement étendues.


{{Version/fr|1.0}}

: cet outil est remplacé par l\'outil [Sketcher Sketcher Contrainte coïncidence unifiée](Sketcher_ConstrainCoincidentUnified/fr.md) si l\'option **Unifier la contrainte de coïncidence et la contrainte de point sur objet** est sélectionnée dans les [préférences](Sketcher_Preferences/fr#Général.md).



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> [Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Contrainte point sur objet** du menu.
    -   Utilisez le raccourci clavier : **O**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez un seul point et une seule arête (dans n\'importe quel ordre).
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez un seul point et une seule arête (dans n\'importe quel ordre).
    -   Sélectionnez plusieurs points et une seule arête (idem).
    -   Sélectionnez un seul point et plusieurs arêtes (idem).
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Script

La contrainte peut être créée à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) à l\'aide de la commande suivante :


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`est un objet esquisse

-    `LineMoving`est le numéro qui désigne la ligne contenant le point qui doit être déplacé sur la ligne `LineFixed` (la ligne qui est fixe).

-    `PointOfLineMoving`est le numéro du sommet de la ligne `LineMoving` qui doit être déplacé sur `LineFixed`.

-    `LinedFixed`est le numéro de la ligne à apposer sur le point `PointOfLineMoving`.

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique comment identifier les nombres qui désignent des lignes et des points.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/fr
