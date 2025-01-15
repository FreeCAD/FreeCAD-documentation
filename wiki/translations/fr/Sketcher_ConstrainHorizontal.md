---
 GuiCommand:
   Name: Sketcher ConstrainHorizontal
   Name/fr: Sketcher_Contrainte horizontale
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte horizontale
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainHorVer/fr, Sketcher_ConstrainVertical/fr
---

# Sketcher ConstrainHorizontal/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Sketcher Contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md) contraint les lignes ou les paires de points à être horizontales (parallèles à l\'axe horizontal de l\'esquisse).


{{Version/fr|1.0}}

: dans la plupart des cas, il est conseillé d\'utiliser l\'outil combiné [Sketcher Contrainte horizontale/verticale](Sketcher_ConstrainHorVer/fr.md) à la place.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) de l\'**outil automatique de contrainte horizontale/verticale** est sélectionnée (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_ConstrainHorVer.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Contrainte horizontale** dans le menu déroulant.

    -   Si cette préférence n\'est pas sélectionnée (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> [Contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Contrainte horizontale** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Contrainte horizontale** du menu contextuel.

    -   Utilisez le raccourci clavier : **H**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux points.
    -   Sélectionnez une seule ligne.
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux points ou plus.
    -   Sélectionnez une ou plusieurs lignes. Les points peuvent être inclus dans la sélection, mais ils seront ignorés.
2.  Lancer l\'outil comme expliqué ci-dessus, ou avec l\'option supplémentaire suivante :
    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Contrainte horizontale** dans le menu contextuel.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/fr
