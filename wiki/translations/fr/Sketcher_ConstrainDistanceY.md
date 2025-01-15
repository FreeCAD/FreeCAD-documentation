---
 GuiCommand:
   Name: Sketcher ConstrainDistanceY
   Name/fr: Sketcher Contrainte de distance en Y
   MenuLocation: Esquisse , Géométries d'esquisse , Contrainte de distance verticale
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/fr, Sketcher_ConstrainDistance/fr
---

# Sketcher ConstrainDistanceY/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Sketcher Contrainte de distance en Y](Sketcher_ConstrainDistanceY/fr.md) fixe la distance verticale entre deux points ou les extrémités d\'une ligne. Si un seul point est présélectionné, la distance est relative à l\'origine de l\'esquisse.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes des dimensions** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Contrainte distance verticale** dans le menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> [Contrainte distance verticale](Sketcher_ConstrainDistanceY/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Contrainte distance verticale** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Contrainte distance verticale** du menu contextuel.

    -   Utilisez le raccourci clavier : **I**.
3.  Pour plus d\'informations, voir [Sketcher Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr#Mode_continu.md).



### Mode unique 

Voir [Sketcher Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr#Mode_unique.md)



## Script

Distance depuis l\'origine :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance entre deux sommets :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Étendue verticale de la ligne (l\'interface graphique permet de sélectionner l\'arête elle-même, mais ce n\'est qu\'un raccourci pour utiliser les deux extrémités de la même ligne):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` et `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/fr
