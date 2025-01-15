---
 GuiCommand:
   Name: Sketcher ConstrainDistanceX
   Name/fr: Sketcher Contrainte de distance en X
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de distance horizontale
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **L**
   SeeAlso: Sketcher_ConstrainDistance/fr, Sketcher_ConstrainDistanceY/fr
---

# Sketcher ConstrainDistanceX/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Sketcher Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr.md) fixe la distance horizontale entre deux points ou les extrémités d\'une ligne. Si un seul point est présélectionné, la distance est relative à l\'origine de l\'esquisse.

![](images/Constraint_H_Distance.png )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes des dimensions** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Contrainte distance horizontale** dans le menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> [Contrainte distance horizontale](Sketcher_ConstrainDistanceX/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Contrainte distance horizontale** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Contrainte distance horizontale** du menu contextuel.

    -   Utilisez le raccourci clavier : **L**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux points (dont l\'un peut être l\'origine).
    -   Sélectionnez une seule ligne.
5.  Si une [contrainte pilotante de dimension](Sketcher_ToggleDrivingConstraint/fr.md) est créée, en fonction des [préférences](Sketcher_Preferences/fr#Affichage.md), une fenêtre de dialogue s\'ouvre pour [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
6.  Une contrainte est ajoutée.
7.  Il est possible de continuer à créer des contraintes.
8.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez un ou deux points.
    -   Sélectionnez une seule ligne.
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  Vous pouvez [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
4.  Une contrainte est ajoutée.



## Script

Distance depuis l\'origine :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance entre deux sommets :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Étendue horizontale de la ligne (l\'interface graphique permet de sélectionner l\'arête elle-même, mais ce n\'est qu\'un raccourci pour utiliser les deux extrémités de la même ligne):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` et `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/fr
