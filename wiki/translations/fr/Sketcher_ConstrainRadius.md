---
 GuiCommand:
   Name: Sketcher ConstrainRadius
   Name/fr: Sketcher Contrainte rayon
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de rayon
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **R**
   SeeAlso: Sketcher_ConstrainRadiam/fr, Sketcher_ConstrainDiameter/fr
---

# Sketcher ConstrainRadius/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> [Sketcher Contrainte de rayon](Sketcher_ConstrainRadius/fr.md) fixe le rayon des cercles, des arcs et des [cercles des poids des B-splines](Sketcher_CreateBSpline/fr#Remarques.md).

![](images/Sketcher_ConstrainRadius_example.png )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes de dimension** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez la **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> Contrainte de rayon** dans le menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> [Contrainte de rayon](Sketcher_ConstrainRadius/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes de l'esquisse → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Contrainte de rayon** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Contrainte de rayon** du menu contextuel.

    -   Utilisez le raccourci clavier : **K** puis **R**.
3.  Pour plus d\'informations, voir [Sketcher Contrainte auto rayon/diamètre](Sketcher_ConstrainRadiam/fr#Mode_continu.md).



### Mode unique 

Voir [Sketcher Contrainte auto rayon/diamètre](Sketcher_ConstrainRadiam/fr#Mode_unique.md).



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `ArcOrCircle` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/fr
