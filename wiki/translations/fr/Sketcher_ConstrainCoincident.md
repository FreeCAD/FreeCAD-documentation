---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   Name/fr: Sketcher Contrainte de coïncidence
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de coïncidence
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **C**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/fr, Sketcher_ConstrainPointOnObject/fr
---

# Sketcher ConstrainCoincident/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) crée une contrainte de coïncidence entre des points, ou ({{Version/fr|0.21}}) une contrainte concentrique entre des cercles, des arcs et/ou des ellipses (en faisant coïncider leurs centres).


{{Version/fr|1.0}}

: cet outil est remplacé par l\'outil [Sketcher Contrainte de coïncidence unifiée](Sketcher_ConstrainCoincidentUnified/fr.md) si l\'option **Unifier la contrainte de coïncidence et la contrainte de point sur objet** est sélectionnée dans les [ préférences](Sketcher_Preferences/fr#Général.md).



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainCoincident.svg" width=16px> [Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainCoincident.svg" width=16px> Contrainte de coïncidence** du menu.
    -   Utilisez le raccourci clavier : **C**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez deux points.
    -   Sélectionnez deux bords de cercles, d\'arcs, d\'ellipses ou d\'arcs d\'ellipses.
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux points ou plus.
    -   Sélectionnez deux ou plusieurs bords de cercles, d\'arcs, d\'ellipses ou d\'arcs d\'ellipses.
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Remarques

-    {{Version/fr|1.0}}: les points avec des contraintes coïncidentes sont marqués avec la [couleur](Sketcher_Preferences/fr#Affichage.md) des **symboles de contrainte**.



## Script

La contrainte peut être créée à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) à l\'aide de la commande suivante :


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

où :

-    `Sketch`est un objet d\'esquisse

-    `LineFixed`est le numéro de la ligne qui ne bougera pas en appliquant la contrainte

-    `PointOfLineFixed`indique quel sommet de `LineFixed` doit remplir la contrainte

-    `LineMoving`est le numéro de la ligne, qui se déplacera en appliquant la contrainte

-    `PointOfLineMoving`indique quel sommet de `LineMoving` doit remplir la contrainte

Comme les noms `LineFixed` et `LineMoving` l\'indiquent, si les deux sommets contraints sont libres de se déplacer dans n\'importe quelle direction, le premier (le premier à être sélectionné dans l\'interface graphique) restera fixe et l\'autre on bougera. En présence de contraintes existantes, cependant, les deux bords peuvent bouger.

La page [Sketcher : Écrire un script](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `LineFixed`, `PointOfLineFixed`, `LineMoving` et `PointOfLineMoving`, et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/fr
