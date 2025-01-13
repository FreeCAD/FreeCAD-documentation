---
 GuiCommand:
   Name: Sketcher ConstrainDistance
   Name/fr: Sketcher Contrainte de distance
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de distance
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **D**
   SeeAlso: Sketcher_ConstrainDistanceX/fr, Sketcher_ConstrainDistanceY/fr
---

# Sketcher ConstrainDistance/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Sketcher Contrainte de distance](Sketcher_ConstrainDistance/fr.md) fixe la longueur d\'une ligne, la distance entre deux points, la distance perpendiculaire entre un point et une ligne, ou {{Version/fr|0.21}}, la distance entre les bords de deux cercles ou arcs, ou entre le bord d\'un cercle ou d\'un arc et une ligne, ou {{Version/fr|1.0}}, la longueur d\'un arc.

![](images/Sketcher_ConstrainDistance_example.png )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes des dimensions** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> Contrainte de distance** dans le menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> [Contrainte de distance](Sketcher_ConstrainDistance/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Contrainte de distance** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Contrainte de distance** du menu contextuel.

    -   Utilisez le raccourci clavier **K** puis **D**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez une seule ligne.
    -   Sélectionnez deux points.
    -   Sélectionnez un point et une ligne (dans cet ordre).
5.  Si une [contrainte pilotante de dimension](Sketcher_ToggleDrivingConstraint/fr.md) est créée, en fonction des [préférences](Sketcher_Preferences/fr#Affichage.md), une fenêtre de dialogue s\'ouvre pour [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
6.  Une contrainte est ajoutée.
7.  Vous pouvez éventuellement continuer à créer des contraintes.
8.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez une seule ligne.

    -   Sélectionnez deux points.

    -   Sélectionnez un point et une ligne (dans n\'importe quel ordre).

    -   Sélectionnez les bords de deux cercles ou arcs.

    -   Sélectionnez le bord d\'un cercle ou d\'un arc et une ligne (idem).

    -   
        {{Version/fr|1.0}}
        
        : sélectionnez le bord d\'un seul arc.
2.  Lancer l\'outil comme expliqué ci-dessus.
3.  Vous pouvez [modifier la valeur de la contrainte](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
4.  Une contrainte est ajoutée.



## Remarques

-   Le cas échéant envisagez d\'utiliser de préférence les fonctions **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Sketcher Contrainte distance en X](Sketcher_ConstrainDistanceX/fr.md)** ou **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Sketcher Contrainte distance en Y](Sketcher_ConstrainDistanceY/fr.md)**. Elles sont plus efficaces.



## Script

Distance depuis l\'origine :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance entre deux sommets :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Longueur de ligne (l\'interface graphique permet de sélectionner l\'arête elle-même, mais ce n\'est qu\'un raccourci pour utiliser les deux extrémités d\'une même ligne) :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distance du point (`Edge, PointOfEdge`) au point perpendiculaire sur la ligne (`Line`) :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Distance entre les bords de deux cercles :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Ligne`, `Cercle1` et `Cercle2`, et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/fr
