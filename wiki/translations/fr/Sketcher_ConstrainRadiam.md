---
 GuiCommand:
   Name: Sketcher ConstrainRadiam
   Name/fr: Sketcher Contrainte auto rayon/diamètre
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte automatique du rayon/diamètre
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **S**
   Version: 0.20
   SeeAlso: Sketcher_ConstrainRadius/fr, Sketcher_ConstrainDiameter/fr
---

# Sketcher ConstrainRadiam/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Sketcher Contrainte auto rayon/diamètre](Sketcher_ConstrainRadiam/fr.md) fixe le rayon des arcs et des [cercles des poids des B-splines](Sketcher_CreateBSpline/fr#Remarques.md), ainsi que le diamètre des cercles.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes de dimension** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez la **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Contrainte automatique du rayon/diamètre** dans le menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> [Contrainte automatique du rayon/diamètre](Sketcher_ConstrainRadiam/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes de l'esquisse → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Contrainte automatique du rayon/diamètre** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Contrainte automatique du rayon/diamètre** du menu contextuel.

    -   Utilisez le raccourci clavier : **K** puis **S**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Effectuez l\'une des opérations suivantes :
    -   Sélectionner le bord d\'un cercle ou d\'un arc.
    -   Sélectionnez le bord d\'un cercle d\'un poids d\'une B-spline.
5.  Si une [contrainte pilotante de dimension](Sketcher_ToggleDrivingConstraint/fr.md) est créée, en fonction des [préférences](https://wiki.freecad.org/Sketcher_Preferences/fr#Affichage.md), une fenêtre de dialogue s\'ouvre pour [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
6.  Une contrainte est ajoutée.
7.  Il est possible de continuer à créer des contraintes.
8.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou lancez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez le bord d\'un ou plusieurs cercles ou arcs.
    -   Sélectionnez le bord d\'un ou de plusieurs cercles de poids B-spline.
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  Il est possible de [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
4.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées, voir [Remarques](##Remarques.md).



## Remarques

-   Si des [contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md) sont créées et que plusieurs éléments qui ne sont pas des [géométries externes](Sketcher_External/fr.md) ont été présélectionnés, seul le premier d\'entre eux reçoit une contrainte de dimension, tandis qu\'entre le premier et les autres, des [contraintes d\'égalité](Sketcher_ConstrainEqual/fr.md) sont appliquées.



## Script


```python
Sketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))
Sketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('246.0 mm')))
```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `ArcOrCircle` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/fr
