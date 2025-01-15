---
 GuiCommand:
   Name: Sketcher ConstrainDiameter
   Name/fr: Sketcher Contrainte diamètre
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de diamètre
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **O**
   Version: 0.18
   SeeAlso: Sketcher_ConstrainRadiam/fr, Sketcher_ConstrainRadius/fr
---

# Sketcher ConstrainDiameter/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;"> [Sketcher Contrainte diamètre](Sketcher_ConstrainDiameter/fr.md) fixe le diamètre des cercles et des arcs. Il ne peut pas être utilisé pour des [cercles des poids des B-splines](Sketcher_CreateBSpline/fr#Remarques.md).



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences#General.md) **Contraintes de dimensionnement** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainDiameter.svg" width=16px> Contrainte de diamètre** dans le menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur **<img src="images/Sketcher_ConstrainDiameter.svg" width=16px> [Contrainte de diamètre](Sketcher_ConstrainDiameter/fr.md)
**

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainDiameter.svg" width=16px> Contrainte de diamètre** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainDiameter.svg" width=16px> Contrainte de diamètre** du menu contextuel.

    -   Utilisez le raccourci clavier : **K** puis **O**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez le bord d\'un cercle ou d\'un arc.
5.  Si une [contrainte pilotante de dimension](Sketcher_ToggleDrivingConstraint/fr.md) est créée, en fonction des [préférences](Sketcher_Preferences/fr#Affichage.md), une fenêtre de dialogue s\'ouvre pour [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
6.  Une contrainte est ajoutée.
7.  Vous pouvez continuer à créer des contraintes.
8.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Sélectionnez le bord d\'un ou de plusieurs cercles ou arcs.
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  Vous pouvez [modifier la valeur de la contrainte](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
4.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées, voir [Remarques](##Remarques.md).



## Remarques

-   Si des [contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md) sont créées et que plusieurs éléments qui ne sont pas des [géométries externes](Sketcher_External/fr.md) ont été présélectionnés, seul le premier d\'entre eux reçoit une contrainte de dimension, tandis qu\'entre le premier et les autres, des [contraintes d\'égalité](Sketcher_ConstrainEqual/fr.md) sont appliquées.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `ArcOrCircle` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/fr
